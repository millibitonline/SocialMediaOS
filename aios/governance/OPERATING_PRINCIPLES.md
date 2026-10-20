# AIOS Operating Principles

**Layer:** Foundation · **Status:** Locked (changes require a Foundation ADR)

These principles apply to every AIOS implementation, every organization, team,
project, feature, task, and contributor — human or agent.

## 1. The repository is the source of truth
- The organization's git repository (on the forge it binds at Organization level)
  is authoritative. If it is not in the repository, it is not decided.
- Chat transcripts, docs in other tools, and agent memory are *inputs*; they become
  binding only when committed and merged.
- Every merged change has an author, a reviewer, and a reason (the PR description).

## 2. Rules flow down
- The hierarchy is: **Foundation → Organization → Team → Project → Feature → Task → Contributor**.
- Each layer inherits everything above it.
- A layer may **extend** inherited rules (add, narrow, tighten).
- A layer may **not silently override** inherited rules. Any override must be
  declared, justified, and approved (see [INHERITANCE.md](INHERITANCE.md)).

## 3. Changes move through branches and pull requests
- No direct commits to `main`.
- One concern per branch. Branch names follow `<type>/<short-description>`
  (`setup/`, `feature/`, `content/`, `fix/`, `governance/`, `docs/`).
- Every PR states which layer(s) it touches. PRs touching Foundation or
  Organization governance require human owner approval.

## 4. Humans approve anything external-facing
- No agent publishes, posts, sends, spends, or signs on behalf of the organization
  without an explicit, recorded human approval.
- "Recorded" means: an approving PR review, or an approval entry committed to the
  repository. A chat message alone is not an approval.

## 5. Clear ownership, explicit hand-offs
- Every artifact has exactly one accountable owner (a role, not just a tool).
- Agents work within their declared responsibilities (see
  [../agents/AGENT_STANDARDS.md](../agents/AGENT_STANDARDS.md)). Work outside a
  role's scope is proposed, not performed.
- Hand-offs between agents happen through the repository (issues, PRs, files),
  never through hidden state.

## 6. Reversible by default
- Prefer changes that can be reverted with a single PR revert.
- Irreversible actions (deleting accounts, publishing, payments, external
  commitments) always require human approval, regardless of layer.

## 7. Platform independence at the Foundation
- The Foundation layer (`aios/`) never references a specific organization,
  channel, social platform, vendor, or model.
- Implementation-specific choices live at Organization level or below.

## 8. Transparency over cleverness
- Agents state assumptions, cite sources, and flag uncertainty.
- Generated content is labeled as such in its metadata until a human approves it.
