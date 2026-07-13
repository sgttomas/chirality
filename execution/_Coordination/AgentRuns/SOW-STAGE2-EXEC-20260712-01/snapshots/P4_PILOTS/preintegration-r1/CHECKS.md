# P4 Pilot Preintegration R1 Checks

Overall verdict: PASS
Basis: main 0d260eb024d8b8dada0df477b70ac880a6906ffa

| Gate | Result |
|---|---|
| Local/main/origin/remote basis | PASS — exact basis; divergence +0/-0 |
| P0/P2/P3 bindings | PASS — P2 15/15; P3 17/17 + 6/6; 154 rows equal |
| Prior blocked snapshot immutability | PASS — 8/8 manifest hashes |
| Repair managers | PASS — 2/2 terminal |
| Exact portability repair | PASS — 17 files; 46 substitutions; pre/post exact |
| Package portability | PASS — checkout/temp prefix counts 0/0 |
| Population and child provenance | PASS — 6 App + 4 Piping; 10 accepted |
| Abandoned DEL-07-01 classification | PASS — unaccepted; fresh R1 accepted |
| Live source/status/lifecycle identity | PASS — 40/40 + 10/10; IN_PROGRESS |
| Stage-1 candidate identity | PASS — 10/10 byte-exact |
| Current and target formats | PASS — 10 LEGACY_FOUR_DOC + 10 SOW_V1 |
| Child verdict classes | PASS — 30/30 |
| Mapping and line parity | PASS — 325/325; 3,466/3,466; all PRESERVED |
| Checklist and HTML determinism/safety | PASS — 10/10 repeated pairs |
| Replacement/rollback manifests | PASS — 50 unique paths + exact inverse |
| Isolated apply/rollback | PASS — 10/10 + 10/10 |
| App focused consumer tests | PASS — 2 files; 20 tests |
| Scope-of-work tool tests | PASS — 18 tests |
| Piping profile checks | PASS — 4/4; 14+18+14+20 dependency rows |
| Structured evidence | PASS — 83 JSON; 19 CSV; 27 TSV; 195 Markdown |
| Live project/source/caller containment | PASS |
| Temporary simulation cleanup | PASS |
| Blockers, material unknowns, waivers | none |

All checks are read-only with respect to candidates and project truth. No
repair, conversion, lifecycle, integration, release, H1/H2, ISSUED, retirement,
or Git action was performed.
