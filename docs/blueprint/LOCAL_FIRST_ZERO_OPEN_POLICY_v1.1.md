# Local-first, zero-open, free-to-use product policy — v1.1

**Decision date:** 24 October 2026  
**Status:** Founder direction locked for first release; behavioral and platform details proposed until tested.  
**Applies to:** `PRODUCT_BLUEPRINT_v1.md`, `SCREEN_REGISTER_v1.csv`, visual design handoff and all future implementation plans.

> **Live your life. Not inside an app.** The product succeeds when users can attend to their real responsibilities with useful, quiet support and without needing to open the application every day.

## 1. Binding product decisions

1. **Free for end users:** First release has no mandatory subscription, purchase, paywall or paid AI quota. No advertising or engagement-driven monetization is planned for v1. Product operation may still have developer/publishing expenses; do not promise zero operating cost.
2. **Local-first:** Private onboarding answers, commitments, preferences, reminders and the current plan are kept on the user's device by default. Core planning does not require creating an account or a continuously available backend.
3. **No required AI:** All essential first-release journeys must work without a language model, AI subscription or AI service account. An AI chat tab is not a required feature.
4. **Background-first, not constant engagement:** The default outcome of an ordinary well-configured day may be **zero app launches**. Necessary information is available through user-selected local alerts or lightweight system surfaces where genuinely supported.
5. **User-controlled interruptions:** Every proactive category is opt-in; frequency, hours and dismissal are adjustable. Disabling notifications must never disable planning or access to information.
6. **Religious integrity is independent of AI:** Applicable prayer windows and related rules come from a documented, reviewed source and an explicitly configured method; the system does not invent rulings, concessions or mosque Iqamah times.
7. **No covert observation:** No always-on GPS, microphone, reading messages, hidden app-usage collection or spiritual scoring. Optional access is explained just before permission is requested.
8. **Reversible assistance:** Suggestions are proposals. Consequential plan changes require approval. The person can pause, correct, export and erase their data.

The policy governs the existing screen catalogue. Do **not** redesign 106 screen/state entries or add new tabs simply to accommodate these decisions.

## 2. Distinguish on-device automation from AI

| Capability | First-release approach | AI required? |
|---|---|---|
| Ask onboarding questions and conditional follow-ups | Deterministic, adaptive question flow; freeform note optional, not automatically interpreted | **No** |
| Maintain work, class, care, sleep and protected-time commitments | On-device storage, recurrence and user editing | **No** |
| Display configured prayer windows | Reviewed methods/timetables and local calculations where valid; expose source and uncertainty | **No** |
| Mosque congregation information | Only sourced, dated entries or user-confirmed information, with staleness visible | **No** |
| Prepare selected reminders | Schedule supported device-local notifications; display fallback in-app if disabled | **No** |
| Offer basic conflict alternatives | Explicit constraints (fixed/flexible, capacity, selected rules); show options and request approval | **No** |
| Respond to user-reported change | Simple edit controls, prefilled options and clear affected-commitment preview | **No** |
| Optional natural-language interpretation | Possible future opt-in enhancement with data minimization and clear fallback | **Optional, later** |
| Personalized religious ruling or personal moral judgment | Prohibited; qualified scholarship and verified content required | **Never delegated to AI** |

The term **intelligent assistance** describes correct product behavior, not a promise of machine learning. Any future AI requires a separate privacy, cost, failure, usability and religious-safety review.

## 3. The zero-open experience: the primary product journey

### A. Initial setup (intentional app opening)

The person opens the app once to select assistance level, priorities, broad schedule, protected periods, prayer-source preference and intentions. Sensitive questions remain optional. The app summarizes its understanding, creates a **draft**, and requires the person to confirm it. No cloud account, payment or AI connection is required.

A user can finish with **on-demand only** and zero enabled alerts. Others may deliberately enable one or more reminder types after seeing the expected benefit.

### B. Ordinary day (zero opens is valid)

