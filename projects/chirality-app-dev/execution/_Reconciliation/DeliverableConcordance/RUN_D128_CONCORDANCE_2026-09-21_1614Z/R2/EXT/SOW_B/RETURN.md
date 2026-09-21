# RETURN: EXT worker W_SOW_B (SOW-043..SOW-084)

- **Ledger:** `SOW_claims.csv`, 62 rows over 42 units.
  - 20 units are split into `.1` (mapping) and `.2` (code or deferral) rows.
  - No run-local keys were used.
- **Validator:** `validate_ledger.py ledger --extension-index R2/EXT/_inputs/EXTENSION_INDEX_SOW_B.csv` returned `RESULT PASS errors=0 warnings=0`.
- **SHA-256 (sealed):** `6f0072e935e1934564a7be9c3f93dfe1ff23e109ad3d556dacf3df45611ccf0c`
- **Dispositions:**

  | Disposition | Rows |
  |---|---|
  | ALIGNED | 39 |
  | PARTIALLY_IMPLEMENTED | 8 |
  | IMPLEMENTED_DIFFERENTLY | 8 |
  | DOCUMENTED_UNIMPLEMENTED | 3 |
  | AUTHORITY_CONFLICT | 3 |
  | STALE_SPECIFICATION | 1 |

- **CauseTags:** CODEX_SOLE_ENGINE 15, A2_TOPOLOGY 5, SHELL_REDESIGN 2, CARRIER_PROPAGATION 1. No `OTHER:` tokens.
- **HumanDecisionNeeded:**
  - `R4-Q1`: 6 rows;
  - `R4`: 2 rows (SOW-075.2, SOW-076);
  - `R4-Q2; R4-Q5`: 1 row (SOW-044.2);
  - `R4-Q5`: 1 row (SOW-061.2);
  - `D-APP-116`: 1 row (SOW-059.2);
  - `D-APP-119`: 1 row (SOW-084.2).
- **LOW-confidence rows:** SOW-061.2, SOW-075.2, SOW-076.
- **PostReleaseBasis YES:** SOW-047.2, SOW-048.2, SOW-064.2 (application-tool hosting added by `da95ec194`).
- **`NO_LIVE_DELIVERABLE`:** SOW-079.1 (DEL-04-01 disclaims the item) and SOW-080 (DEL-09-07 retired by D-APP-127).
- **`NO_CODE_NO_DEFERRAL`:** SOW-084.2, organisation-layer part only.

## For the manager to resolve

1. **Deferral reading.** I counted gated `NOT_SELECTABLE_UNTIL` Remaining items as explicit deferral. This is why SOW-043, 063, 082 and 083 are ALIGNED. If the other half read it differently, the merge needs one rule (see notes §5).
2. **Build-pipeline evidence.** `package.json` and `frontend/scripts` evidence is tagged `REACH=LIVE`, because it is not in `REACHABILITY.csv`. This affects SOW-072, 073, 078 and 079.2.
3. **Decomposition not updated after D-GOV-43 / D-APP-127.** SOW-080, OI-003, OI-007 and OBJ-008 still carry the retired installer and Root-owned supply.
4. **Cross-deliverable observation for PKG-07.** DEL-07-03 `_STATUS.md` has no `## Remaining` section, although its History says V3-01 was retained.
