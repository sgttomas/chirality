# Approved implementation/test scope map — held pending semantic ruling

Status: `PREPARATION ONLY — NO IMPLEMENTATION AUTHORITY FROM THIS PACKET`

The owner already authorized a later bounded tranche at the listed minimum
candidate scope. This map demonstrates implementability; it does not edit or
authorize edits to these surfaces.

| Approved case | Candidate obligation | Later source/test seam | Required observation |
|---|---|---|---|
| Idle | N-STOP-1, 5, 6 | `RuntimeDaemon.stop`; existing fixture | settles without waiting for grace; socket/owner absent; second stop no-op |
| Completed keep-alive | N-STOP-1, 5 | server close + connection tracking | completed client is not interrupted; stop settles before grace; client transport closes; metadata absent |
| Incomplete ordinary request | N-STOP-2, 4, 5 | server connection registry and force timer | still pending before selected grace; forced at deadline; client destroyed; no session interrupt; stop and cleanup settle |
| Live SSE | N-STOP-2, 3, 4 | `sse()` cancellation latch plus stop coordinator | canonical interrupt requested at stop begin; natural completion may win; otherwise forced at grace; no duplicate semantic interrupt |
| Bounded termination | N-STOP-2, 4 | monotonic grace deadline, residual force, and force-settle deadline | force starts at 2,000 ms; response/interrupt promises cannot extend it; close/socket settlement gets at most 500 ms more; test uses scheduling tolerance without redefining either production value |
| Disconnect/interrupt | N-STOP-3, 6 | response-close path, shutdown path, and generation-owned cancellation latch | one idempotent latch; never-yields expires at force with identity-unavailable failure; yields-after-force cannot invoke a late interrupt or mutate restart; no unhandled rejection |
| Socket and owner cleanup | N-STOP-5, 6 | socket unlink + `removeOwnedRecord()` + lifecycle state | socket absence alone is not completion; foreign owner is never removed; injected cleanup failure enters `STOP_FAILED_CLEANUP`; repeated stop retries only incomplete cleanup and reaches the defined terminal state |
| Restart | N-STOP-1, 6 | start/stop state, server-generation token, and in-flight promise | second start while first is in flight rejects and leaves one listener/owner; start during stop rejects; same instance restarts only after successful stop; interruption failure with clean metadata enters `STOPPED_DEGRADED` and blocks reuse; late prior-generation events cannot touch a new generation |

## Minimum implementation boundary already authorized

- Accepted Root shutdown-contract surface selected by the owner after this gate.
- `runtime/packages/daemon/src/runtime-daemon.ts`.
- Bounded cases in `runtime/tests/daemon.test.ts` listed above.

No core coordinator, App, process/SIGTERM, launch-agent, CLI, or additional
runtime package source is silently included. If implementation proves that
canonical interruption cannot be met inside the listed source boundary, the
implementer must return a scope-change request instead of editing outward.

## Non-test claims

- The test suite can prove bounded daemon method behavior under its test event
  loop and sockets. It cannot prove launchd's kill timing, Electron delivery of
  SIGTERM, or App R2 causality.
- The restart case proves the daemon object's listener/owner lifecycle; it does
  not by itself prove external LaunchAgent restart policy.
