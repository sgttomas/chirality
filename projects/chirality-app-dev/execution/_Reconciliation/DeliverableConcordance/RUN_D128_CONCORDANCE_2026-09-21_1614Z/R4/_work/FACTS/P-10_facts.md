# Fact sheet P-10 (cluster CL-10) — Rows held on existing or awaiting decisions (D-APP-nn / D-GOV-nn tokens)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** These rows name an existing decision in HumanDecisionNeeded; D-APP-116..119 are AWAITING_RULING and hold their rows from R5 (RUN_BASIS §1). Which of these rows does each named decision settle once ruled or re-read?

## Counts — PRIMARY rows (18)

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT |  |  | 2 |  |  | 2 |
| PKG-02 |  |  | 1 |  |  | 1 |
| PKG-03 | 1 |  |  |  |  | 1 |
| PKG-04 |  | 1 |  | 3 | 1 | 5 |
| PKG-05 | 1 |  |  | 2 |  | 3 |
| PKG-06 | 1 |  |  |  |  | 1 |
| PKG-07 |  |  |  | 1 |  | 1 |
| PKG-08 | 1 |  |  |  | 1 | 2 |
| PKG-09 | 1 |  | 1 |  |  | 2 |
| **Total** | **5** | **1** | **4** | **6** | **2** | **18** |

## Counts — ALSO/CONTEXT members (23; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| PKG-02 |  |  |  | 1 |  | 1 |
| PKG-04 | 1 | 1 |  |  |  | 2 |
| PKG-05 | 1 |  |  | 12 | 1 | 14 |
| PKG-07 |  | 2 |  |  |  | 2 |
| PKG-08 |  |  |  | 2 |  | 2 |
| PKG-09 |  | 1 |  |  |  | 1 |
| PKG-10 |  |  | 1 |  |  | 1 |
| **Total** | **2** | **4** | **1** | **15** | **1** | **23** |

- PRIMARY AuthorityTier: `LOCAL_DESIGN` 8, `GOVERNANCE_INVARIANT` 5, `NOT_APPLICABLE` 4, `PRD` 1
- PRIMARY HumanDecisionNeeded: `D-APP-127` 4, `D-APP-119` 3, `D-APP-73` 2, `D-APP-116` 2, `D-APP-121` 2, `D-APP-117; R4` 1, `D-APP-118` 1, `D-GOV-43` 1, `D-APP-43` 1, `D-APP-117` 1
- PRIMARY CauseTag: `NONE` 5, `A2_TOPOLOGY` 5, `LIFECYCLE_GATE_PENDING` 2, `CARRIER_PROPAGATION` 2, `CODEX_SOLE_ENGINE` 2, `PRE_V3_DRIFT` 1, `SHELL_REDESIGN` 1
- PRIMARY LatestDecision: `D-APP-127` 5, `D-APP-108` 3, `D-APP-73` 2, `D-APP-121` 2, `D-APP-118` 1, `D-GOV-43` 1, `D-APP-116` 1, `D-APP-43` 1, `D-APP-103` 1, `D-APP-102 (context)` 1
- PRIMARY ClaimType: `REMAINING_WORK` 8, `REQUIREMENT` 4, `ACCEPTANCE` 2, `CONTEXT_CLAIM` 2, `REGISTER_DEFECT` 1, `STATE_ASSERTION` 1
- PRIMARY Confidence: `MEDIUM` 11, `HIGH` 7
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 6, no REACH tag 5, LIVE+TEST_ONLY 3, LEGACY_ONLY+LIVE 2, TEST_ONLY 1, LEGACY_ONLY+LIVE+TEST_ONLY 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-02-02: REM-1, REM-2°
- DEL-03-01: REM-1
- DEL-04-04: SEC-1°, SEC-2, REM-1°
- DEL-04-05: CLM-022.4, REM-1, REGISTER-4, STATE-1
- DEL-05-01: CLM-003°, CLM-004°, CLM-006°, CLM-009°, CLM-010.1°, CLM-010.4°, CLM-010.14°, CLM-013°, CLM-016°, CLM-018°, CLM-024°, CLM-025°, CLM-027, CLM-032
- DEL-05-05: CLM-010.12°, CLM-012.8°, REM-1
- DEL-06-03: CLM-010.15
- DEL-07-01: SEC-1°, SEC-2°, REM-1
- DEL-08-02: REM-1
- DEL-08-04: CLM-011°, CLM-030°, REM-1
- DEL-09-06: CLM-014, CLM-021°, REM-4
- DEL-10-01: CLM-016.1°
- SOW: SOW:SOW-059.2, SOW:SOW-084.2
