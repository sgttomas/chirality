# Dependency Closure Report

## Verdict

RUN_STATUS = OK

Strict all-active DAG verdict = CYCLIC

Blocker-subset verdict = ACYCLIC

## Evidence Summary

| Check | Result |
|---|---:|
| `Dependencies.csv` files | 51 |
| Schema valid | 51 |
| Schema invalid | 0 |
| Total dependency rows | 554 |
| ANCHOR rows | 244 |
| EXECUTION rows | 310 |
| Evidence populated | 554 / 554 |
| Graph nodes | 46 |
| Graph edges | 114 |
| Strict SCCs | 2 |
| Strict SCC sizes | 18, 2 |
| Bidirectional pairs | 13 |
| ID normalizations | 0 |
| Blocker-subset SCCs | 0 |

## Ruling

The canonical dependency ID migration is graph-neutral. No dependency edge semantics were changed by this closure snapshot.

Strict project-wide `BLOCKED/UNBLOCKED` state must still not be reported because the strict all-active execution graph remains cyclic.

The blocker-subset remains acyclic after CODEV-001 and ID canonicalization.

## Remaining SCCs

- SCC-001: Runtime / SDK / Session / Tooling, 18 nodes.
- SCC-002: PKG-10 Policy / Proposal Pair, 2 nodes.

Next reconciliation work should triage SCC-002 first, then produce a focused ruling workbook for SCC-001.

