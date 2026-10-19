# AIOS Agent Standards

**Layer:** Foundation · **Status:** Locked

These standards apply to every AI agent contributing to any AIOS implementation.
They are tool- and vendor-neutral; organizations bind specific agents to roles in
their own configuration.

## 1. Registration
- Every agent that commits, comments, or reviews must be registered in
  `aios/agents/registry.yaml` (role definitions) and bound to a role in the
  Organization's `.aios.yaml` under `contributors:`.
- Unregistered agents may read the repository but may not open PRs.

## 2. Discovery
On starting any task, an agent must:
1. Read the root `AGENTS.md`, then its agent-specific file if one exists
   (e.g. `CLAUDE.md`).
2. Identify the layer it is working in and read every `.aios.yaml` from that layer
   up to `aios/.aios.yaml` (follow `parent:`).
3. Read any `AGENTS.md` it finds along that path — nearer files extend, never
   replace, farther ones.
4. Confirm the task falls inside its role's `responsibilities`. If not, stop and
   propose a hand-off.

Agents discover work through GitHub: open issues labeled `role:<their-role>` and
`status:ready`, review requests on PRs, and comments that mention their role.

## 3. Conduct
- **Work in branches.** Never commit to `main`. Never merge.
- **Stay in lane.** Only modify paths your role's `writes` scope allows. Other paths
  get an issue or a PR comment, not an edit.
- **Declare, don't override.** If a task seems to require breaking an inherited rule,
  stop and raise it; don't work around it.
- **Leave a trail.** Every PR description states: what changed, which layer(s), why,
  open questions, and which agent/model produced it.
- **Label generated content.** Generated drafts carry `generated_by:` and
  `status: draft` metadata until a human approves them.
- **No secrets.** Never write credentials, tokens, or personal data into the
  repository.
- **No external side effects without a gate.** Publishing, messaging, spending,
  and connecting integrations require a recorded human approval
  ([../governance/APPROVALS.md](../governance/APPROVALS.md)).

## 4. Hand-offs and ownership
Hand-offs follow [HANDOFF_PROTOCOL.md](HANDOFF_PROTOCOL.md): a GitHub Issue with
objective, context & references, deliverables, acceptance criteria, assigned
role, status, and decisions requiring approval.

Each decision has one owning role (`owns_decisions` in the registry). Agents never
edit another role's decision; they propose the change through a hand-off labeled
`needs:decision`.

## 5. Escalation
Agents escalate to a human Owner when: rules conflict, an approval is ambiguous, a
task requires an irreversible action, or the agent is uncertain whether an action
is in scope.
