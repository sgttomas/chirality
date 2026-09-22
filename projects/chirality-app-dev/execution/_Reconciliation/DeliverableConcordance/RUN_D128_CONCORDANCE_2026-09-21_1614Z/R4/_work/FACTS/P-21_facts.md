# Fact sheet P-21 (cluster CL-21) — A2 topology, Runtime extraction and facade deprecation

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Behaviour moved to the App-owned Runtime service and runtime-contracts (A2_TOPOLOGY, RUNTIME_EXTRACTION, FACADE_DEPRECATION, NATIVE_DELEGATION). How are these rows to be brought into agreement?

## Counts — PRIMARY rows (139)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 2 | 1 | 5 |  |  | 1 | 5 |  | 14 |
| PKG-01 |  |  | 3 | 2 |  |  |  |  | 5 |
| PKG-02 |  | 2 | 3 |  |  |  |  | 1 | 6 |
| PKG-03 | 5 | 11 | 34 | 1 |  |  |  |  | 51 |
| PKG-04 |  | 1 | 3 |  |  |  |  |  | 4 |
| PKG-05 | 5 |  | 16 |  |  | 3 |  |  | 24 |
| PKG-06 |  |  | 6 |  |  |  |  |  | 6 |
| PKG-08 |  |  | 3 |  |  |  |  |  | 3 |
| PKG-09 | 2 | 2 | 5 |  | 2 |  | 15 |  | 26 |
| **Total** | **14** | **17** | **78** | **3** | **2** | **4** | **20** | **1** | **139** |

