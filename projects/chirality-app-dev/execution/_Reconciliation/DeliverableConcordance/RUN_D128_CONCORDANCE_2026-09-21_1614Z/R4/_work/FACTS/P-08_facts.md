# Fact sheet P-08 (cluster CL-08) — R4-Q2: Codex engine never run through the K-ENGINE-2 conformance suite

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** R4-Q2: the Codex engine was never run through the K-ENGINE-2 conformance suite; what conformance obligation applies to the shipped engine?

## Counts — PRIMARY rows (24)

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 |  |  |  | 2 |  |  | 1 | 4 |
| PKG-01 |  |  | 1 |  |  |  |  |  | 1 |
| PKG-03 |  | 5 | 6 | 1 |  |  | 1 |  | 13 |
| PKG-04 |  | 1 |  |  | 1 |  |  |  | 2 |
| PKG-06 |  |  | 2 |  |  | 1 |  |  | 3 |
| PKG-09 |  | 1 |  |  |  |  |  |  | 1 |
| **Total** | **1** | **7** | **9** | **1** | **3** | **1** | **1** | **1** | **24** |

## Counts — ALSO/CONTEXT members (8; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Total |
|---|---:|---:|---:|
| EXT | 2 | 2 | 4 |
| PKG-01 | 2 |  | 2 |
| PKG-03 | 2 |  | 2 |
| **Total** | **6** | **2** | **8** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 18, `PRD` 4, `LOCAL_DESIGN` 2
- PRIMARY HumanDecisionNeeded: `R4-Q2` 15, `R4-Q1; R4-Q2` 7, `R4-Q2; R4-Q1` 2
- PRIMARY CauseTag: `CODEX_SOLE_ENGINE` 20, `A2_TOPOLOGY` 1, `RUNTIME_EXTRACTION` 1, `PRE_V3_DRIFT` 1, `NONE` 1
- PRIMARY LatestDecision: `D-GOV-43 (context)` 13, `D-GOV-43` 5, `D-APP-127 (context)` 3, `D-APP-127` 2, `NONE_FOUND` 1
- PRIMARY ClaimType: `REQUIREMENT` 21, `ACCEPTANCE` 2, `REMAINING_WORK` 1
- PRIMARY Confidence: `MEDIUM` 19, `HIGH` 4, `LOW` 1
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE+TEST_ONLY 12, LEGACY_ONLY+TEST_ONLY 7, LEGACY_ONLY+LIVE 3, LEGACY_ONLY+LIVE+TEST_ONLY 1, LIVE 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-02: CLM-006.1°, CLM-006.13, CLM-018.4°
- DEL-03-01: CLM-003.8, CLM-003.9, CLM-005.4, CLM-009.8, CLM-009.10, CLM-009.13°, CLM-011.3, CLM-012, CLM-013.2°, CLM-018.4, CLM-019.1, CLM-019.2, CLM-022.2, REM-2
- DEL-03-02: CLM-009.2
- DEL-04-03: CLM-004.6
- DEL-04-05: CLM-004
- DEL-06-04: CLM-009.15, CLM-011, CLM-019.1
- DEL-09-02: CLM-010.2
- DOC:RELIANCE: 3.1°, 3.14, 4.1°, 4.14
- DOC:RUNTIME_ENGINE_CONTRACT: 9°
- SOW: SOW:SOW-018.2, SOW:SOW-037, SOW:SOW-044.2°
