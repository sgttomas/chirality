# RUN SUMMARY - SCC-001 Ready Tranche 001

RUN_STATUS = WARNINGS

Snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301/`

Analyzer command:

`python3 /Users/ryan/ai-env/projects/chirality/tools/coordination/analyze_dep_closure.py execution --output-dir execution/_Reconciliation/DepClosure/CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301/Evidence`

## Result

The accepted SCC-001 ready tranche reduced but did not close the strict active concrete dependency graph.

| Metric | Value |
|---|---:|
| Dependency registers | 51 |
| Schema-valid registers | 51 |
| Total rows | 554 |
| Active deliverable execution edges | 105 |
| Strict SCC count | 2 |
| Strict SCC sizes | 2, 8 |
| Bidirectional pairs | 4 |
| Orphans | 5 |
| ID normalizations | 0 |

## Closure Verdict

SCC-001 is not closed. The former 18-node SCC has split into two residual SCCs:

- `SCC-001`: `DEL-06-01;DEL-06-04`
- `SCC-002`: `DEL-03-01;DEL-03-02;DEL-03-03;DEL-03-04;DEL-04-03;DEL-05-02;DEL-05-03;DEL-05-05`

Project-wide strict `BLOCKED` / `UNBLOCKED` remains unavailable because `scc_count = 2`.

## Next Required Work

Continue RECONCILIATION on the remaining human-ruling-needed rows and residual SCC rows. CHANGE should apply no further dependency-row edits until the next row-level ruling package is accepted.
