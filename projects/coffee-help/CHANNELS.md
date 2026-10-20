# Social Channel Registry: Coffee.help

**Source of truth for identities:** this file and `.aios.yaml` → `channel.handles` / `channel.domains`.
Keep both in the same PR whenever anything changes.

## Social accounts

| Platform | Handle | URL | Account status | Connected to automation | Account type | Notes |
|----------|--------|-----|----------------|-------------------------|--------------|-------|
| YouTube | @getcoffeehelp | https://www.youtube.com/@getcoffeehelp | **Secured** (confirmed by owner, 2026-10-19) | No | TBD (personal channel vs. Brand Account) | Channel ID not yet recorded |
| Instagram | @getcoffeehelp | https://www.instagram.com/getcoffeehelp/ | **Secured** (confirmed by owner, 2026-10-19) | No | TBD (must be a professional account for API publishing) | |
| TikTok | @getcoffeehelp | https://www.tiktok.com/@getcoffeehelp | **Secured** (confirmed by owner, 2026-10-19) | No | TBD (personal vs. business account) | |

**Status values:** `planned` → `secured` (owner controls the account) → `connected` (an
approved integration exists, by ADR + `gate:integration`) → `active` (publishing under `gate:publish`).

## Domains

| Domain | Status | Notes |
|--------|--------|-------|
| coffee.help | **Purchased** (owner confirmed 2026-10-20) | Domain secured; hosting and website launch not yet confirmed. |
| getcoffeehelp.com | **Planned** (not purchased) | Same as above. |

## Rules
- The human owner holds all account credentials. **No credentials, recovery
  codes, tokens, or account emails are stored in this repository.**
- Agents never log in to, connect, or post from these accounts.
- Changing a handle, adding a platform, or changing a status is a PR that the
  owner approves.
- Bios, profile images, and links on these accounts are channel content. They go
  through the content pipeline and `gate:publish` before changing.
