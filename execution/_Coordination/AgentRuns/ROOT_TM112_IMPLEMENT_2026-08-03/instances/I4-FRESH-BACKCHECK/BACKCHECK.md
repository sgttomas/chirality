# I4 fresh final-hash backcheck

Verdict: `PASS_WITH_NONBLOCKING_FINDINGS`

No material finding survives this backcheck. The final candidate implements the
accepted G2+C1+F1 / N-STOP-1..7 semantics within the sealed product scope, and
both I2 material findings are closed. The only nonblocking finding is the
already-disclosed local inability to execute the Node 22.19 floor.

## Identity and scope gate

All sealed inputs matched before review and still matched after the prescribed
checks:

| Item | Required and observed SHA-256 |
|---|---|
| accepted implementation brief, pre-normalization authoring/execution identity | `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218` |
| accepted implementation brief, semantically identical whitespace-normalized publication identity | `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d` |
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` |
| `runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` |
| `daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` |
| I3 return | `ae10f7cf4ae395a9548f290da01973c405b0f6b0e1ecaad08c6a7f52b5418dab` |

The product diff is confined to the three authorized files: `docs/SPEC.md`
`+24/-0`, `runtime-daemon.ts` `+484/-67`, and `daemon.test.ts` `+598/-4`.
Section 14.1 is the only changed SPEC surface. No public timing input was added:
`RuntimeDaemonOptions` still contains only `socketPath`, `runtimeDirectory`,
and `service`; the sole production values are private constants
`STOP_GRACE_MS = 2_000` and `STOP_FORCE_SETTLE_MS = 500`.

## Independent semantic refutation

### N-STOP-1 — lifecycle, admission, ownership, and generations

`RuntimeDaemon` distinguishes `INITIAL`, `STARTING`, `RUNNING`, `STOPPING`,
`STOPPED`, `STOPPED_DEGRADED`, and `STOP_FAILED_CLEANUP`. `start()` sets
`STARTING` before its first await. `stop()` sets `STOPPING`, and
`performStop()` calls `beginServerClose()` before canceling streams. Each start
creates a distinct generation holding its server, tracked sockets, stream
controls, waiters, and owner-generation ID. Listener callbacks, socket close
callbacks, SSE controls, teardown, and owner removal retain that generation.
The concurrent lifecycle/restart test proves second-start rejection, identical
concurrent-stop Promise identity, stopped-stop no-op, authenticated same-instance
restart, metadata cleanup, and successful second stop.

### N-STOP-2 — exact finite grace

The first non-retry stop captures `performance.now() + STOP_GRACE_MS`, where the
constant is exactly 2,000 ms. Its wait uses only the remaining monotonic
deadline. The incomplete ordinary, stubborn SSE, pre-identity, prior-generation,
and force-settlement cases all reach force at the expected approximately
2,000-ms boundary. A cleanup retry does not repeat the grace-phase semantic
interruption work.

### N-STOP-3 — canonical SSE interruption and latch order

Every stream has one idempotent cancellation latch. Admission close begins
first; cancellation then invokes the canonical route-supplied
`interruptSession(projectId, sessionId)` once identity is available. Promise
settlements and iterator-return failures are observed. Disconnect and shutdown
share the same control. At force, a never-started interrupt becomes
`INTERRUPTION_IDENTITY_UNAVAILABLE`; an unsettled interrupt becomes timeout;
`forceExpired` prevents subsequent invocation.

M-I2-01 is closed: the Agent-1 wrapper captures a `managerSessionId` from any
later `harness:event`, and `sse()` now calls `trySseInterrupt(control)` after
every `iterator.next()`, before completion/emission handling. A non-identifying
first event followed by a pre-force identifying event therefore starts exactly
one interrupt. Conversely, the same retry returns immediately when
`forceExpired` is true. Both the frozen two-case adversarial suite and the
canonical later-identity and after-force cases pass.

### N-STOP-4 — force and residual transport

`beginServerClose()` marks and invokes `server.close()` before force is
possible. At the deadline, `forceGenerationTransport()` calls
`closeAllConnections()` and then destroys every socket remaining in the
closing generation's tracked set. Response, iterator-return, and interruption
promises are absent from the post-force settlement predicate and cannot extend
it. Tests cover incomplete ordinary transport, stubborn SSE, pre-identity SSE,
and an injected residual socket.

### N-STOP-5 — bounded settle and owned cleanup

Forced close callback/socket settlement is capped by the exact private 500-ms
constant. After that wait, the implementation records close timeout/residual
socket failures and still attempts control-socket unlink and generation-guarded
owner removal before classification. The observed injected-residual case
settled at 2,514 ms and classified `STOP_FAILED_CLEANUP`; after removal of the
residual, retry reached `STOPPED`.

M-I2-02 is closed: `controlSocketBound` starts false and becomes true only in
the listener's successful bind callback. Start-failure cleanup unlinks the
control path only when that flag is true. Thus a refusal before bind preserves
a foreign non-socket path or absent-socket/live-owner record; both canonical
assertions and the frozen adversarial case pass. If a later start step fails
after actual binding, the true flag still authorizes removal of that attempted
generation's socket. Owner cleanup remains independently fail-closed because
`removeOwnedRecord()` requires daemon ID, process ID, and exact generation ID.
Successful bound-listener shutdown proves socket and owned-record removal, and
the foreign-owner test proves another generation's record is retained.

### N-STOP-6 — errors, coalescing, no-op, and retry

`stop()` returns the stored Promise directly while work is in flight. Start is
permitted only from `INITIAL` or `STOPPED`, so concurrent start, start during
stop, and reuse from either failure state reject. Cleanup failures are collected
while later cleanup still runs. Clean transport/metadata with interruption
failure, timeout, or unavailable identity becomes `STOPPED_DEGRADED`; incomplete
transport or metadata becomes `STOP_FAILED_CLEANUP`. Retry bypasses stream
interruption/grace and retries incomplete transport/metadata only. The bounded
suite directly proves degraded reuse rejection, cleanup-failure retry, and
foreign-owner preservation.

### N-STOP-7 — restart isolation and claim boundary

Successful stop clears only the matching server/generation and permits a new
generation. Old stream/iterator/socket callbacks retain the old generation and
only notify or mutate its sets. Owner removal is generation guarded. The
late-event test releases an earlier iterator after restart and proves the new
owner bytes, authenticated health listener, and interrupt count remain
unchanged. Section 14.1 describes only daemon shutdown behavior. No App/R2
causality, process-level graceful-stop, or SIGTERM semantic claim was added;
the test fixture's unrelated `process:exit` UI event and ordinary PID ownership
checks do not make such a claim.

## Bounded matrix backcheck

| Matrix obligation | Direct evidence | Result |
|---|---|---|
| idle / no-op | lifecycle test plus clean after-each stops | pass |
| completed keep-alive | completed keep-alive case; early stop and empty free socket pool | pass |
| incomplete ordinary request | pending through grace, force/disconnect, owner held until terminal cleanup | pass |
| live SSE graceful | admission-first source order; one interrupt; canonical persisted interruption | pass |
| live SSE stubborn | force at grace, one interrupt, no acknowledgement wait, degraded reuse blocked | pass |
| pre-identity never yields / yields after force | identity-unavailable error, iterator return path, zero late interrupts | pass |
| bounded termination | exact constants; injected residual observes 2,514 ms total and cleanup failure | pass |
| disconnect/interrupt | one latch and one persisted `turn.interrupted` | pass |
| socket/owner cleanup | absence alone not success; owned removal and foreign retention | pass |
| cleanup failure/retry | first unlink failure, start blocked, second stop retries to `STOPPED` | pass |
| concurrent lifecycle | Promise identity, start rejection, stopped no-op | pass |
| restart/generation | authenticated restart and late-old-generation isolation | pass |

## Prescribed final-hash checks

Environment: macOS Darwin 25.6.0 arm64; Node `v24.18.0`; Vitest `v3.2.4`;
TypeScript `5.9.3` from `/Users/ryan/dev/chirality/runtime/node_modules`.
The three socket-using test commands ran outside the filesystem sandbox because
that restriction is known to deny Unix listener creation; no blocked attempt
preceded these one-time runs.

1. Strict full check:
   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/tsconfig.full-check.json`
   — exit 0; real 0.42 s.
