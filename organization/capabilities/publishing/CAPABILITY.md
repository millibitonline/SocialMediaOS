# Capability: Publishing

**Lead role:** engineer (Antigravity) · **Status:** defined, **no production integrations**

## Contract
Moves **approved** content to **scheduled** and **published** — only with a
recorded human approval under `gate:publish`.

## Rules (inherited by every channel; locked)
1. Nothing is scheduled or published without an approval entry that matches the
   content file's current commit SHA ([APPROVALS.md](../../../aios/governance/APPROVALS.md)).
2. Agents re-check approval status immediately before any publish action.
3. Edits after approval invalidate the approval.
4. Account credentials are held by the human owner, never committed, never handled
   by agents until a secrets approach is decided by ADR.

## Current mode: manual
Until an integration ADR is accepted, publishing is manual:
1. Human owner approves the content PR.
2. Human owner posts on the platform.
3. Anyone moves the file to `content/published/` in a PR, adding `published_url`
   and `published_at` to front matter.

## Future (requires ADR + `gate:integration`)
- Scheduler adapter interface (one adapter per platform).
- Dry-run mode that renders the exact payload for human review.
- Audit log of every outbound call, committed to the repo.
