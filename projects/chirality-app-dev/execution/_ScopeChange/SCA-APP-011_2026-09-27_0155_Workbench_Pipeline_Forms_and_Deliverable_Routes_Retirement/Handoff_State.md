# SCA-APP-011 — Handoff State (group-3 CANDIDATE)

**State:** `CANDIDATE`. This file is not accepted and is not the active
snapshot. `_LATEST.md` names SCA-APP-010 and stays unchanged until checkpoint
group 3 is accepted.

## Candidate and pointer posture

| Item | Value |
|---|---|
| `CANDIDATE_SNAPSHOT` | `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/` (the only candidate path for this attempt) |
| Pointer posture | `ACCEPTED_PREDECESSOR` |
| `ACCEPTED_PREDECESSOR_SNAPSHOT` | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/` (`_LATEST.md` SHA-256 `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3`, verified unchanged) |
| `ACCEPTED_GROUP2_DECISION_SNAPSHOT` | `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`, pointer `SCA-APP-011_GROUP-2_AUTHORIZED.md`. Verified to bind the exact amendment, the register, `Propagation_Plan.md`, `Supersession_Delta.csv` and the prior SCA-APP-010 map by hash |
| Expected pre-acceptance pointer state | `_LATEST.md` → SCA-APP-010 (unchanged) |
| Artifact completeness | Present: `Brief.md`, `Intake_Actions.csv`, `Impact_Assessment.md`, `Pre_Change_Coverage.json`, `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`, `Supersession_Delta.csv`, `Supersession_Map.csv`, `Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`, `RUN_SUMMARY.md`, `Evidence/`. Not applicable to SOFTWARE: `Domain_Integrity_*`, `KTY_Remediation_Manifest.csv` |

## Authoritative truth changed by the candidate

The candidate writes the accepted scope text: 126 of 127 edits in 16 files.
- The decomposition, PRD, SPEC and PLAN.
- Nine Scopes of Work: DEL-02-02, DEL-02-03, DEL-03-03, DEL-07-01, DEL-07-02,
  DEL-07-04, DEL-07-05, DEL-08-03 and DEL-09-03.
- Three `_CONTEXT.md` files: DEL-02-02, DEL-07-04 and DEL-08-03.

E47 is withheld until acceptance. No `_STATUS.md`, `Dependencies.csv`,
companion register or code is changed.

## Authoritative action register

`Amendment_Actions.csv`, SHA-256
`416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22`, as
accepted in `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`. It has
29 rows, and row 29 (DEL-07-01) is a reopened group-1 item decided at group 2.
`Intake_Actions.csv` is group-1 evidence only.

## State fields

| Field | Value | Why |
|---|---|---|
| `DecompositionTruthState` | `INCOMPLETE` | Candidate written; E47 waits for acceptance |
| `DerivativePackageState` | `INCOMPLETE` | Dependency registers, audits and exports not yet rerun (below) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY content |
| `DownstreamRerunState` | `FROZEN` | Downstream reruns start after group-3 acceptance |
| `MetadataAlignmentState` | `NOT_REQUIRED` | SOFTWARE variant |
| `AuditState` | `WARNINGS` | Raw deterministic post-change findings, all carried unchanged from the pre-change baseline (`RUN_SUMMARY.md` §4). The independent review is still to run (Q-a) |
| `AdjustedAuditState` | `WARNINGS` | The same carried findings; no new finding; expected consequences listed in `RUN_SUMMARY.md` §4 |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | SOFTWARE variant |

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Dependency registers (DEL-02-02 DEP-02-02-005..009; DEL-07-05 DEP-07-05-025; DEL-02-01, DEL-02-03, DEL-07-04, DEL-08-02, DEL-08-03 wording) | `dependency-extract` | STALE | `Propagation_Plan.md` §7–8 | Re-extract after acceptance, then `analyze_dep_closure.py` |
| Code change (forms, routes, client module, scaffold route and port member, test split) | App loop, per `Propagation_Plan.md` §4 | IN PREPARATION (separate branch) | — | Joint group-3 review with this candidate (Q-a) |
| `RouteAdapterTestIndex.md` (DEL-03-03, lines 24 and 46) | App loop code change | STALE | `Propagation_Plan.md` §4 | Drop or mark the scaffold rows in the code change |
| `dcd37f9ae` records (run receipt, Receipt-269, APP-TRANSITION-FORMS note, MEMORY rows) | App loop code change | STALE | `Propagation_Plan.md` §4 Records | Correct in the rebased code candidate |
| Task Management APP-R058 | Row owner | OPEN | `Propagation_Plan.md` §8 item 6 | Record "closed by removal under SCA-APP-011" |
| Runtime notice | WORKING_ITEMS after acceptance | DRAFT | `DRAFT_NOTICE_TO_RUNTIME.md` | Send after acceptance (acceptance-conditional item 4) |

## Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | Candidate baseline in `Post_Change_Coverage.json`; full `audit-decomp` after acceptance | `Evidence/Group3/PRE_POST_COMPARISON.md` |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | After incremental setup and the code change | — |
| `_Reconciliation/DepClosure` | STALE_REBUILD_REQUIRED | After dependency re-extraction | — |
| `exports/chirality-app` | STALE_REBUILD_REQUIRED | Regenerated with the code change | — |
| Companion register | NO_CHANGE (E) | Unchanged, SHA-256 `918e475a…a944` | `Post_Change_Coverage.json` |

## Remaining blockers and human decisions

- **Checkpoint group 3.** The owner accepts or returns this candidate together
  with the code candidate (Q-a), after the independent review.
- **No reopening.** All nine written deliverables are
  `IN_PROGRESS`. No `ISSUED` deliverable is reopened, and no `CHECKING`
  deliverable is held.

## Closure verdict

`OPEN_PENDING_DERIVATIVE_CLOSURE`

## Next owning workflows

1. **Group 3.** The independent review (not the author), then the owner's act.
   After acceptance, apply the acceptance-conditional edits exactly
   (`Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`) and write the
   `_PostAcceptanceValidation/` record.
2. **`project-setup` in `INCREMENTAL` mode**, for the 29 MODIFY/ADD rows. It
   scaffolds nothing, and the contracts are already written under W-a.
3. **`dependency-extract`**, then `analyze_dep_closure.py`.
4. **`audit-decomp`**, then `audit-scope-closure`, as the post-acceptance
   closure check.
