# QA report — dependency closure

| Core check | Verdict | Result |
|---|---|---|
| Schema compliance | `WARNING` | 0/53 `Dependencies.csv`; extraction is later-gated. |
| Orphan dependency targets | `PASS` | 0 targets and therefore 0 orphan targets. |
| Circular dependencies | `PASS` | 53 singleton SCCs; 0 non-trivial SCCs. |
| Anchor coverage | `WARNING` | 0/53 extracted anchors because no register exists. |
| Misplaced fields | `PASS` | 0 rows; none misplaced. |
| ID format consistency | `PASS` | 53 unique accepted IDs; no row normalization. |
| Isolated deliverables | `INFO` | 53, expected before extraction. |
| Hub analysis | `PASS` | 0 at threshold 20. |
| Bidirectional pairs | `PASS` | 0. |

The two warnings are coverage facts, not invented closure defects. The seven
N1 empty containers are expressly expected post-INIT state. No SOW or
dependency-extraction authority exists in this tranche.
