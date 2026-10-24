# Maintainer launch checklist — make contribution safeguards real

**Status (verified 25 October 2026):** The `main` ruleset and required-check negative test are verified. Confidential report receipt, separate conduct reporting, source rights and qualified human review remain open.  
**Owner:** repository administrator (not yet delegated).  
**Repository:** https://github.com/Safeer1877/islamic-life-companion  
**Prepared:** 24 October 2026.

This document complements [review process](REVIEW_PROCESS.md), [licensing decision](LICENSING_DECISION.md), [licensing rights audit](LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md), and [SECURITY.md](../../SECURITY.md).

## 1. Historical snapshot and current verified state

**Original snapshot from early 24 October (historical, now superseded):** The initial ruleset listing was empty and the connected GitHub App returned HTTP 403 on the legacy protection endpoint. At that time PRs #1 and #2 were drafts, not merged. This records what was known *then*, not the current configuration. The connection's ability to read a ruleset does not mean it can administer settings.

**Verified from the GitHub repository API after owner setup:**

- Active ruleset `main-branch-protection` (ID `25786531`) targets the default branch (`main`), lists no bypass actors, requires a PR and resolved review threads, and blocks deletion/non-fast-forward pushes.
- Required GitHub Actions jobs: `docs-integrity`, `license-scope`, `original-provenance`, `research-slice`. Required approving reviews: **0**, while no second independent maintainer has been established. CODEOWNERS alone is not an approval gate.
- In [test PR #12](https://github.com/Safeer1877/islamic-life-companion/pull/12), `docs-integrity` intentionally [failed on a nonexistent relative link](https://github.com/Safeer1877/islamic-life-companion/actions/runs/40113876824); the other three required jobs passed. GitHub returned `mergeable_state=blocked`. The PR was closed **unmerged** and the deliberately faulty file removed from the test branch. This verifies one required-check rejection case, **not** a direct-push test or all possible access paths.
- PRs [#1](https://github.com/Safeer1877/islamic-life-companion/pull/1), [#2](https://github.com/Safeer1877/islamic-life-companion/pull/2) and licensing [#6](https://github.com/Safeer1877/islamic-life-companion/pull/6) are merged.
- Owner reports enabling private vulnerability reporting; **non-admin access, delivery and actual inbox monitoring have not been independently tested**. A separate confidential conduct-reporting route does not yet exist.
- No application, user study, scholarly approval, physical-device reliability result, complete imported-source rights audit or appointed second maintainer has been established.

Recheck time-sensitive GitHub settings before a release. The four CI jobs verify document consistency, **not** religious, privacy, user or device safety.

## 2. Verify the reported private vulnerability channel (owner action)

GitHub's built-in private vulnerability reporting is supported for public repositories. Official guide:
https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository

1. Open the repository **Settings**.
2. Under **Security and quality**, select **Advanced Security** (names may vary with account UI).
3. Locate **Private vulnerability reporting**. The owner reports it is enabled; verify this rather than assuming operational receipt.
4. Confirm that the repository's Security/Advisories area exposes **Report a vulnerability** to a non-admin reporter, without filing a real secret publicly.
5. Ensure at least one responsible maintainer actually receives security notifications; confirm the expected notification settings.

Use \`SECURITY.md\` to explain safe use after the feature is confirmed. This feature is **separate** from ordinary conduct complaints. A private conduct reporting channel also needs an explicit, tested plan; **do not** treat private vulnerability reporting as an automatic safe conduct-reporting inbox.

**When to check complete:** A contributor can reach a genuinely private disclosure form and a designated maintainer confirms it is monitored.

## 3. Maintain tested protection on `main` — configured

The [official ruleset documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository) explains owner settings; the connected integration can read but cannot edit the ruleset.

**Configured:** default branch PRs, resolved conversations, prevention of deletion/force pushes, four correctly named required CI jobs (`docs-integrity`, `license-scope`, `original-provenance`, `research-slice`) and no listed bypass actors.

**Demonstrated enforcement:** The ordinary, non-draft [PR #12](https://github.com/Safeer1877/islamic-life-companion/pull/12) deliberately broke a local Markdown link. The [required check failed](https://github.com/Safeer1877/islamic-life-companion/actions/runs/40113876824); the other checks passed; GitHub blocked the otherwise textually mergeable PR. It was closed without merge.

**Remaining decisions:** No destructive direct-push test has been performed. When a genuine second qualified maintainer exists, consider independent approval requirements without self-review deadlock. Periodically check job names, settings and exceptions. Rulesets do not substantiate religious interpretations or real-device behavior.

## 4. Contributor licensing and remaining rights audit

The owner approved [MPL-2.0 / AGPLv3 / CC BY-SA 4.0 licensing](../../LICENSES/README.md) in PR #6. Read [Licensing Options & Rights Audit](LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md) for tradeoffs and unfinished source-rights work. Do not automatically license five raw AI reports, modern translations or third-party timetable data.

Adopted steps and remaining checks:

1. **Complete:** Exact, unmodified recognized license texts have been published in a coherent path arrangement.
2. **Complete:** License boundaries are documented in README and `LICENSES/README.md`.
3. **Complete:** Inbound=outbound in `LICENSES/CONTRIBUTION_TERMS.md`. No CLA or mandatory DCO was introduced.
4. **Completed for the current documents:** the PR template, source manifest, license map and license-scope integrity check were published. **Remaining:** future dependency compatibility, authorship and imported-source rights verification.
5. Check that a third party can independently determine what is safe to fork, redistribute, modify or build upon.

**Scoped open licenses are published; they do not prove permission to relicense third-party passages, modern translations, archived AI reports or future imports.**

## 5. Ethical / scholarly review governance

Before releasing religiously consequential copy:

- [ ] Identify qualified actual human reviewer(s) with relevant subject-matter and tradition coverage, reviewed scope and informed consent to name them.
- [ ] Record versioned, exact user-facing copy and behavior, recognized disagreements and reviewer disposition.
- [ ] Publish correction/withdrawal process that protects confidential personal information.
- [ ] Never use a model-generated summary or self-reported contributor title as doctrinal sign-off.
- [ ] Distinguish **mosque administrative authorization** from scholarly qualification.

## 6. External-contribution readiness release gate

- [x] Licenses and inbound=outbound terms approved, scope notice published. **Third-party and imported-source rights audit is still open.**
- [x] Active `main` ruleset and four required checks verified; deliberately failing PR #12 was blocked without merging.
- [ ] Real private vulnerability channel and conduct-reporting path with responsible maintainers.
- [ ] Reviewed provenance and open/unknown claims advertised honestly.
- [ ] Contributors can submit source corrections without using sensitive personal records.
- [ ] Minimal reproducible technical checks and targeted independent review expectations documented.
- [ ] At least one real maintainer consistently triages issues and PRs.

**Until then:** Accept evidence and review suggestions cautiously; do not organize a mass recruitment campaign or imply that submitted code will be automatically accepted/relicensed.
