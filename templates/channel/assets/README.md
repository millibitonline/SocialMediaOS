# <Channel Name> Assets

This channel's asset records and creative references. The library rules
(lifecycle, schema, identifiers, storage, approvals, rights, agent usage) are in
the [asset-management capability](../../../organization/capabilities/asset-management/CAPABILITY.md).

| Setting | Value |
|---------|-------|
| Asset prefix | `<XX>` (set in `.aios.yaml` → `asset_library.asset_prefix`) |
| Storage root (proposed) | `<Channel Name>/`. Not created until the owner authorizes it. |
| Manifest schema | [`ASSET_MANIFEST.schema.json`](../../../organization/capabilities/asset-management/ASSET_MANIFEST.schema.json) |

| Path | Purpose |
|------|---------|
| `manifests/` | One manifest per asset, `<asset_id>.json` |
| `prompts/` | Channel creative references (e.g. `VISUAL_STYLE.md`), added with creative direction |

## Current assets
_None yet._
