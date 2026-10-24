# Islamic Life Companion

> Private working repository for an Islamic life-management product concept. **Research and design stage; no functional application is implemented yet.**

## Purpose

Help Muslims organize practical daily life in accordance with verified Islamic principles while respecting worship, work, family, health, personal agency, capacity, and legitimate differences of jurisprudence. The product is designed to reduce unnecessary friction and phone dependence, not maximize engagement, streaks, or a numerical measure of religiosity.

## Product direction (24 October 2026)

**Free, local-first and designed for zero unnecessary app opens.** First-release core features must work without an AI model, paid service, account or continuous internet. Users opt into notifications and may choose on-demand-only support. AI is a possible future enhancement, not a core feature. The goal is useful assistance in real life, not keeping the user in the app.

**Current policy:** [Local-first, zero-open, free-to-use v1.1](docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md). This policy supersedes any older screen or UX language implying AI-dependent onboarding, mandatory check-ins or automatic background observation.

## Mosque/community direction (proposed, not in core v1)

The future [Mosque & Community Network](docs/blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md) describes verified mosque institutions, authorized timetable editors, voluntary information subscriptions, and a strictly gated pilot. It **does not** add an Imam chat/social network or require a connected mosque account for the local personal-planning experience. Groups and qualified religious guidance are explicitly deferred.

## Start here

1. [`docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md`](docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) — **latest product decisions**: free access, offline core, notification restraint, no required AI and zero-open acceptance tests.
2. [`docs/FOUNDATION_v1.md`](docs/FOUNDATION_v1.md) — consolidated principles, religious boundaries, and decision framework.
3. [`docs/blueprint/PRODUCT_BLUEPRINT_v1.md`](docs/blueprint/PRODUCT_BLUEPRINT_v1.md) — functional product blueprint, screens, journeys and behavioral flows.
4. [`docs/blueprint/SCREEN_REGISTER_v1.csv`](docs/blueprint/SCREEN_REGISTER_v1.csv) — inventory of 106 views, sheets, and states (not 106 primary navigation screens).
5. [`docs/blueprint/READ_BLUEPRINT.html`](docs/blueprint/READ_BLUEPRINT.html) — locally readable HTML edition; styles in `blueprint.css`.
6. [`docs/blueprint/UX_DESIGN_HANDOFF_PROMPT.md`](docs/blueprint/UX_DESIGN_HANDOFF_PROMPT.md) — visual design brief.
7. [`research/original-reports/`](research/original-reports/) — original independent AI-generated research documents for reference, not verified religious rulings.

## Status and caveats

- The foundation is a **conceptual product model**, not religious certification, medical advice, or a tested behavioral intervention.
- Religious claims that would affect practice require documented primary-source verification and appropriate qualified scholarly review.
- The screen inventory and user flows are proposed, not validated with participants.
- No executable app, secrets, production credentials, or dependencies are provided here.
- Treat these documents as version 1 baseline material subject to user research, design critique, and factual review.

## Repository layout

```text
docs/
  FOUNDATION_v1.md
  blueprint/
    LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md
    MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md
    PRODUCT_BLUEPRINT_v1.md
    SCREEN_REGISTER_v1.csv
    READ_BLUEPRINT.html
    blueprint.css
    UX_DESIGN_HANDOFF_PROMPT.md
research/
  original-reports/
```

## Next phase

First prototype and test the **zero-open** lifecycle, optional local reminders, adaptive non-AI onboarding and no-notification/no-account paths. Then visually design the main flows and validate religiously sensitive cases before development.

## Upload status

The complete text-based foundation, blueprint and five research reports are present. The local preparatory package additionally contains an archival ZIP and a screen-register generation script; these two auxiliary files were not transferred through the connected GitHub integration. The CSV screen register itself is present. The repository CSS was recreated for online viewing rather than imported byte-for-byte.
