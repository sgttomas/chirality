# Spike design: stock Codex under an App-owned Runtime service (D-GOV-43, topology A2)

Author: implementing session (Fable 5.1), 2026-09-12. Basis: main `e83cb1f47`
plus the application tranche in this branch. Governing texts: the D-GOV-43
ruling, the A2 supplement, `HANDOFF.md` sections 2-4 and `PERSPECTIVE.md` in
this directory. This document is the shared brief for the four bounded
implementation assignments (W1-W4, section 12). Where it fixes a name, a
shape or a rule, the assignments implement it as written; routine choices
inside an assignment are the assignee's and are recorded in its return.

Protocol facts below were established against the pinned stock binary
(`@openai/codex@0.154.0`, `codex-cli 0.154.0`): the generated JSON schema and
TypeScript bindings (`codex app-server generate-json-schema|generate-ts`) and
a scratch-home probe (`initialize`, `collaborationMode/list`, `thread/start`,
`thread/settings/update`, `turn/start`, `account/read`, `permissionProfile/list`,
`model/list`). No user Codex home, credential or trial file was read.

## 1. Composition

One App-owned service process ("the Runtime service") per running App:

```
Electron main ──spawn/stdio/signals──▶ chirality-runtime-service (Node, standalone-bin)
      │  Unix socket + per-launch token                 │ stdio JSON-RPC, CODEX_HOME=<effective home>
      ▼                                                  ▼
 Next routes / renderer                         codex app-server (stock, pinned 0.154.0)
```

Inside the service (all in one process, `packages/daemon/src/app-owned-composition.ts`):
`ProjectRegistry`, `SessionStore`, `EngineRegistry`, `TurnCoordinator`,
`RuntimeService`, `AuthRegistry`, `NativePlanRegistry`, `RuntimeMethodService`,
`DelegatedRuntime`, the rewritten `CodexSupervisor` over one long-lived
`CodexAppServerClient`, the rewritten `CodexLogin`, the effective-home
manager, the new `TurnRegistry` (section 5) and `RuntimeDaemon`.

Exactly one `codex app-server` child per service, shared by every project
and thread. Threads carry their own `cwd`; a project is a thread's working
root, nothing more. The service restarts the child if it exits, with the
same backoff policy Electron applies to the service (section 9); an exit
during a turn ends that turn as `failed` with the reason, never as completed.

Retired from the product path (deleted, not shimmed): `hosted-private-composition.ts`,
`hosted-private-entry.ts`, `hosted-boot.ts`, `hosted-standalone.ts`,
`hosted-packaged-release*.ts`, `hosted-release-provisioner.ts`,
`hosted-identity-binding.ts`, `host-account-*.ts`, `supplier-authority-*.ts`,
`runtime-conformance-v2-admission.ts`, `codex-admitted-launcher.ts`,
`codex-authenticated-transport.ts`, `codex-containment.ts`, `codex-worker.ts`,
`codex-manager.ts` (if only the retired path uses it), `codex-transport-lifecycle.ts`,
`account-free-login-observation.ts`, `supervisor-server.ts` and the
`supervisor` role of `standalone-bin`; in `packages/core`:
`runtime-conformance*.ts`, `exact-supply.ts`, `hosted-consent.ts`,
`runtime-admission-lock.ts`, `residency-coordinator.ts` (RuntimeService keeps
accepting a residency port only if removing it is disproportionate; the
pi/oMLX engines are not composed on the App path); the `native-admission`
package and every import of it. Tests of retired modules go with them.
Historical evidence stays in git history; nothing is rebuilt under a new
name.

Kept and repaired: `RuntimeService`, `SessionStore`, `TurnCoordinator`,
`DelegatedRuntime`, `delegated-engine-adapter.ts`, `ProcessSupervisor` and
`DescendantTracker` (still used by tests and by the standalone
`chirality-standalone/v1` controlled-worker mode), `worker-retirement.ts`,
`NativePlanRegistry`, `RuntimeMethodService`, `MethodCatalog`, the socket
API, `RuntimeClient`, the App's harness port and routes.

Service configuration (`chirality-app-owned/v1`, JSON file passed as
`chirality-runtime-service daemon --config <path>`; the file is private to
the App, mode 0600, under `userData`):

