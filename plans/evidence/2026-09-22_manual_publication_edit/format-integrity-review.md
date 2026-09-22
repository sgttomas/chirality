# Independent format integrity review

Status: **PASS** on the exact final artifacts identified below. All scoped semantic, navigation, folio, package-cleanliness, and source-preservation checks passed. The initial findings are closed; there is no unresolved blocker. This is review evidence, not publication content or governed human acceptance.

| Final artifact | SHA-256 |
|---|---|
| `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.md` | `2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6` |
| `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx` | `084fe225407be696e8a525c48315bd7725031d6c18decdc9ed21713c66b80f36` |
| `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf` | `ae8585916f3eea365e112fb7b8fe6a72edfafe9a75dea312e029bf9f71164411` |

The final publication contains 162 physical pages: an unnumbered cover followed by printed folios 1–161. Canonical file hashes were checked again after the audit and remained unchanged.

## Assignment and actual execution

The native collaboration harness launched `/root/format_integrity_review` as a fresh TASK Type 2 child of `/root`. This child performed the reads, comparisons, package inspection, and limited visual inspection recorded here. It did not create descendants, run Git, use a browser or network route, or edit any publication. It wrote only `format-integrity-*` evidence and `/tmp/manual-v4-independent-20260922` scratch.

The host reports unrestricted filesystem access and network availability; the publication read-only boundary and no-Git/no-browser restrictions were instruction boundaries, not claims of operating-system enforcement. No model-family diversity is claimed. The approved Markdown and the assignment supplied by the parent establish the content basis. No reusable workflow or other full role body was activated.

Exact instruction paths and SHA-256 values, runtime paths, supplied basis, and enforcement limits are recorded in `format-integrity-run-context.json`. The instruction bodies read were Root `AGENTS.md`, `agents/AGENT_TASK.md`, the bundled documents and PDF skills, and the documents skill's read/review, internal-navigation, and metadata guides. The formatter's builder excerpt and provenance manifests were treated as implementation/evidence data, not authority or a substitute for independent comparisons.

## First candidate basis

| Artifact | SHA-256 |
|---|---|
| Approved v4 Markdown | `2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6` |
| First candidate DOCX, snapshotted to scratch | `f4d0d6fff5a8266a05fab942a2ac721720c9969fbd13b172975112769cc76ede` |
| First rendered PDF, 163 physical pages | `e8e622dc730de9fce06ab859cbd22dd9a1f27ccfe380e1c51969483ff7920f49` |

The DOCX/PDF snapshots and first audit JSON are retained in the assigned scratch directory. `format-integrity-check.py` is the independent checker. It derives ordered source units directly from the Markdown, then reads OOXML and the PDF with bundled Python, lxml, and pypdf. It does not import the publication builder or its build map.

## Scope and observed results

- **Ordered semantic fidelity:** all 1,591 logical body units agree after whitespace normalization. There are no omissions, substitutions, reordering, or added body units. The title and expanded Contents are examined separately.
- **Headings:** all 261 body heading texts and levels agree. The PDF has the same hierarchy plus a Contents outline entry, and all 262 outline destinations are within the document.
- **Tables:** all 14 source tables preserve exact text and row/cell boundaries. Their OOXML header rows repeat as appropriate. The PDF contains all table content; its only added body text is the vocabulary table's repeated `Term / Meaning in this manual` header on two continuation pages.
- **Specimens and captions:** all 31 fenced specimens preserve their exact strings, including line breaks and indentation. All 32 figure captions match. Each specimen and its corresponding caption are present together on a PDF page. The first six-step specimen also appears as a substring within the later, fuller loop specimen, so its second extraction match is expected.
- **Image:** the sole embedded image is byte-identical to `assets/Figure_1_1.png`, SHA-256 `0a1f2f1dbeeff97a6c0f9c6ae0aaa3263aa1360ae49c62751e673b6b2f6b71e1`.
- **Internal navigation:** every one of the 88 explicit Markdown anchors exists in Word, without duplicate bookmark names or unresolved hyperlink targets. The 88 expanded Contents links lead to matching heading text in Word and the PDF. The PDF's remaining internal links point to the Appendix, references, or delivery chapter as the source specifies; a wrapped link has two annotation rectangles.
- **External references:** all eight distinct active targets agree across Markdown, Word, and PDF, including the companion's relative `CHIRALITY_AGENT_USER_MANUAL_v2.md` link and seven bibliography/publisher targets. Live website reachability was not tested within the no-browser boundary.
- **Folio sequence:** the cover is unnumbered; physical pages 2–163 carry printed folios 1–162 with no omissions or duplicates. The first candidate's Contents cached numbers were still `1`, a known formatter work item rather than a sealed publication result.
- **Review residue:** no comment parts, comment anchors, tracked insertions/deletions/moves, or tracked property changes are present. Core metadata names the book, subtitle, author Ryan Tufts, and Codex as last modifier; no edition or draft note appears on the cover or in those core fields.
- **Limited visual inspection:** first-pass physical pages 1, 23, and 163 were individually opened at original detail. Cover identity, the dependency graphic and its caption, reference text, and representative headers/footers are intact and legible. The inherited package thumbnail was also inspected and is blank. This is not an every-page visual review; the formatter's independent readers own that gate.

