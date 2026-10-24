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

**Maintainer setup:** GitHub supports built-in private vulnerability reports for public repositories. The authorized owner should follow [this configuration guide](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository), test that a private report is accepted, and monitor the notifications. A private vulnerability report form is **not** a substitute for a confirmed confidential conduct-reporting path.

**Open operational blocker:** A private disclosure channel and response owner have not been independently verified. Do not assume this repo currently supports private vulnerability reporting. That must be resolved before deployment or public collection of sensitive data.

## What a good private report should contain

Affected version/commit; impacted component; minimal description and reproduction using synthetic test data; confidentiality/privacy risk; expected versus actual behavior; and a secure means to follow up. Do not provide real user identities or production secrets.

## Security principles for future implementation

1. Private routines are device-local by default; optional sync requires explicit design and consent.
2. No inferred prayer attendance or export of a person's private schedule to mosque administrators.
3. Mosque ownership/editing requires independently verified authority, scoped permissions, revocation and audit logs.
4. No undocumented vendor API access; no assumptions about guaranteed background execution.
5. Minimal logs, deletion/retention controls, safe offline behavior and security reviews before launch.

The project cannot promise a response deadline or coordinated-disclosure SLA while no staffed security response process has been established.
