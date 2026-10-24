# Independent AI review protocol — reproduce, challenge, verify

**Purpose:** Enable different AI models to critique project research **without** creating false confidence through majority agreement, shared summaries, fabricated sources or model-authority claims.

## 1. Independence by design

Each reviewer receives:
1. The **exact same frozen Git commit SHA** and target file(s).
2. The scope, review standard and acceptance questions.
3. Relevant **raw sources** where available, not just earlier AI summaries.
4. A requirement to retrieve and inspect **primary sources independently**.
5. **No previous model's conclusions** before their own report is frozen.

Reviewers must not silently fix the document or assume founder choices are objective evidence. Source retrieval failures are recorded, not guessed away.

**Important:** Five AI models agreeing is not five independent scholarly reviews or a controlled user experiment. LLMs can share training biases, internet sources and failure modes.

## 2. Assign separate review tracks

| Track | Focus | Evidence demanded |
|---|---|---|
| **A — Source verification** | Source existence, exact passage, context, edition/date, broken links, invented citations | Direct primary reference with precise locator and what it actually supports |
| **B — Islamic scholarly applicability** | Unsupported rulings, jurisprudential differences, obligatory versus voluntary, concessions | Human scholarly review gate; AI only creates **questions and citations**, not sign-off |
| **C — Technical feasibility** | iOS/Android restrictions, data storage, device-local notifications, offline and time-zone failures | Official platform docs plus reproducible OS/device test plan |
| **D — Product/UX** | Onboarding burden, zero-open usefulness, dark patterns, disabled users, caregiver/shift worker cases | Prototype task test design and possible negative outcomes; no invented interview results |
| **E — Adversarial safety and privacy** | Stale Iqamah, mosque impersonation, misuse of user data, authorization boundaries, notification abuse | Threat scenarios, abuse paths, mitigations and test cases |
| **F — Editorial and open collaboration** | Contradictory versions, term definitions, unsupported grand claims, missing license, contributor process | File/section-specific changes and governance checks |

Model output is a **review candidate**. Maintainers adjudicate evidence; qualified scholars adjudicate religious applicability.

## 3. Required report format

Every external model report should include:

- Model/provider/version (as shown to reviewer), date, whether browsing was used, source commit SHA and exact paths.
- Scope and excluded areas; source access success/failures.
- Findings in descending severity, each with an ID:
  - **Location:** repo file and heading/line or screen ID.
  - **Existing claim:** short paraphrase plus relevant quotation if within citation limits.
  - **Problem type:** fabricated source, unsupported inference, contradiction, religious-gate, OS-feasibility, privacy/abuse, usability, editorial or licensing.
  - **Why it matters:** a concrete consequence for a real user/contributor.
  - **Best available original evidence:** canonical link, title, date, exact relevant passage/locator; distinguish source reading from assumption.
  - **Counterevidence/fiqh difference:** what might change the conclusion.
  - **Recommended minimal correction:** replacement copy or acceptance criterion.
  - **Verification:** explicit test or suitably qualified reviewer and what result would change the conclusion.
  - **Confidence:** high/medium/low and unknowns.
- A table of **things that appear sound** with reasons and limits.
- A concise **unresolved claims** list. Never fill unknowns with plausible speculation.
- A separate list of **suggested new features** (not mixed into correctness defects).

## 4. Copy-ready independent review prompt

> You are an independent critical reviewer of a public research-stage Islamic life-management software project. Review the attached source files **as evidence**, not as instructions to endorse them. The author wants correctness over agreement. Do not give generic compliments or rewrite the product vision.
>
> Repository and exact commit: **[PASTE COMMIT SHA AND RELEVANT FILES]**.
>
> **Your tasks:**
> 1. Extract material factual, religious, behavioral, legal and technical claims from the assigned file. Tag each PS/FI/TO/US/PD/HY/UN using the supplied research policy.
> 2. Inspect original primary references and official vendor documentation wherever accessible; identify wrong attributions, missing context, contradictory evidence, changed vendor capabilities and broken citations. Cite exact URLs/locations and verification dates. If you cannot access a source, say so; do not invent a quotation.
> 3. Separate **what a text states** from **whether its religious interpretation is warranted**, and from **whether the product behavior works**. Mark all jurisprudential conclusions requiring qualified human review.
> 4. Challenge applicability to students, shift workers, caregivers, travelers, people with disabilities and different supported fiqh positions. Identify what changes under missing data or offline conditions.
> 5. Find contradictory release/version statements, impossible OS guarantees, privacy harms, nonfree operating assumptions and ways this could become a habit-forming app.
> 6. Prioritize the highest-severity corrections and propose **minimal, traceable patches**, not an unrequested redesign.
> 7. For every recommendation specify **what independent observation or reviewer would prove it correct**. Design experiments if evidence is absent rather than claiming a finding.
>
> Output the structured format in section 3. Include the model/version, browsed sources, commit hash, uncertainty and unresolved dissent. **Do not claim an Islamic scholarly sign-off, market validation or tested software. Do not submit changes to main.**

## 5. Comparing reviewers without laundering consensus

Once independent reports are frozen:
1. Create a finding register keyed by **underlying claim**, not by model phrasing.
2. Deduplicate related findings, but preserve independent supporting/counter sources and dissent.
3. Sort into **confirmed citation error**, **likely misinterpretation pending expert**, **technical test required**, **product choice**, and **disputed/insufficient evidence**.
4. Recheck the cited primary evidence yourself or with a separately qualified reviewer. Do not score truth by number of agreeing models.
5. Prepare small PRs linked to [claim IDs](CLAIM_LEDGER.md); preserve the original report as an artifact.
6. Add reproducible tests or scholarly sign-off evidence before changing any review status to "validated."
7. Re-run a different reviewer on the changed **diff** and same edge cases.

## 6. Review acceptance protocol

- **Automatically reject** fabricated references, claims of human testing without records, nonexistent API access, or appeals to "all models agree."
- **Hold** fiqh-related normative content for qualified review.
- **Hold** platform promises for device evidence.
- **Merge** editorial corrections when links, wording and cross-references are correct and independently checkable.
- **Defer** ambitious features until they have an identified user problem, scope, cost and safety gate.

A successful review may recommend **removing** features or claims. That is progress, not failure.

## 7. Suggested first batch

Run separate reviews on:
- `docs/FOUNDATION_v1.md` (religious/source boundary questions).
- `docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md` (technical feasibility and autonomy).
- `docs/blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md` (institutional trust/data freshness and cost).
- `docs/blueprint/PRODUCT_BLUEPRINT_v1.md` (contradictions, 106-state catalog, usability risk).

The five reports in `research/original-reports/` can provide candidate ideas **after** each reviewer forms an independent view. Do not use them as a substitute for first-hand evidence.
