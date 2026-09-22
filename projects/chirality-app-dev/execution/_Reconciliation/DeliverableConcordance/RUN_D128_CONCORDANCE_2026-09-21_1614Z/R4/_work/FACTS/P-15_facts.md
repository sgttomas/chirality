# Fact sheet P-15 (cluster CL-15) — Live path: execution-root scaffolding returns 501

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Execution-root scaffolding returns 501 on the live path because no scaffold port is composed, and no ruling or CONTEXT record drops it (XPF-044). What is to change, and in which surface?

## Counts — PRIMARY rows (28)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 1 |  |  |  | 2 |
| PKG-07 | 14 | 3 |  | 1 | 1 | 19 |
| PKG-09 |  | 3 | 1 | 3 |  | 7 |
| **Total** | **15** | **7** | **1** | **4** | **1** | **28** |

## Counts — ALSO/CONTEXT members (8; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| PKG-02 |  |  |  |  | 1 | 1 |
| PKG-04 |  |  |  | 1 |  | 1 |
| PKG-06 |  |  | 1 |  |  | 1 |
| PKG-07 | 2 | 2 |  |  |  | 4 |
| PKG-09 |  |  | 1 |  |  | 1 |
| **Total** | **2** | **2** | **2** | **1** | **1** | **8** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 21, `PRD` 4, `NOT_APPLICABLE` 2, `LOCAL_DESIGN` 1
- PRIMARY HumanDecisionNeeded: `NO` 28
- PRIMARY CauseTag: `A2_TOPOLOGY` 19, `CODEX_SOLE_ENGINE` 3, `PRE_V3_DRIFT` 2, `CARRIER_PROPAGATION` 2, `DOC_HYGIENE` 1, `CREDENTIAL_CUSTODY` 1
- PRIMARY LatestDecision: `D-APP-127 (context)` 18, `D-APP-127` 4, `NONE_FOUND` 3, `D-APP-56` 1, `D-APP-38 (context)` 1, `D-APP-38` 1
- PRIMARY ClaimType: `REQUIREMENT` 25, `STATE_ASSERTION` 2, `CONTEXT_CLAIM` 1
- PRIMARY Confidence: `HIGH` 14, `MEDIUM` 14
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE+TEST_ONLY 16, LIVE 7, LEGACY_ONLY+LIVE+TEST_ONLY 4, LEGACY_ONLY+LIVE 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-02-05: CLM-004.2°
- DEL-04-05: CLM-009.3°
- DEL-06-02: CLM-010.2°
- DEL-07-02: CLM-003, CLM-004.1°, CLM-005, CLM-008, CLM-009.1, CLM-009.2, CLM-009.3, CLM-009.4, CLM-009.5, CLM-009.6, CLM-009.7, CLM-009.8, CLM-009.9, CLM-009.10, CLM-009.12, CLM-009.13, CLM-010, CLM-014.1, CLM-014.2°, CLM-018°, CLM-024°, CLM-029, STATE-1
- DEL-09-01: CLM-009.7, CLM-016
- DEL-09-06: SEC-1, CLM-003, CLM-004, CLM-010.1°, CLM-010.3, CLM-018
- SOW: SOW:SOW-024.2, SOW:SOW-025.2
