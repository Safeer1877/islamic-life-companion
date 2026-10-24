# Decision record — separate licenses for an open, community-maintained project

**Decision:** 24 October 2026  
**Approved by:** repository owner, in the project discussion.  
**Implementation:** scoped legal texts, license map and contribution terms on the licensing PR branch, pending GitHub review/merge verification.

## Approved structure

- **MPL-2.0:** Original future mobile, desktop, web application and shared client-side code, plus ordinary project tools/scripts.
- **AGPL-3.0-only:** Original future **hosted mosque/community network service** code in explicitly identified service directories.
- **CC BY-SA 4.0:** Original project documentation and proposals **only to the extent authors/licensors have grantable rights**.
- **Explicit exclusions:** \`research/original-reports/\`, translations/editions, substantial outside quotations, third-party assets and dependency licenses pending case-by-case rights review.
- **Contribution expectation:** inbound equals outbound as applicable; no blanket copyright assignment and no mandatory CLA or DCO introduced at adoption.

## Rationale and acknowledged tradeoffs

The founder wants a **free-to-use and sustainably public-contributed Islamic life-management system**, with modifications improving covered code/documentation shared under reciprocal obligations.

MPL-2.0 offers **file-level copyleft**, allowing practical mobile interoperability and proprietary *separate* files in larger works. It **does not** force the entire combined application to remain open. That limitation is understood and accepted for the client code unless separately revisited.

AGPLv3 is selected for future hosted mosque services because it adds obligations concerning source of certain **modified network-accessed versions**. It does not itself fund hosting, guarantee ongoing support or grant access to a private service's data.

CC BY-SA 4.0 encourages attributable document adaptation and ShareAlike for qualifying derivatives. It does **not** make religious interpretations universally correct or prevent all commercial use.

The project's **official app** is intended to remain free for people. **Open-source licensing permits commercial use**, so fees charged by others cannot be ruled out through a standard open-source license alone.

## Not established by licensing

This decision does **not** verify source/copyright ownership of every paragraph, authorize copied third-party research or modern religious translations, establish contributor scholarly credentials, validate architectural claims, or require a future maintainer to merge a specific PR.

All substantive user-facing religious claims still need source provenance and qualified review. Before large outside contributions, finish owner-visible GitHub rules, private reporting and contributor provenance checks.

## References

- [License map and exclusions](README.md)
- [Contributor terms](CONTRIBUTION_TERMS.md)
- [Mozilla MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
- [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html)
- [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
