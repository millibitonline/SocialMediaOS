# Claims Policy: Coffee.help

**Owner role:** creative-director (editorial standards) · **Status:** draft, pending owner approval
**Applies to:** every content piece, caption, bio, thumbnail, and on-screen text.

Coffee.help covers coffee science, polyphenols, and botanical ingredients, so it
is close to health territory. The default is **education, not health promises**.

> This policy is an editorial standard, not legal advice. Before the first
> publication that touches health, nutrition, or product claims, have someone
> qualified review this policy and the relevant rules in the target markets
> (e.g. FTC and FDA in the US). That review is an open decision for the owner.

## 1. Never publish
- **Disease claims:** that coffee, a polyphenol, a botanical, or any product
  prevents, treats, cures, or mitigates a disease or condition.
- **Unsubstantiated health claims**, including implied ones ("detox", "boosts
  immunity", "burns fat", "anti-aging") and before/after framing.
- **Medical advice** or dosing guidance ("drink X cups for Y").
- **Product claims about PolyCoffee products** that PolyCoffee has not approved in
  writing (see [EXTERNAL_AUTHORITY.md](EXTERNAL_AUTHORITY.md)).
- **Fabricated or misattributed** studies, experts, quotes, testimonials, or reviews.

## 2. Allowed with substantiation
Factual statements about coffee chemistry, sensory science, brewing, and
research findings are allowed when:
- each factual claim cites a source in the piece's **Sources & rights** section
  (prefer peer-reviewed research, systematic reviews, or authoritative bodies),
- the wording matches the strength of the evidence ("a 2024 study of N people
  found…", not "science proves…"),
- associations are not presented as causes, and lab or animal results are not
  presented as human outcomes,
- limits are stated where they matter (sample size, dose, population).

## 3. Product, health, and nutrition claims
Anything that is a health or nutrition claim, or that refers to a PolyCoffee
product, is marked `claims: true` in the content front matter and needs:
1. sources for every claim,
2. **PolyCoffee approval** of the exact wording,
3. the owner's `gate:publish` approval.

## 4. Disclosures
- **Affiliation:** disclose the PolyCoffee affiliation on every PolyCoffee mention.
- **AI assistance:** follow each platform's AI-content disclosure rules
  (organization default).
- **Sponsored or affiliate content:** labeled per organization rules.
- **Educational framing:** where a piece discusses health research, include a
  short "educational, not medical advice" note.

## 5. Review checklist (for every Coffee.help PR)
- [ ] No disease, cure, or treatment language, explicit or implied
- [ ] Every factual claim has a source, and the wording matches the evidence
- [ ] `claims:` front matter set correctly
- [ ] PolyCoffee approval recorded if there is a product mention or a claim
- [ ] Affiliation and AI disclosures present where required
