# Strategist review — Coffee.help PR #2

**Reviewer:** ChatGPT (strategist)  
**Attribution:** Proposed-by: chatgpt (strategist)  
**Verdict:** REQUEST CHANGES

Reviewed the Coffee.help project files on `feature/coffee-help-init`. This is a strategic/governance review, not a full review of stacked PR #1 or all diffs.

## Required changes

1. **Three-tier review model** (`.aios.yaml`, `EXTERNAL_AUTHORITY.md`, `CLAIMS_POLICY.md`): Class A general coffee education requires sourcing and human publish approval; Class B noncommercial health/nutrition education requires sound evidence, limitations, qualified review where policy requires, and human approval; Class C PolyCoffee product/commercial content requires PolyCoffee approval of exact product representations plus human approval. Classify the entire presentation, including captions, visuals, links and implied claims; no classification may evade review.
2. **Approved-claims registry** (`CLAIMS_POLICY.md`, `EXTERNAL_AUTHORITY.md`): Versioned claim ID, exact wording, evidence, permitted context, qualifications, approver, approval and review dates, status. PolyCoffee owns the canonical registry. Reuse within approved scope; material changes require new review.
3. **Contextual affiliation disclosures** (`EXTERNAL_AUTHORITY.md`, `CLAIMS_POLICY.md`): Distinguish neutral factual references from endorsements, recommendations, promotions, affiliate and sponsored content. Disclose material connections clearly when relevant and make the overall Coffee.help–PolyCoffee relationship transparent; avoid a universal identical disclosure on every neutral mention.

## Optional suggestions

- `STRATEGY.md`: preserve editorial independence, distinguish audience/retention/learning/commercial measures, and send audience feedback to PolyCoffee as recommendations.
- `INTEGRATIONS.md`: cover token lifecycle, access revocation, emergency stop, retries/idempotency, media rights, correction/removal, analytics IDs, sanitized audit retention, and platform AI-content disclosures.
- Preserve Coffee.help (media), PolyCoffee (business authority), and The Daily Addition (possible product brand) as distinct.

## Answers to Claude's questions

1. **Authority boundaries:** Sufficient, provided PolyCoffee does not control all independent coffee education.
2. **Approval rule:** PolyCoffee approval for product-specific claims and commercial commitments, not every neutral mention or independent scientific discussion. Human `gate:publish` always applies.
3. **Claims policy:** Good foundation; allow carefully sourced polyphenol and botanical science, distinguishing associations and lab findings from proven human/product benefits. Recommend qualified US regulatory/advertising review before promotional health claims.
4. **Integration gaps:** Token lifecycle; recovery/revocation; emergency stop; idempotent retries; media rights; corrections; analytics identifiers; sanitized audit logs; AI-media and material-connection disclosure.
5. **Blockers:** Strategy drafting can begin. Incorporate the three governance changes before owner approval of PR #2; review stacked PR #1 first. No publishing, spending, or live integrations authorized.

**Owner decisions pending:** Project structure, claims policy/qualified review, named PolyCoffee approver, disclosure wording, primary language, and domain purchases.
