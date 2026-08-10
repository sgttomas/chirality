# Attempt-6 preparation-only command approval request — D-APP-92 Option A

Status: `OWNER APPROVAL REQUIRED BEFORE C217`

Attempt 5 is accepted only for narrow offline package construction, package
identity/topology, and cleanup. Its sole package invocation was consumed and
all package/runtime state was removed. No real runtime continuation is inferred.

The next runtime graph must coordinate an interactive LLDB PTY with a separate
controller that owns the exact direct-child helper PID and fixed replay clock.
Two bounded packet preparers identified that tool-shape dependency but could not
safely freeze the real graph without live orchestration evidence. Proposed
amendment v1.14 therefore requests only C217-C230: a no-target LLDB PTY check and
a mock two-session `/bin/sleep` PID/sentinel handshake with mandatory cleanup.

This does not attach LLDB to any process, reconstruct/package product, launch a
helper or GUI, send a signal, exercise replay, or read credentials. A passing
probe permits preparation of a fresh real-runtime packet only; that later packet
will still need a new owner grant for its one package invocation and runtime
commands. Existing C196/C197 approval remains preserved and unused.

## Exact owner return token

`APPROVE D-APP-92 ATTEMPT 6 PREPARATION COMMANDS C217-C230 — NO-TARGET LLDB PTY AND MOCK TWO-SESSION DIRECT-CHILD PID/SENTINEL HANDSHAKE ONLY — NO ATTACH, PACKAGE, CACHE SEED, NETWORK, HELPER, GUI, SIGNAL, REPLAY, CREDENTIAL, RELEASE, GIT, OR OTHER AUTHORITY`
