# Capability: Asset Management

**Lead role:** creative-director (production specifications) · engineer (storage integration, automation) · human owner (approvals, rights)
**Status:** defined. No storage connected, no automation. Introduced by [ADR-0003](../../../docs/adr/0003-lift-cross-channel-capabilities.md) (proposed).

## Contract
A shared, AI-native asset library for every SocialMediaOS channel. All
contributors (strategist, creative-director, engineer, external collaborators
and their AI production agents, and the human owner) find, create, review, and
reuse media through it: storyboard frames, generated images, video clips, audio,
and final videos. It is the production backbone for automated social media, not
a picture folder.

| Layer | Holds | Why |
|-------|-------|-----|
| **GitHub**, source of truth | One **manifest** per asset (identity, metadata, prompts, generation settings, storage reference, rights and provenance, review status), plus each channel's prompts, style references, and production specs | Versioned, reviewable, readable by any agent without media access |
| **Media storage** (proposed: Google Drive) | The media files themselves | Large binaries don't belong in git |

**No media files are committed to this repository.** `.gitignore` blocks common
media formats under `projects/*/assets/`.

| File | Purpose |
|------|---------|
| [`ASSET_MANIFEST.schema.json`](ASSET_MANIFEST.schema.json) | JSON Schema (Draft 2020-12) every manifest in every channel must validate against |
| [`LIBRARY_STRUCTURE.md`](LIBRARY_STRUCTURE.md) | Storage layout template, identifiers, versioning, naming, provider abstraction, formats, access |
| [`.aios.yaml`](.aios.yaml) | Rules every consuming project inherits |

## What each channel provides
A channel that uses this capability (`capabilities.uses: [asset-management]`) declares:

```yaml
# projects/<channel>/.aios.yaml
asset_library:
  path: projects/<channel>/assets          # manifests/ + channel creative references
  asset_prefix: CH                         # 2–4 uppercase letters, unique across channels
  storage_root: "Coffee.help/"             # folder name in the storage provider (once created)
  storage_provider_proposed: google_drive  # nothing exists until the owner creates it
```

…and keeps, in `projects/<channel>/assets/`:
- `manifests/<asset_id>.json`, one per asset
- channel creative references (e.g. `prompts/VISUAL_STYLE.md`)
- a short `README.md` with the channel's prefix, storage root, and anything channel-specific

## Asset lifecycle

```
proposed ──► generated ──► in_review ──► approved ──► archived
                               │
                               └──► rejected ──► archived
```

| Status | Meaning | Who moves it here |
|--------|---------|-------------------|
| `proposed` | A spec or prompt exists; no file yet | Any contributor (via PR) |
| `generated` | A file exists (may still be pending upload) | Whoever generated it |
| `in_review` | Selected or submitted for creative review | creative-director, or the contributor via PR |
| `approved` | **Creative asset approval**, recorded by a human (`approved_by`, `approved_at`, `approval_ref`) | Human owner only |
| `rejected` | Not to be used; kept for provenance | creative-director or owner |
| `archived` | Retired or superseded; kept for provenance | Any contributor (via PR) |

Separate from the review lifecycle, each manifest also tracks:
- `storage_status`: `not_created` → `pending_upload` → `uploaded` (or `removed`)
- `rights_status`: `pending_review` → `cleared` / `restricted` / `not_cleared`

### Asset approval is not publication approval
An `approved` asset is approved as a creative asset, not for posting. Media can
appear in a published piece only when:
1. the asset is `approved` **and** its `rights_status` is `cleared`,
2. its `usage_restrictions` allow that use, and
3. the content piece passes its own review: the channel's claims and disclosure
   rules (visuals count, including implied claims or symbolism), any
   external-authority approval the channel requires, and the owner's
   `gate:publish`.

## How agents work with assets

