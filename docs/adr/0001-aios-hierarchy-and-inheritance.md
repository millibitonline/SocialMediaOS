# ADR-0001: Adopt the AIOS hierarchy and inheritance model

- **Status:** proposed
- **Date:** 2026-10-18 (revised 2026-10-19)
- **Layer(s):** foundation, organization
- **Proposed by:** strategist (ChatGPT), written up by creative-director (Claude) at the owner's request
- **Decided by:** _pending: human owner_

## Context
SocialMediaOS needs a structure in which several AI agents and a human owner can
launch and run multiple channels without re-deciding rules for each channel, and
without any agent quietly changing the rules. The model must be reusable by other
organizations (AIOS), independent of any particular forge, social platform, or AI
vendor, and keep the git repository as the source of truth.

## Decision
1. A seven-level hierarchy: **Foundation → Organization → Team → Project → Feature → Task → Contributor**.
2. Every layer down to Feature is declared by an `.aios.yaml` with a `parent:` path. Tasks
   live in `FEATURE.md` or forge issues. Contributors live in the role registry and
   the Organization's `contributors:`.
3. Merge rules: scalars replace, lists append, maps merge. `locks:` freeze keys
   for every descendant.
4. Tightening an inherited value is documented under `extends:`. Loosening or
   changing it requires a declared `overrides:` entry with a reason and a recorded
   human approval. Anything else is a **silent override** and fails CI
   (`scripts/validate_aios.py`).
5. Shared capabilities (content-production, publishing, analytics,
   financial-reporting) are Organization services that projects consume. They are
   not a hierarchy layer.
6. The Foundation (`aios/`) contains no implementation-specific names (forge,
   platform, vendor, model, organization, channel). The Organization lists
   forbidden terms and CI enforces it.
7. Production integrations stay disabled and locked off until a later ADR.
8. The first channel project is **travel-lava**.

## Alternatives considered
1. **Flat repository with one shared rules file.** Simple, but it has no way to
   give channels their own rules or to record who changed a rule and why. Rejected.
2. **Per-channel repositories.** Strong isolation, but shared rules and
   capabilities drift across repos and cross-channel reporting is harder.
   Rejected for now; it can be revisited if channels need separate access control.
3. **Allow child layers to override freely (last-writer-wins).** Less friction, but
   it allows exactly the silent changes this model exists to prevent. Rejected.
4. **Capabilities as a hierarchy layer between Team and Project.** This would
   force every project into exactly one capability. Rejected in favor of
   projects consuming several capabilities.

## Consequences
- A new channel is a copy of `templates/channel/` plus a team registration.
- Rule changes show up in diffs and are enforced in CI.
- Enforcement only bites once branch protection on `main` requires the
  "Validate AIOS" check (see `docs/REPOSITORY_SETTINGS.md`).
- Reusing AIOS elsewhere means copying `aios/` and the validator unchanged.

## Ownership
- **Decision owner:** strategist (architecture). Changes go through an ADR.
- **Implementing roles:** engineer (validator, CI), creative-director (docs, templates).

## Approval requirements
- This ADR requires the **human owner's** approval under `gate:architecture`
  (an approving review on the PR that marks it accepted).
- Future changes to the hierarchy, merge semantics, or locks require a new or
  superseding ADR and the same approval.

## Follow-ups
- [ ] Owner confirms approver handles in `.aios.yaml` and `CODEOWNERS`.
- [ ] Owner enables branch protection on `main` (`docs/REPOSITORY_SETTINGS.md`).
- [ ] Decide task tracking granularity: FEATURE.md tables vs. issues only.