```json
{
  "schema": "chirality-app-owned/v1",
  "socketPath": "/abs/path/runtime.sock",
  "runtimeDirectory": "/abs/userData/runtime",
  "instructionRoot": "/abs/path/to/instruction-root",
  "clientTokenFile": "/abs/userData/runtime/client-token",
  "codex": {
    "executablePath": "/abs/path/to/codex",
    "userCodexHome": "/Users/x/.codex",
    "effectiveHome": "/abs/userData/runtime/codex-home",
    "expectedVersion": "0.154.0"
  }
}
```

On start the service: creates the runtime directory (0700); prepares the
effective home (section 3); spawns the app-server and completes `initialize`
(and checks `codex --version` equals `expectedVersion`, refusing to start
otherwise); issues a fresh random 32-byte client token for client id
`app-host` with the scopes the hosted-bootstrap client had, revoking earlier
`app-host` tokens, and writes it to `clientTokenFile` (0600); starts the
daemon on `socketPath`; prints exactly one stdout line
`{"ready":true,"role":"daemon","socketPath":"...","clientTokenFile":"..."}`.
`SIGTERM` stops the daemon, interrupts live turns (recorded as
`turn.interrupted` with reason `service-shutdown`), terminates the
app-server child (SIGTERM, then SIGKILL after 2 s) and exits 0. No
LaunchAgent, no second socket, no TCP.

## 2. Stock Codex client (`packages/daemon/src/codex-app-server-client.ts`)