1. A locally stored, approved plan exists.
2. The device schedules reminders only for categories the person explicitly enabled.
3. At an appropriate moment, a short notification may show one actionable piece of verified or confirmed information.
4. If no useful and permitted interruption exists, **nothing happens**.
5. The plan stays accessible when the person chooses to open the app, including offline.
6. No "come back", streak, daily check-in, motivational campaign or artificial engagement prompt is generated.

**Example:** A worker requests a departure cue for a chosen mosque congregation. If the Iqamah entry is current, source is known, and the user selected this alert, the cue may appear at their configured preparation time. It must not claim guaranteed timely arrival, say the prayer was missed, or use an unverified Iqamah as an established fact.

### C. Exceptional day (minimum necessary interaction)

If a routine is disrupted, only **known** changes should drive automatic checks. A user-entered schedule change can generate an on-device conflict preview. The person chooses whether to keep, shorten or move flexible activities. Without evidence of a disruption, the app does not pretend to know what happened.

If the device has a supported direct-notification action, one tap may accept a reversible preference or open the smallest appropriate screen. Do not assume quick actions, live widgets or background triggers behave identically on all devices.

### D. Weekly and long-term cycle

Optional review is available **on demand**. A weekly notification is off unless requested. A person who has not opened the app for weeks is not treated as a failure. On eventual return, flag outdated assumptions neutrally and offer an efficient correction path.

## 4. Interruption decision contract

For every proposed outward-facing interruption, require:

- **Consent:** Did this person enable this exact category and applicable hours?
- **Specific usefulness:** Is there an immediate, identifiable decision or preparation benefit?
- **Evidence:** Is the relevant time or context confirmed, suitably sourced, and fresh enough?
- **Feasibility:** Would the action be realistically possible, without pretending to know unavailable data?
- **Respect:** Does the alert avoid protected/quiet periods unless separately authorized?
- **Interaction cost:** Can the message stand alone without forcing an app launch?
- **Expiry:** Does the alert become invalid after an event? If so, do not show a stale call to action.
- **Failure fallback:** If permissions, background delivery or data are unavailable, is there a truthful manual alternative?

If a nonessential interruption fails these checks, remain silent. A requested reminder can follow its configured parameters, while still respecting verified data and device constraints.

**Suggested content rule:** One clear fact + optional single action + source/uncertainty when relevant. No guilt, devotional scoring or implication that notifications are proof of worship.

## 5. Screen and flow changes to the existing blueprint

Keep existing screen IDs. Adjust their purpose and success tests as follows.

| Existing screen / state | Required v1.1 interpretation |
|---|---|
| **S01–S03** welcome/private entry | Explain free use, private local start and quiet assistance. No paywall, AI prompt or mandatory account. |
| **S08–S20** onboarding and draft | Branching forms/question cards rather than dependent AI conversation. A useful approved plan can be completed fully offline. |
| **S25** Today | Useful on request, **not** a daily opening requirement. An empty or quiet day is valid. |
| **S26–S33** context and notification destinations | Information should stand alone when practical. Any notification deep link checks freshness on opening. |
| **S34–S47** plan and conflict routes | Basic alternatives computed on-device from known constraints. No generative model needed. |
| **S48–S60** voluntary intentions | No streak pressure or forced engagement; opt-in reminders only. |
| **S61–S70** prayer and mosque | Source and date accuracy are required; an unverified Iqamah does not trigger a confident departure instruction. |
| **S71–S81 / M99** preferences, privacy and reminders | Clear per-category opt-in, quiet hours, offline status, erase/reset and no-notification alternative. |
| **X95 and other offline/denied states** | Workable manual path; core functionality remains available. |

### Acceptance journeys for design and QA

**ZO-01 — Setup with no account, no AI and no notification access:** Complete S01–S20, confirm a draft routine, then close the app. Reopen offline; the approved plan still exists.

**ZO-02 — Seven days without opening the app:** An ordinary user with only two consented event reminders receives only those relevant reminders when device delivery permits. No engagement nudges, streak prompts or forced weekly check-in.

**ZO-03 — No notification permission:** The person can still see prayer source information, commitments, intentions and plan alternatives when opening the app. No repeated permission pressure.

**ZO-04 — Mosque schedule becomes stale:** No confidently worded Iqamah departure alert is issued from a stale unverified entry. The app offers source-check information on request and does not fabricate a replacement.

