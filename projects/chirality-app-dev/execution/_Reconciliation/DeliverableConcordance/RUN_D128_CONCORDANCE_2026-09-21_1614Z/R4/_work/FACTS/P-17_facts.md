# Fact sheet P-17 (cluster CL-17) — Carrier propagation: D-APP-127 / D-GOV-43 not carried into deliverable text

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** D-APP-127 reached only the _STATUS.md of its carriers (XPF-022). How are these rows' ScopeOfWork, _CONTEXT, _REFERENCES and Dependencies texts to be brought to the ruled state?

## Counts — PRIMARY rows (118)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 1 |  |  |  | 2 |
| PKG-00 |  |  | 10 |  |  | 10 |
| PKG-01 |  | 2 | 8 | 1 | 1 | 12 |
| PKG-02 |  |  | 25 |  | 3 | 28 |
| PKG-03 |  |  | 6 |  | 2 | 8 |
| PKG-04 |  |  | 8 |  | 1 | 9 |
| PKG-05 |  |  | 5 |  | 1 | 6 |
| PKG-06 |  |  | 1 |  |  | 1 |
| PKG-07 |  |  | 22 |  | 3 | 25 |
| PKG-08 |  |  | 9 |  | 1 | 10 |
| PKG-09 |  |  | 6 |  | 1 | 7 |
| **Total** | **1** | **3** | **100** | **1** | **13** | **118** |

## Counts — ALSO/CONTEXT members (43; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|
| PKG-01 | 3 | 2 |  | 5 |
| PKG-02 |  | 1 |  | 1 |
| PKG-04 |  | 3 | 1 | 4 |
| PKG-05 |  | 2 | 1 | 3 |
| PKG-06 |  | 1 | 1 | 2 |
| PKG-07 |  | 3 | 2 | 5 |
| PKG-08 |  | 1 | 1 | 2 |
| PKG-09 |  | 17 | 2 | 19 |
| PKG-10 |  | 2 |  | 2 |
| **Total** | **3** | **32** | **8** | **43** |

- PRIMARY AuthorityTier: `NOT_APPLICABLE` 71, `LOCAL_DESIGN` 35, `GOVERNANCE_INVARIANT` 12
- PRIMARY HumanDecisionNeeded: `NO` 118
- PRIMARY CauseTag: `CARRIER_PROPAGATION` 118
- PRIMARY LatestDecision: `D-APP-127` 18, `D-APP-109` 16, `D-APP-38 (context)` 16, `D-APP-38` 10, `D-APP-111 (context)` 9, `D-APP-56 (context)` 9, `NONE_FOUND` 7, `D-APP-56` 7, `D-APP-109 (context)` 4, `D-APP-127 (context)` 4, `D-APP-53` 3, `D-APP-60 (context)` 3
- PRIMARY ClaimType: `STATE_ASSERTION` 41, `REQUIREMENT` 23, `CONTEXT_CLAIM` 23, `REGISTER_DEFECT` 17, `REMAINING_WORK` 7, `ACCEPTANCE` 6, `EXCLUSION` 1
- PRIMARY Confidence: `HIGH` 70, `MEDIUM` 43, `LOW` 5
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 78, LIVE 26, LEGACY_ONLY 5, LIVE+TEST_ONLY 4, TEST_ONLY 3, LEGACY_ONLY+LIVE+TEST_ONLY 2

## Contested or flagged members

- `DEL-06-06#STATE-2` (ALSO; now REMAINING_STATE_MISMATCH / HDN R4-Q1): R3_UNDECIDED: tie-break; current value stands, both readings in the R3 task files (R3_SUMMARY §8)

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-127
- DEL-00-01: CLM-003, CLM-009.1, CLM-010.2, CLM-011, CLM-015, CLM-016, CLM-022, REGISTER-1, STATE-1
- DEL-00-02: STATE-4
- DEL-01-02: CLM-010.2°, CLM-018.24°, CLM-018.25, CLM-020°, REGISTER-5, CLM-032, CLM-047, CLM-052, CLM-059.4
- DEL-01-03: CLM-008, CLM-011°, CLM-012, CLM-016, CLM-019, CLM-020
- DEL-01-04: CLM-004.5°, CLM-027
- DEL-02-01: SEC-5, CLM-024, CLM-027, CLM-030.2, REM-5
- DEL-02-02: SEC-5, CLM-006, CLM-007, CLM-017, CLM-021.1, REMTXT-2, REM-2°
- DEL-02-03: CLM-001, CLM-004.3, CLM-016, CLM-018, CLM-024, CLM-027, CLM-030, CLM-031, CLM-032, REGISTER-1, REGISTER-2, REGISTER-3
- DEL-02-04: SEC-5, REM-2
- DEL-02-05: SEC-3, REGISTER-4, STATE-1
- DEL-03-02: SEC-2.1, SEC-3, CLM-002, REGISTER-2, REGISTER-3, STATE-1
- DEL-03-03: REM-1
- DEL-03-04: STATE-2
- DEL-04-01: CLM-002, CLM-009°, REGISTER-3, STATE-1°
- DEL-04-02: CLM-010.12°, CLM-013, CLM-017, CLM-020, CLM-025°
- DEL-04-04: SEC-3, CLM-002, CLM-017, CLM-020
- DEL-05-01: CLM-026, CLM-032°, REGISTER-3, REGISTER-5
- DEL-05-02: REM-1°, REM-2, REGISTER-3
- DEL-05-03: CLM-009, CLM-011°
- DEL-06-01: CLM-032°
- DEL-06-03: SEC-3
- DEL-06-06: STATE-2°
- DEL-07-01: SEC-3, CLM-002, CLM-014, CLM-021, REGISTER-3, REGISTER-6
- DEL-07-02: STATE-1°
- DEL-07-03: SEC-3, CLM-011, CLM-012, CLM-015, CLM-016, CLM-020, CLM-021, CLM-022, CLM-027, CLM-028, CLM-029, REGISTER-2
- DEL-07-04: CLM-003°, CLM-004, CLM-019, CLM-023, CLM-032°, STATE-1°
- DEL-07-05: STATE-1°
- DEL-07-06: CLM-019, CLM-026, CLM-027, CLM-029
- DEL-08-01: SEC-3
- DEL-08-02: REMTXT-1°, REM-1°, STATE-1
- DEL-08-03: CLM-003, CLM-008, CLM-016, CLM-023, CLM-024, REGISTER-4
- DEL-08-04: SEC-3, CLM-004
- DEL-09-03: REGISTER-2
- DEL-09-04: CLM-003.1°, CLM-004.3°, CLM-008°, CLM-009.1°, CLM-011.6°, CLM-012.2°, CLM-024, REM-1°
- DEL-09-05: SEC-1, CLM-003°, CLM-009°, CLM-010.6°, CLM-010.7°, CLM-012°, STATE-1°, CLM-020°, CLM-023.2°, REM-2°, REM-3, REGISTER-52°, STATE-52°
- DEL-09-06: SEC-1°, REM-2, STATE-2
- DEL-09-07: STATE-2
- DEL-10-01: CLM-019°
- DEL-10-03: REGISTER-2°
- SOW: SOW:SOW-079.1
