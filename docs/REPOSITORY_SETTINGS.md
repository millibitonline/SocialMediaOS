# Recommended Repository Settings

These are **recommendations for the human owner**. Agents must not change
repository protection settings. Current state (2026-10-19): `main` is **not
protected**.

## Branch protection for `main` (Settings → Branches → Add rule, or a ruleset)

| Setting | Recommended | Why |
|---------|-------------|-----|
| Require a pull request before merging | **On** | Principle 3: changes move through PRs |
| Required approvals | **1** | Human approval (agents can't approve) |
| Require review from Code Owners | **On** | `CODEOWNERS` routes everything to the owner |
| Dismiss stale approvals when new commits are pushed | **On** | Approvals are tied to an exact version (APPROVALS.md) |
| Require approval of the most recent push | **On** | Stops an agent's push landing after approval |
| Require status checks to pass | **On**, check: **`validate`** (workflow "Validate AIOS") | Enforces inheritance, locks, and hand-off rules |
| Require branches to be up to date before merging | **On** | Validator runs against the real merge result |
| Require conversation resolution | **On** | Review threads must be closed out |
| Require linear history | Optional | Cleaner history; squash-merge works well with it |
| Allow force pushes / deletions | **Off** | Protects the source of truth |
| Restrict who can push to `main` | Owner only (or no one; PRs only) | Agents never push to `main` |
| Do not allow bypassing the above | **On** (include administrators) | The owner also merges through PRs |

## Other settings
- **Merge button:** allow squash merging and set the default message to "PR title
  and description" so attribution trailers survive.
- **Auto-merge:** off, so a human explicitly merges.
- **Actions → General:** workflow permissions *read repository contents* by default.
- **Issues:** on. Blank issues are disabled by `.github/ISSUE_TEMPLATE/config.yml`.
- **Labels:** created from `.github/labels.yml` (done 2026-10-19).
