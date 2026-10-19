# ADR-0002: GitHub as the agent coordination layer

- **Status:** proposed
- **Date:** 2026-10-19
- **Layer(s):** foundation (forge-neutral protocol), organization (GitHub binding)
- **Proposed by:** strategist (ChatGPT), written up by creative-director (Claude)
- **Decided by:** _pending: human owner_

## Context
Three agents (currently ChatGPT, Claude, Antigravity) and a human owner need to
share context, hand work to each other, and review each other's contributions.
Coordinating in chat leaves no shared record. ADR-0001 already makes the
repository the source of truth.

Agent access is currently uneven:
- **ChatGPT** can read the repository. Creating a branch returned
  `403 - Resource not accessible by integration`.
- **Claude** has write access.
- **Antigravity** is not connected yet.

No agent can automatically discover new work yet.

## Decision
1. GitHub is SocialMediaOS's coordination layer:
   - **issues** for tasks and hand-offs
   - **pull requests** for proposed changes
   - **Markdown** for strategy, architecture, and creative decisions
   - **ADRs** for significant decisions
   - **comments, commits, and reviews** for communication
2. The protocol is defined forge-neutrally in the Foundation
   (`aios/agents/HANDOFF_PROTOCOL.md`). GitHub is bound at the Organization layer
   (`coordination.platform: github`, locked).
3. Every hand-off has seven required fields: objective, context & references,
   deliverables, acceptance criteria, assigned role, status, and decisions requiring
   approval. These are locked at the Foundation and enforced by the issue form and CI.
4. Work is assigned to **roles**, not models. Bindings live only in the root
   `.aios.yaml` under `contributors:`.
5. Each decision has one owning role (`owns_decisions`). Other roles propose
   changes through a *Decision change request* and never edit it directly
   (`may_change_other_roles_decisions: false`, locked).
6. **Source of truth and communication system are separate concerns:**
   - **Phase 1 (manual, now):** the human owner starts agent sessions and relays
     between agents. An agent without write access hands its output to an agent
     with access, which commits it with attribution (see 7).
   - **Phase 2 (automated, later ADR):** per-agent GitHub identities, label sync,
     and work notification, once the engineer is connected.
7. **Proxy-commit attribution:** when one agent commits another's work, the
   commit message carries `Proposed-by: <agent> (<role>)` and `Committed-by: <agent>`
   trailers, and the PR description names the originating agent. Proxying never
   bypasses permissions. The proxy commits only what the originating agent produced
   and what the proxy's own role or the owner allows.
8. ChatGPT's 403 is recorded as a **current integration limitation**, not an
   architectural one (`docs/AGENT_ACCESS.md`).

## Alternatives considered
1. **Coordinate in chat; commit only final outputs.** Fastest to start, but
   decisions and hand-offs leave no record, and the owner becomes the only memory
   of who decided what. Rejected.
2. **A separate project-management tool (e.g. a task board outside the repo).** Good
   task UX, but it splits context away from the code and docs and adds another
   integration for every agent. Rejected for now.
3. **Wait to coordinate until every agent has write access.** Cleanest
   attribution, but it blocks progress on an integration problem. Rejected in
   favor of Phase 1 proxy commits with explicit attribution.
4. **Hard-code GitHub in the Foundation.** Simpler wording, but it breaks AIOS's
   platform independence. Rejected; the binding lives at Organization level.

## Consequences
- Every hand-off, decision, and approval can be traced from issue to commit to PR to merge.
- In Phase 1, the owner's relaying limits how fast work moves.
- Labels must exist (created from `.github/labels.yml`).
- Changing which agent fills a role is a one-line config edit.
- Proxy commits make the committing agent responsible for faithfully representing
  the originating agent's work.

## Ownership
- **Decision owner:** strategist (architecture). The protocol text is maintained by
  the creative-director (documentation) without changing its substance.
- **Implementing roles:** engineer (issue forms, CI checks, Phase 2 automation),
  creative-director (docs).

## Approval requirements
- This ADR requires the **human owner's** approval under `gate:architecture`.
- Moving to Phase 2, or giving any agent new repository permissions, requires a
  new ADR and the owner's approval (resource allocation). Connecting production
  systems also requires `gate:integration`.

## Follow-ups
- [x] Labels created from `.github/labels.yml` (2026-10-19).
- [ ] Owner decides whether to retry or repair ChatGPT's write access.
- [ ] Phase 2 ADR: agent identities, scopes, and work-discovery mechanism.
