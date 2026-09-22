# Dependency closure report

## Current production conclusion

PASS with isolate warnings for the explicit 51 current production deliverables. The registered analyzer reports COMPLETE/PASS, 111 unique directed edges, zero unresolved workspace targets, zero existing targets outside this scope, zero strongly connected components, zero bidirectional pairs, and zero hubs at degree 20. The graph has 51 selected nodes including 3 isolates: DEL-01-01, DEL-10-04, DEL-10-05. These are topology warnings, not missing target rows.

DEP-10-04-008 is an ACTIVE DOCUMENT prerequisite in DEL-10-04 with current SatisfactionStatus=PENDING, cited at Evidence/dep_10_04_008.json. This snapshot supplies the current candidate graph observation it calls for: zero unresolved targets and zero SCCs under the declared strict filter. The historical SATISFIED D53A claim is not carried forward as current satisfaction; whether and when to update the register remains a separate record decision. The row's TargetLocation is projects/chirality-app-dev/execution/_Evaluation/DepClosure/_LATEST.md; the stable observation pointer is projects/chirality-app-dev/execution/_Evaluation/DepClosure/_LATEST.md.

| Core check | Verdict | Evidence |
| --- | --- | --- |
| Schema compliance | PASS | Evidence/CURRENT51/coverage.csv; closure_summary.json |
| Missing targets | PASS | Evidence/CURRENT51/orphans.csv |
| Cycles / SCCs | PASS | Evidence/CURRENT51/scc_summary.csv; cycles_sample.csv |
| IMPLEMENTS_NODE anchors | PASS | Evidence/CURRENT51/coverage.csv |
| Misplaced target fields | PASS | closure_summary.json |
| ID format | PASS | Evidence/CURRENT51/id_normalization.csv |
| Isolated units | WARNING | Evidence/CURRENT51/isolated.csv |
| Hubs | PASS | Evidence/CURRENT51/hubs.csv |
| Bidirectional pairs | PASS | Evidence/CURRENT51/bidirectional_pairs.csv |

## Full inventory and applicability

The independent folder census is 54 IDs: 52 retained accepted production IDs and two PKG-00 reconciliation controls. Among the 52, DEL-09-07 is retired history under D-GOV-43/D-APP-127 and the live decomposition says SOW-080 is OUT. The control _CONTEXT.md files explicitly require no Dependencies.csv. The full ALL analyzer thus reports COMPLETE/FAIL (52 files, two missing control registers), not ALL PASS; its missing-register and anchor warnings are intentional scope exceptions. The retired DEL-09-07 folder and CSV remain preserved. There are no active current-scope strict edges from or to an excluded unit: outside_scope.csv is header only.

## Prior accepted graph

The accepted CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034 recorded 52 registers, 654 rows, 119 strict edges, 48 connected nodes, zero SCCs, and four isolates including DEL-09-07. This observation has 51 current registers, 648 rows, 111 strict edges, 48 connected nodes and 0 SCCs. Evidence/edge_delta.csv identifies 8 removed and 0 added edges, with each prior row ID and its live status and target type. Edge changes are interpreted row by row rather than inferred from counts. The present analyzer counts all selected nodes, unlike the accepted summary's connected-node convention, so raw graph_nodes totals are not directly comparable.

The accepted _Reconciliation/DepClosure/_LATEST.md is unchanged. This evaluation snapshot is not an acceptance act, a product verification result, or a release qualification. Reproduce with the exact command arrays and SHA-256 basis in Tool_Run.json and Source_Basis.json.
