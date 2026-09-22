# Fact sheet P-13 (cluster CL-13) — Live path: protected paths, instruction root and hooks (K-DOMAIN-2; PKG-06 path/hook rows)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Protected-path, instruction-root and hook guarantees exist only on the legacy path; nothing guards them on the live Codex path (XPF-042). What is to change, and in which surface?

## Counts — PRIMARY rows (25)

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Total |
|---|---:|---:|---:|---:|---:|
| PKG-06 |  |  | 1 |  | 1 |
| PKG-07 | 2 | 4 | 4 |  | 10 |
| PKG-10 |  |  | 5 | 9 | 14 |
| **Total** | **2** | **4** | **10** | **9** | **25** |

## Counts — ALSO/CONTEXT members (51; these rows are decided in their own PRIMARY packet)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| PKG-06 | 2 | 1 | 2 |  | 24 | 29 |
| PKG-07 | 10 |  | 1 |  | 5 | 16 |
| PKG-10 | 2 | 1 |  | 1 | 2 | 6 |
| **Total** | **14** | **2** | **3** | **1** | **31** | **51** |

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 21, `NOT_APPLICABLE` 4
- PRIMARY HumanDecisionNeeded: `NO` 25
- PRIMARY CauseTag: `LIFECYCLE_GATE_PENDING` 9, `PRE_V3_DRIFT` 7, `DOC_HYGIENE` 4, `A2_TOPOLOGY` 4, `FACADE_DEPRECATION` 1
- PRIMARY LatestDecision: `D-APP-37` 6, `D-APP-127 (context)` 4, `D-APP-49` 4, `D-APP-38` 2, `NONE_FOUND` 2, `D-APP-38 (context)` 2, `D-APP-56 (context)` 2, `D-APP-43` 1, `D-APP-45 (context)` 1, `D-APP-89 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 19, `STATE_ASSERTION` 2, `REGISTER_DEFECT` 2, `ACCEPTANCE` 1, `CONTEXT_CLAIM` 1
- PRIMARY Confidence: `MEDIUM` 16, `HIGH` 9
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 7, LEGACY_ONLY+LIVE+TEST_ONLY 5, LIVE+TEST_ONLY 4, TEST_ONLY 4, LIVE 3, LEGACY_ONLY+LIVE 1, LEGACY_ONLY+TEST_ONLY 1

## Contested or flagged members

- `DEL-07-01#CLM-011.4` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q1): SPOT_REFUTED S2-013: HumanDecisionNeeded checked `R4-Q1`, checker proposes `R4-Q1; R4-Q6`
- `DEL-10-02#CLM-024` (ALSO; now AUTHORITY_CONFLICT / HDN R4-Q1): SPOT_UNDECIDED S2-059: Disposition checked `AUTHORITY_CONFLICT`; readings: — Reading A: K-DOMAIN-2 hook enforcement exists only in legacy while D-GOV-43 removed Chirality hooks, AUTHORITY_CONFLICT. Reading B: the text is a trade-off fo

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-06-03: CLM-028
- DEL-06-04: CLM-003°, CLM-004.3°, CLM-005°, CLM-008°, CLM-009.1°, CLM-009.2°, CLM-009.3°, CLM-009.4°, CLM-009.6°, CLM-009.7°, CLM-009.13°, CLM-013°, CLM-018°, CLM-022°, CLM-025°, CLM-029°, CLM-030°
- DEL-06-05: CLM-009.12°, CLM-009.13°, CLM-018°, CLM-026°
- DEL-06-06: CLM-003.2°, CLM-005°, CLM-009°, CLM-010.5°, CLM-015.1°, CLM-020°, CLM-025.3°, CLM-032°
- DEL-07-01: SEC-2°, CLM-003°, CLM-004°, CLM-005°, CLM-011.4°, CLM-011.5°, CLM-011.7°, CLM-011.8°, CLM-019°, CLM-024°, CLM-025°, CLM-028°, CLM-029, REGISTER-5
- DEL-07-02: CLM-004.1, CLM-009.11°, CLM-014.2, CLM-017, CLM-018, CLM-024
- DEL-07-03: CLM-004, CLM-009.8, CLM-026
- DEL-07-05: CLM-004°, CLM-012.15°, CLM-027°
- DEL-10-01: CLM-004.4, CLM-012.7, CLM-025.2
- DEL-10-02: CLM-003.1, CLM-003.2, CLM-003.4, CLM-010.4, CLM-010.5, CLM-010.6, CLM-010.9°, CLM-010.11°, CLM-022, CLM-023, CLM-024°, REGISTER-4
- DEL-10-03: CLM-003.2°, CLM-010.8°
- DEL-10-04: CLM-003, CLM-010.5, CLM-028°
