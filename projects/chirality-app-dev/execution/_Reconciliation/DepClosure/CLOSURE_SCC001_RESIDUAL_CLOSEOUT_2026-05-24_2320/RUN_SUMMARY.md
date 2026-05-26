# RUN SUMMARY - SCC-001 Residual Closeout Attempt

RUN_STATUS = WARNINGS

Snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320/`

Analyzer command:

`python3 /Users/ryan/ai-env/projects/chirality/tools/coordination/analyze_dep_closure.py execution --output-dir execution/_Reconciliation/DepClosure/CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320/Evidence`

## Result

The human-approved residual tranche removed all bidirectional pairs but did not fully close SCC-001.

| Metric | Value |
|---|---:|
| Dependency registers | 51 |
| Schema-valid registers | 51 |
| Total rows | 554 |
| Active deliverable execution edges | 101 |
| Strict SCC count | 1 |
| Strict SCC sizes | 6 |
| Bidirectional pairs | 0 |
| Orphans | 5 |
| ID normalizations | 0 |

## Closure Verdict

SCC-001 is not closed. The residual strict SCC is:

- `SCC-001`: `DEL-03-01;DEL-03-02;DEL-03-03;DEL-03-04;DEL-04-03;DEL-05-02`

Project-wide strict `BLOCKED` / `UNBLOCKED` remains unavailable because `scc_count = 1`.

## Next Required Work

RECONCILIATION should analyze the remaining longer-cycle internal edges in the six-node SCC, especially the `DEL-03-02` runtime lifecycle cluster, `DEL-04-03` mapper links, and `DEL-05-02` event links. CHANGE should apply no further dependency-row edits until the next row-level ruling package is accepted.
