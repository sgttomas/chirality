# Fact sheet P-19 (cluster CL-19) — Pre-v3 drift

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Divergences already present before 2026-08-22. Which side (deliverable text or code) is to change for each?

## Counts — PRIMARY rows (260)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  |  | 6 |  |  |  | 2 |  | 8 |
| PKG-00 |  | 1 |  | 8 |  |  |  |  | 1 | 10 |
| PKG-01 |  | 2 |  | 11 |  |  |  |  |  | 13 |
| PKG-02 |  | 2 |  | 12 |  |  |  |  | 1 | 15 |
| PKG-03 |  | 8 |  | 5 |  |  |  |  |  | 13 |
| PKG-04 |  | 1 |  | 11 |  |  |  |  | 2 | 14 |
| PKG-05 |  | 2 |  | 9 |  |  |  |  |  | 11 |
| PKG-06 |  | 1 | 1 | 18 |  |  |  |  | 2 | 22 |
| PKG-07 | 1 | 12 | 3 | 16 | 1 |  | 1 |  | 1 | 35 |
| PKG-08 |  | 7 |  | 8 |  |  |  |  |  | 15 |
| PKG-09 |  | 4 |  | 25 |  |  |  |  | 2 | 31 |
| PKG-10 |  | 7 |  | 57 |  | 2 |  |  | 7 | 73 |
| **Total** | **1** | **47** | **4** | **186** | **1** | **2** | **1** | **2** | **16** | **260** |

## Counts — ALSO/CONTEXT members (118; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  | 2 |  |  |  | 2 |
| PKG-01 |  |  | 1 |  |  |  | 1 |
| PKG-02 | 1 |  |  |  |  |  | 1 |
| PKG-03 |  |  | 1 |  |  |  | 1 |
| PKG-04 | 27 |  | 2 |  |  |  | 29 |
| PKG-05 | 2 |  | 15 | 3 |  |  | 20 |
| PKG-06 | 1 | 2 | 11 |  |  |  | 14 |
| PKG-07 | 19 |  | 2 |  | 1 |  | 22 |
| PKG-08 |  |  | 4 |  | 3 |  | 7 |
| PKG-09 | 5 |  | 1 |  |  | 1 | 7 |
| PKG-10 | 6 | 1 | 5 | 1 | 1 |  | 14 |
| **Total** | **61** | **3** | **44** | **4** | **5** | **1** | **118** |

- PRIMARY AuthorityTier: `NOT_APPLICABLE` 115, `GOVERNANCE_INVARIANT` 70, `LOCAL_DESIGN` 64, `PRD` 11
- PRIMARY HumanDecisionNeeded: `NO` 260
- PRIMARY CauseTag: `PRE_V3_DRIFT` 260
- PRIMARY LatestDecision: `NONE_FOUND` 94, `D-APP-56` 29, `D-APP-56 (context)` 25, `D-APP-127 (context)` 10, `D-APP-38 (context)` 8, `D-APP-72 (context)` 6, `D-APP-52 (context)` 6, `D-APP-73 (context)` 6, `D-APP-53 (context)` 6, `D-APP-59` 6, `D-APP-68` 5, `D-APP-45 (context)` 5
- PRIMARY ClaimType: `STATE_ASSERTION` 91, `REQUIREMENT` 91, `CONTEXT_CLAIM` 31, `REGISTER_DEFECT` 26, `ACCEPTANCE` 17, `EXCLUSION` 3, `REMAINING_WORK` 1
- PRIMARY Confidence: `HIGH` 135, `MEDIUM` 118, `LOW` 7
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 129, TEST_ONLY 41, LIVE 41, LEGACY_ONLY 16, LIVE+TEST_ONLY 12, LEGACY_ONLY+LIVE 12, LEGACY_ONLY+LIVE+TEST_ONLY 5, LEGACY_ONLY+TEST_ONLY 4

## Contested or flagged members

