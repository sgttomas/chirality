# Independent publication review

Status: PASS on the exact final hashes below. Independent publication review is complete, with no unresolved actionable finding. Suitable for manager fan-in and ordinary Git closeout; this is not governed acceptance or product release.

Date: 2026-09-22. Basis: `e74feb34b7ca99ebeb903ffb52f7fdd2b3efd169`; branch `codex/management-manual-v2-formats-20260922`.

Reviewer `/root/publication_reviewer` is a TASK (Type 2) child of HELP_HUMAN `/root`, using native Codex collaboration. The reviewer did not author the outputs, delegate, mutate Git, edit source artifacts, install software, render through another browser route, or change earlier evidence. Host permissions are broad; the assignment and write restriction are instruction-based. Review writes are limited to this run's `publication-review*` files.

## Scope and method

Reviewed the renderer/CSS and directory README changes, actual v1/v2 DOCX packages, frozen Markdown, final PDF bytes and annotations, and selected actual page images. Selected skills: repository `software-code-review`, bundled `documents`, and bundled `pdf`; read the documents reading/review guide. The existing root/role/skill instruction hashes were verified unchanged from the preceding review. No additional role was activated.

Document inspection used the bundled Python at `/Users/ryan/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`, with bundled XML/PDF libraries. HTML checks used the publisher's existing virtual environment derived from that bundled Python and its pinned Markdown parser. No LibreOffice operation was performed by this reviewer; the inspected PDF/page images came from the manager's bundled-renderer run. No user-installed LibreOffice or browser workaround was used.

The repository scope helper found all changed/untracked paths within the brief's authorized roots. Original v1 Markdown/DOCX/PDF, v2 Markdown, agent-guide Markdown, review Markdown, reference image, and relevant instructions matched the recorded input hashes. Earlier run evidence remains untouched.

## HTML checks

- Compared renderer ASTs at the base commit and candidate after removing only the `CSS` assignment. All non-CSS logic is unchanged, including the passive-source guard, heading/anchor handling, source fingerprint, and CLI.
- Compared complete HTML bytes after replacing only the single style block. All content, semantic markup, navigation, source links, and embedded source identity are unchanged from the previously reviewed publication. This establishes preservation beyond visible-text similarity.
- Independently reran the four previous resource cases: CSS import, inline background URL, object data, and iframe srcdoc all reject. Fixed CSS contains no network resource URL/import mechanism.
- Ran `render_manual.py --check` from `/tmp` with the recorded date and source revision; it reproduced the existing HTML exactly. No publication file was written by the check.
- Inspected the actual reference cover and body images and v1 style/section XML. The candidate's black serif type, centered uppercase cover-style title, restrained hierarchy, and 6.75 by 9.25 inch print geometry follow the reference. The gray table fill and responsive layout are screen adaptations within the user's “matching exactly is not necessary” direction. Code explicitly disables hyphenation.

No browser layout, responsive interaction, accessibility-tree, screen-reader, or HTML print-preview check was executed. The known browser URL boundary remains in force. Static CSS and semantic preservation are not presented as browser visual proof.

## DOCX content and template checks

- Opened the actual ZIP/XML package. Its 28-part inventory matches v1; only `word/document.xml`, `word/_rels/document.xml.rels`, `word/settings.xml`, and `word/footer5.xml` change. The other 24 parts remain byte-identical, including styles, numbering, theme, headers, font table, and the original image. Both section-property trees retain the reference geometry and numbering setup.
- Parsed the v2 Markdown independently using CommonMark with tables/strikethrough. All 1,730 substantive semantic blocks occur in the DOCX text after whitespace normalization that preserves Word breaks and tabs. The four frontmatter lines are intentionally regrouped/cased into the inherited cover. The edition-2 explanatory note remains complete at the start of Preface. Conversely, examined 1,769 DOCX paragraph slots from Preface onward: all 1,719 nonempty paragraphs occur in the Markdown semantic text. These are content-presence checks, not a claim of literal Markdown/Word layout equivalence.
- Read the production recipe as a lead, including its 64-operation manifest replay and source-hash checks; did not rely on its coverage report as a substitute for the independent comparison above.
- Verified 85 tables (84 inherited plus the new project crosswalk), 127 unique bookmarks, retention of every original bookmark, and valid targets for all 81 internal links. No tracked insertions/deletions were present.
- Verified the original drawing subtree as well as its media bytes remain exact. The PDF actually paints the image XObject on physical page 24. Shared PDF resources were distinguished from the actual page drawing operators.
- Every one of the 74 Markdown hyperlinks is retained at least as many times in DOCX. The 71 additional links are the preserved detailed contents entries. All original relationships remain unchanged; new file links resolve from the publication directory. Verified all three distinct external Markdown fragments against the actual target headings.
- The footer retains a real `PAGE` field, edition labels identify edition 2, and `updateFields` is enabled. The contents uses deliberately cached page numbers and hyperlinks; it is not misrepresented as an automatic TOC field.

