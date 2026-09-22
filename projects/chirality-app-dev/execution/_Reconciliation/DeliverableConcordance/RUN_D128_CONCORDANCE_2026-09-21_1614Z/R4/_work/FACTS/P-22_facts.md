# Fact sheet P-22 (cluster CL-22) — Shell redesign and role adoption (not otherwise framed)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** SCA-APP-010 shell redesign and four-role adoption rows that do not cite R4-Q4 (SHELL_REDESIGN, OTHER:V3_ROLE_ADOPTION). How are these rows to be brought into agreement?

## Counts — PRIMARY rows (75)

| Package | Built, not written down (`IMPLEMENTED_UNDOCUMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  | 4 |  |  | 1 |  |  | 5 |
| PKG-01 |  | 2 |  |  |  |  |  | 2 |
| PKG-02 |  | 4 | 2 | 13 | 6 | 22 | 1 | 48 |
| PKG-05 |  |  |  |  |  |  | 1 | 1 |
| PKG-07 |  | 2 |  |  |  |  |  | 2 |
| PKG-08 | 1 | 2 |  | 4 | 8 |  | 1 | 16 |
| PKG-09 |  |  |  |  |  |  | 1 | 1 |
| **Total** | **1** | **14** | **2** | **17** | **15** | **22** | **4** | **75** |

## Counts — ALSO/CONTEXT members (73; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Retired by a ruling (`RETIRED_BY_RULING`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  | 2 |  |  |  |  |  | 2 |
| PKG-02 | 13 | 13 | 15 | 2 |  | 5 | 3 | 51 |
| PKG-08 | 5 | 9 | 5 |  | 1 |  |  | 20 |
| **Total** | **18** | **24** | **20** | **2** | **1** | **5** | **3** | **73** |

- PRIMARY AuthorityTier: `LOCAL_DESIGN` 29, `GOVERNANCE_INVARIANT` 19, `PRD` 17, `NOT_APPLICABLE` 10
- PRIMARY HumanDecisionNeeded: `NO` 75
- PRIMARY CauseTag: `SHELL_REDESIGN` 71, `OTHER:V3_ROLE_ADOPTION` 4
- PRIMARY LatestDecision: `D-APP-108` 50, `D-APP-108 (context)` 9, `D-APP-56` 4, `D-APP-74 (context)` 3, `D-GOV-41 (context)` 2, `NONE_FOUND` 1, `D-APP-120` 1, `D-APP-109` 1, `D-APP-56 (context)` 1, `D-APP-109 (context)` 1, `D-APP-74` 1, `D-APP-96` 1
- PRIMARY ClaimType: `REQUIREMENT` 51, `ACCEPTANCE` 8, `STATE_ASSERTION` 5, `CONTEXT_CLAIM` 5, `REMAINING_WORK` 4, `REGISTER_DEFECT` 2
- PRIMARY Confidence: `MEDIUM` 60, `HIGH` 10, `LOW` 5
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 44, LIVE+TEST_ONLY 20, no REACH tag 9, LEGACY_ONLY+LIVE+TEST_ONLY 1, LEGACY_ONLY+LIVE 1

## Contested or flagged members

- `DEL-02-03#CLM-009.3` (PRIMARY; now IMPLEMENTED_DIFFERENTLY / HDN NO): SPOT_REFUTED S1-024: Disposition checked `IMPLEMENTED_DIFFERENTLY`, checker proposes `ALIGNED`

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-96
- DEL-01-03: CLM-009.1, CLM-009.6
- DEL-02-01: SEC-1°, SEC-2°, SEC-3°, SEC-4°, CLM-003°, CLM-005°, CLM-007, CLM-009°, CLM-010.1°, CLM-010.2, CLM-010.3, CLM-010.4°, CLM-010.5°, CLM-010.6°, CLM-010.7°, CLM-010.8°, CLM-010.9°, CLM-010.10°, CLM-010.11°, CLM-012.1°, CLM-012.2°, CLM-012.3°, CLM-012.4°, CLM-012.5°, CLM-014, CLM-015.1°, CLM-017°, CLM-019°, CLM-020.1, CLM-020.2, CLM-020.3°, CLM-020.4°, CLM-020.5°, CLM-020.6°, CLM-020.7°, CLM-020.8, CLM-021°, CLM-025°, CLM-026°, CLM-029.1°, CLM-029.2°, CLM-029.3, REM-4°, REM-6
- DEL-02-02: SEC-1, SEC-2, CLM-002, CLM-003, CLM-004.1, CLM-005, CLM-009, CLM-010.1, CLM-010.3, CLM-010.4, CLM-010.5, CLM-010.6, CLM-010.7, CLM-010.8, CLM-010.9, CLM-010.11, CLM-011, CLM-012, CLM-014.1, CLM-014.2, CLM-018, CLM-019°, CLM-023, CLM-024°, CLM-025, CLM-026, CLM-027°, REMTXT-1
- DEL-02-03: CLM-003°, CLM-004.2°, CLM-005°, CLM-008°, CLM-009.1, CLM-009.3, CLM-009.7°, CLM-009.8°, CLM-009.9°, CLM-009.10°, CLM-009.13°, CLM-012°, CLM-019°, CLM-020°, CLM-029°, REGISTER-4
- DEL-02-04: SEC-1, SEC-3, CLM-003.1, CLM-005.1, CLM-005.2, CLM-007, CLM-009, CLM-010.1, CLM-015.1, CLM-019
- DEL-02-05: CLM-002
- DEL-05-04: REM-3
- DEL-07-03: SEC-1, SEC-2
- DEL-08-01: CLM-002, CLM-003°, CLM-005.1°, CLM-006, CLM-009.3, CLM-009.7°, CLM-009.8°, CLM-009.9°, CLM-009.10°, CLM-009.11°, CLM-009.14°, CLM-011°, CLM-012.2°, CLM-016°, CLM-017°, CLM-018.2°, CLM-022°, REM-1, REGISTER-5
- DEL-08-02: CLM-004.3°, CLM-005.5°, CLM-009.10°, CLM-009.16°
- DEL-08-03: CLM-004, CLM-005, CLM-006, CLM-012, CLM-013.1, CLM-013.2, CLM-013.3, CLM-013.4, CLM-013.13, CLM-015°, CLM-019.1°, CLM-028
- DEL-08-04: CLM-002
- DEL-09-04: REM-2
- DOC:RELIANCE: 13.1, 13.4, 13.6
- SOW: SOW:SOW-005.2°, SOW:SOW-081.2, SOW:SOW-084.2°
