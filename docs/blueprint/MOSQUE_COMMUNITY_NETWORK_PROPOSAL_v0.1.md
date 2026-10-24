# Mosque & Community Information Network — Product Decision v0.1

**Decision date:** 24 October 2026  
**Status:** Accepted as a **staged future direction**, not an approved first-release requirement; security, fiqh, legal and technical details must be validated.  
**Parent specifications:** [Product Blueprint v1 with v1.1 policy](PRODUCT_BLUEPRINT_v1.md), [Free, local-first, zero-open policy v1.1](LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md), [Islamic foundation](../FOUNDATION_v1.md).  
**Scope:** Mosque profiles, authorized editors, prayer-time and Iqamah data, optional announcements, trusted educational resources, and carefully gated community capabilities.

> **Mission:** One reliable update from an authorized mosque should help many people make appropriate real-world decisions, ideally without opening the app. The person's private life stays theirs. The mosque provides information; it does not gain visibility into users' lives.

## 1. What we are deciding

**Yes, reserve a mosque/community integration layer in the product.** Do **not** launch it as an Imam social-network feature, add a fifth main tab, force user accounts, or make it a prerequisite for the personal planner.

Distinguish three things:

1. **Mosque record (institution):** A durable public identity and calendar independent of any one employee, Imam or volunteer. It can be discovered, followed, corrected and transferred to another authorized team.
2. **Mosque management team (operations):** Authorized representatives can maintain factual information; roles can include Imam, trustee, committee member and volunteer. A mosque administrator is not automatically a scholar.
3. **Religious contributor (education):** A separately identified and reviewed Imam or scholar may eventually contribute attributed, scoped educational material. Mosque ownership verification **never** certifies the religious correctness of every answer.

The value proposition is **accurate mosque facts applied to personal planning** rather than another generic mosque-management suite, social feed or fatwa chatbot.

### Why this addition makes sense

- Existing personal planner already uses prayer windows, selected congregation information, user-set departure cues and uncertainty labels.
- A verified mosque-controlled Iqamah schedule helps resolve a genuine data-quality gap; the mosque may know things that calculation methods cannot, such as multiple congregations or a one-off schedule change.
- A mosque can communicate to many people once; a person's app can consume only the categories and times they selected.
- This feature creates network and operational costs, so preserve a **standalone, usable offline personal core** even if this entire layer does not exist.

**Non-goals:** livestream comments, follower leaderboards, public worship history, geofenced attendance records, private member lists, viral group chat, unmoderated direct messages, payment processing, automatic religious verdicts, mosque ranking by piety, or habitual app-opening campaigns.

## 2. Competitive reality and integration ethics

As of the October 2026 research review:

- **My-Masjid** describes a free mosque-admin-managed timetable, prayer information and announcements that synchronize across displays and phones: https://my-masjid.com/
- **Masjidbox** documents prayer-time calendar subscriptions (iCal) and CSV/Excel exports, but states it does **not** offer a public API for prayer times: https://support.masjidbox.com/does-masjidbox-have-a-public-api-for-prayer-times-sfnfd
- **MAWAQIT** explicitly says its API is private, not publicly available: https://help.mawaqit.net/en/articles/11991838-can-i-use-your-api

**Strategic implication:** Never require mosque staff to duplicate a timetable in yet another dashboard if an **authorized, sustainable, permitted** import or subscription exists. Prefer explicit permission, a public authorized calendar/feed, a manual CSV import supplied by the authorized mosque, or a direct official entry. **Do not scrape or call restricted/private APIs** simply because unofficial code examples exist. Verify permission, technical freshness and terms before any interoperability promise.

No market-size, mosque-adoption, availability or pricing estimates in this research are treated as proven product outcomes.

## 3. Product phases and dependencies

| Phase | What users gain | What mosque staff do | Release dependency |
|---|---|---|---|
| **P0 — Existing personal core** | Manually select a mosque or source; see **sourced/dated** Iqamah where available; choose local reminders. An empty or user-confirmed record remains useful but clearly labeled. | None required. | Existing v1 bounded mosque-information capability; reviewed timing guidance. |
| **P1 — Pilot verified mosque records** | A mosque's maintained location, contact, facilities, Iqamah/Jumu'ah schedules and selected alerts. | Claim/manage an institution and update factual schedule. | Verified authority, moderation, audit log, update freshness, safe opt-in delivery, cost feasibility and live pilot. |
| **P2 — Structured announcements and events** | Subscribe to chosen event categories; see important changes without scrolling. | Post dated, expiring, moderated announcements/events. | Successful P1 and demonstrably useful/nonintrusive notifications. |
| **P3 — Attributed educational resources** | Find sourced articles/recordings/class information from identifiable qualified contributors. | Approved contributors publish reviewed resources; corrections possible. | Named scholars/content review, takedown process, scope limits, local fiqh differences. |
| **P4 — Groups, volunteering and Q&A** | Optional moderated participation for particular community needs. | Authorized moderators manage invites, reports, safeguarding and records. | Dedicated moderation, safety, privacy, abuse prevention, support funding and measurable need. |