- `DEL-06-02#CLM-005` (ALSO): AltReading: OWNER_DEFERRED (Addendum 5): worker B (PKG-06/DEL-06-02_B) Disposition=IMPLEMENTED_DIFFERENTLY; CauseTag=CODEX_SOLE_ENGINE; HumanDecisionNeeded=R4-Q1
- `DEL-06-04#CLM-027` (ALSO; now STALE_SPECIFICATION / HDN R4-Q1): SPOT_REFUTED S1-112: Disposition checked `STALE_SPECIFICATION`, checker proposes `IMPLEMENTED_DIFFERENTLY`
- `DEL-09-05#CLM-010.8` (ALSO; now PARTIALLY_IMPLEMENTED / HDN NO): R3_UNDECIDED: Addendum 10 (OC-05); current value stands, both readings in the R3 task files (R3_SUMMARY §8)
- `DEL-10-03#CLM-025.2` (PRIMARY; now PARTIALLY_IMPLEMENTED / HDN NO): SPOT_UNDECIDED S1-172: Disposition checked `PARTIALLY_IMPLEMENTED`; readings: — The row's evidence is only that DEL-10-03 ScopeOfWork.md:369 omits 'ready-for-construction' from the projects/chirality-app-dev/docs/CONTRACT.md:152 K-DOMAIN-
- `DEL-10-04#CLM-016.1` (ALSO; now AUTHORITY_CONFLICT / HDN R4; R4-Q1): SPOT_UNDECIDED S2-047: Disposition checked `AUTHORITY_CONFLICT`; readings: — Not settled in budget. Reading A: D-APP-56 R4-P27 assigns pec.yaml ownership to DEL-10-04 while PEC-loop commits b1074e7a4/ca49b846d author it under D-APP-70 

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-92, DEC:D-APP-94
- DEL-00-01: CLM-025, STATE-2
- DEL-00-02: CLM-010.3, CLM-011, CLM-026, REGISTER-2, REGISTER-3, STATE-1, STATE-2, STATE-3
- DEL-01-02: CLM-007.10, CLM-011.2, CLM-011.3, CLM-018.7, CLM-018.14°, CLM-022.4, CLM-050
- DEL-01-04: CLM-005, CLM-006.6, CLM-006.7, CLM-016, CLM-026, CLM-028, STATE-1
- DEL-02-01: CLM-018, CLM-023.1, CLM-030.3, REM-3, REGISTER-50
- DEL-02-02: CLM-020
- DEL-02-03: CLM-009.11, CLM-011°
- DEL-02-04: CLM-004.5, CLM-013, CLM-014, CLM-021.1, CLM-029
- DEL-02-05: CLM-013.8, CLM-016, CLM-020.3
- DEL-03-01: CLM-003.5, CLM-005.2, CLM-009.4, CLM-018.1, CLM-025
- DEL-03-02: CLM-018°
- DEL-03-03: CLM-003.7, CLM-005.4, CLM-009.1, CLM-009.8, CLM-012, CLM-013, CLM-020, CLM-023.5
- DEL-04-01: CLM-010.8°, CLM-013.6°, CLM-014.2°, CLM-017, CLM-018°, CLM-019°, CLM-021.2°
- DEL-04-02: CLM-005°, CLM-010.10°, CLM-010.14°, CLM-012°, CLM-019°, CLM-021°, CLM-024°, CLM-029°
- DEL-04-03: CLM-002, CLM-004.7, CLM-005°, CLM-009.3°, CLM-009.8°, CLM-009.12°, CLM-009.14, CLM-010°, CLM-011, CLM-012°, CLM-016, CLM-017°, CLM-018°, CLM-019.1°, CLM-022°, CLM-023, CLM-024°, CLM-025°, CLM-027, REGISTER-4, REGISTER-5
- DEL-04-04: CLM-003, CLM-013
- DEL-04-05: CLM-005°, CLM-012°, CLM-017, CLM-020°, CLM-035
- DEL-05-01: CLM-003°, CLM-004°, CLM-005, CLM-006°, CLM-009°, CLM-010.1°, CLM-010.2°, CLM-010.4°, CLM-010.14°, CLM-010.15, CLM-012°, CLM-013°, CLM-014.1, CLM-014.2°, CLM-016°, CLM-017, CLM-018°, CLM-019°, CLM-020, CLM-021.2°, CLM-024°, CLM-025°, CLM-027°, CLM-030, REGISTER-2
- DEL-05-02: CLM-010.13
- DEL-05-03: CLM-005, CLM-006°, CLM-010.12°, CLM-013, CLM-020.2
- DEL-06-01: CLM-015.1°
- DEL-06-02: CLM-005°, CLM-006, CLM-013, CLM-014°, CLM-021.1, CLM-026°, STATE-1
- DEL-06-03: CLM-013, CLM-019, CLM-020, CLM-028°
- DEL-06-04: CLM-004.7, CLM-005°, CLM-011°, CLM-012°, CLM-016, CLM-019.2, CLM-026°, CLM-027°, REGISTER-2, REGISTER-4
- DEL-06-05: CLM-016, CLM-017°, CLM-019.1°, CLM-031.2, REGISTER-3
- DEL-06-06: CLM-002, CLM-004.6, CLM-006, CLM-014, CLM-022.2, CLM-027°, CLM-029, CLM-030°, CLM-033
- DEL-07-01: CLM-011.10°, CLM-011.11
- DEL-07-02: CLM-009.11°, CLM-011, CLM-012, CLM-013.2, CLM-014.1°, CLM-015, CLM-017°, CLM-019, CLM-020.2, CLM-021.1, CLM-021.2, CLM-025.2, CLM-026, CLM-031, REGISTER-1, REGISTER-2, REGISTER-3
- DEL-07-03: CLM-009.1, CLM-009.8°, CLM-014, CLM-017°, CLM-023, CLM-030
- DEL-07-04: CLM-011.2°, CLM-011.4°, CLM-011.5°, CLM-011.13°, CLM-011.14, CLM-011.15°, CLM-011.16°, CLM-013.7°, CLM-013.9°, CLM-013.10°, CLM-013.12°, CLM-014°, CLM-016°, CLM-022°
- DEL-07-05: CLM-012.3, CLM-012.10, CLM-012.15°, CLM-012.17, CLM-014°, CLM-015, CLM-022, CLM-024.2°, CLM-028, CLM-029, CLM-033, CLM-035, REGISTER-2, REGISTER-3
- DEL-07-06: CLM-020, CLM-021.1, CLM-028, REGISTER-3
- DEL-08-01: CLM-004, CLM-012.1, CLM-015, CLM-018.1
- DEL-08-02: CLM-004.6, CLM-005.6, CLM-018.1
- DEL-08-03: CLM-013.9, CLM-013.12, CLM-025, CLM-026.1, CLM-030, CLM-036
- DEL-08-04: CLM-003.1°, CLM-009°, CLM-011°, CLM-019, CLM-030°
- DEL-08-05: CLM-006°, CLM-012.1°, CLM-012.2°, CLM-032
- DEL-09-01: CLM-003, CLM-004, CLM-006, CLM-009.7°, CLM-011°, CLM-017, CLM-018.6, CLM-023°
- DEL-09-02: CLM-003, CLM-005, CLM-010.15, CLM-010.16, CLM-012.3, CLM-018, CLM-020.1, CLM-020.2°, CLM-024, CLM-025
- DEL-09-03: CLM-004, CLM-012, CLM-015, CLM-018, CLM-020, REGISTER-3, REGISTER-5
- DEL-09-04: CLM-004.1, CLM-015, CLM-021, CLM-023.1
- DEL-09-05: CLM-010.4, CLM-010.8°, CLM-010.14°, CLM-021°
- DEL-09-06: CLM-010.15, CLM-012.6, CLM-013, CLM-017, CLM-020
- DEL-10-01: CLM-003.2, CLM-014, CLM-015, CLM-020, CLM-021°, CLM-022.1, CLM-026, CLM-027, CLM-028
- DEL-10-02: CLM-003.1°, CLM-003.2°, CLM-004, CLM-005, CLM-006, CLM-010.3, CLM-010.10, CLM-011, CLM-012, CLM-013.1, CLM-017, CLM-018, CLM-019.1, CLM-019.2°, CLM-023°, CLM-025, CLM-026, REGISTER-2, REGISTER-5
- DEL-10-03: CLM-003.2°, CLM-003.3°, CLM-004, CLM-005, CLM-009, CLM-010.8°, CLM-010.9, CLM-010.10, CLM-011, CLM-012.2, CLM-013, CLM-018, CLM-019.2, CLM-020.2, CLM-025.2, CLM-026.2, CLM-026.3, CLM-027, CLM-028, CLM-029.2, REGISTER-3, REGISTER-4
- DEL-10-04: CLM-003°, CLM-004.2, CLM-004.6°, CLM-005, CLM-007, CLM-009, CLM-010.2, CLM-010.4°, CLM-013, CLM-015, CLM-016.1°, CLM-019, CLM-020, CLM-021, CLM-022, CLM-023.1, CLM-027, CLM-028°, CLM-030, CLM-031, CLM-032, CLM-034, REGISTER-2, REGISTER-3, REGISTER-4, STATE-2
- DEL-10-05: CLM-004.4, CLM-006, CLM-009.1°, CLM-015, CLM-016, CLM-018, CLM-033, REGISTER-3, REGISTER-4, STATE-2, STATE-3
- DOC:ADDING_A_TOOL: 0°
- DOC:BUILDREL: 3, 6
- DOC:README: 2, 4, 5
- DOC:RUNTIME_ENGINE_CONTRACT: 6°
- DOC:TRACEABILITY: 1
