# W4 return: App renderer and routes

Assignment: W4 of the APP_V3_CODEX_HOST_REPLATFORM_20260912 spike (SPIKE_DESIGN sections 5, 6, 7, 10, 11, 12). Worktree `.claude/worktrees/project-first-impressions-06aed9`, branch `claude/chirality-codex-replatform-3999f1`. All paths below are under `projects/chirality-app-dev/frontend/`. No git write operations were performed; the lead commits. Nothing under `projects/chirality-runtime` source was edited (see the verification note about the gitignored client build).

## Files

Added:

- `src/app/api/harness/session/[id]/turn/stream/route.ts`
- `src/app/api/harness/session/[id]/turn/state/route.ts`
- `src/app/api/harness/session/[id]/requests/route.ts`
- `src/app/api/harness/session/[id]/requests/[requestId]/answer/route.ts`
- `src/components/shell/request-card.tsx` (RequestCard, RequestCards, ServerRequests)
- `src/components/settings/runtime-status.tsx` (RuntimeStatusView, RuntimeStatus)
- `src/__tests__/api/harness/turn-registry-routes.test.ts`
- `src/__tests__/lib/harness-client-turn-registry.test.ts`
- `src/__tests__/lib/harness-event-views-codex.test.ts`
- `src/__tests__/components/request-card.test.tsx`
- `src/__tests__/components/chat-panel-turn-attach.test.tsx`

Changed (production):

- `src/lib/runtime-client/daemon-harness-port.ts`: port interface gains `attachTurn`, `turnState`, `listRequests`, `answerRequest`; `DaemonTurnFrame` (UIEvent plus optional `seq`); `V3TurnRequest.model` and `.reasoningEffort`; `HostedBootstrapStatusResponse` type; `HostedBootstrapPort.getStatus` now returns registration plus status.
- `src/lib/runtime-client/runtime-daemon-harness-port.ts`: implements the four turn-registry methods over W2's `RuntimeClient.attachSessionTurn`, `sessionTurnState`, `listSessionRequests`, `answerSessionRequest`; `turn()` forwards `model` and `reasoningEffort`; `runningTurn(...).cancel()` only cancels the stream and never calls `interruptSession`; `grantProviderNetworkConsent` reads and returns status without mutation; `getStatus` reads hosted status through the project-scoped client.
- `src/lib/harness/http.ts`: `formatSseEvent` emits an `id:` line when a sequence is present; new `turnStreamResponse(turn)` builds the SSE `Response` whose cancel unsubscribes only.
- `src/app/api/harness/turn/route.ts`: uses `turnStreamResponse`; cancel no longer interrupts.
- `src/app/api/harness/hosted-bootstrap/provider-network-consent/route.ts` and `hosted-bootstrap/request.ts`: retained path, no-op returning the current status; the `consent` body field is ignored and no longer validated.
- `src/app/api/harness/hosted-bootstrap/status/route.ts`: now carries hosted account status for a registered folder (doc updated; code unchanged apart from the port contract).
- `src/lib/harness/client.ts`: `HarnessTurnStreamEvent.seq`; exported `parseSseFrame` handling `id:` lines, CRLF and comment frames; `openTurnStream(input, signal)`, `openAttachStream`, `attachHarnessTurn`, `getHarnessTurnState`, `listHarnessSessionRequests`, `answerHarnessSessionRequest`; `streamHarnessTurn(input, onEvent, signal)`; `V3TurnRequest.model` and `.reasoningEffort`.
- `src/lib/harness/hosted-bootstrap-client.ts`: every call now goes through App routes (status GET, login start and cancel, logout, bind, initialize); the retired `window.chirality.runtime.hostedAccount` IPC is no longer referenced; `grantHostedProviderNetworkConsent` removed; the transient retry ladder now keys on an App 503.
- `src/lib/shell/harness-event-views.ts`: `ToolActivityRow.summary`; `PermissionRequestRow.requestId`, `.method`, `.decidedBy`; new `ServerRequestRow`, `UserInputQuestion`, `CodexNotificationRow` types and `deriveServerRequests`, `selectPendingServerRequests`, `classifyServerRequestMethod`, `readUserInputQuestions`, `readElicitationMessage`, `deriveCodexNotifications`.
- `src/components/shell/chat-panel.tsx`: turn observation (attach, dedupe, reconnect), per-turn model and reasoning, four-mode permission selector, request cards, immediate rendering of `turn.interrupted` and `turn.failed`; details under UI changes.
- `src/components/shell/permission-requests.tsx`: doc comment and meta line show the Codex method and request id.
- `src/components/woven-dialogue/activity-shelf.tsx`: Codex item sentences for tool rows, row summary, new `Codex` tab with `CodexNotificationList` (Thinking lines and inspectable notifications).
- `src/components/settings/hosted-bootstrap-controller.tsx`, `hosted-bootstrap-view.tsx`: consent step removed; sign-out wording no longer speaks of "this project".
- `src/components/settings/settings-view.tsx`: hosted runtime group renders `RuntimeStatus`.
- `src/components/settings/runtime-settings.tsx`, `runtime-settings-controller.tsx`: the `runtime.daemon` install, start, stop and uninstall panel is gone; only the legacy local-model (oMLX residency) controls remain, and the hosted shell never probes them.
- `src/components/shell/shell-frame.tsx`: the top-bar runtime check reads `window.chirality.runtime.connectivity.get()` instead of the retired daemon status IPC.