2. Frozen I2 adversarial cases:
   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/adversarial.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/vitest.adversarial.config.mjs`
   — exit 0; 1 file / 2 tests passed; Vitest 2.35 s, real 2.54 s.
3. Canonical daemon suite:
   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run tests/daemon.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`
   — exit 0; 1 file / 15 tests passed; Vitest 13.33 s, real 13.52 s.
4. Full runtime suite:
   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`
   — exit 0; 8 files / 74 tests passed, including daemon 15/15; Vitest
   13.95 s, real 14.14 s.
5. Evidence-output build:
   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I4-FRESH-BACKCHECK/tsconfig.build-check.json`
   — exit 0; real 0.41 s; 47 JavaScript files / 404 KiB emitted only under
   the I4 evidence directory.

## Findings and residual gap

- `MATERIAL`: none.
- `NONBLOCKING / NB-I4-01`: Node 22.19 is not installed (`mise ls node` lists
  only 24.18.0), so the supported-floor compatibility run remains explicitly
  unexecuted. This is a coverage gap, not a claim of Node 22 compatibility.
- `NONBLOCKING / NB-I4-02`: the worktree has no local runtime dependency tree;
  the preserved configs deliberately use the installed main-checkout Node 24
  compiler, Vitest, types, and aliases against the current worktree sources.

No product repair was made. No register, receipt, App, Piping, DEL, lifecycle,
other source, or Git surface was touched. App routing, lifecycle acceptance,
publication, and human acceptance remain outside I4 authority.
