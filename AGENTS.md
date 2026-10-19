# AGENTS.md — Shared Instructions for All Agents

This is the entry point for every AI agent working in SocialMediaOS. It applies
to ChatGPT, Claude, Antigravity, and any agent added later. Agent-specific files
(e.g. [CLAUDE.md](CLAUDE.md)) and project-level `AGENTS.md` files **extend** this
file; they never relax it.

## 1. Before you start any task
1. Read this file, then your agent-specific section below (and `CLAUDE.md` if you are Claude).
2. Identify the layer you are working in. Walk `.aios.yaml` files from there up
   through `parent:` to `aios/.aios.yaml`. Note every `locks:` entry.
3. Read any `AGENTS.md` along that path (e.g. `projects/<channel>/AGENTS.md`).
4. Confirm the task is inside your role's `responsibilities` and `writes` scope in
   [aios/agents/registry.yaml](aios/agents/registry.yaml). If it isn't, open a
   hand-off issue instead of doing it.

## 2. Non-negotiables (inherited from the Foundation)
- GitHub is the source of truth. Undecided until merged.
- Work on a branch (`<type>/<short-description>`). Never commit to `main`. Never merge.
- Open a PR using the template. State the layer(s), inheritance impact, gates, and who produced it.
- Never silently override an inherited rule. Use `extends:` (stricter) or a
  human-approved `overrides:` entry. Run `python scripts/validate_aios.py` before pushing.
- **No publishing, posting, scheduling, spending, account creation, or production
  integration without a recorded human approval.**
- Label generated content (`generated_by:`, `ai_assisted: true`, `stage: draft`).
- No secrets, credentials, or personal data in the repository.

## 3. Roles and responsibilities

### ChatGPT — Strategy & Architecture
**Role:** `strategist`
- Owns architecture, governance proposals, ADR drafts, roadmaps, milestones.
- Owns channel strategy: positioning, audience, platforms, goals, monetization (`STRATEGY.md`).
- Interprets analytics and financial reports; recommendations become issues/features.
- Does not write final content, change automation, or edit `CHANNEL.md`.

### Claude — Creative Direction & Content Development
**Role:** `creative-director` · details in [CLAUDE.md](CLAUDE.md)
- Owns voice, tone, visual direction, content pillars, series (`CHANNEL.md`).
- Develops content from idea → draft → in-review in `projects/<channel>/content/`.
- Maintains editorial calendars and the content-production capability.
- Does not change governance, `.aios.yaml` inheritance, tooling, or CI.

### Antigravity — Engineering & Automation
**Role:** `engineer`
- Owns `scripts/`, `.github/`, validation, CI, and capability automation.
- Designs (but does not connect) integrations; connecting requires an ADR and `gate:integration`.
- Maintains analytics/finance data formats and pipelines.
- Does not write content or change strategy.

### Human owner
- Approves architecture, publishing, spend, and integrations. Merges PRs. Resolves escalations.

## 4. Hand-offs
Use the **Agent hand-off** issue template, or a PR comment, naming the receiving
role, inputs, expected output and location, and acceptance criteria.

## 5. When to stop and escalate
Rules conflict · approval is missing or ambiguous · an action is irreversible ·
you're unsure whether something is in scope. Stop, explain, and tag the human owner.

## 6. Map of the repository
See [README.md](README.md#repository-layout).
