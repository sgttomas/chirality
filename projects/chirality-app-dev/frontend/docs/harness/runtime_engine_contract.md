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
SDK read built-ins and Chirality MCP read tools. Permission callbacks append
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
`HarnessEvent.data`. Bash overflow output may be spilled to redacted session-local
artifacts after descriptor budgets require it; other raw tool artifact storage remains
future scope.

Write/edit lifecycle evidence is persisted for the currently approved SDK built-in write
surfaces: `Write` and `Edit` in `workspaceWrite` mode. Permission callbacks append
`tool.permission` records before execution, and Chirality `PreToolUse` hooks enforce
project-root containment, instruction-root write blocking, symlink write rejection, and
fail-closed audit behavior. The write hooks append provider-neutral `hook.started`,
`hook.completed`, and `hook.failed` events with safe path metadata, pre/post file state
metadata, result-budget metadata, and diff-provenance flags. Raw file contents, raw tool
outputs, and full diffs are not stored in `HarnessEvent.data`; artifact spill files and
full diff storage remain future scope.

Mutating Chirality MCP lifecycle evidence is persisted for the D-APP-13 Option A tools
`mcp__chirality__status_transition` and `mcp__chirality__deps_write`. These tools are
available only when explicitly requested in `workspaceWrite` mode. Because the SDK MCP
behavior probe showed raw in-process `mcp_message` calls do not automatically invoke SDK
`canUseTool` or hook callbacks, each mutating MCP handler runs its own fail-closed
permission/evidence wrapper. The wrapper emits `tool.started`, `tool.permission`, and
then `tool.completed` or `tool.failed`; enforces project-root containment,
instruction-root write blocking, and symlink target rejection; snapshots target-file
SHA-256 and byte length before and after execution; and records only result summaries,
bounded diff metadata, and redacted error metadata. Raw `_STATUS.md`, raw
`Dependencies.csv`, raw full diffs, raw SDK transcripts, and secrets are not stored in
`HarnessEvent.data`.

Bash lifecycle evidence is persisted for the approved SDK `Bash` built-in only in
`workspaceWrite` mode. Bash remains denied in `readOnly`, `dontAsk`, and ordinary `ask`
exposure. Permission callbacks and Chirality `PreToolUse` hooks enforce default timeout
injection, maximum timeout policy, no background execution, no sandbox override,
project-root containment for obvious path and redirection targets, instruction-root
blocking, symlink redirection rejection, and static no-network command checks. Bash
`PostToolUse` hooks record stdout/stderr byte-count metadata separately and spill
redacted overflow results to session-local tool artifacts when descriptor budgets require
it. Raw stdout, stderr, commands, and API keys are not stored in `HarnessEvent.data`.

## Agent/Subagent Runtime Contract

`frontend/src/lib/harness/agent-runtime-contract.ts` defines the current Chirality-owned
agent/subagent contract. Bounded executable child turns are now permitted only through the
D-APP-10 Option C path described below.

Current posture:

- unbounded executable delegation is blocked;
- SDK `agents` definitions may be generated only for already-eligible delegated Type 2
  candidates;
- generated child definitions do not inherit parent tools or capabilities;
- Pi remains a pattern corpus / reference only, with no runtime dependency, adapter, fork,
  sidecar, package import, or spike;
- concrete non-Anthropic provider routing remains blocked;
- child runs do not inherit parent capabilities.

Provider-neutral child-run records use Chirality fields such as `childRunId`,
`parentSessionId`, `parentTurnId`, `parentPersona`, `agentName`, `status`,
`capabilityPolicy`, `governance`, and `outputArtifactPath`. Adapter-specific values such as
external session IDs, task IDs, tool-use IDs, transcript keys, or concrete adapter names may
be retained only under the `adapter` metadata object.

The contract preserves these semantics for governed subagents:

- governance preflight can create `queued` or `denied` child-run records;
- denied delegation records keep the fail-closed gate, reason, allowlist, delegated list,
  and approval metadata where present;
