# Fact sheet P-16 (cluster CL-16) — Live path: legacy-session migration inert

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Legacy-session migration is inert for App-bootstrapped projects (no legacySessionRoots written) and no unit names who declares them (XPF-045). What is to change, and in which surface?

## Counts — PRIMARY rows (8)

| Package | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|
| PKG-01 | 4 | 4 |
| PKG-05 | 4 | 4 |
| **Total** | **8** | **8** |

## Counts — ALSO/CONTEXT members (6; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Total |
|---|---:|---:|---:|---:|
| PKG-03 |  | 1 |  | 1 |
| PKG-05 | 2 | 2 | 1 | 5 |
| **Total** | **2** | **3** | **1** | **6** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 6, `LOCAL_DESIGN` 1, `NOT_APPLICABLE` 1
- PRIMARY HumanDecisionNeeded: `NO` 8
- PRIMARY CauseTag: `RUNTIME_EXTRACTION` 8
- PRIMARY LatestDecision: `D-APP-127` 4, `D-APP-73 (context)` 3, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 7, `REGISTER_DEFECT` 1
- PRIMARY Confidence: `HIGH` 6, `MEDIUM` 2
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LIVE 7, LEGACY_ONLY+LIVE 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-01-01: CLM-005, CLM-009.5, CLM-016
- DEL-01-02: CLM-006.2
- DEL-03-02: CLM-004°
- DEL-05-01: CLM-010.3°, CLM-013°, CLM-014.2°, REM-1°
- DEL-05-04: CLM-003.1, CLM-010.9, CLM-018°, CLM-024, REGISTER-3
