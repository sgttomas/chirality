# TM-PEC-013 WORKING_ITEMS activation and work graph

## Activation

| Field | Value |
|---|---|
| RunID | `TM-PEC-013-CURRENCY-REPAIR-2026-08-09` |
| Parent | HELP_HUMAN / owner-directed session |
| Accepted repository basis | `origin/main@d269f0e04204bc463a11684499213b2283bd28f7` |
| Branch | `codex/pec-currency-repair-20260809` |
| Authority | owner direction dated 2026-08-09; routed handoff `_DomainEngines/pec/_TaskManagement/HANDOFF_TM-PEC-013_SCA004_SOW_CURRENCY.md` |
| Objective | Produce three independent, minimal OI-003-currency successor SOW candidates and exact successor-bound REVIEW checklists |
| Exclusions | REVIEW, REVIEW_TYPE selection, lifecycle, dependencies, source, Task Management rows, receipts, standing plan, PRD, other coordination surfaces, Git state acts |

The route prescribes three independent legacy one-deliverable cycles. They are
kept distinct below; no package-wide lifecycle, production, or review fan-in is
claimed.

## Frozen work graph v1

**Selection authority:** owner direction dated 2026-08-09.

**Posture:** three independent terminal producer/validation cycles.
**Concurrency:** semantically eligible because writes are disjoint; executed
serially so each successor hash could bind its own deterministic checklist and
return evidence before the next cycle closed.

| Cycle | Package / deliverable | Producer write owner | Validation return | Dependencies | Fan-in gate |
|---|---|---|---|---|---|
| C1 | PKG-02 / DEL-02-07 | WORKING_ITEMS; exact target SOW only | SOW_V1 result, semantic-diff inspection, exact checklist | Accepted revision 1.4 plus routed handoff | successor and checklist source hashes equal |
| C2 | PKG-03 / DEL-03-01 | WORKING_ITEMS; exact target SOW only | SOW_V1 result, TBD-005/dependency preservation, exact checklist | Accepted revision 1.4 plus routed handoff | successor and checklist source hashes equal |
| C3 | PKG-04 / DEL-04-01 | WORKING_ITEMS; exact target SOW only | SOW_V1 result, three-edge/no-DEL-01-06 preservation, exact checklist | Accepted revision 1.4 plus routed handoff | successor and checklist source hashes equal |

There are no edges among C1, C2, and C3. Cross-cycle synthesis is limited to
this evidence return. Each later REVIEW remains a separate one-deliverable
owner-gated cycle.
