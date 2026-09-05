# Decomposition Coverage Report — SCA-APP-009 Gate-5 Pre-change R3

**Overall:** `BLOCKERS`
**Closure readiness:** `FAIL`
**Basis:** `aa8554542e3d6d09a925f69e1114bea8e18532f8`

Authoritative inputs: decomposition SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; companion SHA-256 `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`; `_LATEST.md` SHA-256 `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`, pointing uniquely to SCA-APP-008.

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages resolve exactly once. |
| 2 Deliverable forward coverage | PASS | 51/51 declared deliverables resolve exactly once. |
| 3 Reverse folder coverage | WARNING | Undeclared PKG-00 and DEL-00-01/02 remain; 51/53 deliverable reverse coverage. |
| 4 ID consistency | PASS | No duplicate declared-ID root or folder-prefix mismatch. |
| 5 Context fidelity | WARNING | 51 contexts present; 47 match and four remain partial. |
| 6 Artifact presence | WARNING | 12/182 deterministic local-filename matches; 50 incomplete rows remain warning-level while all are IN_PROGRESS. |
| 7 Objective mapping | PASS | 10/10 objectives have live support; no declared deliverable or IN ledger row lacks mapping. |
| 8 Ledger integrity | PASS | 78 rows: 73 IN, four OUT, one TBD; all IN references resolve. |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Stale 81-ID/48-family prose remains; companion remains 83 IDs/50 families. |
| 10 Active snapshot/handoff | BLOCKER | SCA-APP-008 is active and historically reconciled, but six required root artifacts remain absent. |
| 11 Lifecycle | PASS | 51/51 IN_PROGRESS; every paired MEMORY was read. |
| 12 Baseline comparison | PASS | Fresh counts, identities, issue classes, severities, lifecycle, and protected posture equal Gate 1 and the prior Gate-5 pre-change audit. |

The sole blocker is the immutable historical SCA-APP-008 package-shape defect: its root lacks `Propagation_Plan.md`, `Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`, `Decision_Log.md`, and `RUN_SUMMARY.md`. The active post-application dependency audit remains `WARNINGS`: all 112 active endpoints resolve, the nine-node SCC remains surfaced without silent linearization, five isolated deliverables remain visible, and one bidirectional pair is informational.

Protected transaction posture is unchanged: S-7/S-1/S-4a/S-2 remain prospective; S-6 and the SCC remain separate; `SOW-079`, `SOW-080`, `DEL-09-07`, and `DEC-024` remain absent from current authority; the DEL-09-07 folder and SCA-APP-009 snapshot remain absent. Approved Gate-3 postimages remain decomposition `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97` and companion `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`.

The current-main `aa855454` merge delta against first parent `a772b7661` is only five files under `plans/shell-redesign_2026-09-04/` (four markdown surfaces and the mock HTML). It changes no audited or future-write surface. This derivative audit authorizes no repair, application, pointer movement, downstream rerun, product, release, or implementation act.
