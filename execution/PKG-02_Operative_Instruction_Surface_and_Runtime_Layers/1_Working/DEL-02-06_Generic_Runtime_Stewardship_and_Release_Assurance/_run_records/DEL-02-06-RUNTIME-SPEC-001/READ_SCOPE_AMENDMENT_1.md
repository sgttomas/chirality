# Read-scope amendment 1 — accepted-turn recovery discovery

RunID: `DEL-02-06-RUNTIME-SPEC-001`
Amends: activation/work graph plan version 1 to version 2
Disposition: `RECORD` — read-only discovery; no authority effect

## Reason

The owner-routed `TM-ROOT-108` concern requires an exact inventory of the
current accepted-turn persistence, startup/admission, drain-accounting, and
terminal-event surfaces. The first-activation read item 4 names only the
protocol/error contracts, client, and CLI. Those paths do not contain the
coordinator/store/daemon implementation that the routed concern identifies.

## Added read-only paths

- `runtime/packages/contracts/src/events.ts`
- `runtime/packages/contracts/src/harness/event-schema.ts`
- `runtime/packages/core/src/turn-coordinator.ts`
- `runtime/packages/core/src/agent1-run-coordinator.ts`
- `runtime/packages/core/src/session-store.ts`
- `runtime/packages/core/src/runtime-service.ts`
- `runtime/packages/core/src/residency-coordinator.ts`
- `runtime/packages/daemon/src/runtime-daemon.ts`
- `runtime/tests/daemon.test.ts`
- `runtime/tests/turn-hardening.test.ts`
- `runtime/tests/session-and-residency.test.ts`

## Boundary

These paths remain read-only. Their inclusion supports N1/N3 planning only.
It does not authorize implementation commands, registered software checks,
runtime writes, client classification by source proximity, or any later gate.
