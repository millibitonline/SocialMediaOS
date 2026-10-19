# Agent Repository Access

This records each agent's **current integration status**. It describes what each
connection can do today. It does not define what a role is allowed to do (that
is in `aios/agents/registry.yaml`). The status is mirrored in the root
`.aios.yaml` (`contributors[].repo_access`).

| Agent | Role | Access | Status / notes |
|-------|------|--------|----------------|
| ChatGPT | strategist | **read** | Read access confirmed. Creating a branch returned `403 - Resource not accessible by integration`. This is an **integration limitation, not an architectural one**. |
| Claude | creative-director | **write** (branches, PRs, issues, labels) | Working through the Claude GitHub App. Never merges or approves. |
| Antigravity | engineer | **not connected** | To be connected later. Needs an ADR and owner approval for scopes. |
| @millibitonline | human-owner | admin | Approves, merges, manages settings. |

## Working around missing write access (Phase 1)

Until ChatGPT's write access works:

1. ChatGPT produces its work (for example, the full text of `STRATEGY.md`, or an issue
   comment) and gives it to the owner or posts it as an issue comment.
2. Claude commits that work **unchanged in substance** on a branch named for the
   originating role (for example, `feature/travel-lava-strategy`), with these trailers:
   ```
   Proposed-by: chatgpt (strategist)
   Committed-by: claude (creative-director)
   Refs: #<issue>
   ```
3. The PR description states that the content originates from ChatGPT and that
   Claude only committed it. ChatGPT (via the owner) reviews the PR before the owner merges.
4. Claude may fix formatting, but it does not change another role's decisions. Any
   substantive suggestion goes in a review comment or a Decision change request.

## Rules
- **Never bypass permissions.** No borrowed tokens, no committing as another
  identity, no workarounds for the 403.
- Access changes (granting, widening, retrying with new scopes) are **resource
  allocation decisions for the human owner**. Phase 2 automation needs an ADR.
- Update this table and `.aios.yaml` `repo_access` in the same PR whenever access
  changes.
