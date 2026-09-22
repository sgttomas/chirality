# Fact sheet P-04 (cluster CL-04) — R4-Q6: unamended App DIRECTIVE and K-PERM-1/6 versus D-GOV-43

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** R4-Q6: do the unamended App DIRECTIVE clauses (§2.8, §2.10, §4.1, §4.2) and CONTRACT K-PERM-1/K-PERM-6 still bind the Codex-hosted App, or did D-GOV-43 supersede them (Anthropic API-key UI, the live "Full access" option, the unfiltered ~/.codex link, shared config, approval policy)? CONTEXT, NOT YET GOVERNING: the owner's recorded answer (OWNER_DIRECTION r2_r4q6_answer, RUN_BASIS Addendum 9) is that D-GOV-43 superseded those texts, Codex-hosted first, local models later, API no sooner. It becomes GOVERNING only when the R4 ruling records it; the packet asks the owner to confirm it with the row population below.

## Counts — PRIMARY rows (86)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| EXT |  |  |  | 8 | 8 |
| PKG-01 | 1 |  | 1 | 28 | 30 |
| PKG-02 | 2 | 1 |  | 10 | 13 |
| PKG-03 |  |  |  | 6 | 6 |
| PKG-04 |  |  | 1 | 2 | 3 |
| PKG-06 |  |  | 1 | 18 | 19 |
| PKG-09 | 1 |  | 1 | 4 | 6 |
| PKG-10 |  |  |  | 1 | 1 |
| **Total** | **4** | **1** | **4** | **77** | **86** |

## Counts — ALSO/CONTEXT members (0; these rows are decided in their own PRIMARY packet)

_none_

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 76, `PRD` 5, `LOCAL_DESIGN` 4, `NOT_APPLICABLE` 1
- PRIMARY HumanDecisionNeeded: `R4-Q1; R4-Q6` 46, `R4-Q6` 23, `R4-Q5; R4-Q6` 9, `R4-Q5; R4-Q1; R4-Q6` 3, `R4-Q6; R4-Q1` 3, `R4; R4-Q6` 2
- PRIMARY CauseTag: `CODEX_SOLE_ENGINE` 74, `A2_TOPOLOGY` 9, `CARRIER_PROPAGATION` 2, `CREDENTIAL_CUSTODY` 1
- PRIMARY LatestDecision: `D-GOV-43 (context)` 55, `D-APP-127` 12, `D-GOV-43` 9, `D-APP-127 (context)` 5, `D-APP-68` 2, `D-APP-44 (context)` 1, `D-APP-53 (context)` 1, `NONE_FOUND` 1
- PRIMARY ClaimType: `REQUIREMENT` 67, `STATE_ASSERTION` 7, `EXCLUSION` 6, `ACCEPTANCE` 3, `REGISTER_DEFECT` 1, `CONTEXT_CLAIM` 1, `REMAINING_WORK` 1
- PRIMARY Confidence: `MEDIUM` 70, `HIGH` 12, `LOW` 4
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LEGACY_ONLY+LIVE 51, LIVE 27, no REACH tag 4, LEGACY_ONLY 3, LEGACY_ONLY+LIVE+TEST_ONLY 1

## Contested or flagged members

- `DEL-10-01#REM-1` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4; R4-Q6): SPOT_UNDECIDED S3-002: HumanDecisionNeeded checked `R4; R4-Q6`; readings: R4 — Row turns on projects/chirality-app-dev/docs/DIRECTIVE.md:320-330 (s.8 per-user daemon, D-GOV-20) versus D-GOV-43 A2. Reading A: s.8 is not among the claus

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-01: CLM-009.7, CLM-021.5, CLM-023, STATE-1
- DEL-01-02: CLM-006.3, CLM-006.7, CLM-007.3, CLM-007.4, CLM-018.8, CLM-018.10, STATE-1, CLM-040, CLM-044
- DEL-01-03: CLM-024, STATE-1, STATE-3
- DEL-01-04: CLM-003.1, CLM-003.4, CLM-003.5, CLM-004.5, CLM-006.1, CLM-006.2, CLM-010.2, CLM-010.4, CLM-023, CLM-024, CLM-025, REGISTER-3, STATE-2, STATE-4
- DEL-02-05: SEC-2.3, CLM-003.1, CLM-004.2, CLM-005.1, CLM-005.2, CLM-009, CLM-010.1, CLM-010.2, CLM-010.3, CLM-010.4, CLM-011.2, CLM-012, CLM-018
- DEL-03-01: CLM-004.1, CLM-004.6, CLM-009.2, CLM-009.7
- DEL-03-03: CLM-003.6, CLM-023.3
- DEL-04-01: CLM-003
- DEL-04-05: CLM-009.10, CLM-026
- DEL-06-01: CLM-003, CLM-004, CLM-009.3, CLM-009.5, CLM-009.6, CLM-009.9, CLM-024, CLM-025, CLM-027, CLM-031, CLM-032
- DEL-06-03: CLM-004
- DEL-06-04: CLM-003, CLM-009.7, CLM-018, CLM-022
- DEL-06-05: CLM-004.2, CLM-022
- DEL-06-06: STATE-1
- DEL-09-02: CLM-010.6
- DEL-09-03: CLM-005.8, CLM-009.9, CLM-011, CLM-017, CLM-023
- DEL-10-01: REM-1
- DOC:RELIANCE: 3.4, 3.8, 4.4, 4.8
- SOW: SOW:SOW-045.2, SOW:SOW-050.2, SOW:SOW-075.2, SOW:SOW-076
