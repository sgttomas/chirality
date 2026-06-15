# Runtime Engine Contract

## Scope

This contract defines Chirality's product-owned turn boundary for harness runtime adapters.
It applies to the deterministic stub adapter, the existing direct Anthropic Messages adapter,
and the Claude Agent SDK / Anthropic first-adapter path.

SCA-APP-001 establishes a provider-adapter-general runtime strategy. The current Claude
Agent SDK / Anthropic path remains the first concrete adapter and current shipped path;
concrete non-Anthropic providers require bounded future implementation scope.

The browser-facing event stream remains the stable public contract. Provider and SDK message
names, transcript paths, session IDs, tool names, and permission modes are adapter metadata
unless explicitly mapped into Chirality-owned records.

## AgentEnginePort

The product boundary is represented by `frontend/src/lib/harness/agent-engine-port.ts`.

Required behavior:

- `startTurn(input)` yields only the existing `UIEvent` stream names:
  `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`,
  `turn:error`, and `process:exit`.
- `interrupt(sessionId)` attempts to interrupt the active turn and emits terminal process
  evidence through the adapter.
- SDK/provider identifiers may be stored as metadata fields such as `sdkSessionId` or
  `sdkClaudeCodeVersion`; they do not rename public UI events.

## TurnEngine

`frontend/src/lib/harness/turn-engine.ts` owns the product turn lifecycle above the
adapter port. API routes are transport adapters: they parse HTTP, await engine
preflight, format `UIEvent`s as SSE, and delegate cancellation.

Current lifecycle ownership includes:

- same-session active-turn locking;
- session resume and provider API-key preflight;
- runtime option resolution;
- attachment warning and executable attachment shaping;
- persona prompt existence validation;
- subagent governance evaluation and delegated-subagent shaping;
- adapter stream execution through `IAgentSdkManager`;
- engine session metadata persistence on `session:init`;
- mid-stream adapter error mapping to stable `turn:error` and `process:exit` events.

Pre-stream failures remain JSON API errors. Adapter failures after SSE streaming begins
remain browser-visible SSE terminal evidence.

## HarnessEvent Evidence

`frontend/src/lib/harness/event-schema.ts` defines versioned persisted runtime evidence.
`frontend/src/lib/harness/session-events.ts` appends JSONL records under the configured
Chirality session root.

Current persisted event categories include:

- `turn.accepted`
- `turn.started`
- `adapter.initialized`
- `message.accepted`
- `message.queued`
- `message.started`
- `message.delta`
- `message.completed`
- `model.request.started`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`
- `tool.queued`
- `tool.permission`
- `tool.started`
- `tool.progress`
- `tool.completed`
- `tool.failed`
- `hook.started`
- `hook.progress`
- `hook.completed`
- `hook.failed`
- `queue.enqueued`
- `queue.consumed`
- `queue.cleared`
- `branch.created`
- `branch.selected`
- `branch.summarized`
- `interruption.requested`
- `interruption.completed`
- `context.compaction.started`
- `context.compacted`
- `context.compaction.failed`
- `subagent.started`
- `subagent.progress`
- `subagent.completed`
- `subagent.failed`
- `runtime.mirror.error`

Browser `UIEvent` and persisted `HarnessEvent` are separate contracts.

Read-tool lifecycle evidence is persisted for the currently approved read surfaces:
SDK read built-ins and read-only Chirality MCP tools. Permission callbacks append
`tool.permission` records with allow/deny/ask behavior, decision id, reason,
descriptor identity, adapter tool name, mode, surface, and safe metadata. If permission
audit persistence fails, the SDK callback fails closed by denying execution.

Read MCP handlers append `tool.started` before local execution and then append either
`tool.completed` with result-budget metadata or `tool.failed` with redacted error
metadata. SDK built-in read results append inferred `tool.started` when needed and then
`tool.completed` or `tool.failed` from the SDK `tool_use_result` message. Chirality MCP
completion/failure evidence is owned by the local MCP wrapper to avoid duplicate SDK
completion records.

Tool input evidence stores input key names and recognized safe path fields only. Tool
result evidence stores byte counts, MCP content item counts, descriptor inline/artifact
limits, overflow policy, and budget class. Raw tool outputs are not stored in
`HarnessEvent.data`; this tranche does not add artifact spill files or result artifact
storage.

## Harness Tool Descriptor Contract

`frontend/src/lib/harness/tool-descriptor.ts` defines the Chirality-owned
`HarnessToolDescriptor` registry for SDK built-ins and reserved future tool surfaces.
Descriptors record provider-neutral names, aliases, permissions, path scope, idempotence,
concurrency, interrupt behavior, result-budget policy, provenance events, human-gate
metadata, and adapter tool names.

The current runtime exposes only requested read-class first-adapter SDK built-ins
(`Read`, `Glob`, `Grep`, and `LS`) and requested read-only Chirality MCP tools after
descriptor and permission-overlay resolution. The current Chirality MCP read tools are
`mcp__chirality__status_read`, `mcp__chirality__deps_read`,
`mcp__chirality__scope_scan`, and `mcp__chirality__scaffold_preview`.

The SDK options builder passes requested and allowed names through both `tools` and
`allowedTools`, keeps denied and unrequested tool names in `disallowedTools`, attaches
the in-process `chirality` MCP server only when a Chirality MCP read descriptor is
allowed, and keeps `canUseTool` attached for explicit hard-deny enforcement. Unknown
`opts.tools` fail structurally before adapter streaming begins.

Write, edit, shell, network, subagent, and mutating Chirality MCP tools remain unavailable
to the model. Their descriptors remain metadata only until their bounded implementation,
hook, result-storage, and validation tranches land.

## First Adapter Probe Posture

`CHIRALITY_HARNESS_PROVIDER=agentSdk` selects the opt-in Claude Agent SDK probe adapter.
The default provider remains unchanged unless a later bounded runtime tranche changes it.

Probe posture:

- `@anthropic-ai/claude-agent-sdk` is pinned to `0.3.150`.
- `@anthropic-ai/sdk` is pinned to `0.93.0` to satisfy the SDK peer dependency.
- SDK filesystem settings default to `settingSources: []`.
- `CHIRALITY_SDK_SETTING_SOURCES=project` is the only accepted development override.
- `user` and `local` settings are never passed by the CODEV-001 options builder.
- Requested read built-ins and requested read-only Chirality MCP tools are exposed for the
  opt-in `agentSdk` path after descriptor and permission resolution. Denied or unrequested
  built-ins and MCP tools remain in descriptor-derived `disallowedTools`.

Pi is a pattern corpus/reference only. This contract does not authorize a Pi adapter, fork,
package import, Node 22 sidecar, runtime-floor migration, or spike.

## Conformance Gates

An adapter cannot become the default production runtime until it passes:

- stable UI event name checks,
- provider-neutral public type checks,
- SDK options isolation checks,
- SDK message mapping checks,
- session metadata linkage checks,
- interrupt/cancel terminal evidence checks,
- API key redaction checks,
- route/SSE regression checks.

`frontend/src/lib/harness/engine-conformance.ts` provides the executable adapter
conformance evaluator. Companion fixtures use deterministic scripted provider streams so
success, failure, and interruption behavior can be checked without live provider calls or
new backend adapter dependencies.

Packaging remains `BLOCKED_TBD` until a packaged Electron SDK subprocess run is performed.
