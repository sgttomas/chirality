# RETURN: EXT worker DEC (item 3, decision-effect audit)

- **Ledger:** `DEC_claims.csv`, 46 rows.
  - 41 unit rows cover all 38 units; 3 units are split (D-APP-112, 114, 125).
  - There are 5 `DEC:REGISTER-n` rows.
- **Validator:** `RESULT PASS errors=0 warnings=0`.
- **SHA-256:** `7601ffe7e243261671dd8224020eb094de4f5a89aa2fff5dd65dcbcfcf94f912`. The ledger is sealed and there are no errata.
- **Top dispositions:**
  - 25 ALIGNED
  - 8 RETIRED_BY_RULING
  - 3 ACCEPTED_DIVERGENCE
  - 3 PARTIALLY_IMPLEMENTED
  - 2 DOCUMENTED_UNIMPLEMENTED
  - 4 REMAINING_STATE_MISMATCH and 1 STALE_SPECIFICATION (the REGISTER rows)
- **EFFECT_NOT_LANDED:** 88, 92, 99, 101, 121, 125.1, 125.2, 126, 127.
  - Still owed: 99, 101, 121, 125.1, 127.
  - Never landed, then retired: 88, 92, 125.2, 126.
- **Flagged rows:**
  - The flags on D-APP-121 and D-APP-125 are accurate.
  - The flags on D-APP-104, 107, 122 and 123 are stale; the effects landed. See REGISTER-1 and REGISTER-2.
  - D-APP-126's flag is moot, because D-APP-127 retired it.
- **For the manager to resolve:**
  1. D-APP-112.2 (LOW, R4). D-APP-112 item B was displaced by the 2026-09-19 owner direction, which has no register row. I treated that direction as GOVERNING and dispositioned the row ACCEPTED_DIVERGENCE; the alternative is AUTHORITY_CONFLICT.
  2. One OTHER token was used: `OTHER:LOOP_WORKGRAPH_TRANSITION`.
  3. I added a Notes token of my own, `EFFECT_LANDED_THEN_SUPERSEDED` (rows 94, 96, 100, 104, 107, 112.2, 114.2). It is not part of the vocabulary.
  4. Root-side effects are outside the read boundary and were not verified: the D-APP-106 validator and the D-APP-108, 101 and 120 Root routing.
- **Notes:** `DEC_notes.md`.
