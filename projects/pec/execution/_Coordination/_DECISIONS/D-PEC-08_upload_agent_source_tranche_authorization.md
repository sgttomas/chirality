# D-PEC-08 - PROPOSAL: upload-agent source-tranche authorization

**Status:** RULED (O-A, 2026-07-05).
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-08
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04).
**Ruling SHA:** `563a968d3`

## Ruling (2026-07-05)

Owner ruling of record (verbatim, 2026-07-05, in-session steer, Ryan Tufts):

> I authorize `D-PEC-08` with `O-A` for preparation/execution of a bounded upload-agent
> source tranche, limited to an exact file fence, tests, deferred D-PEC-07 obligations
> RV-13 through RV-21, and rollback/verification plan.

Scope of the ruling as given: O-A opens a bounded source tranche whose exact
file fence, tests, RV-13..21 obligation handling, and rollback/verification
plan are named in the tranche packet
`projects/pec/execution/_Coordination/TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md`
prepared and executed under this same ruling. Everything outside that fence
remains closed under F-PEC-1..4; `force=true` remains prohibited in agent runs;
no Gate-2, L3-beyond-this-design, pilot-readiness, or go-live implication.

## Owner ruling that opened this row

Owner ruling of record (verbatim, 2026-07-05, in-session, Ryan Tufts):

> S-4 (register rows): affirmed. Because I adopt the brief this session, open D-PEC-08
> scoped to the remaining gate only — the source-tranche authorization for the upload-agent
> implementation — AWAITING_RULING. Open D-PEC-09 for the CSV formula-injection repair,
> AWAITING_RULING and design-only; it authorizes no source change.

## Decision to rule

Whether to authorize a future source-change tranche implementing the adopted
PEC embedded upload-agent design brief:
`_DomainEngines/proposals/pec/BRIEF_2026-07-05_embedded_upload_agent_design.md`.

## Scope boundary

This packet is an open gate only. It authorizes no implementation, no tranche
request, and no pec source write. F-PEC-1 remains closed unless and until the
owner separately rules this row and names an exact source fence.

Structure precedent: this packet follows the PEC-local residual-work row
convention in `_REGISTER.md` and the decision-packet pattern used by D-PEC-06
and D-PEC-07.

Any future tranche packet must carry the brief's deferred obligations,
including RV-13 through RV-21 from
`projects/pec/execution/_Coordination/REVIEW_2026-07-05_D-PEC-07_artifacts.md`.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Authorize a bounded source tranche. | Opens only the source paths, tests, and implementation steps named in a later tranche packet or ruling. |
| O-B | Defer. | The adopted brief remains design authority only; no implementation proceeds. |

## Recommendation (non-binding)

Defer until a tranche packet is prepared with exact file fence, tests, deferred
obligation handling, and rollback/verification plan.
