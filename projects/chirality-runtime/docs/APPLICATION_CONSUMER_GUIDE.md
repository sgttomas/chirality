# Embedding Runtime in another application

This guide maps the existing implementation for a second application consumer.
Source basis: `42bd234f671508ba9ab157e1981334ba8610279f`. It is preparation,
not evidence that a Tauri host, local model, or SWBPIPE tool session has run.
The executable interfaces remain the exported Runtime types and routes linked
below. [Application tools](APPLICATION_TOOLS.md) defines their tool lifecycle.

For SWBPIPE, the first selected path remains a development Codex session using
the Piping JSON CLI and private bridge to its live controller. That path does
not require this embedded Runtime setup. Piping owns that controller, bridge,
CLI, review UI, and domain semantics. Runtime owns conversation and provider
lifecycle when embedded integration follows. The Chirality App is one consumer;
another application need not install or launch it.

## What can be reused

| Existing source | Reuse and limit |
|---|---|
| [Standalone entry](../packages/daemon/src/standalone-bin.ts) and [composition](../packages/daemon/src/app-owned-composition.ts) | One application-owned service and stock Codex child. Requires a Node host; there is no Tauri sidecar distribution yet. |
| [RuntimeClient](../packages/client/src/client.ts) and [route contract](../packages/contracts/src/protocol.ts) | Typed Node client; HTTP/JSON and SSE over a Unix socket. A Rust host must implement the same wire or host the existing client in its Node sidecar. The browser renderer cannot import this Node client directly. |
| [App host lifecycle](../../chirality-app-dev/frontend/electron/runtime-service-host.ts) | Config writing, ready-line parsing, bounded restart and deliberate shutdown. Its launcher port is separable, but the [production launcher](../../chirality-app-dev/frontend/electron/runtime-service-launcher.ts) uses Electron's `utilityProcess`. |
| [App service bundling](../../chirality-app-dev/frontend/scripts/build-electron.mjs) | Reference for bundling the standalone service. Its Node 24 target and Electron packaging are not a standalone Tauri deliverable. |
| [Application-tool composition tests](../tests/application-tools-composition.test.ts) | Real socket/client/store/registry/supervisor with a controlled Codex transport. Includes host authorization, detach, Stop, late results, and restart/rebind. |

Keep the first CLI's Piping operation handlers independent of Runtime DTOs so
later tool dispatch can call the same handlers. Do not duplicate model state,
validation, review, or application logic in a second adapter.

## Host configuration and startup

Use a separate Runtime instance and private data directory for each owning
application. The client ID `app-host` is local to that instance's token registry;
it is not a globally shared account or a broker for multiple applications.
Do not point a new consumer at the running Chirality App's socket or token file.

The [configuration validator](../packages/daemon/src/app-owned-composition.ts)
accepts `chirality-app-owned/v1` with these exact fields. The following is an
illustrative fixture layout, not a request to create or use these locations:

```json
{
  "schema": "chirality-app-owned/v1",
  "socketPath": "/tmp/runtime-consumer-fixture/control.sock",
  "runtimeDirectory": "/tmp/runtime-consumer-fixture/runtime",
  "instructionRoot": "/tmp/runtime-consumer-fixture/instructions",
  "productInstructionsPath": "/tmp/runtime-consumer-fixture/product/AGENTS.md",
  "clientTokenFile": "/tmp/runtime-consumer-fixture/runtime/app-host.token",
  "codex": {
    "executablePath": "/tmp/runtime-consumer-fixture/bin/codex",
    "userCodexHome": "/tmp/runtime-consumer-fixture/user-codex",
    "effectiveHome": "/tmp/runtime-consumer-fixture/runtime/codex-home",
    "expectedVersion": "0.154.0"
  }
}
```

Choose real application-owned paths at integration time, write the configuration
privately, and preserve these implementation constraints:

- Paths must be normalized and absolute. The socket path limit is 103 UTF-8
  bytes, including the full parent path. Use an owned short location if the
  application's data-directory path is too long.
