# Independent AI Review Reconciliation — First Batch (2026-10-24)

**Status:** Evidence triage; **not** approved engineering requirements, user validation, a scholarly verdict or a majority-vote determination.  
**Repo baseline reviewed by authors:** \`main\` at \`5205a0fe8938400f0c5de15b73061153b2342328\`; governance draft PR #1 head at the time of reviews \`80ad58ec9a8983dcb09a92ba9dd78169e1bc357b\`.  
**Inputs:** Four user-supplied external model review texts, provisionally called **A, B, C and D** below because tool/provider identities were not supplied in the source texts. Model labels should be added only when the originating user confirms them. Original full reports are not reproduced here.  
**Method:** Group findings by underlying claim, inspect baseline repo wording and reconcile against first-party documentation. Independent source citation or test is required for an issue to be upgraded from plausible to verified. No model's agreement is treated as proof.

## 1. Reliability of the four input reviews

| Review | Repo access claimed | Material limitation | Use in this synthesis |
|---|---|---|---|
| **A** — inline limitations/CF-001–004 | **None:** explicitly could not access repository | Assumes the product promises indefinite no-open function, treats all 106 entries as MVP screens and says fiqh exemptions are inferred; these are not accurate descriptions of the actual baseline | Useful to flag OS limits and a prototype; **not** reliable for file-specific defects or proposed exact corrections |
| **B** — "Independent Forensic Audit" | Reports main and PR commit inspection, selected first-hand source checks | Long original reports were only sampled; no devices, scholarly reviewers or actual users | Strong issue inventory, particularly pre-scheduled notification staleness and differentiated release scope |
| **C** — "Reviewed main ... open draft PR" | Reports repository clone and direct row count | No device/study/scholar tests; Masjidbox API page body and some sources unavailable | Important distinctive issues: mobile default cloud backup, false "submit" actions, source integrity, unclear Gentle-category consent |
| **D** — "Independent Forensic Review" | Reports partial direct access to main and PR | Could not access the full CSV and some PR documents; did not obtain main SHA independently | Valuable technical critiques, but confidence for unread file details and per-method calculation tables is lower |

**Review quality principle:** If the same issue appears in four reports, it is still **one hypothesis until evidence settles it**. Conversely, a unique finding such as backup settings or queued Iqamah invalidation can be critical even if only one reviewer spotted it.

## 2. Reconciled priority register

Status key: **CONFIRMED BASELINE** = directly observed in repo; **CONFIRMED EXTERNAL CONSTRAINT** = found in official platform/vendor documentation; **DESIGN GAP** = missing implementation decision; **NEEDS HUMAN/DEVICE EVIDENCE** = no sign-off/test; **REJECTED AS STATED** = conflicts with actual repo wording or not established; **FOUNDER DECISION** = intentional trade-off, not an externally verified fact.

| ID | Priority | Issue | Status and evidence | Proposed disposition | Independent acceptance evidence |
|---|---|---|---|---|---|
| **RR-01** | Blocker for broad contributions | No approved reuse license or settled inbound rights for code/docs/imported research | **CONFIRMED BASELINE**: main and PR #1 lack LICENSE; GitHub explicitly says public is not automatically open-source licensed | Founder chooses appropriate documented licenses and contributor terms after rights/provenance review; do not add a license arbitrarily | Published actual license texts, scoped exceptions, contributor policy; qualified legal advice if needed |
| **RR-02** | High | iOS finite notification queue and nondeterministic background refresh | **CONFIRMED EXTERNAL CONSTRAINT**: Apple engineer Jan 2026 confirms **64 simultaneously pending notifications per app**; system decides when background tasks execute | Design bounded scheduling, priority/expiry rules, visible scheduled-through horizon and no delivery guarantee. Don't insist on weekly launches | iOS prototype logs pending queue and displayed alerts during closed-app/low-power/time-zone conditions |
| **RR-03** | High | Android exact-alarm restrictions, user revocation, Doze variability | **CONFIRMED EXTERNAL CONSTRAINT**: official Android 14 docs; eligibility for USE_EXACT_ALARM not settled | Require denied-permission/inexact fallbacks and store-policy eligibility decision | Android device/OEM test matrix, permission revoke/restore and timed delivery logs |
| **RR-04** | High | An offline previously scheduled **Iqamah** alert can outlive its source's validity/correction | **DESIGN GAP**, derived from official notification scheduling/cancel API and actual mosque proposal promises | No confident unattended source-dependent cue beyond proven effective period; attach source version/validity; cancel/update only after actual sync; disclose unavoidable stale-notification risk | Device offline when source withdrawn or changed; compare actual notification text and correction propagation |
| **RR-05** | High | "Data stays on device" may be false because of OS cloud/device backup | **CONFIRMED EXTERNAL CONSTRAINT**: Android automatic app backup defaults; iOS iCloud backup includes app data where enabled | Add explicit backup/data extraction policy, plain-language notice, restore/security tests, possible local export alternative; evaluate usability cost of turning backup off | Inspect cloud and device-transfer backup/restore on both platforms, verify exactly which records/keys transfer |
| **RR-06** | High | Current nominal first-release breadth: 79 Core, 17 Bounded, 7 Scholar-gated, 3 Later out of 106 catalog entries | **CONFIRMED BASELINE** via CSV. Criticism that the app has 106 built screens is **false** | Keep IDs for provenance; create a smaller **research-prototype slice** with separate release selection, defer unproven flows and classify source-dependent states explicitly | Task→screen traceability and an independently tested offline vertical slice |
| **RR-07** | High | No evidence that integrated planner beats existing prayer app + calendar for an identifiable user segment | **NEEDS HUMAN EVIDENCE**; repo already says no empirical user tests | Start problem interviews and a baseline comparison before treating adoption/benefit as proved; measure attention burden and harmful reminders | Consented task study/diary and comparative tests, publish negative findings and stop criteria |
| **RR-08** | High | Religious source citations do not determine an algorithm for competing obligations, concessions and prayer methods | **NEEDS QUALIFIED SCHOLARLY REVIEW**; primary texts support broad ethical principles, not an automated fatwa | Preserve F01–F15 safety boundaries; build exact text/behavior/school-variation review charter and abstain or show factual data where not approved | Reviewed, dated exact strings and scenarios by suitably qualified human scholars, with scope and dissent |
| **RR-09** | High | No tested domain schema, time semantics, persistence, export/recovery or crash-safety contract | **DESIGN GAP**; blueprint explicitly excludes implementation architecture | Design minimal types and invariants only after prototype scope is chosen; use local-first storage and conservative failure handling | Unit tests for time zones/recurrence, local persistence, migrations, backup and recoverability |
| **RR-10** | High | Religious and mosque data sources aren't globally verified and v1 mosque directory/route claims lack a confirmed dataset | **DESIGN GAP**; future connected network explicitly gated; third-party APIs restricted | For prototype use manually entered mosque details with source/date, or validated user-authorized imports. Defer hosted directory, routing and verified editor service | Tested source/license terms, controlled timetable examples and later written mosque participation |
| **RR-11** | High | Default selection of "Gentle" or "Proactive" may be mistaken for category-level permission to send alerts | **INTERNAL AMBIGUITY** in old flows, despite general opt-in policy | Explicit notification default matrix: **all unsolicited categories off unless individually enabled**; show when suggestions are only in-app | Fresh-install test with Gentle selected and denied OS permission: no unsolicited alerts or reprompt |
| **RR-12** | High | A public "submit timetable correction" or "contact support" button may have no service recipient | **DESIGN GAP**, no backend present | Label as proposed future flow or route to user-controlled external contact; never say "submitted" without receiving/confirming it | Offline/report task with demonstrable destination and truthful error feedback |
| **RR-13** | High | PR #1 adds governance documents but protections and confidential reporting remain unconfigured/unverified | **CONFIRMED BASELINE/GOVERNANCE**: draft PR, CODEOWNERS isn't enforcement | First merge factual editorial improvements after review; separately configure branch rules and private vulnerability/conduct channel | Negative test PR that cannot bypass protection; safe test of private report receipt |
| **RR-14** | Medium | Historical package checksums don't verify current remote files; HTML/duplicate foundation can drift | **CONFIRMED BASELINE** and PR #1 manifest improvement | Document source-of-truth order; introduce current-tree hashes and reproducible generation or retire derived reader | Rebuild artifacts from source and compare, no broken links |
| **RR-15** | Medium | User-facing accessibility/Urdu/Arabic/RTL principles are specified but untested | **NEEDS USER/DEVICE EVIDENCE** | Select pilot languages explicitly and run screen-reader, bidirectional-copy and dynamic-size tests on actual prototype | VoiceOver/TalkBack plus native RTL/large-text audit with relevant users |
| **RR-16** | Medium | Future mosque identity, corrections, support workload and communications moderation are unproven | **FUTURE RESEARCH**; existing proposal already marks P1–P4 conditional | Retain a small opt-in future pilot and strict operational vs scholarly role separation; do not treat proposed pilot sizes as validated thresholds | Written willingness from real mosques, traceable editor claim/correction and operational cost |
| **RR-17** | Medium | Maintenance and app publishing costs are not proven affordable for indefinite free use | **NEEDS COST EVIDENCE** | Preserve free-to-user founder goal, but maintain honest hosting/store/incident budget | Public itemized small-prototype cost assumptions and later actual expenses |
| **RR-18** | Medium | AI-generated report concordance may be confused for independent validation | **CONFIRMED RISK** already accurately disclaimed in foundation and PR #1 | Continue preserving the originals, require precise primary sources and human review, disclose model provenance | Independent reviewed claims, not votes |
| **RR-19** | Medium | "How does the person know the system is still configured?" | **USER TRUST HYPOTHESIS** | Show expiry/scheduled-through status *when opened*; optional user-selected health-status cue where feasible, never mandatory weekly engagement digest | Comprehension/trust study and device-delivery testing |
| **RR-20** | Medium | Scholarly governance lacks appointed coverage across relevant fiqh approaches | **NEEDS HUMAN ORGANIZATION** | Review charter, scope and funding/contact for named appropriately qualified human reviewers; prevent "all Muslims" capability claims | Documented actual review team and review records before religiously consequential release |

## 3. Claims **not** accepted from the reviews as written

| Reviewer suggestion or allegation | Decision and reason |
|---|---|
| **"Change the product to mandatory weekly opens."** | **Do not accept.** Apple's 64 limit constrains simultaneous queued requests, not the proposition that every user must reopen exactly weekly. Repeating triggers may count as one, but changing prayer times need date-specific logic. Set a test-backed horizon, never invent a universal seven-day cadence. |
| **"The repo promises indefinite autonomous execution with zero opens."** | **Inaccurate as stated.** The baseline says an ordinary well-configured day *may* require zero opens and already warns OS background/online freshness cannot be guaranteed. Clarify horizons, but don't ascribe a guarantee the project did not make. |
| **"The app automatically decides menstruation/travel exemptions."** | **Inaccurate description.** Foundation F02/F09/F14 already prohibits inventing concessions or inferencing sensitive status; exact screen scenarios still need professional scholarly review. |
| **"All 106 screens must ship in MVP; archive all but 15."** | **False premise and unjustified number.** The catalog explicitly includes 106 screens, reusable sheets and exception states. Nevertheless **79 marked Core** creates a real scope-management problem. Use an evidence-based MVP selection; don't delete useful traceability. |
| **"Only astronomical prayer calculation can be in MVP."** | **Unnecessary limitation.** A user-provided or responsibly attributed local mosque timetable may be more suitable in some circumstances. Separate prayer windows from verified mosque Iqamah; never manufacture data. |
| **"All integrations must be abandoned because they require the cloud."** | **Not adopted.** A later optional connected public-information adapter is compatible with the person's local private core, but its availability is never guaranteed offline. |
| **"Mandatory weekly health-check digest."** | **Rejected pending evidence.** It recreates unwanted notifications and does not ensure OS delivery. Offer status and user choice, test whether this reduces anxiety. |
| **"Use location/cell-tower tricks to wake the app and replenish the queue."** | **Not a verified or privacy-appropriate v1 plan.** Requires explicit permissions, may drain battery, and isn't a reliable OS execution guarantee. |
| **"Notification fatigue research proves the app improves Khushu' or balance."** | **Unsupported leap.** General interruption studies do not test this product or a religious spiritual outcome. |
| **"The entire personal planning purpose should be removed until prayer scheduling works."** | **Not an established need.** Personal coordination is the differentiated hypothesis; reducing to prayer-only could remove the very value to test. Compare approaches experimentally. |

## 4. First-party source verification performed for this synthesis

Checks on 24 October 2026; these verify stated *platform* constraints, not this app's implementation.

- **Apple engineer (January 2026)**: 64 simultaneously pending \`UNNotificationRequest\` requests per app: https://developer.apple.com/forums/thread/811171
- **Apple local-notification scheduling/cancel API**: local notifications delivered by the OS even when app isn't running; pending requests remain until trigger/cancel: https://developer.apple.com/documentation/UserNotifications/scheduling-a-notification-locally-from-your-app
- **Apple background strategy**: system decides when a background refresh task runs: https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app
- **Android 14 exact alarms**: special permission denied by default for many fresh installs; fallback and policy needed: https://developer.android.com/about/versions/14/changes/schedule-exact-alarms
- **Android Auto Backup**: eligible app files backed up by default unless configured; modern data extraction and D2D exceptions require care: https://developer.android.com/identity/data/autobackup
- **Apple iCloud Backup**: app data included when enabled unless appropriately excluded: https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup
- **GitHub licensing**: public repository visibility doesn't establish open-source reuse rights: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository

Cited Qur'an/hadith excerpts in the reports **have not been given a new qualified jurisprudential review by this synthesis**. Their conceptual role stays open under RR-08 and RR-20.

## 5. Minimal follow-up issue/PR sequence

### First: governance and accurate disclosure (immediate, documentation-only)

1. Review draft PR #1 and merge **after** editorial link/status accuracy review; don't call the audit independent from the authors of its own foundation.
2. Resolve RR-01 (license), reporting owner/channel, contributor permissions and branch-review enforcement **before major recruitment**.
3. Expand the claim ledger to include RR-02–RR-20 and separate actual endorsed claims from adversarial challenges.

### Second: small specification corrections (documentation-only; distinct PR)

1. Make backup behavior explicit; add default-off category matrix and no-surprise prompting.
2. State that queue horizons are finite and version/freshness-sensitive; **no fixed seven-day promise** before testing.
3. Add the impossible-to-guarantee stale queued Iqamah case and an honest no-data fallback.
4. Specify where correction/feedback flows go, otherwise remove misleading \`Submit\` copy.
5. Add a deliberately selected **research MVP slice** separate from the 106-entry catalog, retaining IDs/legacy traceability.

### Third: proof-of-feasibility (small executable prototypes)

- iOS: 64-request queue, varying day-specific prayer times, time zone/DST changes, reboot, force-quit, OS permission, cancel/replace, 7-day and 30-day **unopened** soak tests.
- Android: exact/inexact alarm contrast, Android 14+ denial/restore, OEM battery limits, reboot, Doze, time zones and scheduled delivery logs.
- Both: local data backup/exclusion, export/restore, loss/recovery and no-network behavior.
- Publish **actual logs, supported OS/device matrix and failure cases**, not confident assumptions.

### Fourth: verification of problem and religious boundaries

- Compare baseline calendar + an existing prayer source against a small integrated planner; focus on **one real recurring conflict** and an explanation/reversible suggestion. Record perceived burden, trust and false prompts, not screen time only.
- Recruit appropriate scholars to review exact released prayer-time method choices, Jumu'ah/travel/illness/menstruation-related copy and conditions. Do not convert product trade-offs into religious judgments.
- Preserve open disagreements and state exactly which traditions/scenarios the first prototype does not support yet.

## 6. Decisions intentionally deferred to the founder

- Code and documentation licensing scope and rights to the imported AI-assisted research.
- Launch jurisdiction/languages and initial representative user groups (for research recruitment, not universal doctrinal defaults).
- Which parts of the inventory to prototype first after problem discovery.
- Whether and when to recruit mosque operators and a second maintainer.

## Bottom-line verdict

**Keep the product direction; sharply reduce the scope of what is claimed to be verified.**

Do not turn "zero-open" into a compulsory weekly-open ritual; do not delete 106 IDs as if they were 106 implemented screens; and do not automatically adopt a model's proposed religious or technical solution.

The first real external proofs should be **a small native notification/backup prototype, qualified religious review of limited exact copy, and comparative testing with people who currently use a prayer source plus a calendar**. The public repository can then document what was learned, including failures, rather than merely accumulating more polished design prose.
