# Runtime Engine Contract

## Scope

This contract defines Chirality's product-owned turn boundary for harness runtime adapters.
It applies to the deterministic stub adapter, the existing direct Anthropic Messages adapter,
and the opt-in Claude Agent SDK probe adapter.

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

## HarnessEvent Evidence

`frontend/src/lib/harness/event-schema.ts` defines versioned persisted runtime evidence.
`frontend/src/lib/harness/session-events.ts` appends JSONL records under the configured
Chirality session root.

Initial SDK probe events include:

- `turn.accepted`
- `turn.started`
- `sdk.system.init`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`
- `sdk.permission.denied`
- `sdk.compact.boundary`
- `sdk.mirror.error`

Browser `UIEvent` and persisted `HarnessEvent` are separate contracts.

## Claude Agent SDK Probe Posture

`CHIRALITY_HARNESS_PROVIDER=agentSdk` selects the opt-in Claude Agent SDK probe adapter.
The default provider remains unchanged.

Probe posture:

- `@anthropic-ai/claude-agent-sdk` is pinned to `0.3.150`.
- `@anthropic-ai/sdk` is pinned to `0.93.0` to satisfy the SDK peer dependency.
- SDK filesystem settings default to `settingSources: []`.
- `CHIRALITY_SDK_SETTING_SOURCES=project` is the only accepted development override.
- `user` and `local` settings are never passed by the CODEV-001 options builder.
- Built-in tools are disabled for this tranche with `tools: []` and `allowedTools: []`.

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

Packaging remains `BLOCKED_TBD` until a packaged Electron SDK subprocess run is performed.
