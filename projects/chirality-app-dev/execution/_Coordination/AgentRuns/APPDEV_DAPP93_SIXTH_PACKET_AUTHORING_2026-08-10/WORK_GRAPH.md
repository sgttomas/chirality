# D-APP-93 sixth-lineage work graph v1

Status: `FROZEN BEFORE DISPATCH`

Selection authority: owner direction, 2026-08-10.
Posture: `TERMINAL_FAN_OUT_IN` with serialized author then verifier.

| Node | Role | Depends on | Write owner | Expected return | Gate |
|---|---|---|---|---|---|
| M0 | WORKING_ITEMS manager | none | run control / preflight | clearance identities + intake/tool preflight | all PASS before child exists |
| N1 | fresh ephemeral Agent 2 author | M0 | `authoring/**`, `packet/**`, `returns/N1_AUTHOR_RETURN.md` | complete packet, index, terminal author return | manager validates all 80 rows, zero historical IDs, containment |
| M1 | WORKING_ITEMS manager | N1 | validation / freeze records | immutable packet inventory and frozen identity | freeze complete; no author writes afterward |
| N2 | genuinely fresh read-only Agent 2 verifier | M1 | `returns/N2_VERIFIER_RETURN.md` only | independent PASS/BLOCK | PASS required; no repair |
| M2 | WORKING_ITEMS manager | N2 | closeout / approval-request surface | frozen identity, verifier return, exact owner gate | STOP; no execution |

Concurrency: none. N2 is held until N1 fan-in is accepted and all packet
bytes are frozen. Any mismatch or fence breach blocks only this lineage and
routes to preserved-evidence closeout; no seventh lineage is created.

Pacing: N1 produces six durable authoring stages. Expected stage durations are
6, 8, 14, 12, 10, and 8 minutes (58 minutes total). The first checkpoint is
at 8 minutes. Later checkpoints use 10-minute intervals and judge liveness by
growth in the on-disk file count or byte total. Interrupt only after one full
checkpoint interval with zero growth. Every checkpoint records both measures
and states that native context telemetry is unavailable when it is unavailable.