Newline-delimited JSON-RPC 2.0 over the child's stdio; the child is spawned
as `<executablePath> -c cli_auth_credentials_store="file" app-server` with
`CODEX_HOME=<effectiveHome>` and `HOME` unchanged (the user's real home, so
Codex finds `~/.codex` only through the overlay's links). Facts fixed by the
pinned protocol:

- `initialize {clientInfo:{name:"chirality", title:"Chirality", version}, capabilities:{experimentalApi:true}}`
  → `{userAgent, codexHome, platformFamily, platformOs}`. Do not declare
  `requestAttestation`; do not opt out of notifications.
- `thread/start {cwd, developerInstructions, approvalPolicy, sandbox, model?, ephemeral:false, serviceName:"chirality"}`
  → `{thread:{id,...}, model, modelProvider, approvalPolicy, sandbox, reasoningEffort, instructionSources}`.
  `sandbox` is the string `read-only | workspace-write | danger-full-access`;
  `approvalPolicy` is `untrusted | on-request | never` (granular exists,
  unused). `baseInstructions` is never sent.
- `thread/resume {threadId, cwd, developerInstructions, approvalPolicy, sandbox, model?}`.
- Plan Mode: `thread/settings/update {threadId, collaborationMode:{mode:"plan"|"default", settings:{model, reasoning_effort, developer_instructions:null}}}`
  (returns `{}`; the server then emits `thread/settings/updated`).
  `collaborationMode/list` returns the presets (`Plan` → medium effort by
  default). Plan Mode is therefore a thread setting set before `turn/start`,
  not a `turn/start` parameter; the supervisor sets it whenever the
  requested `interactionMode` differs from the thread's last applied mode.
- `turn/start {threadId, input:[{type:"text",text}|{type:"localImage",path}], model?, effort?, approvalPolicy?, sandboxPolicy?, cwd?}`
  → `{turn:{id,status:"inProgress",...}}`. `turn/interrupt {threadId, turnId}`.
  `turn/steer {threadId, expectedTurnId, input}` exists (unused in the spike).
- Server requests the client must answer (all eight in the pinned export,
  plus the two legacy forms that the same binary still emits on older
  paths): `item/commandExecution/requestApproval` → `{decision: "accept"|"acceptForSession"|"decline"|"cancel"}`;
  `item/fileChange/requestApproval` → same decision set;
  `item/permissions/requestApproval` → `{permissions: <granted profile>, scope?}`
  (decline = empty grant `{}`); `item/tool/requestUserInput` →
  `{answers:{[questionId]:{answers:string[]}}}`; `mcpServer/elicitation/request`
  → `{action:"accept"|"decline"|"cancel", content?}`; `item/tool/call`
  (dynamic tools; we register none) → `{success:false, contentItems:[{type:"inputText", text:"Chirality registers no dynamic tools"}]}`;
  `account/chatgptAuthTokens/refresh` and `attestation/generate` → JSON-RPC
  error `-32601` "unsupported request"; legacy `execCommandApproval` /
  `applyPatchApproval` → `{decision:"approved"|"denied"}`. Any other method →
  JSON-RPC error `-32601`. Every server request, answered or refused, is
  visible to the user as a `codex.request.resolved` event (section 6); an
  unanswered request never implies approval.
- Notifications: every method passes through to the supervisor unchanged
  (`{method, params}`); there is no whitelist and no quarantine. The client
  keeps a per-thread "active turn" from `turn/started` / `turn/completed`
  and routes notifications to the turn's drain queue by `threadId`.
- Account: `account/read {refreshToken:false}` → `{account: null | {type:"chatgpt", email?, planType} | ..., requiresOpenaiAuth}`;
  `account/login/start {type:"chatgpt"}` → `{type:"chatgpt", loginId, authUrl}`;
  `account/login/cancel {loginId}`; `account/logout {}`; completion arrives as
  `account/login/completed {loginId, success, error}`. `model/list {}` works
  signed-out (catalog) and signed-in; hide entries with `hidden:true`.
- Child exit: reject every in-flight request with `ENGINE_UNAVAILABLE`, fail
  active turns, and let the composition restart the child.

The client never logs request or notification payloads that can carry
account data (`account/*`, login URLs); it logs method names and ids only.

## 3. Effective Codex home (`packages/daemon/src/codex-effective-home.ts`)

Directory `<runtimeDirectory>/codex-home` (0700). On every service start:
for each entry of the user's `~/.codex` (or `userCodexHome`), create or
refresh a symlink of the same name in the effective home, except
`auth.json`, `models_cache.json` and any entry whose name starts with
`auth` or ends with `.lock`; remove symlinks whose targets no longer exist;
never create, copy, move or write anything inside the user's home; never
open `auth.json`. The effective home therefore shares `config.toml`,
`AGENTS.md`, `skills/`, `plugins/`, `sessions/`, `archived_sessions/`,
`memories`, MCP definitions and caches by reference, while `auth.json` and
the models cache are private to Chirality and are created by Codex itself
after a Chirality sign-in. A missing user home is not an error (empty
overlay). The T3 Code `CodexHomeLayout.ts` "authOverlay" (MIT) is the
reference layout; no code is copied from it.

Consequences: S-8 holds by construction (another Codex client keeps its own
`auth.json`); Chirality threads land in the user's shared `sessions/`
store, which is what the revised SPEC §14.2 records (shared Codex store plus
App index).

## 4. Threads, roles, policy, delegation

- The Chirality session record (`RuntimeSessionRecord`) is the App index of a
  Codex thread: `engineSessionId` holds the Codex thread id after the first
  turn. The sidebar lists sessions as today. No second index store.
- First turn of a session: `thread/start` with `cwd` = project root,
  `developerInstructions` = the role instruction text for the session's role
  (from the instruction root, `MethodCatalog.loadRoles`) followed by the
  selected workflow/skill context that `RuntimeMethodService.resolveForTurn`
  already produces (`instructionContext.supplied`, rendered as text, not the
  old `<chirality-runtime-context>` prompt wrapper), the session's
  `PolicySelection` (below) and the requested model. Later turns:
  `thread/resume` when the app-server instance does not know the thread
  (after service or child restart), else nothing; if the method selection
  revision changed since the last turn, prepend one additive text input item
  `Chirality context update:\n<rendered context>` to that turn's input. Codex
  discovers the project's `AGENTS.md` itself. Base instructions are never
  replaced.
- `PolicySelection` (TYPES §12) is expressed through the existing App
  `permissionMode` until a dedicated selector exists:
  `readOnly` → `{approvalPolicy:"on-request", sandbox:"read-only"}`;
  `ask` → `{"on-request", "workspace-write"}`; `workspaceWrite` →
  `{"never", "workspace-write"}`; `bypass` → `{"never", "danger-full-access"}`.
  The mapping lives in `packages/contracts` (`policySelectionFromPermissionMode`)
  so daemon and App agree. It is applied at `thread/start`/`thread/resume` and
  re-sent on `turn/start` when the session's mode changed.
- Model and reasoning effort are per turn: `SessionTurnRequest.model` and
  `.reasoningEffort` override the session's `engineSelection`/`reasoningEffort`
  for that turn and are passed on `turn/start` (`model`, `effort`). The
  daemon records the last used values back on the session record.
- Interaction mode `native-plan` maps to the `plan` collaboration mode
  (section 2). Plan items (`item/started|completed` with `type:"plan"`,
  `item/plan/delta`, `turn/plan/updated`) feed `NativePlanRegistry` as today
  through the supervisor's native-plan port; plan clarifications are
  `item/tool/requestUserInput` requests and are answered through the request
  API (section 7), which the existing native-plan clarification routes call.
- Delegation (S-5): Codex's own `[agents]` configuration in the shared
  `config.toml` and its `spawn_agent` tooling; sub-agent activity arrives as
  `subAgentActivity` / `collabAgentToolCall` items and passes through as
  `subagent.*` events (section 6). Evidence that a child received role
  instructions comes from the child thread's `thread/started` payload and
  `instructionSources`, recorded in the events. No Chirality-side spawner.

## 5. Turn ownership and transport (the disconnection rule)

The Runtime service owns every active turn. A browser or renderer
connection only observes it. Explicit Stop is the interrupt endpoint.
Reopening a conversation recovers state, missed activity and outstanding
decisions from the session store and the live turn buffer without
re-sending the prompt or executing twice.

`packages/daemon/src/turn-registry.ts` (new):

- `start(projectId, sessionId, request)`: rejects with
  `SESSION_TURN_IN_PROGRESS` (409) if a turn is active for the session; else
  assigns `turnId` (the request's or a new one), runs
  `service.runSessionTurn(...)` in the background, and appends every yielded
  `UIEvent` to the turn's buffer as `{seq, event}` (seq starts at 1). The
  buffer is retained for 10 minutes after the terminal event.
- `subscribe(projectId, sessionId, afterSeq)`: async iterable of buffered
  frames with `seq > afterSeq`, then live frames until the terminal frame.
  Closing a subscription never affects the turn.
- `state(projectId, sessionId)` → `{active:boolean, turnId?, lastSeq, startedAt?}`.
- `interrupt` delegates to `service.interruptSession`.

Routes (`runtime-daemon.ts`):

- `POST /v1/projects/:p/sessions/:s/turn` starts the turn and streams its
  subscription as SSE. On client close: unsubscribe only.
- `GET  /v1/projects/:p/sessions/:s/turn/stream?after=<seq>`: attaches to the
  active or retained turn; 404 `TURN_NOT_ACTIVE` when neither exists.
- `GET  /v1/projects/:p/sessions/:s/turn/state`.
- `POST /v1/projects/:p/sessions/:s/interrupt` unchanged.
- `POST /v1/projects/:p/sessions/:s/permission` unchanged shape
  (`PermissionDecisionRequest {requestId, decision}` where `requestId` is the
  tool-use id, i.e. the Codex item id carried by `tool.permission`; the App
  route keeps its `{toolUseId, verdict}` form), now answering the Codex
  approval that carries that item id (section 7).
- `GET  /v1/projects/:p/sessions/:s/requests` and
  `POST /v1/projects/:p/sessions/:s/requests/:requestId/answer` (section 7).

SSE writer: frames are `id: <seq>\nevent: <type>\ndata: <json>\n\n`; a
comment line `: keepalive\n\n` every 15 s while the stream is open; the
writer never calls interrupt. `RuntimeClient` stream requests disable the
idle timeout (`timeoutMs: 0` on the SSE path; JSON requests keep 30 s) and
expose `attachSessionTurn(projectId, sessionId, {after})`,
`sessionTurnState`, `listSessionRequests`, `answerSessionRequest`.
`parseSse` accepts any `event` name (the closed `uiEventTypes` set goes) and
surfaces `id` as `seq`.

App side: `POST /api/harness/turn` streams the daemon subscription; its
`cancel()` unsubscribes only. New proxies
`GET /api/harness/session/[id]/turn/stream`, `GET .../turn/state`,
`GET .../requests`, `POST .../requests/[requestId]/answer`. On opening a
session the chat panel asks `turn/state`; if active it replays persisted
events, then attaches with `after=0` and de-duplicates by `eventId`
(`message.delta` events render as streamed text). A stream that ends without
a terminal event re-attaches with backoff; the panel shows "Reconnecting",
never Idle. Stop calls the interrupt route. Live rendering of
`turn.interrupted` / `turn.failed` is immediate (R17-F1).

## 6. Event representation

Upstream method names, ids and payloads are preserved; known items get
normalized views. New `HarnessEvent` types (contracts `event-schema.ts`):
`codex.notification`, `codex.request`, `codex.request.resolved`. New
supervisor progress events (contracts `delegated.ts`):

```ts
export type DelegatedTurnProgressEvent =
  | { type: "started"; providerThreadId: string; providerTurnId: string }
  | { type: "text"; providerThreadId: string; providerTurnId: string; text: string }
  | { type: "notification"; providerThreadId: string; providerTurnId?: string; method: string; params: unknown; occurredAt: string }
  | { type: "request"; providerThreadId: string; providerTurnId?: string; requestId: string; method: string; params: unknown; occurredAt: string }
  | { type: "request-resolved"; providerThreadId: string; providerTurnId?: string; requestId: string; method: string;
      outcome: "answered" | "cancelled" | "unsupported" | "failed"; decision?: unknown; decidedBy?: "user" | "policy" | "runtime"; occurredAt: string };
```

`delegated-engine-adapter.ts` maps progress to `UIEvent`s (all `harness:event`
payloads carry `providerThreadId`, `providerTurnId`, `method` and the raw
`params` under `codex`):

| Progress | UIEvent / HarnessEvent |
|---|---|
| `text` | `chat:delta` (persisted as `message.delta`) |
| `notification item/started`, item type commandExecution, fileChange, mcpToolCall, dynamicToolCall, webSearch, imageView, imageGeneration | `tool.started {toolUseId:item.id, toolName:item.type, summary}` |
| `notification item/completed` for those types | `tool.completed` (status completed) or `tool.failed` (failed, declined) |
| `notification item/commandExecution/outputDelta`, `item/fileChange/outputDelta`, `item/mcpToolCall/progress` | `tool.progress {toolUseId, delta}` |
| items `subAgentActivity`, `collabAgentToolCall` (started / completed) | `subagent.started` / `subagent.progress` / `subagent.completed` / `subagent.failed` `{taskId:item.id, agentThreadId, ...}` |
| items `plan`, `reasoning`, `agentMessage` (completed), `contextCompaction`, `enteredReviewMode`, `exitedReviewMode` | `codex.notification` (plan items also reach `NativePlanRegistry`) |
| `item/agentMessage/delta` | handled as `text` |
| `item/reasoning/*Delta`, `item/plan/delta`, `item/reasoning/summaryPartAdded` | dropped (not persisted); the completed item carries the text |
| `turn/started` | `turn.started` (existing) |
| `turn/completed` | terminal handling as today (`turn.completed` / `turn.interrupted` / `turn.failed` from `turn.status`, with `turn.error`) |
| any other notification (`turn/plan/updated`, `thread/tokenUsage/updated`, `account/rateLimits/updated`, `error`, `warning`, `thread/settings/updated`, `model/rerouted`, ...) | `codex.notification {method, params}` |
| `request` approval methods (commandExecution, fileChange, permissions, legacy exec/patch) | `tool.permission {behavior:"ask", toolUseId: params.itemId ?? params.callId, toolName, reason, requestId, method, request: params}` |
| `request` userInput, elicitation, dynamic tool call, others | `codex.request {requestId, method, kind, request: params}` |
| `request-resolved` | `codex.request.resolved {requestId, method, outcome, decision, decidedBy}`; for approvals additionally `tool.permission {behavior:"allow"|"deny", toolUseId, requestId, decidedBy}` |

The App keeps `deriveToolActivity`, `derivePermissionRequests`,
`deriveSubagentActivity` working on these fields and adds a generic
notification card (method plus collapsed JSON) for `codex.notification` in
the Activity panel, a "Thinking" line from completed reasoning items, and a
request card for `codex.request`. `validateHarnessEventV2` accepts the new
types.

## 7. Server requests and decisions

`CodexSupervisor` keeps, per turn, the pending server requests
(`{requestId, method, params, itemId?, receivedAt}`) and exposes
`SupervisorRequestPort`:

```ts
export interface PendingServerRequest { requestId: string; method: string; params: unknown; itemId?: string; receivedAt: string }
export type ServerRequestAnswer =
  | { kind: "approval"; verdict: "allow" | "deny" | "allowForSession" }
  | { kind: "userInput"; answers: Record<string, { answers: string[] }> }
  | { kind: "elicitation"; action: "accept" | "decline" | "cancel"; content?: unknown };
export interface SupervisorRequestPort {
  pendingRequests(workerId: string, generation: string): Promise<readonly PendingServerRequest[]>;
  answerRequest(workerId: string, generation: string, requestId: string, answer: ServerRequestAnswer): Promise<{ sent: true }>;
}
```

`DelegatedRuntime` exposes `pendingRequests(projectId, sessionId)`,
`answerRequest(projectId, sessionId, requestId, answer)` and
`answerApprovalByToolUseId(projectId, sessionId, toolUseId, verdict)`; a wrong
`kind` for the method is `INVALID_REQUEST`. `RuntimeService.decidePermission`
routes to `answerApprovalByToolUseId` through the permission broker port.
When a turn ends (completed, failed, interrupted) the supervisor answers
every still-pending request with `cancel`/`decline` and emits
`request-resolved` with outcome `cancelled`, `decidedBy: "runtime"`. Pending
requests survive renderer disconnects: reopening shows them from the
persisted `tool.permission`/`codex.request` events with no resolution, while
`turn/state` reports the turn active. Denied approvals (S-7) reach Codex as
`decline`, the item completes as `declined`, and the turn continues or ends
as Codex decides; the App shows the declined item.

## 8. Interruption versus retirement (defect repair and regression)

Rules: interruption (`interrupt`) and final retirement (`retire`) are distinct
operations on the same exact generation. `interrupt` never retires. A
supervisor without a native interrupt does not expose `interrupt`, so
`DelegatedRuntime` takes the retire branch deliberately. `retire` on an exact
generation is idempotent: the first call performs the retirement and every
later call for the same `(workerId, generation)` joins the same memoized
result; a foreign or stale generation is still rejected with
`unknown or stale worker generation`. `DelegatedRuntime.retireWorker` keeps
its per-key memo and `executeTurn` never issues a second, un-joined retire.

For the stock composition `CodexSupervisor.interrupt` sends `turn/interrupt`
and resolves when the turn's `turn/completed` (status `interrupted`) arrives;
`retire` releases the turn's bookkeeping (drain queues, pending requests
answered as cancelled) and is memoized per generation. The supervisor never
kills the app-server for an interrupt.

Regression (`tests/delegated-runtime.test.ts`, deterministic, no added
sleeps): a fixture supervisor whose worker completion is released by an
explicit promise. Order A: interrupt requested → worker completes → final
cleanup; order B: worker completes → interrupt requested → cleanup. Both
orders must yield one `interrupted`/`completed` terminal respectively, one
retirement record, no rejected inner request, `inventory()` empty, and a
second `retire` of the same generation resolving to the same result while a
stale generation still rejects. The two intermittently red tests keep their
assertions.

## 9. Electron: child lifecycle and packaging

`electron/runtime-service-host.ts` (new) replaces `runtime-host.ts`,
`runtime-autostart.ts`, `daemon-activate-policy.ts`, `desktop-daemon-posture.ts`,
`host-account-*.ts`, `protected-runtime-cli.ts` (if unused), the
`runtime.daemon` install/start/stop/uninstall IPC operations and the hosted
variants in `main.ts`. The service is spawned with `process.execPath`,
`ELECTRON_RUN_AS_NODE=1`, argv `[serviceEntry, "daemon", "--config", configPath]`,
`stdio: ["ignore","pipe","pipe"]`, `detached:false`. Service entry: dev →
`../../chirality-runtime/packages/daemon/dist/standalone-bin.js`; packaged →
`resources/runtime-service/standalone-bin.mjs`, bundled by
`scripts/build-electron.mjs` exactly as the runtime CLI is today. Codex
executable: dev → resolved from the installed `@openai/codex` platform
package (`vendor/<triple>/bin/codex`); packaged → `resources/codex/bin/codex`
staged from that package (the whole `vendor/<triple>` tree, so
`codex-path/rg` and `codex-resources` travel with it). Both binaries are
signed with the App's identity and the hardened runtime; the supplier
digest, the native addon and `chirality-supplier` staging go.

Startup: write the config (0600) and spawn; wait up to 30 s for the ready
line; on success set `CHIRALITY_RUNTIME_SOCKET_PATH`,
`CHIRALITY_RUNTIME_TOKEN_FILE` (and `CHIRALITY_RUNTIME_DIRECTORY`) for the
in-process Next server and connect the main-process `RuntimeClient` with the
token file. Restart on unexpected exit with backoff 1, 2, 4, 8, 16, 30 s;
after 5 failures in 3 minutes stop retrying and surface the state through
the existing connectivity IPC (renderer shows "Runtime stopped" with a
retry action). Never restart during `teardown()`. `teardown()` stops the
child (SIGTERM, SIGKILL after 10 s, beyond the service's own close budget of
interrupt grace 3 s, daemon stop 2.5 s and app-server kill grace 2 s) after
the renderer server; quit waits for
it. Window close and hide are distinct from quit and stop nothing. Service
stderr is written to the desktop log with account e-mail redaction
(`grep -v '@'` equivalence) applied at the writer.

`package.json`: add `"@openai/codex": "0.154.0"` (exact) to dependencies;
remove `@chirality/native-admission`; `extraResources` become the codex
platform tree, the runtime service bundle, the runtime CLI bundle and the
instruction root. `pack-electron-with-supply.mjs` becomes a plain pack
(rename permitted); `sign-electron-runtime-v2.mjs` signs the two Codex
binaries and the App; `verify-electron-dist.mjs` and
`desktop:verify-dependencies` check the new layout; a new
`desktop:verify-codex-pin` runs the packaged `codex --version`, compares it
to the lockfile-resolved version, and compares the binary's sha256 to the
installed package's. The short procedure (build, sign, notarize, verify
signature and pin, distinct packaged checks) is written into
`PACKAGING_PROCEDURE.md` in this directory if the App-records assignment has
not already done so, and reconciled with it if it has.

