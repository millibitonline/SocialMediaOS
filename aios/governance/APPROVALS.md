# AIOS Approval Standard

**Layer:** Foundation · **Status:** Locked

## What counts as an approval
An approval is valid only if **all** of the following are true:

1. It was given by a **human** listed as authorized for that gate in the effective
   configuration (`governance.approvers.<gate>`).
2. It is **recorded in the repository** — either as an approving GitHub PR review
   on the PR containing the exact artifact, or as an entry in an approval log
   committed to `main`.
3. It refers to a **specific version** of the artifact (a commit SHA or the PR's
   final head). Edits after approval invalidate it.

Agent reviews, chat messages, emoji reactions, and verbal approvals are not
approvals.

## Approval log entry format
Approval logs are append-only YAML files (e.g. `projects/<p>/content/approved/APPROVALS.yaml`).

```yaml
- gate: publish
  artifact: content/approved/2026-10-25-first-light.md
  commit: <sha>
  approved_by: "@github-handle"
  approved_at: "2026-10-24T18:00:00-07:00"
  scope: "Instagram + TikTok, scheduled 2026-10-25 09:00 PT"
  notes: ""
```

## Revocation
An approver may revoke an approval by appending an entry with `revoked: true`
referencing the original. Agents must re-check approval status immediately before
performing any gated action.
