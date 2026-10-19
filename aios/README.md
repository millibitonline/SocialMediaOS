# AIOS — Foundation Layer

AIOS is a reusable, platform-independent operating system for organizations
where humans and AI agents work together. This directory is the **Foundation**:
the top of every inheritance chain.

> Rule for this directory: nothing here may reference a specific organization,
> social platform, vendor, or model. If it would, it belongs at Organization level.

| Path | Purpose |
|------|---------|
| [`.aios.yaml`](.aios.yaml) | Foundation configuration and locks |
| [`governance/OPERATING_PRINCIPLES.md`](governance/OPERATING_PRINCIPLES.md) | Non-negotiable principles |
| [`governance/GOVERNANCE.md`](governance/GOVERNANCE.md) | Roles, change control, approval gates, ADRs |
| [`governance/INHERITANCE.md`](governance/INHERITANCE.md) | How rules flow down; extend vs. override |
| [`governance/APPROVALS.md`](governance/APPROVALS.md) | What counts as a human approval |
| [`agents/AGENT_STANDARDS.md`](agents/AGENT_STANDARDS.md) | Conduct, discovery, and hand-off rules for agents |
| [`agents/registry.yaml`](agents/registry.yaml) | Vendor-neutral role definitions |
| [`schema/aios-config.md`](schema/aios-config.md) | `.aios.yaml` reference |
| [`templates/`](templates/) | ADR and Feature templates |

To reuse AIOS for another organization, copy `aios/` unchanged, `scripts/validate_aios.py`,
and create a new root `.aios.yaml` with `layer: organization`.
