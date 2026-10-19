# Capability: Financial Reporting

**Lead role:** strategist (analysis) · engineer (data format) · **Status:** defined, manual entry

## Contract
Tracks revenue and cost per channel so the organization can see channel-level
profit and loss. Any action that **commits** money remains gated by `gate:spend`;
this capability only **records**.

## Ledger
One append-only file per channel per month:
`projects/<channel>/reports/finance/YYYY-MM.yaml` following
[`ledger.template.yaml`](ledger.template.yaml).

Categories:
- **Revenue:** platform payouts, sponsorships, affiliate, merchandise, other.
- **Cost:** tools/subscriptions, assets/licensing, paid promotion, contractors, other.

## Monthly report
Strategist produces `projects/<channel>/reports/finance/YYYY-MM-summary.md`:
revenue, cost, net, month-over-month change, and notes. An organization-wide
roll-up lives in `organization/reports/` (created when the second channel goes live).

## Privacy
Record amounts and counterparties at the business level only. No bank or card
numbers, no personal financial data, no tax IDs in the repository.
