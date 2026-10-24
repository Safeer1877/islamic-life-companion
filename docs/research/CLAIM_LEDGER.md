# Claim and validation ledger — initial baseline

**Prepared:** 24 October 2026. This is a **triage ledger**, not evidence of complete review. Unlisted claims in the long research/blueprint files remain unverified until explicitly assessed.

| ID | Claim / decision being assessed | Class | Primary location / evidence | What is established | Remaining gate |
|---|---|---|---|---|---|
| **R-001** | Prayer is prescribed at appointed times | PS | [Qur'an 4:103](https://quran.com/4/103), [foundation](../FOUNDATION_v1.md) | The cited verse contains appointed-time language | **FI:** application, time calculation, jurisdiction/method variation |
| **R-002** | Religious duties must be considered alongside rights to self and family | PS + FI | [Bukhari 1968](https://sunnah.com/bukhari:1968), [Bukhari 5199](https://sunnah.com/bukhari:5199) | Direct narrations support moderation and multiple rights | **FI:** limits of analogy and particular conflicts; no computed priority algorithm proven |
| **R-003** | Consistent manageable acts can be encouraged | PS | [Bukhari 6465](https://sunnah.com/bukhari:6465) | Citation exists and addresses regular acts within ability | **FI:** avoid making voluntary intentions compulsory; no numerical app goal derived |
| **R-004** | Balance should include one's share of worldly life | PS + FI | [Qur'an 28:77](https://legacy.quran.com/28/77) | Relevant passage exists | **FI:** interpret with context; do not equate it with an app timetable |
| **R-005** | Menstruation-related missed-prayer and fasting treatment differs | PS + FI | [Muslim 335c](https://sunnah.com/muslim:335c) | Narration states the distinction | **FI and privacy:** case-sensitive copy review and no forced disclosure/inference |
| **R-006** | A universal, fixed Prophetic 24-hour timetable should not be imposed | PD + HY | [Foundation F01–F15](../FOUNDATION_v1.md) | Founder-adopted product boundary; sources support moderation in principle | Not a historical proof that no schedules existed; qualified religious and historical review |
| **R-007** | More effective assistance may require fewer app openings | PD + HY | [Local-first policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) | Founder direction | **US:** task completion, perceived helpfulness, distress and unwanted interruption comparison |
| **R-008** | First-release essential features can avoid paid AI | PD + TO | [Local-first policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) | Intended architecture constraint | **TO:** native prototypes, storage, reminders, error and offline tests |
| **R-009** | The blueprint has 106 views/states and 30 sample journeys | PD / inventory | [Screen register](../blueprint/SCREEN_REGISTER_v1.csv), [blueprint](../blueprint/PRODUCT_BLUEPRINT_v1.md) | A **proposed catalog**, not 106 implemented views or usability-tested flows | Automated inventory/integrity check and representative end-to-end usability study |
| **R-010** | Accurate mosque-controlled Iqamah could improve personal reminders | HY | [Mosque proposal](../blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md) | Technically plausible purpose, **not** measured benefit | **TO + US:** 3–5 mosque pilot, source freshness, authorized corrections, unwanted alerts |
| **R-011** | MAWAQIT publicly supports third-party API integration | UN — **contradicted** | [Official MAWAQIT help](https://help.mawaqit.net/en/articles/11991838-can-i-use-your-api) | Says its API is private/not publicly available; offers alternative assistance | Obtain explicit authorization before proposing any third-party integration |
| **R-012** | Masjidbox supports prayer-calendar/export options | TO, vendor-described | [Official Masjidbox help](https://support.masjidbox.com/does-masjidbox-have-a-public-api-for-prayer-times-sfnfd) | Vendor documents iCal and CSV/Excel; says no public prayer API | Terms, access, import fidelity, error handling and reproducible test |
| **R-013** | Local notifications can fully guarantee timely support while app remains closed | UN — **not established** | [Local-first policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) | Document already warns about OS/background constraints | **TO:** device/OS trials under sleep mode, power limits, app force close, zone changes |
| **R-014** | The app is free for users with indefinitely zero infrastructure expense | UN — **not established** | [Local-first policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) | Free-to-user intent is a decision; zero operating expense is not established | Budget for stores, maintenance, security, optional hosted mosque information |
| **R-015** | Multiple AI reports constitute independent empirical validation | UN — **false inference** | Five sources in [original reports](../../research/original-reports/), [foundation](../FOUNDATION_v1.md) | The reports are desk research; foundation already disclaims scholarly and trial validation | Use structured independent reviewer protocol, primary sources and field studies |

## Reading and updating this ledger

- **PS** = primary religious source; **FI** = fiqh/legal interpretation; **TO** = technical/operational; **US** = user evidence; **PD** = product decision; **HY** = hypothesis; **UN** = unverified/contradicted; details in [Research standards](RESEARCH_STANDARDS.md).
- `R-011`, `R-013`, `R-014`, `R-015` are **challenge claims**, not statements endorsed by the project.
- A checked link is **provisional citation verification**, never a general religious certification or technical test.
- Prefer specific PRs that change **one claim status** after presenting its direct evidence, verification date, reviewer scope, competing evidence and applicability.
- If a claim has meaningful jurisprudential variation, record named positions and qualified review without silently assuming one applies to every person.
- Unknown claims remain unknown even if no one has opened an issue about them.

## Review backlog

1. Expand this ledger to every religiously consequential claim in the foundation and mosque flows.
2. Audit technical promises related to iOS/Android offline/background, prayer time calculations and map travel assumptions.
3. Verify all third-party API/licensing assertions against current vendor documentation.
4. Run usability and accessibility studies on the zero-open onboarding/notification choices and record actual observations.
5. Resolve licensing and source-redistribution rights before accepting large external contributions.
