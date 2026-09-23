# Cross-format review — authorship front matter in v5

**Verdict: PASS.** No actionable format, navigation, pagination, citation, metadata, or preservation finding was identified in the assigned scope.

The exact reviewed v5 artifact identities match the assignment:

| Artifact | SHA-256 |
|---|---|
| Markdown | `e7f8579110e95f57c618bec304462dc04419b6f48bada9a296404cf8b91f609d` |
| DOCX | `73cf67dea870ebfbfccb903f1b0c4c275b5d3f4770f48f0ce2cc83f2990d2722` |
| PDF and `/tmp/manual-v5-authorship-20260922/final2/` PDF | `dac39dc716c0510cddf5a447506d20b730efb5c2d4410937ce544aa26e8031da` |

I inspected the final2 rendered PNGs for physical pages 1–7 one by one at original resolution and verified that their source PDF is byte-identical to the v5 PDF in the repository. The cover is unnumbered and shows only “A Practical Manual,” the unversioned title, and Ryan Tufts. The authorship account occupies physical pages 2–4 with printed folios i–iii. Contents occupies pages 5–6 with folios iv–v. Preface begins on physical page 7 with Arabic folio 1. The page transitions are clean: no clipped text, overlap, stranded heading, or blank intermediary page. Page 4 ends the authorship material and source notes before Contents; page 6 finishes Contents before the Preface page break.

The DOCX contains 89 static Contents links. The new “Authorship and preparation of this manual” entry is the first link, points to the unique `h_authorship` bookmark on the section heading, and caches the literal folio `i`. In the PDF, I located that row’s topmost link annotation on physical page 5 and resolved its page-object destination to physical page 2, whose visible folio is i. The Preface entry caches 1 and the rendered Preface begins at folio 1. The OOXML section settings use lower-Roman numbering from 1 for front matter and restart decimal numbering at 1 for the Preface section.

The rendered authorship pages contain the `[A1]`–`[A5]` local citations and no bare `[1]`–`[5]` markers. The A2 text refers to the present manual and its Preface and §§1.2 and 1.5; no predecessor-edition labels appear on the authorship pages. The local A labels remain separate from the manual’s global numeric reference set. This check was confined to those front-matter citations; the prior Markdown review remains the substantive content review.

Metadata agrees across DOCX and PDF and with v4’s established metadata. The DOCX title is “Project Management for Human–Agent Teams,” subject “A Practical Manual,” creator Ryan Tufts, and keywords remain the established project terms. Its `lastModifiedBy` and application fields identify Codex, as in v4; page count is 165. The PDF title, subject, author, and keywords match those values; it has 165 pages at 486 × 666 points. Neither cover nor title metadata carries an edition/version label.

All three v4 original artifacts still match the source hashes in `INPUTS.json`:

| v4 original | SHA-256 | Result |
|---|---|---|
| Markdown | `2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6` | Match |
| DOCX | `084fe225407be696e8a525c48315bd7725031d6c18decdc9ed21713c66b80f36` | Match |
| PDF | `ae8585916f3eea365e112fb7b8fe6a72edfafe9a75dea312e029bf9f71164411` | Match |

I used SHA-256 identity checks, original-detail visual inspection of the supplied final2 PNGs, DOCX OOXML inspection for metadata, bookmarks, static Contents text and section numbering, and bundled `pypdf` extraction/annotation resolution against the final2 PDF. The system `pdftotext` executable was unavailable; `pypdf` supplied the bounded text checks. The earlier Markdown authorship review at SHA-256 `45b87b3bb654590ec6adfd8cb332f832b988662e4a0eb6e60d2a071857d2113e` remains applicable as directed.

This was a bounded cross-format review of v5 pages 1–7 and the new Contents destination. I did not inspect the remaining 158 pages, recheck all other Contents destinations, re-render the artifacts, review the full manuscript, or perform Git operations. No v5 artifact was changed; only this report and `format-review-v5-evidence.json` were written.

Native execution parentage was `/root` → `/root/authorship_insert_review`, as shown by the collaboration agent tree. This was a delegated-harness-native Type 2 task; no descendant was created. The active instruction origins and exact hashes were:

- `/Users/ryan/.codex/worktrees/da43/chirality/AGENTS.md` — `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`
- `/Users/ryan/.codex/worktrees/da43/chirality/agents/AGENT_TASK.md` — `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `/Users/ryan/.codex/plugins/cache/openai-primary-runtime/pdf/26.904.11930/skills/pdf/SKILL.md` — `afc4472ec4d625f703e9f414fe6814ce3cfa0ec51c7a07887fe587264c8b561e`
- `/Users/ryan/.codex/plugins/cache/openai-primary-runtime/documents/26.904.11930/skills/documents/SKILL.md` — `3154ace095b79bace582d7dc53c7744a40f835fe762726220708bde2360749aa`
- `/Users/ryan/.codex/plugins/cache/openai-primary-runtime/documents/26.904.11930/skills/documents/tasks/read_review.md` — `3345256289dfe6e4c77a59e26ba0ef9f781296a9633e5769a88090c1ac24ee83`
- `/Users/ryan/.codex/plugins/cache/openai-primary-runtime/documents/26.904.11930/skills/documents/ooxml/hyperlinks_and_fields.md` — `470b6c722d12f614fdd8bd9da66aa9983a3f5c4494c76b5def6ebec668327af6`
- `/Users/ryan/.codex/plugins/cache/openai-primary-runtime/documents/26.904.11930/skills/documents/writing_quality.md` — `30baf502bdea6b565d41344f87e46bf04840e1b99f84a11009992bf6e63596e8`
