# HELPS_HUMANS manager return — N1 TM-ROOT-112 investigation

RunID: `ROOT_TM112_DECISION_PREP_2026-08-03`
Node: `N1`
Verdict: `PASS — ROOT MECHANISM REPRODUCED; APP CAUSAL ATTRIBUTION REMAINS UNPROVED`
Artifact class: `DERIVATIVE EXECUTED INQUIRY — NON-AUTHORITATIVE`

## Outcome first

At exact HEAD/origin-main
`88e7590d3664d4f1daf91bed2a8899bda0748b92`, a live SSE response keeps the
exact `RuntimeDaemon.stop()` call awaiting Node `server.close()`. This occurred
in two direct runs and one child-process SIGTERM run. A completed ordinary
keep-alive JSON request did not block stop; an incomplete ordinary HTTP request
did. Client release allowed stop to resolve, owner cleanup to complete, and the
SIGTERM child to exit zero.

Therefore the Root-level mechanism proposed by the App notice is reproduced,
not disproved. The experiment does not prove that the App R2 GUI connection
was in fact an SSE/active-request connection or that no Electron/signal factor
also contributed; that App-specific causal attribution remains unproved.

## Bound basis

- Source revision and `origin/main`:
  `88e7590d3664d4f1daf91bed2a8899bda0748b92`.
- App notice SHA-256:
  `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`.
- `runtime-daemon.ts` SHA-256:
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`.
- Copied source and lockfile matched the repository; dependency install/build
  occurred only under `/tmp/chirality-tm112-runtime.iID3BU`.
- Environment: macOS 26.6 arm64; Node v24.18.0; npm 11.16.0.

## Executed evidence

| Case | Executed outcome |
|---|---|
| Idle daemon | stop resolved in 0.811-0.833 ms; socket and owner absent |
| Completed ordinary keep-alive JSON client | client was connected and not destroyed before stop; stop resolved in 0.318-0.357 ms; client destroyed; socket/owner absent |
| Incomplete ordinary HTTP request | stop remained pending at 750 ms in both runs; socket absent but owner remained mode 0600; destroying client let stop resolve at 752.857-755.726 ms total and owner was removed |
| Live SSE response | HTTP 200 `text/event-stream` and first frame received; stop remained pending at 750-751 ms in both runs; socket absent but owner remained; destroying client invoked one interruption and let stop resolve at 771.955-772.037 ms total |
| Child process, live SSE, SIGTERM | child PID 33719 received SIGTERM and was still alive at 750 ms; socket absent and owner present; after controlled client release stop resolved at 755.196 ms, owner disappeared, and child exited 0 without a terminating signal |

The existing exact-source daemon suite also passed 5/5 outside the
socket-restricted sandbox, but inspection confirms it has no stop-with-live-
ordinary-client or stop-with-live-SSE case.

Raw transcribed values, environment, commands, fixture hashes, and executable
fixtures are under `instances/H1-TM112-INVESTIGATION/evidence/`.

## Static facts versus executed proof

- **Accepted-source/current implementation fact:** `stop()` sets its server
  reference undefined, awaits `server.close()`, then unlinks the socket and
  removes its owned record. It contains no explicit active connection/response
  cancellation, timeout, or forced-close step.
- **Executed proof:** the exact built implementation remains pending with a
  live SSE or incomplete ordinary request and proceeds after client release.
- **Executed nuance:** on this Node/macOS environment the Unix socket pathname
  disappears when `server.close()` begins, before its callback resolves; the
  owner record remains until the awaited close completes. Socket absence alone
  therefore did not prove completed teardown.
- **Static contract gap:** accepted Root SPEC/README define authenticated
  HTTP/1.1/SSE over the Unix socket and expose daemon stop, but do not state
  active-connection drain/termination behavior or a shutdown time bound. The
  DEL-02-06 material's “drain” decisions concern turn/model-residency accounting
  and do not supply this connection-shutdown contract.

## Warranted scope and gate

A Root contract/source/test change is warranted. N1 does not select the exact
semantics and did not implement anything. The smallest candidate tranche is:

1. accountable-human selection and acceptance of active request/SSE shutdown
   semantics, finite boundary, residual termination, client interruption, and
   cleanup guarantees;
2. the accepted runtime contract surface plus
   `runtime/packages/daemon/src/runtime-daemon.ts`; and
3. bounded `runtime/tests/daemon.test.ts` regression cases asserting stop
   completion, client termination/interruption, socket and owner cleanup, and
   restart with idle, completed keep-alive, incomplete request, and live SSE.

`NOTICE_TO_HELP_HUMAN.md` presents the gate. Recommendation: a separate
bounded TM-ROOT-112 decision/implementation tranche, because TM-ROOT-112 is
HIGH and directly blocks App D-APP-88; routing into TM-ROOT-121 remains a
lawful but slower alternative.

After an accepted Root repair, the next App step is an exact post-GUI
first-SIGTERM rerun preserving the signal command/time, helper PID/liveness,
the transport/request type active at signal time, socket path plus owner record,
client disconnect/interruption, shutdown logs, exit code, and restart outcome.

## Coverage gaps

- Executed only on Node v24.18.0/macOS arm64, not the full supported Node
  `>=22.19.0` or other platforms.
- SSE used the exact daemon route and stop method with a stub RuntimeService;
  it was not a real App/Electron GUI or persisted turn.
- The 750 ms boundary proves bounded non-completion, not mathematical
  permanence; controlled client release establishes the dependency.
- Multiple clients, connection races, stalled response-before-first-frame,
  persistence behavior, and restart under a candidate repair were not tested.
- App R2's second-signal behavior was not reproduced or explained.

## N1 closure

`N1 COMPLETE / PASS FOR HELP_HUMAN FAN-IN`. Inquiry objective met; source
repair and App acceptance remain open behind the recorded human/owner gate.
N2 and N3 were not released or modified.

