# NEXT INSTANCE STATE

Last updated: 2026-05-24

## Current Pointers

| Item | Path / Value |
| --- | --- |
| Execution root | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/` |
| Project root | `/Users/ryan/ai-env/projects/chirality/` |
| Coordination policy | `_Coordination/_COORDINATION.md` |
| Accepted upstream decomposition truth | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` |
| Decomposition variant | `PROJECT_DECOMP` |
| Active setup phase | Phase 2.2, `TASK + four-documents`, `RUN_PASSES=P1_P2` |

## Current Program State

- Workspace count after Batch 13 closeout: 105 packages, 808 deliverable folders.
- Lifecycle distribution after Batch 13 closeout:
  - `OPEN`: 594
  - `INITIALIZED`: 213
  - `SEMANTIC_READY`: 0
  - `IN_PROGRESS`: 0
  - `CHECKING`: 0
  - `ISSUED`: 0
- Tool roots present: `_Coordination`, `_Decomposition`, `_Sources`.
- Tool roots absent/not yet used: `_Aggregation`, `_Estimates`, `_EstimatePrep`, `_Reconciliation`, `_Schedule`, `_Change`.

## Active Human Rulings And Assumptions

1. Accepted upstream decomposition truth is the Gate 7 final published PROJECT_DECOMP snapshot named above.
2. Raw source corpus is not to be reinterpreted by ORCHESTRATOR; Phase 2.2 workers consume Gate 7 plus deliverable-local references as their basis.
3. Coordination mode is `DECLARED`; blocker computation is advisory and limited to declared dependency edges.
4. Default dependency maturity threshold is `INITIALIZED`.
5. Phase 2.2 uses `TASK + four-documents` with `RUN_PASSES=P1_P2`, `DECOMP_VARIANT=PROJECT`, and deliverable-local write scope.

## Completed Batch 13 Closure

Interrupted Batch 13 was restarted and closed.

Scope:
- `DEL-033-03..06`
- `PKG-034..039`
- Total: 40 deliverables

Closure verdict:
- 40 / 40 are `INITIALIZED`.
- 40 / 40 have `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
- 40 / 40 have successful `TASK + four-documents` `P1_P2` run-record evidence.
- No Batch 13 worker remains open.

Evidence notes:
- Initial inspection found 21 deliverables already complete and 19 requiring restart.
- The 19 restart workers completed successfully.
- Final audit result: `Batch13 final total=40 ok=40 bad=0`.
- Project state count after closeout: `INITIALIZED=213`.

## Immediate Next Actions

1. Continue Phase 2.2 after Batch 13.
2. Candidate next batch by Gate 7 register order begins with:
   - `DEL-040-01..06`
   - `DEL-041-01..06`
   - `DEL-042-01..06`
   - `DEL-043-01..04`
   - `DEL-044-01..04`
   - `DEL-045-01..04`
   - `DEL-046-01..06`
   - `DEL-073-01..04`
3. Before dispatching, re-scan filesystem state and exclude any deliverable already closed by evidence.
4. Dispatch each remaining Phase 2.2 unit as bounded `TASK + four-documents` with disjoint deliverable-local write scope.

## Handoff Payload

- Stable coordination policy: `_Coordination/_COORDINATION.md`.
- Mutable handoff state: this file.
- Accepted decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local continuity: each deliverable folder's `_STATUS.md`, four documents, and `_run_records/`.

## Update Protocol

- Update this file at each ORCHESTRATOR handoff with the latest completed batch, lifecycle distribution, active blockers, and next queue slice.
- Do not treat derivative artifacts as replacement decomposition truth.
- If a later phase consumes derivative packages, record the accepted upstream snapshot and derivative package currency before proceeding.
