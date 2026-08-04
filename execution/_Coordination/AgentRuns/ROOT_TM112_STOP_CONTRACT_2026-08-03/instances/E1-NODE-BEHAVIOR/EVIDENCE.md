# E1 Node behavior evidence

Status: `COMPLETE / PRIMARY EXECUTABLE EVIDENCE ON THE BOUND NODE`

This packet separates executable observations from declaration and source
inference. The executable observations bind only Node v24.18.0 on Darwin arm64.

## 1. Basis and environment

Repository inputs:

- `runtime/package.json` SHA-256
  `499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071`;
  it declares Node `>=22.19.0` and `@types/node` `24.12.4`.
- `runtime/package-lock.json` SHA-256
  `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f`;
  lines 913–915 resolve `@types/node` exactly to `24.12.4`.
- `runtime/packages/daemon/src/runtime-daemon.ts` SHA-256
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`.
- Prior controlled application evidence:
  `../../../ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json`.

Exact environment commands and output:

```text
$ node --version
v24.18.0

$ node -p 'process.execPath'
/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node

$ node -p 'process.platform+" "+process.arch'
darwin arm64

$ uname -a
Darwin Mac.lan 25.6.0 Darwin Kernel Version 25.6.0: Sat Jul 11 15:27:04 PDT 2026; root:xnu-12377.161.13~4/RELEASE_ARM64_T6050 arm64

$ sw_vers
ProductName: macOS
ProductVersion: 26.6
BuildVersion: 25G72
```

Only v24.18.0 was installed (`mise ls node` and the installed-node directory
listing exposed no Node 22 executable), so the support floor could not be
executed locally.

## 2. Locked declarations

A disposable copy of `runtime/` was installed without network access:

```text
$ npm ci --offline --ignore-scripts
added 61 packages, and audited 69 packages in 262ms
found 0 vulnerabilities
```

The installed declaration package reported `@types/node` `24.12.4`.
Relevant declarations and comments were:

```text
/tmp/e1-node-types-20260803/node_modules/@types/node/http.d.ts:487-496
Closes all connections connected to this server.
closeAllConnections(): void;
Closes all connections connected to this server which are not sending a request
or waiting for a response.
closeIdleConnections(): void;

/tmp/e1-node-types-20260803/node_modules/@types/node/net.d.ts:639-647
server is finally closed when all connections are ended and the server emits a
'close' event. The optional callback will be called once the 'close' event
occurs. Unlike that event, it will be called with an Error ... if the server was
not open when it was closed.
close(callback?: (err?: Error) => void): this;
```

Declaration hashes:

```text
060d305fe4494d8cb2b99d620928d369d1ee55c1645f5e729a2aca07d0f108cb  http.d.ts
3806cdd6b48ba01a9198134e62a384ec217a98f316d4baef74dd46d62c947a63  net.d.ts
```

Declaration inference: `close()` owns the listening close lifecycle and has a
completion signal; `closeIdleConnections()` and `closeAllConnections()` return
`void` and provide no independent completion signal or stop-listening promise.
The declarations do not state a time bound, application-cancellation behavior,
upgrade behavior, cleanup behavior, or restart serialization.

## 3. Installed executable implementation inspection

Node's installed builtin JavaScript was inspected without modification:

```sh
node -e 'const s=process.binding("natives")._http_server; /* print relevant slices */'
node -e 'const s=process.binding("natives").net; /* print relevant slices */'
```

Exact builtin-source SHA-256 values:

```text
_http_server 08a248b4a3e3ff74f3a43242ffa48c58a3f360183608dcdeb6528a40fec8d130
net          de8f10a443606c5fb32a53978f072dce805f533bfb0ebf4c988bde80aa74d792
```

Relevant v24.18.0 implementation excerpts:

```js
function httpServerPreClose(server) {
  server.closeIdleConnections();
  clearInterval(server[kConnectionsCheckingInterval]);
}

Server.prototype.close = function close() {
  httpServerPreClose(this);
  ReflectApply(net.Server.prototype.close, this, arguments);
  return this;
};

Server.prototype.closeAllConnections = function closeAllConnections() {
  if (!this[kConnections]) return;
  const connections = this[kConnections].all();
  for (let i = 0, l = connections.length; i < l; i++) {
    connections[i].socket.destroy();
  }
};

