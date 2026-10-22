# Coffee.help Asset Library

**Owner role:** creative-director (production specifications) · engineer (future automation) · human owner (approvals)
**Status:** structure and specifications only. No storage is connected, no Drive folders exist yet, nothing is published.

The asset library is how every contributor (ChatGPT, Claude, Antigravity,
external collaborators and their AI production agents, and the human owner)
finds, creates, reviews, and reuses Coffee.help media: storyboard frames,
generated images, video clips, audio, and final videos. It is the production
backbone for an automated social media workflow, not just a picture folder.

## Two layers

| Layer | Holds | Why |
|-------|-------|-----|
| **GitHub (this folder)**, source of truth | One **manifest** per asset (identity, metadata, prompts, generation settings, storage reference, rights and provenance, review status), plus prompts, style references, and production specs | Versioned, reviewable, readable by any agent without media access |
| **Media storage** (proposed: Google Drive) | The media files themselves (images, frames, clips, audio, exports, project files) | Large binaries don't belong in git |

**No media files are committed to this repository.** `.gitignore` blocks
common media formats under `projects/*/assets/`. Manifests reference files by
a provider-neutral `asset_id` and a provider file ID, so storage can change
without breaking identifiers or production records. See
[LIBRARY_STRUCTURE.md](LIBRARY_STRUCTURE.md).

## What's here

| Path | Purpose |
|------|---------|
| [`LIBRARY_STRUCTURE.md`](LIBRARY_STRUCTURE.md) | Storage hierarchy, naming, identifiers, versioning, provider abstraction, formats, access |
| [`ASSET_MANIFEST.schema.json`](ASSET_MANIFEST.schema.json) | JSON Schema (Draft 2020-12) every manifest must validate against |
| [`manifests/`](manifests/) | One JSON manifest per asset, named `<asset_id>.json` |
| [`prompts/VISUAL_STYLE.md`](prompts/VISUAL_STYLE.md) | Working visual style and prompt building blocks |

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
3. the content piece passes its own review: content class per
   [CLAIMS_POLICY.md](../CLAIMS_POLICY.md) (visuals count toward the class,
   including implied health symbolism), PolyCoffee approval if Class C, and the
   owner's `gate:publish`.

## How agents work with assets

| Task | How |
|------|-----|
| **Discover** | List `manifests/*.json`. Filter by `content_id`, `asset_type`, `review_status`, `rights_status`. |
| **Read metadata** | Parse the manifest. It validates against the schema. |
| **Check usability** | `review_status == approved` **and** `rights_status == cleared` **and** `usage_restrictions` permit the use |
| **Find the file** | `storage_provider` + `storage_file_id`. Access the file only through permissions the owner has granted you. Manifests never contain sharing links or tokens. |
| **See how it was made** | `generation_provider`, `generation_model`, `generation_prompt`, `negative_prompt`, `generation_settings`, `source_assets` |
| **Propose a new asset** | Branch, add `manifests/<new asset_id>.json` with `review_status: proposed` (or `generated` once a file exists), and open a PR |
| **Revise an asset** | Same `asset_id`, `version` + 1, for a revision of the same variation. A different take is a new variation (new `asset_id`). |

All changes go through a branch and PR (no direct commits to `main`), with the
repo's attribution trailers (`Agent:` / `Proposed-by:` / `Committed-by:`).
See [docs/OPERATING_MODEL.md](../../../docs/OPERATING_MODEL.md).

## Approval responsibilities

| Decision | Who |
|----------|-----|
| Select candidates, mark `in_review`, recommend approval | creative-director (Claude) |
| Strategic fit of assets to the content plan | strategist (ChatGPT), advisory |
| Pipeline, storage integration, automated validation | engineer (Antigravity), under ADR + `gate:integration` |
| **Approve an asset** (`approved`) | **Human owner**, recorded in a PR review or an approval-log entry |
| **Rights determination** (`cleared` / `restricted` / `not_cleared`) | **Human owner** (with advice as needed) |
| Publish anything that uses the asset | Human owner, `gate:publish` |

## External collaborators

External collaborators and their AI production agents (currently Dan and his
production agents) contribute like any other contributor:
- **Through PRs to this repository**, adding or updating manifests and specs.
  They need a registered contributor entry first: AIOS only lets registered
  contributors open PRs (`aios/agents/AGENT_STANDARDS.md`). This is an owner decision.
- **Media through owner-authorized storage only**, such as a dedicated shared
  folder or a future integration service. Never through the owner's personal
  Adobe or Google credentials.
- Third-party contributions use `source_category: third_party_contributed`, with
  `created_by` naming the contributor and `license_type` pointing to the agreement
  that governs use. `rights_status` stays `pending_review` until the owner clears it.

## Reuse and attribution
- **Reuse by reference.** A new asset derived from existing ones lists them in
  `source_assets`. Composites (`source_category: composite`) must list all inputs.
- **Restrictions are inherited.** A derived asset carries forward every
  `usage_restrictions` entry of its sources, and its rights can't be broader
  than theirs.
- **Never assume rights.** AI-generated assets are not assumed to be
  copyright-protected, exclusive, or unrestricted. Licensed stock is not assumed
  to allow redistribution, sharing with collaborators, or use as input to
  third-party AI systems. Each asset's rights are determined and recorded.
- **Credit the maker.** `created_by` always names the human, agent, or
  collaborator who made it. Prompts are kept verbatim.
- Assets for a PolyCoffee product context follow
  [EXTERNAL_AUTHORITY.md](../EXTERNAL_AUTHORITY.md). No PolyCoffee packaging,
  logos, or product depictions without PolyCoffee approval (Class C).

## Validating manifests

```bash
pip install jsonschema
python3 - <<'EOF'
import json, glob
from jsonschema import Draft202012Validator, FormatChecker
base = "projects/coffee-help/assets"
v = Draft202012Validator(json.load(open(f"{base}/ASSET_MANIFEST.schema.json")),
                         format_checker=FormatChecker())
for path in sorted(glob.glob(f"{base}/manifests/*.json")):
    errs = list(v.iter_errors(json.load(open(path))))
    print(("OK   " if not errs else "FAIL ") + path, *[e.message for e in errs])
EOF
```

Adding this check to CI is proposed for the engineer (see the PR's outstanding decisions).
