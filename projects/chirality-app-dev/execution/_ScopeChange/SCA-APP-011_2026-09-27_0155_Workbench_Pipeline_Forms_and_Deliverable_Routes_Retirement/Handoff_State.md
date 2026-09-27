# SCA-APP-011 — Handoff State (ACCEPTED)

**State:** `ACCEPTED`. The owner accepted checkpoint group 3 on
2026-09-27 ("I accept SCA-APP-011 checkpoint group 3";
`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`).
This folder is the active snapshot, and `_LATEST.md` names it.

## Snapshot and pointer

| Item | Value |
|---|---|
| Active snapshot | `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/` |
| Pointer | `_LATEST.md` → SCA-APP-011 (from `Evidence/Group3/LATEST_POSTIMAGE.md`) |
| Accepted predecessor | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/` (historical) |
| Decision records | Group 1 `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`; group 2 `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`; group 3 `checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/` |
| Post-acceptance validation | `execution/_ScopeChange/_PostAcceptanceValidation/SCA-APP-011_20260927T044456Z/` |

## Authoritative truth changed

The accepted scope text: 127 edits in 16 files, including E47, applied on
acceptance by `Evidence/Group3/group3_corrections.py --finalize`, with the
group-3 correction G3C-01 and the SPEC basis refresh G3B-01
(`Evidence/Group3/G3_CORRECTIONS.md`).
- The decomposition, PRD, SPEC and PLAN.
- Nine Scopes of Work: DEL-02-02, DEL-02-03, DEL-03-03, DEL-07-01, DEL-07-02,
  DEL-07-04, DEL-07-05, DEL-08-03 and DEL-09-03.
- Three `_CONTEXT.md` files: DEL-02-02, DEL-07-04 and DEL-08-03.

The code change of `Propagation_Plan.md` §4 lands in the same PR (Q-a). No
`_STATUS.md`, `Dependencies.csv` or companion register is changed.

## Authoritative action register

`Amendment_Actions.csv`, SHA-256
`416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22`, as
accepted in `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`. It has
29 rows. `Intake_Actions.csv` is group-1 evidence only.

## State fields

| Field | Value | Why |
|---|---|---|
| `DecompositionTruthState` | `COMPLETE` | All accepted decomposition edits applied, E47 included |
| `DerivativePackageState` | `INCOMPLETE` | Dependency registers and the full audits are not yet rerun (below) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY content |
| `DownstreamRerunState` | `IN_PROGRESS` | The downstream handoffs below are open |
| `MetadataAlignmentState` | `NOT_REQUIRED` | SOFTWARE variant |
| `AuditState` | `WARNINGS` | The carried pre-existing findings F1–F4 (`RUN_SUMMARY.md` §4); the post-acceptance validation record reruns the registered tools |
| `AdjustedAuditState` | `WARNINGS` | The same carried findings; no new finding |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | SOFTWARE variant |

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Dependency registers (DEL-02-02 DEP-02-02-005..009; DEL-07-05 DEP-07-05-025; DEL-02-01, DEL-02-03, DEL-07-04, DEL-08-02, DEL-08-03 wording) | `dependency-extract` | STALE | `Propagation_Plan.md` §7–8 | Re-extract, then `analyze_dep_closure.py` |
| Code change | App loop | LANDS WITH THE SCOPE TEXT (Q-a) | run receipt `APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md` | None after merge |
| Task Management APP-R058 | Row owner | OPEN | `Propagation_Plan.md` §8 item 6 | Record "closed by removal under SCA-APP-011" |
| Runtime notice | WORKING_ITEMS | SENT | `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-27_APP_SCA-APP-011_SCAFFOLD_API.md` | The Runtime loop decides on its scaffold API |

## Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | Full `audit-decomp` to run | `Post_Change_Coverage.json` |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | After incremental setup | — |
| `_Reconciliation/DepClosure` | STALE_REBUILD_REQUIRED | After dependency re-extraction | — |
| `exports/chirality-app` | REGENERATED | Regenerated with the integrated candidate | export tooling |
| Companion register | NO_CHANGE (E) | Unchanged | `Post_Change_Coverage.json` |

## Remaining blockers and human decisions

- None for this amendment's acceptance. No `ISSUED` deliverable is reopened,
  and no `CHECKING` deliverable is held; all nine written deliverables are
  `IN_PROGRESS`.

## Closure verdict

`OPEN_PENDING_DERIVATIVE_CLOSURE`

## Next owning workflows

1. **`project-setup` in `INCREMENTAL` mode**, for the 29 register rows. It
   scaffolds nothing; the contracts are already written (W-a).
2. **`dependency-extract`**, then `analyze_dep_closure.py`.
3. **`audit-decomp`**, then `audit-scope-closure`, as the post-acceptance
   closure check.
