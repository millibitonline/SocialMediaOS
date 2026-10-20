#!/usr/bin/env python3
"""Validate AIOS .aios.yaml files and inheritance rules.

Checks (see aios/governance/INHERITANCE.md and aios/schema/aios-config.md):
  1. Every layer file's parent chain resolves and ends at the Foundation.
  2. Each parent is exactly one layer above its child.
  3. Locked keys are never changed by a descendant.
  4. Any unlocked scalar that differs from its inherited value is declared
     under `overrides:` (with reason/approved_by/approval_ref) or `extends:`.
  5. Projects only use capabilities the Organization provides.

Usage:  python scripts/validate_aios.py [repo_root]
Exit code 0 = valid, 1 = errors found.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

LAYERS = ["foundation", "organization", "team", "project", "feature"]
FOUNDATION = "aios/.aios.yaml"
# Directories holding placeholder templates, not live layers.
SKIP_DIRS = ("templates/", "aios/templates/")
# Keys describing the layer itself; never inherited or compared.
IDENTITY_KEYS = {
    "aios_version", "layer", "id", "name", "parent", "description", "owners",
    "status", "owner_role", "locks", "extends", "overrides", "kind",
    # registries of children, specific to each layer
    "teams", "projects", "features", "contributors", "hierarchy", "documents",
}
OVERRIDE_FIELDS = ("key", "from", "to", "reason", "approved_by", "approval_ref")


def load(root: Path, rel: str) -> dict:
    with open(root / rel, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def flatten(data, prefix=""):
    """Yield (dotted_path, value) for every leaf (scalars and lists)."""
    if isinstance(data, dict):
        for key, value in data.items():
            if not prefix and key in IDENTITY_KEYS:
                continue
            path = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(value, dict) and value:
                yield from flatten(value, path)
            else:
                yield path, value


def get_path(data, path):
    node = data
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None, False
        node = node[part]
    return node, True


def set_path(data, path, value):
    parts = path.split(".")
    node = data
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = value


def is_locked(path, locks):
    return any(path == lock or path.startswith(lock + ".") for lock in locks)


class Validator:
    def __init__(self, root: Path):
        self.root = root
        self.errors: list[str] = []
        self.cache: dict[str, dict] = {}
        self.effective: dict[str, tuple[dict, list[str]]] = {}

    def err(self, rel, msg):
        self.errors.append(f"{rel}: {msg}")

    def doc(self, rel):
        if rel not in self.cache:
            self.cache[rel] = load(self.root, rel)
        return self.cache[rel]

    def chain(self, rel):
        """Return [foundation, ..., rel] or None if broken."""
        seen, out, cur = set(), [], rel
        while cur:
            if cur in seen:
                self.err(rel, f"parent cycle at {cur}")
                return None
            if not (self.root / cur).is_file():
                self.err(rel, f"parent not found: {cur}")
                return None
            seen.add(cur)
            out.append(cur)
            cur = self.doc(cur).get("parent")
        if out[-1] != FOUNDATION:
            self.err(rel, f"chain ends at {out[-1]}, not {FOUNDATION}")
            return None
        return list(reversed(out))

    def resolve(self, rel):
        """Effective (config, locks) for a layer file, validating along the way."""
        if rel in self.effective:
            return self.effective[rel]
        data = self.doc(rel)
        parent_rel = data.get("parent")
        if parent_rel is None:
            eff = {k: copy.deepcopy(v) for k, v in data.items() if k not in IDENTITY_KEYS}
            result = (eff, list(data.get("locks", [])))
            self.effective[rel] = result
            return result

        parent_eff, parent_locks = self.resolve(parent_rel)
        eff = copy.deepcopy(parent_eff)
        overrides = {o.get("key"): o for o in data.get("overrides") or [] if isinstance(o, dict)}
        extends = {e.get("key") for e in data.get("extends") or [] if isinstance(e, dict)}

        for key, o in overrides.items():
            missing = [f for f in OVERRIDE_FIELDS if not o.get(f) and o.get(f) != 0]
            if missing:
                self.err(rel, f"override '{key}' missing fields: {', '.join(missing)}")
            if is_locked(key, parent_locks):
                self.err(rel, f"override '{key}' targets a locked key")

        for path, value in flatten(data):
            inherited, exists = get_path(parent_eff, path)
            if not exists:
                set_path(eff, path, copy.deepcopy(value))
                continue
            if isinstance(inherited, list) and isinstance(value, list):
                merged = list(inherited) + [v for v in value if v not in inherited]
                set_path(eff, path, merged)
                continue
            if value == inherited:
                continue
            if is_locked(path, parent_locks):
                self.err(rel, f"changes locked key '{path}' ({inherited!r} -> {value!r})")
                continue
            if path in overrides:
                if overrides[path].get("from") != inherited:
                    self.err(rel, f"override '{path}' declares from={overrides[path].get('from')!r} "
                                  f"but inherited value is {inherited!r}")
            elif path not in extends:
                self.err(rel, f"silent override of '{path}' ({inherited!r} -> {value!r}); "
                              "declare it under overrides: or extends:")
            set_path(eff, path, copy.deepcopy(value))

        locks = parent_locks + [l for l in data.get("locks", []) if l not in parent_locks]
        result = (eff, locks)
        self.effective[rel] = result
        return result

    def run(self):
        files = sorted(
            p.relative_to(self.root).as_posix()
            for p in self.root.rglob(".aios.yaml")
            if ".git/" not in p.as_posix()
        )
        files = [f for f in files if not f.startswith(SKIP_DIRS)]
        if FOUNDATION not in files:
            self.err(FOUNDATION, "Foundation config missing")
            return

        org_rel = ".aios.yaml"
        provided = set()
        if (self.root / org_rel).is_file():
            for cap in (self.doc(org_rel).get("capabilities") or {}).get("provides", []):
                provided.add(cap.get("id"))
                if not (self.root / cap.get("path", "") / "CAPABILITY.md").is_file():
                    self.err(org_rel, f"capability '{cap.get('id')}' has no CAPABILITY.md")

        for rel in files:
            data = self.doc(rel)
            if data.get("kind") == "capability":
                if data.get("parent") != org_rel:
                    self.err(rel, "capability parent must be the Organization (.aios.yaml)")
                if data.get("id") not in provided:
                    self.err(rel, f"capability '{data.get('id')}' not listed in organization provides")
                continue

            layer = data.get("layer")
            for key in ("layer", "id", "name"):
                if not data.get(key):
                    self.err(rel, f"missing required key '{key}'")
            if layer not in LAYERS:
                self.err(rel, f"unknown layer '{layer}'")
                continue
            if layer != "foundation" and not data.get("parent"):
                self.err(rel, "missing 'parent'")
                continue

            chain = self.chain(rel)
            if chain is None:
                continue
            for parent_rel, child_rel in zip(chain, chain[1:]):
                pl, cl = self.doc(parent_rel).get("layer"), self.doc(child_rel).get("layer")
                if pl in LAYERS and cl in LAYERS and LAYERS.index(cl) - LAYERS.index(pl) != 1:
                    self.err(child_rel, f"layer '{cl}' cannot have parent layer '{pl}'")
            self.resolve(rel)

            if layer == "project":
                uses = (data.get("capabilities") or {}).get("uses", [])
                for cap in uses:
                    if cap not in provided:
                        self.err(rel, f"uses unknown capability '{cap}'")

        self.check_contributors(org_rel)
        self.check_role_extensions(org_rel)
        self.check_foundation_purity(org_rel)
        self.check_handoff_form()
        print(f"Checked {len(files)} .aios.yaml file(s).")

    def check_contributors(self, org_rel):
        """Every contributor must be bound to a role defined in the registry."""
        if not (self.root / org_rel).is_file():
            return
        foundation = self.doc(FOUNDATION)
        registry_rel = (foundation.get("agents") or {}).get("registry")
        if not registry_rel or not (self.root / registry_rel).is_file():
            self.err(FOUNDATION, "agents.registry missing or not found")
            return
        roles = set((load(self.root, registry_rel).get("roles") or {}).keys())
        for c in self.doc(org_rel).get("contributors") or []:
            if c.get("role") not in roles:
                self.err(org_rel, f"contributor '{c.get('id')}' bound to unknown role '{c.get('role')}'")

    def check_role_extensions(self, org_rel):
        """Organization role extensions may only append to roles that exist."""
        if not (self.root / org_rel).is_file():
            return
        registry_rel = (self.doc(FOUNDATION).get("agents") or {}).get("registry")
        if not registry_rel or not (self.root / registry_rel).is_file():
            return
        roles = set((load(self.root, registry_rel).get("roles") or {}).keys())
        for role, ext in (self.doc(org_rel).get("role_extensions") or {}).items():
            if role not in roles:
                self.err(org_rel, f"role_extensions names unknown role '{role}'")
                continue
            for key, value in (ext or {}).items():
                if not isinstance(value, list):
                    self.err(org_rel, f"role_extensions.{role}.{key} must be a list (append-only)")

    def check_foundation_purity(self, org_rel):
        """Operating Principle 7: no implementation-specific names in aios/."""
        if not (self.root / org_rel).is_file():
            return
        terms = [t.lower() for t in self.doc(org_rel).get("foundation_forbidden_terms") or []]
        if not terms:
            return
        for path in sorted((self.root / "aios").rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(self.root).as_posix()
            for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                low = line.lower()
                for term in terms:
                    if term in low:
                        self.err(rel, f"line {lineno}: Foundation must not reference '{term}'")

    def check_handoff_form(self):
        """The hand-off issue form must require every Foundation hand-off field."""
        required = (self.doc(FOUNDATION).get("coordination") or {}).get("handoff_required_fields") or []
        if not required:
            return
        form_rel = ".github/ISSUE_TEMPLATE/handoff.yml"
        if not (self.root / form_rel).is_file():
            self.err(form_rel, "hand-off issue form missing")
            return
        body = load(self.root, form_rel).get("body") or []
        fields = {
            b.get("id"): (b.get("validations") or {}).get("required", False)
            for b in body if isinstance(b, dict) and b.get("id")
        }
        for f in required:
            if f not in fields:
                self.err(form_rel, f"missing required hand-off field '{f}'")
            elif not fields[f]:
                self.err(form_rel, f"hand-off field '{f}' must be marked required")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    v = Validator(root)
    v.run()
    if v.errors:
        print("\nAIOS validation FAILED:")
        for e in v.errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    print("AIOS validation passed ✓")


if __name__ == "__main__":
    main()
