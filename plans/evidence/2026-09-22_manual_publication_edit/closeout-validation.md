# Publication-edit validation and reference record

WORKING_ITEMS `/root/closeout_manager`, 22 September 2026. Basis:
`0a258f145eac41a62de02b06f032ccbc183838ec`. The initial scoped preflight below preceded the final editorial and format
repairs; final reviewed bindings and integration checks follow it.

## Scoped checks

`python3 tools/run_affected_tests.py --base 0a258f145eac41a62de02b06f032ccbc183838ec`
selected practitioner-harness and validation: **897 tests and 48 subtests
passed**, exit 0, in 38.00 seconds. No product-wide suite was run locally.
The eight live commands for role validation, workflow metadata, harness
self-check and G0–G4 all exited 0. They found no role errors, 74 valid workflow
packages and 95 schema-valid tranche manifests. The entrypoints are the
unchanged commands in `.github/workflows/governance-harness.yml`; G4 here is
schema/current-tree validation, not the final committed-range check.

The currently visible change set stays within the brief; all five protected
paths presently changed are declared by the new G4 manifest. The anticipated
book DOCX/PDF paths are already declared. No new image asset is present.
All four external originals and the earlier preserved repository inputs match
`INPUTS.json`. No external original has been copied into Git or modified.

At the earlier preflight checkpoint, the operational companion Markdown matched SHA-256
`8e0782a12c9cd845d46b912c2c0dd34d90ea331b2cebd922add27fa356de86da`;
its HTML matched `861abe7b24ff9a5d80b00ead7cd0a56fdd3e3c1aa80497d17368b474a6943698`.
The renderer and dependency pins are unchanged. The publisher's exact-content,
link, anchor and resource checks pass and bind to these bytes. The closeout
manager independently reproduced the HTML in `--check` mode from an isolated
copy containing only renderer, requirements, v2 Markdown and expected HTML,
using the explicit v2 source/output paths, date 2026-09-22 and this basis.
The resulting HTML contains 22 sections, 29 headings, 8 tables and 12 code
blocks. No old-guide file or dated run evidence is a rendering dependency.
At that checkpoint the README had 15 valid local links and book-format links were pending. The final catalog and label-cleanup bindings are recorded below.

## Parent-verified public references

The primary `/root` reports reading these official sources through web tools
on **22 September 2026**. This recorder matched their URLs to the current
Selected References and editor return; it did not perform another web review
or claim full-book reading. The recorded scope is deliberately narrow.

