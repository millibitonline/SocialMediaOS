# `.aios.yaml` Reference

Every layer declares itself with an `.aios.yaml`. `scripts/validate_aios.py`
checks these files on every PR.

## Required keys (all layers)

| Key           | Type   | Notes |
|---------------|--------|-------|
| `aios_version`| string | Semver of the AIOS spec the file targets. Foundation only; others inherit. |
| `layer`       | enum   | `foundation`, `organization`, `team`, `project`, `feature` |
| `id`          | string | kebab-case, unique within its layer |
| `name`        | string | Human-readable |
| `parent`      | path   | Repo-relative path to parent `.aios.yaml`. Omitted only on Foundation. |

Parent `layer` must be the layer directly above (feature → project → team →
organization → foundation).

## Inheritance control keys

| Key         | Type | Meaning |
|-------------|------|---------|
| `locks`     | list of dotted paths | Keys descendants may not change. Append-only. |
| `extends`   | list of `{key, reason}` | Tightening of inherited values. Documented, no approval needed. |
| `overrides` | list of `{key, from, to, reason, approved_by, approval_ref}` | Declared loosening/change of an unlocked inherited value. Requires human approval. |

## Common optional keys

| Key            | Used by | Meaning |
|----------------|---------|---------|
| `owners`       | any     | GitHub handles accountable for the layer |
| `contributors` | organization | Binds concrete agents/humans to registry roles |
| `capabilities` | organization (`provides`), project (`uses`) | Shared services |
| `content`      | organization, project | Cadence, review, and pipeline settings |
| `channel`      | project | Channel identity: platforms, niche, handle placeholders |
| `status`       | project, feature | `planning`, `active`, `paused`, `archived` |

## Validation rules
1. Parent chain resolves and ends at `aios/.aios.yaml`.
2. Parent layer is exactly one level up.
3. No locked key differs from its inherited value.
4. Any unlocked scalar that differs from its inherited value has a matching
   `overrides:` or `extends:` entry.
5. Every `overrides:` entry has `reason`, `approved_by`, and `approval_ref`.
6. Every project's `capabilities.uses` names a capability the Organization provides.
