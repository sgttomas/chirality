# Group-3 handoff — SCA-APP-011

**Decision.** Checkpoint group 3 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The acceptance covers the
integrated candidate at `d48c785c5`, corrections G3C-01 and G3B-01, and the
acceptance-conditional list.

**Next steps, in order.** WORKING_ITEMS applies
`Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` exactly:
1. this folder;
2. E47;
3. `_LATEST.md`;
4. the Runtime notice;
5. the status records;
6. the `_PostAcceptanceValidation/` record.

The coordinating session then lands the scope text and the code in one PR
(#995).

**Active snapshot after the pointer move.**
`execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`.
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
- `dependency-extract`, then `analyze_dep_closure.py`;
- `audit-decomp`, then `audit-scope-closure`.

**Still unauthorized:**
- lifecycle transitions;
- dependency-register writes in this change;
- any edit not on the acceptance-conditional list;
- release.
