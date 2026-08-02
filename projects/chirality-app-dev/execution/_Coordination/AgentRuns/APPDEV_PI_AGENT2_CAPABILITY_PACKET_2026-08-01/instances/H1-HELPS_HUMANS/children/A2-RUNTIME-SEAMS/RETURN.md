# Agent 2 Return — Runtime Seams

Status: `COMPLETE / READ_ONLY`
Basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

- Current Root protocol/coordinator and App adapter enforce one `read_file`,
  zero write targets, and read-only descriptors.
- Generic permission/path/write/shell descriptors exist, but are not a live Pi
  execution registry; Pi uses ad hoc bound callbacks.
- Both Pi descriptors say `durableResume: false`; the active adapter uses and
  disposes an in-memory session. Product event replay does not hydrate Pi.
- Interruption and compaction evidence are live. Neither supplies durable
  resume state.
- App executable dependency surfaces pin `0.82.0`; the Root engine descriptor
  declares `0.82.0`; App governing records say `0.80.10`.
- Root Pi engine factory has no caller; the packaged daemon registers the
  App compatibility adapter. Root semantic work must precede App conformance.

Principal evidence: `runtime/packages/contracts/src/protocol.ts:55-76`;
`runtime/packages/core/src/agent1-run-coordinator.ts:213-330,660-758`;
`runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:34-93`;
`projects/chirality-app-dev/frontend/src/lib/harness/pi-agent-engine-adapter.ts:361-445,560-609,654-669,787-804,999-1007`;
`projects/chirality-app-dev/frontend/electron/runtime-host.ts:154-235,440-446`.
