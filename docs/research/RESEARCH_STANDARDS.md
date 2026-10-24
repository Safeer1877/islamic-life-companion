# Research integrity and evidence standards

**Status:** Editorial protocol for a publicly reviewable research-stage project.  
**Checked:** 24 October 2026.  
**Purpose:** Ensure that thoughtful language does not get mistaken for established religious, technical, scientific or user research.

## 1. Evidence classes and trust hierarchy

| Label | Meaning | What counts | What it does not establish |
|---|---|---|---|
| **PS** | Primary religious text | Direct Qur'anic passage or identified hadith collection entry with stable reference and translation/editorial provenance | A comprehensive contemporary fatwa, a single global calculation method, or an app algorithm |
| **FI** | Fiqh interpretation | Attributed qualified scholarly explanation, context, school/tradition where relevant, applicability and review record | Universal consensus unless genuinely documented |
| **TO** | Technical/operational evidence | Official vendor/platform spec, reproducible test, authorized data-source documentation and observed failures | Guaranteed operation on every OS/device/network |
| **US** | User/field evidence | Documented consented interview, contextual inquiry, task test or deployment study with method/sample/limitations | Universal effectiveness or clinical outcomes |
| **PD** | Founder/product decision | Explicit product constraints and tradeoffs recorded in a decision log | Empirically proven user benefit or religious obligation |
| **HY** | Untested hypothesis | Plausible behavior, schedule or solution awaiting a defined test | Established fact |
| **AR** | AI-generated research material | Unreviewed desk-research output, preserved for traceability | Independent human scholarly endorsement, experiment, or directly checked source |
| **UN** | Unverified assertion | Incomplete, contested, outdated or missing evidence | Release-approved factual statement |

An attributed AI desk-research report can generate candidate claims; it never automatically upgrades a claim to **PS**, **FI**, **TO** or **US**.

## 2. Required structure of a material claim

Record these fields in the [claim ledger](CLAIM_LEDGER.md) or linked issue:

- **Claim ID** and its exact statement, avoiding sweeping paraphrase.
- **Class** from the table above.
- **Where it appears** (repo file and heading/line or screen ID).
- **First-hand source** (canonical URL, publication/edition/date, section, quoted passage kept short).
- **What that source actually establishes**, and what it **does not**.
- **Verification performed** (who checked, date, mechanism). If only an AI checked it, say so.
- **Confidence / status**: cited-but-not-interpreted, provisionally verified citation, awaiting fiqh review, proposed product decision, needs user test, technically unverified, withdrawn.
- **Counterevidence or known disagreement**, with references when applicable.
- **Proposed independent test or reviewer gate** and named acceptance evidence.

Do not conflate “link exists,” “text says this,” “interpretation is correct,” “behavior is appropriate for every user,” and “software works.” They are separate checks.

## 3. Religious-source review gates

- Check the **exact** verse/hadith and context, not an unattributed summary. Verify citation numbering, text, translation and context.
- Distinguish Qur'an text, hadith narration, scholarly legal analysis, practical educational guidance and our product interaction design.
- Specific rulings affecting prayer windows, school-dependent methods, combining/shortening prayer, menstruation, travelers, disability and related accommodations require **qualified scholarly review**, with applicability and recognized differences recorded.
- No assumption of universal timetable; no label of missed worship from a missed app event/notification.
- A reviewer should sign off on actual **wording and behavior**, not just the general concept. Record their identity/qualification only with consent, scope, date and any dissent.
- A **verified mosque editor** is operationally authorized to publish factual mosque times, not automatically an academically qualified religious authority.

## 4. Behavioral and product claims

“Zero-open use is beneficial”, “people prefer silence”, “onboarding can be completed quickly”, “this reduces guilt”, and “a local-first workflow improves adherence” are **testable hypotheses**. Define a baseline, user group, task, acceptance criterion, confounders and harm measures; do not call them proven before studies.

A low number of app launches can be good, but **zero opens alone is not evidence of useful assistance**. Ask whether the person achieved their intended task without added friction or unwanted reminders.

## 5. Technical claims

Use reproducible checks for permissions, background scheduling, notification delivery, offline fallback, data deletion/export, time-zone changes, localization and accessibility. Capture platform/OS version, device conditions, timestamp, exact steps, expected/actual behavior and negative cases. Do not promise constant background monitoring on iOS or Android.

## 6. External integrations and legal rights

- Check official API terms, redistribution conditions and revocation/usage restrictions for mosque data, texts, translations, maps and embedded media.
- Do **not** treat an undocumented endpoint as permission to scrape a private API.
- Attribution and quotations may require licenses. User-submitted content and volunteer contributions raise separate copyright and privacy questions.
- **Scoped licenses have been adopted** for original app code, a future hosted service, and rights-controlled documentation; see the [licensing decision](../governance/LICENSING_DECISION.md) and [license map](../../LICENSES/README.md). That decision does **not** establish clearance of third-party sources, translations, quoted material or the five original AI reports.

## 7. Verification log and change control

Research originals are preserved under `research/original-reports`. The reviewed documents should point back to them via [SOURCE_MANIFEST.md](../../SOURCE_MANIFEST.md), but should never say they have been independently verified merely because several model outputs agree. Add a new claim ID or update status with dated evidence rather than silently revising a prior record.

Review stages: **claim extraction → source verification → disagreement search → qualified domain review where needed → reproducible test → recorded decision**.

### Initial sources checked on 24 October 2026

These links were opened to verify the directly cited text exists and is relevant—not as religious legal sign-off:

- Qur'an 4:103 — https://quran.com/4/103
- Qur'an 28:77 — https://legacy.quran.com/28/77
- Sahih al-Bukhari 1968 — https://sunnah.com/bukhari:1968
- Sahih al-Bukhari 5199 — https://sunnah.com/bukhari:5199
- Sahih al-Bukhari 6465 — https://sunnah.com/bukhari:6465
- Sahih Muslim 335c — https://sunnah.com/muslim:335c

Additional official technical/commercial references checked:

- GitHub community contribution standards — https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions
- MAWAQIT private API policy — https://help.mawaqit.net/en/articles/11991838-can-i-use-your-api
- Masjidbox public API/export options — https://support.masjidbox.com/does-masjidbox-have-a-public-api-for-prayer-times-sfnfd

**Remaining gap:** Citation existence is not a qualified scholarly verdict, implementation feasibility test or user study.
