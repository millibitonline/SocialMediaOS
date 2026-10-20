# Feature: Channel Launch

- **Project:** coffee-help
- **Owner role:** strategist (coordinates); each phase owned as listed
- **Accountable human:** @millibitonline
- **Status:** active (Phase 0 complete in `feature/coffee-help-init`)
- **Gates required:** publish (Phase 4); integration and spend if automation or domains are pursued

## Goal
Take Coffee.help from a registered project to its first approved, published
posts, following the [Channel Launch Playbook](../../../../organization/teams/channels/LAUNCH_PLAYBOOK.md),
within PolyCoffee's authority and the claims policy.

## Acceptance criteria
- [ ] STRATEGY.md accepted by the human owner
- [ ] CLAIMS_POLICY.md accepted by the human owner (and reviewed by a qualified person if the owner requires it)
- [ ] PolyCoffee approver and affiliation disclosure wording recorded
- [ ] CHANNEL.md accepted by the human owner
- [ ] 4-week editorial calendar and ≥6 seed ideas committed
- [ ] First batch of posts approved under `gate:publish` and published manually
- [ ] First weekly analytics snapshot committed
- [ ] Project status → `active`

## Tasks
| # | Task | Role | Status | Branch |
|---|------|------|--------|--------|
| 0.1 | Scaffold project, register channel identities and domains | creative-director (implementation support) | done | feature/coffee-help-init |
| 0.2 | External authority, claims policy, integration requirements documented | creative-director | done (pending approval) | feature/coffee-help-init |
| 0.3 | Owner supplies account details listed in INTEGRATIONS.md §4 (no credentials) | human owner | todo | n/a |
| 0.4 | Name PolyCoffee approver, agree disclosure wording | human owner + PolyCoffee | todo | n/a |
| 1.1 | Positioning, audience, platform priorities → STRATEGY.md | strategist | todo | feature/coffee-help-strategy |
| 1.2 | 90-day metric targets | strategist | todo | feature/coffee-help-strategy |
| 1.3 | Monetization hypothesis (within PolyCoffee's authority) | strategist | todo | feature/coffee-help-strategy |
| 2.1 | Voice, visuals, pillars → CHANNEL.md | creative-director | blocked by 1.x | feature/coffee-help-creative |
| 2.2 | Series concepts + 4-week calendar | creative-director | blocked by 2.1 | feature/coffee-help-creative |
| 2.3 | 6–10 seed ideas in content/ideas | creative-director | blocked by 2.1 | feature/coffee-help-creative |
| 3.1 | Integration ADR (secrets, app ownership, scopes, dry-run) | engineer | blocked by 0.3 | feature/coffee-help-integration-adr |
| 4.1 | Approve + publish first batch | human owner | blocked by 2.x | content/coffee-help-batch-1 |

## Hand-offs
Each hand-off becomes a GitHub Issue from the *Agent hand-off* form
([protocol](../../../../aios/agents/HANDOFF_PROTOCOL.md)).

| From | To | Input | Expected output |
|------|----|-------|-----------------|
| human owner | strategist | this project's docs | STRATEGY.md |
| strategist | creative-director | merged STRATEGY.md | CHANNEL.md + calendar |
| human owner | engineer | INTEGRATIONS.md + owner-supplied details | integration ADR |
| creative-director | human owner (+ PolyCoffee if claims) | content PR in `in-review/` | approvals |
