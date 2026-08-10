# Attempt-7 preparation-only command approval request — D-APP-92 Option A

Status: `OWNER APPROVAL REQUIRED BEFORE C231`

The fresh Attempt-6 adversarial verifier at SHA-256
`fed5aa422277720f2d74d8cfefe042f82ba76b7a8b05ac9d05889c143c91a5b5`
accepted only a bounded timing/order repair. Attempt 6 already proved the
no-target LLDB PTY shape, so this request does not rerun LLDB. Its mock
controller timed out after five seconds even though session B later produced a
schema-valid sentinel carrying the matching direct-child PID.

Proposed amendment v1.15 requests only C231-C244. It replaces only the mock
controller with a hash-bound v2 that durably emits its `ATTACH_READY` record
immediately, registers child exit before any wait, allows a bounded 30-second
sentinel window, and produces a result only after exact schema/PID/state match
and natural exit of its sole direct child `/bin/sleep 35`. Session B uses the
existing byte-identical script. The protocol root is fixed, total execution is
bounded, and only `protocol-result.json` may be copied. After every controller
start, a separate mandatory gate first polls only that existing session to a
confirmed terminal state without bytes, signals, or process inspection; only
then may exact root cleanup run. A quiescence timeout blocks cleanup rather
than deleting state beneath a possibly live controller.

Passing C231-C244 permits preparation of a fresh real-runtime packet only. It
does not authorize that packet or any real-runtime action. Existing C196/C197
approval remains preserved and unused.

## Exact owner return token

`APPROVE D-APP-92 ATTEMPT 7 PREPARATION COMMANDS C231-C244 — TIMING-ONLY MOCK TWO-SESSION DIRECT-CHILD PID/SENTINEL HANDSHAKE RETRY WITH TERMINAL-SESSION-BEFORE-CLEANUP GATE — NO LLDB, ATTACH, PACKAGE, CACHE SEED, NETWORK, HELPER, GUI, SIGNAL, REPLAY, CREDENTIAL, MEMORY, ENVIRONMENT DUMP, PROCESS INSPECTION, RELEASE, GIT, OR OTHER AUTHORITY`
