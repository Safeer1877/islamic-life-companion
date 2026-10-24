# Licensing options, rights audit, and founder decision — v0.1

**Prepared:** 24 October 2026  
**Status:** Recommendation for owner review; **no license chosen or granted** by this document. This is not legal advice.  
**Current repository:** Public, research-stage, no root LICENSE, no implemented application, and multiple preserved AI-assisted source reports with redistribution rights not fully audited.

## 1. The decision is about reuse rights, not whether the app costs money

The founder intends a **free-to-use and publicly maintained application**, but that intention does not by itself dictate a copyright license.

- **Free-to-use:** users are not charged for core app features; this is a product/funding decision.
- **Open source:** the software's license grants permission to use, study, modify and redistribute under stated conditions; even strong reciprocal licenses can permit commercial use.
- **Public repository:** files are visible and may be forkable through platform functionality, but publication alone grants no general license.
- **Documentation/research:** may have **different authorship, copyright, translation and provider rights** from the future executable software.
- **Religious source citations:** authentic religious source status and copyright on a particular modern *translation*, edition, scan, commentary or dataset are distinct issues.

**Never present this project as Open Source Initiative-approved licensed until the owner actually adopts an appropriate license and the repository scope is clear.**

## 2. Practical choices for code

| Candidate | What collaborators gain | Tradeoff for this project |
|---|---|---|
| **Apache License 2.0** | Permissive reuse; commercial and closed derivatives allowed; explicit patent grant and notice/changes provisions | Widest integration path, but a third party can make a proprietary fork of independently distributed derivatives without releasing modifications |
| **MIT** | Short, broadly understood, permissive; attribution/license notice | No express patent grant; proprietary reuse also allowed |
| **Mozilla Public License 2.0 (MPL-2.0)** | File-level reciprocal source sharing for distributed changes to covered files, with explicit patent grant | A larger combined product can still include separately licensed files; **does not** ensure an entire future service remains open |
| **GPLv3** | Broad copyleft for distribution of covered combined software | More compatibility/distribution considerations for mobile app distribution and integration; not a server-network-source guarantee on its own |
| **AGPLv3** | Strong reciprocity that also addresses certain modified network-service use | Higher compatibility and integration burden; may be apt for a separately hosted mosque service but not automatically the best license for an iOS/Android app |

Sources (verified from official or established project documentation on 24 October 2026):

