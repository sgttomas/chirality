# Phase 5.7 scan and report (Phase 3.1/3.2)

Read-only. `tools/query/count_workspace_state.sh` output:

```
=== Project State Summary ===
Execution Root: projects/chirality-app-dev/execution
Date: 2026-09-27

Packages: 11
Deliverables: 54

| State | Count |
|-------|-------|
| OPEN | 1 |
| INITIALIZED | 0 |
| SEMANTIC_READY | 0 |
| IN_PROGRESS | 53 |
| CHECKING | 0 |
| ISSUED | 0 |

Tool Roots:
  [ ] _Aggregation
  [x] _Coordination
  [x] _Decomposition
  [ ] _Estimates
  [ ] _EstimatePrep
  [x] _Reconciliation
  [ ] _Schedule
  [x] _Sources
  [ ] _Change
```

## By lifecycle state

- OPEN: 1 (DEL-09-07)
- INITIALIZED: 0
- SEMANTIC_READY: 0
- IN_PROGRESS: 53
- CHECKING: 0
- ISSUED: 0

`2_Checking/` items: 1; `3_Issued/` items: 1.

## Dependencies (advisory; FULL_GRAPH; no accepted project DAG)

Computed from the recorded register after the closure audit (`_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234`, 0 SCC).
An upstream edge is met when its `SatisfactionStatus` is SATISFIED, WAIVED or NOT_APPLICABLE, or the upstream deliverable's lifecycle state is at least the row's `RequiredMaturity` (SEMANTIC_READY when TBD).
Retired DEL-09-07 is listed separately and excluded.

- UNBLOCKED: 53
- BLOCKED: 0
- HELD (unresolved cycles): none (0 SCC).
- DAG PENDING: not applicable (no accepted project DAG).
- Retired: DEL-09-07 (lifecycle `OPEN`, unchanged).

WORKING_ITEMS does not assign or recommend priorities.
