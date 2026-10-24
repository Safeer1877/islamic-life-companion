# Licensing and attribution scope — Islamic Life Companion

**Adopted direction:** 24 October 2026, on the repository owner's approval.  
**Nature:** Different components have **different licenses**. Public availability is not itself a license. The license texts linked below, not this explanation, control their respective covered material. This explanation is not legal advice.

## 1. License map

| Covered material | License | Full text |
|---|---|---|
| **Original app/client software code** (future \`apps/\`, shared client \`packages/\`, ordinary scripts/tools and other original code unless an applicable file/directory notice says otherwise) | **Mozilla Public License 2.0 (MPL-2.0)** | [root LICENSE](../LICENSE) |
| **Original future hosted mosque/community service code** within \`services/mosque-network/\` and any future backend directories **explicitly designated AGPL** | **GNU Affero General Public License v3.0 only (AGPL-3.0-only)** | [AGPL text](AGPL-3.0-only.txt) |
| **Original, rights-controlled project documentation**, including Markdown documentation in \`docs/\`, \`README.md\`, \`SOURCE_MANIFEST.md\`, and project-authored policy/template prose | **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** | [CC BY-SA text](CC-BY-SA-4.0.txt) |
| **Original stylesheet \`docs/blueprint/blueprint.css\`** and original automation/build scripts or CI workflow code | **MPL-2.0** | [root LICENSE](../LICENSE) |
| **Raw research inputs** in \`research/original-reports/\` | **Excluded pending provenance and rights review** | Not covered by blanket project license |
| **Externally owned material** (e.g., third-party translations/editions, substantial third-party quotations, screenshots, fonts, icons, datasets, maps, third-party dependencies and trademarks) | **Their respective authors'/providers' terms** | Consult source/file-specific provenance |

**Important:** A file's **original copyrightable content** is covered only to the extent the licensor/contributors have rights to grant. Licenses do not purport to relicense third-party material or confer copyright over material that is not protectable under applicable law. Attribution and original source quotations may require separate permissions. A repository-level license notice is not proof that every embedded quotation or generated paragraph has cleared a legal rights audit.

### Current repository status

There is **no implemented mobile app or mosque server** as of this decision. MPL-2.0 and AGPLv3 establish the license structure for code developed in their defined areas; the presence of the legal texts does **not** imply the software exists.

The official project intends to distribute its core app **free to users**. This is a product/publishing choice; MPL, AGPL and CC BY-SA allow commercially permitted uses within their terms. None of these standard open licenses can guarantee that every third-party distributor offers a free service.

## 2. Practical reading

- **For app source:** A distributor of covered MPL code must satisfy MPL's source and notice requirements for covered files. Its file-level reciprocity does **not** require that all separate files in a larger program be open.
- **For a modified network-accessed mosque service:** AGPLv3 has specific modified-program source-offer requirements for users interacting remotely over the network. This is **not** a blanket claim about unmodified servers or every cloud service run by someone else.
- **For original documentation:** CC BY-SA 4.0 allows reuse and adaptations with attribution and share-alike requirements for licensed adaptations; it permits commercial use. It does **not** approve religious interpretations or certify scientific claims.
- **For future combined app/server/shared-code arrangements:** Do not copy and combine code across MPL/AGPL boundaries without checking license compatibility, dependency terms and each license's actual conditions.
- **For external sources or the original AI desk reports:** Do not assume they are licensed because this file is present. See [source manifest](../SOURCE_MANIFEST.md), [licensing and rights audit](../docs/governance/LICENSING_OPTIONS_AND_RIGHTS_AUDIT_v0.1.md) (proposed in draft PR #1) and the original publisher terms.

## 3. Files outside a simple folder rule

- A future file with an explicit, lawful \`SPDX-License-Identifier\` notice can identify a different applicable license; contributors must explain exceptions and compatible provenance in the PR. Such labels do not override someone else's rights.
- \`docs/blueprint/READ_BLUEPRINT.html\` is a **derived HTML presentation** of the original product prose. The covered original project prose is CC BY-SA 4.0; externally produced tool boilerplate and embedded third-party items retain their own rights.
- \`docs/blueprint/FOUNDATION_REFERENCE.md\` is a duplicated research foundation for navigation. It carries no distinct religious authority or new copyright grant beyond the rights-controlled original content.
- \`.github\` Markdown prose and templates are CC BY-SA 4.0; GitHub Actions YAML, build automation and any executable code are MPL-2.0, unless specifically marked otherwise.
- The textual \`README.md\` inside an AGPL-coded service directory remains CC BY-SA 4.0 **as documentation**; executable source in that service directory is AGPL-3.0-only, absent a valid explicit exception.

## 4. Contributor terms

See [Contribution licensing and provenance](CONTRIBUTION_TERMS.md). The project expects **inbound contributions to use the same outbound license appropriate to the file's designated scope**, not a blanket transfer of contributor copyright. Contributors must have appropriate rights and identify imported third-party materials. No copyright assignment or mandatory Developer Certificate of Origin has been introduced by this licensing decision.

A pull request is not, by itself, permission to relicense an external author's protected work. Maintainers should review both source rights and substantive research claims before merging.

## 5. Canonical legal sources

The exact text files were imported without edits from [SPDX's license-list-data project](https://github.com/spdx/license-list-data/tree/main/text) at the time of this decision:

- MPL-2.0 — https://www.mozilla.org/en-US/MPL/2.0/
- AGPL-3.0-only — https://www.gnu.org/licenses/agpl-3.0.en.html
- CC BY-SA 4.0 International — https://creativecommons.org/licenses/by-sa/4.0/legalcode.en

SPDX IDs: \`MPL-2.0\`, \`AGPL-3.0-only\`, \`CC-BY-SA-4.0\`.

The exact language of the individual licenses takes precedence over simplified summaries here.

## 6. Outstanding rights checks

Before accepting large outside contributions or packaging third-party sources, maintainers should:
- Confirm protectable original content and rights for AI-assisted edited specification pages;
- Review \`research/original-reports/\` for possible unlicensed quotations, data or sensitive material, without assuming model output is automatically copyright-protected;
- Select and document lawful licenses for future third-party code, translation texts, map datasets and photographs;
- Track contributors and their source/permission statements;
- Add per-file SPDX notices in executable code and maintain attribution records.

**Current grant is deliberately scoped, not an assertion that a comprehensive third-party audit has already passed.**