- child capability policy starts with `inheritParentCapabilities: false`,
  `allowedToolNames: []`, and explicit denied capabilities for read, write, shell, MCP,
  network, and subagent surfaces until a later bounded implementation grants a narrower
  child tool set;
- `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed`
  remain the provider-neutral runtime event categories for child-run lifecycle evidence;
- completed executable child runs must carry an output artifact reference when the adapter
  provides one.

`R5-BRIDGE-001` implements the D-APP-09 Option B non-executable bridge through
`R5-SLICE-003`; `R5-SLICE-006` then implements the D-APP-10 Option C executable path. The
SDK `Agent` tool is model-visible only when the parent explicitly requests it and
`evaluateSubagentGovernance` has produced delegated Type 2 child names. Agent definitions
carry `tools: []`, descriptor-derived `disallowedTools` including `Agent`, `maxTurns: 1`,
and `permissionMode: dontAsk`. The Agent permission callback and
`chirality.subagent.pre_tool_use` hook both re-check the requested child name against the
delegated list before execution. Adapter task messages are mapped into provider-neutral
`subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed`
events.

This executable path does not approve child capability inheritance, unrestricted child tool
access, nested subagent execution, provider routing, network expansion, Pi runtime paths,
dependency-register edits, project-wide dependency-closure claims, or release and
professional-boundary claims.

## Harness Tool Descriptor Contract

`frontend/src/lib/harness/tool-descriptor.ts` defines the Chirality-owned
`HarnessToolDescriptor` registry for SDK built-ins and reserved future tool surfaces.
Descriptors record provider-neutral names, aliases, permissions, path scope, idempotence,
concurrency, interrupt behavior, result-budget policy, provenance events, human-gate
metadata, and adapter tool names.

The current runtime exposes requested read-class first-adapter SDK built-ins (`Read`,
`Glob`, `Grep`, and `LS`), requested Chirality MCP read tools, requested
SDK `Write` / `Edit` built-ins, requested SDK `Bash` only in `workspaceWrite` mode,
and requested mutating Chirality MCP tools only in `workspaceWrite` mode after descriptor,
permission-overlay, and handler-wrapper resolution. The current Chirality MCP read tools
are `mcp__chirality__status_read`,
`mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and
`mcp__chirality__scaffold_preview`. The current mutating Chirality MCP tools are
`mcp__chirality__status_transition` and `mcp__chirality__deps_write`.

The SDK options builder passes requested and allowed names through both `tools` and
`allowedTools`, keeps denied and unrequested tool names in `disallowedTools`, attaches
the in-process `chirality` MCP server only when a Chirality MCP descriptor is
allowed, and keeps `canUseTool` attached for explicit hard-deny enforcement. Unknown
`opts.tools` fail structurally before adapter streaming begins.

`MultiEdit`, notebook edits, network, unrestricted subagent capability, and
`mcp__chirality__scaffold_exec` remain
unavailable to the model. Their descriptors remain metadata only until their bounded
implementation, hook, result-storage, and validation tranches land.

## First Adapter Probe Posture

`CHIRALITY_HARNESS_PROVIDER=agentSdk` selects the opt-in Claude Agent SDK probe adapter.
The default provider remains unchanged unless a later bounded runtime tranche changes it.

Probe posture:

- `@anthropic-ai/claude-agent-sdk` is pinned to `0.3.150`.
- `@anthropic-ai/sdk` is pinned to `0.93.0` to satisfy the SDK peer dependency.
- SDK filesystem settings default to `settingSources: []`.
- `CHIRALITY_SDK_SETTING_SOURCES=project` is the only accepted development override.
- `user` and `local` settings are never passed by the CODEV-001 options builder.
- Requested read built-ins, requested Chirality MCP read tools, requested
  `Write` / `Edit` built-ins, requested `Bash` in `workspaceWrite` mode, and requested
  mutating Chirality MCP tools in `workspaceWrite` mode are exposed
  for the opt-in `agentSdk` path after descriptor, permission, handler-wrapper, and hook-policy
  resolution. Denied or unrequested built-ins and MCP tools remain in descriptor-derived
  `disallowedTools`.

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
