# Agent Repository Access

This records each agent's **current integration status**. It describes what each
connection can do today. It does not define what a role is allowed to do (that
is in `aios/agents/registry.yaml`). The status is mirrored in the root
`.aios.yaml` (`contributors[].repo_access`).

| Agent | Role | Access | Status / notes |
|-------|------|--------|----------------|
| ChatGPT | strategist | **write, via the owner's account** | Working since 2026-10-19 (first commit `b468c13`). ChatGPT's GitHub connector authenticates as **@millibitonline**, so its commits show the owner as author. The earlier `403 - Resource not accessible by integration` is resolved. See *Shared-identity caveats* below. |
| Claude | creative-director | **write** (branches, PRs, issues, labels) | Working through the Claude GitHub App. Never merges or approves. |
| Antigravity | engineer | **not connected** | To be connected later. Needs an ADR and owner approval for scopes. |
| @millibitonline | human-owner | admin | Approves, merges, manages settings. |

## Shared-identity caveats (ChatGPT, current)

Because ChatGPT writes as @millibitonline:
- **Attribution lives in the content, not the author field.** ChatGPT commits must
  carry `Agent: chatgpt (strategist)` (or `Proposed-by: chatgpt (strategist)`) in
  the commit message, and authored files should name ChatGPT. Reviewers treat an
  owner-authored commit without that marker as the human owner's own.
- **It technically holds the owner's permissions** (admin, merge, approve). The
  rules still apply: agents never merge, approve, change settings, or approve
  gates. A PR review or merge from @millibitonline counts as a human approval only
  when the owner performs it personally.
- **Branch protection interaction:** GitHub won't let an account approve its own
  PR, and "Require approval of the most recent push" blocks approval by whoever
  pushed last. If ChatGPT pushes to a PR as @millibitonline, the owner may be unable
  to approve it under those settings. Options: give ChatGPT a dedicated GitHub
  identity (preferred, Phase 2 ADR), or have ChatGPT deliver changes that another
  agent commits.

## Proxy commits for agents without write access

When an agent has no write access:

1. The agent produces its work (for example, the full text of `STRATEGY.md`, or an issue
   comment) and gives it to the owner or posts it as an issue comment.
2. Claude commits that work **unchanged in substance** on a branch named for the
   originating role (for example, `feature/travel-lava-strategy`), with these trailers:
   ```
   Proposed-by: <agent> (<role>)
   Committed-by: claude (creative-director)
   Refs: #<issue>
   ```
3. The PR description states which agent the content came from and that
   Claude only committed it. The originating agent reviews the PR before the owner merges.
4. Claude may fix formatting, but it does not change another role's decisions. Any
   substantive suggestion goes in a review comment or a Decision change request.

## Rules
- **Never bypass permissions.** No borrowed tokens and no acting under another
  identity beyond what the owner explicitly connects (as with ChatGPT's connector
  today).
- Access changes (granting, widening, retrying with new scopes) are **resource
  allocation decisions for the human owner**. Phase 2 automation needs an ADR.
- Update this table and `.aios.yaml` `repo_access` in the same PR whenever access
  changes.
