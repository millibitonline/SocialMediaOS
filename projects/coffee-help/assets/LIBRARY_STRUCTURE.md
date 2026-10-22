# Asset Library Structure: Coffee.help

**Status:** proposed. The storage folders below **do not exist yet**. The owner
creates or authorizes them in a later step.

## 1. Proposed storage hierarchy (Google Drive)

```
Coffee.help/
  00_Brand_References/      brand_reference          CH-LIB-REF-####
  01_Storyboards/           storyboard_frame         CH-###-S##-V##
  02_Generated_Images/      image                    CH-###-S##-V##, CH-###-T##-V##
  03_Video_Clips/           video_clip               CH-###-S##-V##
  04_Audio/                 audio                    CH-###-A##-V##, CH-LIB-SND-####
  05_Final_Videos/          final_video              CH-###-F##-V##
  06_Production_Projects/   production_project       CH-###-F##-V## (project file), CH-LIB-TPL-####
```

Inside each top-level folder, group content-bound files by content id (e.g.
`01_Storyboards/CH-001/`). Folder placement is a convenience only: **identity
comes from the `asset_id` in the manifest, never from the folder path.**

## 2. Asset identifiers

| Form | Pattern | Example | Use |
|------|---------|---------|-----|
| Content-bound | `CH-<content>-<part><nn>-V<variation>` | `CH-001-S01-V04` | Asset made for one content piece |
| Library | `CH-LIB-<kind>-<nnnn>` | `CH-LIB-REF-0001` | Reusable across content (brand references, templates, sound) |

- `CH` is the Coffee.help project prefix.
- `<content>` is a 3-digit content sequence (`CH-001` = Coffee.help Video 001).
  Content files declare it as `content_ref: CH-001` in front matter, which links
  a content piece to its assets.
- `<part>`: `S` scene, `A` audio track, `T` thumbnail, `F` final export.
- `V<variation>` is an alternative take of the same part (V01, V02, …).
- Library `<kind>`: `REF` brand/style reference, `TPL` template or project file,
  `SND` reusable sound.

IDs are permanent. They are never reused, even after an asset is archived or rejected.

## 3. Versioning

| Concept | Where | Changes when |
|---------|-------|--------------|
| **Variation** | In the `asset_id` (`V04`) | A different take or alternative composition |
| **Version** | `version` field (1, 2, …) | A revision of the same variation (retouch, upscale, re-render with the same intent) |

The manifest describes the current version. Earlier versions stay in git
history, and their files stay in storage with their own versioned filenames.

## 4. Naming convention

`<asset_id>_v<version>.<ext>`. Examples:
- `CH-001-S01-V04_v1.png`
- `CH-001-F01-V01_v3.mp4`

Names use no spaces or dates. Dates live in manifest metadata.

## 5. Storage provider abstraction

- Manifests store `storage_provider` (e.g. `google_drive`), `storage_file_id`
  (the provider's stable ID), and optionally `storage_url`.
- **The provider-neutral key is `asset_id`.** To migrate storage, copy the files,
  then update `storage_provider` and `storage_file_id` in each manifest by PR.
  IDs, prompts, approvals, and production records don't change.
- `storage_url` must be an access-controlled link for authorized users. **Never**
  a public or "anyone with the link" URL, and never a URL that embeds a token,
  signature, or resource key. The schema rejects common forms of these.
- No credentials, tokens, or private sharing links go in any manifest or file in
  this repository.

## 6. File formats (recommended)

| Asset type | Master format | Notes |
|------------|---------------|-------|
| Generated image / storyboard frame | PNG (or the provider's original export) | Keep the provider's original. Derived crops are new versions. |
| Brand reference | PNG, PDF, SVG | |
| Video clip | MP4 (H.264) or MOV (ProRes) for masters | Keep the highest-quality original. |
| Audio | WAV (master), AAC/MP3 (delivery) | |
| Final video | MP4 (H.264/AAC), per-platform aspect ratios (e.g. 9:16, 16:9, 1:1) | One final asset per platform cut (`F01`, `F02`, …) |
| Production project | The editing tool's native format | Bundle linked media references |

## 7. Access and permissions

- **The owner controls storage.** Drive folders are created and shared by the
  owner, not by agents.
- **Least privilege:** grant each collaborator or agent integration access only
  to the folders it needs (e.g. read-only `00_Brand_References`, write to its own
  working folder).
- **No personal credentials** are shared with agents or external collaborators.
  Access is through explicitly granted folder permissions or a future integration
  service (an engineer ADR with `gate:integration`).
- Prefer a dedicated shared drive owned by the business over a personal "My Drive"
  folder, so access survives personnel changes. This is an owner decision.
- Revoking a collaborator's storage access doesn't change their manifests;
  provenance stays intact.

## 8. From generated assets to published videos

```
proposed spec ─► generated frames/clips ─► approved assets ─► edit (production project)
      │                                                            │
      └──────────────────── source_assets links ◄──────────────────┘
                                                                   ▼
                                       final_video (F##) ─► content piece (content_ref) ─► gate:publish
```

- A `final_video` manifest lists every clip, frame, audio track, and template it
  uses in `source_assets`, so rights and restrictions can be traced from any
  published video back to its inputs.
- The content file (`projects/coffee-help/content/<stage>/…`, see
  [content-production](../../../organization/capabilities/content-production/CAPABILITY.md))
  references its final asset IDs. Its **Sources & rights** section summarizes
  the rights of the listed assets.
- Publication follows the publishing capability: owner `gate:publish`, approval
  tied to the exact commit, manual posting until an integration ADR is accepted.
