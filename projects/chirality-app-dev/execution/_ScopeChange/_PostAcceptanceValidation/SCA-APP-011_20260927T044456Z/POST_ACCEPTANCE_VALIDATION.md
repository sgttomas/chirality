# SCA-APP-011 post-acceptance validation

Owner act: "I accept SCA-APP-011 checkpoint group 3" (2026-09-27; `checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`). Accepted revision `d48c785c5`. Record `20260927T044456Z`. Written by `verify_post_acceptance.py`; candidate evidence reviewed at group 3 is not modified.

| Check | Result | Detail |
|---|---|---|
| 1. decision folder heading | PASS | projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/DECISION.md |
| 1. group-3 manifest binds the accepted revision | PASS | 34 entries; mismatches 0 |
| 2. E47 applied exactly (candidate + E47 with the date) | PASS | cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876 |
| 2. other 15 files keep their accepted candidate hash | PASS | 15/15 |
| 3. _LATEST.md equals the filled template | PASS | 904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637 |
| 4. Runtime notice equals the filled template | PASS | projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-27_APP_SCA-APP-011_SCAFFOLD_API.md |
| 5. Brief.md status line | PASS |  |
| 5. Decision_Log.md G3 row | PASS |  |
| 5. Handoff_State.md equals the filled template | PASS | ac46161a6ea15fe2027b1470c8adc1204bcb650ee4adabe179400211163f3e9e |
| 6. coverage and topology equal the reviewed candidate | PASS | differing: [] |
| 6. registered tools unchanged (audit_structure, analyze_dep_closure, validate_decomposition_registers) | PASS | nodes 54, edges 111, SCC 0, register findings {'EVQ-006': 592} |
| 6. decomposition hash moved only by E47 | PASS |  |
| 6. scope-change pointer is the applied _LATEST.md | PASS |  |
| 7. supersession --check-map | PASS | Findings: 0 total, 0 blocking |

Result: PASS
