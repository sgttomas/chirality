# Receipt — APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27

Derivative account of the SCA-APP-011 post-acceptance follow-ups. SCA-APP-011
and the sources below keep their authority.

**Status: audits run; setup and dependency writes held for the owner.**
- Run and written: `audit-decomp`, `audit-scope-closure`, a pre-extraction
  `analyze_dep_closure` reconfirmation, and the MEMORY rows.
- Held and prepared as proposals, with nothing applied:
  - `project-setup` INCREMENTAL;
  - `dependency-extract` and the post-extraction closure audit;
  - the APP-R058 disposition.

## Authority and basis

- **SCA-APP-011 accepted.** The owner accepted checkpoint group 3 on
  2026-09-27 ("I accept SCA-APP-011 checkpoint group 3";
  `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`).
  It landed on `main` in PR #995 (`78e74f590`).
- **Handoffs run.** These are the ones the amendment names:
  - `Propagation_Plan.md` §7–§8;
  - `Handoff_State.md` next owning workflows;
  - `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` (all six items applied
    before merge).
- **Brief.** The coordinating session's brief: run the handoffs, follow each
  workflow's method, and stop before any write that needs a human checkpoint,
  changes scope or changes lifecycle state.
- **Workflows loaded.** All are bundled, from `workflows/`:
  - `project-setup` (WORKFLOW.md; `resources/method.md` Function 5;
    `resources/contract.md` INCREMENTAL treatment);
  - `dependency-extract` (WORKFLOW.md);
  - `audit-decomp` (WORKFLOW.md; `resources/contract.md`; `resources/method.md`);
  - `audit-scope-closure` (WORKFLOW.md; `resources/contract.md`;
    `resources/method.md`);
  - `audit-dep-closure` (WORKFLOW.md).
- **Base.** `origin/main` `78e74f590`.

## Result, per handoff

| Handoff | Result | Evidence |
|---|---|---|
| `project-setup` INCREMENTAL | **Held for the owner.** Phase 5.0 (adoption baseline; there is no `SETUP_LOG.md` yet) and Phase 5.1 (incremental plan) need human confirmation before any write. The proposal: baseline SCA-APP-010; plan with 0 scaffold, 0 retired, 9 modified (all `SOW_V1` `IN_PROGRESS`, VERIFY only) and 17 neighbours under FULL_GRAPH; no accepted project DAG | `INCREMENTAL_SETUP_PROPOSAL.md` |
| `dependency-extract` | **Held for the owner.** It runs as Phase 5.6 after the plan is confirmed. HGD-2 (DEP-02-01-007/008) is an open owner decision, and earlier App edge changes ran under owner rulings (D-APP-109, D-APP-110). The proposal has 14 exact field changes over 11 ACTIVE stale rows | `DEPENDENCY_EXTRACT_PROPOSAL.md`, `DEPENDENCY_EXTRACT_PROPOSAL.csv` |
| `analyze_dep_closure` | **Run on the unchanged registers** as a pre-extraction reconfirmation: 54 nodes, 111 edges, 0 SCC, 0 orphans, `subject_status` FAIL. The same 2 schema-invalid registers and 2 implements-missing units carry over from the accepted baseline. The post-extraction `audit-dep-closure` stays held with extraction | `dep_closure/` |
| `audit-decomp` | **Run.** WARNINGS; 0 blockers; 57 warnings. Topology 10/52/84/10 is unchanged. Context 51 MATCH, 1 PARTIAL (the retired DEL-09-07, as before). The Scope of Work validator passes 54/54. Closure readiness is FAIL while the snapshot stays `OPEN_PENDING_DERIVATIVE_CLOSURE`. The DecompCoverage `_LATEST.md` is not moved | `execution/_Evaluation/DecompCoverage/COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500/` |
| `audit-scope-closure` | **Run before setup.** Verdict OPEN: 0 critical, 16 major, 5 minor. All 29 register actions are VERIFIED, and the supersession bindings are 15/15 with 0 accumulator findings. Open items: setup and dependency re-extraction not run (8 major); 11 stale dependency rows (8 major, 3 minor); post-extraction closure and APP-R058 (minor). The ScopeClosureAudit `_LATEST.md` is not moved | `execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_0505/` |
| MEMORY rows | **Appended** one dated row to each of the nine deliverables whose SCA-APP-011 code-change row said "checkpoint-group-3 candidate … after group-3 acceptance". Each new row sits directly after that row, and the older rows are unchanged | the nine `MEMORY.md` files |
| APP-R058 | **Held for the row's owner.** The row is in the owner-decided finite retirement account. The DEL-07-02 SOW already records "Closed by SCA-APP-011" | `APP_R058_PROPOSAL.md` |

## Owner decisions prepared

One reply covers all three:

> Adopt incremental setup with baseline SCA-APP-010; confirm the SCA-APP-011
> incremental plan under FULL_GRAPH; apply DX-01 to DX-06 and DX-08 to DX-14;
> HGD-2: retire DEP-02-01-007 and [retire | keep compatibility-only]
> DEP-02-01-008; APP-R058: option 1.

## Checks

The following were run against `origin/main` on the committed change:
- this ledger's validator;
- Root G0–G4;
- the conflict-marker and run-record-leak checks;
- `build_workflow_index.py --check` and `git diff --check`;
- export regeneration.

The results are in the hand-off and in Receipt-272.

## Limits

- **Nothing held was written.** No `Dependencies.csv`, `_DEPENDENCIES.md`,
  `SETUP_LOG.md`, `_COORDINATION.md`, `_STATUS.md`, scope file, Task
  Management record or pointer was written.
- **Artifact screen.** The audit-decomp artifact screen (Check 6) is a
  path/filename heuristic. Its 18/194 is not comparable with the prior run's
  11/194.
- **Pre-setup audit.** The scope-closure audit is the pre-setup state. Rerun
  it after incremental setup (Phase 5.7).
- **No release.** There is no lifecycle change and no release.
