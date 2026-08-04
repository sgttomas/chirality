# TM-ROOT-112 candidate normative clauses

Status: `PROPOSAL — NON-AUTHORITATIVE UNTIL SIGNED OWNER RETURN`
Candidate set: `ROOT-TM112-SEMANTICS-01 / G2 + C1 + F1`
Implementation: `HELD`

The words SHALL, MUST, and MAY below are proposed contract language only. They
do not amend Root authority unless the accountable human selects and signs the
corresponding option set.

## N-STOP-1 — lifecycle and admission

`RuntimeDaemon.stop()` SHALL enter a single `STOPPING` operation, stop admission
of new HTTP connections before waiting on existing work, and return the same
in-flight promise to every concurrent caller. A completed keep-alive connection
with no active request is idle transport and SHALL NOT prolong stop. A call made
after successful stop SHALL be a fulfilled no-op.

## N-STOP-2 — finite grace

The production graceful-stop interval SHALL be exactly **2,000 milliseconds**,
measured by a monotonic clock from the first transition to `STOPPING`. During
that interval active response work may finish and shutdown-requested
interruptions may reach their canonical terminal persistence. No active or idle
HTTP connection, incomplete request, SSE response, or interruption
acknowledgement may extend the transport wait beyond that deadline.

## N-STOP-3 — runtime stream interruption and order

Immediately after new-connection admission is closed, the daemon SHALL request
cancellation of every active runtime-owned SSE response. For session-turn SSE,
it SHALL invoke the route's canonical `interruptSession(projectId, sessionId)`
operation. For high-level Agent 1 run SSE, it SHALL invoke that same canonical
operation as soon as the manager-session identity is known; a stop or disconnect
before the first identifying event SHALL latch the request and invoke it when
the identity becomes available before the force deadline. At force, a still-
pre-identity latch SHALL expire as owned by the closing server generation,
SHALL record `INTERRUPTION_IDENTITY_UNAVAILABLE`, and MUST NOT invoke a late
interrupt if identity appears afterward. The iterator's close/return path SHALL
also be requested where available, and later settlement SHALL be observed
without mutating a restarted generation. Disconnect and shutdown share one idempotent
cancellation latch per response: they MUST NOT create semantically distinct or
unbounded duplicate interrupts. Completed responses are not interrupted. An
incomplete ordinary HTTP request with no admitted runtime operation has no
runtime session to interrupt and is handled as residual transport under
N-STOP-4.

## N-STOP-4 — force boundary and bounded transport termination

At the 2,000 millisecond deadline, if the Node server close has not completed,
the daemon SHALL call `server.closeAllConnections()` **after** `server.close()`
and SHALL destroy every still-tracked server-side socket. The explicit socket
registry is the residual safety net for pre-header connections and connection
classes that Node does not close through `closeAllConnections()`. Forced socket
termination ends the daemon's wait on response completion and interruption
acknowledgement; those promises MUST NOT keep `stop()` pending after the force
step. The implementation SHALL contain no upgrade route, but any socket accepted
by the server remains subject to the tracked-socket force rule. Transport
termination is therefore bounded by the 2,000 millisecond grace plus the event-
loop turn needed to issue forced destruction; filesystem scheduling and event-
loop starvation are not claimed to have a wall-clock bound. No final HTTP body,
SSE terminal frame, or graceful client EOF is promised after the force deadline;
the portable client-visible contract is disconnection, which may surface as EOF
or reset according to Node and the operating system. After force is issued, the
daemon SHALL allow at most **500 additional milliseconds** for the Node close
callback and tracked-socket set to settle, without waiting on any response or
interruption promise. If that force-settle boundary expires, it SHALL record a
close-timeout failure, continue owned metadata cleanup, and reject after cleanup.
Thus connection-governed termination has a 2,500 millisecond production bound
(2,000 ms grace + 500 ms force settlement), subject only to event-loop
starvation; filesystem cleanup is separately awaited under N-STOP-5.

The 500 millisecond force-settle value is a proposed human-selected product
policy, not an evidence-derived Node guarantee. It trades a short window for
bound Node close/socket events to settle against deterministic exit from an
anomalous close lifecycle. Expiry rejects stop even after forced destruction.
For G1, G2, and G3 the derived connection bounds are respectively 1,500,
2,500, and 4,500 milliseconds; the bound is never fixed independently of grace.

## N-STOP-5 — cleanup, completion, and evidence meaning

Socket-path disappearance is not stop completion. After graceful close or the
forced step, the daemon SHALL attempt both control-socket unlink (accepting
`ENOENT`) and owner-record removal, and owner-record removal SHALL remain
identity guarded to this daemon instance and process. `stop()` SHALL fulfill
only after those cleanup attempts complete and the owned socket and owner record
are absent. The observable completion condition is the settled stop promise
plus owner cleanup, not socket-path absence alone.

## N-STOP-6 — errors, idempotence, and restart

Interruption, server-close, force, socket-unlink, and owner-record failures SHALL
be collected without skipping later teardown steps. An interruption still
pending at the grace deadline SHALL be recorded as a timeout; its eventual
settlement SHALL be observed so it cannot become an unhandled rejection, but it
SHALL NOT extend stop. After best-effort teardown, `stop()` SHALL reject with the
collected failure(s); reaching the force boundary alone is not a failure.

Failure state SHALL be classified exactly:

1. If transport is closed and owned socket/owner metadata is absent but an
   interruption timed out, failed, or lacked pre-force identity, the instance
   enters `STOPPED_DEGRADED`. Its stop promise rejects; later settlement is
   observed, but `start()` on that instance remains rejected. Recovery is
   process/runtime-service replacement, not reuse of a generation whose
   application work may still be unresolved.
2. If close/force/socket/owner cleanup is incomplete, the instance enters
   `STOP_FAILED_CLEANUP`. A repeated `stop()` is the retry operation: it retries
   only incomplete transport and owned-metadata cleanup, coalesces concurrent
   retries, and transitions to `STOPPED` only if cleanup completes with no
   unresolved interruption failure, otherwise to `STOPPED_DEGRADED`.

`start()` SHALL reject while start or stop is in flight, in
`STOPPED_DEGRADED`, or in `STOP_FAILED_CLEANUP`. After a successful stop, the
same daemon instance SHALL support restart, create a new listener/connection
generation and owner record, serve an authenticated request, and stop again
under this contract. Late close/error/iterator/identity events from the previous
generation MUST NOT interrupt, close, unlink, or otherwise mutate the restarted
generation. This clause does not change the public meaning of `daemonId` or
`startedAt`; any required identity rollover is a separate contract question.

## N-STOP-7 — claim boundary

This is the Root daemon transport and runtime-route shutdown contract. It does
not guarantee any external process manager's signal deadline, prove that an App
R2 GUI used the reproduced SSE or incomplete-request mechanism, or establish
that Electron/signal behavior did not contribute. A Root acceptance and repair
would authorize App's separate parity rerun; it would not itself satisfy that
App proof.
