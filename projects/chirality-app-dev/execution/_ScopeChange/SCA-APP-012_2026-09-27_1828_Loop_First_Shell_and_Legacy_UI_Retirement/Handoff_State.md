# SCA-APP-012 — Handoff State (group-3 CANDIDATE)

**State:** `CANDIDATE`. This file is not accepted and is not the active
snapshot. `_LATEST.md` names SCA-APP-011 and stays unchanged until checkpoint
group 3 is accepted.

## Candidate and pointer posture

| Item | Value |
|---|---|
| `CANDIDATE_SNAPSHOT` | `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/` (the only candidate path for this attempt) |
| Pointer posture | `ACCEPTED_PREDECESSOR` |
| `ACCEPTED_PREDECESSOR_SNAPSHOT` | `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/` (`_LATEST.md` SHA-256 `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`, verified unchanged) |
| `ACCEPTED_GROUP2_DECISION_SNAPSHOT` | `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`, pointer `SCA-APP-012_GROUP-2_AUTHORIZED.md`. Verified to bind the exact amendment, the register, `Propagation_Plan.md`, `Supersession_Delta.csv`, the prior SCA-APP-011 map and the group-2 tooling by hash |
| Expected pre-acceptance pointer state | `_LATEST.md` → SCA-APP-011 (unchanged) |
| Artifact completeness | Present: `Brief.md`, `Intake_Actions.csv`, `Impact_Assessment.md`, `Pre_Change_Coverage.json`, `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`, `Supersession_Delta.csv`, `Supersession_Map.csv`, `Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`, `RUN_SUMMARY.md`, `Evidence/`. Not applicable to SOFTWARE: `Domain_Integrity_*`, `KTY_Remediation_Manifest.csv` |

## Candidate revision

The scope-text candidate: 79 of the 80 accepted edits, written by
`Evidence/Group2/build_amendment_preview.py --candidate` with every `GIT_*`
variable removed from the environment. E26 is withheld until acceptance and is
applied, with the other acceptance-conditional items, by
`Evidence/Group3/group3_finalize.py`. There is no group-3 correction and no
basis refresh of an edited file.

The code change of `Propagation_Plan.md` §4 is prepared separately and is
integrated for the joint group-3 review (Q-a). Until then the candidate is the
scope text alone.

## Authoritative truth changed by the candidate

The candidate writes the accepted scope text: 79 of 80 edits in 12 files.
- The decomposition, PRD, SPEC and PLAN.
- Eight Scopes of Work: DEL-02-01, DEL-02-02, DEL-02-03, DEL-06-03,
  DEL-07-02, DEL-07-03, DEL-08-02 and DEL-08-03.

E26 is withheld. The scope-text candidate changes no code, `_CONTEXT.md`,
`_STATUS.md`, `Dependencies.csv`, companion register or Task Management
register.

## Authoritative action register

`Amendment_Actions.csv`, SHA-256
`a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad`, as
accepted in `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`. It has
24 rows. `Intake_Actions.csv` is group-1 evidence only.

## State fields

| Field | Value | Why |
|---|---|---|
| `DecompositionTruthState` | `INCOMPLETE` | Candidate written; E26 waits for acceptance |
| `DerivativePackageState` | `INCOMPLETE` | Dependency registers, audits and the export not yet rerun (below) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY content |
| `DownstreamRerunState` | `FROZEN` | Downstream reruns start after group-3 acceptance |
| `MetadataAlignmentState` | `NOT_REQUIRED` | SOFTWARE variant |
| `AuditState` | `WARNINGS` | Raw deterministic post-change findings, all carried unchanged from the pre-change baseline (`RUN_SUMMARY.md` §4) |
| `AdjustedAuditState` | `WARNINGS` | The same carried findings; no new finding; expected consequences listed in `RUN_SUMMARY.md` §4 |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | SOFTWARE variant |

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Dependency registers (DEL-02-03 DEP-02-03-009 and DEP-02-03-004; DEL-08-03 DEP-08-03-007) | `dependency-extract` | STALE | `Propagation_Plan.md` §8 item 2 (DX-01, DX-02, DX-03, DX-05) | Re-extract after acceptance, then `analyze_dep_closure.py` |
| Code change (`Propagation_Plan.md` §4) | App loop, on a separate branch | IN PREPARATION; integrated for the joint review (Q-a) | `RUN_SUMMARY.md` §6 | Integrate, then the independent review of scope text and code together |
| Task Management TM-APP-051 | Row owner | NOTE PENDING | `Propagation_Plan.md` §8 item 5 | Record the disposition note after acceptance |

## Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | Candidate baseline in `Post_Change_Coverage.json`; full `audit-decomp` after acceptance | `Evidence/Group3/PRE_POST_COMPARISON.md` |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | After incremental setup and the code change | — |
| `_Evaluation/DepClosure` | STALE_REBUILD_REQUIRED | After dependency re-extraction | — |
| `exports/chirality-app` | STALE_REBUILD_REQUIRED | Regenerated with the integrated code change | export tooling |
| Companion register | NO_CHANGE (E) | Unchanged, SHA-256 `918e475a…a944` | `Post_Change_Coverage.json` |

## Remaining blockers and human decisions

- **Code integration and joint review.** The code change of §4 is integrated
  and the independent review covers scope text and code together (Q-a).
- **Checkpoint group 3.** The owner accepts, amends or returns this candidate
  together with the code candidate.
- **No reopening.** All eight written deliverables are `IN_PROGRESS`. No
  `ISSUED` deliverable is reopened, and no `CHECKING` deliverable is held.

## Closure verdict

`OPEN_PENDING_DERIVATIVE_CLOSURE`

## Next owning workflows

1. **Group 3.** The owner's act, after the joint independent review. After
   acceptance, apply the acceptance-conditional edits exactly
   (`Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`) and write the
   `_PostAcceptanceValidation/` record.
2. **`project-setup` in `INCREMENTAL` mode**, for the 24 register rows. It
   scaffolds nothing, and the contracts are already written under T-a.
3. **`dependency-extract`**, then `analyze_dep_closure.py`.
4. **`audit-decomp`**, then `audit-scope-closure`, as the post-acceptance
   closure check.
