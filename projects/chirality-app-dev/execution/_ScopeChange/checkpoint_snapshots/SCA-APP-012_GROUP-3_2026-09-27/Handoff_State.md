# Group-3 handoff — SCA-APP-012

**Decision.** Checkpoint group 3 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The acceptance covers the
integrated candidate at `ac67109d9` and the acceptance-conditional list. There
is no group-3 correction.

**Next steps, in order.** WORKING_ITEMS applies
`Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` exactly:
1. this folder, committed first;
2. `Evidence/Group3/group3_finalize.py --date 2026-09-27 --owner-act "I accept SCA-APP-012 checkpoint group 3" --utc {UTC}`,
   which applies E26, `_LATEST.md`, the `Brief.md` status line, the
   `Decision_Log.md` G3 row and `Handoff_State.md`;
3. the `_PostAcceptanceValidation/SCA-APP-012_{UTC}/` record.

The code records are then updated from "awaiting acceptance" to accepted, and
the coordinating session lands the scope text and the code in one PR (#1020).

**Active snapshot after the pointer move.**
`execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/`.
Its `Handoff_State.md` carries the post-acceptance state fields and the
derivative-package table.

**State fields after application.**

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `IN_PROGRESS` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `WARNINGS` |
| `AdjustedAuditState` | `WARNINGS` |
| `ReadyForNextPhase` | `NOT_APPLICABLE` |

**Next owning workflows:**
- `project-setup` in `INCREMENTAL` mode;
- `dependency-extract` for DEL-02-03 and DEL-08-03 (DX-01, DX-02, DX-03,
  DX-05), then `analyze_dep_closure.py`;
- `audit-decomp`, then `audit-scope-closure`;
- the Task Management TM-APP-051 note, by the row owner.

**Still unauthorized:**
- lifecycle transitions;
- dependency-register and Task Management writes in this change;
- any edit not on the acceptance-conditional list;
- release.
