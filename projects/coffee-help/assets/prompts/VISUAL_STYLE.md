# Visual Style: Coffee.help (working hypothesis)

**Owner role:** creative-director (Claude) · **Status:** initial creative
hypothesis, **not** a finalized brand design system. It will be folded into
[CHANNEL.md](../../CHANNEL.md) once STRATEGY.md is accepted.
**Reference asset:** [`CH-001-S01-V04`](../manifests/CH-001-S01-V04.json), the
first selected storyboard frame (pending approval).

## Working aesthetic

> **Natural editorial photography with botanical curiosity.**

Coffee.help should look like a thoughtful independent coffee magazine: real
objects, real light, real textures. It takes coffee seriously without being
precious, and it is curious enough to surprise now and then.

| We are | We are not |
|--------|-----------|
| Warm, natural light (window light, early morning, late afternoon) | Flat studio lighting or harsh flash |
| Tactile materials: wood, ceramic, paper, linen, stone, glass | Glossy plastic, chrome, generic office desks |
| Rich coffee browns, warm ivory, and muted botanical greens, ambers, and berry tones | Neon, saturated gradients, sci-fi glows |
| Real ingredients shown truthfully (beans, cacao, spices, herbs, flowers) | Stylized "superfood" splashes or glowing particles |
| Thoughtful composition with room to breathe | Busy, cluttered, maximal frames |
| Beautiful but approachable: a kitchen counter, not a jewelry ad | Overly luxurious product styling |
| Occasional playful or unexpected moments (a surprising angle, a scale shift, a small visual joke) | Exaggerated caffeine humor (jittery eyes, "don't talk to me" memes) |
| Restrained typography, used sparingly | Excessive text overlays |

## Composition

- **Vertical 9:16 first** (Shorts, Reels, TikTok). Keep **generous negative space
  in the upper third** for titles and captions, and keep key subjects clear of
  platform UI zones (bottom fifth, right edge).
- One clear subject per frame. Use shallow depth of field to guide the eye.
- Show the steps of a process in order: bean → grind → bloom → cup.
- Keep consistent left-side window light across a sequence so scenes cut together.
- Horizontal 16:9 versions (long-form YouTube) are re-composed, not just cropped.

## Botanicals and science visuals

These rules apply the [claims policy](../../CLAIMS_POLICY.md) to imagery.
Visuals count toward a piece's content class.
- Show botanicals **as they really are**: identifiable, physically plausible, at
  realistic scale. No glowing leaves, energy auras, or "absorbing" effects.
- **No unsupported health symbolism**: no hearts, shields, brains, glowing organs,
  "immunity" halos, before/after bodies, flexed muscles, or medical props next
  to coffee or ingredients.
- Science visuals (extraction, molecules, chemistry) should be diagrammatic and
  honest, not decorative pseudo-science.
- No PolyCoffee packaging, logos, or product depictions, and no "The Daily
  Addition" branding, unless PolyCoffee approves it for a Class C piece.

## Relationship to PolyCoffee

Coffee.help is an independent educational media brand affiliated with
PolyCoffee. Its look should **complement PolyCoffee without copying its product
branding**: no shared logo treatment, no packaging look, no product-style
hero shots. A viewer should read Coffee.help as a publication, not an ad.

## Honest AI imagery

- AI-generated images are labeled per platform rules (`ai_assisted: true` on the
  content piece) and tracked in a manifest with the full prompt.
- No synthetic "experts," fake testimonials, or realistic people presented as
  real individuals. No imitation of a named photographer's, artist's, or brand's
  signature style.
- No legible fake text, labels, or logos in generated images (add real text in
  the edit instead).

## Prompt building blocks

Compose prompts from these blocks and record the final prompt verbatim in the
asset's manifest.

```
[Subject]      <what, specifically: vessel, liquid, ingredient, action>
[Setting]      <surface and place: walnut/oak table, linen, stone counter, window>
[Light]        soft natural morning light from the left | warm late-afternoon side light
[Palette]      rich coffee-brown tones, warm ivory highlights, muted botanical accents
[Materials]    tactile, handmade, subtle natural imperfections
[Mood]         intimate, curious, calm; independent coffee magazine photography
[Camera]       85mm (still life) or 35mm (scene), shallow depth of field, soft film grain
[Frame]        vertical 9:16, generous negative space in the upper third for typography
[Exclusions]   no people, no text, no logos, no packaging, no artificial-looking effects,
               no health symbolism
```

The prompt for `CH-001-S01-V04` is the reference example of these blocks.

## Review checklist (creative)

- [ ] Natural light, real materials, physically plausible
- [ ] Palette in range: coffee browns, ivory, muted botanicals
- [ ] Upper-third space and UI-safe zones respected (vertical)
- [ ] No health symbolism, pseudo-science effects, or PolyCoffee branding (unless Class C and approved)
- [ ] No fake text, people presented as real, or imitation of a named creator's style
- [ ] Manifest complete: prompt verbatim, provider, `source_category`, `rights_status`

## Open creative questions

- Typeface pairing and on-screen text style (pending CHANNEL.md).
- Whether people appear at all (hands only? never faces?). Currently: no people.
- How much playfulness, and in which pillars (e.g. Coffee Experiments vs Coffee Science).
- A motion language for video: pacing, transitions, macro shots.