## 10. App renderer

Chat panel and providers: attach/reconnect flow (section 5); Stop →
interrupt; immediate rendering of terminal events; model and effort
selectable between turns and sent per turn; permission mode selector kept as
the `PolicySelection` control (section 4) with the four modes explained in
Codex terms; account row without the consent step; `PermissionDecisionCards`
fed by the mapped `tool.permission` events with `active` derived from
`turn/state`; a `RequestCard` for `codex.request` (questions with options and
free text, elicitation accept/decline) answering through the request route,
which the native-plan clarification card also uses; Activity panel with tool
rows, sub-agent rows, a "Thinking" line and the generic notification cards;
event log inspectable. Reasonable minimal presentation is the target; the
loop working end to end comes first.

Retired in the renderer: the provider-network consent step and its client
function (the route stays as a no-op that returns status), the
`runtime.daemon` control panel (install/uninstall), model/effort freeze, any
admission/identity text.

## 11. Sign-in and sign-out (S-8)

`CodexLogin` over the client: `startLogin` → `account/login/start` →
`{loginId, authUrl}` returned to the App, which opens the URL in the system
browser (existing status route and `shell.openExternal` flow); the owner
completes OAuth; `account/login/completed` updates the state; `cancelLogin` →
`account/login/cancel`; `signOut` → `account/logout`. `HostedBootstrapStatus`
keeps its wire shape: `ceremony` is `ready-to-start` when signed out (the
`consent-required` value is never produced), `pending` during login,
`signed-in` afterwards, `failed`/`cancelled` as before; `admission` is
`ready` exactly when signed in, `unavailable` otherwise (`establishing` only
while signed in but the catalog read failed; the next status read retries); `models`/`selection` come from `model/list` (non-hidden;
default the entry with `isDefault`, else the first). The status is App-wide;
the per-project route reports the same account for every project. No
credential is read, copied or displayed; the account e-mail from
`account/read` is shown in the account row only and never logged.

