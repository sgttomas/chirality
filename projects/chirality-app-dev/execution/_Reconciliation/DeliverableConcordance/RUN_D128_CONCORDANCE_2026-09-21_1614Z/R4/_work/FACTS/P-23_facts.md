# Fact sheet P-23 (cluster CL-23) — Open lifecycle gates and v3 release scope

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Normal open human gates and explicit v3 scope boundaries (LIFECYCLE_GATE_PENDING, V3_RELEASE_SCOPE). Which of these gates or scope boundaries are to be closed or restated?

## Counts — PRIMARY rows (38)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 2 | 1 | 3 |  |  | 6 |
| PKG-02 |  | 2 | 1 |  | 1 | 4 |
| PKG-03 | 1 | 2 |  |  |  | 3 |
| PKG-06 | 1 |  |  |  |  | 1 |
| PKG-08 | 3 | 6 | 4 |  |  | 13 |
| PKG-09 | 1 | 1 |  |  |  | 2 |
| PKG-10 | 1 | 4 |  | 4 |  | 9 |
| **Total** | **9** | **16** | **8** | **4** | **1** | **38** |

## Counts — ALSO/CONTEXT members (72; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  |  | 1 |  |  | 1 | 2 |
| PKG-02 |  | 4 | 2 |  |  |  |  | 6 |
| PKG-04 | 2 | 2 |  |  |  |  |  | 4 |
| PKG-05 |  | 2 | 3 |  |  |  |  | 5 |
| PKG-06 |  | 1 |  |  |  |  |  | 1 |
| PKG-07 |  | 1 |  |  |  |  |  | 1 |
| PKG-08 | 3 | 19 | 15 |  |  |  |  | 37 |
| PKG-09 |  | 1 |  |  |  | 1 | 1 | 3 |
| PKG-10 |  | 3 |  |  | 10 |  |  | 13 |
| **Total** | **5** | **33** | **20** | **1** | **10** | **1** | **2** | **72** |

- PRIMARY AuthorityTier: `LOCAL_DESIGN` 21, `NOT_APPLICABLE` 7, `GOVERNANCE_INVARIANT` 7, `PRD` 3
- PRIMARY HumanDecisionNeeded: `NO` 38
- PRIMARY CauseTag: `LIFECYCLE_GATE_PENDING` 29, `V3_RELEASE_SCOPE` 9
- PRIMARY LatestDecision: `NONE_FOUND` 13, `D-APP-127` 4, `D-APP-38 (context)` 3, `D-APP-50` 3, `D-APP-121` 2, `D-APP-108` 2, `D-APP-37` 2, `D-APP-108 (context)` 1, `D-APP-36 (context)` 1, `D-GOV-42 (context)` 1, `D-APP-114` 1, `D-APP-49` 1
- PRIMARY ClaimType: `REQUIREMENT` 19, `ACCEPTANCE` 8, `STATE_ASSERTION` 5, `REMAINING_WORK` 3, `CONTEXT_CLAIM` 3
- PRIMARY Confidence: `MEDIUM` 23, `HIGH` 13, `LOW` 2
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 19, no REACH tag 8, LIVE+TEST_ONLY 4, TEST_ONLY 4, LEGACY_ONLY+LIVE 2, LEGACY_ONLY 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-101, DEC:D-APP-121, DEC:D-APP-125.1
- DEL-02-01: REM-1, REM-7°
- DEL-02-02: SEC-3°, SEC-4°, CLM-010.2°, REM-1°, REM-3°
- DEL-02-03: REM-1
- DEL-02-04: CLM-010.14
- DEL-02-05: REM-1
- DEL-03-02: SEC-1, SEC-2.2, SEC-2.3
- DEL-04-04: SEC-1°, SEC-2°, CLM-010.5°, REM-1°
- DEL-05-04: CLM-004.2°, CLM-010.14°, CLM-010.15°, CLM-010.19°, REM-2°
- DEL-06-03: SEC-2.2, CLM-024°
- DEL-07-01: SEC-2°
- DEL-08-01: SEC-1°, SEC-2°
- DEL-08-02: CLM-003.2°, CLM-003.3°, CLM-003.4°, CLM-003.5°, CLM-003.6°, CLM-003.7°, CLM-005.2°, CLM-005.3°, CLM-005.4°, CLM-008°, CLM-009.2°, CLM-009.6°, CLM-009.7°, CLM-009.8°, CLM-009.9°, CLM-009.11°, CLM-009.12°, CLM-009.13°, CLM-009.14°, CLM-009.18°, CLM-009.19°, CLM-011.1°, CLM-011.2, CLM-012.1, CLM-012.2°, CLM-017°, CLM-018.2°, CLM-021°, CLM-022°, CLM-023, CLM-024, CLM-025
- DEL-08-04: SEC-1°, SEC-2.1°, SEC-2.2, CLM-033°, CLM-016.1°, CLM-016.3°, CLM-016.7°, CLM-022.2°
- DEL-08-05: CLM-037, CLM-018.1, CLM-018.2, CLM-018.3, CLM-018.4, CLM-018.6, CLM-025.1°, CLM-025.2
- DEL-09-02: REM-1
- DEL-09-03: CLM-009.11
- DEL-09-05: CLM-022°, CLM-023.1°, CLM-026°
- DEL-10-01: CLM-004.4°, CLM-004.5, CLM-012.7°, CLM-012.10, CLM-025.2°, CLM-025.3
- DEL-10-02: CLM-003.4°, CLM-010.4°, CLM-010.5°, CLM-010.6°, CLM-010.11°, CLM-010.12, CLM-022°
- DEL-10-04: CLM-010.3°, CLM-010.5°, CLM-010.7, CLM-010.10, CLM-010.12, CLM-012°
- DEL-10-05: CLM-009.3°, CLM-011, CLM-019
- DOC:BUILDREL: 1, 9.5°, 11°, 14
- DOC:VALSTRAT: 4.14
