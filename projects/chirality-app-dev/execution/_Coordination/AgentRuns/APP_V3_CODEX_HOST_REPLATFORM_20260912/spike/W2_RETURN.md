# W2 return: Daemon transport and service glue

Assignment: W2 of `SPIKE_DESIGN.md` section 12 (sections 5, 6 validator, 7 routes and broker, 11 routes). Executor: Fable 5.1 TASK instance, 2026-09-12. Basis: the worktree at branch `claude/chirality-codex-replatform-3999f1` on main `e83cb1f47` plus the lead's pre-authored contract seam. No git write operations were performed; the lead commits.

## 1. Files added

- `projects/chirality-runtime/packages/daemon/src/turn-registry.ts`: the Runtime-owned turn execution of design section 5 (`TurnRegistry`, `TurnFrame`, `TurnSubscription`, `TurnRegistryService`, `TurnShutdownSettlementPort`).
- `projects/chirality-runtime/tests/turn-registry.test.ts`: registry tests over a scripted stub service (7 tests).

## 2. Files changed

Contracts (`packages/contracts/src`, beyond the lead's seam):
- `errors.ts`: `TURN_NOT_ACTIVE` added to `RUNTIME_ERROR_CODES` so the client maps the 404 to a typed code.
- `protocol.ts`: `validateServerRequestAnswer` and `validateAnswerSessionRequestRequest` (shape gate for `POST .../requests/:id/answer`); `RuntimeSseFrame` is now `UIEvent & { seq?: number }`.
- `session.ts`: additive `RuntimeSessionRecord.lastUsedModel` and `lastUsedReasoningEffort`.
- `harness/agent-engine-port.ts`: additive `AgentEngineRunInput.reasoningEffort` (effective per-turn effort; `opts.model` carries the effective model).
- `v2-events.ts`: `validateHarnessEventV2` accepts `codex.notification`, `codex.request` (non-empty `method`, optional non-empty `requestId`) and `codex.request.resolved` (`outcome` in the four values, optional `method`, `requestId`, `decidedBy`). Extra payload fields are allowed only for these three passthrough types.

Core (`packages/core/src`):
- `turn-coordinator.ts`: validates `SessionTurnRequest.model` and `.reasoningEffort` against the hosted identifier patterns (400 `INVALID_REQUEST`, reasons `TURN_MODEL_INVALID` and `TURN_REASONING_EFFORT_INVALID`, before any event); passes the effective model in `opts.model` and `input.session.engineSelection.model`, the effective effort in `input.reasoningEffort` and `input.session.reasoningEffort`; records the overrides on `turn.accepted`; keeps the stored session's `engineSelection` unchanged when an override was used; writes `lastUsedModel` and `lastUsedReasoningEffort` on every terminal update; `interrupt(projectId, sessionId, reason?)` records the reason on the synthesized `turn.interrupted`; new `isActive(projectId, sessionId)`.
- `runtime-service.ts`: `createDelegatedPermissionBroker(port)` returning a `PermissionDecisionPort` that forwards `{requestId, decision}` to `port.answerApprovalByToolUseId(projectId, sessionId, requestId, decision)`; the port type `DelegatedApprovalAnswerPort` names only that method. `interruptSession` accepts the optional reason.
- `session-store.ts`: `markInterruptedOnShutdown(projectId, sessionId, turnId, reason = "service-shutdown")`, which appends `turn.interrupted {reason}` and moves a still-running session to `interrupted`; a settled session is left unchanged and the method returns `false`.

Client (`packages/client`):
- `src/sse.ts`: `SseFrame.seq` derived from a numeric `id`; `parseUiEvent` accepts any non-empty event name (the closed `uiEventTypes` set is gone), rejects arrays, and copies `seq` onto the UI frame.
- `src/client.ts`: SSE requests pass `timeoutMs: 0` (idle timeout disabled; JSON requests keep 30 s); `request()` only arms `setTimeout` when the value is positive; new `attachSessionTurn(projectId, sessionId, {after})`, `sessionTurnState`, `listSessionRequests`, `answerSessionRequest(projectId, sessionId, requestId, answer)`; `turnSession` sends the whole `SessionTurnRequest`, so `model` and `reasoningEffort` pass through unchanged.
- `test/client.test.ts`: three new tests.

Daemon (`packages/daemon/src/runtime-daemon.ts`):
- Turn routes go through the registry (section 3). SSE writer emits `id: <seq>` on every frame and `: keepalive` comments every 15 s (`sseKeepaliveMs` option for tests); a client close only unsubscribes (`cancelSse`/`trySseInterrupt` on close are gone); the writer never calls interrupt.
- Daemon stop still interrupts live work once: every active registry turn (attached or not) with reason `service-shutdown`, and the Agent 1 `/runs` stream through its manager identity when known. The stop-grace, force and degraded-state accounting is unchanged in shape; the pre-identity Agent 1 cases keep their existing tests.
- `RuntimeDaemonOptions`: added `turnRegistry?`, `requests?: DelegatedRequestPort`, `sseKeepaliveMs?`; `delegated?` is now the local `DelegatedControlPort` (`startGeneration`, `close`, optional `assertProjectRoot` and optional legacy v2 operations that answer 503 when absent); `approvals?` is the local `RuntimeApprovalControl`. Removed `supplierAuthority?` and `accountHost?` together with their start/stop hooks and the account-proof header path, because their modules (`supplier-authority-*.ts`, `host-account-*.ts`, `supervisor-server.ts`) are on W1's retirement list and the daemon must not import them. `assertNoPrivateAuthoritySurface` (from `supervisor-server.ts`) is no longer applied to bodies and responses.
- Hosted-bootstrap v3 routes remain wired to `hostedBootstrap` with the same five methods.

Tests: `tests/daemon.test.ts` (rewritten disconnect test plus four new route tests; imports the daemon from source), `tests/runtime-v3-api.test.ts` (one new test; imports the daemon from source), `tests/turn-hardening.test.ts` (two new tests), `tests/session-and-residency.test.ts` (one new test), `tests/v2-contracts.test.ts` (one new test).

Not mine, already present when dispatched: `contracts/delegated.ts`, `contracts/harness/event-schema.ts` (the lead's seam).

## 3. Route table

All routes are under `/v1/projects/:projectId/sessions/:sessionId`, bearer-authenticated with the project scopes shown.

| Route | Scope | Request | Response |
|---|---|---|---|
| `POST .../turn` | `sessions:write` | `SessionTurnRequest` (`message` or `prompt`, optional `turnId`, `model`, `reasoningEffort`, `interactionMode`, `permissionMode`, `methods`, `attachments`, `opts`) | 200 `text/event-stream` of the new turn from seq 1. Pre-stream failures stay typed JSON: 409 `SESSION_TURN_IN_PROGRESS`, 404 `SESSION_NOT_FOUND`, 400 `INVALID_REQUEST`. Client close unsubscribes only. |
| `GET .../turn/stream?after=<seq>` | `sessions:read` | `after` non-negative integer, default 0 | 200 SSE: buffered frames with `seq > after`, then live frames until the terminal frame, then end. 404 `TURN_NOT_ACTIVE` when nothing is active or retained; 400 for a malformed `after`. |
| `GET .../turn/state` | `sessions:read` | none | 200 `SessionTurnState` `{active, turnId?, lastSeq, startedAt?, endedAt?}`; 404 `SESSION_NOT_FOUND` for an unknown session. |
| `POST .../interrupt` | `sessions:write` | none | 200 `{interrupted: true, sessionId}`; runs through the registry (joins an in-flight interruption) and then `RuntimeService.interruptSession`. |
| `POST .../permission` | `sessions:write` | `PermissionDecisionRequest {requestId, decision, reason?}` (`requestId` is the tool-use id, that is the Codex item id) | 200 `{accepted: true, requestId, decision}`; the service's permission broker forwards to `answerApprovalByToolUseId`. 409 `ENGINE_UNAVAILABLE` when no broker is composed; 400 for a malformed decision. |
| `GET .../requests` | `sessions:read` | none | 200 `SessionRequestsResponse {requests: PendingServerRequest[]}`; 503 `ENGINE_UNAVAILABLE` when no `requests` port is composed. |
| `POST .../requests/:requestId/answer` | `sessions:write` | `AnswerSessionRequestRequest {answer}` with `answer` one of `{kind:"approval", verdict}`, `{kind:"userInput", answers}`, `{kind:"elicitation", action, content?}` | 200 `{sent: true}`; 400 `INVALID_REQUEST` (reason `SERVER_REQUEST_ANSWER_INVALID`) for any other shape; 503 without a port. A wrong `kind` for the request's method is the delegated runtime's `INVALID_REQUEST`. |

SSE wire format: `id: <seq>\nevent: <UIEvent.type>\ndata: <JSON of UIEvent.data>\n\n`, with `: keepalive\n\n` comment lines while idle. Frames are the `UIEvent`s the coordinator yields (`harness:event`, `session:init`, `chat:delta`, `process:exit`, ...); the terminal frame of every turn is `process:exit`.

Every other route (health, daemon status, projects, credentials, models, roles, methods, agents, scaffold, runs, sessions CRUD, boot, replay, context resolve, session methods, native-plan routes, v2 login, approvals and delegated routes, v3 hosted-bootstrap routes) is unchanged in shape.

## 4. Decisions

1. `TurnRegistry.start` awaits the first event before resolving. Failures before the first event therefore keep their typed HTTP status (the existing daemon contract), and the registry never records a turn that did not start. A `starting` set guards the window so a concurrent second start gets 409.
2. A subscription is a small manual iterator rather than an async generator, so `close()` (and `return()`) wake a pending wait immediately; a disconnected writer therefore leaves the daemon promptly instead of lingering until the next frame.
3. The terminal frame is the end of the coordinator's stream (its last frame is `process:exit`). If the stream itself throws after the first event, the registry appends a synthetic `process:exit {exitCode: 1, fatal: true, errorType: "INTERNAL_FAILURE"}` so subscribers and the App see a terminal rather than a silent end, and logs only a bounded message.
4. Retention is 10 minutes after the terminal frame (`setTimeout`, unref'd); a new turn for the same session replaces a retained record immediately.
5. `interrupt` on the registry joins concurrent calls for the same active turn into one in-flight `interruptSession`, which is what keeps the "interrupts once at shutdown" tests true when the stop path interrupts both by turn and by attached stream. With no active turn, the call still delegates to the service (Agent 1 runs, idempotent no-op otherwise).
6. Shutdown: `RuntimeDaemon.stop()` interrupts active registry turns with reason `service-shutdown` and waits within the existing 2 s grace; unsettled work still forces transport and degrades exactly as before. `TurnRegistry.close({reason, graceMs})` is the composition-level shutdown (SIGTERM handler in W1's `app-owned-composition.ts`): it interrupts, waits, and settles leftover session records through `SessionStore.markInterruptedOnShutdown` so a relaunch never shows a dead turn as running.
7. The per-turn override is applied to the engine input's `session` copy as well as `opts.model` and the new `reasoningEffort` field, so W1's current adapter (which validates `input.opts.model` against `input.session.engineSelection.model` and reads `session.reasoningEffort`) works without change, while the stored session keeps its default `engineSelection`. The session-init attribution check for local providers compares against the effective turn model.
8. `parseUiEvent` accepts any non-empty event name: the Runtime streams the open `UIEvent` set and every Codex notification passes through `harness:event`, so a closed type list would drop faithful frames. JSON arrays are now rejected like non-objects.
9. Removed the private supplier-authority body/response assertion and the `supplierAuthority`/`accountHost` daemon options, because their modules are retired by W1 and the daemon must compile without them. The v3 hosted-bootstrap routes therefore authorize through the ordinary bearer scopes (`runtime:read` for status, `credentials:write` for the mutations) with the same failure logging (operation, project, code, status, bounded message; never URLs or account fields).
10. The retained v2 delegated routes call the legacy operations only when the composed runtime still has them; otherwise they answer 503 `ENGINE_UNAVAILABLE`. This lets W1's rewritten `DelegatedRuntime` (which no longer has `assertProjectRoot`, `capabilities`, `preflight`, `grantConsent`, `decideApproval`, `pendingApprovals`, `authorizeControl`) be passed as `delegated` without a compile error.
11. `tests/daemon.test.ts` and `tests/runtime-v3-api.test.ts` import `RuntimeDaemon` from `../packages/daemon/src/runtime-daemon.js` instead of the package entry. The package entry (`dist/index.js`) re-exports W1's in-flux modules and currently fails to load under vitest (`Missing "./runtime-conformance-v2" specifier in "@chirality/runtime-core"`); the source import keeps W2's tests independent of that. The lead may revert to the package import once `index.ts` settles.
12. No em-dashes were introduced. No payload that can carry account data is logged: the registry logs method-free identifiers and bounded messages; the daemon's existing bounded diagnostics are unchanged.

## 5. Tests

Commands run from `projects/chirality-runtime`.

Type checks (`npx tsc -b packages/<pkg>`):
- contracts: clean.
- core: clean (W1's `delegated-engine-adapter.ts` errors present at the start of the assignment were fixed by W1 during it).
- client: clean.
- daemon: `runtime-daemon.ts` and `turn-registry.ts` compile with no errors. Remaining errors are all in W1's files, and none are attributable to W2 except one composition site: `standalone.ts(387)` passes a `DelegatedRuntime` as `approvals` (`RuntimeApprovalControl`), which W1's rewritten class no longer satisfies; that legacy composition is on W1's retirement list. Error counts by file at return time: `standalone.ts` 21, `hosted-standalone.ts` 17, `hosted-private-composition.ts` 12, `codex-containment.ts` 12, `codex-login.ts` 10, `hosted-packaged-release-state.ts` 7, `hosted-release-provisioner.ts` 5, `codex-authenticated-transport.ts` 5, `account-free-login-observation.ts` 5, `runtime-conformance-v2-admission.ts` 4, `hosted-bootstrap.ts` 3, `codex-supervisor.ts` 3, `codex-worker.ts` 2, and one each in `native-admission/src/index.ts`, `supplier-authority-journal.ts`, `supplier-authority-controller.ts`, `standalone-bin.ts`, `hosted.ts`, `hosted-private-entry.ts`, `hosted-packaged-release.ts`, `host-account-release.ts`, `codex-session.ts`. Their causes are missing core exports W1 removed (`ApprovalStore`, `HostedConsentStore`, `RuntimeConformance*`, `runtimeStageC*`) and W1's changed `DelegatedRuntime` and `DelegatedEngineAdapterOptions` surfaces.

In-scope files (the seven files below, as counted by vitest inside the full run): 104 tests, all passing:
- `tests/turn-registry.test.ts` 7 (start and background execution, frame numbering from 1, replay of missed frames after a closed subscription, retained replay, 409 on a second start, typed pre-stream failure with no record, 404 `TURN_NOT_ACTIVE` before any turn and after 10 minute retention expiry with fake timers, no interrupt on close, joined in-flight interruption, synthetic terminal on a mid-stream throw, `close()` with shutdown reason and settlement of unsettled turns).
- `tests/daemon.test.ts` 20 (14 existing kept; the old "interrupts a disconnected SSE turn" test replaced by "keeps a turn running after its subscriber disconnects and replays the missed frames on attach", plus interrupt route and 404/400 handling, keepalive comments with a 20 ms cadence, requests routes with a stub port including answer-shape validation, and 503 without a port plus the permission route through `createDelegatedPermissionBroker`).
- `tests/runtime-v3-api.test.ts` 33 (32 existing plus client pass-through of model and effort, session `lastUsed*` fields, and attach after `cancel()` with `after=2` recovering frames 3 to 6 with no interruption).
- `tests/turn-hardening.test.ts` 11 (9 existing plus overrides and malformed overrides, and the interruption reason on the synthesized terminal).
- `tests/session-and-residency.test.ts` 7 (6 existing plus `markInterruptedOnShutdown`).
- `tests/v2-contracts.test.ts` 18 (17 existing including the expanded `it.each` cases, plus the codex passthrough types).
- `packages/client/test/client.test.ts` 8 (5 existing plus parsing, attach with the idle timeout disabled, and the state/requests/answer/pass-through calls).

Full suite (`npm test -- --maxWorkers=1`): exit code 1. 86 test files: 44 passed, 41 failed, 1 skipped. 632 tests: 561 passed, 68 failed, 3 skipped. All seven W2 files passed inside this run. None of the 68 failures is attributable to W2 files; every failed file fails while loading or composing W1-scope modules:
- Package entry load failures (`Missing "./runtime-conformance-v2" specifier in "@chirality/runtime-core"`, raised by `packages/daemon/dist/hosted-packaged-release.js` when `@chirality/runtime-daemon` is imported): `packages/cli/test/cli.test.ts`, `tests/attachment-content-path.test.ts`, `tests/bootstrap-api.test.ts`, `tests/codex-primary-chat-integration.test.ts`, `tests/hosted-bootstrap-integration.test.ts`, `tests/hosted-private-composition.test.ts`, `tests/hosted-packaged-release.test.ts`.
- Missing retired core or daemon modules or exports (`approval-store`, `exact-supply`, `hosted-consent`, `runtime-admission-lock`, `runtime-conformance*`, `runtime-dependencies`, `HostedConsentStore`, `runtimeStageC*`, `runtimePolicyParameterSchemaDigestV2`, `compareRuntimeUtf8V2`, `createCustomSupplyVerifier`): `tests/approval-store.test.ts`, `tests/delegated-runtime.test.ts` (W1 owns its section 8 regression), `tests/manager-approval-integration.test.ts`, `tests/codex-native-tools.test.ts`, `tests/codex-session.test.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-attachment-adapter.test.ts`, `tests/codex-authenticated-transport.test.ts`, `tests/codex-containment.test.ts`, `tests/d36-v2-connected.test.ts`, `tests/standalone.test.ts` (8 of 14), `tests/account-free-login-observation.test.ts`, `tests/runtime-conformance-v2-admission.test.ts` (12 of 14), `tests/runtime-conformance-v2.test.ts`, `tests/runtime-conformance.test.ts`, `tests/runtime-conformance-inventory.test.ts`, `tests/runtime-dependencies.test.ts`, `tests/exact-*.test.ts` (eight files), `tests/hosted-consent.test.ts`, `tests/hosted-identity-binding.test.ts`, `tests/hosted-release-provisioner.test.ts`, `tests/local-supplier-authority.e2e.test.ts`, `tests/supplier-authority-controller.test.ts`, `tests/supplier-authority-journal.test.ts`, `tests/runtime-admission-native.test.ts`, `tests/p2-host-xpc-probe.test.ts` (deleted `tools/native-admission` probe).
All of these are tests of modules on W1's retirement or rewrite list (design section 1 and 12); they are expected to be deleted or rewritten by W1.

## 6. Needed outside my scope

1. `packages/daemon/src/index.ts` (W1): add `export * from "./turn-registry.js";` so the composition and the App can import `TurnRegistry` and `DelegatedRequestPort` from the package.
2. `app-owned-composition.ts` (W1): construct `new TurnRegistry(service, { sessions, logger })`, pass it as `turnRegistry`, pass the `DelegatedRuntime` as `requests` (it already has `pendingRequests` and `answerRequest` with the expected signatures) and as `delegated`, compose `RuntimeService` with `createDelegatedPermissionBroker(delegatedRuntime)` as its `permissions` port, and on SIGTERM call `turnRegistry.close({ reason: "service-shutdown" })` before or alongside `daemon.stop()` (the daemon's own stop interrupts too; the registry call is what settles session records for turns that do not finish in time).
3. `delegated-engine-adapter.ts` (W1): read `input.reasoningEffort ?? session.reasoningEffort` and `input.opts.model` for `turn/start`; today it works because the coordinator also overrides the `session` copy on the input, but the explicit field is the intended contract.
4. `RuntimeDaemonOptions.supplierAuthority` and `.accountHost` were removed; W1's `hosted-private-composition.ts` and `hosted-standalone.ts` (both retired) are the only consumers.
5. Frontend (W4): `RuntimeSseFrame` now carries `seq`; `attachSessionTurn`, `sessionTurnState`, `listSessionRequests`, `answerSessionRequest` are available on `RuntimeClient`; `TURN_NOT_ACTIVE` is a typed `RuntimeError` code.
6. W1 added a `validateServerRequestAnswer` in `core/delegated-runtime.ts` (assertion style) while contracts now exports one of the same name (returning the normalized answer). They do not collide at import sites today, but the lead may want a single definition; the contracts one is the wire gate used by the route.

## 7. Open risks

1. The daemon package entry does not build or load until W1 finishes retiring its modules; W2's tests were made independent of it, but `tests/runtime-v3-api.test.ts` still imports `@chirality/runtime-client` and `@chirality/runtime-core` from `dist`, so a broken core build would block them as well (core is clean at return time).
2. The Agent 1 `/runs` stream is not registry-owned. Under the disconnection rule it now keeps draining silently after a client close; it is interrupted only at daemon stop and only once its manager identity is known. Nothing on the App path uses it.
3. `RuntimeDaemon.stop()` no longer aborts a turn that outlives the 2 s grace (the registry keeps it running in the process). In the service this is followed by process exit; in tests such turns finish or stay pending without holding the event loop.
4. `hosted-paths.ts` is still imported by the daemon for `hostedProjectClientId` (v3 hosted-bootstrap registration). It is not on W1's retirement list; if W1 removes it the two-line helper must move into `runtime-daemon.ts`.
5. `markInterruptedOnShutdown` appends a terminal without a coordinator lock; it is intended for the process-exit path only. If a turn later completes in the same process, a second terminal would follow. `TurnRegistry.close()` only calls it for turns that did not finish within the grace.
