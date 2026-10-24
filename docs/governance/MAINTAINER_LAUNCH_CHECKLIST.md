# Maintainer launch checklist — make contribution safeguards real

**Status:** Operational checklist, **not confirmation that GitHub settings are configured**.  
**Owner:** repository administrator (not yet delegated).  
**Repository:** https://github.com/Safeer1877/islamic-life-companion  
**Prepared:** 24 October 2026.

This document complements [review process](REVIEW_PROCESS.md), [licensing decision](LICENSING_DECISION.md), [licensing rights audit](LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md), and [SECURITY.md](../../SECURITY.md).

## 1. Current settings actually verified

- The repository is public and the maintainer account has admin permission through the connected GitHub integration.
- **Ruleset list returned an empty array (\`[]\`) on 24 October 2026.** That establishes no repository rulesets were listed at that instant. It does **not** prove no legacy branch protection is configured: the connected GitHub App returned HTTP 403 when accessing \`branches/main/protection\`.
- GitHub draft PRs #1 and #2 are present; they represent different independent workstreams and are **not merged**.
- GitHub Actions documentation checks completed successfully for the PR versions inspected; passing link/inventory checks do **not** validate source truth, mobile implementation, fiqh applicability or usability.
- Private vulnerability reporting enablement status was **not established** from an authorized account settings read.
- **Scoped code/docs licenses were approved and merged in PR #6.** The imported-material rights audit remains open; an independent scholarly panel and second human maintainer have not been verified.

**Never mark a checklist item complete merely because a policy document exists or the connected AI said “done.”**

## 2. Restore a verified private vulnerability channel (owner action)

GitHub's built-in private vulnerability reporting is supported for public repositories. Official guide:
https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository

1. Open the repository **Settings**.
2. Under **Security and quality**, select **Advanced Security** (names may vary with account UI).
3. Locate **Private vulnerability reporting** and enable it.
4. Confirm that the repository's Security/Advisories area exposes **Report a vulnerability** to a non-admin reporter, without filing a real secret publicly.
5. Ensure at least one responsible maintainer actually receives security notifications; confirm the expected notification settings.

Use \`SECURITY.md\` to explain safe use after the feature is confirmed. This feature is **separate** from ordinary conduct complaints. A private conduct reporting channel also needs an explicit, tested plan; **do not** treat private vulnerability reporting as an automatic safe conduct-reporting inbox.

**When to check complete:** A contributor can reach a genuinely private disclosure form and a designated maintainer confirms it is monitored.

## 3. Protect \`main\` via a branch ruleset (owner action)

Official GitHub help:
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository

GitHub currently makes branch rulesets available on public repositories under GitHub Free. Admins can configure them. This integration has **read-only** access to listed rulesets, so these steps are **not yet performed**.

**Safe initial configuration proposal:**

1. Open **Settings → Rules → Rulesets → New branch ruleset** (UI labels can vary).
2. Name it \`main-reviewed-changes\`.
3. Target **default branch/main** only.
4. Set **Enforcement: Active** once settings are checked.
5. Require a **pull request before merging**.
6. Block branch deletion and force pushes on \`main\`.
7. Require conversation resolution, and require successful documented CI checks that actually run on both head and merge where applicable.
8. **Review approvals:** Before a second authorized reviewer exists, do not pretend one approval can be supplied independently. Either hold activation of a one-human approval requirement until a reviewer joins, or configure PR+CI protection first and publicly explain the interim manual-review process. Once a second maintainer is onboarded, require one independent approval and prevent stale/bypass approvals if appropriate.
9. Keep admin bypass exceptions narrowly controlled and documented. Treat the owner's emergency access as a transparent exception, not an invisible routine merge shortcut.
10. Verify on a **test PR** that an unreviewed change cannot be pushed directly to \`main\`, and that merging fails when checks/required reviews are missing.

**Dependency detail:** Some proposed CI workflows live only on PR branches (#1 and #2). **Do not require nonexistent status-check names in the \`main\` ruleset before those workflows have been introduced.** If PR #1 is merged first, consider requiring its observed \`Documentation integrity / docs-integrity\` check. When PR #2 merges, consider additionally requiring \`Research slice integrity / research-slice\`, matching GitHub's actual reported check names. Prevent a deadlock caused by a check that never runs.

Rulesets only enforce configured GitHub mechanics. They **cannot** check scholarly correctness, opinion quality, model hallucinations or user consent.

## 4. Contributor licensing and remaining rights audit

The owner approved [MPL-2.0 / AGPLv3 / CC BY-SA 4.0 licensing](../../LICENSES/README.md) in PR #6. Read [Licensing Options & Rights Audit](LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md) for tradeoffs and unfinished source-rights work. Do not automatically license five raw AI reports, modern translations or third-party timetable data.

Adopted steps and remaining checks:

1. **Complete:** Exact, unmodified recognized license texts have been published in a coherent path arrangement.
2. **Complete:** License boundaries are documented in README and `LICENSES/README.md`.
3. **Complete:** Inbound=outbound in `LICENSES/CONTRIBUTION_TERMS.md`. No CLA or mandatory DCO was introduced.
4. Update PR template, source manifest, reviewed content licensing and any license compatibility checks.
5. Check that a third party can independently determine what is safe to fork, redistribute, modify or build upon.

**Do not describe the repository as fully open-source licensed until these decisions exist.**

## 5. Ethical / scholarly review governance

Before releasing religiously consequential copy:

- [ ] Identify qualified actual human reviewer(s) with relevant subject-matter and tradition coverage, reviewed scope and informed consent to name them.
- [ ] Record versioned, exact user-facing copy and behavior, recognized disagreements and reviewer disposition.
- [ ] Publish correction/withdrawal process that protects confidential personal information.
- [ ] Never use a model-generated summary or self-reported contributor title as doctrinal sign-off.
- [ ] Distinguish **mosque administrative authorization** from scholarly qualification.

## 6. External-contribution readiness release gate

- [x] Licenses and inbound=outbound terms approved, scope notice published. **Third-party and imported-source rights audit is still open.**
- [ ] Admin-verified branch ruleset protecting \`main\`, shown to enforce as tested.
- [ ] Real private vulnerability channel and conduct-reporting path with responsible maintainers.
- [ ] Reviewed provenance and open/unknown claims advertised honestly.
- [ ] Contributors can submit source corrections without using sensitive personal records.
- [ ] Minimal reproducible technical checks and targeted independent review expectations documented.
- [ ] At least one real maintainer consistently triages issues and PRs.

**Until then:** Accept evidence and review suggestions cautiously; do not organize a mass recruitment campaign or imply that submitted code will be automatically accepted/relicensed.
