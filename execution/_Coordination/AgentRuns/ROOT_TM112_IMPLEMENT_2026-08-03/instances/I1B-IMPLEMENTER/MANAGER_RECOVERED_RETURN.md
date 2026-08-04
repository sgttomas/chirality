# I1B manager-recovered terminal output

Status: `PRODUCT BYTES FROZEN / AUTHOR INTERRUPTED AFTER GREEN EVIDENCE / MANAGER-RECOVERED RETURN`
Failure class for the missing child return: `AGENT_RETURN_TIMEOUT_POSTVALIDATION`
Scope posture: `WITHIN AUTHORIZED THREE PRODUCT FILES`

The I1B Agent 2 produced the bounded candidate and repeatedly reported test
results, but did not write its promised terminal `RETURN.md` after explicit
manager requests. HELP_HUMAN directed the manager to interrupt it, freeze the
product bytes, preserve the reported evidence, independently rerun final-hash
checks, and proceed to fresh refutation. This file is a manager recovery; it is
not represented as an Agent 2-authored return.

## Frozen product identity

| File | Diff from sealed basis | Frozen SHA-256 |
|---|---:|---|
| `docs/SPEC.md` | +24 / -0 | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` |
| `runtime/packages/daemon/src/runtime-daemon.ts` | +477 / -67 | `bbee7e403942808c2de18cbcc02cbb2919598bcd8d6049da2da7dfcdb02ada76` |
| `runtime/tests/daemon.test.ts` | +529 / -2 | `d36f76dea9b8dcdf1d078ff98d9474ed171a63e0d3da0ff244c4a417fb38d25b` |

`git diff --check` passed on all three files. No public timing override was
introduced. Product constants are exactly `STOP_GRACE_MS = 2_000` and
`STOP_FORCE_SETTLE_MS = 500`.

## Semantic implementation map

- N-STOP-1: explicit initial/starting/running/stopping/stopped/degraded/cleanup-
  failure lifecycle; start transition occurs before asynchronous setup;
  generation IDs bind listener, sockets, SSE controls, callbacks, owner
  record, teardown, and late events.
- N-STOP-2: first `STOPPING` transition captures its immutable monotonic
  2,000-ms deadline; `server.close()` begins before cancellation dispatch;
  active SSE controls share one cancellation latch and request the canonical
  `interruptSession` at most once when identity is available.
- N-STOP-3: pre-identity cancellation retries when the first harness event
  supplies identity; force expires the latch and forbids late interrupt.
  Iterator return is observed after graceful canonical persistence drains, or
  requested at force for stuck/pre-identity streams.
- N-STOP-4: deadline force calls `closeAllConnections()` only after close was
  initiated and destroys all generation-tracked residual sockets.
- N-STOP-5: forced transport receives no more than 500 additional ms for close
  callback/socket settlement; response/interruption promises do not extend it;
  socket unlink and generation-guarded owner cleanup are still attempted.
- N-STOP-6: concurrent stop returns the identical stored Promise; stopped stop
  is a no-op; start concurrency/failure states reject; complete cleanup is
  attempted before collected errors are reported; cleanup retry touches only
  incomplete transport/metadata work.
- N-STOP-7: successful stop supports authenticated same-instance restart;
  prior-generation late iterator/socket/callback events cannot unlink or
  mutate the new owner/listener; clean interruption failure becomes
  `STOPPED_DEGRADED`, incomplete cleanup becomes `STOP_FAILED_CLEANUP`.

## Frozen-hash deterministic validation

Environment: macOS Darwin 25.6.0 arm64; Node `v24.18.0`; Vitest `v3.2.4`;
TypeScript from `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc`.

1. Full package-scope strict check:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/tsconfig.full-check.json`

   Result: exit 0, 0.29 s.

2. Frozen bounded daemon suite:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run tests/daemon.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`

   Result outside the filesystem sandbox: 1 file / 14 tests passed, 11.30 s.
   Timed observations: incomplete ordinary force 2,016 ms; stubborn degraded
   2,043 ms; pre-identity degraded 2,086 ms; prior-generation restart 2,110 ms;
   injected residual force-settle cap 2,515 ms. An initial sandboxed attempt
   failed 12 socket-using cases with macOS `listen EPERM`; it was correctly
   classified as an execution-permission failure and rerun outside that
   restriction.

3. Frozen full existing runtime suite:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`

   Result outside the filesystem sandbox: 8 files / 73 tests passed, 11.87 s;
   daemon matrix 14/14 passed within that run.

4. Evidence-output build check:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/tsconfig.build-check.json`

   Result: exit 0, 0.27 s; 47 emitted JavaScript files / 404 KiB under the
   authorized I1B `build-output/` evidence directory. No runtime package
   `dist/` path was written.

## Bounded matrix coverage

The final daemon suite contains direct cases for idle/no-op/coalescing/start
concurrency/restart; completed keep-alive; incomplete ordinary force; graceful
live SSE; stubborn live SSE/degraded; pre-identity never-yields and late-yield;
2,000+500 bounded termination; disconnect canonical persistence; metadata and
foreign-owner cleanup; injected cleanup failure/retry; and prior-generation
late-event isolation. The suite also retains the pre-existing authentication,
wire-format, pre-stream failure, and stale-owner checks.

## Gaps and holds

- Node 22.19 is not installed locally (`mise ls node` lists only 24.18.0), so
  the supported floor remains an explicit unexecuted compatibility gap.
- The worktree intentionally has no `runtime/node_modules`; exact package
  scripts could not be invoked in-place. Equivalent current-worktree source
  checks used the installed main-checkout compiler/Vitest with explicit alias
  and output configs preserved in this carrier.
- I1B did not author a terminal return. The fresh refuter must treat this
  manager recovery and the final product hashes—not earlier author messages—as
  its input identity.
- This is an implementation candidate only. App routing, lifecycle acceptance,
  Git action, process/SIGTERM claims, and human acceptance of the repair remain
  held.
