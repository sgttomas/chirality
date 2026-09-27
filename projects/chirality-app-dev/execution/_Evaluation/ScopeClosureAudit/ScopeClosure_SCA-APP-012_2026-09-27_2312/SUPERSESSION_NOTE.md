# Supersession note

This snapshot supersedes
`projects/chirality-app-dev/execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-012_2026-09-27_2240`,
the first SCA-APP-012 snapshot. The superseded snapshot's bytes are unchanged.

## Reason

The independent review fix N2 (`ed2afdd37`) reworded the EVQ-006 note line in
the DEL-05-03 and DEL-06-01 `_DEPENDENCIES.md` indexes. The 2240 snapshot's
`INPUT_MANIFEST.sha256`, and the `Tool_Run.json` of the closure snapshot it
reads (`CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234`), bind the earlier
bytes of those two files. Rerun at `ed2afdd37`, the 2240 script's closure check
finds the input basis no longer current: `CLOSED_WITH_OBSERVATIONS`, 1 minor
finding, 8 of 9 reruns. The closure evidence therefore had to be rebound, as
the SCA-APP-011 precedent `d08b589ea` did.

## What changed in inputs and evidence binding

- **Changed inputs.** Only the DEL-05-03 and DEL-06-01 `_DEPENDENCIES.md`
  indexes (`9381bf13…` → `ac6a1aae…`; `ad877d0e…` → `551c642a…`). No register
  row, count or edge changed. Each index now names the one `LastSeen`-only row
  that carries the pre-existing EVQ-006 finding (DEP-05-03-001,
  DEP-06-01-001).
- **Closure evidence.** The post-extraction closure evidence is now
  `_Evaluation/DepClosure/CLOSURE_SCA_APP_012_REBIND_2026-09-27_2311/`. It binds
  the current registers and indexes. Its topology is unchanged: 54 nodes,
  102 edges, 0 SCC and 7 isolates in ALL; the 51 current units PASS; every
  analyzer delta against 2234 is zero.
- **Script.** `audit_scope_closure_run.py` is the 2240 script with the closure
  snapshot path, the supersession reference and the matching report text
  changed. The checks are the same.

All the other inputs are unchanged. Their hashes are in
`INPUT_MANIFEST.sha256`.

## Result

`CLOSED`: 0 critical, 0 major, 0 minor and 0 observations.
- All 24 actions are verified.
- All 9 downstream reruns are COMPLETED.
- All 7 expected extraction outcomes (DX-01 to DX-07) are VERIFIED.
- Supersession bindings 14/14; the map check is clean (exit 0, 0 findings,
  byte-for-byte).
- A rerun of `audit_scope_closure_run.py` reproduces this snapshot
  byte-for-byte.
