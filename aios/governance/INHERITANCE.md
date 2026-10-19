# AIOS Inheritance Rules

**Layer:** Foundation · **Status:** Locked

AIOS resolves configuration and rules by walking the hierarchy from the top down:

```
Foundation → Organization → Team → Project → Feature → Task → Contributor
```

Each layer is declared by an `.aios.yaml` file. A layer's **effective
configuration** is the merge of every ancestor's configuration, in order, with its
own applied last — subject to the rules below.

## 1. Locating parents

Every `.aios.yaml` (except the Foundation's) declares `parent:` as a path, relative
to the repository root, to its parent's `.aios.yaml`. Parent chains must be acyclic
and must terminate at the Foundation (`aios/.aios.yaml`).

| Layer        | Lives at                                          | Declared by          |
|--------------|---------------------------------------------------|----------------------|
| Foundation   | `aios/`                                           | `aios/.aios.yaml`    |
| Organization | repository root                                   | `/.aios.yaml`        |
| Team         | `organization/teams/<team>/`                      | `.aios.yaml`         |
| Project      | `projects/<project>/`                             | `.aios.yaml`         |
| Feature      | `projects/<project>/features/<feature>/`          | `.aios.yaml`         |
| Task         | tracked in `FEATURE.md` / GitHub Issues           | (no file required)   |
| Contributor  | `aios/agents/registry.yaml` + org `contributors:` | registry entry       |

Shared **capabilities** (`organization/capabilities/<name>/`) are not a hierarchy
layer. They are services owned by the Organization that projects *consume* via
`capabilities.uses`. A capability's rules are inherited by any project that uses it.

## 2. Merge semantics

| Value type            | Default behavior when a child sets it                    |
|-----------------------|----------------------------------------------------------|
| Scalar (string/number/bool) | Child value replaces parent value **only if the key is not locked** |
| List                  | **Append-only.** Child items are added to the parent's list |
| Map                   | Merged recursively, key by key, using these same rules   |

## 3. Locked keys

A layer may lock any key it defines by listing its dotted path under `locks:`.

```yaml
locks:
  - governance.human_approval.publishing
  - governance.source_of_truth
```

- A locked key cannot be changed by any descendant, with or without a declared
  override. Changing it requires a PR to the layer that set the lock.
- Locks themselves are inherited and append-only — a child may add locks, never
  remove them.

## 4. Extending (always allowed)

A child may, without approval:
- Add new keys that no ancestor defines.
- Append to inherited lists (more reviewers, more checks, more banned topics).
- **Tighten** a rule — e.g. raise a required approval count, shorten a deadline,
  add a required label. Tightening is expressed by setting a stricter value **and**
  listing it under `extends:` with a one-line reason so reviewers can see it.

## 5. Overriding (allowed only when declared)

Loosening or changing an inherited, unlocked value is an **override**. Overrides
must be declared in the child's `.aios.yaml`:

```yaml
overrides:
  - key: content.cadence.posts_per_week
    from: 5
    to: 3
    reason: "Long-form channel; quality over volume during launch quarter."
    approved_by: "@seth"          # GitHub handle of the approving human
    approval_ref: "PR #12"        # where the approval was recorded
```

A value that differs from its inherited value **without** a matching `overrides:`
entry is a **silent override** and is a validation error. `scripts/validate_aios.py`
enforces this, and CI runs it on every pull request.

## 6. Precedence summary

1. Locks always win.
2. Declared, approved overrides apply next.
3. Otherwise the nearest layer that sets a value wins for scalars; lists accumulate.

## 7. Contributors

Contributors (humans and agents) don't carry their own `.aios.yaml`. Their
permissions are the **intersection** of:
- their role definition in `aios/agents/registry.yaml` (and any organization
  extension of it), and
- the effective configuration of the layer they are working in.

A contributor can never gain a permission by moving down the hierarchy.
