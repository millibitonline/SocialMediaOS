# Operating Model: How Agents Collaborate Through GitHub

SocialMediaOS uses GitHub for two different things:

1. **Shared source of truth**: what is decided, built, and approved. This works
   today for every contributor that can read the repository.
2. **Agent communication system**: how contributors find work, hand it off,
   and review each other. This needs every agent to have the right GitHub
   permissions and a way to notice new work.

We start with **manual coordination** (Phase 1) and automate it later (Phase 2).
See [ADR-0002](adr/0002-github-as-agent-coordination-layer.md).

## The building blocks

| GitHub object | Used for | Example |
|---------------|----------|---------|
| **Issue** | A task or a hand-off between roles | "[handoff] Creative direction for travel-lava" |
| **Pull request** | A proposed change that needs review | `feature/travel-lava-creative` → `main` |
| **Markdown document** | Architecture, strategy, creative direction, decisions | `projects/travel-lava/STRATEGY.md` |
| **ADR** | A significant or structural decision | `docs/adr/0002-…` |
| **Agent instructions** | What each role does and may touch | `AGENTS.md`, `CLAUDE.md`, `aios/agents/registry.yaml` |
| **Comments, commits, reviews** | Conversation attached to the work | "Claiming", review notes, "Closes #4" |

## Roles are configurable

Work is assigned to **roles**, not models. The current bindings live in one place,
the root [`.aios.yaml`](../.aios.yaml) under `contributors:`:

| Role | Currently bound to | Owns |
|------|--------------------|------|
| strategist | ChatGPT | Strategy, business models, research, architecture, evaluation |
| creative-director | Claude | Creative direction, content development, documentation, implementation support |
| engineer | Antigravity | Engineering, automation, integrations, testing |
| human-owner | @millibitonline | Approvals, merges, conflict resolution |

To move a role to a different agent, change its `contributors:` entry in a PR.
Labels, issue forms, and docs all refer to roles, so nothing else changes.

## How agents work

### 1. Discover work
An agent starting a session looks, in order, at:
1. Open issues labeled `role:<my-role>` + `status:ready` (new hand-offs).
2. Open issues labeled `role:<my-role>` + `status:in-progress` that it already claimed.
3. PRs where its role was asked to review.
4. Issues labeled `needs:decision` about decisions its role owns.

In **Phase 1** the human owner starts each agent session and points it at the
issue or PR. In **Phase 2** agents poll or receive these through automation.

### 2. Claim and contribute
- Comment "Claiming — <agent id>" and switch the label to `status:in-progress`.
- Create a branch `<type>/<project>-<topic>` (e.g. `feature/travel-lava-creative`).
- Read the inheritance chain (`.aios.yaml` files) and the context the issue links.
- Change only paths your role may write (`aios/agents/registry.yaml`).
- Run `python scripts/validate_aios.py`.

### 3. Request review
- Open a PR with `Closes #<issue>`. Fill in the template's "Decisions" section.
- Set the issue to `status:in-review`.
- Ask for review from the role that sent the hand-off, plus the human owner if a
  gate applies. In Phase 1, the human owner relays the review request to the
  other agent.

### 4. Hand off
- File a new **Agent hand-off** issue for the next role, with every required
  field (see [HANDOFF_PROTOCOL.md](../aios/agents/HANDOFF_PROTOCOL.md)).
- Link it from the PR so the chain stays visible.

### 5. Disagree without overriding
- Don't edit a decision another role owns. File a **Decision change request**
  issue to that role. The owning role decides, and the human owner settles disputes.

## Worked example: launching travel-lava

This is the intended flow. The example content is illustrative; nothing below has
been decided.

### Step 1: The owner starts the strategy hand-off
The human owner files issue **#2** using the *Agent hand-off* form:

