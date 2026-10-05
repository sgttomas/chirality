# v8 revision (2026-10-05): three LOOP_INIT sentences corrected

**What this is.** The record of how the v8 Markdown, Word and PDF editions were revised on 2026-10-05. The owner's direction is in `execution/_Coordination/AgentRuns/ROOT-AUM-PEC-AND-FOLLOWUPS-20261005/OWNER_DECISIONS.md`.

## The change

Three §4.2 sentences told a loop to point LOOP_INIT at the work graph. That contradicts the evergreen rule: a loop's LOOP_INIT carries no undertaking-specific pointer, and the human's steering selects the graph. See `workflows/construct-local-work-graph/WORKFLOW.md` §4: "Return its path so the continuing session can locate it through its steering or project records. Keep undertaking-specific paths and state out of reusable loop instructions."

| Before | After |
|---|---|
| "…keep it current, and point LOOP_INIT to its actual location." | "…keep it current, and return its path so the continuing session can locate it through its steering or project records; LOOP_INIT stays evergreen and names no undertaking's graph." |
| "…relative to the project, and LOOP_INIT must point there." | "…relative to the project, where the human's steering selects it." |
| "Keep LOOP_INIT's pointer aligned with the actual selected graph at the required WorkGraphs path." | "Keep the selected graph at the required WorkGraphs path, and return that path for continuation; LOOP_INIT names no undertaking." |

Nothing else in the manual changed.

## Method

v8's own method, unchanged (`plans/evidence/2026-10-04_manual_v8/production-note.md`).
- **The scripts,** copied here with one edit: `format-finalize-v8.py`'s `EXPECTED_MD` is the revised Markdown's hash.
  - `format-build-v8.py` rebuilds the Word file from the retained v7 package, the v7 Markdown and the revised v8 Markdown, and writes `build-check.json` here.
  - `format-finalize-v8.py` updates the Contents folios and summary fields from a render, and writes `toc-map-v8.json` here.
- **The renderer** is the same one v8 used: the Codex runtime's bundled `soffice`, LibreOfficeDev 26.8.0.0.alpha0, as the v7 contract requires. It ran with a scratch user profile.
- **The steps:** build; render to PDF; finalize; render the finalized Word file to the final PDF.
- **Reproducibility, checked first.** Running v8's scripts on the unchanged v8 Markdown rebuilt a Word file whose every package part is byte-identical to the committed v8 Word file. Only the ZIP container differed (timestamps and compression). Its PDF had the same 172 pages and byte size. That check wrote nothing into v8's evidence: one hash file it rewrote was restored.

## Files

| File | sha256 |
|---|---|
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.md` (source) | `3ce966305415d2b39a444fc1622c5e54633d209b13516cd286442d4eb2afda76` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.docx` | `742b469ff96f46c433545cf92020128b9703ba59c3fb92c25a6c49cc00e3f2e2` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.pdf` (172 pages) | `0e99e465f23e611f7fa1c6bbdee5a596d375a9c13a71d2303cbf74b305533b2c` |

## Checks

- **Content check** (`content-check-final.json`, v8's checker). Results equal v8's:
  - Word: 1,656 of 1,656 source text units; 266/266 headings; 15/15 tables; 31/31 specimens; 9/9 list items; no mismatches;
  - PDF: no missing units; the same 3 interstitial extras (repeated table header rows).
- **Pagination.** Compared with v8's PDF, page text differs only on physical pages 83 (folio 79) and 87 (folio 83), which hold the edited paragraphs. Every other page's text is identical, and the page count is unchanged.
- **Visual inspection.** Both changed pages were rendered and inspected at full page. The type, justification and spacing match the book, and the edited paragraphs fit their pages.

**Not used:** LibreOffice 26.8.1, downloaded for this task under the owner's approval. The bundled renderer that v8 used was found to be available.
