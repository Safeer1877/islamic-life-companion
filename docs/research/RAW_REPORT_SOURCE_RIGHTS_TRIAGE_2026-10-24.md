# Original research source-rights triage — 24 October 2026

**Scope:** The five AI-assisted reports at \`research/original-reports/\`, **without editing any of their contents**.  
**Method:** Read the full file text programmatically; record current Git blob identities and every literal HTTP(S) URL with its source line; inspect visible quotation, reference-formatting and attribution signals; check for common textual credential/email patterns.  
**Status:** **Mechanical inventory completed; legal and source-rights clearance NOT completed.** This is a screening report, not a copyright infringement finding, legal advice, a completed citation audit, or qualified Islamic review.

## Executive result

The **5 originals are preserved unchanged** and the repository now has a frozen line-level inventory of **173 HTTP(S) URL occurrences**, including **52 web-preview favicon URLs** rather than ordinary source citations. The remaining URLs include tracker-tagged references, direct references, DOI links and secondary sources. Some files contain religious quotations and commentary requiring review for exact source, attribution, translation, length and applicable rights. **No third-party material has been proven freely relicensable by this automated audit.**

The [project license map](../../LICENSES/README.md) already **excludes the original five reports from its blanket MPL/AGPL/CC grants**. That is the correct interim response while provenance and rights remain unresolved.

## File inventory (committed Git blob identity, not author/content verification)

| Original | Lines | Literal URL occurrences | Flagged formats | Git blob ID |
|---|---:|---:|---|---|
| \`01-islamic-framework-investigation.txt\` | 1,424 | 30 | **30 web-preview favicon links**, with embedded source-domain labels; no ordinary standalone source URLs extracted by the literal scanner | \`0338b9d930d8d077b6ca6370fcb7502104b231ea\` |
| \`02-foundational-research-report.txt\` | 1,839 | 44 | **22 web-preview favicon links; 22 tracker-tagged direct links** | \`dc105673bf20bad16d41f0d63e445945d8ba7102\` |
| \`03-functional-model-research.txt\` | 1,691 | 57 | **56 tracker-tagged direct links**, one other URL | \`1e35cf3bc2fe77f6256ead1e17380ffa1647306d\` |
| \`04-six-deliverables-research.txt\` | 161 | 0 | **No literal URLs.** Includes source names/numbers and at least one quoted hadith translation; citation and translation rights must be checked directly | \`ef3bc0f71bf340efe96d39f222b700475b59a9b5\` |
| \`05-functional-foundation-research.md\` | 771 | 42 | **6 direct religious-reference links, 9 DOI links, 27 other URLs**; internally marks some sources ✔ as opened and others ○ as not re-opened | \`675bda107b237ee9785cb670dc3a0ccee3f93d1c\` |

**Total:** 5 reports, **5,886 lines** and **173 literal URLs**. The [full source-url inventory](../../research/provenance/original-report-url-inventory.csv) includes the original filename, exact line, literal extracted URL and mechanical link-type classification. It is an **audit aid**, not a set of verified sources or license grants. It includes tracking URLs **as preserved in historical input**, not links this project recommends sharing.

### Why those formats matter

- Report 01's repeated \`www.google.com/s2/favicons?domain=...\` URLs are **icon preview addresses**, not reliable citations for the underlying scholarly or scientific assertions. Original UI/export artifacts including \`&#x20;\`, escaped punctuation and icon labels survive in some text.
- Reports 02–03 contain multiple URLs tagged with \`utm_source=chatgpt.com\`. Tracking parameters and branded source labels are not proof that the exact page was read or the inference checked.
- Report 04 is short but has no direct source URLs. It requires manual look-up of collection/verse numbers, actual text and the translation reproduced before we claim precise attribution or reuse rights.
- Report 05 self-discloses no participant study, no scholar consultation and no real tests. Its ✔ “retrieved and read” annotations describe the **original model's research session**, not an independently reproduced verification by this repository's current reviewers. Those badges should not appear as scholarly certification in downstream product UI.

## Specific rights/external-evidence risks

| ID | Item needing verification | What can be stated now | Still requires |
|---|---|---|---|
| **SRC-01** | Modern English/Urdu/Arabic translations and commentaries quoted or paraphrased in raw reports | References to Qur'an/hadith are present; copyright on a **specific modern translation/commentary** can differ from underlying religious text | Passage-by-passage comparison with actual edition/publisher, accurate quotation, attribution, permission or applicable quotation exceptions |
| **SRC-02** | Source-check and bibliography claims, including report 01's “source-checked evidence register” | It is a statement within an AI-generated report; a favicon link does not itself verify the cited original | Independent first-hand inspection of primary references, edition/context and applicable fiqh interpretation |
| **SRC-03** | DOI/academic evidence and behavioral-science claims | Source URLs and bibliographic references exist but their claims and quoted text have **not** been exhaustively verified | DOI/article identification, abstract/full-text inspection where lawfully available, correct inference and quotation/reuse-rights review |
| **SRC-04** | Source material apparently reproduced in long quoted segments | Quote candidates appear in some files; a basic pattern scan cannot distinguish original UX mock copy from protected third-party prose | Manual quote-by-quote classification and similarity/context review; qualified legal advice where appropriate |
| **SRC-05** | Generated research-output authorship/provider rights | Reports are identified as AI-assisted desk studies; there may be provider terms and third-party embedded content; not all generated material necessarily has copyright | Document originating tool/provider where known, terms in force at creation, human contribution and third-party quotation provenance |
| **SRC-06** | User/community sensitive information | A basic scan found no simple email addresses or common token prefixes in these five report texts, **not a privacy clearance** | Human examination for names, identities, clinical anecdotes and inadvertently included secrets; do not paste private user data into public PRs |

### Editorial conclusion

- **Do not delete, hide, relicense or silently normalize the originals.** Keep the literal historical record and append independently checked errata/citations in reviewed documents.
- **Do not treat source URL presence as verification** or a model's “source checked” assertion as proof.
- **Do not mark any of the five raw reports as cleared for CC BY-SA sublicensing** until the relevant rights and source chain have actually been verified.
- **Do not use a generic project copyright notice to imply ownership of modern translations, linked journals, vendor content or unnamed scholar opinions.**
- Maintaining an excluded source archive makes the repository transparent without granting rights that the maintainer may not have.

## Confidence boundaries and incompleteness

Completed here:
- Exact Git blob identity inventory and file-level freeze.
- Literal URL extraction and link-type classification across the whole source text.
- Basic identification of web-preview, tracking artifacts and absent direct links.
- A first-pass search for common credential and email patterns, with **no guarantee that all sensitive data is absent**.
- Confirmation that project's currently merged license map excludes raw reports.

**Not completed:** External URL reachability/accuracy checks for all 173 occurrences; full direct-source review of all claims; quotation-by-quotation third-party rights assessment; verified human contributors/provider terms; scholarly interpretations; user experiments; jurisdiction-specific copyright advice.

This **partially fulfills** [GitHub issue #3](https://github.com/Safeer1877/islamic-life-companion/issues/3) by delivering a verifiable source index, but **must not close the issue as legally cleared**.

## Remaining review plan, ordered by risk

1. **Translation/quote audit:** Start with direct quotations from Qur'anic and hadith English translations and other attributable research passages; record precise translator/edition and policy/permission for reproduction.
2. **Claim-to-reference crosswalk:** For every religiously consequential claim selected for the foundation, link the exact passage, primary source, interpretive status and qualified scholar review requirement. Use [claim ledger in draft governance PR #1](https://github.com/Safeer1877/islamic-life-companion/blob/docs/research-integrity-and-contributor-readiness/docs/research/CLAIM_LEDGER.md) rather than pronouncing source reports valid in bulk.
3. **Research citation check:** Resolve DOI titles/metadata and read the original studies; compare what they measured against claims of user benefit.
4. **Provider and ownership provenance:** Record exactly which original reports came from which model/provider/date where known, including provider output-use terms and any imported external texts.
5. **Privacy/safety screening:** Human scan of any descriptive personal cases; preserve only appropriately public information.
6. **Qualified legal decision:** Determine whether additional licensing exclusions, attributions or removals are necessary before redistributing the archive beyond its existing public repository access.

## Repeatable check

\`python scripts/check_research_provenance.py\`

The script confirms the preserved **five Git blobs** and exact source-link line inventory stay stable. It will fail if the original bytes or the index changes unexpectedly. A passed workflow does **not** establish any legal, academic or religious validity.

**Related references:** [License scope](../../LICENSES/README.md), [historical source manifest](../../SOURCE_MANIFEST.md), [raw report exclusion notice](../../research/original-reports/README.md).
