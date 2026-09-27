# Supersession note

This snapshot supersedes
`projects/chirality-app-dev/execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_0505`.
The superseded snapshot's bytes stay unchanged as historical evidence.

## Reason

The 0505 snapshot recorded the pre-setup state, with verdict `OPEN`. Its open
items were:
- incremental setup not run;
- dependency re-extraction not run for seven deliverables;
- the post-extraction closure audit not run;
- the APP-R058 disposition not recorded;
- eleven ACTIVE rows describing retired surfaces.

All of these have since been carried out under the owner's act of 2026-09-27
(`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`).

## What changed in inputs and evidence binding

- **Setup log.** `_Coordination/SETUP_LOG.md` now exists, with the `BASELINE`
  line and `INCREMENTAL SCA-APP-011 setup COMPLETE`.
- **Registers.** `Dependencies.csv` and `_DEPENDENCIES.md` of the 25 planned
  deliverables were re-extracted. Their Run Notes bind decomposition SHA-256
  `cf6e56eb…1876`.
- **Closure.** A new closure snapshot binds the current registers:
  `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/`.
- **APP-R058.** The disposition is recorded in
  `_Coordination/_TaskManagement/ROW_MAINTENANCE_APP-R058_SCA-APP-011_CLOSURE_2026-09-27.md`.
- **Method extensions.**
  - The retired-surface screen now also carries the reviewer's broadened
    case-insensitive terms and an explicit allow-list for retained-dispatch
    rows.
  - A new extension verifies the expected extraction outcomes DX-01 to DX-16
    (`DX_Verification.csv`).
- **Unchanged inputs.** The accepted register, the decomposition, the
  supersession delta and map, and the same-day audit-decomp matrix are as
  before. Their hashes are in `INPUT_MANIFEST.sha256`.

## Result

`CLOSED_WITH_OBSERVATIONS`: 0 critical, 0 major, 0 minor and 1 observation.
The observation is the DEL-02-03-REQ-009 wording residual, DX-15. All 29
actions are verified, and 16 of 16 expected outcomes are verified.