- `instructionRoot` supplies the bundled registry, roles and method resources.
  `productInstructionsPath` is optional, must be outside both Codex homes, and
  supplies the product's shared guidance. It does not replace Codex's base
  instructions. A v2 project's working directory must be disjoint from its
  Runtime instruction root.
- Pin the stock Codex executable deliberately. `expectedVersion` is checked
  before startup; the example matches the current App's 0.154.0 basis, not an
  instruction to follow whatever binary happens to be on `PATH`.
- The [effective-home implementation](../packages/daemon/src/codex-effective-home.ts)
  shares the user's configuration/resources by reference, excluding auth-prefixed
  entries, `models_cache.json` and lock files. Regular overlay entries are retained.
  A separate overlay alone does not prove every credential backend or shared
  configuration write is isolated. Native sign-in/sign-out isolation remains a
  test for the eventual packaged consumer. Never copy credentials between apps.

After building the Runtime workspace, the source entry is:

```sh
node packages/daemon/dist/standalone-bin.js daemon --config /absolute/private-config.json
```

The owning host supplies the Node runtime and packaged resources; the end user
should not start this command manually. Await the child's single ready line:

```json
{"ready":true,"role":"daemon","socketPath":"/absolute/control.sock","clientTokenFile":"/absolute/app-host.token"}
```

Check it against the paths launched, then connect and query health. Readiness
means the socket and token are ready, not that an account is signed in or a
tool handler is bound. Keep token/config paths and credential operations in the
trusted host, outside renderer messages and logs. On unexpected exit, apply
bounded restart and expose interruption honestly. On quit, stop the owned child
deliberately. Closing an observation stream is not Stop.

## Project, account, session, and tools

Follow this order using the trusted host and existing client methods:

1. Construct the host `RuntimeClient` with the launched socket and host token
   file. Register an existing manifest through `registerHostedBootstrapProject`,
   or deliberately initialize a selected working folder through
   `initializeHostedBootstrapProject`. Initialization can write a minimal
   `chirality.project.json`; it is not a read-only attachment operation.
2. Registration returns only `projectId` and `manifestHash`. It issues a separate
   project token. The trusted host resolves that path using
   [resolveHostedProjectTokenFile](../packages/daemon/src/hosted-paths.ts), then
   constructs a project client. A Runtime filesystem project is not automatically
   a Piping model/document; retain an explicit mapping between them.
3. Query `hostedBootstrapStatus` with the host client. It provides safe status
   and the current model/effort catalog. The current composition requires a
   signed-in Codex account and catalog for default session creation. Account
   methods operate on the instance's Codex account, across its registered
   projects, despite their project-scoped route names. Do not promise per-project
   sign-out isolation. The legacy provider-consent method is a compatibility
   no-op, not another setup requirement.
4. Create the conversation with the project client. The default role is
   HELP_HUMAN; preserve role, method, permission and interaction-mode distinctions.
   Before boot or the first turn, the host registers the application's immutable
   tool catalog and workspace identity. An ordinary project client cannot
   register, list, release or complete application-tool calls.
5. Start the turn and dispatch pending calls to the existing application handlers.
   Preserve the Runtime invocation identity, original provider identities, and
   the application's own workspace basis. Validate the domain request at the
   application boundary; Runtime's bounded-JSON checks are not full JSON Schema
   or engineering validation. Use the result shape in `APPLICATION_TOOLS.md`.

The project's [v2 manifest contract](../packages/contracts/src/project.ts) uses
`instructionRoot: { "mode": "runtime" }`, existing relative working/execution
paths and a safe project ID. Do not use the Piping source repository's development
manifest as a replacement for the user's working-project binding.

The host must also expose pending questions/approvals through
`listSessionRequests` and `answerSessionRequest`. Keep provider execution
approval separate from the human's Piping proposal review and Apply action.
Do not route an application-owned tool call through a second generic handler.

## Reconnect, receipts, and persistence

