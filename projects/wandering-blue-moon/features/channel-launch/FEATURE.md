# Feature: Channel Launch

- **Project:** wandering-blue-moon
- **Owner role:** strategist (coordinates); each phase owned as listed
- **Accountable human:** @millibitonline
- **Status:** active — Phase 0 complete in `setup/initial-architecture`
- **Gates required:** publish (Phase 4)

## Goal
Take Wandering Blue Moon from an empty project to its first approved, published
posts, following the [Channel Launch Playbook](../../../../organization/teams/channels/LAUNCH_PLAYBOOK.md).

## Acceptance criteria
- [ ] STRATEGY.md accepted by the human owner
- [ ] CHANNEL.md accepted by the human owner
- [ ] 4-week editorial calendar and ≥6 seed ideas committed
- [ ] First batch of posts approved under `gate:publish` and published manually
- [ ] First weekly analytics snapshot committed
- [ ] Project status → `active`

## Tasks
| # | Task | Role | Status | Branch |
|---|------|------|--------|--------|
| 0.1 | Scaffold project from `templates/channel` | engineer | done | setup/initial-architecture |
| 1.1 | Positioning, audience, platforms → STRATEGY.md | strategist | todo | feature/wandering-blue-moon-strategy |
| 1.2 | 90-day metric targets | strategist | todo | feature/wandering-blue-moon-strategy |
| 1.3 | Monetization hypothesis | strategist | todo | feature/wandering-blue-moon-strategy |
| 2.1 | Voice, visuals, pillars → CHANNEL.md | creative-director | blocked by 1.x | feature/wandering-blue-moon-creative |
| 2.2 | Series concepts + 4-week calendar | creative-director | blocked by 2.1 | feature/wandering-blue-moon-creative |
| 2.3 | 6–10 seed ideas in content/ideas | creative-director | blocked by 2.1 | feature/wandering-blue-moon-creative |
| 3.1 | CI check for content front matter | engineer | todo | feature/content-frontmatter-check |
| 4.1 | Secure handles/accounts | human owner | todo | — |
| 4.2 | Approve + publish first batch | human owner | blocked by 2.x, 4.1 | content/wandering-blue-moon-batch-1 |

## Hand-offs
| From | To | Input | Expected output |
|------|----|-------|-----------------|
| strategist | creative-director | merged STRATEGY.md | CHANNEL.md + calendar |
| creative-director | human owner | content PR in `in-review/` | approval (PR review) |
| human owner | engineer | published URLs | files moved to `published/` |