## Counts — ALSO/CONTEXT members (172; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 1 | 7 | 1 |  |  | 1 |  | 11 |
| PKG-01 |  |  | 2 | 4 |  |  | 6 |  | 12 |
| PKG-02 |  |  |  | 1 |  |  | 4 |  | 5 |
| PKG-03 |  | 4 | 6 | 2 |  | 1 | 2 |  | 15 |
| PKG-04 |  | 6 | 2 | 5 |  | 1 |  |  | 14 |
| PKG-05 | 6 | 10 |  | 17 | 3 |  | 1 |  | 37 |
| PKG-06 | 3 |  | 5 | 2 | 1 |  | 2 |  | 13 |
| PKG-07 | 16 | 5 |  | 1 |  |  |  |  | 22 |
| PKG-08 |  | 3 | 7 | 4 |  | 3 |  |  | 17 |
| PKG-09 |  | 14 | 2 |  |  | 1 | 3 | 2 | 22 |
| PKG-10 |  |  | 1 | 2 |  |  | 1 |  | 4 |
| **Total** | **26** | **43** | **32** | **39** | **4** | **6** | **20** | **2** | **172** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 56, `LOCAL_DESIGN` 49, `NOT_APPLICABLE` 28, `PRD` 6
- PRIMARY HumanDecisionNeeded: `NO` 139
- PRIMARY CauseTag: `A2_TOPOLOGY` 86, `RUNTIME_EXTRACTION` 48, `FACADE_DEPRECATION` 5
- PRIMARY LatestDecision: `D-APP-127` 63, `D-APP-127 (context)` 26, `D-GOV-43` 13, `D-GOV-43 (context)` 10, `NONE_FOUND` 9, `D-APP-56` 5, `D-APP-108` 4, `D-APP-56 (context)` 2, `D-GOV-20 (context)` 2, `D-APP-89` 1, `D-APP-47` 1, `D-APP-40 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 75, `ACCEPTANCE` 23, `STATE_ASSERTION` 21, `CONTEXT_CLAIM` 11, `REGISTER_DEFECT` 6, `REMAINING_WORK` 2, `EXCLUSION` 1
- PRIMARY Confidence: `HIGH` 72, `MEDIUM` 58, `LOW` 9
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 70, LEGACY_ONLY+LIVE 36, no REACH tag 24, TEST_ONLY 5, LIVE+TEST_ONLY 3, LEGACY_ONLY 1

## Contested or flagged members

- `DEL-02-05#CLM-003.2` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-052: Disposition checked `AUTHORITY_CONFLICT`, checker proposes `ALIGNED`
- `DEL-02-05#CLM-003.2` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-052: HumanDecisionNeeded checked `R4-Q5`, checker proposes `NO`
- `DEL-02-05#CLM-011.3` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-038: Disposition checked `AUTHORITY_CONFLICT`, checker proposes `ALIGNED`
- `DEL-02-05#CLM-011.3` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-038: HumanDecisionNeeded checked `R4-Q5`, checker proposes `NO`
- `DEL-02-05#CLM-025` (ALSO; now STALE_SPECIFICATION / HDN R4-Q1; R4-Q5): SPOT_UNDECIDED S1-035: Disposition checked `STALE_SPECIFICATION`; readings: STALE_SPECIFICATION/NOT_AUDITABLE — CONTEXT_CLAIM trade-off (ScopeOfWork.md:460) 'Preserve browser-facing SSE names while runtime internals move behind TurnEngi
- `DEL-06-04#STATE-2` (ALSO; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: Disposition checked `AUTHORITY_CONFLICT`; readings: STALE_SPECIFICATION — Reading A: projects/chirality-app-dev/docs/CONTRACT.md:17 (preamble, D-GOV-43) names K-RELEASE-1 ("read with D-GOV-43 items 1 and 4") and 
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: HumanDecisionNeeded checked `R4`; readings: NO — Follows the Disposition: NO (or D-GOV-43) under reading A; R4 under reading B
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-09-04#CLM-023.3` (ALSO; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-10-01#REM-1` (ALSO; now AUTHORITY_CONFLICT / HDN R4; R4-Q6): SPOT_UNDECIDED S3-002: HumanDecisionNeeded checked `R4; R4-Q6`; readings: R4 — Row turns on projects/chirality-app-dev/docs/DIRECTIVE.md:320-330 (s.8 per-user daemon, D-GOV-20) versus D-GOV-43 A2. Reading A: s.8 is not among the claus

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-88, DEC:D-APP-100, DEC:D-APP-104, DEC:D-APP-107, DEC:D-APP-114.2
- DEL-01-01: CLM-005°, CLM-009.1, CLM-009.5°, CLM-011, CLM-016°
- DEL-01-02: CLM-006.2°, CLM-006.8°, CLM-007.5, CLM-018.16°, REM-1, STATE-2
- DEL-01-04: CLM-003.1°, CLM-003.4°, CLM-006.1°, CLM-010.2°, CLM-023°, CLM-024°
- DEL-02-01: REGISTER-6, REM-2
- DEL-02-04: REGISTER-7
- DEL-02-05: CLM-003.2°, CLM-005.5°, CLM-010.7°, CLM-010.10, CLM-011.3°, CLM-013.3, CLM-013.5, CLM-025°
- DEL-03-01: CLM-002, CLM-005.7, CLM-008, CLM-015, CLM-017, REM-2°, REGISTER-3, STATE-1
- DEL-03-02: CLM-003, CLM-004°, CLM-005, CLM-008, CLM-009.1, CLM-009.2°, CLM-009.3, CLM-009.5, CLM-009.8, CLM-011, CLM-012, CLM-015, CLM-016, CLM-017, CLM-020, CLM-021.1, CLM-021.3, CLM-022
- DEL-03-03: CLM-003.3°, CLM-004.4, CLM-005.1°, CLM-009.2°, CLM-009.4, CLM-023.2°, STATE-1, STATE-2
- DEL-03-04: CLM-002, CLM-003, CLM-004.2, CLM-004.6°, CLM-005, CLM-008, CLM-009.4, CLM-009.7°, CLM-009.10, CLM-009.11, CLM-009.12, CLM-009.13°, CLM-010.3, CLM-010.4°, CLM-011°, CLM-012°, CLM-013.1, CLM-013.2, CLM-016, CLM-017, CLM-018, CLM-019, CLM-022.3, CLM-022.4°, CLM-022.5, CLM-023, CLM-027, CLM-031, STATE-3°, STATE-4, STATE-5, REGISTER-3
- DEL-04-02: CLM-003°, CLM-010.1°, CLM-014°, CLM-028°
- DEL-04-03: CLM-003°, CLM-004.5°, CLM-008, CLM-009.4, STATE-1
- DEL-04-04: CLM-010.1°, CLM-010.4°, CLM-010.10°
- DEL-04-05: CLM-009.13, CLM-022.4°, REM-1°, REGISTER-4°, STATE-1°, STATE-3°
- DEL-05-01: CLM-010.10°, REM-1°, REGISTER-4, STATE-1°
- DEL-05-02: SEC-1, SEC-2, CLM-003, CLM-004, CLM-005, CLM-009, CLM-012, CLM-013, CLM-015, CLM-017, CLM-018, CLM-021, CLM-025, CLM-028, STATE-1
- DEL-05-03: CLM-010.1°, CLM-010.3°, CLM-010.5, CLM-010.6°, CLM-010.7°, CLM-010.11°, CLM-010.13°, CLM-012°, CLM-019, CLM-022°, CLM-023°, CLM-024°, REM-1°, REGISTER-5°
- DEL-05-04: CLM-003.1°, CLM-003.3°, CLM-004.1°, CLM-006°, CLM-009, CLM-010.1, CLM-010.8°, CLM-010.9°, CLM-010.10°, CLM-010.12°, CLM-010.13°, CLM-011°, CLM-012°, CLM-013.1°, CLM-013.2°, CLM-016°, CLM-017°, CLM-018°, CLM-019.1°, CLM-022°, CLM-023, CLM-024°, REGISTER-2°, REGISTER-3°
- DEL-05-05: CLM-009, CLM-010.1, CLM-016, CLM-026°
- DEL-06-01: CLM-002, CLM-008°, CLM-014, CLM-034.1°, CLM-034.2°
- DEL-06-02: CLM-035.1°, STATE-2°
- DEL-06-03: CLM-035.1°
- DEL-06-04: CLM-032.1°, CLM-032.2°, STATE-2°
- DEL-06-05: CLM-031.1°, REGISTER-4
- DEL-06-06: CLM-003.1, CLM-004.4°, CLM-010.11°, CLM-019, CLM-025.2, STATE-1°
- DEL-07-01: REM-1°
- DEL-07-02: CLM-003°, CLM-004.1°, CLM-005°, CLM-008°, CLM-009.1°, CLM-009.2°, CLM-009.3°, CLM-009.4°, CLM-009.5°, CLM-009.6°, CLM-009.7°, CLM-009.8°, CLM-009.9°, CLM-009.10°, CLM-009.12°, CLM-009.13°, CLM-010°, CLM-014.2°, CLM-018°, CLM-024°, CLM-029°
- DEL-08-01: CLM-009.12°, STATE-1
- DEL-08-04: CLM-003.2°, CLM-010.1°, CLM-010.2°, CLM-013°, CLM-021°, CLM-022.1°, CLM-024°, CLM-025°, CLM-026°, CLM-028°, REM-2°, REM-3°, STATE-1
- DEL-08-05: CLM-003°, CLM-013°, CLM-028°, REM-1°, STATE-1
- DEL-09-01: CLM-012, CLM-013, CLM-019, REM-1°
- DEL-09-02: CLM-010.4°, CLM-010.11°
- DEL-09-03: CLM-005.1, CLM-005.3°, CLM-009.1, CLM-009.5°, STATE-2
- DEL-09-04: SEC-1, CLM-004.4, CLM-005°, CLM-009.9, CLM-011.1°, CLM-011.2°, CLM-011.3°, CLM-011.4°, CLM-011.5°, CLM-011.7°, CLM-011.9, CLM-012.1°, CLM-016°, CLM-018°, CLM-022°, CLM-023.3°, STATE-51
- DEL-09-05: CLM-010.13°, CLM-016.3°, CLM-016.5°, CLM-016.6°
- DEL-09-06: CLM-016°
- DEL-09-07: SEC-1, SEC-2.1, SEC-2.2, SEC-2.3, SEC-2.4, SEC-2.5, SEC-2.6, SEC-2.7, SEC-2.8, SEC-3.1, SEC-3.2, SEC-3.3, SEC-3.4, SEC-4, STATE-3
- DEL-10-01: CLM-016.1°, REM-1°
- DEL-10-02: REGISTER-4°
- DEL-10-03: REGISTER-5°
- DOC:ADDING_A_TOOL: 6°
- DOC:BUILDREL: 4.13, 4.14°, 10.6
- DOC:RELIANCE: 3.3°, 3.9°, 4.3°, 4.9°, 11.5, 11.7, 11.8
- DOC:RUNTIME_ENGINE_CONTRACT: 5°
- DOC:TOOL_CATALOG: 2°
- SOW: SOW:SOW-024.2°, SOW:SOW-025.2°, SOW:SOW-056.2, SOW:SOW-064.2, SOW:SOW-075.2°, SOW:SOW-079.2, SOW:SOW-080
