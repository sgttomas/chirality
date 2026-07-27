# Read-only Adversarial Return

## Verdict

`PASS` — the bounded M2 pin refresh is correctly scoped and proves the 46-file
Root state without weakening the tests. Residuals are non-blocking.

## Required static evidence

The three live-root tests now correctly bind:

- adapter baseline: 46 files, zero mismatch;
- drift: 46 files, 46 matches, zero mismatch, zero unparseable documents,
  zero documents without a state assertion, and exact baseline text `0/46`;
- status: 45 `INITIALIZED`, one `OPEN`, 46 total, and the unchanged
  no-DAG-pointer observation.

Test names and local provenance now attribute the 46th deliverable to the
bounded 2026-07-26 SCA-001 DEL-02-06 PROJECT_SETUP refresh.

## Scope and amendment disposition

The specialist initially identified the stale module-level LIVE-tree summary.
Agent 0 then issued `BRIEF_AMENDMENT_01.md`, allowing only that directly
coupled summary to change from 45/all-OPEN to 46 total, zero mismatch, and 45
`INITIALIZED` plus one `OPEN`. The manager applied the amendment. No production
harness, adapter value, guard, scaffold, audit, decomposition, runtime,
lifecycle, downstream-loop, dynamic assertion, or unrelated test changed.

## Atomic SCC

- Accepted basis `ff04694`: 45 status files, all `INITIALIZED`, adapter `45/0`;
  the 46-file pin fails.
- Project Setup candidate `dd28d201b`: 46 files, 45 `INITIALIZED` plus
  DEL-02-06 `OPEN`, adapter `46/0`; the old 45-file tests fail exactly three
  times.
- Resolution move: `MERGE` — state commit and pin commit stay separate inside
  the one human-gated PR #369. Neither half is independently acceptable.

## Governance and derivative disposition

- The G4 manifest declares the exact two protected paths, complete M2 fields,
  `human-gated-pr`, `self_merge: false`, M6 `none-required`, bounded scope, SCC
  disposition, and export deferral.
- No active project/domain pin or mirror was found for either touched path.
- The public export includes the test and root governance documents as
  derivative bytes; regeneration remains deferred until it can consume
  accepted post-merge bytes.
- Separate SCA-001 App/PEC carrier notices remain separate program follow-ons;
  this test-only M6 disposition does not discharge them.

## Independently reviewed validation

- Focused test file: `38/38 PASS`
- Full practitioner harness: `349/349 PASS`
- G0–G4 tests: `124/124 PASS`
- Live G0–G4 validators: `PASS`
- Direct manifest validation: zero failures, zero notes
- Instruction coverage: two paths, zero uncovered or unauthorized
- Pin-only overlay on `ff04694`: exactly three failures and 35 passes
- `git diff --check`: `PASS`

## Non-blocking residual

`execution/_harness/adapter.yaml` retains an obsolete D-GOV-21 step-9
provenance lead-in immediately before its correct SCA-001 explanation. The
live values are correct and all deterministic checks pass. Adapter-state edits
are excluded from this lane, so PROJECT_SETUP owns any later owner-authorized
prose-only correction.
