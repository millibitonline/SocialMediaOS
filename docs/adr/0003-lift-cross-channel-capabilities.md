# ADR-0003: Lift cross-channel capabilities out of Coffee.help

- **Status:** proposed
- **Date:** 2026-10-21
- **Layer(s):** foundation (principles), organization (capabilities, templates), project (coffee-help, travel-lava)
- **Proposed by:** creative-director (Claude), at the owner's request
- **Decided by:** _pending: human owner (strategist review requested)_

## Context
Coffee.help was set up first and in detail. Along the way it gained machinery
that has nothing to do with coffee: an asset library, a content-class and
disclosure standard, an approved-claims registry, per-platform publishing
requirements, rights and provenance tracking, and several document formats.
All of it lives under `projects/coffee-help/`. Travel Lava, and every future
channel, would have to copy it. That goes against ADR-0001, where shared
capabilities belong to the Organization and projects consume them. Some ideas
are not even specific to social media and belong in the platform-neutral
AIOS Foundation.

## Decision
Lift cross-channel elements to the lowest layer where they apply to everyone,
in four phases, each its own PR.

### Phase 1: Asset management capability (PR #5)
- New capability `organization/capabilities/asset-management/`: the generic
  manifest schema, lifecycle, ID and naming conventions, storage-provider
  abstraction, storage-layout template, rights/provenance categories, agent
  interoperability, and external-collaborator rules.
- Each channel keeps only its asset ID prefix, its storage root, its manifests,
  and its creative references.
- `content_ref` becomes a standard optional content front-matter field
  (content-production), linking content to assets.

### Phase 2: Organization standards (follow-up PR)
- **Claims and disclosure standard** (content-production): Class A general / B
  sensitive-topic education / C commercial; whole-presentation classification;
  contextual disclosures; approved-claims registry pattern. Each channel
  declares its own sensitive topics (e.g. health for Coffee.help).
- **Platform publishing requirements** (publishing): YouTube, Instagram, and
  TikTok API rules, audits, limits, and the operational requirements (emergency
  stop, idempotency, token lifecycle, corrections, sanitized audit logs).
- **Honest AI imagery** rules (content-production).
- **Channel templates:** channel registry, external-authority, business brief,
  visual style, and assets skeleton in `templates/channel/`.

### Phase 3: Foundation principles (follow-up PR, `gate:architecture`)
Platform-neutral additions to `aios/`:
1. Approving an artifact is not approving its external release.
2. Provenance and rights travel with every external-facing artifact and are never assumed.
3. Large binary artifacts live outside the repository; the repository holds
   records with storage-independent identifiers.
4. **External authorities:** an outside party may own named decisions, declared
   in configuration and checked by the validator.
5. Reviews are recorded as repository files, with agent attribution where
   identities are shared.

### Phase 4: Backfill
Bring Travel Lava (and the channel template) onto the lifted capabilities and
standards. Coffee.help's project files are reduced to channel-specific content
that references the shared versions.

## Alternatives considered
1. **Leave everything in Coffee.help; copy per channel.** Fastest now, but
   channels drift and fixes have to be repeated everywhere. Rejected.
2. **Lift everything to the Foundation.** Simpler hierarchy, but it breaks
   AIOS platform neutrality (Principle 7). Social-specific pieces belong at
   Organization level. Rejected.
3. **Lift everything in one large PR.** Fewer cycles, but hard to review and it
   mixes a Foundation change (`gate:architecture`) with routine capability
   work. Rejected in favor of phases.
4. **Wait until a second channel actually needs it.** Avoids premature
   abstraction, but Travel Lava already needs the same pieces, and lifting
   before Coffee.help's library is merged avoids building it twice. Rejected.

## Consequences
- New channels start with assets, claims, disclosure, and publishing
  standards in place.
- Coffee.help's documents get shorter and point to shared capabilities.
- Organization-level changes now affect every channel, so reviews must
  consider all channels, not just one.
- The asset ID prefix becomes per-project configuration (`CH` for Coffee.help).

## Ownership
- **Decision owner:** strategist (architecture). The owner approves.
- **Implementing roles:** creative-director (capability docs, standards,
  templates), engineer (schema validation in CI, platform requirements, future
  storage integration).

## Approval requirements
- This ADR, and Phase 3 (Foundation), require the **human owner's approval**
  under `gate:architecture`.
- Phases 1, 2, and 4 are Organization/project changes and require the owner's
  approval of each PR.
- No phase authorizes storage creation, integrations, publishing, or spending.

## Follow-ups
- [ ] Phase 1: PR #5 (asset-management capability).
- [ ] Phase 2: claims/disclosure standard, platform requirements, templates.
- [ ] Phase 3: Foundation principles + external-authority validator support.
- [ ] Phase 4: Travel Lava backfill.
- [ ] Engineer: add manifest schema validation to CI.
