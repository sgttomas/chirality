# Alignment manual and agent guide

This directory brings together the supplied project-management manuscript, its repository-informed revision, and practical documentation for agent-assisted work in Chirality. These documents explain and propose; the repository and applicable project instructions, accepted decisions, and current source records govern the work.

## Documents

| Document | Use |
| --- | --- |
| [Chirality Agent User Manual v1 — HTML](CHIRALITY_AGENT_USER_MANUAL_v1.html) · [Markdown](CHIRALITY_AGENT_USER_MANUAL_v1.md) | Operational guidance for entry, coordination, project development, checking, continuity, and closeout across App, Piping, Runtime, and PEC. The HTML is the offline reading edition. |
| [Project Management for Human–Agent Teams — Consolidated v2](Project_Management_for_Human_Agent_Teams_Consolidated_v2.md) | The incremented manuscript with repository-informed improvements, preserving v1 as its source lineage. |
| [Manual review v1](MANUAL_REVIEW_v1.md) | The repository applicability review, chapter findings, revision rationale, and source basis. |
| [Project Management for Human–Agent Teams — Consolidated v1](Project_Management_for_Human_Agent_Teams_Consolidated_v1.md) | The supplied Markdown manuscript, preserved without changes. Original [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v1.docx) and [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v1.pdf) copies are also preserved. |

## Read offline

The agent guide’s HTML edition is a complete rendering of its Markdown source. Open the HTML file directly in a browser. It has chapter navigation, a compact contents menu on small screens, browser-find support, accessible table scrolling, and print styles. Reading requires no network connection, downloaded fonts, or external assets. Links to repository source files work when this directory remains inside the repository checkout; external reference links need a connection when followed.

The visible source date and repository revision describe the edition’s basis. The SHA-256 fingerprint identifies the exact Markdown bytes used for the HTML. They do not establish current project status or human acceptance.

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
  --basis-date 2026-09-22 \
  --basis-revision 9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8
```

Add `--check` to verify that the committed HTML matches the source and renderer without writing. The default input is `CHIRALITY_AGENT_USER_MANUAL_v1.md` beside the renderer, and the output has the same name with an `.html` extension. `--source` and `--output` accept other paths. Keep the HTML beside its Markdown source so that repository-relative source links retain their meaning.

The date and revision are required arguments rather than the current clock or `HEAD`, so identical inputs produce identical output. Update those arguments deliberately when the guide’s source basis changes. The renderer rejects duplicate IDs, missing in-page link targets, and non-embedded image or media assets. Raw source HTML is limited to a passive semantic tag and attribute subset; style, script, embedded application, and unsupported resource markup fail clearly without being stripped. This is an authoring constraint for trusted repository documentation, not a general HTML sanitizer. Ordinary browser links are preserved as authored.

After regeneration, check source links and inspect the HTML at desktop and narrow mobile widths, including a table and code block. Check print preview for clipped content. The renderer verifies document structure and staleness; it does not replace editorial or visual review.