## 12. Assignments, write scopes, returns

Common rules for W1-W4: Fable 5.1 at medium; read this document, the
governing texts it names, and only the source you need; never read the
owner's live `~/.codex/auth.json`, keychain, session or event files, the R17
userData or the preserved trial worktree; never enter credentials; no `git`
write operations (the lead commits); no `git stash`; scratch files only under
the session scratchpad; run the relevant test suites before returning
(`npm test -- --maxWorkers=1` in `projects/chirality-runtime` for W1/W2; the
frontend `npm test` and `npm run typecheck`/`build:electron` for W3/W4) and
report real results; write a return record at
`.../APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/<W>_RETURN.md` listing files
changed, decisions taken, tests run with pass/fail counts, and anything left
for integration. Write scopes are disjoint; anything needed outside a scope
is reported, not edited. The lead pre-authors the contract seam (contracts
package) before dispatch, so W1-W4 code against it.

- **W1 Runtime core (Codex composition).** Scope: `packages/daemon/src/codex-*.ts`
  (new client, effective home, rewritten supervisor and login), new
  `app-owned-composition.ts`, `standalone.ts`/`standalone-bin.ts` (add the
  `chirality-app-owned/v1` schema, drop the hosted branch and the supervisor
  role), `hosted-bootstrap.ts` (reduce to the status/login controller over the
  new login, or replace and re-export the same names), the retirements listed
  in section 1 within `packages/daemon/src` and `packages/core/src`,
  `packages/core/src/delegated-runtime.ts`, `delegated-engine-adapter.ts`,
  `process-supervisor.ts`, the `native-admission` package removal, and the
  tests of everything above (`tests/*` matching those modules, including the
  section 8 regression). Sections 1, 2, 3, 4, 6 (adapter side), 7 (supervisor
  and DelegatedRuntime side), 8.
