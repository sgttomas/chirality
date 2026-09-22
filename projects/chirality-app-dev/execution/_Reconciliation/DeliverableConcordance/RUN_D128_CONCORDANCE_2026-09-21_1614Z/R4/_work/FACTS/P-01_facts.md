# Fact sheet P-01 (cluster CL-01) — Owner-deferred DEL-06-02 keys (Addendum 5)

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** The owner reserved these two keys: worker A read IMPLEMENTED_DIFFERENTLY and worker B STALE_SPECIFICATION (or the reverse). Which reading stands, after the owner reviews the surrounding context?

## Counts — PRIMARY rows (2)

| Package | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|---:|
| PKG-06 | 1 | 1 | 2 |
| **Total** | **1** | **1** | **2** |

## Counts — ALSO/CONTEXT members (0; these rows are decided in their own PRIMARY packet)

_none_

- PRIMARY AuthorityTier: `GOVERNANCE_INVARIANT` 1, `LOCAL_DESIGN` 1
- PRIMARY HumanDecisionNeeded: `R4-Q1` 2
- PRIMARY CauseTag: `PRE_V3_DRIFT` 1, `CODEX_SOLE_ENGINE` 1
- PRIMARY LatestDecision: `NONE_FOUND` 1, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 1, `ACCEPTANCE` 1
- PRIMARY Confidence: `HIGH` 1, `MEDIUM` 1
- PRIMARY reach mix (REACH tags in ImplementationEvidence): LEGACY_ONLY 1, LEGACY_ONLY+LIVE 1

## Contested or flagged members

- `DEL-06-02#CLM-005` (PRIMARY): AltReading: OWNER_DEFERRED (Addendum 5): worker B (PKG-06/DEL-06-02_B) Disposition=IMPLEMENTED_DIFFERENTLY; CauseTag=CODEX_SOLE_ENGINE; HumanDecisionNeeded=R4-Q1
- `DEL-06-02#CLM-032` (PRIMARY): AltReading: OWNER_DEFERRED (Addendum 5): worker B (PKG-06/DEL-06-02_B) Disposition=STALE_SPECIFICATION; CauseTag=PRE_V3_DRIFT; HumanDecisionNeeded=NO

## Members by deliverable (° = ALSO/CONTEXT)

- DEL-06-02: CLM-005, CLM-032
