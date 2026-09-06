# Supervisor implementation return

Agent: bounded ephemeral Agent 2, OpenAI GPT-6; exact serving model ID unavailable. Role not mechanically enforced, instruction-asserted. No descendants dispatched.

## Delivered

`ProcessSupervisor` implements the exact additive supervisor port. Its executable, arguments, environment and cwd come exclusively from trusted constructor configuration; ambient environment defaults to empty. Caller input is stdin only. Worker IDs use the canonical safe-identifier grammar and input sizes are checked; duplicate acquisition rejects. Acquisition awaits actual spawn and rejects launch failure without a phantom handle. Inventory defaults to a 64-entry capacity, including cached exits; concurrent acquisition cannot exceed it. Handles carry fresh generations, terminal results remain cached until retirement. Lifetime defaults to 30 seconds and output defaults to 64 KiB per stream; overruns kill the process group. Retirement sends TERM then bounded-delay KILL, including descendants in the same group. Normal leader exit also kills surviving group descendants, including inherited-pipe holders. `close()` retires every managed entry.

`startSupervisorServer({socketPath, supervisor, recoverStale?})` returns a broker-private credential and `close()`. `SupervisorClient({socketPath, credential, timeoutMs?})` implements the same port. Unix-only socket, owner-private 0700 directory, 0600 socket, symlink ancestor rejection and same-UID owner validation. Stale recovery probes the old socket, refuses an active owner and checks inode before removal. Every new owner generates a new epoch and secret; every request authenticates a HMAC bound to owner/epoch/operation/worker/generation/input. The secret is not sent as the request token. Old credentials fail after recovery. Each connection accepts one bounded frame with a fixed operation vocabulary; errors and responses are bounded. No public daemon route or command passthrough is introduced here.

## Validation

`npx vitest run tests/supervisor.test.ts`: 10 passed, 2026-09-06 (local displayed time 20:51:26); real child execution and teardown, cached exits, duplicate IDs, stale generations, token/owner/epoch mismatch, operation/authentication tampering, overlarge frames, active owner refusal, real SIGKILL owner crash/stale socket recovery, worker lifetime kill, output flood kill, symlink refusal, spawn-failure cleanup, concurrent/cached inventory capacity, and actual inherited-pipe grandchild cleanup after normal leader exit.

Initial sandbox execution could not bind private Unix sockets (EPERM); authorized sandbox escalation ran the actual tests, no simulation. Workspace `npm run typecheck` passed before concurrent integration; latest repeat reports only the manager-owned `delegated-runtime.ts:73` contract error union mismatch. Parent notified to rerun after integration. One mistaken typecheck from repo root had no package.json and was corrected; not counted as a check.

## Integration and limits

Manager owns index exports and daemon integration. It must close both process supervisor and socket server during broker teardown. These controlled process tests do not establish hosted provider conformance, OS hard containment, production two-job deployment, or deliverable acceptance. Trusted command configuration remains responsible for the approved outer process/filesystem/network envelope; this module does not manufacture a sandbox. Workers deliberately escaping their process group are outside this process-group termination guarantee. No holds, status or authority records changed.
