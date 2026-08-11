# D-APP-93 seventh-lineage work graph v1

Status: `FROZEN BEFORE DISPATCH`

Selection authority: owner direction, 2026-08-10.
Posture: `TERMINAL_FAN_OUT_IN`, serialized author → manager freeze → fresh verifier.

| Node | Role | Depends on | Write owner | Expected return | Gate |
|---|---|---|---|---|---|
| M0 | WORKING_ITEMS | none | control/preflight | exact citations + allowlist + intake/tool preflight | PASS before child exists |
| N1 | fresh ephemeral Agent 2 author | M0 | authoring/packet/scratch/N1 return | fresh packet plus command-form probe ledger | manager accepts 80-row alignment, all probes/classifications, zero historical IDs |
| M1 | WORKING_ITEMS | N1 | validation/freeze | independent safe re-probes; accepted immutable freeze | every safe probe passes; every RNE is justified; no changed byte |
| N2 | genuinely fresh read-only Agent 2 verifier | M1 | verifier return only | independent PASS/BLOCK over complete freeze | PASS only; no repair |
| M2 | WORKING_ITEMS | N2 | handoff/approval request | frozen identity + verifier identity + exact approval surface | STOP; no execution |

No concurrency. Any failed node holds all descendants. No improvisational
replacement chain and no eighth lineage.

N1 durable-stage expectations: 7, 9, 18, 16, 10, 9, and 8 minutes (77 total).
The first checkpoint is no earlier than 10 minutes; later checkpoints are at
12-minute intervals. Liveness is measured only by growth in durable output
file count or byte total. One full interval with zero growth permits
interruption; quietness alone does not. Each event records both measures and
states native context telemetry is unavailable when it remains unavailable.
