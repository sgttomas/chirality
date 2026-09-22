# HTML book-style return

Date: 2026-09-22. Executor: `/root/html_publisher`, TASK Type 2; parent: `/root`. Basis commit: `e74feb34b7ca99ebeb903ffb52f7fdd2b3efd169`.

The agent guide’s HTML now follows the retained management manual’s book style: black local serif typography, a centered uppercase title, white paper, a narrower reading measure, and grayscale table/code treatment. The screen edition uses 18px type with more generous leading; narrow screens retain left-aligned prose and the existing contents control. Print CSS uses the original 6.75 × 9.25 inch trim, corresponding margins, 10.5pt body, 9pt tables, and 8pt code. Code hyphenation is disabled. The guide’s own title and all content remain unchanged.

The reference was inspected through the original v1 DOCX style XML and PDF pages 1, 5, and 6, including its cover and chapter/body typography. Reference inspection used bundled Python, pypdf, and Poppler, plus `view_image`. The document manager also supplied its source-derived style profile. No DOCX or PDF was authored or edited by this executor.

Only the renderer’s CSS changed: its remaining Python AST is identical to the baseline, and the complete generated HTML outside its stylesheet is byte-for-byte identical to the prior edition. This preserves the content, metadata, navigation, anchors, script, and security behavior. The Markdown SHA-256 remains `2b749f8f12dcd803c6017c93fa6e850257f4aaf88b3d07781842a8a4c0d2ab2b`.

Current renderer SHA-256: `4d70e13e78307da22d622f511251530f6cb7a206680f1cb35487ea9a18eacc08`.

Current HTML SHA-256: `f743bb5ed751329007b89d9385dfb2c6dcf7525925a2040e288f0a1fae530ead`.

The current candidate passes exact paragraph/table/code/heading/link parity, all local links and in-page targets, unique-ID and embedded-asset checks, and deterministic `--check`. The four previously reported raw resource mechanisms still reject. The stylesheet adds no external resource URL or font load. The unchanged old-run checker was copied into this evidence directory so its new report does not overwrite historical evidence.

The directory README now links the actual v2 Word and PDF outputs, describes the reference styling, and distinguishes the one-off management-manual format production from the maintained agent-guide HTML renderer. All 11 local README links exist. The document manager retains responsibility for the new Word/PDF files and their final visual QA.

No browser, WebKit, HTTP preview, or alternate route around the prior URL policy block was used. Reference-document images were inspected; the restyled HTML itself was not visually rendered. No live responsive behavior or browser/print-layout visual validation is claimed. The pre-existing native Pango limitation was not retried or bypassed.

The source guide, source manuscripts, original v1 formats, dependency pins, root README, prior run evidence, project state, and Git state were not changed by this executor. Independent review and Git integration remain with the parent.
