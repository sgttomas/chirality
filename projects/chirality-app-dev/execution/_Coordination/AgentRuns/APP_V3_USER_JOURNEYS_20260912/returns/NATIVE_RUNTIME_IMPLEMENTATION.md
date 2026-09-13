# Native Runtime interaction implementation return

TASK Type 2; no delegation. Implementation complete within the assigned Runtime packages/tests. No App source, instructions, governance, Git mutations, packaged builds or live supplier/account operations. Parent owns independent review, integration, actual native qualification and acceptance. This return is derivative implementation evidence, not a governed acceptance act.

## Exported client contract

- `SessionSteerRequest { operationId: string; expectedTurnId: string; text: string }` and `SessionSteerResponse { operationId: string; turnId: string; status: "accepted" | "rejected" | "unknown"; message?: string; providerTurnId?: string }` exported from Runtime contracts.
- `RuntimeClient.sessionTurnSteer(projectId, sessionId, request, signal?)` returns `Promise<SessionSteerResponse>`.
- `RUNTIME_ROUTES.sessionTurnSteer(projectId,sessionId)` is POST `/v1/projects/:projectId/sessions/:sessionId/turn/steer`. Existing sessions:write authorization and session lookup apply.
- `expectedTurnId` is the Runtime turn, never an arbitrary native target supplied by the renderer.
- `codex.steer` harness evidence data contains request fields plus status submitted/accepted/rejected/unknown, message and providerTurnId where known. Stable operationId is reused only for identical payload/target reconciliation; conflict returns 409.

## Production changes

`packages/contracts/src/{protocol.ts,delegated.ts,harness/event-schema.ts}`: additive steering request/response validation, route, supervisor capability and event type.

`packages/contracts/src/harness/transcript-replay.ts`: shared `deriveTranscriptView` now reconstructs primary native agent messages by session/thread/turn/item. `TranscriptItem` adds nativeItemId, providerThreadId and phase (`commentary` / `final_answer` / null). Completed snapshots replace partial text; repeated event IDs and late deltas do not duplicate text. Native-evidenced turns suppress legacy aggregate assistant copies. Other historical turns retain old behavior. Steering intent/outcomes become one user message with receipt state.

`packages/core/src/delegated-engine-adapter.ts`: preserves native message/reasoning/plan deltas and turn completion as codex.notification. Actual native IDs are derived from raw params and `codex.isPrimaryThread` identifies parent versus descendants. Checklist updates remain their distinct raw `turn/plan/updated` records. Completed collab CALLS produce tool completion plus raw target states/results, never fabricated subagent completion. Legacy text remains for older clients.

`packages/core/src/delegated-runtime.ts`: resolves the existing session's live worker and checks exact Runtime turn before calling its optional native steering capability.

`packages/daemon/src/codex-supervisor.ts`: sends stock 0.154 `turn/steer` with expected native turn and clientUserMessageId after checking live worker generation, Runtime turn, provider generation and thread ownership. Only request/method/parameter JSON-RPC errors are definitive rejection; transport/internal errors and mismatched acknowledgments remain unknown. Descendant serverRequest/resolved now clears its pending request. Known active children at parent completion produce an explicit observation-limit notification.

`packages/daemon/src/native-steering.ts` (new): Runtime-owned deduplication using the existing session event journal. Intent is persisted before dispatch; `SessionStore.appendEvent` uses fsynced append. Identical concurrent operations join, later/restarted requests consult persisted evidence, and intent without outcome remains unknown rather than resending. Exact primary userMessage.clientId/content/native turn evidence can reconcile receipt on the response/reconciliation path. No silent new turn, Stop, permission or instruction changes.

`packages/daemon/src/{runtime-daemon.ts,turn-registry.ts}`: authorized route, Runtime turn-state guard and publication of already-persisted steering events to matching active/retained turn subscribers.

`packages/client/src/client.ts`: encoded JSON client route.

## Validation

Passed `npm run typecheck` (`tsc -b --pretty false`).

Passed one final focused invocation: `npx vitest run tests/native-steering.test.ts tests/native-message-replay.test.ts tests/native-event-adapter.test.ts tests/codex-supervisor.test.ts tests/codex-attachment-adapter.test.ts tests/turn-registry.test.ts tests/daemon.test.ts tests/delegated-runtime.test.ts` — 8 files, 76 tests passed.

New tests cover fsynced-journal interface ordering, concurrent/restarted deduplication, conflicting operation IDs, stale turn rejection, crash after intent, lost acknowledgment, native echo reconciliation, negative child echo, client route encoding, malformed/authenticated route requests, partial/full/repeated/native-null-phase/legacy message replay, preserved checklist/summary notifications, completed spawn with running child, descendant identity/question resolution and explicit late-child observation limit. Existing supervisor, delegated lifecycle, attachment, daemon and turn registry cases also passed. `git diff --check -- projects/chirality-runtime` passed.

New tests: `tests/native-steering.test.ts`, `tests/native-message-replay.test.ts`, `tests/native-event-adapter.test.ts`. Extended `tests/codex-supervisor.test.ts` and `tests/daemon.test.ts`.

## Remaining qualification and limits

- No native supplier/model run or packaged UI proof performed by this child; parent must qualify stock 0.154 interaction and full App integration.
- Current primary-turn observer retires when its primary completes. Known active descendants generate `codex.notification` method `chirality/nativeChildren/observationEnded`, params `{threadId,turnId,agentThreadIds,reason:"parentTurnEnded",message}`. Their later activity is not captured by that retired observer. This explicitly states missing observation and does not claim completion or interrupt the child. A longer-lived session-tree observer is outside this bounded implementation.
- Unknown steering outcome can be reconciled with the same request/operationId; this queries evidence and never resends. A raw native echo is durable evidence even if no further reconciliation request arrives. UI may safely refresh the same operation after transport uncertainty. Absence of an echo is never interpreted as non-delivery.
- Parent's selected inactive-chat request popover consumes existing per-session request ownership; no detached primary-turn ownership redesign was introduced.
- Independent review must cover these actual source changes; this child is their author, not the reviewer. No acceptance pointer moved.
