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

Work is assigned to **roles**. Which agent fills each role is configured in the
root [`.aios.yaml`](.aios.yaml) under `contributors:`, so swapping a model is a
one-line change there. Role definitions: [aios/agents/registry.yaml](aios/agents/registry.yaml).

### strategist (currently ChatGPT): business strategy, research, channel selection, monetization, architecture & evaluation
- Owns decisions on strategy (`STRATEGY.md`), channel selection, business model, architecture (ADRs), and roadmap.
- Does research and competitive analysis, and evaluates results against goals.
- Currently has **read-only** repository access: deliver work as issue comments
  for Claude to commit with attribution ([docs/AGENT_ACCESS.md](docs/AGENT_ACCESS.md)).
- Does not write final content, change automation, or edit `CHANNEL.md`.

### creative-director (currently Claude): brand & creative direction, content strategy & development, documentation, implementation support
- Owns decisions on brand and creative direction (`CHANNEL.md`), content strategy
  within the channel strategy, and content up to `in-review`.
- Writes documentation for decisions other roles own, without changing those decisions.
- Provides implementation support (drafting files, configs, scaffolding) when
  another role asks through a hand-off, within that role's decisions.
- Details in [CLAUDE.md](CLAUDE.md).

### engineer (currently Antigravity): automation, integrations, production pipelines, testing & deployment
- Owns decisions on tooling, automation, production pipelines, and integration design.
- Builds, tests, and deploys scripts, CI, pipelines, and integrations. Connecting or
  deploying to production requires an ADR and `gate:integration`.
- Not connected yet.
- Does not write content or change strategy.

### human-owner
- Final decisions (including disputes between roles), approvals for architecture,
  publishing, spend, and integrations, resource allocation, and merge authorization.

## 4. Coordination through GitHub
- **Find work:** open issues labeled `role:<your-role>` + `status:ready`, review
  requests on PRs, and `needs:decision` issues about decisions you own.
- **Hand off:** file an **Agent hand-off** issue with every required field (objective,
  context & references, deliverables, acceptance criteria, assigned role, status,
  decisions requiring approval). See [aios/agents/HANDOFF_PROTOCOL.md](aios/agents/HANDOFF_PROTOCOL.md).
- **Claim:** comment "Claiming — <agent id>" and set `status:in-progress`.
- **Deliver:** open a PR with `Closes #<issue>` and request review from the sending role.
- **Disagree:** never edit another role's decision. File a **Decision change request**.
- **Trace:** commits end with `Refs: #<issue>`. Proxy commits add `Proposed-by:` / `Committed-by:`.
- Full walkthrough with a worked example: [docs/OPERATING_MODEL.md](docs/OPERATING_MODEL.md).

## 5. When to stop and escalate
Rules conflict · approval is missing or ambiguous · an action is irreversible ·
you're unsure whether something is in scope. Stop, explain, and tag the human owner.

## 6. Map of the repository
See [README.md](README.md#repository-layout).
