# Run Summary — COV_SCA005_PRECHANGE_2026-09-23

`RUN_STATUS = WARNINGS`

- Overall status: `WARNINGS`
- Closure readiness: `WARN` for structural pre-change-baseline use
- Issues: 0 blockers / 3 warnings / 69 info
- Coverage: 11/11 packages; 64/64 deliverables; 64/64 contexts (all
  provenance on revision 1.4)
- Lifecycle: 26 `INITIALIZED`; 32 `OPEN`; 4 `CHECKING`; 2 `IN_PROGRESS`
- Contracts: 32 valid `SOW_V1`; 32 absent at `OPEN`; 0 ambiguous
- Artifacts: 3/64 anticipated artifact sets found in their deliverable
  folders (`artifact_presence_pct` 4.6875)
- Ledger: 94 rows (`72 IN / 14 OUT / 8 TBD`); all 72 `IN` references resolve
- Objectives: all 6 have active filesystem-backed support. 9 deliverables and
  11 `IN` rows remain unmapped residue
- Strict register validation: 64 registers / 255 rows / 0 findings (exit 0)
- Reliance-hold preflight: `ALLOW` (exit 0)
- Expected source: revision 1.4 `current_basis` (SCA-004 active) plus D-PEC-86
  SCA-005 Gate 1 opened intake (not a checkpoint-1 acceptance)
- Phase: `SCA-005 checkpoint group 1 pre-change baseline`

The three warnings come from Check 6's deliverable-folder-local rule
escalating at `IN_PROGRESS` or later:

- `DEL-01-03` (`IN_PROGRESS`; D-PEC-85 candidate bytes in `projects/pec/v2/`)
- `DEL-01-05` (`IN_PROGRESS`; D-PEC-84 L reversal; bytes in `projects/pec/v2/`)
- the unchanged `DEL-08-02` (`CHECKING`)

Two of the warnings are new since `COV_SCA004_POSTCHANGE_2026-08-03_1442`. The
cause is lifecycle movement, not decomposition drift: the decomposition
package bytes are identical to the SCA-004 postimage.

The 69 informational findings comprise:

- 58 other absent anticipated artifact sets at pre-production states
- 9 accepted unmapped deliverables
- 2 Check-10 notes: stale-conservative pointer metadata-alignment fields, and
  the non-active empty SCA-005 candidate folder

This snapshot is derivative evidence. It does not accept SCA-005 checkpoint 1
or authorize any amendment. The audit `_LATEST.md` pointer is unchanged.