- [Apache-2.0, MIT, MPL-2.0 and GNU family overview](https://choosealicense.com/licenses/)
- [MPL-2.0 duties and patent grant](https://choosealicense.com/licenses/mpl-2.0/)
- [GNU AGPLv3 network-use condition](https://choosealicense.com/licenses/agpl-3.0/)
- [MIT conditions](https://choosealicense.com/licenses/mit/)

**Recommended starting comparison for this founder:** Apache-2.0 vs MPL-2.0 for future original code. Apache-2.0 better serves unrestricted adoption and interoperability; MPL-2.0 better protects openness of *modified existing source files on distribution* while remaining less restrictive than GPL/AGPL. If the founder explicitly wants reciprocal openness of the **whole distributed application** or **modified network service**, evaluate GPLv3/AGPLv3 and mobile distribution implications separately before selecting.

**No automatic license choice:** A public-contribution goal does not tell us whether the founder prefers permissive reuse or reciprocity. Founder approval is required.

## 3. Practical choices for original documentation

| Candidate | Reuse | Tradeoff |
|---|---|---|
| **CC BY 4.0** | Share and adapt with attribution, including commercial uses | Does not require derivatives to share under identical license |
| **CC BY-SA 4.0** | Share and adapt with attribution and ShareAlike for adaptations | Additional downstream compatibility obligations |
| **No general license (temporary)** | Anyone can read, submit specific permission requests and use rights granted by law | Blocks broad reuse/collaborative editing and is unsuitable as a permanent public-contribution model |

Docs reference: [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and [CC BY-SA 4.0 legal terms](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en).

**Recommended starting comparison:** CC BY 4.0 for original reviewed specifications (easy reuse) versus CC BY-SA 4.0 where the founder specifically wants redistributed adaptations to remain open.

**Do not use CC licenses for the primary software code.** Treat source code and prose/designs as separate licensing scopes.

## 4. Rights audit by current repository area

| Scope | Current state | Needed before any broad relicensing |
|---|---|---|
| **New original application source** | Not written yet | Choose code license, notice, contributor terms and dependency compatibility before starting implementation |
| **Reviewed docs: \`docs/FOUNDATION_v1.md\`, \`docs/blueprint/*\`, \`docs/research/*\`, governance prose, README** | Generated/edited with AI assistance; authorship and source quotations vary | Confirm who may license the protectable original content and audit substantial copied third-party text/assets; adopt documentation license with **explicit scoped paths** |
| **\`research/original-reports/*\`** | Five preserved AI-assisted desk reports with source-link and originality uncertainties | **Temporarily exclude from new blanket license** until origin, model/provider terms, source quotations, third-party rights and any personally sensitive material are assessed; preserving a raw report isn't proof of permission to sublicense its contents |
| **Qur'an/hadith editions, translations, tafsir and vendor screenshots** | External referenced/quoted material | Check each applicable translation/editor/publisher rights; link and cite carefully. Do not claim a blanket project license over materials owned by third parties |
| **Future logos, typefaces, icons, photographs, datasets, mosque directories** | Not governed by a public asset notice | Each needs documented license/provenance; public timetable facts don't automatically authorize database copying or publication |
| **Future community-submitted docs and code** | No accepted contribution licensing policy | Contributors need disclosed inbound licensing terms *before* substantial submission; clarify whether DCO is needed, and what that attestation means |

Do not delete or rewrite originals merely to improve optics; classify, audit and provide clear source provenance.

## 5. Contributor-rights choices

**Baseline:** Inbound contributions under the **same applicable outbound license**, with a PR attestation that the author holds sufficient rights and has not introduced sensitive or incompatible third-party material.

**Optional DCO (Developer Certificate of Origin 1.1):** A public sign-off process by which contributors affirm a right to contribute under the project's license. A DCO sign-off is public and contains personal information associated with the sign-off; explain that before requiring it. It is not a broad copyright assignment. See https://developercertificate.org/.

**CLA:** A contributor license agreement may be relevant if the maintainer truly needs special relicensing powers or commercial dual licensing. It increases legal/administrative friction. Do not impose a CLA or require contributors to assign copyright without a clear reason and explicit decision.

**Pragmatic initial recommendation:** Prefer ordinary inbound=outbound contribution terms, source disclosure and evidence requirements; consider DCO **after** publishing code/docs licensing boundaries and a fair privacy explanation. Avoid an unsupported claim that checking an issue template transfers ownership.

## 6. Proposed owner decisions (not completed)

- [ ] **L-01 — Code license:** Apache-2.0 / MPL-2.0 / GPLv3 / AGPLv3 / another researched option.
- [ ] **L-02 — Original reviewed documentation license:** CC BY 4.0 / CC BY-SA 4.0 / other.
- [ ] **L-03 — Excluded material:** confirm \`research/original-reports/\` and specific externally authored translations, fonts, images, assets and data are **not automatically relicensed**.
- [ ] **L-04 — Contribution rule:** inbound=outbound and PR attestation, with optional DCO only after conscious approval.
- [ ] **L-05 — Attribution owner:** identify copyright owner(s) for protectable original material; don't invent a legal person's name.
- [ ] **L-06 — Source and dependency review:** confirm source rights and compatibility; file-level attribution process.
- [ ] **L-07 — Publish actual license texts and \`LICENSES/README.md\` scope table, update repo banner and PR templates.**
- [ ] **L-08 — Confirm external contributor communication is unambiguous** before requesting major patches.

## 7. Acceptance test

Ask an unfamiliar contributor to read the README and answer:
1. May I legally modify and redistribute the *app code* (when published), and what must I provide?
2. May I reuse and adapt the *reviewed blueprint* in my own project?
3. Does the repo license cover the five unreviewed imported AI reports and particular translations?
4. What rights am I granting if I submit a PR, and do I retain my contribution's copyright?
5. Which parts still need verification or third-party permission?

If any answer is unclear, the project is **not** ready to advertise an open-source contribution drive.

**No automatic deployment/merge:** publish licensing only after an owner choice and source-rights assessment. This decision aid changes no existing copyrights or licenses.
