# Independent review: App-owned stock Codex host replatform (D-GOV-43 A2)

Reviewer: Type 2 independent reviewer, Claude Fable 5.1, medium reasoning, no
delegation. Read-only source review on the worktree checkout at HEAD
`886eb2707` (PR #774) against base `e83cb1f47`, reviewed as
`git diff e83cb1f47..886eb2707 -- projects/chirality-runtime/packages projects/chirality-app-dev/frontend/{electron,scripts,src,package.json}`
together with the complete final files of every product module the diff
touches. AGENTS.md, REVIEW_BRIEF.md, the R16 pattern record and
SPIKE_DESIGN.md were read first. No product, test or coordination file other
than this record was edited; nothing was staged, committed, pushed or
stashed; no App, Electron, packaging, signing, window or network was run; the
running App instance and `/private/tmp/claude-501` were left alone; no live
identity, auth, token, binding, keychain, Codex home, session or event file
was read. Source files and checked-in fixtures were the only inputs.

Path prefixes for `file:line` references below: `runtime/` means
`projects/chirality-runtime/`; `frontend/` means
`projects/chirality-app-dev/frontend/`.

## Verdict: PASS

No blocking finding. The turn registry, the stock app-server client, the
effective-home overlay, the login relay, the supervisor, the delegated
runtime, the Electron service host and the packaging scripts implement the
spike design as written, and the diff removes the retired supply-model code
without leaving live references. One Medium, three Low and five
Informational findings are recorded below, plus the test gaps. The Medium
finding (shutdown budgets nest 5 s inside 5 s and a hard-killed service can
leave a session permanently `running`) deserves a follow-up before the spike
is relied on for daily use, but it is a bounded lifecycle repair, not a
correctness, duplication, instruction or authentication defect.

## Commands run

| Command (cwd) | Result |
|---|---|
| `npx tsc -b --pretty false` (`runtime/`) | exit 0, no diagnostics |
| `npm run typecheck` (`frontend/`) | exit 0 |
| `npx vitest run tests/turn-registry.test.ts tests/delegated-runtime.test.ts tests/codex-supervisor.test.ts tests/codex-app-server-client.test.ts tests/codex-effective-home.test.ts tests/app-owned-composition.test.ts tests/standalone.test.ts tests/daemon.test.ts tests/runtime-daemon-signal.test.ts tests/process-supervisor.test.ts tests/instruction-basis-and-method-transition.test.ts` (`runtime/`, vitest 3.2.7) | 11 files passed, 85 tests passed, 0 failed, 0 skipped, 14.77 s |
| `npx vitest run src/__tests__/electron/runtime-service-host.test.ts src/__tests__/electron/codex-executable.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/desktop-log.test.ts src/__tests__/scripts/pack-electron.test.ts src/__tests__/scripts/verify-codex-pin.test.ts src/__tests__/scripts/sign-electron-runtime-v2.test.ts src/__tests__/scripts/finalize-electron-resources.test.ts src/__tests__/scripts/verify-packaged-dependency-boundary.test.ts src/__tests__/scripts/build-electron.test.ts src/__tests__/api/harness/turn-registry-routes.test.ts src/__tests__/api/harness/hosted-bootstrap.test.ts src/__tests__/components/chat-panel-turn-attach.test.tsx src/__tests__/components/request-card.test.tsx src/__tests__/components/hosted-bootstrap.test.tsx src/__tests__/lib/harness-client-turn-registry.test.ts src/__tests__/lib/harness-event-views-codex.test.ts src/__tests__/lib/hosted-bootstrap-client.test.ts src/__tests__/lib/runtime-daemon-harness-port.test.ts src/__tests__/components/chat-panel-runtime-reconnect.test.tsx src/__tests__/components/shell-frame-runtime-connectivity.test.tsx` (`frontend/`, vitest 4.1.10) | 21 files passed, 167 tests passed, 0 failed, 0 skipped, 1.98 s |

Per runtime file: codex-effective-home 4, turn-registry 7, process-supervisor
2, codex-supervisor 6, codex-app-server-client 7, delegated-runtime 9,
instruction-basis-and-method-transition 14, standalone 5,
runtime-daemon-signal 2, app-owned-composition 9, daemon 20.

Working-tree note: `RUN_LOG.md` was already modified and `REVIEW_BRIEF.md`
already untracked in this worktree before the review began; neither was
touched.

## Q1: Turn ownership and reconnection

Answer: the Runtime owns every turn; the renderer only observes. Frames are
numbered, replay is by `after=`, retention is bounded, keepalives flow on
both hops, and the chat panel recovers without re-sending anything.

- Sequence numbers are 1-based and contiguous: `append` stamps
  `seq: record.frames.length + 1` (`runtime/packages/daemon/src/turn-registry.ts:333-334`);
  `Subscription.next` reads `frames[cursor]` and advances `cursor = frame.seq`
  (`:124-130`), so `subscribe(afterSeq)` (`:200-209`) replays exactly the
  frames with `seq > after` and then waits for live frames.
- `state()` reports `active`, `turnId`, `lastSeq = frames.length`,
  `startedAt`/`endedAt`, and treats a turn still in `starting` as active with
  `lastSeq 0` (`:212-224`), which is what the renderer uses to decide between
  reconnect and settle.
- Retention: a finished record stays for `DEFAULT_TURN_RETENTION_MS` (10 min,
  `:18`, `:152`) via an unref'd timer set in `finish` (`:338-346`); a
  subscriber that arrives after release gets 404 `TURN_NOT_ACTIVE` (`:206`).
- Daemon routes: `GET .../turn/state` (`runtime/packages/daemon/src/runtime-daemon.ts:679`),
  `GET .../turn/stream?after=` (`:685-692`, validated by `afterSequence`
  `:815`), `POST .../turn` starts through `turns.start` and subscribes from 0
  (`:753-757`). A client close only runs `onDisconnect: () => subscription.close()`
  (`:691`, `:757`, `:925`); the `interrupt` hook on those streams is invoked
  only by daemon stop (`:690`, `:756`, `:1028-1037`).
- SSE framing carries `id: <seq>` and a `: keepalive` comment every
  `sseKeepaliveMs` (15 s default, `:169-170`, `:196`, `:945-948`). The Next
  hop re-emits `id:` (`frontend/src/lib/harness/http.ts:45-49`, `:83`) with
  its own keepalive (`:74-76`) and its `cancel` only unsubscribes (`:101-105`);
  the browser parser skips comment lines and reads `id:` into `seq`
  (`frontend/src/lib/harness/client.ts:125`, `:132-134`, `:147`).
- Chat panel: `observeTurn` tracks `lastSeq` (`frontend/src/components/shell/chat-panel.tsx:891`),
  deduplicates harness events by `eventId` (`:896-898`), renders
  `turn.interrupted` on arrival (`:906-911`), and on a closed stream without a
  terminal asks `turn/state` before deciding (`:1001-1009`); a still-active
  turn reconnects on the backoff ladder `RECONNECT_DELAYS_MS` (`:116`,
  `:1010-1020`) with `attachHarnessTurn(after = lastSeq)`; a 404
  `TURN_NOT_ACTIVE` settles from the persisted log (`:988-992`,
  `:1023-1046`). Opening a chat with an active turn runs `recoverActiveTurn`
  (`:711`, `:1058-1114`): replay hydrates events, then attach from seq 0 with
  the hydrated ids pre-seeded, so streamed text is rebuilt from the retained
  `chat:delta` frames and no event is appended twice. The unmount hook aborts
  the observation only (`:463`), never the turn.

No duplicate execution path was found: the only way a turn starts is
`POST .../turn`, which the panel issues once per submit (`:1226-1244`); every
reconnect goes through `turn/stream`. No lost-frame path was found: the
buffer is retained across disconnects and released only by the retention
timer or `close()`.

## Q2: Interruption versus retirement; shutdown order; regression tests

Answer: Stop is `turn/interrupt` and never retirement; the PR #767 confusion
is gone; the shutdown order matches the design; the budgets nest (Finding 1).

- `CodexSupervisor.interrupt` sends `turn/interrupt` and awaits the turn's
  own terminal, never `retire` (`runtime/packages/daemon/src/codex-supervisor.ts:190-197`).
  `retire` is memoized per exact generation, settles an unsettled entry as
  failed, and rejects stale generations (`:200-217`).
- `DelegatedRuntime.executeInterrupt` refuses a second interrupt (`FORBIDDEN`,
  `runtime/packages/core/src/delegated-runtime.ts:214-226`) and takes the
  supervisor's native `interrupt` when present; the retire branch is only for
  supervisors without one (`:222-224`). The turn's own path calls `retire()`
  after the terminal (`:365`), and `interrupted` is derived from the supervisor
  result (`exitCode === null && signal === "SIGTERM"`, `:366`).
- `TurnCoordinator.interrupt` aborts its controller and awaits
  `engine.interrupt(sessionId)` (`runtime/packages/core/src/turn-coordinator.ts:490-496`).
  The abort signal is not passed into the engine input (`:164-213` builds the
  input without `signal`; the adapter forwards `input.signal`, which is
  undefined, `runtime/packages/core/src/delegated-engine-adapter.ts:232`), so
  the delegated `cancel` listener (`delegated-runtime.ts:340-347`) never
  fires from the coordinator and the interrupt reaches `executeInterrupt`
  exactly once. The adapter's `interrupt(sessionId)` maps to
  `delegated.interruptTurn` (`delegated-engine-adapter.ts:325-328`).
- `TurnRegistry.interrupt` joins concurrent Stop calls on one in-flight
  promise (`turn-registry.ts:228-241`); the daemon's interrupt route is the
  only renderer path (`runtime-daemon.ts:762`; `chat-panel.tsx:1116-1129`,
  `:1660-1669`).
- Shutdown order in the service: `turnRegistry.close({reason:"service-shutdown"})`
  then `delegated.close()`, `daemon.stop()`, `hostedBootstrap.close()`,
  `login.close()`, `supervisor.close()`, `host.close()` (`runtime/packages/daemon/src/app-owned-composition.ts:223-231`).
  `TurnRegistry.close` interrupts every active turn, waits up to 5 s for
  terminals, and records `turn.interrupted` through `markInterruptedOnShutdown`
  for any turn that did not settle (`turn-registry.ts:261-280`;
  `runtime/packages/core/src/session-store.ts:153-159`). The standalone binary
  routes SIGTERM/SIGINT to `job.close()` once and exits 0
  (`runtime/packages/daemon/src/standalone-bin.ts:14-22`, `:36`). The
  app-server host terminates its child with SIGTERM then SIGKILL after 5 s
  (`runtime/packages/daemon/src/codex-app-server-client.ts:78-82`).
  The daemon's stop closes admission, interrupts registry turns once, and
  removes the socket (`runtime-daemon.ts:1028-1060`; the composition test
  asserts `ENOENT` on the socket, `runtime/tests/app-owned-composition.test.ts:135`).
- Electron: `stop()` sends SIGTERM and SIGKILL after `killGraceMs` 5 s
  (`frontend/electron/runtime-service-host.ts:212`, `:349-367`, `:529-538`);
  `teardown` closes the renderer server first, then the service host
  (`frontend/electron/main.ts:875-916`), and `before-quit` funnels every quit
  into that path (`:953-963`).
- Deterministic regressions: `runtime/tests/delegated-runtime.test.ts:150`,
  `:172`, `:191-230` (section 8 order A and order B, cleanup settles once),
  `runtime/tests/codex-supervisor.test.ts:166` (interrupt without retire,
  memoized retire, stale generation rejected),
  `runtime/tests/app-owned-composition.test.ts:111`, `:125` (interrupt through
  the route; shutdown with a live turn records `turn.interrupted`, terminates
  the app-server, removes the socket, second close is a no-op),
  `runtime/tests/daemon.test.ts:410`, `:464` (turn survives disconnect;
  interrupt only through the route),
  `frontend/src/__tests__/electron/runtime-service-host.test.ts:175`, `:202`
  (SIGTERM on teardown; SIGKILL escalation),
  `frontend/src/__tests__/components/chat-panel-turn-attach.test.tsx:178`
  (Stop calls the interrupt route without closing the stream). All run
  against fakes with no timers left to real time except the daemon's
  production grace tests.

See Finding 1 (budget nesting) and Findings 2 and 3 (two narrow interrupt
edge cases) below.

## Q3: Protocol completeness

Answer: every server request is answered, notifications are not filtered,
and no configuration is overridden except the per-turn policy and the
credential store selector.

- Argv is exactly `-c cli_auth_credentials_store="file" app-server`
  (`codex-app-server-client.ts:39`), spawned with `CODEX_HOME` set to the
  effective home and the parent environment otherwise untouched (`:47-53`).
  No other `-c`, no config file rewrite, no model or provider override.
- Server requests: the client's default handler answers `-32601` for anything
  the supervisor does not claim (`:94`, `:107`, `:237`). The supervisor
  handles approvals (`APPROVAL_REQUEST_METHODS`, `codex-supervisor.ts:31`),
  `item/tool/requestUserInput` (`:32`) and `mcpServer/elicitation/request`
  (`:33`) as pending requests answered through the request routes;
  `dynamicToolCall` is refused immediately; unknown methods get a
  `request-resolved` frame with outcome `unsupported` plus a warning, then
  `-32601` (`:376-396`). Pending requests are cancelled on turn end, on the
  supplier resolving them itself, and on child exit (`:338`, `:347`,
  `:360-372`). Tests: `codex-supervisor.test.ts:110`, `:148`;
  `codex-app-server-client.test.ts:8`.
- Notifications: every notification of a known thread is pushed as a
  `notification` progress event before any specialised handling
  (`:299-309`), and the adapter turns each into a `codex.notification`
  harness event (`delegated-engine-adapter.ts:250`, `:278`) alongside
  `codex.request`/`codex.request.resolved`/`tool.permission` (`:287-299`).
  The composition test asserts `serverRequest/resolved`, `item/started` and
  `item/completed` pass through (`app-owned-composition.test.ts:89`).
- Policy is per turn: `approvalPolicy`/`sandbox` are sent on
  `thread/start`/`thread/resume` and again on `turn/start` only when they
  changed (`codex-supervisor.ts:126`, `:146-147`, `:167-169`). Model and
  reasoning effort are per turn (`:167-168`;
  `turn-coordinator.ts:118-121`).
- `initialize` declares `clientInfo` and `experimentalApi: true`
  (`codex-app-server-client.ts:266`); a refused initialize closes the child
  without scheduling a restart (`:268`; test `codex-app-server-client.test.ts:94`).

Informational: `thread/settings/update` is sent only when the collaboration
mode changes and carries `developer_instructions: null`
(`codex-supervisor.ts:142-145`). Whether the stock server reads `null` as
"leave the thread's developer instructions alone" or as "clear them" cannot
be established from source in this checkout (the bundled package is a binary
plus README). See Test gaps.

## Q4: Authentication separation

Answer: authentication is confined to the effective home; sign-out cannot
reach `~/.codex/auth.json`; project tokens cannot perform account actions;
tokens and socket are private; no credential or e-mail is logged.

- Effective home: `isExcludedCodexHomeEntry` excludes `auth.json`,
  `models_cache.json`, any `auth*` and any `*.lock`
  (`runtime/packages/daemon/src/codex-effective-home.ts:33-34`); excluded
  names are never linked (`:63`) and an existing overlay link with an excluded
  name is removed (`:82`); the overlay refuses a symlinked directory (`:47`)
  and never creates, copies or writes anything inside the user's home
  (`:1-12`, only `symlink`/`unlink` on overlay paths, `:76`, `:82`, `:86`).
  Tests: `runtime/tests/codex-effective-home.test.ts:34`, `:51`, `:74`, `:87`.
- Only `CODEX_HOME=<effectiveHome>` is exported to the child
  (`codex-app-server-client.ts:48`; wired at `app-owned-composition.ts:152`,
  `:157`). Electron resolves the user home from `CODEX_HOME` or the default
  (`frontend/electron/main.ts:440-444`) and the effective home under
  `userData/runtime` (`:699`).
- Sign-out is `account/logout` issued to the app-server running under the
  effective home (`runtime/packages/daemon/src/codex-login.ts:76`); the
  service has no code path that opens `auth.json` anywhere.
- Scopes: `account/logout`, `login/start` and `login/cancel` require
  `credentials:write` (`runtime-daemon.ts:433`, `:441-443`). Project tokens
  are issued with `runtime:read`, `sessions:read`, `sessions:write`,
  `models:read` only (`:834-839`; `runtime/packages/core/src/runtime-service.ts:151-157`).
  The App-host token carries `credentials:*` and is re-issued per launch,
  revoking every earlier `app-host` record (`app-owned-composition.ts:234`;
  `runtime/packages/core/src/auth-registry.ts:66-80`). The renderer's hosted
  port routes sign-in/out through the app-host client and everything else
  through the project client
  (`frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:763-803`,
  `:913-923`).
- File modes: runtime directory `0700` (`app-owned-composition.ts:178`),
  token file `0600` with an explicit `chmod` (`:235-237`; test
  `app-owned-composition.test.ts:56`); Electron writes the config `0600`
  atomically under a `0700` directory (`runtime-service-host.ts:123-129`);
  `RuntimeClient` re-reads the token file per request and checks it with
  `lstat` (`runtime/packages/client/src/client.ts:94-105`, `:152`, `:175`).
  The socket path is bounded to 103 bytes on both sides
  (`app-owned-composition.ts:99`; `runtime-service-host.ts:21`).
- Logging: the login relay logs event names only (`codex-login.ts:41-42`,
  `:63`, `:78`); app-server diagnostics pass through `redactAccountText`
  (`codex-app-server-client.ts:41-43`); the desktop log redacts e-mails at
  the writer (`frontend/electron/desktop-log.ts:60-63`, `:103`). Tests assert
  no `@` in status, logs or the desktop log
  (`app-owned-composition.test.ts:65`, `:108`;
  `runtime-service-host.test.ts:307-322`).

## Q5: Additive transitions and bootless boot

Answer: additive engines skip the instruction-policy drift refusal; the
context update is sent with the accepting turn; the basis bytes are frozen
with that turn; boot records readiness without a Codex turn.

- `RuntimeMethodService` treats an engine without `prepareContextSuccessor`
  as additive: `resolveForTurn` skips the drift refusal (`runtime/packages/core/src/runtime-method-service.ts:161-177`),
  and `replaceSelectedMethods` reports `{ status: "additive", successorAvailable: false }`
  instead of demanding a successor (`:204`, `:235-238`, `:270`).
- The adapter renders developer instructions from the resolved context,
  digests them, and adds `Chirality context update:\n<instructions>` to the
  turn input only when a previous turn exists and the digest changed
  (`delegated-engine-adapter.ts:35`, `:204-207`, `:230-231`); the digest is
  recorded when the turn is `started` (`:242`). The supervisor places the
  update before the prompt in `turn/start` input (`codex-supervisor.ts:150-151`).
- The basis is frozen with the accepting turn regardless of engine:
  `commitWithAcceptedTurn` writes the accepted-turn transaction with the
  snapshot (`turn-coordinator.ts:227`; `session-store.ts:624-664`), and the
  recovery marker is replayed on next read (`:127`, `:708-750`).
- After a service restart the adapter's digest map is empty, so no context
  update is produced for the first turn; instead the supervisor finds no
  thread state and issues `thread/resume` with the full current
  `developerInstructions` (`codex-supervisor.ts:104`, `:126`), so the current
  role/workflow/project instructions are re-supplied rather than dropped.
  The same holds after an app-server restart (`codex-supervisor.test.ts:93`).
- Bootless boot: `descriptor.boot === "none"` records readiness without a
  turn (`runtime-service.ts:325`); the Codex adapter is never gated by
  `enabledAdapterIds` (`:231`). Tests: `app-owned-composition.test.ts:186`
  (no `thread/start`/`turn/start` during boot; first message starts the
  thread), `:200` (additive change keeps one thread and carries the update),
  `:218` (legacy manifest without the Codex adapter still creates sessions).

## Q6: Service lifecycle and failure handling

- Ready line: exactly one JSON line is printed after the daemon is up
  (`standalone-bin.ts:29`); Electron parses only that shape and treats a
  missing line within 30 s as a failure that kills the child and schedules a
  restart (`runtime-service-host.ts:208`, `:460-464`; tests `:163`, `:252`).
- Restart ladder 1, 2, 4, 8, 16, 30 s; give up after 5 failures in 180 s with
  a `stopped` snapshot carrying the reason (`:209-211`, `:304-330`,
  `:476-477`; tests `:214`, `:226`, `:281`). The renderer shows the state and
  offers a manual restart only once stopped
  (`frontend/src/components/settings/runtime-status.tsx:67-97`;
  `runtime-control-ipc-contract.ts`). Operator restart replaces the live
  child and keeps one owner (`runtime-service-host.ts:521`; test `:262`).
- Crash of the app-server inside the service: the host restarts it with
  backoff and fails live turns (`codex-app-server-client.ts:293-300`;
  `codex-supervisor.ts:367-372`; tests `codex-app-server-client.test.ts:59`,
  `:84`; `app-owned-composition.test.ts:139`). Threads are resumed on the next
  turn (`codex-supervisor.ts:104`, `:126`).
- Stale socket: recovery requires an authenticated owner record
  (`runtime-daemon.ts:1319`; `daemon.test.ts:586`, `:1096`).
- Version pin: the service refuses a Codex whose `--version` differs from
  `expectedVersion` before spawning the app-server
  (`app-owned-composition.ts:112`, `:153`; `standalone.test.ts:43`).
- Token permissions and socket length: see Q4.

See Finding 1 for the one lifecycle gap.

## Q7: Packaging scripts

- `pack-electron.mjs` requires the built service, CLI and instruction bundle
  (`frontend/scripts/pack-electron.mjs:30-32`), requires every
  `extraResources.from` to exist, requires the `codex` resource with both
  executables, and requires an exact `@openai/codex` pin (`:115-145`).
- `verify-codex-pin.mjs` compares the `package.json` pin with the lockfile,
  the packaged `codex --version` with the lockfile, the staged
  `codex-package.json` with the lockfile, and (before signing) the sha256 of
  the packaged binaries with the installed platform package
  (`frontend/scripts/verify-codex-pin.mjs:58-67`, `:110-161`); tests
  `frontend/src/__tests__/scripts/verify-codex-pin.test.ts:55-110`.
- `sign-electron-runtime-v2.mjs` signs once through `@electron/osx-sign`
  with the hardened runtime everywhere, JIT entitlements only for
  `codex-code-mode-host`, and verifies both Codex binaries afterwards
  (`frontend/scripts/sign-electron-runtime-v2.mjs:26-35`, `:44-62`; tests
  `sign-electron-runtime-v2.test.ts:22-64`).
- `finalize-electron-resources.mjs` requires `codex/bin/codex`,
  `codex/bin/codex-code-mode-host`, `codex/codex-package.json`,
  `runtime-service/standalone-bin.mjs` and forbids the retired inventories
  (`frontend/scripts/finalize-electron-resources.mjs:20-44`, `:100-113`).
- `verify-packaged-dependency-boundary.mjs` forbids the legacy runtime
  packages, checks the Codex tree is regular, executable and path-exact, and
  checks the manifest entrypoint (`frontend/scripts/verify-packaged-dependency-boundary.mjs:51-61`,
  `:100-116`, `:133-137`).
- Same composition as the source run: the packaged App spawns
  `runtime-service/standalone-bin.mjs daemon --config` with the packaged
  `codex/bin/codex` (`frontend/electron/codex-executable.ts:15`, `:66-71`,
  `:90`; `main.ts:423`, `:699-700`, `:756`) through the same
  `chirality-app-owned/v1` config the tests exercise
  (`runtime-service-host.test.ts:131`).

## Q8: Removed code

- No live reference to the retired supply-model modules remains in
  `runtime/packages/daemon/src` (the directory holds only the fourteen
  App-owned modules) or in `runtime/packages/core/src`.
- In the frontend, `LaunchAgent`, `native-admission` and
  `CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE` survive only as comments, as the
  explicit `delete` at `frontend/electron/main.ts:672`, and inside forbidden
  lists (`verify-packaged-dependency-boundary.mjs:137`,
  `build-controlled-ci-runtime.mjs:57`). The settings UI no longer offers
  install/start/stop/uninstall (`runtime-settings.tsx`,
  `runtime-settings-controller.tsx`); `shell-frame.tsx:497-507` reads the
  connectivity bridge, not the retired `runtime.daemon` IPC.
- `frontend/docs/harness/README.md:3-10` and
  `runtime_engine_contract.md:8-11`, `:37-51` carry the D-GOV-43 note and
  state that a closed stream never interrupts; no doc contradicts the code.
- Stale comment: `frontend/electron/api-key-ipc.ts:131` still explains a
  behaviour in terms of a LaunchAgent that no longer exists (Informational).

## Q9: Test adequacy

The new suites are real: they drive the production composition over a Unix
socket with a scripted fake app-server (`runtime/tests/fake-codex-transport.ts`,
`tests/fixtures/fake-codex-app-server.mjs`), the production Electron host
with a fake service binary
(`frontend/src/__tests__/electron/fixtures/fake-runtime-service.mjs`), and
the production chat panel with a mocked harness client. They cover the
brief's named scenarios: disconnect and replay, interrupt only through the
route, keepalive, request listing and answers, shutdown with a live turn,
app-server death, sign-in relay, effective home exclusions, ready-line
timeout, SIGKILL escalation, backoff and give-up, pin verification and
signing policy. Gaps are listed at the end; none is blocking.

## Findings

No blocking finding.

### Finding 1: Medium (non-blocking): shutdown budgets nest and a hard-killed service leaves a session permanently `running`

Evidence. `TurnRegistry.close` awaits the interrupt fan-out with no bound
before it starts the 5 s grace (`runtime/packages/daemon/src/turn-registry.ts:264-266`).
That await runs `service.interruptSession` to `CodexSupervisor.interrupt`,
which awaits the `turn/interrupt` request (60 s default timeout,
`codex-app-server-client.ts:131`) and then the turn's own terminal
(`codex-supervisor.ts:194-196`). After the registry closes, `daemon.stop()`
has a 2 s grace (`runtime-daemon.ts:52`) and `host.close()` a 5 s SIGKILL
grace (`codex-app-server-client.ts:80`). Electron SIGKILLs the whole service
5 s after SIGTERM (`frontend/electron/runtime-service-host.ts:212`,
`:359-363`), and the design itself specifies both 5 s figures
(SPIKE_DESIGN.md:94-96, :409).

Failure scenario. The operator quits while a Codex turn is mid tool call and
the supplier takes more than about four seconds to deliver the interrupted
terminal (or the app-server is wedged). Electron kills the service before
`markInterruptedOnShutdown` runs. The session record was set to `running` at
turn start (`turn-coordinator.ts:231`) and nothing on the next service start
repairs it: `reconcileAcceptedTurn` only replays the accepted-turn marker and
rewrites `status: "running"` (`session-store.ts:708-750`). Every later turn
or method change on that session is refused with 409
`SESSION_TURN_IN_PROGRESS` (`session-store.ts:194`, `:233`, `:644`; the
coordinator's own guard at `turn-coordinator.ts:113` is in-memory only), and
the renderer tells the operator to wait for or interrupt a turn that does
not exist (`frontend/src/lib/harness/error-display.ts:47-51`). The chat
panel's recovery sees `active: false` and does nothing (`chat-panel.tsx:1061`).
The Codex child is also left without a killer: it is spawned `detached: false`
with no parent-death signal (`codex-app-server-client.ts:47-53`), so after a
SIGKILL of the service its exit depends on how the stock binary treats stdin
EOF, which this review could not verify. The same stuck state follows any
service crash mid-turn; that part is pre-existing, but the App-driven
SIGKILL on quit is new with this topology.

Smallest repair. (a) In `TurnRegistry.close`, race the interrupt fan-out
against the grace deadline instead of awaiting it unbounded, so the
`markInterruptedOnShutdown` loop always runs inside the grace; (b) on
service start, move any session whose record says `running` to
`interrupted` with reason `service-restart` (a fresh service owns no turns,
so the state is unambiguous); (c) make the Electron kill grace exceed the
service's worst-case close (grace plus daemon stop plus app-server kill
grace), or shorten the inner budgets so their sum stays under 5 s.

### Finding 2: Low: Stop during the `turn/start` round trip sends `turnId: ""` and can latch the turn as no longer interruptible

Evidence. The supervisor registers the entry before `turn/start` goes out
(`codex-supervisor.ts:156-165`), and `interrupt` sends
`turnId: entry.turnId ?? ""` when the response has not arrived
(`:194`). `executeInterrupt` adds the key to `interruptedTurns` before
awaiting the supervisor and never removes it on rejection
(`delegated-runtime.ts:220-223`).

Failure scenario. Stop is pressed in the window between entry registration
and the `turn/start` response (longer when `thread/resume` precedes it). If
the stock server rejects an empty turn id, the interrupt route fails, the
turn continues, and a second Stop is refused with 403 "Turn is no longer
interruptible" for the rest of that turn.

Smallest repair. Have `interrupt` await the turn id (the `turn/start`
response or the `turn/started` adoption) before sending `turn/interrupt`, and
remove the key from `interruptedTurns` when the supervisor interrupt rejects.

### Finding 3: Low: a polling failure retires a live worker without interrupting the Codex turn

Evidence. `void polling.catch(() => { void retire().catch(() => {}); })`
(`delegated-runtime.ts:359`). `retire` settles the entry as failed and drops
its bookkeeping without sending `turn/interrupt` (`codex-supervisor.ts:200-213`).

Failure scenario. A throw inside `drainTurnProgress`, the native-plan sink or
the observer's `onProgress` retires the worker; the Chirality turn ends
`failed`, while the Codex turn keeps running in the app-server with its
notifications dropped (no entry) and its pending requests cancelled. The
thread then refuses the next turn with "Codex thread already has a live
turn" (`:140`) until the supplier finishes on its own.

Smallest repair. On polling failure, call the supervisor's `interrupt` first
(joining the turn's own terminal) and only then `retire`; or record the
polling error and let the normal terminal path handle retirement.

### Finding 4: Low: `admission: "establishing"` is still produced, contrary to the design

Evidence. `hosted-bootstrap.ts:47` yields `establishing` when the account is
signed in but `model/list` failed; SPIKE_DESIGN.md:458 states `establishing`
is never produced. The catalog failure is logged (`:44`) and the cache
cleared, so the next status read retries. Consequence: the renderer shows a
pending account state after a transient `model/list` failure instead of a
ready state with an explicit catalog error. Repair: either report `ready`
with a `models` omission and a reason, or update the design text to name
this state.

### Informational

- I1. `runtime-service-launcher.ts` uses `utilityProcess.fork` rather than
  the design's `ELECTRON_RUN_AS_NODE` spawn, justified in its header comment
  by the `runAsNode` fuse being off (`frontend/electron/runtime-service-launcher.ts:5-15`,
  `:28-31`). Exit records always carry `signal: null` (`:39`), so a
  signal-killed service is indistinguishable from a coded exit in the desktop
  log and the connectivity snapshot.
- I2. `verify-codex-pin.mjs --after-signing` skips the digest comparison
  (`verify-codex-pin.mjs:17-19`), so post-signing binding is version plus
  staged manifest plus `codesign --verify` of both binaries
  (`sign-electron-runtime-v2.mjs:62`). Adequate, but the digest of the signed
  binary is not recorded anywhere for later comparison.
- I3. `thread/settings/update` sends `developer_instructions: null` on every
  collaboration-mode change (`codex-supervisor.ts:143`). If the stock server
  reads `null` as "clear", switching to Plan Mode and back would drop the
  role/workflow/project instructions for the rest of the thread until the
  next context update. Unverifiable from source here; see Test gaps.
- I4. The `operator` client is still ensured with `credentials:write`
  (`runtime-daemon.ts:223-232`). Pre-existing and unreachable from the App
  (no operator token file is handed out), but it is a second principal that
  can sign out.
- I5. Stale comment at `frontend/electron/api-key-ipc.ts:131` mentions a
  LaunchAgent.

## Scope statement

Reviewed: the complete diff `e83cb1f47..886eb2707` restricted to
`projects/chirality-runtime/packages` and
`projects/chirality-app-dev/frontend/{electron,scripts,src,package.json}`,
and the complete final files of `runtime/packages/daemon/src/*` (all
fourteen), `runtime/packages/core/src/{delegated-runtime,delegated-engine-adapter,runtime-method-service,turn-coordinator,runtime-service,session-store,auth-registry,process-supervisor,fs}.ts`,
the contracts and client changes, `frontend/electron/{main,runtime-service-host,runtime-service-launcher,codex-executable,desktop-log,desktop-process-policy,runtime-control-ipc,runtime-control-ipc-contract,preload}.ts`,
the five packaging scripts plus `build-electron.mjs` and `package.json`,
the harness routes, `frontend/src/lib/harness/{client,http,server-request-answer}.ts`,
`frontend/src/lib/runtime-client/{daemon-harness-port,runtime-daemon-harness-port}.ts`,
`frontend/src/lib/shell/harness-event-views.ts`,
`frontend/src/components/shell/{chat-panel,request-card,permission-requests}.tsx`,
the settings and activity components, `frontend/docs/harness/*`, and the
test files named in the commands table. Not reviewed: the stock
`@openai/codex` binary's behaviour (only its argv, environment and protocol
use as coded here), CSS, and files outside the two workspace roots.

## Test gaps (non-blocking)

1. No test hard-kills the service mid-turn (SIGKILL or crash) and then
   starts a new service and a new turn on the same session; that is the path
   of Finding 1.
2. `runtime-service-host.test.ts:202` covers SIGKILL escalation with a
   service that ignores SIGTERM, but no test combines a live Codex turn that
   outlasts the grace with the service's own `markInterruptedOnShutdown`.
3. No test presses Stop between entry registration and the `turn/start`
   response, or asserts recovery after a rejected `turn/interrupt`
   (Finding 2).
4. No test drives a `drainTurnProgress` or native-plan sink failure to show
   what happens to the Codex turn (Finding 3).
5. The fake app-server accepts any `thread/settings/update`; no fixture or
   acceptance note records how the stock 0.154.0 server treats
   `developer_instructions: null` (I3), nor that `thread/resume` with
   `developerInstructions` re-applies them after a service restart (the
   supervisor test covers app-server restart only).
6. `verify-codex-pin.test.ts` has no `--after-signing` case.
7. `hosted-bootstrap` status with a signed-in account and a failing
   `model/list` (the `establishing` branch, Finding 4) is untested.
8. The effective-home tests prove exclusion of the names; no test spawns a
   process under `CODEX_HOME=<overlay>` and shows a write to `auth.json`
   lands in the overlay, which is the property the design relies on.

## Re-check 2026-09-12: repair commit `26fffb89a` (delta only)

Reviewer: Claude Fable 5.1, medium reasoning, no delegation. Read-only review
of `git diff 886eb2707..26fffb89a` (HEAD now `26fffb89a`, one commit) in the
same worktree, restricted to the product and test files the coordinator
named, together with the complete final `turn-registry.ts`,
`codex-supervisor.ts`, `delegated-runtime.ts`, `app-owned-composition.ts`,
`session-store.ts` (`settleRunningOnStart` and its callers) and
`runtime-service-host.ts` constants. Same constraints as the main review;
only this file was edited.

### Verdict for the delta: PASS

Findings 1 to 4 are closed. No regression in the interrupt-versus-retirement
rule. Two Informational residuals and two test gaps are recorded; none is
blocking.

### Finding 1 (shutdown budgets; stuck `running` session): closed

- The interrupt fan-out is now raced against the grace
  (`runtime/packages/daemon/src/turn-registry.ts:264-274`), so the
  `waitForTerminal` loop and `markInterruptedOnShutdown` always run inside
  the grace; the default grace is 3 s (`:20`). The app-server kill grace is
  2 s (`codex-app-server-client.ts:47`, `:83`); the App host's SIGKILL grace
  is 10 s (`frontend/electron/runtime-service-host.ts:217`). Worst-case
  service close is registry 3 s, then `delegated.close()` (immediate, see
  below), daemon stop 2 s plus the 0.5 s force-settle cap
  (`runtime-daemon.ts:52-53`), then app-server kill 2 s: about 7.5 s plus
  overhead, inside the 10 s window. SPIKE_DESIGN.md:94-96 and :409-411 now
  state the same figures.
- On start, `settleRunningOnStart` moves every `running` session of every
  registered project to `interrupted` with a `turn.interrupted` event
  (reason `service-restart`) against the last accepted or started turn
  (`runtime/packages/core/src/session-store.ts:168-180`;
  `app-owned-composition.ts:166-171`). It runs before the engine registry,
  the delegated runtime and the daemon exist, so within the new process no
  turn can own a session at that moment.
- Abandoned interrupt question. When the race times out, the fan-out
  promise keeps running with `CodexSupervisor.interrupt` awaiting
  `entry.result`. The next close step, `delegated.close()`
  (`delegated-runtime.ts:249-262`), skips turns already latched in
  `interruptedTurns` (every fan-out reached `executeInterrupt` within the
  grace unless `binding()` itself stalled) and retires every worker in the
  supervisor inventory; `retire` settles an unsettled entry
  (`codex-supervisor.ts:210`), which resolves the abandoned await and the
  turn's own `wait`. `host.close()` then SIGTERMs and SIGKILLs the app-server
  within 2 s, so no live Codex turn outlives the service. The next service
  resumes the durable thread through `thread/resume` on the first turn
  (`codex-supervisor.ts:104`, `:126`); the composition test at
  `runtime/tests/app-owned-composition.test.ts:142-167` runs a new turn on
  the settled session after a relaunch. The only path that still leaves a
  live child is a SIGKILL from Electron before `host.close()`, which the
  10 s window is sized to prevent.
- Sweep-versus-live-turn question. The sweep cannot settle a session owned
  by the new process. It could touch a session owned by a predecessor only
  if two services share the runtime directory at once; Electron's
  `restart()` awaits the previous child's termination (`runtime-service-host.ts:521`),
  and a crashed child is dead. The ready-timeout path does not await
  `terminateChild` (`:463`) before the restart ladder, so a predecessor that
  received SIGTERM at 30 s could still be closing when the successor starts
  1 s later; but such a predecessor is already settling its own turns with
  `markInterruptedOnShutdown`, which returns false once the record is no
  longer `running` (`session-store.ts:155`), and the successor's daemon then
  fails closed on the live owner record (`runtime-daemon.ts:1319`). No
  double settlement and no misreported live turn; see residual R1.

### Finding 2 (Stop during the `turn/start` round trip): closed

`interrupt` now awaits the turn identity (`entry.turnId ?? await
entry.turnIdReady`, `codex-supervisor.ts:202-204`), which is resolved on the
`turn/start` response through `adoptTurn` (`:239`), on `turn/start` failure
(`:176`) and on settlement (`:167`), so it can never wait past the turn's
own end and never sends an empty id. A rejected supervisor interrupt now
unlatches `interruptedTurns` before rethrowing
(`delegated-runtime.ts:224-227`), so a later Stop is accepted. Test
`runtime/tests/codex-supervisor.test.ts:192-213` holds the `turn/start`
response, calls `interrupt`, asserts no `turn/interrupt` was sent, releases
the response, and asserts the exact `turn/interrupt` with the adopted id
followed by the `SIGTERM` result.

### Finding 3 (polling failure retired a live worker): closed

A polling failure now sends the supervisor's `interrupt` (which joins the
turn's own terminal) before `retire`, and the polling error is thrown after
the terminal arrives (`delegated-runtime.ts:363-376`); the catch path joins
the same memoized retirement (`:397`). The interrupt-versus-retirement rule
is intact: apart from service shutdown (`delegated.close()` inventory
retirement after the interrupts, and `supervisor.close()`), no path retires
a live worker without an interrupt first. Trade-off accepted: a supplier
that never honours the interrupt now keeps the failed turn open until Stop
or shutdown instead of orphaning it upstream.

### Finding 4 (`establishing`): closed by design text

SPIKE_DESIGN.md:460-461 now names the state (signed in, catalog read failed,
next status read retries); the code is unchanged. The related
`resolveProject` change (`app-owned-composition.ts:202`) reads the catalog
on demand when nothing is cached so a first turn after relaunch validates
its model and effort; a failed read falls back to the pre-delta
catalog-less binding.

### Regression check: interrupt versus retirement

No regression. `interrupt` still never retires (`codex-supervisor.ts:196-206`);
`retire` is still memoized per generation (`:212-227`); `executeInterrupt`
still takes the retire branch only for supervisors without a native
interrupt (`delegated-runtime.ts:228`); the section 8 order A/B tests and
`codex-supervisor.test.ts:166` pass unchanged.

### Test coverage and determinism

- `runtime/tests/turn-registry.test.ts:73-89`: holds the service interrupt
  forever, closes with a 100 ms grace, asserts the close returned in under
  2 s with the turn reported unsettled, the session marked interrupted with
  reason `service-shutdown`, and the registry state inactive. Real timers
  against an in-process stub; deterministic.
- `runtime/tests/session-and-residency.test.ts:132-148`: store-level sweep
  with one running and one idle session; asserts the event, the turn id, the
  idempotent second sweep. Deterministic.
- `runtime/tests/app-owned-composition.test.ts:142-167`: emulates a hard kill
  by stopping the daemon and the app-server, then rewrites the record to
  `running`, restarts a second service over the same directory, and asserts
  the settlement log line, the `interrupted` status, the `service-restart`
  terminal and a successful new turn on the same session. Deterministic
  (2.5 s, the daemon's production stop grace). Fidelity note: because the
  emulated stop already appended a terminal, the log ends with two
  terminals; a real SIGKILL leaves none. The sweep does not read the log's
  terminal state, so the assertion still proves the repair.
- `runtime/tests/codex-supervisor.test.ts:192-213`: ordering relies on 1 ms
  sleeps against a synchronous in-process fake host; deterministic in
  practice.
- Frontend: `DEFAULT_KILL_GRACE_MS` has no direct test (the host tests pass
  `killGraceMs: 300`); the relation "App kill grace exceeds the service close
  budget" is asserted nowhere (gap G2).

### Residuals (non-blocking)

- R1 (Informational): the start sweep runs before the daemon acquires the
  socket owner record (`app-owned-composition.ts:166` precedes
  `daemon.start`). Moving it after the owner record is held would make "a
  fresh service owns no turns" hold by construction rather than by the
  Electron launcher's single-owner discipline.
- R2 (Informational): `daemon.stop()` calls `delegated.close()` a second time
  (`runtime-daemon.ts:366`); it is idempotent in effect but not memoized.
- R3 (Informational, unchanged from the main review): when
  `engine.interrupt` rejects, `TurnCoordinator.interrupt` has already aborted
  its controller (`turn-coordinator.ts:494-495`), so the eventual terminal of
  a turn that was never interrupted is reported with `interrupted: true`.
  Far less reachable now that Finding 2 is closed.

### Test gaps after the delta

- G1: no composition-level test drives a fake app-server that ignores
  `turn/interrupt` through `runtime.close()` end to end and asserts the total
  close time and that the app-server was terminated (the registry-level
  test covers the bound; the budget composition is argued, not measured).
- G2: no test or static assertion ties `DEFAULT_KILL_GRACE_MS` (10 s) to the
  service's close budget.
- G3 (carried): the polling-failure path (Finding 3) has no test.

### Re-check commands

| Command (cwd) | Result |
|---|---|
| `npx tsc -b --pretty false` (`runtime/`) | exit 0, no diagnostics |
| `npx vitest run tests/turn-registry.test.ts tests/session-and-residency.test.ts tests/app-owned-composition.test.ts tests/codex-supervisor.test.ts tests/delegated-runtime.test.ts tests/codex-app-server-client.test.ts tests/standalone.test.ts tests/daemon.test.ts tests/runtime-daemon-signal.test.ts` (`runtime/`) | 9 files passed, 76 tests passed, 0 failed, 14.97 s (turn-registry 8, session-and-residency 8, codex-supervisor 7, app-owned-composition 10, delegated-runtime 9, codex-app-server-client 7, standalone 5, daemon 20, runtime-daemon-signal 2) |
| `npx vitest run tests/turn-registry.test.ts tests/session-and-residency.test.ts tests/codex-supervisor.test.ts` (`runtime/`) | 3 files passed, 23 tests passed |
| `npm run typecheck` (`frontend/`) | exit 0 |
| `npx vitest run src/__tests__/electron/runtime-service-host.test.ts` (`frontend/`) | 1 file passed, 12 tests passed |

## Re-check 2026-09-12: sign hook repair `388de6973` (delta only)

Reviewer: Claude Fable 5.1, medium reasoning, no delegation. Read-only
review of `git diff 26fffb89a..388de6973 -- projects/chirality-app-dev/frontend/scripts projects/chirality-app-dev/frontend/src/__tests__/scripts`
(HEAD now `388de6973`; the other commit in the range, `825cacbbb`, is this
review record). The complete final `frontend/scripts/sign-electron-runtime-v2.mjs`
was read, together with the installed electron-builder call site
(`app-builder-lib` 26.15.3, `out/macPackager.js`, `out/util/resolve.js`,
`out/mac/MacTargetHelper.js`) to check the hook against the real call. No
build, packaging, signing or `security` command was run; only this file was
edited.

### Verdict for the delta: PASS

The signing policy is unchanged and the hook now matches electron-builder's
actual `sign(options, packager)` call.

### Policy unchanged

The diff touches only the hook's construction (`sign-electron-runtime-v2.mjs:80-98`).
`createSignOptions` (`:37-59`) is byte-for-byte the same: `hardenedRuntime: true`
on every file, the App entitlements on `appPath` and any `.app`, the Code Mode
host entitlements on `Contents/Resources/codex/bin/codex-code-mode-host`
only, the inherit entitlements everywhere else. `verifySignedBundle`
(`:65-78`) is unchanged: strict verification and the hardened-runtime flag
on both Codex binaries, then a deep strict verification of the bundle. The
entitlement sources are still electron-builder's own `optionsForFile` for the
bundle (`mac.entitlements`, `package.json:155`) and for a nested path
(`mac.entitlementsInherit`, `:156`), falling back to the checked-in plists
(`:89-92`). The policy tests at
`frontend/src/__tests__/scripts/sign-electron-runtime-v2.test.ts:22-43`,
`:56-75` are unchanged and pass.

### Fix complete for the real call

- `MacPackager.doSign` resolves the configured hook with
  `resolveFunction(type, config.sign, "sign", root)` and calls it as
  `customSign(opts, this)` (`node_modules/app-builder-lib/out/macPackager.js:324`,
  `:334`). `resolveFunction` imports the module and returns the named export
  `sign` if present, else `m.default || m`
  (`node_modules/app-builder-lib/out/util/resolve.js:21-58`). The module
  exports no `sign`, so the default export, `createCustomMacSign()` bound to
  `signAsync` and `verifySignedBundle` (`:86-98`), is what runs; its second
  argument (the `MacPackager`) is ignored by the function signature, so the
  packager's unbound `sign` method can no longer be picked up. That is the
  exact failure the coordinator reported.
- The `opts` electron-builder passes (`MacTargetHelper.js`, `buildSignOptions`)
  carry `app`, `identity` (hash or name), `type`, `platform`, `version`,
  `keychain`, `binaries`, `strictVerify`, `preAutoEntitlements`,
  `optionsForFile` and `provisioningProfile`; the hook spreads them into the
  `signAsync` options and only overrides `optionsForFile`, so nothing the
  packager decided (identity, keychain, ignore filter) is dropped.
- No other caller of the hook exists (`pack-electron.mjs:18` is a comment;
  `package.json:154` is the only binding), so the removed second-argument
  injection point has no remaining users; tests inject through the factory.
- Test `:56-67` calls the bound hook with a packager whose `sign` throws if
  used and asserts the verify result and that `packager.sign` was never
  called; it also asserts the default export is a function. Deterministic
  (in-process fakes, temp directory).

### Residual (Informational)

- R4: the resolution rule prefers a named export called `sign`. Adding one
  to this module in future would silently replace the bound default hook. A
  comment or a test asserting `import * as m` has no `sign` export would
  guard it.

### Re-check commands

| Command (cwd) | Result |
|---|---|
| `npx vitest run src/__tests__/scripts/sign-electron-runtime-v2.test.ts src/__tests__/scripts` (`frontend/`) | 21 files passed, 145 tests passed, 0 failed, 2.17 s |
