# QA Report

## Input and schema coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Dependency-register discovery | PASS | 51 `Dependencies.csv` files discovered; `Evidence/coverage.csv` contains 51 rows. |
| v3.1 schema | PASS | 51 valid, 0 invalid; all four refreshed registers independently passed `validate_dependencies_schema.py`. |
| Evidence population | PASS | 564/564 rows contain `EvidenceFile`; `Evidence/closure_summary.json`. |
| `IMPLEMENTS_NODE` anchors | PASS | 51 present, 0 missing; `Evidence/coverage.csv`. |
| Active deliverable endpoints | PASS | 112/112 resolved to the 51 discovered deliverables; 0 missing source IDs, target IDs, or invalid directions; `Evidence/core_checks.json`. |
| Misplaced fields | PASS | 0 ACTIVE EXECUTION rows have a non-DELIVERABLE `TargetType` with a populated `TargetDeliverableID`; `Evidence/core_checks.json`. |
| ID normalization | PASS | 0 normalizations; `Evidence/id_normalization.csv`. |

The analyzer's `execution_rows = 317` includes ACTIVE and RETIRED rows. Its graph filter consumes 296 ACTIVE EXECUTION rows, of which 112 target deliverables and collapse to 98 distinct directed edges over 46 connected graph nodes.

## Refreshed-register identity and class checks

| Deliverable | SHA-256 | Rows | Required semantic check |
| --- | --- | ---: | --- |
| DEL-02-05 | `c39a3d533bf5f811f35d3a3b7fbfd839e7c1baedc28607cc4d59ad9eb200b8d0` | 10 | Stable IDs retained; account/consent and validation handoff edges are evidence-grounded. |
| DEL-08-04 | `6c838e527a0f45f26dd12ae8ff15724369be23a8fce2f15114c9abf46ad9c9ed` | 10 | Exactly one managed-class row (`DEP-08-04-009`) and one native-class row (`DEP-08-04-010`); native row explicitly denies Agent-role inference. |
| DEL-08-05 | `70b4ef79271978b1b6d99ed34d768f8970ca67307ea819c024a2fe9138634042` | 11 | Exactly one managed-class row (`DEP-08-05-004`) and one native-class row (`DEP-08-05-011`); native row explicitly denies Agent 0/1/2 inference. |
| DEL-09-05 | `bde522ad79fb274157fe2bfa27ae527bb6c8715ed167235cf89a6576a8310afb` | 15 | `DEP-09-05-015` preserves the G6a exact-candidate owner gate and the WP-09/WP-11 separation. |

## Analyzer limitations and supplements

- The current registered analyzer does not create `cycles_sample.csv`; the bounded deterministic supplement is recorded in `Decision_Log.md` and `Evidence/cycles_sample.csv`.
- The analyzer labels isolated deliverables as orphans. No active deliverable endpoint is unresolved; the five entries in `Evidence/orphans.csv` are treated as isolates.
- No prior live-register closure snapshot was requested for comparison. The nine-node SCC is new relative to the accepted objective-relative SCA DAG, but this audit does not claim Gate-5 caused it.

## Write containment

This dedicated auditor did not modify dependency registers or other deliverable files. It wrote only this audit package and its child control return. No `_Evaluation` path and no `_LATEST.md` pointer was created or modified.
