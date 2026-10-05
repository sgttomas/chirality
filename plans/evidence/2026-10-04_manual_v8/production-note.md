# v8 Word and PDF production note

**What this is.** The record of how the v8 Word and PDF editions were
produced on 2026-10-04, and what was and was not checked.

## Method

The v7 method was carried forward unchanged except for one new element type
(numbered lists). `format-build-v8.py` builds the Word file from the v8
Markdown in the retained v7 layout; `format-finalize-v8.py` finalizes it and
converts it to PDF with LibreOffice (`soffice`), as v7 did. `toc-map-v8.json`
is the contents map. `format-content-check-v8.py` is the v7 checker with list
items added.

## Files

| File | sha256 |
|---|---|
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.md` (source) | `28a1aafda799083c86420be3c90cbd7708290afad19bdc6ad82db6588d534df9` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.docx` | `e42b8b6b3da7504b5395cd7fcf0a07fbf0eca7ee37ff49531cb75aeab983e345` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v8.pdf` (172 pages) | `75fc02db997bbdc4ca3957405f79b46d0d559b427c2747889d3596d06e24c2b6` |

## Content check (on the committed files)

`content-check-final.json`:
- Word: 1,656 of 1,656 source text units; 266/266 headings; 15/15 tables;
  31/31 specimens; 9/9 list items with list styles; no missing link targets.
- PDF: no missing text units. Three interstitial extras are table header
  rows repeated after a page break (the tables repeat their header row by
  design).

## Visual inspection: partial

The production agent inspected pages by eye, but image loading repeatedly
failed and it re-viewed pages. The owner directed on 2026-10-04: "stop the
checking and get this merged." The inspection was stopped before it covered
all of §4.12 (pages 107–117 were not all confirmed) and before a full
front-to-back pass. No defect was reported from the pages it did view.
Unlike v7, there is no page-by-page visual coverage record for v8.