- **W2 Daemon transport and service glue.** Scope: `packages/daemon/src/runtime-daemon.ts`,
  new `turn-registry.ts`, `packages/core/src/runtime-service.ts`,
  `turn-coordinator.ts`, `session-store.ts` (last-used model/effort, session
  status on service shutdown), `packages/client/src/**`, `packages/contracts/src/**`
  beyond the pre-authored seam (validators, route constants, response types),
  and their tests (`daemon.test.ts`, `runtime-v3-api.test.ts`, client tests,
  `v2-contracts.test.ts`, new `turn-registry.test.ts`). Sections 5, 6
  (validator), 7 (routes and broker), 11 (routes). W2 tests the registry with
  a stub engine; it does not touch W1's modules.
- **W3 Electron lifecycle and packaging.** Scope: `frontend/electron/**`,
  `frontend/scripts/**`, `frontend/package.json` and lockfile, `frontend/build/**`,
  `frontend/src/__tests__/electron/**` and `frontend/src/__tests__/scripts/**`,
  `frontend/src/types/chirality-window.d.ts` for retired IPC surfaces,
  `frontend/scripts/controlled-ci-runtime.ts`. Section 9.
- **W4 App renderer and routes.** Scope: `frontend/src/**` except the W3
  directories above, including `src/lib/runtime-client/**`, `src/app/api/**`,
  `src/components/**`, `src/lib/harness/hosted-bootstrap-client.ts`,
  `src/lib/shell/**`, and their tests. Sections 5 (App side), 6 (views), 7
  (cards), 10, 11 (renderer).

