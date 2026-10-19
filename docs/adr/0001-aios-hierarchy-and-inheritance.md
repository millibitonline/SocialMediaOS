# ADR-0001: Adopt the AIOS hierarchy and inheritance model

- **Status:** proposed
- **Date:** 2026-10-18
- **Layer(s):** foundation, organization
- **Proposed by:** Claude (creative-director), at the owner's request
- **Decided by:** _pending — human owner_

## Context
SocialMediaOS needs a structure in which several AI agents and a human owner can
launch and run multiple channels without re-deciding rules per channel, and
without any agent quietly changing the rules. The model must be reusable for
other organizations (AIOS) and keep GitHub as the source of truth.

## Decision
1. Seven-level hierarchy: Foundation → Organization → Team → Project → Feature → Task → Contributor.
2. Each layer (through Feature) is declared by an `.aios.yaml` with a `parent:` path.
3. Merge semantics: scalars replace, lists append, maps merge; `locks:` freeze keys.
4. Loosening/changing an inherited value requires a declared, human-approved
   `overrides:` entry; tightening is documented via `extends:`. Anything else is a
   silent override and fails CI (`scripts/validate_aios.py`).
5. Shared capabilities (content-production, publishing, analytics,
   financial-reporting) are organization services that projects consume, not a
   hierarchy layer.
6. Agents are bound to vendor-neutral roles: ChatGPT → strategist,
   Claude → creative-director, Antigravity → engineer. Only humans merge and approve gates.
7. Production integrations are disabled and locked off until a later ADR.

## Consequences
- Every new channel is a copy of `templates/channel/` plus a team registration.
- Rule changes are visible in diffs and enforced in CI.
- Tasks and Contributors have no `.aios.yaml`; they are tracked in `FEATURE.md`/Issues
  and in the role registry respectively.
- CI enforcement is only as strong as branch protection on `main` (see follow-ups).

## Follow-ups
- [ ] Owner confirms approver handles in `.aios.yaml` and `CODEOWNERS`.
- [ ] Enable branch protection on `main`: require PR, 1 approval, Code Owners, status check "Validate AIOS".
- [ ] Decide Task tracking: FEATURE.md tables vs. GitHub Issues/Projects.
