# Agent 2 Return — Packet Conventions

Status: `COMPLETE / READ_ONLY`
Basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

- D-APP-84 is the next free App decision ID at the inspected basis.
- Current convention supports a `PROPOSAL / AWAITING_RULING` packet and one
  appended register row; a later ruling uses a separate ruling record and
  transitions the row without rewriting the packet.
- Packet staging does not update `_Coordination/_LATEST.md` or
  `_ScopeChange/_LATEST.md` and does not append a receipt before the owner act.
- On ruling, App implementation routes through SCOPE_CHANGE; Root generic
  runtime changes require a separate Root route.

Principal evidence: `execution/_Coordination/_DECISIONS/_REGISTER.md` preamble
and Decision Preparation Rules; D-APP-50 §§recording; D-APP-70 and D-APP-71
packet/ruling convention; `loop/LOOP_INIT.md` owner-gate and receipt rules.
