# Mobile reliability, consent and local-data contract — research draft v0.1

**Prepared:** 24 October 2026  
**Status:** Engineering design constraints, **not** tested platform support. This document corrects specific risks raised by four external AI reviews. It does not approve religious rules or promise delivery behavior.  
**Decision hierarchy:** [founder local-first policy](../blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md) → this implementation-risk contract → platform-specific prototypes and reviewed Islamic source rules.  
**Applies to:** prototype, \`S08/S15/S16/S25/S33/S61/S69/S74/S78–S80/S87/M99/X89/X90/X95\` and future mosque integration.

## 1. Meaning of “zero-open”

**Product objective:** minimize *unnecessary* app openings, not require zero interaction forever. An ordinary configured day may require zero launches if the device already has valid data and the requested alerts are supported.

**Not a guarantee:** The app cannot promise indefinite unattended recalculation, unlimited future alerts, instantaneous cancellation of obsolete mosque times, real-time synchronization while offline, continuous background execution, or successful delivery under every permission, power and Focus mode.

Never impose a weekly app-opening ritual solely as a workaround. Design the system to state the **actual horizon of presently scheduled reminders**, and test whether periodic foreground contact is needed for different configurations. “No notification” can mean (a) user selected none; (b) time not yet due; (c) device delivery suppressed; (d) nothing could be safely scheduled. Do not silently equate these cases.

### Platform evidence checked for this design

- Apple's notification API permits user-authorized local notifications when the app is not running, but queued requests remain until delivery or explicit cancellation: https://developer.apple.com/documentation/UserNotifications/scheduling-a-notification-locally-from-your-app
- Apple's legacy documentation states only the soonest 64 scheduled local notifications are retained, with repeating triggers counted as one; an Apple engineer also discusses a 64-pending-request limit for current requests: https://developer.apple.com/documentation/uikit/uilocalnotification and https://developer.apple.com/forums/thread/811171 . **Prototype the supported API on target OS versions; do not use 64 as a universal calendar-day count or assume infinite delivery.**
- Apple's background task execution timing is system-directed: https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app
- Android 14 denies \`SCHEDULE_EXACT_ALARM\` by default for many newly installed apps; \`USE_EXACT_ALARM\` is restricted to qualifying alarm/calendar use cases subject to Play policy: https://developer.android.com/about/versions/14/changes/schedule-exact-alarms
- Android alarm scheduling, permissions and inexact fallback: https://developer.android.com/develop/background-work/services/alarms
- Apple explicitly says notification delivery is attempted, not guaranteed: https://developer.apple.com/documentation/UserNotifications/

These sources establish boundaries, **not** that our intended behavior has been implemented or observed.

## 2. Consent contract: assistance style is not alert permission

**Default for a new installation: all unsolicited notification categories OFF.** Choosing *Gentle* or *Proactive* changes which in-app suggestions may be shown, not permission for OS notifications, background sensing, remote mosque announcements or anything religiously sensitive.

| Category | Default | Activation requires | Fallback |
|---|---|---|---|
| User-entered commitment reminder | Off | Opt-in for that event or category; preview | Visible in Plan/Today on demand |
| Reviewed prayer-window reminder | Off | Explicit selected prayer(s), timing source/method, buffer, notice | Source/window displayed only on demand |
| User-entered Iqamah reminder | Off | Named mosque/event date, provenance and cautious wording | Manual calendar/view with date and origin |
| Sourced network Iqamah cue (future) | Not available in personal-core prototype | Reviewed valid source + effective range + subscribed mosque + category opt-in | No automatic confident departure cue |
| Voluntary intention or weekly review | Off | Independent opt-in and quiet-hour confirmation | On-demand only |
| Mosque announcements (future) | Off | Separate mosque selection, category subscription and explicit notification opt-in | View on demand, no push |

Only request the OS notification permission when the person chooses an eligible alert, after a clear benefit-and-limits explanation. OS permission alone does **not** enable categories. Never request precise location, background location, calendar or notification access because someone chose “Proactive.”

Quiet hours protect rest by default; a specifically approved individual alert override is explicit, granular and revocable. **A reason-free “pause these alerts” control** must exist without requesting a menstrual, medical, travel or doctrinal explanation. Pausing notifications is not a ruling that a religious duty ceased.

## 3. Reminder sources and validity classes

A scheduled event is not just a title and clock time. Minimum proposed record:

\`\`\`text
reminder_id; notification_category; consent_version
event_id; scheduled_instant_utc; intended_local_time
time_zone_id; calculated_or_source_valid_from; source_valid_until
source_kind: user_entered | reviewed_calculation | mosque_direct | authorized_feed
source_id; source_revision; last_verified_at; last_sync_at
message_class: factual | preparation_option | needs_confirmation
status: proposed | queued | delivered_if_observable | expired | cancelled | uncertain
device_scheduling_timestamp; intended_preparation_buffer; quiet_hour_override
\`\`\`

Actual status transitions must reflect only events the OS/app can observe. A delivered notification is **not** evidence the person saw it, acted or prayed.

Source-specific scheduling rules:

1. **Stable user-entered commitments:** may use OS repeating reminders when recurrence semantics actually match the person's selected local civil time, and cancellation is supported.
2. **Calculated prayer windows:** derive dated instances with a reviewed, explicitly chosen method; respect high-latitude/no-result limitations. Daily changing times are not safely represented as one fixed-time repeating alarm.
3. **Manually entered Iqamah:** date, mosque and confirmation status must be visible. Avoid “official/verified” unless authority and freshness are established.
4. **Future authorized mosque feeds:** publisher revisions, effective ranges, staleness and corrected/deleted events must be versioned. **An offline phone cannot know an amendment published after its last sync.**

For each candidate notification: check explicit consent, horizon, source validity, time zone, event relevance, expiration, quiet hours, queue budget and known permissions before enqueueing. Unsupported or unknown cases become a *manual information path*, not invented timing.

## 4. Already-queued obsolete Iqamah: hard failure boundary

**Counterexample:** At 08:00 the app queues a 17:45 departure reminder from a mosque's 18:15 Iqamah listing. At noon the mosque publishes a change. The device is offline/suspended until 18:00.

The OS may present the old queued text. **The app cannot guarantee a cancellation it never executed.** Therefore “suppress all stale Iqamah reminders” is not a truthful invariant for a disconnected device.

Proposed mitigation hierarchy:
- **Before queueing:** require an explicitly valid date/effective range; limit how far future mosque-derived cues are scheduled; never pre-schedule indefinite firm departure instructions.
- **Message wording:** distinguish “Iqamah last reported at [time] by [source], confirmed [date]” from “leave now” or a guaranteed congregation. Never use a past confirmation to imply a current guarantee.
- **When update arrives:** compare source revision and validity, cancel/replace affected pending requests by stable ID, show affected plan without silently modifying unrelated commitments.
- **When a correction does not arrive:** do not pretend the OS knows. Tell the user in settings/on request how recently the phone checked its source and the reminder horizon; permit turning external-data alerts off.
- **At notification deep link:** re-check what is known and offer current factual options rather than an expired CTA.
- **Release decision pending tests:** If the residual risk remains too high, **do not ship proactive mosque-derived departure cues**; a manual mosque time is still useful.

A message being “last reported at” does not make a wrong reminder harmless. Evaluate misunderstanding and false-confidence harm with real users.

## 5. Queue scheduling strategy — proposed and unproven

When the app is permitted to run:
1. Read current consent, user preference, time-zone settings, approved timing source and pending OS requests.
2. Remove locally identifiable cancelled, expired, superseded or unconsented requests.
3. Create the next dated instances within a conservative, configurable **request-count** and **validity** limit; prioritize requested near-term factual alerts.
4. Persist the queued-intent registry transactionally and reconcile with OS pending requests where API permits.
5. Detect and display a **scheduled-through date** only from requests actually accepted by the OS; do not display a generic seven-day guarantee.
6. On app resume, clock/time-zone change observed by the app, permission grant/revocation observed by the app, OS reboot/startup triggers where supported, or a genuinely delivered source update, re-evaluate. Background callbacks are opportunities, **never guaranteed schedulers**.
7. If OS permissions or precise delivery are unavailable, remain usable and show an understandable manual path.

For iOS, explicitly test the finite pending-request limit using the current \`UNUserNotificationCenter\` API, varying daily prayer instances and several categories. For Android, don't assume a \`USE_EXACT_ALARM\` permission or permission exemption without qualifying and meeting store policy.

Do **not** use background location, cell-tower changes, permanent tracking or silent pushes as covert tricks to force queue replenishment.

## 6. Device backups: local-first is not “never in the cloud”

Native operating systems may back up app data by default:
- Android Auto Backup can include private app files/databases and supports distinct cloud vs device-transfer rules: https://developer.android.com/identity/data/autobackup
- iCloud Backup may include an iOS app's nonpurgeable data. Apple's \`isExcludedFromBackup\` flag provides guidance, **not an absolute guarantee**: https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup

A **device-local architecture alone does not prove that private religious/life information never leaves the phone**. Nor does exclusion alone solve the user harm of irrecoverable device loss.

Before a test build processes real personal data, establish:

1. **Data classification:** sensitive private routines and free-text notes; nonsensitive cached public mosque facts; preferences; reminder metadata; secret keys.
2. **Backup/transfer policy:** explicit desired cloud-backup and device-to-device behavior **by data class and OS version**. Research default choices and user comprehension rather than pretending every platform can enforce identical results.
3. **Storage security:** OS-protected local storage, encryption/key lifecycle where appropriate, least-privileged app access, migration and export safeguards. Encryption claims need implementation evidence.
4. **User disclosure:** plain-language explanation of device backup, third-party system backup settings, loss/restore tradeoffs, and which categories are at risk.
5. **Export/erase:** user-controlled export, data category scope and confirmed local deletion behavior. Never claim that deleting local data deletes existing OS backups, screenshots or exports.
6. **Tests:** on-device backup and restore into another device; observe actual restored records, database, keys, alerts and permission state; test device transfer separately from cloud backup.

**No implementation has been selected yet.** This is a test obligation and risk register, not a claim that encryption, exclusion or restoration works.

## 7. Operational actions must have a real destination

No v1 \`Submit correction\`, \`Submit safety report\` or similar success confirmation may appear without a configured and observable receiving service.

- For a personal-core prototype, **Copy report** or **Open the published contact method** is acceptable, with a clear warning if no recipient/contact is configured.
- For future network service, a report is \`submitted\` only after acknowledged receipt. Offline actions are \`saved locally, not sent\`, and must allow inspect/cancel/retry.
- A religious error report involving private circumstances must not silently upload someone's schedule, faith practice history or family details.
- If no safe destination exists, leave the reporting UI in a disabled/explanatory state; do not fake submission.

## 8. Explicit release tests (none completed)

| ID | Scenario | Observable criterion |
|---|---|---|
| **MOB-01** | iOS local queue >64 dated instances | Document exactly which requests remain pending and fire; app neither crashes nor displays false horizon |
| **MOB-02** | iOS 7- and 30-day unopened soak test | Actual timestamps for scheduled/delivered/blocked alerts, including no-open limitations; no guaranteed success asserted in advance |
| **MOB-03** | Android 14+ denied/revoked exact-alarm permission | No permission-crash, truthful fallback, no fabricated delivery precision |
| **MOB-04** | Background/force-stop, battery saver and reboot | Record actual permission and notification behavior by device/OS; avoid overclaiming |
| **MOB-05** | Time-zone, manual clock, DST and travel while unopened | Identify stale scheduled instances; explain/update when allowed, never silently label old data current |
| **MOB-06** | Mosque timetable changed with offline phone | Inspect already queued message; confirm what **cannot** be cancelled; test cautious text and user comprehension |
| **MOB-07** | Restore/transfer with sensitive data | Verify selected cloud vs device-to-device backup policy, key recovery and notice |
| **MOB-08** | First install: Gentle selected, notifications denied | Zero unrequested alerts and no repetitive permission nagging |
| **MOB-09** | No source/method, high-latitude calculation failure | Abstain from specific timings; avoid fabricated or guessed religious outputs |
| **MOB-10** | Report with no server/contact, offline | No false “sent” status; user knows whether information remains local |
| **MOB-11** | Pause alert category without reason | No religious/health inference, no collected explanation, past cues cancelled only when application can act |
| **MOB-12** | 14-day plan with no AI, account or internet | Existing commitments/editing work offline; actual notification support and limitations logged |

**Go/no-go threshold must be set before tests.** “Prototype runs” is not sufficient. Record exact devices, builds, OS versions, failures, logs, user expectations, risk owner and release decision.

## 9. Open decisions (do not silently decide)

- User-visible reminder coverage/horizon, budget and priority for each OS.
- Whether person-supplied mosque Iqamah may generate a cue, and how uncertainty is expressed.
- Opt-out from cloud backup vs user-selected recoverability, per platform and data sensitivity.
- Product's treatment of Android exact-alarm eligibility and whether an inexact cue is helpful/safe.
- Who will review religiously consequential notification copy and applicability, with named qualifications.
- How sensitive report delivery is implemented before a network service exists.

**Bottom line:** Quiet operation is a worthy product goal; truthfully bounded scheduling and disclosed backup behaviors are prerequisites, not optional implementation details.