Seam already authored by the lead before dispatch (do not re-author; extend
only inside your scope): contracts `delegated.ts` (`DelegatedTurnProgressEvent`,
`PendingServerRequest`, `ServerRequestAnswer`, `SupervisorRequestPort`,
`PolicySelection`, `policySelectionFromPermissionMode`), `harness/event-schema.ts`
(three `codex.*` types), `protocol.ts` (`sessionTurnStream`, `sessionTurnState`,
`sessionRequests`, `sessionRequestAnswer` routes; `SessionTurnState`,
`SessionRequestsResponse`, `AnswerSessionRequestRequest/Response`),
`session.ts` (`SessionTurnRequest.model`, `.reasoningEffort`). Contracts
build clean (`tsc -b`).

Integration (lead): build the runtime workspace, run both suites, run the
spike from source with a distinct `userData`, and perform S-1..S-8 and the
disconnect check with the owner's sign-in.

## 13. Acceptance (from HANDOFF section 4)

S-1 native Plan Mode with revision; S-2 execution with real reads and tool
use beyond 30 s of silence; S-3 save workflow through conversation; S-4 reuse
and iterate; S-5 delegated task whose child demonstrably receives role
instructions; S-6 quit and relaunch continuation; S-7 interruption and
approval handling including a denied approval; S-8 sign-in/out scoped to
Chirality with another Codex client unchanged; plus the renderer disconnect
during tool work with recovery of missed activity and outstanding decisions
and no duplicate execution. Evidence goes to `spike/EVIDENCE.md` with UTC
times and filtered logs (`grep -v '@'`).
