# Work Graph v1 — D-GOV-16 Ruling Publication

| Node | Owner | Depends on | Write scope | Gate |
|---|---|---|---|---|
| R1 | HELPS_HUMANS | approved proposal snapshot | D-GOV-16 decision/register, D-GOV-16 package status, root receipt/handoff, this run's return | exact 1–10 ruling; no Stage-2 implementation |
| R2 | HELP_HUMAN | R1 | none | hashes, references, status, containment, checks PASS |
| R3 | CHANGE | R2 | Git commits plus SHA-binding handoff amendments | scoped commits; no merge/push/rebase/reset |
| R4 | HELP_HUMAN | R3 | plan/handoff status only if required | clean stop; synchronized-main planning gate named |

No nodes may run concurrently because all publication surfaces share the same
governance authority boundary.
