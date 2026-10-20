# Capability: Content Production

**Lead role:** creative-director (Claude) · **Status:** defined, no automation

## Contract
Turns channel strategy into reviewable content. Every channel stores content in
`projects/<channel>/content/<stage>/` where stage is one of
`ideas`, `drafts`, `in-review`, `approved`, `published`.

## Content file format
One Markdown file per piece, named `YYYY-MM-DD-<slug>.md`, with front matter:

```yaml
---
id: 2026-10-25-first-light
channel: travel-lava
stage: draft                # idea | draft | in-review | approved | published
format: short-video         # short-video | carousel | single-image | long-video | text | story
platforms: [instagram, tiktok]
pillar: <content pillar from CHANNEL.md>
series: <optional series id>
generated_by: claude        # required while AI-generated and unapproved
ai_assisted: true           # drives platform disclosure
sponsored: false
target_publish_date: 2026-10-25
---
```

Body sections: **Hook**, **Script / Copy**, **Visual direction**, **Caption**,
**Hashtags / keywords**, **Sources & rights** (music, footage, quotes, licenses).

## Workflow
1. **Idea** — one paragraph + pillar. Anyone may add.
2. **Draft** — creative-director develops full piece.
3. **In-review** — PR opened; human reviews. Agents may leave advisory review.
4. **Approved** — human approval recorded (PR review on the exact version).
5. Hand-off to **publishing**.

Stages are moved by `git mv` in a PR so history shows each transition.

## Standards
- Every claim of fact has a source in **Sources & rights**.
- All third-party assets list license/permission; unknown rights = not publishable.
- No impersonation of real people; no fabricated testimonials or reviews.
- Disclosures per [organization rules](../../ORGANIZATION.md).
