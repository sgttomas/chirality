# P4 Pilot Preintegration Checks

Overall verdict: BLOCKED
Blocking finding: PF-PORT-001

| Gate | Result |
|---|---|
| Local/main/origin/remote basis | PASS — 0d260eb024d8b8dada0df477b70ac880a6906ffa, divergence +0/-0 |
| P3 accepted/internal hashes | PASS — 17/17 and 6/6 |
| P2 consumer hashes | PASS — 15/15 |
| Population and provenance | PASS — 6 App + 4 Piping; ten accepted terminals |
| Abandoned DEL-07-01 classification | PASS — nonterminal/unaccepted; R1 accepted |
| Live source/status/lifecycle identity | PASS — 40/40 + 10/10; all IN_PROGRESS |
| Stage-1 candidate identity | PASS — 10/10 byte-exact |
| Current/target format | PASS — 10 LEGACY_FOUR_DOC + 10 SOW_V1 |
| Mapping and line parity | PASS — 325/325; 3,466/3,466; all PRESERVED |
| Checklist and HTML determinism/safety | PASS — 10/10 repeated pairs |
| Replacement/rollback manifests | PASS — 50 unique paths + exact inverse |
| Isolated apply/rollback | PASS — 10/10 + 10/10 |
| App focused consumer tests | PASS — 2 files, 20 tests |
| Scope-of-work tool tests | PASS — 18 tests |
| Piping four-document/dependency checks | PASS — 4/4; 14+18+14+20 rows |
| Structured package evidence | PASS — 81 JSON, 19 CSV, 25 TSV |
| Live project write containment | PASS — scoped project porcelain empty |
| Temporary simulation cleanup | PASS |
| Evidence portability | BLOCKED — 46 checkout-prefix occurrences / 17 paths |
| Waivers | PASS — none |

No source, project, candidate, control, lifecycle, Git, H1/H2, release,
ISSUED, integration, or retirement repair was attempted.
