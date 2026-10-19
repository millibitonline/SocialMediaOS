# AIOS Hand-off Protocol

**Layer:** Foundation · **Status:** Locked (changes require a Foundation ADR)

A **hand-off** transfers a unit of work from one contributor to another. In AIOS
every hand-off is an **issue** in the organization's git forge, created from the
*Agent hand-off* form, so
that it is visible, versioned, and reviewable. Nothing is handed off in chat.

## 1. Required fields

| Field | What it contains |
|-------|------------------|
| **Objective** | One or two sentences: the outcome wanted, not the method. |
| **Context & references** | Links to the files, ADRs, issues, and PRs the receiver must read. |
| **Deliverables** | Each artifact to produce, with its path in the repository. |
| **Acceptance criteria** | Checkable statements the reviewer will use to accept the work. |
| **Assigned role** | The receiving role (`strategist`, `creative-director`, `engineer`, `human-owner`). The agent bound to that role picks it up. |
| **Status** | One of the statuses below, kept current via labels. |
| **Decisions requiring approval** | Every decision in scope that needs a human or another role's sign-off, with who must approve. "None" is a valid answer and must be stated. |

An issue missing any field is not a valid hand-off; the receiver comments asking
for it and leaves the status at `status:blocked`.

## 2. Statuses (labels)

```
status:ready → status:in-progress → status:in-review → status:done
                     ↘ status:blocked ↗
```

| Label | Meaning | Who sets it |
|-------|---------|-------------|
| `status:ready` | Complete hand-off, waiting for the assignee | sender |
| `status:in-progress` | Assignee has claimed it (comment + label) | assignee |
| `status:blocked` | Waiting on information, a decision, or another issue | anyone, with a comment saying on what |
| `status:in-review` | A PR referencing the issue is open | assignee |
| `status:done` | PR merged; issue closed by the merge | automatic / human |

Routing labels: `role:strategist`, `role:creative-director`, `role:engineer`,
`role:human-owner`. Approval labels: `needs:approval`, `gate:<name>`.

## 3. Lifecycle

1. **Open.** Sender files the issue with all fields, labels `role:<receiver>` and
   `status:ready`.
2. **Claim.** Receiver comments "Claiming" (with its agent id), swaps to
   `status:in-progress`. One claimant at a time.
3. **Clarify.** Questions go in issue comments. If the answer changes scope, the
   sender edits the issue body (the history keeps the original).
4. **Deliver.** Receiver opens a PR whose description says `Closes #<issue>`,
   sets `status:in-review`, and requests review from the sender's role (and the
   human owner where a gate applies).
5. **Accept.** The sender's role reviews against the acceptance criteria. A human
   merges. The issue closes.

## 4. Ownership and no silent overrides

- Each decision has exactly one **owning role** (`owns_decisions` in
  `aios/agents/registry.yaml`). The owner of a decision is the only role that
  changes it.
- A contributor who disagrees with another role's decision **does not edit it**.
  They open a hand-off to the owning role labeled `needs:decision`, stating the
  proposed change and why. The owning role accepts, declines, or escalates.
- A PR that changes a file belonging to another role's decision must say so in
  its description and request that role's review. Reviewers reject PRs that
  change another role's decision without that hand-off.
- Conflicts the two roles cannot settle go to the human owner, whose ruling is
  recorded in the issue (and in an ADR if structural).
- Accepted decisions are recorded where they live (STRATEGY.md, CHANNEL.md, an
  ADR); later work cites them rather than restating them.

## 5. Decisions requiring approval

| Decision type | Approver |
|---------------|----------|
| Architecture / governance / hierarchy | human owner (`gate:architecture`) + ADR |
| Publishing anything | human owner (`gate:publish`) |
| Spending money | human owner (`gate:spend`) |
| Connecting a production system | human owner (`gate:integration`) + ADR |
| Changing another role's decision | owning role; human owner if disputed |
