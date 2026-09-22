# Fact sheet P-03 (cluster CL-03) — Release signing posture and G6a (run-wide call f)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Does the amended CONTRACT preamble (with SPEC §19.4 and PRD §12.8) supersede the unsigned/unnotarized target of K-RELEASE-1, the D-APP-97 F-APP-2 signing fence and the G6a exact-candidate gate for DEL-09-04 and DEL-09-05? (Done-declaration Q-02 is CONTEXT.)

## Counts — PRIMARY rows (22)

| Package | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| EXT |  | 1 |  |  | 1 |
| PKG-09 | 1 | 16 | 1 | 3 | 21 |
| **Total** | **1** | **17** | **1** | **3** | **22** |

## Counts — ALSO/CONTEXT members (5; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|
| EXT |  | 1 |  | 1 |
| PKG-09 | 2 | 1 | 1 | 4 |
| **Total** | **2** | **2** | **1** | **5** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 18, `LOCAL_DESIGN` 2, `NOT_APPLICABLE` 2
- PRIMARY HumanDecisionNeeded: `NO` 16, `R4` 6
- PRIMARY CauseTag: `CARRIER_PROPAGATION` 16, `A2_TOPOLOGY` 4, `CODEX_SOLE_ENGINE` 1, `V3_RELEASE_SCOPE` 1
- PRIMARY LatestDecision: `D-APP-127` 14, `D-GOV-43` 6, `D-APP-127 (context)` 1, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 13, `ACCEPTANCE` 3, `STATE_ASSERTION` 3, `EXCLUSION` 1, `REMAINING_WORK` 1, `REGISTER_DEFECT` 1
- PRIMARY Confidence: `MEDIUM` 13, `HIGH` 7, `LOW` 2
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 16, no REACH tag 4, TEST_ONLY 1, LIVE+TEST_ONLY 1

## Contested or flagged members

- `DEL-09-04#CLM-022` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: Disposition checked `AUTHORITY_CONFLICT`; readings: STALE_SPECIFICATION — Reading A: projects/chirality-app-dev/docs/CONTRACT.md:17 (preamble, D-GOV-43) names K-RELEASE-1 ("read with D-GOV-43 items 1 and 4") and 
- `DEL-09-04#CLM-022` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: HumanDecisionNeeded checked `R4`; readings: NO — Follows the Disposition: NO (or D-GOV-43) under reading A; R4 under reading B
- `DEL-09-04#CLM-022` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-09-04#CLM-023.3` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-09-04: CLM-003.1, CLM-004.3, CLM-008, CLM-009.1, CLM-011.6, CLM-012.2, CLM-016, CLM-017°, CLM-022, CLM-023.3
- DEL-09-05: CLM-003, CLM-009, CLM-010.6°, CLM-010.7, CLM-012, CLM-013, CLM-016.3°, CLM-016.6°, STATE-1, CLM-020, CLM-023.2, CLM-026, REM-2, REGISTER-52, STATE-52
- DOC:BUILDREL: 4.14, 11°
