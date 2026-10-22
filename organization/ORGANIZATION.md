# SocialMediaOS — Organization

SocialMediaOS is an implementation of [AIOS](../aios/README.md) that launches and
operates social media channels. It inherits every Foundation rule and adds
social-media-specific structure on top.

## Structure

```
Foundation   aios/                                   (inherited, unchanged)
Organization /.aios.yaml + organization/             SocialMediaOS
Team         organization/teams/channels/            owns all channel projects
Project      projects/<channel>/                     one per channel (e.g. travel-lava)
Feature      projects/<channel>/features/<feature>/  a deliverable (launch, a series, a campaign)
Task         rows in FEATURE.md or GitHub Issues     leaf work items
Contributor  ChatGPT · Claude · Antigravity · human owner
```

## Contributors and responsibilities

Roles are bound to agents in the root `.aios.yaml` (`contributors:`), so they
can be reassigned without touching anything else.

| AIOS role | Currently bound to | Owns | Never does |
|-----------|--------------------|------|------------|
| strategist | **ChatGPT** | Business strategy, research & competitive analysis, channel selection, monetization, architecture & evaluation | Write final content, change automation, merge |
| creative-director | **Claude** | Brand & creative direction, content strategy & development, documentation, implementation support | Change other roles' decisions, publish, merge |
| engineer | **Antigravity** | Automation, integrations, production pipelines, testing & deployment | Connect production systems without `gate:integration`, publish, merge |
| human-owner | **@millibitonline** | Final decisions, approvals, resource allocation, merge authorization | — |

Agents coordinate through GitHub issues (hand-offs), pull requests (proposed
changes), and Markdown/ADRs (decisions). See
[docs/OPERATING_MODEL.md](../docs/OPERATING_MODEL.md) and the
[hand-off protocol](../aios/agents/HANDOFF_PROTOCOL.md).

## Shared capabilities
Capabilities are organization-owned services that every channel consumes. Each
has a `CAPABILITY.md` (contract) and `.aios.yaml` (rules projects inherit).

| Capability | Lead role | Purpose |
|------------|-----------|---------|
| [content-production](capabilities/content-production/CAPABILITY.md) | creative-director | Idea → draft → review pipeline and content standards |
| [publishing](capabilities/publishing/CAPABILITY.md) | engineer | Approved → scheduled → published, gated by human approval |
| [analytics](capabilities/analytics/CAPABILITY.md) | engineer (+ strategist for insight) | Standard metrics and reporting cadence |
| [financial-reporting](capabilities/financial-reporting/CAPABILITY.md) | strategist (+ engineer for data) | Revenue, cost, and P&L per channel |
| [asset-management](capabilities/asset-management/CAPABILITY.md) | creative-director (+ engineer for storage) | Asset manifests, lifecycle, rights/provenance, storage abstraction (no media in git) |

## Organization-level rules (beyond Foundation)
- Production integrations are **off** (`integrations.production_enabled: false`, locked).
- Content moves through `idea → draft → in-review → approved → scheduled → published`;
  `scheduled` and `published` require `gate:publish`.
- AI-assisted and sponsored content must carry platform-appropriate disclosures.
- Default cadence: 3 posts/week per channel (projects may override with approval).