| Event | Required consumer behavior using the current contract |
|---|---|
| Renderer/stream disconnect | Reattach through turn state/stream and replay. Do not send an interrupt merely because observation ended. |
| Explicit Stop | Call `interruptSession`. Pending Runtime calls settle; Piping must check cancellation before its own publication. A completed model commit cannot be rolled back by transport cancellation. |
| Lost submit reply | Recover using the same Piping idempotency key/preview. Reserve that association before awaits. Queued and committed remain distinct. |
| Runtime restart | Reload the session/catalog, reconnect with current credentials, and explicitly rebind the same catalog at idle with the application's current workspace generation. The App host lifecycle alone does not orchestrate handler rebinds. |
| App/controller restart or project replacement | Reconcile Piping's live state first. Preserve known historical outcomes; return expiry/uncertainty when recovery cannot establish them. No blind mutation replay. |
| Save/reopen | Follow Piping persistence. A Runtime conversation, completed tool call, or in-memory model commit is not proof that a project file was saved. Reopen establishes a fresh application basis. |

Runtime call records last until the next prepared turn. Their durable conversation
events preserve observation; replay does not run handlers. Piping retains the
operation outcomes needed for its promised recovery window. The first CLI
proposal promises same-controller-session recovery, not durable restart recovery;
embedding must not silently strengthen that claim.

An atomic batch preserves its submitted order through preview, review and
application. Intermediate validation may depend on earlier temporary operations.
Human approval applies the exact reviewed batch against a still-valid basis;
one invalid operation publishes none. The application receipt confirms published
model/history/result invalidation. A provider tool's `success: true` does not
establish human approval or engineering correctness.

## Prepared follow-on work and verification

These are integration tasks, not additional owner-approval gates or replacements
for Piping's authorized implementation brief and writer handoffs:

| Next task | Owner and proof needed |
|---|---|
| Finish CLI-first loop | Piping: one real human-prompted agent journey for a single change and an atomic batch, actual human Apply, confirmed outcome, Undo and stale/retry cases. |
| Package an independent sidecar | Piping owns Tauri launch/UI; Runtime lead supplies reusable service changes if needed. Establish Node/Codex/instruction resources, private config, startup, shutdown, crash recovery and host-only IPC. No dependency on an installed Chirality App. |
| Add tool binding lifecycle | Consumer host: bind before first turn, reconnect handlers after restart, reject old bindings, and reuse existing Piping handlers. Runtime lead owns fixes to the reusable API if the connecting test exposes one. |
| Qualify the native path | Actual selected Codex and packaged consumer: tool request/result, approved mutation, denial/Stop, detach, restart/rebind/resume. Qualify descendant tool inheritance only if that consumer will rely on it. Controlled transports do not establish these facts. |
| Account/UI readiness | Owning consumer: actual sign-in/sign-out isolation, safe status, native questions/approvals and project/session restoration. App implementation is reusable reference, not completed Piping qualification. |
| Local provider follow-on | Runtime lead: current composition couples default session/model selection to hosted account status. oMLX is a later provider integration requiring an actual local tool loop and observed data boundary, not merely a base-URL setting. |

The current controlled suites already exercise much of the reusable boundary:
[standalone startup](../tests/standalone.test.ts),
[App-owned composition](../tests/app-owned-composition.test.ts),
[application-tool composition](../tests/application-tools-composition.test.ts),
[registry](../tests/application-tools.test.ts),
[supervisor](../tests/codex-application-tools.test.ts), and
[effective home](../tests/codex-effective-home.test.ts).
Use their maintained fixtures for targeted integration checks rather than
creating another parallel test harness. Running them requires a built Runtime;
the App-owned composition suite also imports the sibling App attachment helper.

No Runtime production change is required for Piping's initial CLI projection.
The next useful Runtime code change should follow a concrete consumer contract
or a reproduced failure on the shared path. Service packaging for Tauri,
unattended model application, local inference, Computer Use, CAEPIPE correlation
and public release are not established by this guide.
