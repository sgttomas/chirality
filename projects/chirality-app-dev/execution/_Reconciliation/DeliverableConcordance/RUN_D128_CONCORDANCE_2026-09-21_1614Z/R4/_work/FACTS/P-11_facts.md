# Fact sheet P-11 (cluster CL-11) — Unframed owner questions (plain R4)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Rows needing an owner ruling that no named question frames (T1 themes: replay continuation versus the read-only lens; D-GOV-43 topology carriers; Runtime session-store contract; SCA-APP-010 presentation versus later direction; ruling-versus-ruling or TYPES; event registry drift; singletons). Which owner question does each theme put?

## Counts — PRIMARY rows (26)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  |  | 1 |  |  | 1 |
| PKG-02 | 1 | 1 |  |  |  | 1 | 3 |
| PKG-03 |  | 1 |  |  |  |  | 1 |
| PKG-04 |  |  | 1 |  | 1 |  | 2 |
| PKG-05 | 5 | 3 | 1 |  |  | 1 | 10 |
| PKG-06 |  | 2 |  |  |  | 1 | 3 |
| PKG-08 | 2 | 3 |  |  |  |  | 5 |
| PKG-09 |  |  | 1 |  |  |  | 1 |
| **Total** | **8** | **10** | **3** | **1** | **1** | **3** | **26** |

## Counts — ALSO/CONTEXT members (22; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| PKG-02 | 3 |  |  |  | 3 |
| PKG-05 | 2 |  |  |  | 2 |
| PKG-06 |  |  |  | 1 | 1 |
| PKG-08 | 1 |  | 1 | 3 | 5 |
| PKG-09 | 2 | 1 | 2 | 4 | 9 |
| PKG-10 |  |  |  | 2 | 2 |
| **Total** | **8** | **1** | **3** | **10** | **22** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 15, `LOCAL_DESIGN` 11
- PRIMARY HumanDecisionNeeded: `R4` 26
- PRIMARY CauseTag: `V3_RELEASE_SCOPE` 12, `A2_TOPOLOGY` 4, `PRE_V3_DRIFT` 4, `CODEX_SOLE_ENGINE` 2, `CARRIER_PROPAGATION` 2, `RUNTIME_EXTRACTION` 1, `OTHER:LOOP_WORKGRAPH_TRANSITION` 1
- PRIMARY LatestDecision: `NONE_FOUND` 5, `D-APP-74` 5, `D-APP-74 (context)` 4, `D-APP-108` 3, `D-APP-73 (context)` 2, `D-APP-127 (context)` 2, `D-APP-127` 2, `D-APP-40` 1, `D-GOV-43` 1, `D-APP-112` 1
- PRIMARY ClaimType: `REQUIREMENT` 16, `STATE_ASSERTION` 5, `REMAINING_WORK` 4, `ACCEPTANCE` 1
- PRIMARY Confidence: `MEDIUM` 21, `HIGH` 4, `LOW` 1
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 16, LEGACY_ONLY+LIVE 5, LIVE+TEST_ONLY 3, no REACH tag 2

## Contested or flagged members

- `DEL-06-04#STATE-2` (PRIMARY; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: Disposition checked `AUTHORITY_CONFLICT`; readings: STALE_SPECIFICATION — Reading A: projects/chirality-app-dev/docs/CONTRACT.md:17 (preamble, D-GOV-43) names K-RELEASE-1 ("read with D-GOV-43 items 1 and 4") and 
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): SPOT_UNDECIDED S2-031: HumanDecisionNeeded checked `R4`; readings: NO — Follows the Disposition: NO (or D-GOV-43) under reading A; R4 under reading B
- `DEL-09-04#CLM-022` (ALSO; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-09-04#CLM-023.3` (ALSO; now AUTHORITY_CONFLICT / HDN R4): RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)
- `DEL-10-01#REM-1` (ALSO; now AUTHORITY_CONFLICT / HDN R4; R4-Q6): SPOT_UNDECIDED S3-002: HumanDecisionNeeded checked `R4; R4-Q6`; readings: R4 — Row turns on projects/chirality-app-dev/docs/DIRECTIVE.md:320-330 (s.8 per-user daemon, D-GOV-20) versus D-GOV-43 A2. Reading A: s.8 is not among the claus
- `DEL-10-04#CLM-016.1` (ALSO; now AUTHORITY_CONFLICT / HDN R4; R4-Q1): SPOT_UNDECIDED S2-047: Disposition checked `AUTHORITY_CONFLICT`; readings: — Not settled in budget. Reading A: D-APP-56 R4-P27 assigns pec.yaml ownership to DEL-10-04 while PEC-loop commits b1074e7a4/ca49b846d author it under D-APP-70 

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-112.2
- DEL-02-01: REM-7
- DEL-02-02: SEC-3°, SEC-4°, REM-1°, REM-3
- DEL-02-05: SEC-2.2
- DEL-03-04: CLM-009.7
- DEL-04-01: CLM-009, STATE-1
- DEL-05-01: CLM-010.2, CLM-010.3°, CLM-014.2, REM-1, STATE-1
- DEL-05-04: CLM-004.2, CLM-010.14, CLM-010.15, CLM-010.19, CLM-013.2°, CLM-017, REM-2
- DEL-06-04: STATE-2
- DEL-06-06: CLM-027, CLM-030, STATE-1°
- DEL-08-02: CLM-003.5, CLM-005.4, CLM-009.11, CLM-009.18, CLM-009.19, CLM-012.2°, REMTXT-1°
- DEL-08-05: CLM-006°, CLM-012.1°, CLM-012.2°
- DEL-09-04: CLM-016°, CLM-017°, CLM-022°, CLM-023.3°
- DEL-09-05: CLM-016.3°, CLM-016.6°, CLM-020°, CLM-023.2°, CLM-026°, CLM-027
- DEL-10-01: REM-1°
- DEL-10-04: CLM-016.1°