Changed (tests): `src/__tests__/api/harness/fake-daemon-harness-port.ts`, `daemon-proxy-boundary.test.ts`, `turn-route-attachments.test.ts`, `hosted-bootstrap.test.ts`; `src/__tests__/lib/runtime-daemon-harness-port.test.ts`, `hosted-bootstrap-client.test.ts`; `src/__tests__/components/account-presentation.test.tsx`, `activity-view-presentation.test.tsx`, `chat-panel-empty-state.test.ts`, `chat-panel-failed-send.test.ts`, `chat-panel-folder-binding.test.tsx`, `chat-panel-model-selectors.test.tsx`, `chat-panel-native-attachments.test.tsx`, `chat-panel-runtime-reconnect.test.tsx`, `hosted-bootstrap.test.tsx`, `runtime-settings.test.ts`, `runtime-settings-reconnect.test.tsx`, `settings-view-codex.test.tsx`, `shell-frame-runtime-connectivity.test.tsx`.

Deleted: none by W4. (The worktree also shows W3 changes under `electron/`, `scripts/`, `package.json`, `src/types/chirality-window.d.ts`, `src/__tests__/electron/**`, plus `docs/harness/*.md` and `package-lock.json` changes that are not mine.)

## App route table

| App route | Method | Port call | Runtime route | Notes |
|---|---|---|---|---|
| `/api/harness/turn` | POST | `turn(body)` | `POST .../sessions/:id/turn` | SSE; frames carry `id: <seq>` when Runtime supplies one; closing the response unsubscribes only |
| `/api/harness/session/[id]/turn/stream?after=N` | GET | `attachTurn(id, after)` | `GET .../turn/stream?after=N` | 400 on a malformed `after`; 404 with `details.reason = TURN_NOT_ACTIVE` when nothing is retained |
| `/api/harness/session/[id]/turn/state` | GET | `turnState(id)` | `GET .../turn/state` | `{active, turnId?, lastSeq, startedAt?, endedAt?}` |
| `/api/harness/session/[id]/requests` | GET | `listRequests(id)` | `GET .../requests` | pending server requests |
| `/api/harness/session/[id]/requests/[requestId]/answer` | POST `{answer}` | `answerRequest(id, requestId, answer)` | `POST .../requests/:requestId/answer` | shape check for `approval`, `userInput`, `elicitation`; Runtime validates against the method |
| `/api/harness/interrupt` | POST | `interrupt` | `POST .../interrupt` | unchanged; the only path that stops a turn |
| `/api/harness/permission` | POST | `decidePermission` | `POST .../permission` | unchanged; approvals still answered here |
| `/api/harness/hosted-bootstrap/status` | GET | `getStatus` | `hostedBootstrapStatus` | now returns `{registration, projectId, status}` |
| `/api/harness/hosted-bootstrap/provider-network-consent` | POST | `grantProviderNetworkConsent` | `hostedBootstrapStatus` | retained path, no-op, returns status |
| `/api/harness/hosted-bootstrap/login/start`, `login/cancel`, `logout`, `project/bind`, `project/initialize` | POST | as before | as before | unchanged, now the renderer's only path for these |
| native-plan clarification routes | as before | `listNativePlanClarifications`, `replyNativePlanClarification` | daemon native-plan routes | paths kept; the list still comes from the daemon native-plan routes |

## UI changes by surface

