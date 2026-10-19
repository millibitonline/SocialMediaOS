# ADR-0002: GitHub as the agent coordination layer

- **Status:** proposed
- **Date:** 2026-10-19
- **Layer(s):** foundation, organization
- **Proposed by:** strategist (ChatGPT), written up by creative-director (Claude)
- **Decided by:** _pending, human owner_

## Context
Three agents (currently ChatGPT, Claude, Antigravity) and a human owner need to
share context, hand work to each other, and review each other's contributions.
Chat-based coordination leaves no shared record. ADR-0001 already makes GitHub
the source of truth. Not every agent can write to the repository yet (ChatGPT's
write attempt was refused), and none can automatically discover new work.

## Decision
1. GitHub is the coordination layer: **issues** for tasks and hand-offs, **pull
   requests** for proposed changes, **Markdown** for strategy, architecture, and
   creative decisions, **ADRs** for significant decisions, and **comments,
   commits, and reviews** for communication.
2. Hand-offs follow `aios/agents/HANDOFF_PROTOCOL.md`. The required fields are
   objective, context & references, deliverables, acceptance criteria, assigned
   role, status, and decisions requiring approval. These fields are locked at
   the Foundation.
3. Work is assigned to **roles**, not models. Bindings live only in the root
   `.aios.yaml` `contributors:`.
4. Each decision has one owning role (`owns_decisions`). Other roles propose
   changes through a *Decision change request*. They never edit it directly
   (`may_change_other_roles_decisions: false`, locked).
5. We separate **source of truth** (works now) from **communication system**
   (needs permissions and discovery):
   - **Phase 1, manual:** the owner starts agent sessions and relays between
     agents. Agents without write access give their output to an agent with
     access or to the owner to commit, and the PR records the true author.
   - **Phase 2, automated:** decided in a future ADR once the engineer
     (Antigravity) is connected. It covers per-agent GitHub identities, label
     sync, and work notification.

## Consequences
- Every hand-off and decision can be traced.
- Phase 1 depends on the owner relaying between agents, so throughput is limited
  by the owner's attention.
- Issue forms enforce required fields. Labels must be created once from
  `.github/labels.yml`.
- Role changes are one-line config edits.

## Follow-ups
- [ ] Owner creates labels from `.github/labels.yml` (or approves an engineer automation for it).
- [ ] Decide how agents without write access are credited (`Co-Authored-By` trailer vs. PR body attribution).
- [ ] Phase 2 ADR: agent identities, scopes, and work discovery mechanism.