**Do not build P3/P4 merely because P1 succeeds.** A mosque schedule publishing tool and a chat community have very different abuse and operating costs.

## 4. Identity, trust and role permissions

| Role | May do | May NOT assume |
|---|---|---|
| **Ordinary person (no account required)** | Discover public mosque information, select/follow locally, manually set alerts, report suspected inaccuracies. | Access any person's following list, prayer attendance or private routines. |
| **Unverified community suggester** | Submit a suggested mosque or correction for review, without claiming ownership. | Publish official Iqamah or an official announcement. |
| **Verified mosque owner contact / trustee** | Claim administrative control, manage authorized editors, approve factual updates or revoke access. | Issue app-wide religious rulings; view followers' private schedules. |
| **Delegated schedule editor** | Maintain timing entries and factual facility details within assigned scope. | Manage owner verification, export follower identities, publish content beyond permission. |
| **Delegated announcements editor** | Post structured announcements and events within allowed categories. | Force notifications to all users; access their private data. |
| **Imam or scholarly contributor** | Publish attributed education only after separate qualification/scope review, if P3 is launched. | Claim an app-wide fatwa authority; access confidential questions without authorization. |
| **Platform trust & safety reviewer** | Resolve competing claims, correct misinformation with audit trail, suspend impersonating editors. | Quietly alter doctrinal content without a documented editorial basis. |

**Verification means:** "this representative is authorized to manage this mosque's record." It does not mean: "every statement from this person is a universal religious ruling."

### Minimum authority verification process (P1 pilot)

1. Community suggestion may create a **provisional, unclaimed listing** with public location/source only; plainly label it unverified.
2. Claimant must identify the mosque and a role; provide a verifiable official contact channel or documentary authorization from the recognized management.
3. Reviewer independently checks authority using a trusted publicly listed contact or other reliable out-of-band procedure; do not accept self-uploaded identity text or account possession alone as decisive evidence.
4. Review competing ownership claims; prevent duplicate records. Escalate disputes rather than let first claim win.
5. Record verifier, verification method category, date, scope, and permitted editors privately; **never publish identity documents**.
6. Allow transfer of ownership and immediate revocation when an Imam/committee member leaves; enforce authentication, authorization checks and audit history on every write.
7. Public label shows "managed by a verified representative" only while the operational verification is active. Provide an accessible report/correction path.

The exact evidence burden varies by jurisdiction. Keep stored proof minimal and retention-controlled.

## 5. Scope of a mosque profile