| Task | How |
|------|-----|
| **Discover** | List `projects/<channel>/assets/manifests/*.json`. Filter by `content_id`, `asset_type`, `review_status`, `rights_status`. |
| **Read metadata** | Parse the manifest. It validates against the schema. |
| **Check usability** | `review_status == approved` **and** `rights_status == cleared` **and** `usage_restrictions` permit the use |
| **Find the file** | `storage_provider` + `storage_file_id`. Access the file only through permissions the owner has granted you. Manifests never contain sharing links or tokens. |
| **See how it was made** | `generation_provider`, `generation_model`, `generation_prompt`, `negative_prompt`, `generation_settings`, `source_assets` |
| **Propose a new asset** | Branch, add `manifests/<new asset_id>.json` with `review_status: proposed` (or `generated` once a file exists), and open a PR |
| **Revise an asset** | Same `asset_id`, `version` + 1, for a revision of the same variation. A different take is a new variation (new `asset_id`). |

All changes go through a branch and PR (no direct commits to `main`), with the
repo's attribution trailers (`Agent:` / `Proposed-by:` / `Committed-by:`). See
[docs/OPERATING_MODEL.md](../../../docs/OPERATING_MODEL.md).

## Approval responsibilities

| Decision | Who |
|----------|-----|
| Select candidates, mark `in_review`, recommend approval | creative-director |
| Strategic fit of assets to the content plan | strategist, advisory |
| Pipeline, storage integration, automated validation | engineer, under ADR + `gate:integration` |
| **Approve an asset** (`approved`) | **Human owner**, recorded in a PR review or an approval-log entry |
| **Rights determination** (`cleared` / `restricted` / `not_cleared`) | **Human owner** (with advice as needed) |
| Publish anything that uses the asset | Human owner, `gate:publish` |

## External collaborators
External collaborators and their AI production agents contribute like any other contributor:
- **Through PRs**, adding or updating manifests and specs. They need a
  registered contributor entry first: AIOS only lets registered contributors
  open PRs (`aios/agents/AGENT_STANDARDS.md`). This is an owner decision.
- **Media through owner-authorized storage only**, such as a dedicated shared
  folder or a future integration service. Never through the owner's personal
  credentials (Adobe, Google, or other).
- Third-party contributions use `source_category: third_party_contributed`, with
  `created_by` naming the contributor and `license_type` pointing to the agreement
  that governs use. `rights_status` stays `pending_review` until the owner clears it.

## Rights and provenance
The schema distinguishes five source categories, each tracked for rights and
restrictions:

| `source_category` | Examples | Default stance |
|-------------------|----------|----------------|
| `ai_generated` | Adobe Firefly, other image or video models | Not assumed copyright-protected, exclusive, or unrestricted. The provider's terms at generation time govern. |
| `licensed_stock` | Adobe Stock | Not assumed to allow redistribution, sharing with collaborators, or use as input to third-party AI systems. The license tier governs. |
| `original` | Owner/team photography and video | Owner confirms ownership and any releases (people, locations) |
| `third_party_contributed` | Collaborator deliveries | Governed by the contributor agreement |
| `composite` | Edits combining several sources | Rights are no broader than the most restrictive input. All inputs listed in `source_assets`. |

Agents identify usable assets by `rights_status` (`cleared`), unusable ones
(`restricted`, `not_cleared`), and pending ones (`pending_review`).

## Reuse and attribution
- **Reuse by reference.** A derived asset lists its inputs in `source_assets`.
- **Restrictions are inherited.** A derived asset carries forward every
  `usage_restrictions` entry of its sources.
- **Credit the maker.** `created_by` always names the human, agent, or
  collaborator who made it. Prompts are kept verbatim.
- **Cross-channel reuse** is allowed only with a new manifest in the receiving
  channel (its own prefix) that lists the original in `source_assets`, and only
  if the original's rights and restrictions permit it.

## Validating manifests

```bash
pip install jsonschema
python3 - <<'EOF'
import json, glob
from jsonschema import Draft202012Validator, FormatChecker
schema = json.load(open("organization/capabilities/asset-management/ASSET_MANIFEST.schema.json"))
v = Draft202012Validator(schema, format_checker=FormatChecker())
for path in sorted(glob.glob("projects/*/assets/manifests/*.json")):
    errs = list(v.iter_errors(json.load(open(path))))
    print(("OK   " if not errs else "FAIL ") + path, *[e.message for e in errs])
EOF
```

Proposed for the engineer: run this in CI, and also check that each manifest's
`asset_id` prefix and `project_id` match its project's `.aios.yaml`.
