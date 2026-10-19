# AIOS Governance

**Layer:** Foundation · **Status:** Locked

## Purpose
AIOS is a reusable, platform-independent operating model for organizations whose
work is done by a mix of humans and AI agents. This document defines how
decisions are made, recorded, and changed. Implementations (such as
SocialMediaOS) inherit it unchanged and may extend it.

## Roles

| Role            | Who                          | Authority |
|-----------------|------------------------------|-----------|
| **Owner**       | Designated human(s) per org  | Final say on Foundation/Organization changes, publishing, spending, and external commitments. |
| **Maintainer**  | Humans with merge rights     | Review and merge PRs within their layer. |
| **Agent**       | Registered AI contributors   | Propose changes via branches and PRs within their declared responsibilities. Agents never merge to `main` and never approve their own work. |
| **Reviewer**    | Human or agent, as configured | Review PRs. An agent review is advisory; it never satisfies a required human approval. |

## Decision records
- Significant decisions are captured as Architecture Decision Records (ADRs) in
  `docs/adr/`, using [../templates/ADR.md](../templates/ADR.md).
- An ADR is required for: adding/removing a hierarchy layer, changing a lock,
  changing agent responsibilities, adding a shared capability, or connecting any
  production integration.
- ADR status flows: `proposed → accepted | rejected → (superseded)`.

## Change control by layer

| Layer touched           | Minimum approval to merge                    |
|-------------------------|----------------------------------------------|
| Foundation (`aios/`)    | Owner + accepted ADR                          |
| Organization (root, `organization/`) | Owner                            |
| Team                    | Owner or team maintainer                      |
| Project                 | Project maintainer                            |
| Feature / Task          | Project maintainer                            |
| Content marked for publishing | Owner or designated human publisher — always human |

Layers may raise these minimums; they may not lower them (see
[INHERITANCE.md](INHERITANCE.md)).

## Approval gates
Gates are named checkpoints that require recorded human approval:

- `gate:architecture` — Foundation or Organization structure changes.
- `gate:publish` — any content leaving the repository for a public audience.
- `gate:spend` — any action that commits money.
- `gate:integration` — connecting a production system or credential.

Gate approval is recorded as a PR review from an authorized human, or as a signed-off
entry in the relevant `APPROVALS.md` / approval log. See [APPROVALS.md](APPROVALS.md).

## Amending governance
1. Open a branch `governance/<change>`.
2. Write or update an ADR.
3. Open a PR labeled `layer:foundation` (or the appropriate layer).
4. Obtain the approvals required above.
