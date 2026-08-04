# Sealed implementation brief — ROOT-TM112-IMPLEMENT-01

Status: `AUTHORIZED / SEALED / NOT STARTED`
Parent authority: `ROOT-TM112-SEMANTICS-01 G2 C1 F1`
Implementation carrier: future run must cite this brief and its manifest hash.

## Objective

Implement the accepted N-STOP-1 through N-STOP-7 daemon shutdown contract and
its bounded regression tests, then return implementation evidence for human
acceptance. Do not route the App notice until that repair is accepted.

## Sealed basis

- Signed transcript SHA-256:
  `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.
- Signed TM112 block SHA-256:
  `a18f963d4666af73dd44674ea2d43f5052dc7eb96ddfe977f7a84070927f3a53`.
- Accepted post-whitespace clause SHA-256:
  `fd3ba31a8c53719e165b131d872868a53760adab4dc7ae92015fbd6641a11ead`.
- Pre-whitespace equivalent clause SHA-256:
  `2428824746c5a6928c2894619d67bbc817717bed536f5ee64b11cdafda0db62e`.
- Current source basis at freeze:
  - `docs/SPEC.md`:
    `988c4b90287753d1249f53d01838819028ecb959a8fa1cbecf873e50c0fb62db`;
  - `runtime/packages/daemon/src/runtime-daemon.ts`:
    `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`;
  - `runtime/tests/daemon.test.ts`:
    `bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e`;
  - runtime manifest/lock:
    `499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071` /
    `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f`.

If any sealed input drifts before implementation begins, stop and rebind the
brief. Do not silently carry semantics onto changed source.

## Exact future write scope

Only these surfaces are authorized:

1. `docs/SPEC.md`, section 14.1 `Local control plane` — the single canonical
   Root shutdown-contract surface. Add the accepted externally observable
   shutdown semantics; do not change unrelated runtime or governance rules.
2. `runtime/packages/daemon/src/runtime-daemon.ts` — implementation only.
3. `runtime/tests/daemon.test.ts` — bounded regression cases only.
4. A new implementation run carrier under
   `execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/**` for
   briefs, raw results, validation, refutation, return, and handoff evidence.

No write to `docs/CONTRACT.md`, `docs/TYPES.md`, `runtime/README.md`, runtime
core/client/CLI packages, App content, registers, receipts, lifecycle records,
or Git is authorized. If the accepted semantics cannot be implemented within
the three product files above, return a scope-change request instead of writing
outward.

## Required implementation behavior

### Lifecycle and generations

- Introduce an explicit lifecycle sufficient to distinguish initial/stopped,
  starting, running, stopping, `STOPPED_DEGRADED`, and
  `STOP_FAILED_CLEANUP` states.
- Set the starting state before the first asynchronous `start()` operation so a
  concurrent second start rejects and leaves exactly one listener/owner.
- Make `stop()` return the identical stored in-flight Promise to concurrent
  callers; do not rely on repeated Node `server.close()` calls.
- A stop after successful stop fulfills as a no-op. Start during stop, in either
  failure state, or during another start rejects.
- Bind server, socket, SSE, timers, callbacks, cleanup, and late events to a
  generation token. A prior generation may not interrupt, close, unlink, or
  mutate a restarted generation.
- After a successful stop the same daemon instance must start a new generation,
  serve authenticated health, and stop again.

### Grace, interruption, and force ordering

1. On the first stop call, transition to `STOPPING` and capture a monotonic
   deadline exactly 2,000 ms later.
2. Call `server.close()` to stop admission before requesting active SSE
   interruption.
3. Immediately request each active SSE route's canonical
   `interruptSession(projectId, sessionId)` at most once per cancellation latch.
   Session-turn identity is known from the route. High-level Agent 1 identity is
   latched until known, but only before force.
4. Request the iterator close/return path where present. Observe every eventual
   settlement so no rejection becomes unhandled, but never let it mutate a later
   generation.
5. At 2,000 ms, if close is incomplete, call
   `server.closeAllConnections()` after the prior `server.close()` call, then
   destroy the closing generation's still-tracked server sockets. No final HTTP
   or SSE frame is guaranteed after force; client-visible EOF versus reset is
   platform-dependent disconnection.
6. At force, expire any pre-identity latch, record
   `INTERRUPTION_IDENTITY_UNAVAILABLE`, and forbid a late interrupt.
7. Wait no more than 500 additional ms for Node close callback and tracked-
   socket settlement. Do not wait on response or interruption promises. On
   expiry, record close timeout and proceed to owned metadata cleanup.
8. Attempt control-socket unlink (`ENOENT` accepted) and identity-guarded owner
   removal before settling stop. Socket-path absence alone is not completion.

### Failure states

- Collect interruption, server-close, force, socket-unlink, and owner failures
  without skipping later teardown; reaching force alone is not a failure.
- If transport and owned metadata are clean but interruption timed out, failed,
  or lacked identity, reject stop and enter `STOPPED_DEGRADED`. Later settlement
  is observed, instance reuse stays blocked, and recovery is process/runtime-
  service replacement.
- If transport or owned metadata cleanup is incomplete, reject stop and enter
  `STOP_FAILED_CLEANUP`. A repeated stop retries only incomplete transport and
  metadata cleanup, coalesces concurrent retries, and ends in `STOPPED` or
  `STOPPED_DEGRADED` according to remaining interruption state.
- Report collected failures after cleanup attempts; do not emit unhandled
  rejections.

## Bounded regression matrix

All cases belong in `runtime/tests/daemon.test.ts` and must avoid weakening the
production constants through a public timing override.

| Case | Required observations |
|---|---|
| Idle | Stop settles before grace; socket/owner absent; repeated stop fulfills no-op. |
| Completed keep-alive | Completed response is not interrupted; stop settles before grace; client transport closes; metadata absent. |
| Incomplete ordinary request | Pending before 2,000 ms; forced at deadline; client disconnected; no session interrupt; stop/cleanup settle within the accepted force window subject to timer tolerance. |
| Live SSE — graceful interrupt | Interruption is requested immediately after admission closes; exactly one semantic interrupt; canonical terminal persistence may complete during grace. |
| Live SSE — stubborn interrupt | At grace, transport is forced; pending interruption cannot extend stop; clean metadata plus interruption timeout becomes `STOPPED_DEGRADED`; start rejects. |
| Pre-identity Agent 1 — never yields | Latch expires at force with identity-unavailable failure; iterator return requested/observed; no unhandled rejection. |
| Pre-identity Agent 1 — yields after force | No late interrupt and no mutation of any replacement/restarted generation. |
| Bounded termination | Force starts at 2,000 ms; Node close/socket settlement receives at most 500 ms more; test tolerance does not redefine either production value. |
| Disconnect/interrupt | Disconnect and shutdown share one idempotent latch; no duplicate semantic interrupt; canonical persisted interruption remains distinct from transport close. |
| Socket and owner cleanup | Socket absence before close completion is not success; owner remains until accepted terminal cleanup; foreign owner is never removed. |
| Cleanup failure/retry | Inject cleanup failure, enter `STOP_FAILED_CLEANUP`, reject start, and prove repeated stop retries only incomplete cleanup to the defined terminal state. |
| Concurrent lifecycle | Concurrent stop returns the same Promise; second start during first start rejects with one listener/owner; start during stop rejects. |
| Restart/generation | Successful stop permits same-instance health-serving restart; second stop passes; late prior-generation close/error/iterator/identity events cannot affect the new generation. |

Run the existing daemon suite plus runtime typecheck/build. Preserve exact raw
commands, Node/platform identity, durations, client outcomes, interrupt counts,
socket/owner states, failure states, and restart generation evidence. Execute at
the supported Node 22.19 floor and current Node 24 where available; otherwise
return the unexecuted compatibility gap rather than claiming coverage.

## Acceptance checks

- `docs/SPEC.md` and implementation match accepted N-STOP-1..7 without adding
  new public configurability or widening runtime ownership.
- Every matrix case passes and the existing daemon/runtime suite remains green.
- Node `closeAllConnections()` is ordered only after `server.close()`; explicit
  socket tracking covers residual/upgrade-class connections.
- No App/process/SIGTERM causal claim appears in contract, code comments, tests,
  or return.
- App notice remains unshipped until human acceptance of the repair.
- Independent read-only refutation and deterministic validation examine the
  final implementation candidate before acceptance.
- The implementation run returns exact changed-file hashes, commands/results,
  coverage gaps, and a terminal handoff. Validation/commit/publication is not
  semantic acceptance or merge authority.

## Prohibitions

Do not edit before checking the sealed hashes. Do not change the 2,000/500 ms
policies, relax degraded/cleanup failure states, substitute transport close for
canonical interruption, permit late pre-identity interrupts, or route App work.
Do not implement signal handling. Do not expand scope, update lifecycle, stage,
commit, push, merge, or open a PR without the separately applicable gate.
