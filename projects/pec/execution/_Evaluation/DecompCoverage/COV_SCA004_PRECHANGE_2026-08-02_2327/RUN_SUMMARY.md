# Run Summary — COV_SCA004_PRECHANGE_2026-08-02

`RUN_STATUS = WARNINGS`

- Overall status: `WARNINGS`
- Closure readiness: `WARN` for structural pre-change-baseline use
- Issues: 0 blockers / 1 warning / 69 info
- Coverage: 11/11 packages; 64/64 deliverables; 64/64 contexts
- Lifecycle: 28 `INITIALIZED`; 32 `OPEN`; 4 `CHECKING`
- Contracts: 32 valid `SOW_V1`; 32 absent at `OPEN`; 0 ambiguous
- Artifacts: 3/64 anticipated artifact sets found in their deliverable folders
- Ledger: 94 rows; all 71 `IN` references resolve
- Objectives: all 6 have active filesystem-backed support
- Expected source: revision 1.3 `current_basis` plus D-PEC-78 O-A and the
  confirmed SCA-004 Gate 1 intake
- Phase: `SCA-004 Gate 2 pre-change baseline`

The single warning is deliverable-local artifact-location evidence:
`DEL-08-02` is `CHECKING`, while its anticipated schema/test set is not found
inside its deliverable folder. Accepted production bytes exist elsewhere,
but this audit's Check 6 is explicitly deliverable-folder-scoped. This does
not contradict the accepted artifact ruling and is non-blocking for the
SCA-004 pre-change topology baseline.

The 69 informational findings comprise 60 other absent anticipated artifact
sets at pre-production states and 9 accepted unmapped deliverables.
