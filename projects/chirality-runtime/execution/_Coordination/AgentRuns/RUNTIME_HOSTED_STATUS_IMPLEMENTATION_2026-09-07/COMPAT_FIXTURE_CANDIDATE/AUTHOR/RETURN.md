# Compatibility fixture candidate — preparation only

One complete tests/supervisor.test.ts candidate is prepared outside live scope. The sole changed line is the private login service status fixture: pending/controlled-fixture now also includes schema chirality-hosted-login-status/v2, unavailable binding schema/reason, and hostedReady:false. All assertions and other bytes are preserved exactly; replacement reversal reproduces the original byte-for-byte. No live test or source file changed, and no tests ran.

The old fixture is rejected by the newly strict supervisor server/client validator. This candidate restores the intended positive-channel fixture; it does not weaken validators or alter the channel assertions. The existing bad-token rejection, start/cancel counts, pending status and empty worker inventory assertions remain unchanged.

## Execution effects for owning disposition

Selecting only `keeps login commands on the private authenticated capability channel` would create an owned temporary directory, start a real private Unix socket server, generate in-memory synthetic supervisor capability material, send authenticated and rejected local socket requests, and close/remove owned resources. ProcessSupervisor construction is inert; the selected case never calls acquire, so its configured Node command is never launched. No supplier, provider endpoint, user credential store, keyring or protected operation is required.

This file has no shared before/after hooks. Its full suite does launch Node workers, process groups and descendant fixtures, including recovery and bounded kill cases. A selected-case authorization must not be read as authorization for the full suite. Direct imports use process-supervisor.ts and supervisor-server.ts; these source import chains have no runtime-conformance import or eager production inventory. Codex login/manager imports in supervisor-server are type-only. If a later runner adds a core barrel or other hooks, its eager import effects must be inspected separately; the previous custody-suite inventory disposition does not conceal those effects.

Closure: candidate frozen for parent review and separate owning disposition; application and execution remain pending because this test is outside the original fifteen live paths. No new status contract, authority, qualification or deployment claim. OpenAI GPT-6; exact serving identifier unavailable; nondelegating Agent2 role instruction-asserted.
