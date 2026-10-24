# Research-slice UX handoff — first investigate need, then test a minimal decision

**Status:** Proposed design-test brief, not approval to build the app. The older 106-state blueprint is a **reference catalog**, not a compulsory wireframe list.

Read the [research MVP plan](../research/RESEARCH_MVP_VALIDATION_PLAN_v0.1.md) and [local-first policy](LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) first, then consult the [mobile limitations](../architecture/MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md), [product blueprint](PRODUCT_BLUEPRINT_v1.md) and [screen register](SCREEN_REGISTER_v1.csv) for traceability. The first slice consists of **19 candidate contracts, not 19 required screens**. Do not silently promote the historical 79 Core entries into a release scope.

## Before any wireframes

Do not pitch an interface or show app mockups during the initial recent-behavior discovery interviews. Obtain voluntary, privacy-respecting evidence that real, solvable problems recur and existing tools do not already handle them adequately. Research results, recruitment, informed consent and stopping criteria must be recorded separately and without publishing identifiable personal schedules.

A calendar cannot create an authorized break, rearrange another person's responsibilities or settle a religious ruling. When the problem is structural or no feasible choice exists, the best proposed interaction may be an explicit **no solution / no change** result.

Only after an evidence-based decision to explore a tiny prototype should a designer start the tasks below. If the hypothesis fails, report that result rather than polishing UI.

## Research design deliverables (conditional, in order)

1. **Baseline journey:** Document the participant's actual trusted prayer-information source, calendar/paper planning and human workarounds. Account for setup and recurring correction costs; don't use an artificially weak comparator.
2. **One neutral conflict/no-conflict task:** Sketch a fixed commitment, flexible/protected period, a real overlap *only when supported by the provided data*, and a no-conflict control. Do not claim a prayer-time calculation or religious permission. Mark all unverified timing content as a synthetic fixture.
3. **Minimal low-fidelity views:** Sketch only the contracts necessary to complete and undo that task, drawing selectively from `S01`, `S03`, `S08`, `S11`, `S12`, `S19`, `S20`, `S25`, `S33`, `S34`, `S37`–`S40`, `S74`, `S79`, `S80`, `X95`, `M99`. Consolidate screens freely and preserve traceability to relevant IDs. **No entire-screen-catalog assignment.**
4. **Failures and control:** Test the option to keep the original plan; a truly blocked or structural conflict; unknown data; denied notification permission; offline/no-account/no-AI operation; and an easily discoverable undo path. Never silently modify consequential commitments.
5. **Comparison protocol:** Present comparable tasks through the participant's existing tools and the proposed paper/clickable flow, counterbalancing order where practical. Record task outcome, effort, errors, mistaken religious confidence, user agency, interruptions and willingness to maintain data.
6. **Review:** Record contradictions, accessibility and RTL/Urdu/Arabic readability questions, source-provenance comprehension, and dissent or negative results. Separate research observations from untested design preferences. **Only if these gates justify investment**, prepare a small component library and optional high-fidelity visual directions for the retained interaction.

## Non-negotiable boundaries

- Essential user flow works without account, required AI, paid AI subscription, continuous location, network or mandatory daily opens.
- Notifications default **OFF by category**; selecting an assistance style does not silently grant permission.
- Distinguish prayer window, sourced Iqamah event, user-entered commitment and unverified estimate; no invented mosque data or jurisprudential outcomes.
- **Already queued** mosque reminders may still fire after an offline correction; no unconditional cancellation promise.
- Do not infer piety, attendance, health status or personal religious circumstances. No scores, streak penalties, coerced behavior or tracking of others.
- Consequential religious copy is marked **Pending Qualified Scholarly Review** and cannot be presented as a ruling before review of exact text, context and applicability.
- No fake submission, verified mosque authority, guaranteed OS background behavior or unsupported backup/deletion claim.
- Test accessible exits, screen-reader reading order, large text, RTL and no-action states before treating a visual direction as ready.

## Report back before polishing

Provide the observed or missing evidence of recurring need, a truthful current-tools baseline, minimal task maps, the negative/no-action results, sample and method limits, and explicit recommendations to **continue, narrow, postpone or stop**. If no real participant testing occurred, label any sketch **proposed and untested**. Do not invent trial counts or quote unreviewed religious text.

The original [full blueprint](PRODUCT_BLUEPRINT_v1.md) and [HTML reading edition](READ_BLUEPRINT.html) remain a **historical design reference**. They do not override the current research gates or mandate large screen production.
