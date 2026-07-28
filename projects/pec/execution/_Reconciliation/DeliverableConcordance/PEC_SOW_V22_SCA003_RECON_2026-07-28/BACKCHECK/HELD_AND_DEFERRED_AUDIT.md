# Held and deferred audit

## Active hold

`PEC-HOLD-001` remains `ACTIVE`. The hold register SHA-256 is still
`d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a`,
byte-identical to the activation basis.

`HOLD_TESTS.json` confirms:

- `ALLOW`: historical read-only inspection, exact correction preparation,
  and candidate validation;
- `BLOCK` with exit 4: production reliance, production dispatch, promotion,
  and consumption; and
- `holdReleased: false`.

The held `DEL-00-01` claims `CLM-005` and `REQ-004` were not included in the
repair manifest and remain unchanged.

## Deferred or excluded

- Production and runtime implementation remain excluded.
- Reliance, promotion, dispatch, consumption, release, lifecycle transition,
  dependency/topology change, estimates, and schedules remain excluded.
- All explicit `TBD-*` and `CON-*` records remain for their owning production
  or owner-decision workflows.
- PRD v2.2 §13 still describes ADR-002 and ADR-014 as live postures, while
  D-PEC-67/-68, PRD §15, SCA-003, and decomposition `SOW-088` make ADR-014
  historical lineage only. This is routed to PRD authority and was not
  silently repaired in a ScopeOfWork contract.

These items do not block this exact reconciliation closeout. The active hold
does block every prohibited production/reliance act until separately released
by its owning authority.
