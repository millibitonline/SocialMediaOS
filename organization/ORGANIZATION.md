# SocialMediaOS — Organization

SocialMediaOS is an implementation of [AIOS](../aios/README.md) that launches and
operates social media channels. It inherits every Foundation rule and adds
social-media-specific structure on top.

## Structure

```
Foundation   aios/                                   (inherited, unchanged)
Organization /.aios.yaml + organization/             SocialMediaOS
Team         organization/teams/channels/            owns all channel projects
Project      projects/<channel>/                     one per channel (e.g. wandering-blue-moon)
Feature      projects/<channel>/features/<feature>/  a deliverable (launch, a series, a campaign)
Task         rows in FEATURE.md or GitHub Issues     leaf work items
Contributor  ChatGPT · Claude · Antigravity · human owner
```

## Contributors and responsibilities

| Contributor | AIOS role | Owns | Never does |
|-------------|-----------|------|------------|
| **ChatGPT** | strategist | Strategy, architecture, roadmaps, channel positioning, ADR drafts | Write final content, change automation, merge |
| **Claude** | creative-director | Creative direction, voice, content ideation and development, editorial calendars | Change governance or tooling, publish, merge |
| **Antigravity** | engineer | Repo tooling, validation, CI, automation, integration design, data pipelines | Connect production systems without `gate:integration`, publish, merge |
| **Human owner** | human-owner | Approvals for architecture, publishing, spend, integrations; merges | — |

## Shared capabilities
Capabilities are organization-owned services that every channel consumes. Each
has a `CAPABILITY.md` (contract) and `.aios.yaml` (rules projects inherit).

| Capability | Lead role | Purpose |
|------------|-----------|---------|
| [content-production](capabilities/content-production/CAPABILITY.md) | creative-director | Idea → draft → review pipeline and content standards |
| [publishing](capabilities/publishing/CAPABILITY.md) | engineer | Approved → scheduled → published, gated by human approval |
| [analytics](capabilities/analytics/CAPABILITY.md) | engineer (+ strategist for insight) | Standard metrics and reporting cadence |
| [financial-reporting](capabilities/financial-reporting/CAPABILITY.md) | strategist (+ engineer for data) | Revenue, cost, and P&L per channel |

## Organization-level rules (beyond Foundation)
- Production integrations are **off** (`integrations.production_enabled: false`, locked).
- Content moves through `idea → draft → in-review → approved → scheduled → published`;
  `scheduled` and `published` require `gate:publish`.
- AI-assisted and sponsored content must carry platform-appropriate disclosures.
- Default cadence: 3 posts/week per channel (projects may override with approval).
