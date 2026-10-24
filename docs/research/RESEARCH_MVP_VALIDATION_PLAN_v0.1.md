# Research MVP & Validation Plan — Candidate Slice v0.1

**Decision date:** 24 October 2026  
**Status:** **Proposed experimental scope**, not an approved release or a finished MVP. This document selects what to *test*, not what every Muslim needs or which school of jurisprudence should apply.  
**Baseline:** \`PRODUCT_BLUEPRINT_v1.md\`, 106 screen/state records, 30 fictional journey descriptions, [local-first founder policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md), [mobile reliability contract](../architecture/MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md).  
**Founder direction protected:** free for users, local-first, no required AI, consent and humane assistance, minimal unnecessary opens, religiously sourced/practically responsible guidance.

## 1. What we need to prove first

**Main hypothesis (untested):** Compared with a trusted prayer-time source plus a normal calendar/reminder, a compact integrated planner will help selected people handle a recurring, real conflict among worship-related time constraints, work/study/care, protected rest and freely chosen intentions *without increased intrusive phone interaction or guilt*.

We are **not** testing whether a screen count, generic reminders, attractive graphics, or five agreeing AI reviews prove product-market fit.

### Primary task

A participant with a real or realistic schedule:
1. Opens the app voluntarily and completes a **short, skippable structured setup**, no account or AI model.
2. Enters one fixed commitment, one flexible/protected period, and optionally a prayer-time source.
3. Sees a day with an explainable overlap or practical constraint; if none exists, receives no invented conflict.
4. Receives a small set of **reversible choices**, including keep the original plan; nothing labels a religious ruling or silently changes a binding obligation.
5. Selects whether to receive one specific local reminder; all categories were OFF by default.
6. Can use the plan, change it, export/reset and inspect status **offline**. Closing the app and not using it further is a legitimate completion.

**Do not collect histories of sins, menstruation, prayer attendance, personal relationships or diagnosis to make this task work.**

## 2. Three independent research tracks

### Track A — Problem discovery (before declaring a release MVP)

- Interview people with meaningfully different lives (e.g., student, shift worker, caregiver, office worker, disabled person, different supported prayer-timing practices), with consent and no pressure to disclose sensitive religious information.
- Ask for **real recent conflicts and current tools**, not whether they like a narrated product idea.
- Compare established prayer-time source + calendar/reminder with proposed integrated planner; identify whether the app provides a benefit that the existing combination does not.
- Keep source, sample, interview method, recruitment bias and contradictory findings in a repository study record.
- **Stopping rule:** If users do not report recurring solvable coordination problems, or existing tools solve them just as well with less burden, narrow or abandon the integrated approach rather than inflate features.
- **No invented trial counts or effect sizes.** Plan sample/recruitment with a UX researcher; early interviews are exploratory and cannot establish population-wide effectiveness.

### Track B — Tiny native technical spike

Build an unbranded **device-local test harness**, not a commercial app and not headless "always-on" surveillance. It must demonstrate:
- Typed persistent schedule entries, time-zone-aware dates and a few user-selected local notifications.
- On-device queue scheduling and cancellation, 64+ requested instances on iOS, and “scheduled through” reporting.
- Android 14+ exact-alarm-denied/inexact handling, reboot, idle, battery restrictions and permission revocation.
- Changing day/time-zone/DST, recalculation on known app events and a closed-app soak test.
- A **known obsolete mosque event queued before an offline correction** and the resulting unpreventable exposure.
- OS backup/restore and device-to-device transfer visibility for private records.

**Never mark this track passed solely because notifications fired once on a simulator.** Use physical supported devices, dated records and negative scenarios, including denied permissions.

### Track C — One useful end-to-end vertical slice

Build a simple interface for the primary task; assess whether people understand provenance, schedules, alternatives, choice and notification limits. Preserve minimal accessibility, privacy and religious safeguards. It may share screens and omit parts of the master catalog.

## 3. Candidate screen contracts from the existing 106-entry register

The original stable IDs are **reference labels**, not a promise of one screen per ID. The first experiment may combine or simplify their UI. Selection is reversible after user/technical evidence.

| Slice role | Existing IDs | Minimum behavior to test |
|---|---|---|
| **Essential candidate** | \`S01\`, \`S03\` | Clear promise, privately start with no account/network |
| **Essential candidate** | \`S08\`, \`S11\`, \`S12\` | Assistance choice, schedule regularity, editable fixed/flexible commitments; skip is real |
| **Essential candidate** | \`S19\`, \`S20\` | Distinguish confirmed vs unknown; explicit first draft approval |
| **Essential candidate** | \`S25\`, \`S34\`, \`S37\` | Optional Today, editable day plan, create/change one commitment |
| **Essential candidate** | \`S38\`, \`S39\`, \`S40\` | Identify one actual overlap from known data, show rationale, offer keep/adjust/undo |
| **Essential candidate** | \`S74\`, \`M99\`, \`X95\`, \`S33\` | Per-category opt-in, refusal path, truthful queued reminder and freshness-aware notification deep-link |
| **Essential candidate** | \`S79\`, \`S80\` | Inspect/export/reset or delete own local data with a truthful scope |
| **Optional research variant** | \`S15\`, \`S16\`, \`S61\` | Prayer-window data only when person configures a reviewed source; distinct from Iqamah |
| **Specialist / not required to demonstrate core** | \`S17\`, \`S62–S70\` | Mosque directory/routing/official-source editing and departure cues remain separate gated experiments; no assumption of available data |
| **Later unless separately justified** | \`S45/S46\`, \`S76\`, \`M103\`, community accounts, learning, advanced focus | No compulsory weekly app visit, pattern inference, ongoing check-ins or attention-driving engagement |

**No hard commitment to 10, 15, 20 or 106 UI pages.** The implementation team should consolidate flows based on observed tasks and accessibility. All catalog IDs remain for historical traceability.

The added \`research_slice\` column in \`SCREEN_REGISTER_v1.csv\` is **triage only** and does not overwrite historical \`release\` values. It exposes where the older “Core” flag is wider than the actual first experiment.

## 4. First-release “religious boundary” without trying to decide fiqh

For the candidate vertical slice:
- Prayer-window information is **optional** until a named, reviewed timing method or explicitly user-supplied recognized timetable can be chosen. No silent default from city/gender.
- Different astronomical conventions, Asr rules, high-latitude situations, travel, Jumu'ah and individual exemptions are **not solved by planner optimization**. Show supported factual information, narrow ambiguity or abstain/refer.
- An overlapped prayer window may be described factually; do not say the person is sinning, exempt, permitted to combine, or required to rearrange another person's rights.
- “Pause reminders” works without giving a reason and without implying any change in religious obligation.
- Neither a missed congregation nor a missed notification proves a missed obligatory prayer.
- Real implementation needs a **qualified human review of exact copy, source data, relevant schools and applicability** before religiously consequential experiences ship.

## 5. Minimal conceptual domain contract (not a committed stack)

Keep typed provenance separate from product recommendations:

\`\`\`text
LocalProfile { profile_version, assistance_mode, consent_categories, privacy_settings }
Commitment { id, title_optional, starts_at, ends_at_or_unknown, zone, recurrence,
             flexibility, origin, people_affected_flag, last_user_confirmation }
ProtectedPeriod { id, time_scope, user_reason_optional, interruption_policy }
Intention { id, self_selected_goal, flexible_window_optional, status }
ReligiousTimingSource { id, method_or_timetable, provenance, effective_range, applicability,
                        verification_state, scholarly_review_status }
PrayerWindow { start, end, calculation_or_timetable_version, zone, confidence }
CongregationEvent { mosque_label, time, local_date, source, last_confirmation, validity }
Proposal { id, affected_ids, reason, alternatives, known_unknowns, approval_state }
ReminderConsent { category, enabled, approved_event_ids_optional, quiet_hours, revision }
ScheduledCue { request_id, proposed_event, approved_source_revision, scheduled_through,
               OS_state_if_observable }
\`\`\`

**Invariants for implementation tests:**
1. An unspecified value remains **unknown**, never a guessed religious or behavioral fact.
2. A user intention never silently becomes an obligatory act or a missed-prayer verdict.
3. User-visible “changed plan” requires explicit approval for consequential changes.
4. Each alert requires category-level consent and an applicable, sufficiently valid source when timing-dependent.
5. External mosque information does not grant access to the private profile or subscribers.
6. The app must be useful with no account, paid AI or network; unavailable online data must not generate fake entries.
7. Export/erase describe precisely what can be controlled, especially OS backups and copies.
8. A user's silence, non-response, lack of app opening or notification dismissal is not a signal of spiritual performance.

## 6. Evidence collection and research acceptance

| Experiment | Minimal observed outcome to record | Failure conditions to record |
|---|---|---|
| Problem discovery | Participants describe actual coordination problems and current workaround; whether integrated experience adds value | No recurring problem, user distrust, existing tools are simpler |
| Setup and first plan | Task completion, skipped questions, time to meaningful plan, corrections, misunderstood source | Mandatory sensitive disclosure, inability to skip, fake assumptions |
| One conflict | Participant can explain what changed and how to undo; no religious rule silently asserted | Harmful changes, unclear alternatives, wrongly inferred exemptions |
| No-notification path | Individual controls remain visible with OS permission denied | Repeated prompts, blocked app, falsely promised alert |
| Queue/closed-app test | Real pending and actual presented-alert logs by device/OS/conditions | Stale departure cue, false scheduled-through date, missing delivery, unobserved delivery incorrectly counted |
| OS backup test | Exact data classes restored in cloud vs device-transfer cases | Private data unexpectedly copied; user didn't understand loss or backup |
| Accessibility | Screen-reader, RTL/Urdu/Arabic where supported and large-text task review | Incorrect reading order, truncated times, confusing source/provenance |
| Return after absence | User easily corrects stale assumptions; no shame or forced weekly action | False confidence or insistence on repeated app visits |

**No pre-established success rate is claimed.** A researcher should predefine task-specific acceptance thresholds, sample selection, risk severity and stop criteria before the studies, then publish both successful and failed results.

## 7. Clear exclusions from the first experiment

- Public mosque registry, verified Imam accounts, groups, user-to-Imam Q&A, member lists, announcements, hosted timetable management, or automatic crowd-sourced corrections.
- Automatic calendaring across external accounts, reading phone usage, persistent background location monitoring and entitlement-dependent phone blocking.
- Generative AI planner, fatwa chatbot, “trained Islamic manager”, learned piety metrics or invasive inferred states.
- Full 106-state implementation, full-device multi-platform parity and global fiqh coverage.
- Claims that notification support works indefinitely without a launch, or that no support server will ever be needed.

**A scope reduction is not a change to the vision.** It is a refusal to spend developer effort on assumptions before testing them.

## 8. Go/no-go gates and work order

1. **Licensing and rights:** Founder selects usable code/documentation licenses and resolves imported material rights; before asking contributors to implement.
2. **Evidence and qualified review:** Catalog normative claims, appoint actual scholarly reviewers for intended prayer copy, consult prospective users on the specific coordination problem.
3. **Technical proof:** Deliver a minimal native device spike including failed/denied/unopened cases and backup policy verification.
4. **UX experiment:** Compare baseline prayer information + normal calendar against the integrated vertical slice.
5. **Iteration decision:** Extend only if results show useful differentiation without unacceptable religious, privacy or notification harm.
6. **Separate mosque pilot later:** Actual consented organizations, ownership proof, support capacity, authorized data access and correction cycle.

**Decision required after research, not before:** Exact first release feature list, languages, launch region, architectural stack, supported jurisprudential sources, OS version range and economic sustainability. Do not present them as already solved.