**Minimal public record:**
- Stable mosque ID; official and alternative/transliterated name, language variants.
- City/time zone and public map location/address (not any person's private home or inferred live location).
- Optional published contact and accessibility/facility data, with source and last confirmation.
- Optional opening information and multiple entrances where confirmed.
- Timetable entries distinguished by **prayer start/window**, **Adhan**, **Iqamah/congregation**, **multiple congregations**, **Jumu'ah session(s)**, and **Eid/Ramadan exception(s)**.
- Publisher/verification label, source URL or management confirmation, update timestamp, effective date range, and data freshness status.
- Announcement/event entries only in later phases, with category, location, session dates, expiry and moderation state.

**Do not assume:** A mosque's published Adhan equals Iqamah; a calculated window equals an official mosque timetable; all Fridays have identical Jumu'ah schedules; a Ramadan change applies all year; a single Hanafi/majority timing method works universally; wheelchair/ablution/women's access exists without a sourced claim.

**Time record example (illustrative field schema, not actual timings):**

~~~text
mosque_id; schedule_version; source_type; publisher_id
event_type: Iqamah | Adhan | Jumuah session | Eid session | other
prayer_or_session; local_date; local_time; IANA_time_zone
effective_from; effective_until; exceptions; recurring_pattern
published_at; last_confirmed_at; last_checked_at; verification_state
supersedes_version; status: current | uncertain | withdrawn
~~~

A change creates a new version and invalidates/corrects affected earlier entries. Historic updates remain in a restricted audit trail for resolving errors and disputes, not for profiling individuals.

**Freshness principles:**
- Freshness is **per data type**, not one generic verified badge; a stable location and a tonight-only Iqamah cannot share the same expiry assumption.
- The mosque can publish an effective date span; the system checks changed/superseded entries.
- Missing, stale or ambiguous Iqamah ⇒ no falsely confident "leave now for X" cue.
- Offline cached entries show their last update. Users can still consult an older timetable with a visible warning, but **do not automatically generate an authoritative upcoming-congregation instruction from known stale data**.
- Confidence must be judged by provenance + effective range + synchronization status, not solely by time since the phone last opened.

## 6. Five end-to-end journeys to design later

### MN-F01 — Person selects a mosque

From existing **S61 prayer detail → S62 mosque choices → S64 mosque detail**. Person searches manually by name/area, inspects source/last updated, and optionally saves the mosque as a preference **on-device**. No account, continuous location or following disclosure is required. No new bottom tab.

### MN-F02 — Authorized representative claims a mosque

Separate, lightweight **management experience** (web/mobile, not a new everyday-user area): search existing listing → request claim → independent verification → assign scoped editor → publish/review first timetable → view history. Unverified claims cannot trigger "official" alerts. Claim review and recovery must not rely solely on control of a single email account.

### MN-F03 — Iqamah schedule change impacts reminders

An authorized editor changes tomorrow's Iqamah and publishes it with correct effective date. On a later successful sync, an opted-in person's device fetches the updated version, checks their chosen reminder + quiet hours, and updates/cancels affected **local** notifications when OS capabilities allow. If their phone is offline or background sync does not occur, **no real-time guarantee** is made. No automatic rescheduling of unrelated user commitments.

### MN-F04 — Two mosques and multiple congregations

Person selects more than one mosque or congregation. Distinct sessions keep distinct source, location, date, travel assumption, alert subscription and eligibility; no silent selection of a "better" mosque. A mosque's changed location/session does not overwrite other mosque preferences.

### MN-F05 — Report, dispute, correction

Person sees a questionable timetable → reports the specific date/event/source → authorized editor or reviewer verifies/corrects → affected entries are withdrawn or republished → optional subscribers are informed only if they opted into material-change messages. An unresolved ownership dispute suspends the **verified** label and relevant official publishing rights; display clearly sourced existing information with caution.

## 7. Communication without turning into social media

**P2 permitted by default only as a future proposal:**
- Structured, mosque-originated announcements: Friday change, class time, Ramadan arrangements, accessibility/service change, time-limited community event.
- User actively follows a mosque and then separately chooses **announcement categories** and interruption windows.
- Messages have category, author/role, created/expiry dates, priority justification and a direct useful action. Expired items stop circulating.
- Prefer a concise lock-screen event update, calendar addition or a read-on-demand page. **No endless feed.**
- Notification budgets/rate limits for mosque editors; no ability to override a person's quiet hours by marking everything "urgent".
- Clear unsubscribe and report controls; no follower identity export, read receipts or attendance inference.

**P3 religious education** is different from operational communications:
- Publish attributed, dated, sourced material and what tradition/interpretation it represents; show corrections.
- An Imam's identity may be displayed with consent, but "verified mosque editor" must **not** be rendered as "verified scholar."
- For personalized fiqh, disputes, relationship issues, or sensitive questions, link to qualified independent advice or reviewed sources; do not promise automated judgments.
- No blanket "the mosque says Islam requires ..." pushed into a user's planner without review and applicability checking.

**P4 groups / direct interactions** are **not approved** for v1 or P1:
- Moderation/safeguarding for harassment, children, volunteer disputes, dangerous guidance, financial requests and privacy is a separate operational undertaking.
- Opt-in membership, group moderators, report/block, content retention limits, limits on direct contact, and separate funding/support are mandatory prerequisites.
- Discussion cannot be mined into personal religiosity assessments or shared with other members by default.

## 8. Separation of public community information from private personal life

The mosque's public **information** may be remotely stored; the person's **life model** stays on-device by default.

- A mosque must not see who has planned attendance, which prayer alerts were delivered, private family calendars, sleep preferences, device locations or religious activity logs.
- Anonymous/aggregated operational counters, if ever introduced, require a privacy review, sufficient thresholds to avoid revealing identifiable users, and user choice where applicable; they are not necessary for P1.
- Prefer manual city/area selection. No perpetual location sampling or mosque geofencing by default.
- Following a mosque does not imply joining its membership list, giving it a phone number or receiving its announcements.
- Platform logging should be restricted to publishing, security and error resolution, with retention limits and protection from exporting detailed subscriber behavior.
- Sensitive inquiries, scholar consultations, volunteer membership and any group chat require separate consent/retention rules.

## 9. Free-use and sustainability constraint

The personal app remains free and useful without the online network. The **P1 pilot should also be free to mosque staff**, with no paywall for factual timetable publishing. Avoid ads, payment processing, donation management and broad media hosting at this stage.

However, ownership verification, security, abuse handling, hosting, monitoring, corrections and notifications all cost time or money. Minimize by:
- Starting with a **small geographically focused, consented pilot** instead of worldwide listing claims.
- Keeping published mosque data mostly static/versioned, with economical cache-aware delivery and local alert scheduling on subscriber devices.
- Offering import/authorized subscriptions rather than requiring another repetitive editing workflow.
- Supporting volunteers/delegated roles while retaining accountable management.
- Deferring group chat, personalized fatwa requests, donations and rich social activity.

**Honesty rule:** Free for users is a deliberate product commitment; "free to operate forever" is not proven. Before broad rollout, measure cost per active mosque and support workload.

## 10. Failure cases and safeguards

| Failure | Required outcome |
|---|---|
| Fake Imam/committee claimant | Claim stays unverified; independently verify before editor rights. |
| Two boards dispute mosque ownership | Freeze verified status and publishing privileges pending documented resolution; preserve evidence. |
| Editor publishes wrong Iqamah | Corrections/versioning; cancel or amend future cues after sync; no false guarantee of delivery. |
| Publisher goes inactive | Timetable expires/loses freshness; mark uncertainty; no fabricated official feed. |
| Mosque changes timetable while device offline | Use cached data with status; do not promise current times or instant notification. |
| Time zone/DST mistake or multiple Jama'ah | Each dated event identifies time zone/session; reject ambiguous publication. |
| Misleading theological or sectarian claim | Distinguish sourced educational claim from binding user instruction; human review/correction; no default doctrinal notification. |
| Offensive announcement or spam | Category/rate limits, rapid reporting, moderation, suspension and appeal. |
| Attempted follower identification | Reject in authorization/privacy model; no public subscriber list. |
| Imam leaves position | Role revoked; mosque remains under verified organizational custody. |
| Mosque and calendar integration terms change | Disable integration safely; retain provenance; use manual source or opt-in import; no unauthorized scraping. |
| User wants zero notifications | Offline planner and mosque look-up remain usable; no nagging. |

## 11. Concrete decision gates: from proposal to pilot

**P1 readiness checklist (all required):**
1. Evidence that ~3–5 real mosques are willing to maintain or authorize import of accurate schedules.
2. At least one no-duplicate-entry mechanism or documented acceptable administrative workload.
3. Independent claim verification + editor delegation/revocation + audit log + dispute response.
4. Source, validity range, data-version and correction flows demonstrated for prayer windows, Iqamah, Jumu'ah and exceptions.
5. Opt-in device-local reminder contract tested in real OS/device conditions, including offline/stale updates and failure.
6. Public information remains separate from user private routines; no user-account prerequisite.
7. Clear support owner, published correction/report workflow, and believable no-paywall operating budget.
8. Qualified Islamic review for any religiously consequential timetable wording or proposed concessions.

**Pilot experiment (proposed; not yet conducted):** Recruit 3–5 mosques and consenting people who use those mosques over 4–6 weeks. Record factual update accuracy against publicly displayed/on-site mosque sources, schedule-change propagation where devices are online, reported stale reminders, editor workload, trust disputes, unwanted alerts, and how frequently people needed to open the app for the information. Measure *usefulness*, not followers or impressions. Provide a baseline of manual/current timetable consultation and compare where practical.

**Proceed** only if published times remain sufficiently reliable and staff effort/cost are manageable. **Narrow or cancel** P1 if there is recurring wrong/stale data, ownership abuse, poor permission compliance, large support costs or demonstrably worse user experience. These are evaluation criteria, **not evidence that the product is already validated**.

## 12. Roadmap decision record

**Adopt now:** The underlying concept, separate mosque-institution identity, operational vs scholarly roles, source/freshness requirements, modular personal-data separation, initial screen and notification interfaces, and deferred group/community roadmap.

**Not adopted for core v1:** Mandatory mosque registration, a special Imam social profile, open Q&A, public groups, permanent community tab, mosque-to-user personal analytics, paid platform, automatic real-time background monitoring, or unrestricted data imports.

**Open for targeted discovery:** Whether to partner with existing mosque tools vs host limited official profiles; claim verification in each jurisdiction; minimum support/correction process; real willingness of staff to update schedules; achievable low-cost operations; how to handle institution-specific jurisprudential conventions without misrepresenting individual obligations.

**UX accounting:** Do not silently increase the original 106 screen/state count. Allocate temporary IDs \`MN-xx\` to **future-only** management and community surfaces in a later design supplement. First-release user paths continue through \`S61–S70\`, existing permission sheets and current prayer-preparation actions. A future management dashboard is a separate role-limited interface, not a user-facing daily tab.
