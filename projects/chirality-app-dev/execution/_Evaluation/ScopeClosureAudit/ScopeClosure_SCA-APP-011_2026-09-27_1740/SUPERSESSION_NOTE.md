# Supersession note

This snapshot supersedes
`projects/chirality-app-dev/execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_1726`.
The superseded snapshot's bytes are unchanged, as are those of its
predecessors 1701 and 0505.

## Reason

The owner ruled on ESR-1 in chat on 2026-09-27 (verbatim;
`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION_ESR-1_2026-09-27.md`):

> ESR-1: retire DEP-02-02-021, DEP-02-04-015, DEP-02-04-016 and DEP-02-01-014.

The four rows are retired, so the registers and closure evidence this audit
binds have changed.

## What changed in inputs and evidence binding

- **Registers and indexes.** The `Dependencies.csv` and `_DEPENDENCIES.md` of
  DEL-02-02, DEL-02-04 and DEL-02-01 changed: four rows are `RETIRED`, and
  ESR-1 is recorded as closed.
- **Closure evidence.** It is now
  `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739/`:
  51 current units PASS, 103 edges, 0 SCC. Against 1725, four edges were
  removed.
- **Unchanged.** Everything else, including the method and the deterministic
  export check. Hashes are in `INPUT_MANIFEST.sha256`.

## Result

`CLOSED_WITH_OBSERVATIONS`: 0 critical, 0 major, 0 minor and 1 observation
(the DEL-02-03-REQ-009 residual, DX-15).
- All 29 actions are verified, and all 13 downstream reruns are COMPLETED.
- All 16 expected extraction outcomes are VERIFIED.
- The retired-surface screen has no hits.
- A rerun reproduces this snapshot byte-for-byte.

None of the ESR-1 rows was an SCA-APP-011 effect, so the verdict is unchanged.
