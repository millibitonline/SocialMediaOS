# Coffee.help Assets

Coffee.help's asset records and creative references. How the library works
(lifecycle, schema, identifiers, storage, approvals, rights, agent usage,
external collaborators) is defined once, for every channel, by the
**[asset-management capability](../../../organization/capabilities/asset-management/CAPABILITY.md)**.
This folder holds only what is specific to Coffee.help.

**Status:** no storage exists or is connected yet. No media is in git. Nothing is published.

## Coffee.help settings

| Setting | Value |
|---------|-------|
| Asset prefix | `CH` (e.g. `CH-001-S01-V04`, `CH-LIB-REF-0001`) |
| Storage root (proposed) | `Coffee.help/` with the standard subfolders in [LIBRARY_STRUCTURE.md §1](../../../organization/capabilities/asset-management/LIBRARY_STRUCTURE.md#1-storage-layout-template-proposed-provider-google-drive). Not created yet. |
| Manifest schema | [`ASSET_MANIFEST.schema.json`](../../../organization/capabilities/asset-management/ASSET_MANIFEST.schema.json) |
| Claims and disclosure rules for visuals | [`CLAIMS_POLICY.md`](../CLAIMS_POLICY.md). Visuals count toward the content class, including implied health symbolism. |
| External authority | [`EXTERNAL_AUTHORITY.md`](../EXTERNAL_AUTHORITY.md). No PolyCoffee packaging, logos, or product depictions without PolyCoffee approval (Class C). |
| External collaborators | Dan and his AI production agents (pending registration as contributors) |

## Contents

| Path | Purpose |
|------|---------|
| [`manifests/`](manifests/) | One manifest per Coffee.help asset |
| [`prompts/VISUAL_STYLE.md`](prompts/VISUAL_STYLE.md) | Working visual style and prompt building blocks (creative-director) |

## Current assets

| Asset | Type | Review | Rights | Storage |
|-------|------|--------|--------|---------|
| [`CH-001-S01-V04`](manifests/CH-001-S01-V04.json) | storyboard_frame (Adobe Firefly) | in_review (selected reference) | pending_review | pending_upload |