| Source | Parent-verified scope |
|---|---|
| [APEGA, Relying on the Work of Others and Outsourcing](https://www.apega.ca/docs/default-source/pdfs/standards-guidelines/relying-on-the-work-of-others-and-outsourcing.pdf) | May 2021, version 4.0; §3.1 and §§3.1.1–3.1.2, pages 10–12. |
| [APEGA, Guidance for Registrants Regarding the Use of Artificial Intelligence Tools](https://www.apega.ca/news/2026/03/23/guidance-for-registrants-regarding-the-use-of-artificial-intelligence-tools) | 23 March 2026; continuing responsibility and due diligence. |
| [Government of Alberta, Hub Development Plan](https://www.alberta.ca/system/files/em-ets-cs-hub-development-plan-template-instructions.pdf) | Item 4.2, “Project Design Details”; DBM terminology only. No publication date verified. |
| [Anthropic, Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | Screenshot, mouse and keyboard operation in a controlled environment only. |
| [MIT Press, Brian Cantwell Smith, The Promise of Artificial Intelligence: Reckoning and Judgment](https://mitpress.mit.edu/9780262043045/the-promise-of-artificial-intelligence/) | Title, author, publisher and 2019 bibliographic metadata. |
| [University of Chicago Press, Michael Polanyi, Personal Knowledge](https://press.uchicago.edu/ucp/books/book/chicago/P/bo19722848) | Publisher/title metadata and first publication in 1958; further reading. |
| [University of Chicago Press, Michael Polanyi, The Tacit Dimension](https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368) | Verified 2009 edition, with Amartya Sen foreword; further reading. |

These checks do not establish whole-book interpretation, empirical performance,
or validation of the manual's whole framework. The source front matter and
thesis bibliography were consulted for lineage, as reported by the primary;
the unpublished thesis is not offered as public authority. Private source
notes and dispositions remain in `editor-original-source-mapping.md` and
`editor-citation-consolidation.json`, outside the book's public apparatus.

## Final candidate, reviews and integration

Root's final readiness signal and the format-integrity reviewer's sealed PASS
and stopped-write notice have been received. The two independent editorial
reviews bind the final book Markdown; the Chapter-5-through-end scope remains
byte-identical at `9ea131463569eda378013b8543816cba2ee435cb7f69c6ff5900771f0ac8b37a`.
The operational review's exact inverse confirms that the companion's later
public-title label cleanup changed no operating content. All six final
publication hashes below were independently recomputed by the closeout manager.

| Final subject under `docs/alignment-manual/` | SHA-256 |
|---|---|
| `Project_Management_for_Human_Agent_Teams_Consolidated_v4.md` | `2d9638c50a948623e7b94e7544308c1bd411765e679873a6911cdf09a8e37ca6` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v4.docx` | `084fe225407be696e8a525c48315bd7725031d6c18decdc9ed21713c66b80f36` |
| `Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf` | `ae8585916f3eea365e112fb7b8fe6a72edfafe9a75dea312e029bf9f71164411` |
| `CHIRALITY_AGENT_USER_MANUAL_v2.md` | `6739f5a559c5bae3efcdd8623457e48677fd92e21106410cba5e8e57310ddb1d` |
| `CHIRALITY_AGENT_USER_MANUAL_v2.html` | `00f3024074e8e66a2057961bde114e8a48c28bfb46583382baf6d02b9c2f9b2c` |
| `README.md` | `e2957e1d54de2fd4a967200a63c1e3b19e7e82a4bf080797e2f83a9d56f10e83` |

The full 162-page rendered-document visual evidence is PASS: 83 unchanged
whole pages, 46 directly re-inspected pages, and 33 pages with only verified
footer-digit changes cover every final page exactly once. The independent
integrity reviewer verified all 162 final3/final2 page identities and all 27
scoped content/package/navigation checks. The closeout manager checked that
coverage arithmetic and its artifact hashes, without claiming another full
visual read. The format review binds all 88 Contents destinations and folios.
The HTML's own browser/responsive/print visual QA and live Microsoft Word
interaction remain unperformed; no browser workaround was used.

Actual execution is recorded in the role-specific source/return files:
`editor-run-context.json` identifies the HELPS_HUMANS editorial manager and
three executed TASK children; `operations-sources.json` identifies the
WORKING_ITEMS operational manager with no descendants; `html-inputs.json`
identifies the TASK publisher. `format-production-provenance.json` and
`format-visual-coverage.json` identify the WORKING_ITEMS formatting manager,
five TASK final-page readers and root's actual pages 141–163 read after a
sixth launch hit the thread limit. No nonexistent sixth child is counted.
The editorial, operational and integrity reviewers identify their independent
native TASK execution in their returns; `format-integrity-run-context.json`
records its supplied basis and actual boundary. These were native Codex
collaboration agents, not Chirality-managed sessions. Role/write scopes were
instruction-based on the broad host; no model-diversity or separate mechanical
sandbox claim is made. This closeout manager spawned no children.

Fresh main was fast-forwarded from the source basis to
`1b5adbf50142a4c01c454c62a31dfcdc60da1894`, with no publication overlap and no
closeout-instruction or CI-entrypoint change. It updated the live-baseline
fixture and project-state records. The affected test module passed **11 tests**
and harness self-check exited 0; the earlier 897-test/48-subtest preflight was
not redundantly repeated. All **264 local link/fragment targets** across the
book Markdown, companion MD/HTML and catalog resolve against the integrated
submission. None intersects an incoming changed target, so no cited operating
instruction needed reopening. The companion keeps its explicit `0a258f…`
source basis. The final catalog has 17 valid local links. External originals
and earlier preserved repository inputs remain unchanged.

Complete committed-range G4/conflict checks, source commit, required CI and
merge outcome are retained in ordinary PR/Git history rather than a
self-referential commit hash. The root's standing Git grant and final-ready
signal authorize scoped closeout; additional non-required product coverage
is reported truthfully and left running rather than made into a new gate.
Git integration establishes neither public release nor live workflow adoption.