Chat panel. On open (resume or reconnect) the panel calls `turn/state`; when a turn is active it marks the chat running, replays the persisted log into the event bridge, then attaches with `after=0`. Events are deduplicated by `eventId` against the hydrated log; `message.delta` frames from the attach stream are rendered as streamed text (the attach from seq 0 is the complete text source, so text is assembled even when the log already holds those deltas). A stream that closes without a terminal frame asks `turn/state` first: an inactive turn settles from the log; an active turn or an unreachable Runtime shows "Reconnecting to the running turn..." with backoff (1, 2, 4, 8, 15, 30 seconds) and re-attaches after the last sequence seen; a 404 `TURN_NOT_ACTIVE` on re-attach settles from the log. The chat never shows Idle while the Runtime says the turn is active. Stop calls the interrupt route and leaves the stream open; `turn.interrupted` and `turn.failed` render the moment they arrive. Model and reasoning effort are selectable between turns (disabled only while running or without a catalog) and sent as top-level `model` and `reasoningEffort` on every turn; the selectors start from the explicit choice, else the session's recorded pair when the catalog offers it, else the catalog default, and never offer a pair the Runtime did not publish. A new Permissions selector offers four modes explained in Codex terms: Read only (read-only sandbox, approval on request), Ask before changes (workspace-write, on request), Write in workspace (workspace-write, never), Full access (danger-full-access, never); a recorded chat with an unknown mode names it and asks the user to continue with Write in workspace. Permission cards are fed by `tool.permission` with `active` from turn state and show the Codex method and request id. New request cards answer `item/tool/requestUserInput` (radio options, free text, secret inputs) and `mcpServer/elicitation/request` (Accept, Decline, collapsed request JSON); a request already presented as a Plan Mode clarification is not shown twice.

Activity panel. Tool rows use the Codex item type as `toolName` with a sentence per type (command execution, file change, MCP tool call, dynamic tool call, web search, image view, image generation) and the adapter summary; sub-agent rows unchanged; a new Codex tab lists a "Thinking" line for each completed reasoning item and every other notification by method with its params collapsed for inspection. The event log remains inspectable through the existing Events tab.

Account row and popover. The provider-network consent step is gone; setup leads straight to sign-in. Sign-out is labelled "Sign out" and explained as affecting only Chirality. Status now arrives through the App status route; no admission or identity wording is shown.

Settings. The `runtime.daemon` install, start, stop and uninstall panel is removed. The hosted Runtime group shows a read-only status derived from the connectivity snapshot (Running, Starting, Stopped with the last error and a "quit and reopen the App" hint, or "Unavailable outside Chirality Desktop") and states that the service is started and stopped by Chirality.

Top bar. The explicit runtime check uses the connectivity bridge; messages read "Runtime service is unreachable: <error>" or "Runtime status is not reported yet".

## Decisions

1. Hosted account status moves onto the App status route. W3 removed the `runtime.hostedAccount` and `runtime.models` preload bridges, and under D-GOV-43 there is no account-host admission proof, so `HostedBootstrapPort.getStatus` now reads status through the project-scoped Runtime client and the renderer client uses the App routes for status, login start and cancel, and sign-out. The transient retry ladder keys on an App 503.
2. W2's client methods are used directly. Their source is present in `packages/client/src/client.ts`, so the port calls `attachSessionTurn(projectId, sessionId, {after}, signal)`, `sessionTurnState`, `listSessionRequests` and `answerSessionRequest(projectId, sessionId, requestId, answer, signal)` with no local fallback interface.
3. Cancel never interrupts. Dropping a turn observer (POST stream or attach) only unsubscribes; the only interrupt path is the explicit interrupt route, and the interruption is rendered from the Runtime's own `turn.interrupted` event.
4. Clean stream end is not assumed to be completion. The panel consults `turn/state` before deciding; only an inactive turn settles from the log. When the settle read of the log fails, no error is shown: the streamed text stays on screen and reopening the chat replays the log.
5. Text source. The first source seen wins between `chat:delta` UIEvents (current coordinator) and persisted `message.delta` harness events, so the panel works with either emission without doubling text.
6. `ask` is a supported posture. The former "Ask before changes is no longer supported" interstitial now applies only to modes outside the four; recorded chats with `ask` continue without an extra step.
7. Native-plan clarifications keep their routes. The clarification list still comes from the daemon native-plan routes; the same Codex request would also appear as a `codex.request` card, so cards suppress request ids already shown by the plan sidebar.
8. Legacy oMLX residency controls remain in `RuntimeSettingsView` for the non-hosted shell only; the hosted shell renders `RuntimeStatus` and never probes local models.
9. Verification build. `@chirality/runtime-client` and `@chirality/runtime-contracts` have no committed `dist`; for verification I ran `npx tsc -b` in `packages/contracts` and `packages/client` (gitignored output only, no source edits).

