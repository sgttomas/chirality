# SCA-APP-012 post-acceptance validation

Owner act: "I accept SCA-APP-012 checkpoint group 3" (2026-09-27; `checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/`). Accepted revision `ac67109d9`. Applied state `c83a868cd`. Record `20260927T214035Z`. Written by `verify_post_acceptance.py`; candidate evidence reviewed at group 3 is not modified.

| Check | Result | Detail |
|---|---|---|
| 1. decision folder heading and verbatim act | PASS | projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/DECISION.md |
| 1. decision folder committed and unchanged | PASS |  |
| 1. group-3 manifest binds the accepted revision | PASS | 37 entries; mismatches 0 |
| 2. candidate decomposition at the accepted revision has its candidate hash | PASS | 929267727acbfd276359319877c0d3e4dc8eea9202ac5b0173d482b7a2fad4e0 |
| 2. E26 applied exactly (candidate + E26 with the date) | PASS | 6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577 |
| 2. other 11 files keep their accepted candidate hash | PASS | 11/11 |
| 3. _LATEST.md equals the filled template | PASS | 3d7e0352b4ce271535d801d86706142481845227bdfe87f4693f1ce10bc95d8b |
| 4. Brief.md status line | PASS |  |
| 5. Decision_Log.md G3 row | PASS |  |
| 6. Handoff_State.md equals the filled template | PASS | e9b3c0987d9dac0e0c55639b7b580d8539b555b03605de1076109cc856019625 |
| 7. coverage and topology equal the reviewed candidate | PASS | differing: []; packages 10, deliverables 52, scope items 84, objectives 10 |
| 7. registered tools unchanged (audit_structure, analyze_dep_closure, validate_decomposition_registers) | PASS | nodes 54, edges 104, SCC 0, register findings {'EVQ-006': 36} |
| 7. decomposition hash moved only by E26 | PASS |  |
| 7. scope-change pointer is the applied _LATEST.md | PASS |  |
| 8. supersession --check-map | PASS | Findings: 0 total, 0 blocking |

Result: PASS
