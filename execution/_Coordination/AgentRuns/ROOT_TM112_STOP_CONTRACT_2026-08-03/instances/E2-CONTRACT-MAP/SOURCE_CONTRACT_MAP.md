# TM-ROOT-112 source and contract map

Artifact class: `DERIVATIVE DECISION SUPPORT — NON-AUTHORITATIVE`

Instance: `E2-CONTRACT-MAP`

Source revision: `88e7590d3664d4f1daf91bed2a8899bda0748b92`

Current `runtime-daemon.ts` SHA-256:
`a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`

## 1. Epistemic key

- **ACCEPTED CONSTRAINT** — binding Root text already accepted by the owner.
- **SOURCE FACT** — directly visible in the current source at the cited lines.
- **EXECUTED FACT** — observed by the N1/H1 controlled investigation at the
  bound revision and environment.
- **INFERENCE** — consequence reasoned from cited source/evidence but not
  directly exercised by N1/H1.
- **PROPOSAL** — decision-support framing only; it does not select semantics.
- **GAP / TBD** — not supplied by accepted contract or executed evidence and
  still requires human selection or later verification.

## 2. Bound basis and authority

| Classification | Map |
|---|---|
| ACCEPTED CONSTRAINT | The daemon is the exclusive production owner of engines, sessions, turn locks, interruption, and related runtime state; clients must not construct a competing runtime (`docs/CONTRACT.md:161`; `runtime/README.md:7-11`). A shutdown design therefore cannot transfer canonical interruption ownership to Desktop, CLI, or project proxies. |
| ACCEPTED CONSTRAINT | Runtime control is authenticated, project-scoped HTTP/1.1 over the protected Unix socket, with no TCP listener (`docs/CONTRACT.md:162`; `docs/SPEC.md:892-910`; `runtime/README.md:24-25,33-35`). The selected stop semantics must preserve that listener/security boundary. |
| ACCEPTED CONSTRAINT | Root specifies health, session, turn, interrupt, and canonical SSE routes but gives no daemon connection-drain duration, stream-cancellation order, or forced residual-connection rule (`docs/SPEC.md:892-911`). This absence is the contract gap; the unrelated model-residency rule drains active Pi work during model activation, not daemon HTTP shutdown (`docs/CONTRACT.md:165`; `docs/SPEC.md:928-939`). |
| ACCEPTED HUMAN AUTHORITY | The owner authorized a separate bounded semantic-contract and implementation/test tranche at the minimum candidate scope, while reserving exact grace duration, stream-cancellation obligations, and forced residual-connection behavior for another human selection before implementation (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md:14-21`, SHA-256 `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`). |
| COORDINATION BOUNDARY | The original App notice is coordination, not authority, and requested Root reproduction/disproof, intended connection-drain/termination semantics, cleanup, bounded tests, and a reciprocal response (`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md:9-16,97-117`, SHA-256 `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`). |

## 3. Current daemon lifecycle

### 3.1 Start

| Step | Classification | Current behavior and consequence |
|---|---|---|
| S1 | SOURCE FACT | `start()` rejects only while `this.server` is non-`undefined` (`runtime/packages/daemon/src/runtime-daemon.ts:49-50`). |
| S2 | SOURCE FACT | It prepares private directories, runs stale-socket recovery, then writes the owner record before constructing/listening on the HTTP server (`runtime/packages/daemon/src/runtime-daemon.ts:51-61,72-85`). |
| S3 | SOURCE FACT | The server routes each request asynchronously; route failure is converted to an HTTP error (`runtime/packages/daemon/src/runtime-daemon.ts:72-74`). |
| S4 | SOURCE FACT | After listen succeeds, the socket is chmod `0600` (`runtime/packages/daemon/src/runtime-daemon.ts:81-87`). |

### 3.2 Stop

| Step | Classification | Current behavior and consequence |
|---|---|---|
| T1 | SOURCE FACT | `stop()` copies `this.server` and immediately clears the field (`runtime/packages/daemon/src/runtime-daemon.ts:90-93`). This stops the field from representing a stop-in-progress state. |
| T2 | SOURCE FACT | If a server existed, `stop()` awaits the callback of `server.close()` and rejects on a callback error (`runtime/packages/daemon/src/runtime-daemon.ts:93-97`). There is no timeout, request/response inventory, explicit stream interruption, or residual-connection force step in `stop()`. |
| T3 | SOURCE FACT | Only after the awaited close succeeds does source explicitly unlink the socket (ignoring `ENOENT`) and call owner-record cleanup (`runtime/packages/daemon/src/runtime-daemon.ts:98-102`). |
| T4 | SOURCE FACT | Owner cleanup removes the record only if its daemon ID and PID match the current instance; owner-record read failures are treated as no readable owner and leave the record untouched (`runtime/packages/daemon/src/runtime-daemon.ts:577-582`). |
| T5 | SOURCE FACT | A `server.close()` rejection exits before T3/T4, so current source does not guarantee cleanup on that error path (`runtime/packages/daemon/src/runtime-daemon.ts:94-102`). |
| T6 | SOURCE FACT | A sequential second `stop()` after completion sees no server and tolerates an absent socket/owner (`runtime/packages/daemon/src/runtime-daemon.ts:91-101,577-582`). |
| T7 | INFERENCE | A concurrent second `stop()` while the first awaits `server.close()` also sees no server and can advance to socket/owner cleanup before the first close finishes. N1/H1 did not execute this race. The desired concurrent-stop rule is TBD. |
| T8 | INFERENCE | `start()` is admitted by the field check while a prior stop is pending. With the N1/H1 observed state (socket pathname absent, live same-PID owner present), stale recovery would reject because the recorded PID is not demonstrably absent (`runtime/packages/daemon/src/runtime-daemon.ts:49-53,471-519`; N1/H1 result below). If a concurrent second stop had already removed the owner, a different race may result. No restart-during-stop contract or test exists. |

### 3.3 Cleanup state is not one bit

**EXECUTED FACT:** on Node v24.18.0/macOS arm64, the socket pathname was already
absent at the 750 ms observation while `server.close()` remained pending, but
the mode-`0600` owner record remained. After client release, stop resolved and
the owner record disappeared
(`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json:34-62,94-118`).

**Consequence:** socket absence proves that new connects through that pathname
cannot use the old listener; it did not prove completion of existing
connection teardown, `stop()` resolution, owner cleanup, or process exit in
the executed environment. Any acceptance criterion that uses only
`control.sock` absence is insufficient for this tranche.

## 4. Request, SSE, disconnect, and interruption flow

### 4.1 Ordinary requests

| Classification | Map |
|---|---|
| SOURCE FACT | Request bodies are consumed with `for await` until end and have a one-MiB payload limit (`runtime/packages/daemon/src/runtime-daemon.ts:354-369`). There is no stop signal or request abort passed into this loop. |
| SOURCE FACT | JSON responses end normally after fixed-length output (`runtime/packages/daemon/src/runtime-daemon.ts:378-386`). |
| EXECUTED FACT | A completed authenticated health response on a connected keep-alive client did not hold stop: both runs resolved in 0.318-0.357 ms and the client socket became destroyed (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json:24-31,85-91`). |
| EXECUTED FACT | An incomplete ordinary request (headers not terminated) held stop pending at 750 ms in both runs; destroying the client released it (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json:34-46,94-104`). |
| GAP / TBD | Accepted Root text does not say whether an incomplete ordinary request receives the selected grace, is rejected/terminated immediately, receives a protocol response, or is forcibly disconnected at the deadline. |

### 4.2 SSE routes

| Stage | Classification | Current behavior and consequence |
|---|---|---|
| E1 | SOURCE FACT | The run route captures the manager session ID from the first `harness:event`, then delegates disconnect handling to `RuntimeService.interruptSession()` only if the ID has become known (`runtime/packages/daemon/src/runtime-daemon.ts:210-231`). |
| E2 | SOURCE FACT | The session-turn route supplies `interruptSession(projectId, sessionId)` directly as its disconnect callback (`runtime/packages/daemon/src/runtime-daemon.ts:306-318`). |
| E3 | SOURCE FACT | `sse()` installs a one-shot response `close` listener. Close marks the stream disconnected and queues `onDisconnect`; callback rejection is swallowed (`runtime/packages/daemon/src/runtime-daemon.ts:388-407`). |
| E4 | SOURCE FACT | `sse()` awaits the first iterator event before sending SSE headers. If disconnection preceded first-event identity capture, it retries the idempotent callback after the first event (`runtime/packages/daemon/src/runtime-daemon.ts:409-423`). If a manager-run iterator never yields the identifying event, current source has no manager session ID to interrupt. |
| E5 | SOURCE FACT | After disconnect, `sse()` stops writing but continues awaiting/consuming the iterator until it ends; finalization waits only for queued disconnect tasks and ends a still-open response (`runtime/packages/daemon/src/runtime-daemon.ts:424-443`). Disconnect is therefore not by itself a source-level guarantee that the producer iterator terminates. |
| E6 | SOURCE FACT | `RuntimeService.interruptSession()` concurrently invokes the turn coordinator and optional Agent 1 runner interruption (`runtime/packages/core/src/runtime-service.ts:463-467`). Turn interruption aborts the active controller and awaits the engine interrupt (`runtime/packages/core/src/turn-coordinator.ts:387-392`); terminal persistence/status then occurs as the engine iterator unwinds (`runtime/packages/core/src/turn-coordinator.ts:304-384`). |
| E7 | SOURCE FACT | Existing daemon tests prove a client-disconnected session-turn can produce exactly one persisted `turn.interrupted` and `status=interrupted` with the test engine (`runtime/tests/daemon.test.ts:266-355`). They do not call `stop()` in that state. |
| E8 | EXECUTED FACT | The N1/H1 live manager-run SSE received HTTP 200 plus a first frame and held stop pending at 750-751 ms in both direct runs. Controlled client destruction caused one interruption callback and released stop at about 772 ms total (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json:49-62,107-118`). The fixture used a stub service and manually released its stream (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/fixtures/runtime-stop-reproducer.mjs:41-70,207-259`). |
| GAP / TBD | `stop()` neither enumerates live SSE responses nor calls their disconnect/interrupt callbacks (`runtime/packages/daemon/src/runtime-daemon.ts:90-102,388-443`). The human must select whether shutdown requests interruption at grace start, allows normal stream completion during grace, interrupts at deadline, or uses another exact ordering. |

## 5. Exact reproduced distinctions

All rows below are **EXECUTED FACT** at exact source revision
`88e7590d3664d4f1daf91bed2a8899bda0748b92`, Node v24.18.0, macOS 26.6 arm64.
The 750 ms boundary demonstrates bounded non-completion, not permanence
(`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/MANAGER_RETURN.md:94-104`).

| Case | At stop | 750 ms outcome | Release/outcome | What it establishes |
|---|---|---|---|---|
| Idle | No client | Resolved in 0.811-0.833 ms | Socket and owner absent | Current clean idle path completes promptly. |
| Completed keep-alive | Response 200 complete; client connection still open | Resolved in 0.318-0.357 ms | Client destroyed; socket and owner absent | A completed keep-alive connection is distinct from an active request in this environment. |
| Incomplete ordinary request | Connected client with incomplete headers | Pending; socket absent, owner present | Client destroy allowed resolution at 752.857-755.726 ms | Active ordinary protocol work can hold close. |
| Live SSE | HTTP 200, `text/event-stream`, first frame received, connection live | Pending; socket absent, owner present | Client destroy caused one interrupt and resolution at 771.955-772.037 ms | A live streaming response can hold close; disconnect can release the stubbed producer. |
| Child process + live SSE + SIGTERM | Fixture's signal handler called `daemon.stop()` | Child still alive; no exit code/signal; socket absent, owner present | Controlled client release allowed stop and owner cleanup; child exited 0 | Process exit awaited the fixture's stop promise. It does not prove `RuntimeDaemon` owns signals. |

Numeric evidence: `execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json:14-64,76-155`.

## 6. Approved minimum cases: present proof versus required regression

| Owner-approved case | Existing evidence | Semantic/test consequence still open |
|---|---|---|
| Idle | N1/H1 direct pass; ordinary teardown calls stop in `afterEach` (`runtime/tests/daemon.test.ts:24-27`) | Regression must bind completion and both cleanup artifacts to the selected contract. |
| Completed keep-alive | N1/H1 direct pass only | Regression must keep this distinct from incomplete/active HTTP and state whether grace is consumed. |
| Incomplete ordinary request | N1/H1 demonstrated pending-until-client-release | Regression must enforce the human-selected deadline/residual behavior without external manual release. |
| Live SSE | N1/H1 demonstrated pending-until-client-release with stub manager run | Regression must exercise the selected shutdown ordering and terminal client/producer result. Session-turn and Agent 1 run paths are distinct callback-identification cases. |
| Bounded termination | N1/H1 had an observation boundary but current code has no deadline | Exact duration, clock start, deadline action, and test tolerance remain human-selected/TBD. |
| Disconnect/interrupt | Existing test covers voluntary client disconnect for a session turn; N1/H1 covers manual disconnect of a stub manager run | Required shutdown-induced disconnect/interruption obligations and terminal evidence remain human-selected/TBD. |
| Socket and owner cleanup | N1/H1 proved normal cleanup after external release and showed socket/owner states can diverge | Regression must require the selected terminal state on success and define error-path guarantees. |
| Restart | Current suite starts new fixtures but does not prove stop-then-start on one daemon instance after active-client shutdown | Define admission after successful stop, identity/owner refresh expectations, and behavior while stop is pending or failed. |

The existing suite contains five tests but no stop-with-live-ordinary-client or
stop-with-live-SSE case
(`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/BASELINE_DAEMON_TESTS.md:18-30`).

## 7. Human selections still required

Nothing in this section is a ruling. Each row is a **GAP / TBD** or a
**PROPOSAL** that exposes consequences for the manager's decision packet.

### 7.1 Exact grace duration

The owner must select:

1. the exact duration;
2. the start instant (proposed candidates include `stop()` invocation or the
   instant new admissions are closed);
3. whether zero grace is allowed;
4. what counts as graceful completion before the deadline (connection ended,
   route iterator ended, interruption persisted, cleanup completed, or an
   exact combination); and
5. deterministic test tolerance versus the normative duration.

**Consequence:** the N1/H1 750 ms observation is evidence of non-completion at
that boundary, not an accepted grace duration (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/MANAGER_RETURN.md:94-103`).

