# Publishing & Integration Requirements: Coffee.help (proposed)

**Owner role:** engineer (Antigravity) · **Prepared by:** creative-director (Claude) as implementation support
**Status:** proposal only. **Nothing is connected or authorized.**
Connecting any account requires an accepted ADR and `gate:integration`. Each post
also needs `gate:publish`. Coffee.help reuses the organization's
[publishing](../../organization/capabilities/publishing/CAPABILITY.md) and
[analytics](../../organization/capabilities/analytics/CAPABILITY.md) capabilities;
it does not build channel-specific infrastructure.

Platform facts below were checked against the official developer docs on
2026-10-19. These rules change often, so **re-verify them when building**.

## 1. Current mode: manual
1. A content PR is approved by the owner (plus PolyCoffee where
   [EXTERNAL_AUTHORITY.md](EXTERNAL_AUTHORITY.md) requires it).
2. The owner posts manually on each platform.
3. The file moves to `content/published/` with `published_url` and `published_at`.
4. Weekly analytics are entered by hand from each platform's dashboard
   (`reports/analytics/`).

## 2. Per-platform requirements for future automation

### YouTube (@getcoffeehelp)
- **API:** YouTube Data API v3, `videos.insert` for uploads.
- **Auth:** OAuth 2.0, with a scope such as `youtube.upload` (or `youtube` / `youtube.force-ssl`).
- **Quota:** the docs list `videos.insert` at 1 unit from a dedicated
  *Video Uploads* bucket, with 100 calls per day.
- **Unverified projects:** the current reference page says uploads from
  unverified API projects are not restricted to private viewing (older guidance
  said they were). Confirm at build time.
- **OAuth app status:** a Google Cloud project with an OAuth consent screen.
  Sensitive scopes for external users may need Google's app verification, and
  apps left in *Testing* status issue short-lived refresh tokens. Confirm the
  approach at build time.
- **Needed from owner:** the channel ID, whether the channel is a Brand Account, and
  who manages it.

### Instagram (@getcoffeehelp)
- **API:** Instagram Platform content publishing (images, videos, Reels,
  carousels of up to 10 items, Stories).
- **Account:** must be an Instagram **professional** account.
- **Login options:**
  - *Instagram Login* (Business Login for Instagram), with permissions
    `instagram_business_basic` and `instagram_business_content_publish`, or
  - *Facebook Login for Business* through a linked Facebook Page, with
    `instagram_basic`, `instagram_content_publish`, and `pages_read_engagement`.
    This option is required for resumable local video uploads.
- **Media:** must be on a publicly reachable URL when published. Images are JPEG only.
- **Limits:** a per-account cap on API-published posts in any rolling 24 hours.
  The docs give conflicting figures (100 vs. 50), so check the
  `content_publishing_limit` endpoint.
- **Meta app:** needs the right access level (Standard or Advanced) and any
  required app review.
- **Needed from owner:** the account type, whether a Facebook Page or Meta
  business portfolio exists, and which login option to use.

### TikTok (@getcoffeehelp)
- **API:** Content Posting API (Direct Post), scope `video.publish`.
- **Audit:** "All content posted by unaudited clients will be restricted to
  private viewing mode." The developer app must pass TikTok's audit before
  any public post.
- **UX requirements:** before each post, call `creator_info/query`. The chosen
  privacy level must be one TikTok returns, and the creator must explicitly consent.
- **Limits:** 6 init requests per minute per user token, daily per-user post caps,
  and upload URLs that expire after 1 hour.
- **Needed from owner:** the account type, and a TikTok developer account and app to
  submit for audit.

## 3. Shared infrastructure needed (organization-level, built once)
These belong to the organization's publishing and analytics capabilities, not to
Coffee.help. They serve every channel.
- **Secrets management** outside the repository (decided by ADR). Tokens are never committed.
- **Dry-run publisher** that renders each post's exact payload for human review
  (the publishing capability already requires `dry_run_required_before_live`).
- **Approval check** that matches the content file's commit SHA to a recorded
  `gate:publish` approval (and the PolyCoffee approval where required) right
  before any API call.
- **Media hosting** with public URLs (needed by Instagram).
- **Audit log** of every outbound call, committed to the repo.
- **Analytics importer** for each platform's insights API (read-only scopes),
  feeding the standard metric snapshots.

## 4. Missing information required for automation

| # | Item | Who provides | Blocks |
|---|------|--------------|--------|
| 1 | YouTube channel ID, and whether it's a Brand Account | Owner | YouTube integration |
| 2 | Instagram account type (Business / Creator) and whether a Facebook Page or business portfolio is linked | Owner | Instagram integration and login choice |
| 3 | TikTok account type (personal / business) | Owner | TikTok integration |
| 4 | Developer accounts and apps: Google Cloud project, Meta app, TikTok developer app (who owns them, under which legal entity) | Owner | All integrations |
| 5 | Secrets storage approach (secret manager, CI secrets, etc.) | Engineer proposes via ADR, owner approves | All integrations |
| 6 | Media hosting location for public media URLs | Engineer proposes, owner approves (may involve `gate:spend`) | Instagram |
| 7 | Named PolyCoffee approver and how approvals are recorded | Owner / PolyCoffee | Any product or claim content |
| 8 | Affiliation disclosure wording | PolyCoffee + owner | Any PolyCoffee mention |
| 9 | Platform priorities, formats, and cadence | Strategist (STRATEGY.md) | Pipeline design |
| 10 | Posting timezone and scheduling windows | Strategist / owner | Scheduler |
| 11 | Brand assets (logo, colors, fonts, intro/outro) | Creative-director, with owner approval | Templates and thumbnails |
| 12 | Link destination for bios (a domain, once purchased, or a link page) | Owner | Profile setup |
| 13 | Whether a qualified review of the claims policy is required, and by whom | Owner | Health or claim content |

## 5. Proposed sequence (each step its own PR or ADR)
1. Owner supplies items 1–4 and 7 (no credentials in the repo).
2. Engineer drafts an **integration ADR** covering secrets, app ownership, scopes,
   dry-run-first, and audit logging (`gate:integration`).
3. Build and test the dry-run publisher and approval check against fixtures, with
   no live calls.
4. Read-only analytics import, as the first live connection, after approval.
5. Publishing connections one platform at a time, each separately approved.
   TikTok public posting only after its audit passes.
