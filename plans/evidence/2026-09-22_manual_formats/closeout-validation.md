# Formats closeout validation

WORKING_ITEMS `/root/closeout_manager`, 2026-09-22. Branch:
`codex/management-manual-v2-formats-20260922`. Initial basis:
`e74feb34b7ca99ebeb903ffb52f7fdd2b3efd169`.

## Scoped preflight

The maintained affected-test wrapper selected practitioner-harness and
validation only: **897 tests and 48 subtests passed**. Role/workflow
validation, self-check and live G0–G4 also exited 0. G4 schema validation
includes this run's new manifest among 94 manifests. Commands, timing and
summaries are retained in `closeout-local-checks.json`.

`closeout-preflight.json` records the independent checks of the frozen HTML
submission while the DOCX/PDF table-wrapping repair and visual reviews were
still active. The checked change set stayed within the brief, all six
protected paths were declared, and all preserved input hashes matched.
The renderer's Python AST outside its CSS value is unchanged; the complete
HTML outside the stylesheet is byte-identical to the prior edition. The
publisher's parity report matches current HTML bytes. Deterministic
`--check` also passes from an isolated copy containing only renderer,
requirements, Markdown source and expected HTML, using installed pinned
dependencies. No permanent Word/PDF builder or dependency-pin change is
included in the inspected submission.

The restyled HTML remains source-complete and reproducible. Its own browser,
responsive and print layout are not visually verified; no alternate route
around the earlier browser URL policy was attempted. Reference-document
inspection does not establish rendered HTML layout.

## Final publication and visual review

The document manager sealed all six disjoint TASK review ranges, covering
physical pages 1–180 with PASS and no unresolved findings. The two corrections
are complete: header-cell insets on page 17 avoid the inherited midword wrap,
and local left alignment on page 5 improves two technical paragraphs without
changing their text. The closeout manager independently compared the recorded
page hashes: 178 pages remain identical to the fully inspected candidate;
only pages 5 and 17 changed, and both have explicit passing rechecks.

The independent publication reviewer completed source, package, link,
numbering and selected visual checks, with no unresolved actionable finding.
Its final DOCX/PDF hashes match the artifacts and the manager's sealed visual
and structural records. All 81 Contents destinations match the final printed
folios. All frozen Markdown/v1/figure inputs still match. The six publication
subject hashes, exact range coverage and evidence bindings are recorded in
`closeout-review-binding.json`; the closeout manager does not claim a second
full page-by-page visual read.

Thus full rendered DOCX/PDF visual QA has passed. The restyled HTML's own
browser/responsive/print visual QA remains unverified, and no live Microsoft
Word interaction or Word-native field-refresh check is claimed. These are
separate boundaries.

The root gave its content/visual-ready signal and the independent reviewer
delivered its final notice. Freshly fetched origin/main still equals the
branch's base, so no integration change was necessary before committing.
Publication bytes remain frozen. Complete committed-range conflict/G4 checks,
source revision and CI/merge outcome are retained in ordinary PR/Git history.
The final binary layout and evidence-only corrections do not invalidate the
completed Python suites; no full-suite repetition is claimed or needed.

The actual merge gate remains required CI and independent review under the
standing owner authorization. Extra automatic Piping coverage is not a new
gate for a slice with no Piping product change; investigate material failures
and report pending/skipped checks truthfully. Preserve final candidate, check
and merge state in ordinary PR/Git history. No staging, commit or push was
performed during the earlier preflight; the final signal now authorizes
ordinary Git closeout.