**ZO-05 — AI unavailable forever:** All core setup, calculation, planning, editing and opted-in local reminders work exactly as designed. No hidden paid API calls.

**ZO-06 — Shift worker / caregiver:** Rest and care boundaries remain respected; the product does not flood the person with fixed-day reminders. Existing obligatory prayer guidance is applied only within reviewed, relevant limits.

**ZO-07 — Changed plans:** Person edits one commitment; app identifies affected optional plans and offers choices. It does not silently move them or infer religious negligence.

**ZO-08 — Return after absence:** The app welcomes the person without reproach, flags assumptions that may be outdated, offers optional review and lets them continue unchanged.

These scenarios add coverage to the existing 30 user flows; they do not create eight new full screens.

## 6. Cost and privacy implications

- Prefer on-device computation, data persistence and local notification scheduling.
- Do not require server accounts, usage analytics, paid push providers or AI inference for core usefulness.
- Optional online services (fresh mosque information, backups or future sync) must have an explicit offline/manual fallback and a clear explanation of their privacy/cost implications.
- Cloud backup, multi-device synchronization and automatic data acquisition are **not part of the required local-first core**; evaluate separately.
- Explain backup/device-loss risk plainly. A completely local experience can lose data if the device is lost or reset without an export or user-enabled backup.
- Launching and maintaining a free application still involves distribution, review, maintenance, accessibility and support costs. Define a sustainable funding plan before any promise of indefinite operation.

### Optional connected mosque network (not a core dependency)

The proposed [Mosque & Community Network v0.1](MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md) may eventually offer verified mosque-managed Iqamah schedules, dated announcements, and user-selected subscriptions. Treat these as **remote public information**, not a reason to move private calendars, family situations or religious behavior logs to mosque administrators or the server. Core app functions work independently. Mosque information may be stale/offline, and automatic background propagation cannot be guaranteed. Community groups, personal religious Q&A, and compulsory mosque membership are not approved for the first release.

## 7. Platform reality and limits

- iOS and Android impose restrictions on background execution, location access, notification delivery and third-party control. Do not promise an always-running intelligence that continuously detects the user's activities.
- Use OS-supported **scheduled local notifications**, not a permanently running background agent, for first-release reminder flows.
- Notification timing or execution may be deferred by device settings, power management or OS policies. Delivery is not a proof of prayer attendance or missed worship.
- Home-screen/lock-screen widgets, watch features, focus controls, calendar ingestion and live activities are **optional, platform-specific enhancements** and are not prerequisites for v1.
- Device time, time zone, location, daylight-saving rules or selected prayer source can change. Show limitations and re-check schedules when the app is permitted to run; do not imply it always receives instant background updates.
- Offline means previously configured commitments, available approved timing data and manual editing are usable locally. **Fresh external mosque information cannot be guaranteed offline**.

## 8. What success means

Measure useful help and absence of harm, not session time or daily active usage alone. Proposed evaluation outcomes:

- User reports that assistance improved a real planning decision.
- Fewer avoidable conflicts within consented routines.
- Low unwanted-interruption rate and strong control over notification preferences.
- Fewer **necessary** app opens for repetitive planning or checking.
- Stable access to key information without internet or AI.
- No rise in guilt, anxiety, fatigue or dependence on the app.

A zero-open day is a valid success, not automatically proof of impact. The person must still be able to obtain help when needed and confirm that the tool was useful.

## 9. Review gates

**Required before shipping:** platform-specific feasibility test for local reminders/background limits; reliable prayer source and content verification by qualified Islamic reviewers; accessibility checks; offline/permission denial tests; privacy audit; user testing of onboarding burden and notification usefulness.

**Can remain later:** on-device AI experiments, external language-model integration, advanced calendar automation, cross-device sync, digital restriction integrations and richer personalized suggestions.

**Change control:** This v1.1 policy supersedes any earlier blueprint copy that suggests compulsory app interaction, AI-dependent onboarding, automatic background surveillance or compulsory online services. The original 106-entry screen register remains the screen index, with the revised interpretations above.
