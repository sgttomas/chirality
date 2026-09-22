# Fact sheet P-02 (cluster CL-02) — Owner check: off-code events known only by absence of a record (Addendum 10)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Did the release, signing, notarization, publication, CI/release-job, attestation and manual steps these rows describe happen? The answers are collected by OWNER_CHECK.md before any R4 packet; rows are then dispositioned from the owner's answers, and an answer the owner cannot give stays UNKNOWN.

## Counts — PRIMARY rows (63)

| Package | Matches (`ALIGNED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 3 |  | 6 |  |  |  | 1 | 10 |
| PKG-00 |  |  |  |  |  |  | 2 | 2 |
| PKG-01 |  |  | 1 |  |  |  | 5 | 6 |
| PKG-02 |  |  |  |  |  |  | 5 | 5 |
| PKG-03 |  |  | 1 |  |  |  |  | 1 |
| PKG-05 |  |  |  | 1 |  |  | 2 | 3 |
| PKG-09 |  | 23 | 2 |  | 2 | 1 | 4 | 32 |
| PKG-10 |  |  |  | 1 |  |  | 3 | 4 |
| **Total** | **3** | **23** | **10** | **2** | **2** | **1** | **22** | **63** |

## Counts — ALSO/CONTEXT members (0; these rows are decided in their own PRIMARY packet)

_none_

- PRIMARY AuthorityTier: `LOCAL_DESIGN` 36, `GOVERNANCE_INVARIANT` 22, `NOT_APPLICABLE` 3, `PRD` 2
- PRIMARY HumanDecisionNeeded: `NO` 56, `R4-Q1` 3, `R4` 3, `D-APP-121` 1
- PRIMARY CauseTag: `DOC_HYGIENE` 16, `A2_TOPOLOGY` 15, `CODEX_SOLE_ENGINE` 13, `PRE_V3_DRIFT` 8, `CARRIER_PROPAGATION` 3, `LIFECYCLE_GATE_PENDING` 3, `NONE` 3, `UNRECORDED_JUDGMENT` 1, `V3_RELEASE_SCOPE` 1
- PRIMARY LatestDecision: `D-APP-127 (context)` 18, `NONE_FOUND` 16, `D-APP-127` 9, `D-GOV-43` 7, `D-APP-56 (context)` 5, `D-APP-56` 2, `D-APP-68 (context)` 1, `D-APP-68` 1, `D-APP-54 (context)` 1, `D-APP-121` 1, `D-GOV-16 (context)` 1, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `ACCEPTANCE` 35, `REQUIREMENT` 20, `STATE_ASSERTION` 5, `REMAINING_WORK` 2, `CONTEXT_CLAIM` 1
- PRIMARY Confidence: `MEDIUM` 40, `LOW` 13, `HIGH` 10
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 28, LIVE 17, TEST_ONLY 7, LIVE+TEST_ONLY 6, LEGACY_ONLY+LIVE+TEST_ONLY 2, LEGACY_ONLY 2, LEGACY_ONLY+TEST_ONLY 1

## Contested or flagged members

- `DEL-09-05#CLM-010.8` (PRIMARY; now PARTIALLY_IMPLEMENTED / HDN NO): R3_UNDECIDED: Addendum 10 (OC-05); current value stands, both readings in the R3 task files (R3_SUMMARY §8)

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-00-01: CLM-018.2
- DEL-00-02: CLM-021.2
- DEL-01-01: CLM-018
- DEL-01-02: CLM-038.4
- DEL-01-03: CLM-011, CLM-017, CLM-022
- DEL-01-04: CLM-020.2
- DEL-02-01: CLM-023.2
- DEL-02-02: CLM-021.2
- DEL-02-03: CLM-023.2
- DEL-02-04: CLM-021.2
- DEL-02-05: CLM-020.1
- DEL-03-02: CLM-018
- DEL-05-03: CLM-020.1
- DEL-05-04: CLM-019.2
- DEL-05-05: CLM-020.2
- DEL-09-01: CLM-009.8, CLM-011, CLM-023, REM-1
- DEL-09-02: CLM-020.2
- DEL-09-04: CLM-005, CLM-009.8, CLM-011.1, CLM-011.2, CLM-011.3, CLM-011.4, CLM-011.5, CLM-011.7, CLM-011.8, CLM-012.1, CLM-017, CLM-018, REM-1
- DEL-09-05: CLM-010.6, CLM-010.8, CLM-010.9, CLM-010.13, CLM-010.14, CLM-010.15, CLM-016.3, CLM-016.5, CLM-016.6, CLM-021, CLM-022, CLM-023.1
- DEL-09-06: CLM-016, CLM-021
- DEL-10-01: CLM-022.2
- DEL-10-02: CLM-019.2
- DEL-10-04: CLM-023.2
- DEL-10-05: CLM-020.1
- DOC:BUILDREL: 9.3, 9.5, 11, 12
- DOC:RELIANCE: 8, 11.1
- DOC:RQGATES: 12
- DOC:VALSTRAT: 4.11, 7, 8
