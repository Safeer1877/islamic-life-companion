# Islamic Life Companion — UX Blueprint Package

> **Read first:** [`LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md`](LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md), adopted on 24 October 2026. This is the latest product decision layer: free for users; local-first; no required AI; a well-configured day may need **zero app opens**; proactive alerts are opt-in. Where older wording conflicts, this v1.1 policy prevails.

**Future module: `MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md`** — staged verified mosque profiles, safe timetable updates, opt-in communications, separate admin/scholar roles and pilot verification gates; not a v1 launch dependency.

**0. `LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md`** — binding experience constraints, zero-open journeys, existing screen-ID adaptations, offline/OS boundaries, and acceptance tests.

**1. `READ_BLUEPRINT.html`** — easiest to read: styled, accessible table of contents and complete blueprint; keep `blueprint.css` beside it.

**2. `PRODUCT_BLUEPRINT_v1.md`** — master Markdown specification. Full product logic, screen designs, onboarding, 30 user flows, weekly/life cycles, copy rules and verification gates.

**3. `SCREEN_REGISTER_v1.csv`** — 106 views, screens, reusable sheets and exception states with content, actions, entry/exit routes, state and release tier. It is a *catalog*, not a mandate to build 106 separate main screens.

**4. `UX_DESIGN_HANDOFF_PROMPT.md`** — a **research-slice-first** design handoff; broader historical screens are references, not a wireframe backlog.

**5. `FOUNDATION_REFERENCE.md`** — the previously adopted consolidated foundation that governs the blueprint.

**6. `blueprint.css`** — styling for the HTML reading edition.

Research basis: the [consolidated foundation](../FOUNDATION_v1.md) and five preserved [original AI-assisted reports](../../research/original-reports/), whose source rights and claims are not fully verified. Religious content needing interpretation **still requires qualified scholarly review**; proposed interventions and visuals still require user testing.

## Research corrections from four external reviews (24 October 2026)

- [**Research MVP & Validation Plan v0.1**](../research/RESEARCH_MVP_VALIDATION_PLAN_v0.1.md) selects candidate contracts from this inventory; the historical `release` column is **not** a committed v1 backlog. The register now has a separate `research_slice_v0_1` column so none of the 106 IDs need to be deleted or mistaken for required individual screens.
- [**Mobile Reliability, Consent & Local-Data Contract v0.1**](../architecture/MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md) spells out limited mobile notification queues, impossible-to-guarantee offline mosque reminder correction, permission defaults, actual OS backup behavior, reporting recipients and device tests.
- Full conceptual blueprint remains the reference for user journeys and exceptional cases, **not proof of feasibility**. External scholars and real-device/user tests remain required. These are separate *proposed* implementation/risk documents, not a new release certification.

## Immediate use — evidence before broad design

First investigate whether real people have repeated, **solvable** coordination problems inadequately handled by their existing prayer-information sources and calendars. This has **not been done**. If discovery supports a need, use the [research MVP plan](../research/RESEARCH_MVP_VALIDATION_PLAN_v0.1.md) and [updated design handoff](UX_DESIGN_HANDOFF_PROMPT.md) to compare one low-fidelity reversible decision against that baseline, including no-conflict and no-permission cases.

Use the four top-level areas, original wireframes, 30 illustrative flows, and 106-state CSV as **historical design references**, not an instruction to draw every screen. Do not design mandatory daily opens, AI chat front pages, coercive reminders or always-on tracking. Device prototypes and consequential religious copy need independent technical and qualified human review respectively.