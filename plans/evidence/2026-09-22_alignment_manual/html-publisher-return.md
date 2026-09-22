# Offline HTML publication return

Date: 2026-09-22. Executor: `/root/html_publisher`, TASK Type 2. Parent: `/root`.

## Delivered

- `docs/alignment-manual/render_manual.py`: deterministic renderer using `markdown-it-py==4.2.0` and `mdurl==0.1.2`; no handwritten Markdown parser.
- `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v1.html`: self-contained offline reading edition, generated from source SHA-256 `2b749f8f12dcd803c6017c93fa6e850257f4aaf88b3d07781842a8a4c0d2ab2b`. HTML SHA-256: `77bbc449bca0daa3ba4dd3644119a6deaedff3f89f606b26824a0bce504339b5`.
- `docs/alignment-manual/README.md` and `requirements.txt`: document links, edition basis, dependency pins, rendering/check invocation, and maintenance instructions.
- One root `README.md` navigation link under “Develop and contribute.” No other root edits.
- Reproducible publication check in `html-publisher-check.py`, plus JSON evidence for input origins/hashes, fixture checks, the focused offline-markup repair, production parity, and README local links.

The HTML contains all 193 source paragraphs, 7 tables, 10 code blocks, 28 headings, and 364 anchor elements. There are 22 H2 navigation sections: the source Contents plus 21 numbered chapters. Its sticky desktop navigation, mobile native contents control, skip link, visible source metadata, scrollable tables/code, local fonts, and print CSS are supplied by the renderer. The mobile contents control uses one local script to close after a section link is selected. No resource fetch is required to read the file.

## Verification

The production checker passes visible-text, exact paragraph/table/code content, heading content, source-link sequence, and source-element-count parity against the maintained Markdown parser's baseline rendering. Page IDs are unique, all in-page targets resolve, all linked local paths and Markdown/HTML fragments resolve, and source SHA-256 is visible. All 20 local links in the two README files exist. Regenerating in `--check` mode reports an exact byte match.

Publication review found and backchecked a bounded correction: the initial resource audit did not catch CSS/object/iframe resource mechanisms. Raw source HTML now uses an explicit passive tag/attribute subset, validated before the renderer's trusted CSS and script are inserted. The four reported bypasses fail clearly; normal anchors, aligned tables, and literal code remain supported. This is an authoring constraint for trusted documentation, not a general HTML sanitizer. The reviewer also verified the corrected “sections” navigation count. The checked renderer SHA-256 is `caaa10a48f51b79f451b238327cdd57bed9a89de6c97b2c29db3851300dc1e4e`.

Generation command, run from the repository root:

```sh
python3 docs/alignment-manual/render_manual.py \
  --basis-date 2026-09-22 \
  --basis-revision 9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8
```

Append `--check` to verify the current HTML without writing. Run the production checker with:

```sh
python3 plans/evidence/2026-09-22_alignment_manual/html-publisher-check.py
```

## Visual boundary and cleanup

The parent retained visual inspection. After generation, the parent initially requested a loopback-only preview; session `31946` listened on `127.0.0.1:62702`. The parent then reported that CUA's URL security policy had blocked `file://` viewing and explicitly forbade alternate browser routes. The preview was stopped immediately with SIGINT, before this executor made any HTTP or browser request. It is not available and was not used as a workaround.

No live desktop browser, mobile viewport, responsive interaction, or browser print-preview result is claimed by this executor. A subsequent parent assignment requested bounded static print inspection with WeasyPrint, every URL fetch denied, and Poppler images. The PDF skill and bundled runtime paths were read. Prerequisite inspection found no native Pango library in system lookup, `/opt/homebrew/lib`, `/usr/local/lib`, or the bundled dependency inventory. Bundled Cairo, GObject, and Poppler do not provide the missing Pango requirement. As instructed, the attempt stopped at that limit rather than spending excessive effort on native dependency installation.

No Python environment, PDF, page image, contact sheet, or additional preview route was created. No PDF authoring command was reached, so the skill's create marker was not run. There are no additional large temporary products to remove. The exact checked paths, unchanged source/HTML hashes, and tool boundary are recorded in `html-publisher-offline-qa.json`. Static print layout therefore remains unverified by this attempt. Structural checks alone do not establish rendered layout, and static output would not establish live browser behavior.

No guide Markdown, supplied originals, v2 manuscript, review manuscript, project instructions, project state, or Git state was changed by this executor. The parent carries final content review, static visual inspection, integration, and Git closeout. The renderer is ready to regenerate if that review changes the source.
