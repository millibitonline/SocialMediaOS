# SocialMediaOS

SocialMediaOS launches and operates social media channels with a small team of
AI agents and an accountable human owner. It is an implementation of **AIOS** —
a reusable, platform-independent operating system for human + AI organizations.

> **Status:** initial architecture. No production integrations. Nothing is
> published without human approval.

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ Foundation    aios/                    AIOS — reusable, locked │
├──────────────────────────────────────────────────────────────┤
│ Organization  .aios.yaml, organization/   SocialMediaOS        │
│   └ Capabilities (shared services): content-production,       │
│     publishing, analytics, financial-reporting                 │
├──────────────────────────────────────────────────────────────┤
│ Team          organization/teams/channels/                     │
├──────────────────────────────────────────────────────────────┤
│ Project       projects/<channel>/          e.g. travel-lava │
├──────────────────────────────────────────────────────────────┤
│ Feature       projects/<channel>/features/<feature>/           │
├──────────────────────────────────────────────────────────────┤
│ Task          rows in FEATURE.md / GitHub Issues               │
├──────────────────────────────────────────────────────────────┤
│ Contributor   ChatGPT · Claude · Antigravity · human owner     │
└──────────────────────────────────────────────────────────────┘
          rules flow down ▼   ·   overrides must be declared ▲
```

### Inheritance in one paragraph
Each layer declares itself in an `.aios.yaml` that points to its `parent:`. A
layer's effective rules are everything above it plus its own additions. Lists
append, maps merge, scalars replace — except **locked** keys, which nobody below
may change. Making a rule **stricter** is allowed and documented under
`extends:`. **Loosening or changing** an inherited value requires an `overrides:`
entry with a reason and a recorded human approval. Anything else is a *silent
override* and fails CI. Full rules: [aios/governance/INHERITANCE.md](aios/governance/INHERITANCE.md).

### Who does what

| Role | Currently bound to | Owns |
|------|--------------------|------|
| strategist | ChatGPT | Business strategy, research & competitive analysis, channel selection, monetization, architecture & evaluation |
| creative-director | Claude | Brand & creative direction, content strategy & development, documentation, implementation support |
| engineer | Antigravity | Automation, integrations, production pipelines, testing & deployment |
| human-owner | @millibitonline | Final decisions, approvals, resource allocation, merge authorization |

Roles are configurable: bindings live only in `.aios.yaml` → `contributors:`.
Agents propose via branches and PRs. Only humans approve gates and merge.
Instructions: [AGENTS.md](AGENTS.md) (all agents), [CLAUDE.md](CLAUDE.md) (Claude).

### How agents collaborate
GitHub is the coordination layer. **Issues** carry tasks and hand-offs,
**pull requests** carry proposed changes, **Markdown and ADRs** hold decisions,
and **comments, commits, and reviews** are the conversation. Each hand-off states
its objective, context, deliverables, acceptance criteria, assigned role, status,
and the decisions that need approval. Each decision has one owning role, and
nobody edits another role's decision. Coordination is manual for now: the owner
starts agent sessions and relays between agents. Automation comes later through
an ADR. Full model and worked example: [docs/OPERATING_MODEL.md](docs/OPERATING_MODEL.md).

## Operating model

1. **GitHub is the source of truth.** Not decided until merged.
2. **Branch → PR → human review → merge.** Branches: `setup/`, `feature/`,
   `content/`, `fix/`, `governance/`, `docs/`, `chore/`.
3. **Content pipeline:** `ideas → drafts → in-review → approved → (scheduled) → published`.
   Reaching `approved` and beyond requires a human approval tied to the exact commit.
4. **Publishing is manual** until an integration ADR is accepted and
   `gate:integration` is approved.
5. **Analytics** snapshots weekly, reviews monthly; **finance** ledgers monthly
   per channel — both manual entry for now.
6. **Decisions** that change structure are recorded as ADRs in [docs/adr/](docs/adr/).

## Repository layout

```
.aios.yaml                      Organization config (SocialMediaOS)
AGENTS.md · CLAUDE.md           Agent instructions
aios/                           Foundation (reusable AIOS)
  .aios.yaml                    Foundation config + locks
  governance/                   Principles, governance, inheritance, approvals
  agents/                       Agent standards + role registry
  schema/                       .aios.yaml reference
  templates/                    ADR, Feature templates
organization/
  ORGANIZATION.md               Org structure and rules
  capabilities/                 content-production, publishing, analytics, financial-reporting
  teams/channels/               Channels team + launch playbook
templates/channel/              Copy to start a new channel
projects/travel-lava/   First channel (planning)
projects/coffee-help/   Coffee.help channel (planning; affiliated with PolyCoffee)
docs/OPERATING_MODEL.md         How agents discover work, hand off, review, and trace work
docs/AGENT_ACCESS.md            Current per-agent repository access + proxy-commit rules
docs/REPOSITORY_SETTINGS.md     Recommended branch protection for main
docs/handoffs/drafts/           Hand-off issues prepared before they can be filed
docs/adr/                       Architecture decision records
scripts/validate_aios.py        Inheritance validator (runs in CI)
.github/                        CI, PR template, CODEOWNERS, issue templates
```

## Launching a new channel
Follow [organization/teams/channels/LAUNCH_PLAYBOOK.md](organization/teams/channels/LAUNCH_PLAYBOOK.md):
copy `templates/channel/` to `projects/<id>/`, register it in the Channels team
config, run the validator, and open a PR.

## Validating locally
```bash
pip install pyyaml
python scripts/validate_aios.py
```

## Reusing AIOS elsewhere
Copy `aios/` and `scripts/validate_aios.py` unchanged into a new repository, then
write a root `.aios.yaml` with `layer: organization` and `parent: aios/.aios.yaml`.
