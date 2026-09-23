# Alignment manual and agent guide

This directory contains a general project-management reference and the Chirality Agent User Manual. The book explains management practice; the companion provides operational guidance for work in this repository. Applicable instructions, accepted decisions, and current source records govern actual project work.

## Current editions

| Document | Use |
| --- | --- |
| [Project Management for Human–Agent Teams](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md) · [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v7.docx) · [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v7.pdf) | General management practice from conception through delivery, written as a technical reference. |
| [Chirality Agent User Manual v3 — HTML](CHIRALITY_AGENT_USER_MANUAL_v3.html) · [Markdown](CHIRALITY_AGENT_USER_MANUAL_v3.md) | Operational guidance for entry, coordination, project development, checking, continuity, and closeout across App, Piping, Runtime, and PEC. The HTML is the offline reading edition. |

The companion describes the management manual’s current methods and identifies where adopted project instructions still differ. Reading either manual does not amend those instructions or adopt a new execution basis.

## Read offline

The agent guide’s HTML edition is a complete rendering of its Markdown source. Open the HTML file directly in a browser. It has chapter navigation, a compact contents menu on small screens, browser-find support, accessible table scrolling, and print styles. Reading requires no network connection, downloaded fonts, or external assets. Links to repository source files work when this directory remains inside the repository checkout; external reference links need a connection when followed.

The HTML follows the supplied manuscript’s book style: black serif type, white paper, restrained headings, and gray table headers. Its type size and spacing are adapted for screen reading, with local Liberation Serif, Times New Roman, or Georgia fonts. Print styles use the manuscript’s 6.75 × 9.25 inch page size.

The visible source date and repository revision describe the edition’s basis. The SHA-256 fingerprint identifies the exact Markdown bytes used for the HTML. They do not establish current project status or human acceptance.

## Maintain the management-manual formats

The Word and PDF editions follow the retained technical-reference book layout. Their current preparation is recorded in the [v7 preparation and review evidence](../../plans/evidence/2026-09-22_manual_v7/). For a later revision, carry the authorized Markdown changes into the retained layout, preserve its typography and page setup, then regenerate and visually inspect the Word/PDF output. The renderer below generates the agent guide’s HTML edition only.

## Maintain the HTML edition

Edit the Markdown source and regenerate the HTML; do not edit the generated HTML directly. The renderer uses Python 3.10 or newer and the two exact dependency versions in [requirements.txt](requirements.txt). It uses the installed `markdown-it-py` parser for CommonMark, tables, and strikethrough. It does not fetch resources. Rendering preserves supported semantic HTML, including explicit anchors, and adds unique stable IDs to all headings.

From the repository root, install the dependencies once in a local environment outside tracked content:

```sh
python3 -m venv /tmp/chirality-manual-renderer
/tmp/chirality-manual-renderer/bin/python -m pip install -r docs/alignment-manual/requirements.txt
```

Render this edition with its explicit source basis:

```sh
/tmp/chirality-manual-renderer/bin/python docs/alignment-manual/render_manual.py \
  --source docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.md \
  --output docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.html \
  --basis-date 2026-09-22 \
  --basis-revision b3e2ce4ec74e01d6f393fc0bc069699bb079df91
```

Add `--check` to verify that the committed HTML matches the source and renderer without writing. Use explicit `--source` and `--output` paths as shown for the current edition; the renderer’s unqualified default remains v1. Keep the HTML beside its Markdown source so that repository-relative source links retain their meaning. Archived editions retain their own source date and revision.

The date and revision are required arguments rather than the current clock or `HEAD`, so identical inputs produce identical output. Update those arguments deliberately when the guide’s source basis changes. The renderer rejects duplicate IDs, missing in-page link targets, and non-embedded image or media assets. Raw source HTML is limited to a passive semantic tag and attribute subset; style, script, embedded application, and unsupported resource markup fail clearly without being stripped. This is an authoring constraint for trusted repository documentation, not a general HTML sanitizer. Ordinary browser links are preserved as authored.

After regeneration, check source links and inspect the HTML at desktop and narrow mobile widths, including a table and code block. Check print preview for clipped content. The renderer verifies document structure and staleness; it does not replace editorial or visual review.

## Archive

Earlier files and review records remain available for repository continuity.

| Document | Files |
| --- | --- |
| Project Management for Human–Agent Teams — Consolidated v5 | [Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v5.md) · [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v5.docx) · [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf) · [Preparation evidence](../../plans/evidence/2026-09-22_manual_authorship_frontmatter/) |
| Chirality Agent User Manual v2 | [HTML](CHIRALITY_AGENT_USER_MANUAL_v2.html) · [Markdown](CHIRALITY_AGENT_USER_MANUAL_v2.md) |
| Project Management for Human–Agent Teams — Consolidated v4 | [Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v4.md) · [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx) · [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf) · [Publication evidence](../../plans/evidence/2026-09-22_manual_publication_edit/) |
| Chirality Agent User Manual v1 | [HTML](CHIRALITY_AGENT_USER_MANUAL_v1.html) · [Markdown](CHIRALITY_AGENT_USER_MANUAL_v1.md) |
| Project Management for Human–Agent Teams — Consolidated v2 | [Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v2.md) · [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx) · [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v2.pdf) · [Format-production evidence](../../plans/evidence/2026-09-22_manual_formats/) |
| Project Management for Human–Agent Teams — Consolidated v1 | Preserved original [Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v1.md) · [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx) · [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v1.pdf) |
| Manual review v1 | [Repository applicability review](MANUAL_REVIEW_v1.md) |
