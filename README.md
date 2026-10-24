# Islamic Life Companion

**Research-stage, community-reviewable product specification. Not yet an application or an authoritative religious advisory service.**

Islamic Life Companion explores how to help Muslims organize daily commitments, worship-related planning, family responsibilities, rest and freely chosen personal intentions **without increasing phone dependence**. The aim is useful, quiet assistance that the person controls, with no spiritual scores, coerced check-ins or invented religious rulings.

> **Current maturity:** Concept and experience blueprint written · primary citations *partly checked* · scholarly review **pending** · user research **pending** · technical prototype **not built** · release **not ready**.

## Core commitments

- **Free to use:** First-release core should not rely on a subscription or paid AI. This is a product goal, **not a proof of zero operating cost**.
- **Local-first and private:** Essential plans should work on the device without an account or always-on internet.
- **Low-interruption / zero-open:** A normal day may require no app launch. Reminders are selected by the person and must be useful rather than engagement-driven.
- **Religious care:** Primary religious sources are distinguished from fiqh interpretation and software scheduling choices; qualified scholarly review is required for consequential guidance.
- **No required AI:** Core onboarding, planned routines and approved reminders must work without model inference.
- **Optional community layer:** A future verified mosque data network may publish sourced Iqamah and events; this is not a required part of the first release.

## Read this first

| Document | Purpose |
|---|---|
| [Initial repository audit](docs/research/AUDIT_REPORT_2026-10-24.md) | Verified gaps, audit limits and blockers |
| [Original research provenance and rights triage](docs/research/RAW_REPORT_SOURCE_RIGHTS_TRIAGE_2026-10-24.md) | Five preserved reports, 173 source-link occurrences, and unresolved rights verification |
| [Research standards](docs/research/RESEARCH_STANDARDS.md) | Distinguishes evidence, interpretation, decisions and hypotheses |
| [Claim ledger](docs/research/CLAIM_LEDGER.md) | Selected claims, checked citations and unresolved verification gates |
| [Functional foundation](docs/FOUNDATION_v1.md) | Core rights-aware product model and religious boundaries |
| [Local-first zero-open policy](docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) | Latest binding founder constraints |
| [Product experience blueprint](docs/blueprint/PRODUCT_BLUEPRINT_v1.md) | Proposed screens, behavior, journeys and exceptions |
| [Research MVP and validation plan](docs/research/RESEARCH_MVP_VALIDATION_PLAN_v0.1.md) | **Proposed** narrow vertical slice, baseline comparison, user and engineering tests; not built |
| [Issue #11 field-study kit](docs/research/field-study/README.md) | Blank consent, interview, diary, baseline-comparison and go/no-go materials; **no participants or outcomes yet** |
| [Mobile reliability, consent and backup contract](docs/architecture/MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md) | Mobile OS constraints, pre-scheduled stale reminders, privacy and permission risks; not verified on devices |
| [Screen/state register](docs/blueprint/SCREEN_REGISTER_v1.csv) | 106 historical contracts, separately triaged into a proposed smaller experiment; **not** 106 built screens |
| [Mosque and community proposal](docs/blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md) | Future verified information network, with pilot gates |
| [Original AI-assisted desk research](research/original-reports/) | Five preserved research inputs — **not** scholarly approval or field evidence |
| [Independent AI review protocol](docs/research/INDEPENDENT_AI_REVIEW_PROTOCOL.md) | Reproducible adversarial reviews without counting consensus as proof |

The styled [HTML blueprint](docs/blueprint/READ_BLUEPRINT.html) is a reading convenience based on the original v1.0 experience text; **the Markdown master plus later policy files govern** where versions differ.

## Help improve the foundation

We welcome **concrete, evidence-backed criticism**, especially source errors, religious applicability questions, iOS/Android feasibility limitations, privacy/security issues, accessibility gaps and unnecessary user interactions.

- Read [CONTRIBUTING.md](CONTRIBUTING.md), the [review workflow](docs/governance/REVIEW_PROCESS.md), and [community conduct](CODE_OF_CONDUCT.md).
- Prefer a focused issue or pull request containing **the exact claim, a first-hand reference, proposed correction and an independent verification method**.
- If you use AI to review documents, disclose the model, date, source access and commit, and follow the [independent review procedure](docs/research/INDEPENDENT_AI_REVIEW_PROTOCOL.md).
- Do **not** present a model's confidence, five similar model outputs, or an attractive screen as religious certification or proof of user benefit.
- Do not post secrets, private religious or family details, or exploitable vulnerabilities publicly. See [SECURITY.md](SECURITY.md).

### Contribution readiness

A transparent public repository still needs real rights and safety controls. **As of 25 October 2026**, a four-check branch ruleset is active and a deliberately failing PR [was blocked without merging](https://github.com/Safeer1877/islamic-life-companion/pull/12). This establishes required-check enforcement, **not** user, religious or device validation. The owner reports enabling private vulnerability reporting, but actual confidential receipt and a separate conduct-reporting route have not been tested. The [maintainer launch checklist](docs/governance/MAINTAINER_LAUNCH_CHECKLIST.md) tracks the remaining actions; the [rights audit](docs/governance/LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md) tracks outstanding source provenance. Focused corrections are welcome; **do not assume the project accepts unrestricted code or imported content**.

### Adopted licensing and exclusions

The repository owner approved and merged a scoped licensing structure in [PR #6](https://github.com/Safeer1877/islamic-life-companion/pull/6): **MPL-2.0** for future original app code, **AGPL-3.0-only** for original future hosted mosque/community backend code, and **CC BY-SA 4.0** for original, rights-controlled documentation. The five original AI-assisted reports and third-party material remain excluded pending rights review. Read the actual [license map](LICENSES/README.md), [decision record](LICENSES/DECISION_RECORD.md) and [contributor terms](LICENSES/CONTRIBUTION_TERMS.md). Licensing is not religious or technical certification.

## Repository map

```text
LICENSE                                 Original application code: MPL-2.0
LICENSES/                               AGPL, CC BY-SA, scope and contribution terms
docs/
  FOUNDATION_v1.md                     Conceptual model
  blueprint/                           Product behavior and screen inventory
  research/                            Research standards, ledger and review protocol
  governance/                          Decision log, licensing and review process
research/original-reports/             Preserved AI-assisted desk-research inputs
.github/                               Review templates, code owners and checks
scripts/                               Documentation integrity checks
```

## What still needs independent evidence

1. **Qualified Islamic review** of the religiously consequential rules and actual screen wording, including recognized fiqh variations.
2. **Usability and accessibility tests** for people with different schedules, disabilities, family responsibilities and languages.
3. **Native prototypes** for local data storage, on-device notifications, time-zone changes and offline/no-permission paths.
4. **Verification and authorization** for any mosque data sources, institutional editor roles and correction process.
5. **Imported-source rights clearance, independently monitored confidential reporting, and qualified human review** before promoting substantial public development. GitHub's four required checks and negative PR-blocking test are configured and verified; they do not replace these human gates.

**Next evidence gates, not a commitment to build all candidate screens:** First study recent, real coordination problems against existing calendar and trusted prayer-information practices ([Issue #11](https://github.com/Safeer1877/islamic-life-companion/issues/11)); only then consider a narrow comparison and bounded native feasibility testing ([Issue #10](https://github.com/Safeer1877/islamic-life-companion/issues/10)). A negative or inconclusive result can justify narrowing or stopping the proposed planner. No participants, physical-device tests or qualified religious review are claimed.

The repository aims to show precisely **what is known, what was chosen, what remains uncertain, and what would demonstrate that a proposed feature actually works**.
