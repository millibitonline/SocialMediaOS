# External Business Authority: PolyCoffee

Coffee.help is affiliated with **PolyCoffee**, an independent coffee
product-development business.

## Brand separation
These are distinct and must not be conflated in content, configuration, or claims:

| Name | What it is | Authority |
|------|-----------|-----------|
| **Coffee.help** | Educational media brand (this project) | SocialMediaOS: social strategy, creative, distribution, analytics |
| **PolyCoffee** | Coffee product-development business | Product strategy, formulation, sourcing, pricing, commercialization, product claims |
| **The Daily Addition** | Proposed consumer-facing PolyCoffee product brand. **Not finalized** (owner-approved business brief, 2026-10-20). No product names or formulations approved for commercial use. | PolyCoffee. Coffee.help content does not reference it until PolyCoffee finalizes it and approves its use (Class C). |

## Who decides what

| Area | Decided by | SocialMediaOS role |
|------|-----------|--------------------|
| Product strategy | **PolyCoffee** | None. References only what PolyCoffee has approved for public use. |
| Formulation | **PolyCoffee** | None. Never describes ingredients, ratios, or processes beyond approved claims. |
| Sourcing | **PolyCoffee** | None. Never describes suppliers or origins of PolyCoffee ingredients beyond approved claims. |
| Pricing | **PolyCoffee** | None. Never states or implies prices, discounts, or offers without approval. |
| Commercialization (launches, availability, partnerships, sales) | **PolyCoffee** | None. Never announces or implies availability or commercial commitments. |
| Product claims | **PolyCoffee** (owns the canonical approved-claims registry) | Uses only approved registry claims within their permitted context |
| Independent coffee education (Class A/B) | **SocialMediaOS** (strategist and creative-director), with owner approval | Owns it. PolyCoffee does not control independent coffee education. |
| Social strategy, positioning on social | SocialMediaOS: strategist | Owns it, within the limits above |
| Creative direction, editorial standards, content | SocialMediaOS: creative-director | Owns it, within the limits above |
| Distribution, publishing infrastructure, analytics | SocialMediaOS: engineer | Owns it (no live connections yet) |
| Final approval to publish | SocialMediaOS: human owner (`gate:publish`) | Always required |

### Editorial independence
Coffee.help's independent education is decided by SocialMediaOS and the owner,
not by PolyCoffee. Coffee.help may cover coffee science, other producers, and
research that doesn't favor PolyCoffee's products. Audience feedback and insights
about products go to PolyCoffee as **recommendations**, never as product
decisions.

## Approval routing (by content class)

Content classes are defined in [CLAIMS_POLICY.md §2](CLAIMS_POLICY.md#2-content-classes-three-tier-review).

| Class | PolyCoffee approval | Owner `gate:publish` |
|-------|---------------------|----------------------|
| **A**: general coffee education | Not required | Required |
| **B**: non-commercial health/nutrition education | Not required (qualified review per owner policy) | Required |
| **C**: PolyCoffee product / commercial | **Required** for the exact product representations and any commercial commitment. Every product claim must be an approved registry claim within its context. | Required |

A neutral factual reference to PolyCoffee (named as context, with no endorsement,
recommendation, or call to action) doesn't make a piece Class C. If a viewer could
reasonably take the mention as an endorsement, it is Class C.

**Recording PolyCoffee approval:** a review comment on the content PR from the
named PolyCoffee approver, or an approval-log entry naming them and the commit SHA
(per `aios/governance/APPROVALS.md`). Approved product claims are added to the
registry mirror (`claims/APPROVED_CLAIMS.yaml`) from PolyCoffee's canonical
registry.

## Disclosure
Disclosure depends on context ([CLAIMS_POLICY.md §5](CLAIMS_POLICY.md#5-disclosures-contextual)):
- The overall Coffee.help–PolyCoffee relationship is stated openly at channel level
  (bios / About sections, website).
- Endorsements, recommendations, promotions, and affiliate or sponsored content
  disclose the material connection clearly, in the content itself.
- Neutral factual references rely on channel-level transparency, unless they could
  reasonably be read as an endorsement.

## Open items
- Who is the named PolyCoffee approver, and how do they record approvals (forge
  account, or a written approval the owner commits)?
- Where PolyCoffee keeps the canonical approved-claims registry, and how the mirror is synced.
- The exact nature of the affiliation to disclose (ownership, sponsorship, shared
  founders, etc.) and the channel-level wording.
- ~~Confirm or remove The Daily Addition~~: confirmed as a proposed, not-finalized brand in [POLYCOFFEE_BUSINESS_BRIEF.md](POLYCOFFEE_BUSINESS_BRIEF.md).
