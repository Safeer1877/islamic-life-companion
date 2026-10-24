# Contributing to Islamic Life Companion

Thank you for helping make the research, design and eventual software accurate, accessible and useful. This project is **research and product specification**, not a completed app, certified religious guidance, or evidence of proven effectiveness.

**Important licensing status:** A repository license has not yet been selected. See [licensing decision](docs/governance/LICENSING_DECISION.md) before reusing material or offering substantial code/design contributions. Public GitHub access by itself does not grant an open-source license. Maintainers should resolve this before actively recruiting contributions.

**Current intake boundary:** Please begin with evidence-linked issues, source corrections and proposed review notes. Broad new software modules and substantial imported writing are **not yet being actively solicited** until licensing, rights and maintainer safeguards are settled. A pull request does not by itself transfer rights to the maintainer or establish that its content is properly licensed. See [owner launch checklist](docs/governance/MAINTAINER_LAUNCH_CHECKLIST.md) and [licensing options](docs/governance/LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md).

## Before proposing changes

Read, in order:

1. [Project introduction](README.md)
2. [Research integrity and evidence policy](docs/research/RESEARCH_STANDARDS.md)
3. [Claim and validation ledger](docs/research/CLAIM_LEDGER.md)
4. [Religious and behavioral foundation](docs/FOUNDATION_v1.md)
5. [Free, local-first, zero-open policy](docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md)
6. [Product blueprint](docs/blueprint/PRODUCT_BLUEPRINT_v1.md)
7. [Governance and review process](docs/governance/REVIEW_PROCESS.md)

## Useful contributions

- **Source correction:** Identify a claim, precise original passage, reliable primary evidence, date accessed, translation/edition, and proposed wording. Describe conflicting interpretations; never present an AI response as a primary source.
- **Technical feasibility:** Reproduce device/OS behavior with version, test conditions, limitations, evidence, and truthful alternatives (offline, permissions denied, time-zone changes).
- **UX critique:** A concrete user scenario, where the specified flow fails, expected harm/burden, improved wording or behavior, and how it would be tested.
- **Accessibility/localization:** Screen-reader order, RTL, Urdu/Arabic rendering, low-vision and motor-access considerations, with steps to reproduce.
- **Privacy/security:** Data-flow boundaries, abuse cases, minimum permissions and safe failure paths. Report potential exploitable weaknesses through [SECURITY.md](SECURITY.md), not public issues with sensitive details.
- **Mosque data/operations:** Verified source provenance, freshness rules, authorized editor proof, correcting incorrect Iqamah, no unauthorized API access and no disclosure of followers' private routines.

## Proposal process

1. **Check existing issues and PRs** to prevent duplicates.
2. Open a focused issue first for theological changes, architecture, new modules, or major founder product directions. Small corrections can go directly to a pull request.
3. Make a branch from `main` and submit a **small, traceable PR**. Avoid sweeping rewrites that erase evidence or merge unrelated subjects.
4. In the PR template, specify claim IDs (when applicable), original and revised text, linked evidence, confidence, affected flows/screens and tests. Describe what remains unknown.
5. Keep **research originals intact** under `research/original-reports/`; corrections belong in reviewed documents and provenance notes, not silent edits of the submitted AI texts.
6. For religiously consequential content, request qualified human scholarly review. Neither automated review nor maintainer approval alone substitutes for the subject-matter gate.
7. Maintainers decide what to merge after assessing evidence, community impact and review gates. **AI agreement is not evidence.**

## Editorial rules

- Write plainly. Avoid hype such as “scientifically proven,” “universally accepted,” “100% accurate,” or “fully Islamic” unless a defined claim has evidence.
- Keep **fact**, **religious interpretation**, **design decision**, **hypothesis**, and **future possibility** distinct.
- Date time-sensitive sources; provide direct links and exact passages/page or hadith references.
- Do not fabricate interview participants, benchmarks, usage data, scholarly endorsement, OS permissions, locations or mosque timetables.
- Identify when Islamic jurisprudence varies and when applicability needs qualified review. Do not insert new religious rulings under the guise of copyediting.
- Don't publish passwords, API keys, private messages, IDs, sensitive religious disclosures or personal details of users/Imams.
- Preserve the free, local-first, no-required-AI, low-interruption approach unless a founder-reviewed proposal explicitly changes it.
- Use inclusive, respectful language; provide concrete evidence over assumptions about communities or individuals.

## AI-assisted contributions

AI tools may draft, challenge, translate or compare documents. Each contributor **remains responsible** for every citation, technical claim, licensing restriction and change. Disclose substantive AI assistance in the PR. Use the [independent review protocol](docs/research/INDEPENDENT_AI_REVIEW_PROTOCOL.md) and provide model/date/prompt and source links when submitting a review. Never upload third parties' personal or sensitive data to models without permission.

## Review and acceptance

Proposed fixes are not accepted solely because they read convincingly. Research claims need original sources, fiqh-sensitive behavior needs appropriate qualified review, and UX/technical promises need reproducible testing. See [REVIEW_PROCESS.md](docs/governance/REVIEW_PROCESS.md).

## Current stage

There is no executable application yet. Contributions should first strengthen verifiable assumptions, internal consistency, risk handling, community governance, platform feasibility and usable prototype plans. Once a license and initial engineering standards are approved, this guide can expand to code, testing and release processes.