> **From:** human-owner · **Assigned role:** strategist
> **Objective:** Define travel-lava's channel strategy.
> **Context:** `projects/travel-lava/STRATEGY.md` (template), `organization/capabilities/analytics/CAPABILITY.md` (metrics), launch playbook Phase 1.
> **Deliverables:** completed `projects/travel-lava/STRATEGY.md`.
> **Acceptance criteria:** positioning, audience, 1–3 platforms with rationale, 90-day targets using standard metrics, monetization hypothesis.
> **Status:** ready
> **Decisions requiring approval:** platform choice and monetization model, human owner.

Labels: `handoff`, `role:strategist`, `status:ready`.

### Step 2: ChatGPT (strategist) defines the strategy
1. ChatGPT comments "Claiming — chatgpt" and sets `status:in-progress`.
2. On branch `feature/travel-lava-strategy` it researches and fills `STRATEGY.md`.
3. It opens PR **#3**, "Closes #2", listing *platform choice* and *monetization* as
   decisions needing owner approval.
4. The owner reviews and approves. PR #3 merges and issue #2 closes. The strategy
   is now a recorded decision **owned by the strategist**.
5. ChatGPT files hand-off **#4** to `creative-director`: objective "creative
   direction for travel-lava", context = merged `STRATEGY.md`, deliverables =
   `CHANNEL.md` + a 4-week calendar + 6–10 seed ideas, decisions needing approval
   = "visual identity (human owner)".

### Step 3: Claude (creative director) develops the creative direction
1. Claude claims #4 and works on `feature/travel-lava-creative`.
2. It writes `CHANNEL.md` (voice, visuals, pillars, series), the editorial
   calendar in the feature's `FEATURE.md`, and seed ideas in `content/ideas/`,
   all citing `STRATEGY.md` instead of restating it.
3. Claude thinks one platform in the strategy suits the format poorly. It does
   **not** change `STRATEGY.md`. It files a *Decision change request* (#5) to the
   strategist and continues on the rest.
4. Claude opens PR **#6**, "Closes #4", and requests review from the strategist
   (alignment with strategy) and the owner (visual identity).
5. ChatGPT reviews #6 and answers #5 (it accepts and opens a small PR to
   `STRATEGY.md`, or it declines with a reason). The owner approves and merges #6.
6. Claude files hand-off **#7** to `engineer`: objective "automate the travel-lava
   content pipeline up to the publish gate", context = `CHANNEL.md`, content
   front-matter spec, publishing capability, deliverables listed below, decisions
   needing approval = "any production connection (human owner, `gate:integration`)".

### Step 4: Antigravity (engineer) implements the production automation
1. Antigravity claims #7 and works on `feature/travel-lava-pipeline`.
2. It builds, with tests:
   - a CI check that validates content front matter and stage moves,
   - a dry-run publisher that renders the exact post payload for each `approved/`
     file without sending it,
   - an analytics snapshot importer that runs manually for now.
3. It drafts **ADR-0003** for platform connections and a secrets approach, labeled
   `gate:integration`, *without* connecting anything.
4. It opens PR **#8**, "Closes #7". The owner reviews, merges the dry-run tooling,
   and decides on ADR-0003 separately.
5. Only after ADR-0003 is accepted and `gate:integration` approved does
   `integrations.production_enabled` change, through its own PR. Each post still
   needs `gate:publish`.

### What the owner sees
Every step is an issue, a PR, or a commit. The owner can trace any decision to
the hand-off that requested it, the PR that made it, and the approval that
accepted it.

## Phase 1 vs Phase 2

| | Phase 1: Manual (now) | Phase 2: Automated (after ADR) |
|-|-----------------------|--------------------------------|
| Work discovery | Owner opens an agent session and points to the issue | Agents query issues by label, or automation notifies them |
| Agent write access | Agents with repo access push branches; others hand their output to an agent or the owner to commit | Each agent has its own scoped GitHub identity |
| Review requests | Owner relays between agents | Automation assigns reviewers by role |
| Labels | Applied by hand | Synced from `.github/labels.yml`; statuses updated by automation |
| Publishing | Manual, after `gate:publish` | Still gated. Automation only does the action after approval |
