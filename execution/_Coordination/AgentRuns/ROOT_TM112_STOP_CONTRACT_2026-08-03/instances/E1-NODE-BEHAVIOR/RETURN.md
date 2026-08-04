# E1 Node behavior return

Status: `COMPLETE / PASS FOR FAN-IN`

## Determination

On the bound Node v24.18.0 runtime, `http.Server.close()` stops the listener and
automatically destroys a completed keep-alive connection, but it remained
pending for an accepted/no-bytes socket, incomplete headers, an incomplete
request body, live SSE, and an upgraded connection. This reproduces the
mechanism behind N1 without relying on RuntimeDaemon internals.

`closeIdleConnections()` added no coverage beyond completed keep-alive and did
not stop listening. `closeAllConnections()` forcibly destroyed every tested
ordinary HTTP class, including incomplete requests and SSE, but did not stop
listening and did not destroy the upgraded connection. Ordering `close()` first
and `closeAllConnections()` second completed ordinary active cases while
preventing new accepts; it still required explicit tracked-socket destruction
for the upgraded class.

The two 27-case runs reproduced exactly after removing timestamp and PID. See
`EVIDENCE.md`, `PROBE_RESULTS.json`, and `PROBE_RESULTS_REPEAT.json`.

## Ordering consequences

1. Stop accepting first with `server.close(callback)`; the connection helpers
   alone continue accepting and create a race with new connections.
2. Treat the close callback as the terminal listener/connection-drain signal.
   It is asynchronous and unbounded. A repeated close callback can receive
   `ERR_SERVER_NOT_RUNNING`; daemon-level stop must therefore coalesce or define
   idempotence rather than blindly repeating Node close.
3. During a human-selected grace interval, initiate application-owned
   cancellation/interruption for SSE and other active work. Node does not do it.
4. At an accepted force boundary, call `closeAllConnections()` for ordinary
   HTTP connections and destroy still-tracked sockets to cover upgrades/raw
   residuals; then await close and socket-set drainage before removing the
   owner record or permitting restart.
5. Serialize generations. Node allowed a fresh server to bind the same IPC
   pathname while the prior generation's close was still pending.

This ordering is a non-authoritative implementation recommendation. Exact
grace duration, required SSE cancellation acknowledgment, and peer-visible
forced-termination behavior remain human-selected contract semantics.

## RuntimeDaemon-specific risks

- Current `stop()` has no bound or force step.
- Current `stop()` clears `this.server` before drain completes. Concurrent stop
  can skip the live server and reach cleanup, while concurrent start passes the
  in-memory started guard. A lifecycle state/shared stop promise is required.
- Current source does not track sockets, so `closeAllConnections()` alone would
  leave upgraded residuals.
- Cleanup and restart must be owned by the closing generation and occur only
  after its accepted terminal state.

## Gaps

Only Node v24.18.0 on Darwin arm64 was executable locally. The support floor
Node 22.19.0 and Linux/Windows IPC behavior require CI coverage. The public
declarations specify no close deadline, application cancellation, upgrade
cleanup, filesystem cleanup, or lifecycle idempotence.

All persistent writes are confined to this instance directory. No runtime
source, tests, lifecycle records, Git state, or external content was modified.
