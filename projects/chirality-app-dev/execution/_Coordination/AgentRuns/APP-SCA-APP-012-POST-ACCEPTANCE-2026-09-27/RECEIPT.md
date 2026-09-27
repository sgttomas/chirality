# Receipt — APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27

This is a derivative account of the SCA-APP-012 post-acceptance follow-ups.
Authority stays with SCA-APP-012 and the sources below.

**Status: the post-change `audit-decomp` baseline has run. Setup waits on one
owner confirmation, and the TM-APP-051 note waits on the row's owner.**
- **Run and written:**
  - `audit-decomp` (post-change baseline);
  - a pre-extraction `analyze_dep_closure` reconfirmation and a read-only
    quote screen of the 24 in-scope registers;
  - the dependency expected-outcome file (DX-01 to DX-07);
  - MEMORY rows for the four modified deliverables that had none.
- **Not run:**
  - `project-setup` INCREMENTAL. Its Phase 5.1 plan gate needs the owner.
  - `dependency-extract` and `audit-dep-closure`. These run straight through
    inside setup Phase 5.6, after the plan is confirmed.
  - `audit-scope-closure`. `Propagation_Plan.md` §8 item 3 and
    `Handoff_State.md` place it after the setup; it is not run before.
- **Not recorded:** the TM-APP-051 disposition note, held for the row's owner.

## Authority and basis

- **Acceptance.** The owner accepted SCA-APP-012 checkpoint group 3 on
  2026-09-27 ("I accept SCA-APP-012 checkpoint group 3";
  `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/`).
  It landed on `main` in PR #1020 (`bc1ea504d`).
