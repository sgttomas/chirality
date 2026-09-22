# Fact sheet P-12 (cluster CL-12) — Live path: unredacted event storage (K-EVENT-6)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** The live Runtime event store persists and streams raw Codex notification params with no structural secret redaction that amended K-EVENT-6 requires (XPF-041). What is to change, and in which surface?

## Counts — PRIMARY rows (25)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| PKG-01 |  | 2 |  |  |  | 2 |
| PKG-02 |  | 3 |  |  |  | 3 |
| PKG-03 |  | 4 |  |  |  | 4 |
| PKG-04 |  | 1 |  |  |  | 1 |
| PKG-05 |  | 6 |  | 5 | 1 | 12 |
| PKG-06 | 2 |  | 1 |  |  | 3 |
| **Total** | **2** | **16** | **1** | **5** | **1** | **25** |

## Counts — ALSO/CONTEXT members (32; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT |  | 1 |  |  |  |  | 1 |
| PKG-01 |  |  |  |  |  | 1 | 1 |
| PKG-03 |  | 2 |  |  |  |  | 2 |
| PKG-04 |  | 1 | 1 | 2 |  | 1 | 5 |
| PKG-05 | 6 | 6 | 1 | 5 | 1 |  | 19 |
| PKG-06 |  | 1 | 1 |  |  |  | 2 |
| PKG-08 |  | 2 |  |  |  |  | 2 |
| **Total** | **6** | **13** | **3** | **7** | **1** | **2** | **32** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 24, `PRD` 1
- PRIMARY HumanDecisionNeeded: `NO` 25
- PRIMARY CauseTag: `RUNTIME_EXTRACTION` 12, `CREDENTIAL_CUSTODY` 6, `CODEX_SOLE_ENGINE` 2, `CARRIER_PROPAGATION` 2, `PRE_V3_DRIFT` 2, `A2_TOPOLOGY` 1
- PRIMARY LatestDecision: `D-APP-127 (context)` 12, `D-GOV-43 (context)` 3, `D-APP-127` 3, `D-GOV-43` 3, `D-APP-67` 2, `NONE_FOUND` 1, `D-APP-38 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 21, `ACCEPTANCE` 2, `REMAINING_WORK` 1, `STATE_ASSERTION` 1
- PRIMARY Confidence: `MEDIUM` 17, `LOW` 5, `HIGH` 3
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 13, LEGACY_ONLY+LIVE 9, no REACH tag 2, TEST_ONLY 1

## Contested or flagged members

- `DEL-04-05#CLM-009.14` (ALSO; now IMPLEMENTED_DIFFERENTLY / HDN R4-Q1; R4-Q5): SPOT_REFUTED S1-055: Disposition checked `IMPLEMENTED_DIFFERENTLY`, checker proposes `AUTHORITY_CONFLICT`

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-02: CLM-006.12, CLM-018.5°, CLM-018.19
- DEL-02-05: CLM-004.4, CLM-010.9, CLM-011.4
- DEL-03-01: CLM-009.10°, CLM-009.13°, CLM-018.7
- DEL-03-04: CLM-004.6, CLM-009.13, CLM-011
- DEL-04-03: CLM-004.5, CLM-009.12°
- DEL-04-05: CLM-003°, CLM-009.14°, CLM-009.17°, CLM-026°
- DEL-05-02: CLM-010.9°, CLM-022, REM-1
- DEL-05-03: CLM-003°, CLM-006, CLM-010.1, CLM-010.6°, CLM-010.7°, CLM-010.11, CLM-010.12, CLM-011, CLM-012, CLM-022, CLM-023, CLM-024, REM-1°, REGISTER-5°
- DEL-05-04: CLM-003.3°, CLM-006°, CLM-010.8°, CLM-011, CLM-016°, CLM-017°, CLM-018°, REGISTER-2°
- DEL-05-05: CLM-003°, CLM-004°, CLM-010.6°, CLM-010.7°, CLM-023°, CLM-028°
- DEL-06-06: CLM-004.4, CLM-010.11, CLM-010.12, CLM-015.1°, CLM-030°
- DEL-08-05: CLM-004°, CLM-012.9°
- DOC:RELIANCE: 3.13°
