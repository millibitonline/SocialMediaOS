# Agent Instructions — Coffee.help

This file **extends** the root [AGENTS.md](../../AGENTS.md). It adds
channel-specific guidance. It does not relax anything above it.

## Read before working here
1. [`.aios.yaml`](.aios.yaml): effective config, channel identities, external authority
2. [`EXTERNAL_AUTHORITY.md`](EXTERNAL_AUTHORITY.md): what PolyCoffee decides
3. [`CLAIMS_POLICY.md`](CLAIMS_POLICY.md): health, nutrition, and product claim rules
4. [`features/channel-launch/FEATURE.md`](features/channel-launch/FEATURE.md): current phase
5. [`STRATEGY.md`](STRATEGY.md) and [`CHANNEL.md`](CHANNEL.md)

## Current phase: 1 (Strategy)

### strategist (ChatGPT)
- Owns the next deliverable, STRATEGY.md.
- Research and positioning stay within PolyCoffee's authority. Don't set product
  strategy, pricing, or commercialization.

### creative-director (Claude)
- Owns editorial standards (CLAIMS_POLICY.md) and, after strategy, CHANNEL.md.
- No content drafts until STRATEGY.md is merged and generation is authorized.

### engineer (Antigravity)
- Owns INTEGRATIONS.md.
- No account connections, live publishing, or spending.
- Integration work starts with an ADR.

### Everyone
- Never log in to, connect, or post from @getcoffeehelp accounts.
- Never store credentials in the repository.
- Never write a health claim or a PolyCoffee product claim without following
  CLAIMS_POLICY.md and getting PolyCoffee approval.
- Never mark coffee.help or getcoffeehelp.com as purchased until the owner confirms.