- **Handoffs addressed (run or prepared).** These are the ones the amendment names:
  - `Propagation_Plan.md` §7, §8 (items 1, 2, 3 and 5; items 4, 6 and 7 were
    done in PR #1020) and §11;
  - `Handoff_State.md`, next owning workflows.
- **Brief.** The coordinating session asked for stage 1: run `audit-decomp`,
  prepare the incremental setup plan without executing it, draft the
  TM-APP-051 note and the MEMORY rows, and stop at the owner gate. Nothing is
  pushed or merged by this run.
- **Precedent.** The SCA-APP-011 follow-ups (PR #1009, first commit
  `54d96f2a6` as revised by `0ca5ffcca`), mirrored in structure and names.
- **Workflows loaded.** All are bundled, from `workflows/`, unchanged since
  the SCA-APP-011 run:
  - `project-setup` (WORKFLOW.md; `resources/method.md` Function 5;
    `resources/contract.md` INCREMENTAL inputs and treatment);
  - `dependency-extract` (WORKFLOW.md);
  - `audit-decomp` (WORKFLOW.md; `resources/contract.md`;
    `resources/method.md`), run through the SCA-APP-011 run script with its
    SCA-specific constants updated;
  - `audit-dep-closure` (WORKFLOW.md).
- **Base.** `origin/main` `bc1ea504d`.

## Result, per handoff

| Handoff | Result | Evidence |
|---|---|---|
| `project-setup` INCREMENTAL | **Held at its plan gate.** Phase 5.0 is not needed: `SETUP_LOG.md` already has its `BASELINE`, and SCA-APP-011 is `COMPLETE`, so SCA-APP-012 alone is queued. Phase 5.1 needs the owner. Proposed plan: 0 to scaffold, 0 retired, 8 modified (all `SOW_V1` `IN_PROGRESS`, VERIFY only under T-a) and 16 neighbours with ACTIVE edges, under FULL_GRAPH. There is no accepted project DAG | `INCREMENTAL_SETUP_PROPOSAL.md` |
| `dependency-extract` | **Not run; no owner ruling needed.** It runs straight through as setup Phase 5.6 over 24 registers (the workflow's set; `Propagation_Plan.md` §8 item 2 names only the two where changes are expected). The file lists DX-01 to DX-05 from the plan and two more the quote screen found: DX-06 (DEP-02-03-007 re-evidenced to the restated REQ-010) and DX-07 (DEP-02-03-008 retired, since the CLM-005 widget row now says dependency snapshots moved out of this UI) | `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`, `.csv` |
| `analyze_dep_closure` | **Run on the unchanged registers** as a pre-extraction reconfirmation: 54 nodes, 104 edges, 0 SCC, 0 orphans, 7 isolates, `subject_status` FAIL from the 2 CONTROL units without registers and 2 implements-missing units. The counts equal the accepted census `CLOSURE_HGD_FC_RULING_2026-09-27_1923/Evidence/ALL/`. Expected after extraction: 102 edges, 0 SCC | `dep_closure/` |
| `audit-decomp` | **Run.** WARNINGS; 0 blockers; 57 warnings. Topology 10/52/84/10 is unchanged. Context: 51 MATCH, 1 PARTIAL (retired DEL-09-07, as before). The Scope of Work validator passes 54/54. The issue log and matrix are identical, row for row, to the SCA-APP-011 run: SCA-APP-012 adds no finding. Decomposition and `_LATEST.md` hashes equal the post-acceptance validation record. Closure readiness is FAIL while the snapshot stays `OPEN_PENDING_DERIVATIVE_CLOSURE`. The DecompCoverage `_LATEST.md` is not moved | `execution/_Evaluation/DecompCoverage/COV_SCA_APP_012_POST_ACCEPTANCE_2026-09-27_2200/` |
| `audit-scope-closure` | **Not run before setup**, as `Propagation_Plan.md` §8 item 3 orders (the SCA-APP-011 run also took a pre-setup `OPEN` snapshot; here the group-3 post-acceptance validation already verified the accepted poststate) | — |
| MEMORY rows | PR #1020 gave DEL-02-01, DEL-02-02, DEL-02-03 and DEL-08-02 an SCA-APP-012 row that records the group-3 acceptance; they get nothing now. DEL-06-03, DEL-07-02, DEL-07-03 and DEL-08-03 had none: each gets one dated row for the accepted scope text, in its `## Runs` structure. All eight get their setup row at closeout (`Propagation_Plan.md` §7) | the four `MEMORY.md` files |
| TM-APP-051 | **Held for the row's owner.** A read-only federation preflight is `COMPLETE` with no finding on the row. Recommended: row maintenance appending the §8 item 5 note, the row kept `DEFERRED` | `TM_APP_051_PROPOSAL.md` |

## For the owner: one confirmation and TM-APP-051

1. **Setup Phase 5.1, plan.** Confirm the SCA-APP-012 incremental plan under
   FULL_GRAPH: 0 to scaffold, 0 retired, 8 modified (VERIFY only), 16
   neighbours. `dependency-extract` then runs straight through over the 24
   registers, and the post-setup audit checks DX-01 to DX-07.
   - Knowingly included: DX-07 retires DEP-02-03-008, an edge the accepted
     plan did not list, because the accepted DEL-02-03 text no longer states
     it.
   - Alternative, not recommended: limit extraction to DEL-02-03 and
     DEL-08-03 as §8 item 2 names them. That departs from Phase 5.6 FULL_GRAPH.
   - Semantic lensing of the eight modified deliverables stays stale unless
     you select a rerun.
2. **TM-APP-051 (the row's owner).**
   - Option 1, recommended: row maintenance that appends the note, sets
     `ScaRef` to SCA-APP-012 and keeps the row `DEFERRED` for the summary
     widget.
   - Option 2: record nothing now; the audit then carries the note open.

**Proposed reply:**

> Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; TM-APP-051:
> option 1.

## Checks

These ran against `origin/main` on the committed change:
- this ledger's validator;
- Root G0–G4;
- the conflict-marker and run-record-leak checks;
- `build_workflow_index.py --check` and `git diff --check`;
- export freshness.

The results are in the hand-off and the loop receipts.

## Limits

- **Nothing held was written.** No `Dependencies.csv`, `_DEPENDENCIES.md`,
  `SETUP_LOG.md`, `_COORDINATION.md`, `_STATUS.md`, scope file, Task
  Management record or pointer was written.
- **Screens are heuristics.** The quote screen and the DX-05 screen read
  register fields and cited sources as text; the extraction's own reading
  governs. The audit-decomp artifact screen (Check 6) is a path/filename
  heuristic.
- **No release.** There is no lifecycle change and no release.