### 7.2 Stream-cancellation obligation and ordering

The human must select, separately for live SSE/runtime work and incomplete
ordinary HTTP:

- whether shutdown requests canonical runtime interruption immediately, only
  at grace expiry, or not at all before transport force;
- whether no new routes are admitted before interruption begins;
- whether `stop()` waits for terminal turn/run evidence, merely awaits the
  interruption call, or treats transport closure as sufficient;
- what happens when manager session identity is not yet known;
- whether interruption errors reject stop, are recorded while cleanup
  continues, or have another exact disposition; and
- whether session-turn SSE and governed Agent 1 run SSE have the same or
  distinct obligations.

**Consequence:** transport `close` currently triggers canonical interruption,
but callback errors are swallowed and iterator termination remains a separate
condition (`runtime/packages/daemon/src/runtime-daemon.ts:398-443`). Treating socket destruction as both
transport cleanup and semantic turn cancellation would silently conflate two
states unless the human expressly selects and tests that contract.

### 7.3 Forced residual-connection behavior

The human must select:

- which residuals are force-terminated at the deadline (ordinary HTTP,
  keep-alive, SSE, and any upgraded/non-HTTP socket if applicable);
- the required client-visible result and whether any final SSE/HTTP terminal
  frame is attempted before force;
- whether force is best-effort or completion-gating;
- what `stop()` resolves/rejects with when residual force or close reports an
  error;
