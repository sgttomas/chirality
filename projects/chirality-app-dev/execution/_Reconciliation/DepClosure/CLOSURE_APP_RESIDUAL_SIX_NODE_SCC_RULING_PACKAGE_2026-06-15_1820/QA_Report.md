# QA Report - Dependency Closure

## Tooling QA

| Check | Result | Evidence |
|---|---|---|
| Analyzer executed | PASS | `Evidence/closure_summary.json` |
| Analyzer copied into snapshot | PASS | `analyze_closure.py` |
| Root summary copied into snapshot | PASS | `closure_summary.json` |
| Required analyzer evidence present | PASS | `coverage.csv`, `orphans.csv`, `scc_summary.csv`, `hubs.csv`, `bidirectional_pairs.csv`, `id_normalization.csv` |
| Cycle sample evidence present | PASS | `Evidence/cycles_sample.csv` |
| Cycle-participating edge evidence present | PASS | `Evidence/cycle_participating_edges.csv` |

## Register QA

| Check | Result | Evidence |
|---|---|---|
| Dependency registers discovered | PASS | 51 files in `Evidence/closure_summary.json` |
| Schema compliance | PASS | 51 valid, 0 invalid in `Evidence/closure_summary.json`; per-deliverable status in `Evidence/coverage.csv` |
| `IMPLEMENTS_NODE` anchor coverage | PASS | 51 present, 0 missing in `Evidence/closure_summary.json` |
| Evidence field coverage | PASS | 554/554 populated in `Evidence/closure_summary.json` |
| ID normalization | PASS | 0 normalizations in `Evidence/id_normalization.csv` |
| Unknown direction rows | PASS | Ad hoc check found 0 active deliverable execution rows with direction outside `UPSTREAM`/`DOWNSTREAM` |
| Missing-target active execution rows | PASS | Ad hoc check found 0 active deliverable execution rows targeting a non-discovered deliverable |
| Misplaced target fields | PASS | Ad hoc check found 0 rows where `TargetType != DELIVERABLE` while `TargetDeliverableID` is populated |

## Core Closure Checks

| Core check | Verdict | Notes |
|---|---|---|
| Schema compliance | PASS | All 51 discovered dependency registers are schema-valid. |
| Orphan dependencies | PASS | No active deliverable execution row targets a missing deliverable. |
| Circular dependencies | WARNING | One strict SCC remains. See `Evidence/scc_summary.csv`. |
| Anchor coverage | PASS | All 51 discovered deliverables have `IMPLEMENTS_NODE` anchors. |
| Misplaced fields | PASS | No misplaced `TargetDeliverableID` rows found in current registers. |
| ID format consistency | PASS | No ID normalization occurred. |
| Isolated deliverables | WARNING | Analyzer `orphans.csv` lists five deliverables with zero active execution edges: `DEL-01-01`, `DEL-01-03`, `DEL-02-04`, `DEL-10-04`, `DEL-10-05`. |
| Hub analysis | PASS | No node has total degree >= 20. |
| Bidirectional pairs | PASS | No bidirectional pairs remain. |

## Method Notes

- `analyze_dep_closure.py` names `orphans.csv` as orphan output, but its implementation records deliverables with no active execution edges, not missing target references.
- Missing-target active execution rows were checked separately for this run and none were found.
- `cycles_sample.csv` and `cycle_participating_edges.csv` were derived from the current analyzer graph semantics and current dependency registers to satisfy the SCC-focused evidence requirement.
