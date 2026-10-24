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

## 3. GitHub workflow (proposed; enforcement must be configured)

1. Keep `main` as the project baseline.
2. Contributors branch → submit a focused PR → complete the template with references and tests.
3. A maintainer checks changed links, screen IDs, provenance and conflicts across documents.
4. Sensitive and religious claims remain pending until the proper reviewer gate passes.
5. Document accepted product direction in a dated decision log and make rejected/deferred scope explicit.
6. After merge, track revisions with issues and changelog/decision records rather than quietly changing historical research files.

**Maintainer setup not yet verified:** Require a PR before merging, code owner review and at least one approval using GitHub branch protection/rulesets. Do not claim protection is in force until settings are inspected. The CODEOWNERS file identifies a review contact but does **not** itself block direct pushes.

### Concrete configuration and verification (maintainer-only)

The [Maintainer Launch Checklist](MAINTAINER_LAUNCH_CHECKLIST.md) documents the proposed `main` ruleset, real PR/CI enforcement tests, GitHub private vulnerability reporting, reviewer-dependency caveats and licensing gate. **Repository API check on 24 October 2026 showed no listed rulesets; a legacy branch-protection read was forbidden to the connected integration, so full protection status remains unverified.** GitHub settings and private reporting controls must be configured by an authorized human administrator; repository policy files do not enable them.

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