## Tests

Command: `npx vitest run src/__tests__ --exclude 'src/__tests__/electron/**' --exclude 'src/__tests__/scripts/**'`.
Result: Test Files 3 failed, 163 passed, 1 skipped (167); Tests 1 failed, 1605 passed, 4 skipped (1610).

The three failing files are all `src/__tests__/integration/**` and fail outside W4 scope: `controlled-ci-runtime.integration.test.ts` (esbuild cannot resolve `@chirality/runtime-core/runtime-conformance-v2` while W1 rewrites core), `runtime-canonical-replay-restart.integration.test.ts` (cannot resolve the `@chirality/runtime-cli` package entry), `runtime-desktop-cli-shared-daemon.integration.test.ts` (imports `electron/daemon-instruction-root`, removed by W3).

Excluding integration as well: Test Files 160 passed (160); Tests 1588 passed (1588).

Command: `npx tsc --noEmit --incremental false`. Result: 2 errors, both in `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` (the removed electron module and a resulting implicit any). No errors under `electron/**` or `src/__tests__/electron/**` at the time of the run.

New coverage: attach-and-dedupe, reconnect state (Reconnecting shown, re-attach after last seq, settle on inactive state, 404 `TURN_NOT_ACTIVE` settle), Stop as interrupt with immediate `turn.interrupted` rendering (`chat-panel-turn-attach.test.tsx`); request card answering for user input and elicitation, failure retention, notification list rendering (`request-card.test.tsx`); permission mapping with request id and method, server request derivation, thinking and notification rows, Codex tool rows (`harness-event-views-codex.test.ts`); per-turn model override sent as top-level fields, selectors open between turns and disabled while running (`chat-panel-model-selectors.test.tsx`); `parseSseFrame` id parsing, attach URL, answer POST (`harness-client-turn-registry.test.ts`); new App routes including the `id:` line, `after` validation, answer validation, 404 mapping (`turn-registry-routes.test.ts`); port attach, state, requests, answer, cancel-without-interrupt, model forwarding, hosted status through `getStatus` (`runtime-daemon-harness-port.test.ts`); App-owned runtime status instead of the daemon panel (`runtime-settings.test.ts`, `account-presentation.test.tsx`); connectivity-based top-bar check (`shell-frame-runtime-connectivity.test.tsx`).

## Needed outside W4 scope

- `src/types/chirality-window.d.ts` (W3) now declares `runtime.service.restart()`; the renderer does not yet offer that retry. A "Restart Runtime service" action in the settings status view would use it.
- `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` imports the removed `electron/daemon-instruction-root`; it needs W3's replacement or retirement.
- `HostedBootstrapStatus` (W2 contracts) still allows `ceremony: 'consent-required'`; the renderer treats it as "Sign in required" but the value could be dropped from the contract.
- `deriveTranscriptView` in `src/lib/shell/harness-event-views.ts` ignores `codex.*` event types; transcript projection of raw Codex notifications is not attempted here.
- The turn POST stream only carries `id:` lines when the Runtime frames carry `seq`; W2's registry does for attach streams, and the same is expected for the POST stream.
- `docs/harness/*.md` and `package-lock.json` show changes in the worktree that are not W4's.

## Open risks

- The reconnect loop relies on `turn/state` being reachable to distinguish a finished turn from a dropped connection; when the Runtime is down the panel keeps reconnecting (by design) until the user leaves the chat or starts a new one.
- If the Runtime ever closes a POST turn stream cleanly without a terminal frame while `turn/state` reports inactive and the log cannot be read, the turn shows as finished with whatever text was streamed and no error.
- Approval decisions still go through the legacy `/api/harness/permission` route rather than the new answer route; both reach the same Runtime request registry, but the permission card does not yet offer `allowForSession`.
- The hosted bootstrap controller's retry ladder now treats any App 503 as transient, which includes a genuinely unavailable engine; the ladder is short (250 ms, 1 s, 5 s) so the cost is bounded.
- Live checks against a running App-owned Runtime were not performed in this session; verification is unit and route level only.
