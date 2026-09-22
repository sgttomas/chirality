# Fact sheet P-14 (cluster CL-14) — Live path: human gate and status transition

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** On the live status-transition route actor and approval SHA are caller-supplied and no live UI performs the human gate (XPF-043; see R4-Q3). What is to change, and in which surface?

## Counts — PRIMARY rows (13)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|---:|
| PKG-01 | 2 |  | 2 |
| PKG-07 | 4 | 6 | 10 |
| PKG-10 | 1 |  | 1 |
| **Total** | **7** | **6** | **13** |

## Counts — ALSO/CONTEXT members (44; these rows are decided in their own PRIMARY packet)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 4 |  |  |  |  | 5 |
| PKG-01 |  | 3 |  |  |  | 1 | 4 |
| PKG-04 |  | 1 |  |  |  |  | 1 |
| PKG-06 |  | 2 | 2 | 4 | 1 | 5 | 14 |
| PKG-07 | 5 | 12 |  | 1 |  | 1 | 19 |
| PKG-08 |  |  |  | 1 |  |  | 1 |
| **Total** | **6** | **22** | **2** | **6** | **1** | **7** | **44** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 9, `NOT_APPLICABLE` 4
- PRIMARY HumanDecisionNeeded: `NO` 13
- PRIMARY CauseTag: `PRE_V3_DRIFT` 6, `DOC_HYGIENE` 5, `CODEX_SOLE_ENGINE` 1, `CARRIER_PROPAGATION` 1
- PRIMARY LatestDecision: `NONE_FOUND` 6, `D-APP-56 (context)` 3, `D-APP-38` 2, `D-APP-38 (context)` 1, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 6, `ACCEPTANCE` 3, `STATE_ASSERTION` 2, `CONTEXT_CLAIM` 1, `REGISTER_DEFECT` 1
- PRIMARY Confidence: `MEDIUM` 7, `HIGH` 4, `LOW` 2
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 5, LIVE 5, LEGACY_ONLY+LIVE 3

## Contested or flagged members

- `DEL-06-04#CLM-027` (ALSO; now STALE_SPECIFICATION / HDN R4-Q1): SPOT_REFUTED S1-112: Disposition checked `STALE_SPECIFICATION`, checker proposes `IMPLEMENTED_DIFFERENTLY`

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-01: CLM-004.4°, CLM-009.6°
- DEL-01-02: CLM-036, CLM-043°
- DEL-01-03: CLM-004, CLM-024°
- DEL-04-04: CLM-010.7°
- DEL-06-03: CLM-009°, CLM-028°
- DEL-06-04: CLM-004.4°, CLM-004.5°, CLM-008°, CLM-009.4°, CLM-009.10°, CLM-009.15°, CLM-011°, CLM-012°, CLM-018°, CLM-019.1°, CLM-027°, CLM-030°
- DEL-07-03: CLM-004°, CLM-017
- DEL-07-04: CLM-005°, CLM-008, CLM-010°, CLM-011.2, CLM-011.4, CLM-011.5°, CLM-011.9°, CLM-011.10°, CLM-011.11°, CLM-011.12°, CLM-011.13°, CLM-011.15°, CLM-011.16, CLM-013.5°, CLM-013.6°, CLM-013.7°, CLM-013.9, CLM-013.10°, CLM-013.12°, CLM-014°, CLM-016°, CLM-020°, CLM-028°, CLM-032, REGISTER-2
- DEL-07-06: CLM-018, CLM-025
- DEL-08-04: CLM-011°
- DEL-10-05: CLM-009.1
- DOC:ADDING_A_TOOL: 4°
- DOC:RELIANCE: 3.6°, 3.10°, 4.6°, 4.10°