Server.prototype.closeIdleConnections = function closeIdleConnections() {
  if (!this[kConnections]) return;
  const connections = this[kConnections].idle();
  for (let i = 0, l = connections.length; i < l; i++) {
    if (connections[i].socket._httpMessage &&
        !connections[i].socket._httpMessage.finished) continue;
    connections[i].socket.destroy();
  }
};
```

The installed `net.Server.prototype.close` source removes its listening handle,
then emits `close` on a later `process.nextTick` only when neither a handle nor
connections remain. If no handle exists, each supplied callback is attached to
the next `close` event through a wrapper that supplies
`ERR_SERVER_NOT_RUNNING`.

These internals explain the observations but are not a public compatibility
contract. In particular, connection-tracker classification is an internal
implementation detail and may differ across Node releases.

## 4. Executable probe

Fixture:
`probe-node-http-stop.mjs`, SHA-256
`e1d22806e0a38cbd4da57f9b35a2cd840869dd2059b8ca1a5449bbff278108a1`.

It uses only local Unix-domain sockets under `/tmp`; it creates no IP listener
and makes no network request. The socket-bearing invocations ran outside the
filesystem sandbox because the sandbox denies local `listen`, matching the N1
environmental finding.

Exact invocations:

```sh
node /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/instances/E1-NODE-BEHAVIOR/probe-node-http-stop.mjs /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/instances/E1-NODE-BEHAVIOR/PROBE_RESULTS.json
node /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/instances/E1-NODE-BEHAVIOR/probe-node-http-stop.mjs /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/instances/E1-NODE-BEHAVIOR/PROBE_RESULTS_REPEAT.json
```

Both invocations completed 27 matrix cases. Result hashes:

```text
0f189a4b4aec299baf0713f2b5ac80f699ff81e18b837d266d44e0bb3f8ae94e  PROBE_RESULTS.json
cbb55139c54c5b4e6186eb59ebe06b88fecc11bb072f2708658dcbd398777d62  PROBE_RESULTS_REPEAT.json
```

This comparison exited zero with no output:

```sh
diff \
  <(jq 'del(.executedAt,.environment.pid)' PROBE_RESULTS.json) \
  <(jq 'del(.executedAt,.environment.pid)' PROBE_RESULTS_REPEAT.json)
