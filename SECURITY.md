# Security and sensitive-information reporting

**Status:** Research/documentation stage. There is no deployed app, server, login system or public API in this repository at the time this policy was prepared.

## Please do not publish

- Credentials, tokens, keys, private endpoints or user data.
- Personally identifying information about worshipers, children, scholars, mosque staff or other contributors.
- Sensitive religious/medical/family information.
- Reproducible steps that would compromise a future deployed service, private data or mosque ownership claim.

## Security concerns in current documents

A public GitHub issue is appropriate for **non-sensitive** architectural questions about privacy-by-design, local storage, data deletion, stale Iqamah, roles, and misuse cases. State the affected document, proposed threat, impact and safe mitigation without including exploitable details or secrets.

For information that could be exploited or identifies individuals, **do not create a public issue or PR**. If the repository has enabled GitHub's **Report a vulnerability** feature, use its private reporting workflow on the Security tab. If that facility is unavailable, please refrain from publishing sensitive details and request a confirmed private disclosure channel from the maintainer using a non-sensitive contact request.

**Maintainer status (25 October 2026):** The owner reports enabling GitHub **Private vulnerability reporting**. This does **not yet prove** that a non-admin reporter can reach it or that a maintainer receives and monitors test advisories. Verify both using [GitHub's official guide](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository). A vulnerability form is **not** a confidential conduct-reporting channel.

**Open operational blocker:** Reported enablement is not independently verified delivery or staffed response ownership. Do not claim that confidential reporting is operational until its access, receipt and owner have actually been tested; resolve this before deployment or public collection of sensitive data.

## What a good private report should contain

Affected version/commit; impacted component; minimal description and reproduction using synthetic test data; confidentiality/privacy risk; expected versus actual behavior; and a secure means to follow up. Do not provide real user identities or production secrets.

## Security principles for future implementation

1. Private routines are device-local by default; optional sync requires explicit design and consent.
2. No inferred prayer attendance or export of a person's private schedule to mosque administrators.
3. Mosque ownership/editing requires independently verified authority, scoped permissions, revocation and audit logs.
4. No undocumented vendor API access; no assumptions about guaranteed background execution.
5. Minimal logs, deletion/retention controls, safe offline behavior and security reviews before launch.

The project cannot promise a response deadline or coordinated-disclosure SLA while no staffed security response process has been established.
