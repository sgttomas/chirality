# SCA-APP-012 — Handoff State (ACCEPTED)

**State:** `ACCEPTED`. The owner accepted checkpoint group 3 on
{APPLICATION_DATE} ("{OWNER_ACT_VERBATIM}";
`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`).
This folder is the active snapshot, and `_LATEST.md` names it.

## Snapshot and pointer

| Item | Value |
|---|---|
| Active snapshot | `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/` |
| Pointer | `_LATEST.md` → SCA-APP-012 (from `Evidence/Group3/LATEST_POSTIMAGE.md`) |
| Accepted predecessor | `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/` (historical) |
| Decision records | Group 1 `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`; group 2 `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`; group 3 `checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/` |
| Post-acceptance validation | `execution/_ScopeChange/_PostAcceptanceValidation/SCA-APP-012_{UTC}/` |

## Authoritative truth changed

The accepted scope text: 80 edits in 12 files, including E26, applied on
acceptance by `Evidence/Group3/group3_finalize.py`.
- The decomposition, PRD, SPEC and PLAN.
- Eight Scopes of Work: DEL-02-01, DEL-02-02, DEL-02-03, DEL-06-03,
  DEL-07-02, DEL-07-03, DEL-08-02 and DEL-08-03.

The code change of `Propagation_Plan.md` §4 lands in the same PR (Q-a). No
`_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`, companion register or Task
Management register is changed.

## Authoritative action register

`Amendment_Actions.csv`, SHA-256
`a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad`, as
accepted in `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`. It has
24 rows. `Intake_Actions.csv` is group-1 evidence only.

## State fields

| Field | Value | Why |
|---|---|---|
| `DecompositionTruthState` | `COMPLETE` | All accepted decomposition edits applied, E26 included |
| `DerivativePackageState` | `INCOMPLETE` | Dependency registers and the full audits are not yet rerun (below) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY content |
| `DownstreamRerunState` | `IN_PROGRESS` | The downstream handoffs below are open |
| `MetadataAlignmentState` | `NOT_REQUIRED` | SOFTWARE variant |
| `AuditState` | `WARNINGS` | The carried pre-existing findings (`RUN_SUMMARY.md` §4); the post-acceptance validation record reruns the registered tools |
| `AdjustedAuditState` | `WARNINGS` | The same carried findings; no new finding |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | SOFTWARE variant |

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Dependency registers (DEL-02-03 DEP-02-03-009 and DEP-02-03-004; DEL-08-03 DEP-08-03-007) | `dependency-extract` | STALE | `Propagation_Plan.md` §8 item 2 (DX-01, DX-02, DX-03, DX-05) | Re-extract, then `analyze_dep_closure.py` |
| Code change | App loop | LANDS WITH THE SCOPE TEXT (Q-a) | `RUN_SUMMARY.md` §6 | None after merge |
| Task Management TM-APP-051 | Row owner | NOTE PENDING | `Propagation_Plan.md` §8 item 5 | Record the disposition note |

## Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | Full `audit-decomp` to run | `Post_Change_Coverage.json` |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | After incremental setup | — |
| `_Evaluation/DepClosure` | STALE_REBUILD_REQUIRED | After dependency re-extraction | — |
| `exports/chirality-app` | REGENERATED | Regenerated with the integrated candidate | export tooling |
| Companion register | NO_CHANGE (E) | Unchanged | `Post_Change_Coverage.json` |

## Remaining blockers and human decisions

- None for this amendment's acceptance. No `ISSUED` deliverable is reopened,
  and no `CHECKING` deliverable is held; all eight written deliverables are
  `IN_PROGRESS`.

## Closure verdict

`OPEN_PENDING_DERIVATIVE_CLOSURE`

## Next owning workflows

1. **`project-setup` in `INCREMENTAL` mode**, for the 24 register rows. It
   scaffolds nothing; the contracts are already written (T-a).
2. **`dependency-extract`**, then `analyze_dep_closure.py`.
3. **`audit-decomp`**, then `audit-scope-closure`, as the post-acceptance
   closure check.
4. **Task Management TM-APP-051**: the disposition note, by the row owner.
