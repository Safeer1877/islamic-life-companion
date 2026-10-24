# Repository audit — initial contribution-readiness review

**Date:** 24 October 2026  
**Base reviewed:** `main` at `5205a0fe8938400f0c5de15b73061153b2342328`  
**Nature:** Repository/editorial/process audit, with a **limited** check of selected primary and vendor references. **Not** a full scholarly ruling review, exhaustive citation verification, security penetration test, accessibility test or user study.  
**Project state at baseline:** Public, 18 files, documentation and original AI desk-research materials. No deployable app or established community moderation workflow.

## Executive finding

The underlying concept is coherent: rights-aware everyday support; not another engagement feed, prayer-compliance score or generalized religious chatbot. The foundation explicitly distinguishes religious source references from untested design outcomes, and the latest documents consistently favor free, local-first, low-interruption operation.

**However, publication is not verification.** The repo currently describes a proposed user experience, not a proven scientific model, certified religious guidance or technically implemented app.

## Prioritized findings

| ID | Priority | Observed issue on baseline | Consequence | Initial response and remaining work |
|---|---|---|---|---|
| **A-01** | P0 | No selected **LICENSE** for software or docs | Readers cannot reliably infer reuse/contribution permissions from public visibility | [Licensing decision required](../governance/LICENSING_DECISION.md); founder must approve license and source rights |
| **A-02** | P0 | No `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue/PR templates or documented reviewer gates | Contributions may mix conjecture and evidence; abuse/sensitive data handling undefined | Added in review branch; confirm actual maintainer enforcement/reporting channels |
| **A-03** | P0 | No **claim-level provenance ledger** or repeatable independent-review procedure | AI-generated convergence may be misread as validated scholarly or empirical evidence | [Research standards](RESEARCH_STANDARDS.md), [claim ledger](CLAIM_LEDGER.md), [independent review protocol](INDEPENDENT_AI_REVIEW_PROTOCOL.md); deeper review outstanding |
| **A-04** | P1 | Five imported desk-research reports are not independent field studies or a scholarly panel | Strong-sounding summaries risk overstating correctness | Foundation already says this; README should repeat it prominently |
| **A-05** | P1 | Primary texts are cited, but applicability to religiously sensitive decisions has **no recorded qualified scholarly approval** | Inappropriate or overgeneralized prayer and exemption guidance | Provisional check of references performed; qualified independent fiqh review still mandatory |
| **A-06** | P1 | Large blueprint with 106 view/state entries and 30 flows but no testable release MVP or real participant results | Appearance of finished specification may be confused with implementability | Retain original catalog; pilot narrow end-to-end tasks and mark test status explicitly |
| **A-07** | P1 | Local notification/background behavior not demonstrated on actual iOS/Android devices | “Zero-open” may be interpreted as uninterrupted background capability | Require device/OS evidence, denial tests and honest offline limitations |
| **A-08** | P1 | Mosque network needs operational authority and long-term data freshness | Incorrect Iqamah and impersonation risk | Future-only module; 3–5 mosque **proposed** pilot, not completed |
| **A-09** | P1 | Source manifest lists local/archive/generator files that are **not** present in the remote | Readers may assume they can reproduce byte-identical originals from GitHub | Explicit uploaded/pending distinction; do not publish unverifiable checksums as hashes of remote content |
| **A-10** | P1 | Public README previously called repository “Private working repository” | Immediate credibility/confidence mismatch | Correct on review branch |
| **A-11** | P2 | Related foundation appears at two paths, and HTML reading edition can diverge from edited master Markdown | Unclear authoritative source and stale copies | Identify authoritative master, make derived copies clearly marked, later automate generation |
| **A-12** | P2 | No automated screen/link regression check | Small edits can break 106-state inventory and links | Add a simple CI integrity check; it **cannot** verify religious correctness |
| **A-13** | P2 | No real contributor onboarding, decision records or ongoing issue triage | Future community input may become unmanaged feature accumulation | Contribution guide, decision log, scope gates and templates introduced |
| **A-14** | P2 | Terms and permissions for AI desk reports, translations and third-party media not comprehensively documented | Redistribution/licensing ambiguity | Include in founder licensing and provenance review |

### What was checked directly

- The repo existed and was **public** at the audit time.
- Baseline tree had **18 files** and no root LICENSE/contributor/community health policies.
- `docs/FOUNDATION_v1.md` identifies the five AI desk studies as **not** experiments or scholarly endorsement.
- The screen register contains **106 catalog entries**, including exception states and sheets; they are not 106 implemented main screens.
- The master product blueprint describes **30 proposed user flows**, not validated participant behavior.
- Directly inspected citations: Qur'an 4:103 and 28:77; Sahih al-Bukhari 1968, 5199, 6465; Sahih Muslim 335c. The listed passages exist and are relevant to the limited statements in the [initial claim ledger](CLAIM_LEDGER.md), without constituting jurisprudential sign-off.
- Vendor documentation: MAWAQIT describes its API as private; Masjidbox describes timetable exports/iCal and lack of public prayer-time API. Terms and authorization must be checked before integration.

### What was **not** checked

- All citations across the five long AI-generated reports or every blueprint flow.
- Correctness of contemporary religious jurisprudence for every relevant school and individual circumstance.
- End-to-end OS background behavior; no functional software exists to test.
- Technical cost assumptions, real mosque staffing capacity, user needs, privacy implementation or security.
- Open-source license fitness, all third-party redistribution permissions or contributor ownership terms.
- GitHub branch protection, enforced code-owner reviews or availability of confidential security reporting.

## Research-ready, not contribution-ready: decision gates

**Before recruiting major contributions:**
1. Choose and publish appropriate licenses/permissions for code, original docs and third-party source material.
2. Configure a private safety/security contact and publish expected response ownership.
3. Enable reviewed PR workflow and appropriate branch protection/ruleset controls; verify they actually work.
4. Triage and prioritize source-claim reviews. Assign separate human scholarly reviewers for religiously consequential rules.
5. Define and test the smallest actual prototype for private local onboarding, one user-selected reminder, and offline/no-permission use.

**Before claiming any product works:** Test the relevant OS/device cases, realistic personal-life examples and negative outcomes with representative users, recording method and limitations.

**Before mosque-network pilot:** Obtain mosque-admin consent, verification and timetable accuracy plan, volunteer workload/cost estimate, data correction procedures and clear opt-in rules.

## First independent review batch

Use the frozen independent reviewer prompt for four tracks in parallel, **without** showing one model another model's answer first:

1. Qur'an/hadith and fiqh applicability in `docs/FOUNDATION_v1.md`.
2. iOS/Android zero-open, local notification and privacy feasibility.
3. Mosque ownership, verified schedules, offline freshness and abusive communications.
4. Cross-document contradictory statements, MVP size, and accessibility.

Consolidate findings by **claim ID and first-hand evidence**, not voting. Open focused follow-up issues rather than approving sweeping automated edits.

## Why this audit is not a stamp of approval

A credible public foundation displays what has been checked, what remains unknown, who must review consequential decisions and what evidence would change the plan. This audit creates that *process*; it does not transform AI-generated research into verified religion or a tested app.
