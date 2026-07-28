# OD7-G3 EH-D — Event-Contract Home Deferral Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-EH-D`
**Provisional PEC carrier:** `D-PEC-67`

## Exact candidate disposition

Defer selection of the canonical home for PEC v2 coordination-event
contracts. Keep `SOW-083` / `OI-009` open. PEC may prepare non-canonical
exploratory types only inside the owning deliverable boundary, but no such
file may be published or relied upon as the canonical shared event contract.
No Root mirror or Root write is authorized.

PEC owns monitoring of this deferral. It expires before the earliest of:

1. acceptance of `DEL-00-02` as a canonical publication;
2. asking any Root, App, or other consumer to pin or rely on PEC event types;
3. `DEL-07-01`, `DEL-07-02`, `DEL-07-03`, `DEL-07-04`, or `DEL-07-05`
   needing a stable contract input; or
4. a proposed Root write under `SOW-074`.

At expiry, the owner must select an exact Root-home, PEC-home, or split-home
candidate. This deferral creates no schema, version, mirror, compatibility,
transport, or implementation contract.

## Conditional write surfaces

- PEC decision record and register
- PEC open-item/coordination status surfaces carrying `SOW-083` / `OI-009`
- non-binding notices only if an affected external loop has a pending
  reliance proposal

No contract source file, PRD, decomposition, ScopeOfWork, Root surface, or
implementation surface is authorized.
