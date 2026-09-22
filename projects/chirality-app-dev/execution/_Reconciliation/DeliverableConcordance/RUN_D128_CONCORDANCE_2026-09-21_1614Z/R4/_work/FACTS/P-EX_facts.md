# Fact sheet P-EX (cluster CL-EX) — Exceptions

Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.

## R3 cluster text

**Question.** Rows in scope that no cluster above takes (for example UNRECORDED_JUDGMENT, OTHER: cause tokens, or a divergent row with CauseTag NONE). Each needs its own look in R4.

## Counts — PRIMARY rows (3)

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Agent-instruction matter (`DEFERRED_AGENT_WORKFLOW`) | Total |
|---|---:|---:|---:|---:|
| EXT | 1 | 1 | 1 | 3 |
| **Total** | **1** | **1** | **1** | **3** |

## Counts — ALSO/CONTEXT members (0; these rows are decided in their own PRIMARY packet)

_none_

- PRIMARY AuthorityTier: `LOCAL_DESIGN` 1, `PRD` 1, `NOT_APPLICABLE` 1
- PRIMARY HumanDecisionNeeded: `NO` 3
- PRIMARY CauseTag: `UNRECORDED_JUDGMENT` 1, `OTHER:WORKFLOW_CONVENTION` 1, `OTHER:DUPLICATE_TEST_RETIREMENT` 1
- PRIMARY LatestDecision: `D-APP-99` 1, `NONE_FOUND` 1, `D-GOV-43 (context)` 1
- PRIMARY ClaimType: `REQUIREMENT` 2, `STATE_ASSERTION` 1
- PRIMARY Confidence: `MEDIUM` 2, `LOW` 1
- PRIMARY reach mix (REACH tags in ImplementationEvidence): no REACH tag 2, TEST_ONLY 1

## Contested or flagged members

_none_

## Members by deliverable (° = ALSO/CONTEXT)

- DEC: DEC:D-APP-99
- DOC:RQRUN: 2
- SOW: SOW:SOW-033.2
