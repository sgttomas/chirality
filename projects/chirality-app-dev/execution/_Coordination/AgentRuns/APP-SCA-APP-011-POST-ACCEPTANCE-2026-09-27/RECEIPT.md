# Receipt — APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27

This is a derivative account of the SCA-APP-011 post-acceptance follow-ups.
Authority stays with SCA-APP-011 and the sources below.

**Status: the audits have run. Setup waits on three owner decisions, and
APP-R058 waits on its owner.**
- **Run and written:**
  - `audit-decomp`;
  - `audit-scope-closure`, with its per-amendment `_LATEST.md` row;
  - a pre-extraction `analyze_dep_closure` reconfirmation;
  - the MEMORY rows.
- **Not run:**
  - `project-setup` INCREMENTAL. Its baseline and plan gates need the owner.
  - `dependency-extract` and the post-extraction closure audit. These run
    straight through inside setup Phase 5.6, after the plan is confirmed.
- **Not recorded:** the APP-R058 disposition, which is held for the row's
  owner.

## Authority and basis

- **Acceptance.** The owner accepted SCA-APP-011 checkpoint group 3 on
  2026-09-27 ("I accept SCA-APP-011 checkpoint group 3";
  `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`).
  It landed on `main` in PR #995 (`78e74f590`).
- **Handoffs run.** These are the ones the amendment names:
  - `Propagation_Plan.md` §7–§8;
  - `Handoff_State.md`, next owning workflows;
  - `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv`, all six applied before
    the merge.
- **Brief.** The coordinating session asked for the handoffs to be run by each
  workflow's own method. It said to stop before any write that needs a human
  checkpoint, changes scope, or changes lifecycle state.
- **Workflows loaded.** All are bundled, from `workflows/`:
  - `project-setup` (WORKFLOW.md; `resources/method.md` Function 5;
    `resources/contract.md` INCREMENTAL treatment);
  - `dependency-extract` (WORKFLOW.md);
  - `audit-decomp` (WORKFLOW.md; `resources/contract.md`;
    `resources/method.md`);
  - `audit-scope-closure` (WORKFLOW.md; `resources/contract.md`;
    `resources/method.md`);
  - `audit-dep-closure` (WORKFLOW.md).
- **Base.** `origin/main` `78e74f590`. This revision follows independent review
  of `54d96f2a6`.

## Result, per handoff

| Handoff | Result | Evidence |
|---|---|---|
| `project-setup` INCREMENTAL | **Held at its gates.** Phase 5.0 (the adoption baseline; there is no `SETUP_LOG.md`) and Phase 5.1 (the incremental plan) each need human confirmation before any write. Proposed baseline: SCA-APP-010, accepted up to 2026-09-07 with its DEL-02-05 carrier addendum. Proposed plan: 0 to scaffold, 0 retired, 9 modified (all `SOW_V1` `IN_PROGRESS`, VERIFY only) and 16 neighbours with ACTIVE edges, under FULL_GRAPH. There is no accepted project DAG | `INCREMENTAL_SETUP_PROPOSAL.md` |
| `dependency-extract` | **Not run; no owner approval of values is needed.** The workflow runs straight through and derives rows from the source text. Here it runs as setup Phase 5.6, after the plan is confirmed. The file lists expected outcomes (DX-01 to DX-16) for the post-extraction audit to check. Retiring DEP-02-01-007 was already accepted at groups 1 and 2. The only open dependency question is HGD-2 for DEP-02-01-008 | `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`, `.csv` |
| `analyze_dep_closure` | **Run on the unchanged registers**, as a pre-extraction reconfirmation: 54 nodes, 111 edges, 0 SCC, 0 orphans, `subject_status` FAIL. The same 2 schema-invalid registers and 2 implements-missing units carry over from the accepted baseline | `dep_closure/` |
| `audit-decomp` | **Run.** WARNINGS; 0 blockers; 57 warnings. Topology 10/52/84/10 is unchanged. Context: 51 MATCH, 1 PARTIAL (the retired DEL-09-07, as before). The Scope of Work validator passes 54/54. The QA report discloses the report layout change and confirms the generator reproduces the committed report. The DecompCoverage `_LATEST.md` is not moved | `execution/_Evaluation/DecompCoverage/COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500/` |
| `audit-scope-closure` | **Run before setup.** OPEN: 0 critical, 16 major, 5 minor, 1 observation. All 29 register actions are VERIFIED, and supersession checks 15/15. Method Pass 3 finds 0 orphaned references, because no ID is retired. A disclosed retired-surface screen files 11 stale rows as `METADATA_STALE` and 1 observation (DEP-02-03-009). Snapshot regenerated in place after review. A per-amendment row is added to `_LATEST.md` (method step 5) | `execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_0505/` |
| MEMORY rows | **Appended** one dated row to each of the nine deliverables whose SCA-APP-011 code-change row said "checkpoint-group-3 candidate … after group-3 acceptance". Each links the change's receipt and this receipt. The row sits directly after the row it follows up, because the MEMORY files mix oldest-first and newest-first order. Older rows are unchanged | the nine `MEMORY.md` files |
| APP-R058 | **Held for the row's owner.** The row is in the closed finite retirement account. The DEL-07-02 SOW already records "Closed by SCA-APP-011". The hold is moot for the App but not released: the Runtime `ProjectScaffoldPort` composition is still absent | `APP_R058_PROPOSAL.md` |

## For the owner: three decisions and APP-R058

1. **Setup Phase 5.0, baseline.** Adopt incremental setup with baseline
   SCA-APP-010 (accepted up to 2026-09-07, including its DEL-02-05 carrier
   addendum).
   - This covers 10 earlier accepted amendments.
   - SCA-APP-011 stays in the queue.
2. **Setup Phase 5.1, plan.** Confirm the plan: 0 to scaffold, 0 retired,
   9 modified and 16 neighbours under FULL_GRAPH.
   - `dependency-extract` then runs straight through. The rerun audit checks
     DX-01 to DX-16.
3. **HGD-2, for DEP-02-01-008 only.**
   - (a) Retire it. The reviewer recommends this: the `/pipeline` query
     handler is dead legacy shell code, and route/query compatibility is keyed
     with DEL-08-02.
   - (b) Keep it as compatibility-only, if the `/pipeline` deep link should
     be tracked as a DEL-02-01 obligation.
   - Once DEP-02-02-005 and DEP-02-01-007 retire, the four-node cycle concern
     behind HGD-3 no longer applies.
4. **APP-R058 (the row's owner).**
   - Option 1, recommended: append a closure echo beside the finite account.
     It needs the federation preflight and a verbatim transcription of your
     act.
   - Option 2: record nothing. ASC-ISS-010 (MINOR) then stays, so closure can
     reach at best `CLOSED_WITH_OBSERVATIONS`.

**Proposed reply:**

> Confirm baseline SCA-APP-010 (accepted up to 2026-09-07) and the SCA-APP-011
> incremental plan under FULL_GRAPH; HGD-2: retire DEP-02-01-008; APP-R058:
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
  `SETUP_LOG.md`, `_COORDINATION.md`, `_STATUS.md`, scope file or Task
  Management record was written. The only pointer written is the
  ScopeClosureAudit per-amendment row.
- **Artifact screen.** The audit-decomp artifact screen (Check 6) is a
  path/filename heuristic. Its 18/194 is not comparable with the prior run's
  11/194.
- **Pre-setup audit.** The scope-closure snapshot is the pre-setup state. It is
  superseded by a rerun after setup (Phase 5.7) and extraction.
- **No release.** There is no lifecycle change and no release.