- whether socket-path and owner-record cleanup must proceed in `finally` even
  on close/interruption/force errors;
- the postcondition for tracked connections/sockets and runtime producers;
  and
- concurrent/repeated `stop()` and `start()` behavior, including restart after
  a forced shutdown.

**Consequence:** the implementation mechanism (Node server APIs versus
explicit socket tracking/destruction) is not selected here. E1's installed
Node behavior evidence should constrain that choice; this map only shows the
Root contract and source consequences.

## 8. Causality and process/SIGTERM calibration

- **EXECUTED FACT:** N1/H1 reproduced a Root mechanism: live SSE and incomplete
  ordinary HTTP held the current awaited close; completed keep-alive did not
  (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/MANAGER_RETURN.md:10-21,35-47`).
- **GAP:** that experiment did not establish that App R2's GUI connection was
  SSE/active HTTP or exclude Electron, signal, or environment factors
  (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/MANAGER_RETURN.md:18-21,94-104`; `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md:62-73`).
- **SOURCE FACT:** `RuntimeDaemon` contains no process signal handler and
  `stop()` does not exit the process (`runtime/packages/daemon/src/runtime-daemon.ts:39-102`). The H1 child
  fixture itself receives SIGTERM, calls `daemon.stop()`, and exits only after
  it resolves (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/fixtures/runtime-signal-sse-reproducer.mjs:72-92`).
- **APP-SOURCE FACT, not Root contract:** current App teardown awaits
  `runtimeHost.stop()` before logging `desktop.shutdown.completed`, while App
  code owns its Electron/signal funnel
  (`projects/chirality-app-dev/frontend/electron/main.ts:701-752,777-798,876-883`).
- **CONSEQUENCE:** a bounded Root `stop()` contract can remove the demonstrated
  indefinite-wait mechanism. It cannot by itself prove App first-SIGTERM
  receipt, App handler execution, or D-APP-88 completion. Owner Addition 4
  correctly holds the App notice until human acceptance of semantics **and** an
  accepted repair landing
  (`OWNER_RULING_TRANSCRIPT_2026-08-03.md:56-59`).

## 9. Exact source/test boundary

The authorized minimum candidate scope is limited to:

1. one accepted shutdown-contract surface;
2. `runtime/packages/daemon/src/runtime-daemon.ts`; and
3. bounded cases in `runtime/tests/daemon.test.ts` for the eight owner-named
   cases.

This map does not authorize bytes in those files. No need for a new runtime
owner, client-side substitute, App change, lifecycle change, register change,
or process-signal implementation is established here. If the selected
semantics cannot be implemented inside that boundary, the implementation
manager must return a scope-gap decision rather than silently expand it.
