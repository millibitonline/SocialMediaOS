# Claims Policy: Coffee.help

**Owner role:** creative-director (editorial standards) · **Status:** draft (revision 2, incorporating the strategist review), pending owner approval
**Applies to:** every content piece, including captions, titles, thumbnails, on-screen
text, voice-over, visuals, links, bios, and pinned comments.

Coffee.help covers coffee science, polyphenols, and botanical ingredients, so it
works close to health territory. The default is **education, not health promises**.

> This policy is an editorial standard, not legal advice. Before any
> **promotional** health or nutrition claim, have someone qualified review this
> policy and the claim against the rules in the target markets (e.g. FTC and FDA
> in the US). Whether to also review Class B content is an owner decision (§2).

## 1. Never publish (any class)
- **Disease claims:** that coffee, a polyphenol, a botanical, or any product
  prevents, treats, cures, or mitigates a disease or condition.
- **Unsubstantiated health claims**, including implied ones ("detox", "boosts
  immunity", "burns fat", "anti-aging") and before/after framing.
- **Medical advice** or individual dosing guidance ("drink X cups for Y").
- **Product representations about PolyCoffee products** that aren't in the
  approved-claims registry (§3) within their approved scope.
- **Fabricated or misattributed** studies, experts, quotes, testimonials, or reviews.

## 2. Content classes (three-tier review)

Every piece declares `content_class: A | B | C` in its front matter.

| Class | What it is | Requirements before `gate:publish` |
|-------|-----------|------------------------------------|
| **A: General coffee education** | Culture, brewing, flavor, rituals, history, sensory and chemistry topics with no health/nutrition outcome and no commercial content | Every factual claim sourced (Sources & rights); the owner's `gate:publish` approval |
| **B: Non-commercial health/nutrition education** | Discusses health, nutrition, or physiological effects (e.g. polyphenol research, caffeine and sleep) with no product, promotion, or commercial call to action | All of Class A, plus: sound evidence (§4); limitations stated; associations not presented as causes; lab/animal findings not presented as human outcomes; "educational, not medical advice" note; qualified review **where the owner's policy requires it** (default: recommended, not required, until the owner decides); owner approval |
| **C: PolyCoffee product / commercial** | Mentions a PolyCoffee product in an endorsing, recommending, or promotional way; makes a product representation; includes offers, pricing, availability, links to buy, affiliate or sponsored elements | All applicable Class A/B requirements, plus: every product representation matches an **approved registry claim** (§3) used within its permitted context; **PolyCoffee approval** of the exact product representations in this piece; contextual disclosure (§5); qualified review for any health or nutrition representation; owner approval |

### Classification rules
- **Classify the whole presentation:** script, captions, visuals, music cues,
  links, hashtags, and what a reasonable viewer would take away, including
  **implied claims**.
- **Mixed content takes the highest class present.** A Class A brewing video with a
  link to buy a PolyCoffee product is Class C.
- **When unsure, choose the higher class.** Reviewers may raise a class. Only the
  owner may lower one, with a reason in the PR.
- **No classification may be used to avoid review.** Splitting a claim across a
  video and its caption, or moving a claim into a pinned comment or link, does not
  change the class.

## 3. Approved-claims registry

**Canonical owner:** PolyCoffee keeps the canonical registry of approved product
claims. SocialMediaOS keeps a read-only **mirror** at
[`claims/APPROVED_CLAIMS.yaml`](claims/APPROVED_CLAIMS.yaml) so reviewers and
agents can check claims in the repo. When the two differ, PolyCoffee's canonical
registry wins, and the mirror is corrected by PR.

Each entry records:

| Field | Meaning |
|-------|---------|
| `id` + `version` | Stable claim ID (e.g. `CLM-0001`) and version (`v1`, `v2`, …) |
| `exact_wording` | The approved wording, verbatim |
| `evidence` | References that substantiate it |
| `permitted_context` | Platforms, formats, content classes, and audiences where it may be used |
| `qualifications` | Required qualifiers, disclaimers, or adjacent wording |
| `approver` | Named PolyCoffee approver (plus qualified reviewer, if any) |
| `approved_at` / `review_by` | Approval date and next review date |
| `status` | `draft`, `approved`, `suspended`, `retired`, or `superseded` |
| `supersedes` | Previous version, if any |

**Reuse:** an `approved` claim may be reused verbatim within its
`permitted_context` and before its `review_by` date, without new PolyCoffee
approval of the claim itself. Content cites it as `claim_ids: [CLM-0001@v1]`. The
piece still needs owner approval, and PolyCoffee approval of the overall product
presentation when the piece is Class C.

**Material changes need new review:** different wording that changes meaning, a
new context or platform, a stronger qualifier-free form, new evidence, or an
expired `review_by` date. Each produces a new version that goes through approval
again. Expired, suspended, or retired claims may not be used.

## 4. Evidence standards (Classes A–C)
- Each factual claim cites a source in **Sources & rights**. Prefer peer-reviewed
  research, systematic reviews, or authoritative bodies.
- Wording matches the strength of the evidence ("a 2024 study of N adults
  found…", not "science proves…").
- Polyphenol and botanical science is welcome when it is sourced carefully and keeps
  three things distinct: **associations** (observational), **lab/animal findings**,
  and **demonstrated human outcomes**. None of them is a demonstrated benefit of a
  specific product unless it is an approved registry claim.
- State the limits that matter: sample size, dose, population, study duration, funding.

## 5. Disclosures (contextual)

Disclosure depends on what the content is doing. It is not one identical label
on every mention.

| Situation | Disclosure |
|-----------|-----------|
| **Channel-level transparency** (always) | The Coffee.help–PolyCoffee relationship is stated plainly in profile bios / About sections on every platform and on the website when it exists. The wording is agreed with PolyCoffee. |
| **Neutral factual reference**: PolyCoffee named as context or a source, with no endorsement, recommendation, or call to action | Channel-level transparency is enough. Add an in-content note if a viewer could reasonably read the mention as an endorsement. |
| **Endorsement, recommendation, review, or comparison** involving a PolyCoffee product | A clear in-content disclosure of the material connection, close to the claim, in the same medium (spoken in video, on-screen, and in the caption) |
| **Promotion, offer, launch, link to buy** | In-content disclosure, plus the platform's branded-content or paid-partnership tools where they apply |
| **Affiliate or sponsored content** (any brand) | Labeled per organization rules and platform tools, and the material connection disclosed |
| **AI-assisted media** | Per platform AI-content disclosure rules (organization default) |

When unsure whether a mention is neutral, treat it as an endorsement and disclose.

## 6. Review checklist (every Coffee.help content PR)
- [ ] `content_class` set; whole presentation (captions, visuals, links, implied claims) considered
- [ ] No disease, cure, or treatment language, explicit or implied
- [ ] Every factual claim sourced, and the wording matches the evidence
- [ ] Class B: limitations and "not medical advice" note present; qualified review done if required
- [ ] Class C: every product representation maps to an `approved` registry claim within context (`claim_ids` listed); PolyCoffee approval recorded
- [ ] Disclosures match §5 for each mention
- [ ] AI disclosure present where required