```

Thus every recorded semantic field reproduced; only execution timestamp and
PID differed.

## 5. Executable results

The boundary was 80 ms. `pending` below means the close callback had not fired
at that boundary and the server-side connection remained tracked. Every
pending case resolved after the fixture explicitly destroyed its tracked
socket during cleanup.

| Connection state | `close()` | `closeIdleConnections()` | `closeAllConnections()` |
|---|---|---|---|
| accepted socket, no bytes | pending; listener stopped | preserved; listener remained | destroyed; listener remained |
| completed HTTP keep-alive | closed; listener stopped | destroyed; listener remained | destroyed; listener remained |
| incomplete headers | pending; listener stopped | preserved; listener remained | destroyed; listener remained |
| incomplete request body | pending; listener stopped | preserved; listener remained | destroyed; listener remained |
| live SSE response | pending; listener stopped | preserved; listener remained | destroyed; listener remained |
| upgraded connection | pending; listener stopped | preserved; listener remained | preserved; listener remained |

Source: both result files, `matrix` entries for operations `close`,
`closeIdleConnections`, and `closeAllConnections`.

Ordering combinations:

- `close()` followed immediately by `closeAllConnections()` stopped listening
  and completed close for accepted/no-bytes, incomplete headers, incomplete
  body, and SSE. It did not complete for the upgraded connection. See `matrix`
  entries with operation `closeThenCloseAll`.
- `close()` followed by `closeIdleConnections()` did not complete for
  accepted/no-bytes, incomplete headers/body, or SSE. See `closeThenCloseIdle`.
- Both connection-closing helpers left `server.listening === true` and the
  server accepted a new request afterward. See `acceptsAfterConnectionClosers`.
- A socket set populated from the server's `connection` event included the
  upgraded socket. After `close()` remained pending, destroying that tracked
  socket allowed close to complete and the client observed destruction. See
  `trackedSocketDestroyUpgrade`.

Callback and event behavior:

- `close()` returned the server synchronously. `close` event and callback were
  later than the caller's `after-close-call` marker.
- Closing a never-listened or already-closed server delivered
  `ERR_SERVER_NOT_RUNNING` to the callback.
- Two close calls issued before the first no-connection close event produced a
  successful first callback and `ERR_SERVER_NOT_RUNNING` in the second callback;
  both ran off the same later `close` event.
- With the probe's close-event listener registered before `close()`, the event
  listener ran before the callback.

Source: `callbackAndOrdering` in both result files. Listener execution order is
registration-sensitive; only “callback occurs once the close event occurs” is
supported by the declaration.

Restart behavior:

- The same `http.Server` successfully listened, served, and closed for two
  sequential generations after the preceding close callback completed. See
  `repeatedListen`.
- While an old SSE generation was draining after `close()`, a fresh server
  successfully bound the same Unix-socket pathname and served a request. The
  old close callback remained pending until its old socket was destroyed. See
  `overlappingGenerations`.

The second observation establishes that Node does not serialize daemon
generations by socket pathname. It does not establish cross-platform pathname
behavior.

## 6. Consequences for current RuntimeDaemon

These are source inferences, not additional executable observations:

1. `RuntimeDaemon.stop()` at lines 90–101 awaits only `server.close()`. It has
   no grace bound, active-response cancellation step, `closeAllConnections()`,
   socket registry, or forced residual-connection step. The probe therefore
   explains why incomplete requests and SSE can hold its promise indefinitely.
2. Completed keep-alive connections require no extra helper on the bound Node:
   the installed implementation calls `closeIdleConnections()` before
   `net.Server.close()`, and the probe saw immediate completion.
3. `body()` at lines 354–370 awaits request EOF; an incomplete body remains
   active. `sse()` at lines 388–443 can remain active while its iterator remains
   live. Node's close APIs do not define how to terminate those application
   operations.
4. A force step based only on `closeAllConnections()` would still miss upgraded
   connections on the bound runtime. Tracking sockets from `connection` and
   destroying residuals covered that class in the probe.
5. `stop()` sets `this.server = undefined` before the old close completes.
   A concurrent second `stop()` therefore skips `server.close()` and can reach
   socket/owner cleanup while the first stop is pending. A concurrent `start()`
   is no longer rejected by the `server !== undefined` guard, though current
   owner-record recovery may reject it. These races require an application
   lifecycle state or shared stop promise; Node does not supply one.
6. Node allowed a replacement listener on the same pathname while the old
   generation still had an active connection. Cleanup must therefore be
   generation-owned and restart must await the accepted stop terminal state.

## 7. What the APIs do not guarantee

The inspected public declarations and executable behavior provide no guarantee
of:

- a maximum close duration;
- application-level cancellation, iterator completion, or session interruption;
- an HTTP response or SSE terminal event before forced destruction;
- upgraded/raw socket closure by the HTTP connection helpers;
- a callback from either connection-closing helper;
- prevention of new accepts unless `close()` is ordered first;
- owner-record or socket-path cleanup;
- stop idempotence, concurrent stop coalescing, or restart serialization;
- equal connection classification/timing on Node 22.19, Linux, or Windows.

`socket.destroy()` is forcible transport teardown, not graceful application
completion. It can truncate requests/responses. The probe establishes that it
unblocks the server close lifecycle; it does not establish delivery semantics
to the peer.

## 8. Caveats and remaining gaps

- Executable coverage is Node v24.18.0, Darwin arm64, macOS 26.6, local IPC.
- Node 22.19.0 was not locally installed, so the declared support floor remains
  an explicit CI/compatibility-test requirement.
- Windows named pipes and Linux Unix sockets were not executed. The pathname
  rebinding observation is platform-specific until repeated there.
- HTTP/2 was not in scope because the daemon creates `node:http` HTTP/1.1 only.
- Upgrade behavior was tested with a generic HTTP/1.1 upgrade, not a WebSocket
  library. It is sufficient to show the class escapes `closeAllConnections()`.
- No timing claim beyond “settled or still pending at the bounded observation”
  is made. The APIs expose no grace-duration policy.