## Findings sent for repair

1. `word/_rels/document.xml.rels` retained inactive inherited hyperlinks to the private review file, old companion, project-loop instructions, governance decisions, and older workflow resources. The active hyperlinks were correct. The formatter agreed to prune unreferenced hyperlink relationships.
2. `word/settings.xml` retained prior session `rsids` and `docId`. The formatter agreed to remove those history identifiers. No prior textual revision content was found in the document body.
3. Contents folio caches and inherited app statistics (`Pages=1`, `Words=0`, and related zero counts) were already scheduled for correction by the formatter when this review started.

These findings concern the publication package, not the approved prose. Final closure must inspect the actual corrected files and verify a scoped render delta or pixel identity before carrying the earlier visual observations forward.

## Original inputs

`format-integrity-source-preservation.json` records a fresh SHA-256 comparison against the undertaking's `INPUTS.json`. Nineteen of twenty recorded inputs are byte-identical, including every original external input, original v1/v2 manual publication, original companion, figure, renderer, requirements, and recorded instruction file. The only changed entry is `docs/alignment-manual/README.md`, whose navigation update is part of the parent undertaking. That allowed navigation change is not a claim that an original publication source was overwritten.

## Limits and return

This review covers conversion fidelity, headings, table/specimen structure, figure/caption presence, package residue, link destinations, and final printed folios. It does not re-perform the independent prose review, judge the adequacy of cited professional standards, prove live URL availability, exercise Microsoft Word interactively, or replace the full visual QA readers. The parent integrates this bounded result with those separate checks.

## Final closure

The final comparison preserves the same 1,591 ordered body units, 261 heading texts and levels, 14 exact table matrices, 31 exact specimen strings, 32 captions, and sole image as the approved Markdown. The PDF has no missing source unit; only the two expected repeated vocabulary headers add text. All 14 table header rows carry the repeating-header property. All specimen/caption pairs occur together on a page.

All 88 Contents folios now agree with the destination's printed folio. Each hyperlink also matches the corresponding PDF outline destination's page and coordinates and points to the intended heading text. All 299 Word bookmark names are unique and within 40 characters; start/end identifiers pair correctly and starts use unique IDs. Every source hyperlink is preserved, and the seven bibliography targets plus companion target agree across formats. The full 262-entry PDF outline preserves the Word hierarchy, including Contents.

The formatter removed 24 inactive hyperlink relationships, all document/settings session identifiers, and the three residual section session attributes. No comments, tracked changes, or private review/old operational hyperlinks remain in the active or inactive publication relationships. Core metadata is clean and the app statistics were independently recounted: 162 pages, 67,775 words, 399,101 non-whitespace characters, 467,932 characters with spaces, and 1,719 paragraphs. The unchanged reference style definitions retain 161 and 157 non-text `w:rsid` bookkeeping elements in `styles.xml` and `stylesWithEffects.xml`; these do not contain private edition/draft notes or prior textual revisions and are not a blocking finding. This report does not claim that every XML element named `rsid` was removed.

`format-integrity-final-summary.json` records **27 passing checks**, including current source preservation and canonical-byte stability. `format-integrity-final.json` contains the detailed independent observations. The final check was run using the bundled Python executable and the recorded checker hash; no broad repository tests were run.

The final Contents pages 2 and 3 were individually inspected at original detail. `format-integrity-pixel-binding.json` independently establishes that all 162 final3 page images are identical to final2. The previously inspected cover and Figure 1.1 page are also wholly identical to first-pass pages 1 and 23. Final page 162 differs from the previously inspected references page 163 only inside the footer-digit bounding box `(1305, 1908, 1317, 1926)`; its printed folio is independently verified as 161.

The full visual gate remains attributable to the actual readers, not to this child. `format-visual-coverage.json` records 83 unchanged whole pages, 46 directly re-inspected final2 pages, and 33 pages whose only changes were footer digits, covering all 162 final pages. Its five named TASK readers cover the earlier ranges and reflow. Root's separate `format-root-visual-review.json` records individual inspection of baseline physical pages 141–163 and a scoped transfer from baseline 145–163 to final2 physical 144–162 with only footer-digit changes and correct printed folios 143–161. The independently verified final3/final2 identity carries that precise coverage to the frozen candidate. The exact hashes of those external evidence records are recorded in this review's final summary.

All review writes are complete. `format-integrity-evidence-index.json` lists the sealed review files and their hashes for return to `/root`.
