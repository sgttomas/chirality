# User Manual v2 HTML return

Date: 2026-09-22. Executor: `/root/html_publisher`, TASK Type 2; parent: `/root`. Repository basis: `0a258f145eac41a62de02b06f032ccbc183838ec`.

Generated `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v2.html` from the parent-approved final Markdown candidate, including the one-label public-title cleanup following the independently backchecked operational repairs. The existing book-style renderer and its CSS are unchanged. The v1 Markdown/HTML and all source manuscripts remain untouched by the publisher.

- Approved source SHA-256: `6739f5a559c5bae3efcdd8623457e48677fd92e21106410cba5e8e57310ddb1d`.
- HTML SHA-256: `00f3024074e8e66a2057961bde114e8a48c28bfb46583382baf6d02b9c2f9b2c`.
- Unchanged renderer SHA-256: `4d70e13e78307da22d622f511251530f6cb7a206680f1cb35487ea9a18eacc08`.

The generated document preserves all 214 paragraphs, 8 tables, 12 code blocks, 29 headings, and 393 source anchor elements. The inherited navigation contains 22 H2 sections, including Contents. All exact content/link parity, local paths/fragments, in-page targets, unique IDs, embedded-resource, source-fingerprint and deterministic-output checks pass. The four known raw resource bypasses still reject. No renderer extension was necessary.

Exact generation command from the repository root, using the bundled-derived temporary environment:

```sh
/var/folders/96/1_3ww0012pv5ptwwsd1990yw0000gn/T/chirality-html-book-style-3sufm493/venv/bin/python docs/alignment-manual/render_manual.py \
  --source docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v2.md \
  --output docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v2.html \
  --basis-date 2026-09-22 \
  --basis-revision 0a258f145eac41a62de02b06f032ccbc183838ec
```

Append `--check` for the no-write deterministic check. The exact-content and link check is `python plans/evidence/2026-09-22_manual_publication_edit/html-check.py` in an environment with the unchanged pinned requirements. Its report is `html-publisher-production-checks.json`; security cases are in `html-security-checks.json`.

The README now presents PM v4 Markdown/Word/PDF and User Manual v2 Markdown/HTML as current editions, with earlier repository editions and review records in a less prominent Archive group. The current book title is plain. Its renderer instructions use explicit v2 source/output paths and the correct source basis. All 17 local catalog links resolve. The final Word/PDF target hashes match the parent-supplied artifact hashes; they were linked but not authored or edited by this executor. No publisher work remains.

No browser, WebKit, HTTP preview, alternate local URL route, or rendered HTML visual inspection was performed. The prior URL-policy boundary remains in force. This return establishes source/content/navigation/security parity, not live responsive behavior or browser/print-layout visual validation. No DOCX/PDF or Git operations were performed by this executor in this continuation.
