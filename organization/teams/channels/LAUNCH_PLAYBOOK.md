# Channel Launch Playbook

Every new channel follows these phases. Each phase is a **feature** in the
channel's project and ends with a PR reviewed by the human owner.

## Phase 0 — Scaffold (engineer)
- [ ] Branch `feature/<channel>-scaffold`.
- [ ] Copy `templates/channel/` to `projects/<channel-id>/`.
- [ ] Fill `.aios.yaml` (`id`, `name`, `channel.*`), register the project in
      `organization/teams/channels/.aios.yaml`.
- [ ] `python scripts/validate_aios.py` passes.

## Phase 1 — Strategy (strategist)
- [ ] Positioning, audience, competitive landscape, platform choice → `STRATEGY.md`.
- [ ] Success metrics for the first 90 days (uses analytics capability metrics).
- [ ] Monetization hypothesis (feeds financial-reporting).

## Phase 2 — Creative direction (creative-director)
- [ ] Voice, tone, visual direction, content pillars → `CHANNEL.md`.
- [ ] Series concepts and first 4-week editorial calendar.
- [ ] 6–10 seed ideas in `content/ideas/`.

## Phase 3 — Pipeline readiness (engineer)
- [ ] Content metadata validated by CI.
- [ ] Reporting stubs in `reports/`.
- [ ] (Later, via ADR + `gate:integration`) platform connections.

## Phase 4 — Launch gate (human owner)
- [ ] Handles/accounts secured by the human owner (never by an agent).
- [ ] First batch of posts approved under `gate:publish`.
- [ ] Project `status` moves `planning → active`.
