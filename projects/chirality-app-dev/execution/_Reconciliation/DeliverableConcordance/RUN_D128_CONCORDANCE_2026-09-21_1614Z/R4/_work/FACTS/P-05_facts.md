# Fact sheet P-05 (cluster CL-05) — R4-Q5: Codex event payloads stored as received or translated

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** R4-Q5: are Codex event payloads stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3)?

## Counts — PRIMARY rows (53)

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 |  | 9 | 5 |  | 1 | 16 |
| PKG-01 |  |  | 2 |  |  | 1 | 3 |
| PKG-02 |  |  |  |  | 3 | 4 | 7 |
| PKG-03 |  |  | 3 |  |  | 8 | 11 |
| PKG-04 |  |  |  | 1 |  |  | 1 |
| PKG-05 |  | 3 | 1 | 5 | 2 |  | 11 |
| PKG-09 |  | 2 |  | 1 |  | 1 | 4 |
| **Total** | **1** | **5** | **15** | **12** | **5** | **15** | **53** |

## Counts — ALSO/CONTEXT members (12; these rows are decided in their own PRIMARY packet)

| Package | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|
| PKG-01 | 3 | 3 |
| PKG-02 | 1 | 1 |
| PKG-03 | 6 | 6 |
| PKG-04 | 1 | 1 |
| PKG-09 | 1 | 1 |
| **Total** | **12** | **12** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 45, `PRD` 5, `NOT_APPLICABLE` 2, `LOCAL_DESIGN` 1
- PRIMARY HumanDecisionNeeded: `R4-Q5` 31, `R4-Q1; R4-Q5` 13, `R4-Q2; R4-Q5` 8, `D-APP-117; R4-Q5` 1
- PRIMARY CauseTag: `CODEX_SOLE_ENGINE` 39, `A2_TOPOLOGY` 9, `RUNTIME_EXTRACTION` 2, `CARRIER_PROPAGATION` 1, `DOC_HYGIENE` 1, `NONE` 1
- PRIMARY LatestDecision: `D-GOV-43 (context)` 19, `D-GOV-43` 16, `D-APP-127 (context)` 8, `D-APP-127` 4, `D-APP-42` 3, `NONE_FOUND` 2, `D-APP-38` 1
- PRIMARY ClaimType: `REQUIREMENT` 42, `STATE_ASSERTION` 6, `REMAINING_WORK` 2, `CONTEXT_CLAIM` 1, `ACCEPTANCE` 1, `REGISTER_DEFECT` 1
- PRIMARY Confidence: `MEDIUM` 43, `LOW` 7, `HIGH` 3
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 19, LEGACY_ONLY+LIVE 17, LEGACY_ONLY+LIVE+TEST_ONLY 7, LIVE+TEST_ONLY 5, LEGACY_ONLY 2, TEST_ONLY 1, no REACH tag 1, LEGACY_ONLY+TEST_ONLY 1

## Contested or flagged members

- `DEL-02-05#CLM-003.2` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-052: Disposition checked `AUTHORITY_CONFLICT`, checker proposes `ALIGNED`
- `DEL-02-05#CLM-003.2` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-052: HumanDecisionNeeded checked `R4-Q5`, checker proposes `NO`
- `DEL-02-05#CLM-011.3` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-038: Disposition checked `AUTHORITY_CONFLICT`, checker proposes `ALIGNED`
- `DEL-02-05#CLM-011.3` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4-Q5): SPOT_REFUTED S2-038: HumanDecisionNeeded checked `R4-Q5`, checker proposes `NO`
- `DEL-02-05#CLM-025` (PRIMARY; now STALE_SPECIFICATION / HDN R4-Q1; R4-Q5): SPOT_UNDECIDED S1-035: Disposition checked `STALE_SPECIFICATION`; readings: STALE_SPECIFICATION/NOT_AUDITABLE — CONTEXT_CLAIM trade-off (ScopeOfWork.md:460) 'Preserve browser-facing SSE names while runtime internals move behind TurnEngi
- `DEL-04-05#CLM-009.14` (PRIMARY; now IMPLEMENTED_DIFFERENTLY / HDN R4-Q1; R4-Q5): SPOT_REFUTED S1-055: Disposition checked `IMPLEMENTED_DIFFERENTLY`, checker proposes `AUTHORITY_CONFLICT`

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-01: CLM-009.7°, CLM-021.5°, CLM-023°
- DEL-01-02: CLM-006.1, CLM-018.4, CLM-018.5
- DEL-02-02: REM-2
- DEL-02-05: CLM-003.2, CLM-005.5, CLM-009°, CLM-010.7, CLM-011.3, CLM-023, CLM-025
- DEL-03-01: CLM-004.1°, CLM-004.6°, CLM-009.2°, CLM-009.7°, CLM-009.13, CLM-011.1, CLM-013.2, CLM-018.2, CLM-022.1, CLM-022.5
- DEL-03-02: CLM-009.10, CLM-021.2
- DEL-03-03: CLM-003.6°, CLM-005.3, CLM-009.6, CLM-023.3°
- DEL-03-04: CLM-022.4
- DEL-04-05: CLM-009.14, CLM-026°
- DEL-05-02: CLM-010.12
- DEL-05-03: CLM-003, CLM-010.7, REM-1, REGISTER-5
- DEL-05-04: CLM-010.7
- DEL-05-05: CLM-010.2, CLM-010.4, CLM-022, CLM-023, CLM-027
- DEL-09-02: CLM-010.3, CLM-010.9, CLM-010.10
- DEL-09-03: CLM-009.10, CLM-023°
- DOC:README: 0
- DOC:RELIANCE: 3.1, 3.3, 3.13, 4.1, 4.3, 4.13
- DOC:RQGATES: 5
- DOC:RUNTIME_ENGINE_CONTRACT: 0, 2, 4, 9
- DOC:TRACEABILITY: 2
- SOW: SOW:SOW-039, SOW:SOW-044.2, SOW:SOW-061.2