## PDF and selected visual checks

Opened the actual produced PDF, verified its title/author metadata and edition-2 cover/preface text, and compared its bytes with the manager's final rendered PDF. The book has 180 pages of 486 by 666 points. After the unnumbered cover, extracted footer folios run from 1 to 179.

Independently checked all 81 cached DOCX contents page numbers against the final PDF annotation destinations and actual destination-page folios. All matched. All local targets among 71 PDF URI annotations resolve from the publication directory; URI paths remain relative rather than binding to a temporary render location. Remote URLs were preserved, not fetched or requalified.

Inspected selected candidate images individually at original resolution: physical pages 1 (cover), 2 (contents), 4 (Preface), 5 (repository crosswalk), and 17 (phase table/header repair). Compared cover/body treatment with the actual reference images. These selected pages were readable and their title/body/table content matched the source. The page-17 repair reported by another reader reduced only the affected header cell's left/right margins to 45 twips while preserving text, type size, and grid; its words now wrap intact. Previously inspected pages 1, 2, 4, and 5 were byte-identical through that repair.

The root requested left alignment for only the two new technical paragraphs on page 5. Independently opened the final2 page-5 image at original resolution: spacing is now normal, the wording and crosswalk are intact, and the reference styling is retained. Rechecked final2 DOCX/PDF content, package preservation, numbering, bookmarks, source links, and all 81 TOC destination/folio bindings. The PDF is byte-identical to the final2 render. Previously inspected pages 1, 2, and 4 remain byte-identical to their original candidate images; final2 page 17 is byte-identical to the independently inspected repaired image. All 11 final README links resolve.

Full page-by-page visual QA belongs to the manager's six TASK readers; this reviewer does not claim to have inspected all 180 pages or to have executed their checks. Read the sealed `format-visual-coverage.json` (SHA-256 `1f85d74e78074aa50bb5ff153d77be9bceb2c6d28992dc20f0871c824e74d7c8`) and `format-review.md` (SHA-256 `5f87e1b22cb2a23633f30e35e1eb8cd94d129f55ac824506dfbe8327943cf4ad`). Their six disjoint ranges cover physical pages 1–180, all PASS, with pixel-identity carryover and explicit rechecks for changed pages 5 and 17. The bound DOCX/PDF hashes match this independent review. The earlier midword header wrapping is resolved; the root-requested page-5 refinement is also complete. Final artifact hashes were re-observed unchanged at this closing boundary.

## Exact final publication targets

| Repository-relative target | SHA-256 |
| --- | --- |
| `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx` | `076dbf426edf0afa42f9989296b4b3882a5a1b8542da0134ba5a26b66812ee00` |
| `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.pdf` | `fe2cb359afab4b154ff414cc1957ae7329c1d52f89252ca75dbde9b116cf6fae` |
| `docs/alignment-manual/render_manual.py` | `4d70e13e78307da22d622f511251530f6cb7a206680f1cb35487ea9a18eacc08` |
| `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v1.html` | `f743bb5ed751329007b89d9385dfb2c6dcf7525925a2040e288f0a1fae530ead` |
| `docs/alignment-manual/README.md` | `9babc3d10fa429e97e70cde35b334d55a10b27c9d6719bab6453faf332322259` |
| `docs/alignment-manual/requirements.txt` | `ac981afac84d512ce043af011e6274637949d90e9de4fc114190f55fc322ad10` |

## Return boundary

The review establishes source preservation, template/package integrity, publication navigation, candidate identity, and the specifically recorded visual observations. It does not reopen editorial/governance acceptance, verify remote source claims, qualify Word/browser interaction, or replace required repository CI. Any change to a listed target requires reassessment of its affected checks.
