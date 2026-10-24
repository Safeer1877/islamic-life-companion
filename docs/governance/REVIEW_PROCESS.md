# Review and decision process

**Stage:** Public research specification; no application code has been released or tested.

## 1. Who may do what

- **Public contributors** may propose issues and PRs, provide original source citations and report defects.
- **Maintainers** triage, document decisions, edit specifications and approve/merge changes.
- **Independent reviewers** may conduct research, usability, accessibility, legal or technical critiques without being presumed authoritative outside their expertise.
- **Qualified Islamic reviewers** must review religiously consequential wording/rules and the intended user interaction **before** those features are promoted as authoritative or shipped.
- **Product founder/maintainer** retains control of product priorities and roadmap. Governance may evolve transparently through community discussion.

A role, reviewer panel or qualification not actually appointed **must not be claimed**. Reviewer sign-off should have identity/qualification (with consent), decision scope, date, version and dissent recorded.

## 2. Change classification and merge gates

| Change | Review standard |
|---|---|
| Broken links, typos, formatting | Source/diff check and repository integrity test |
| Factual claims, numerical facts, policy or vendor specs | First-hand link, exact wording, dated verification, uncertainty |
| Qur'an/hadith citations | Direct passage/context check; no automatic extrapolation into rulings |
| Fiqh and religiously consequential behavior | **Hold** for appropriate qualified scholarly review; show recognized differences |
| Privacy/security or mosque edit/identity authority | Threat model, data-flow check, safe failure and appropriate specialist review |
| Platform functionality/offline/background claims | Official docs and repeatable device tests (including denial cases) |
| Major architecture or new feature | Founder product decision, feasibility, cost, impact on zero-open/free constraints |
| Claims of real-world effectiveness | Field/user testing with method, sample limitations, and adverse effects |

Every merged normative change should cite the corresponding [claim ledger](../research/CLAIM_LEDGER.md) entry and its status, or create one.

## 3. GitHub workflow (required CI enforced; human gates still open)

1. Keep `main` as the project baseline; use a focused PR, complete the template, record evidence and applicable tests.
2. Confirm documentation/check integrity; review cited claims at their primary sources, noting source-rights limitations.
3. Hold religiously consequential copy for qualified human scholarly review; require explicit privacy/security review for sensitive mechanisms.
4. Record accepted/rejected/deferred decisions in the versioned ledger. Do not change archived raw AI research to imply previously nonexistent validation.
5. After merging, track corrections and remaining review obligations in issues.

**Verified 25 October 2026:** Active `main-branch-protection` ruleset (ID `25786531`) requires PRs, resolved conversations, and four checks: `docs-integrity`, `license-scope`, `original-provenance`, `research-slice`. It blocks branch deletion and force pushes; no bypass actors are listed. Required independent approving reviews are currently **0**, since no second reviewer has been established. CODEOWNERS does not constitute independent approval.

**Enforcement evidence:** A deliberate documentation failure in [test PR #12](https://github.com/Safeer1877/islamic-life-companion/pull/12) made the required [`docs-integrity` job fail](https://github.com/Safeer1877/islamic-life-companion/actions/runs/40113876824); GitHub reported `mergeable_state=blocked` and the PR was closed **unmerged**. A direct-push rejection was **not** tested. Historical initial API results showing zero rulesets are superseded by these later checks.

The [maintainer launch checklist](MAINTAINER_LAUNCH_CHECKLIST.md) records exact status and remaining gates. The owner reports enabling private vulnerability reporting, but **actual receipt** and a separate confidential conduct channel are not verified. The connected integration cannot edit ruleset settings. None of these mechanics replace independent qualified reviews, source-rights clearance or real-device/usability testing.


## 4. Resolving disagreement

- State precisely which claim is disputed.
- Prefer direct and original evidence over a model's confident synthesis.
- Record relevant qualified alternative positions and limits rather than silently generalizing.
- For religious applicability, request a reviewer with relevant recognized expertise; preserve dissent when real.
- Where evidence cannot settle a founder design preference, label it as a choice and explain the tradeoff.
- Where evidence is missing, defer the claim or design a test.

## 5. Release gates (none are complete yet)

- Religious content mapped to qualified reviews and source provenance.
- User scenarios tested with diverse representative people; do not invent sample sizes or results.
- Accessibility, RTL/Urdu/Arabic, offline and no-notification paths independently exercised.
- Security/privacy policy, data deletion and mosque-owner verification appropriately tested.
- Licensing, dependency/source redistribution and contributor terms resolved.
- Operational budget and support process credible for free use.

## 6. Volunteer and contributor safety

Do not accept secrets, documents containing religious/private medical details, names of worshipers or private mosque management credentials in public issues. See [SECURITY.md](../../SECURITY.md) and [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md). This repository is public: issue and PR content is visible to others.
