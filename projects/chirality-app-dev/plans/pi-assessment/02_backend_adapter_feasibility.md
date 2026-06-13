# Pi Backend Adapter Feasibility

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863`.

## Scope

Assess whether Pi can sit behind Chirality's owned runtime contract as a backend adapter alongside the Claude Agent SDK.

Primary sources:

- `/Users/ryan/ai-env/projects/pi/packages/ai/README.md`
- `/Users/ryan/ai-env/projects/pi/packages/ai/package.json`
- `/Users/ryan/ai-env/projects/pi/packages/ai/src/types.ts`
- `/Users/ryan/ai-env/projects/pi/packages/ai/src/stream.ts`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/sdk.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/agent-engine-port.ts`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/claude-agent-sdk-manager.ts`

## Current Chirality Boundary

Chirality already has the right top-level seam: `AgentEnginePort` exposes `subject`, `startTurn(input): AsyncIterable<UIEvent>`, and `interrupt(sessionId)` (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/agent-engine-port.ts:12`). However, the subject union only allows `stub`, `anthropic-direct`, and `claude-agent-sdk` (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/agent-engine-port.ts:3`).

The current SDK path is implemented by `ClaudeAgentSdkManager`, which calls Anthropic's `query()`, appends `turn.accepted` and `turn.started`, maps SDK messages to UI and harness events, tracks active turns, and handles interrupt (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/claude-agent-sdk-manager.ts:21` and `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/claude-agent-sdk-manager.ts:97`).

`sdk-options-builder.ts` is Claude SDK-specific: it imports SDK types, maps permission modes, passes `resume`, isolates `settingSources`, and uses a `claude_code` preset (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/sdk-options-builder.ts:1` and `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/sdk-options-builder.ts:73`).

## Pi Adapter Fit

Pi's `pi-ai` package is provider-rich. Its README describes a unified LLM API with model discovery, provider configuration, token/cost tracking, context persistence, and cross-model handoff (`/Users/ryan/ai-env/projects/pi/packages/ai/README.md:1`). It supports many providers, including OpenAI, Anthropic, Google, Vertex, Mistral, OpenRouter, Bedrock, Copilot, and arbitrary OpenAI-compatible APIs (`/Users/ryan/ai-env/projects/pi/packages/ai/README.md:51`).

This breadth is useful as reference material but dangerous as a shipped Chirality default. Chirality's current product scope maintains Anthropic-only outbound policy (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:58`) and already depends on `@anthropic-ai/claude-agent-sdk` plus `@anthropic-ai/sdk` (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/package.json:23`).

The narrow viable adapter shape is:

1. Add a future `pi-ai-anthropic` or `pi-agent-core` subject behind `AgentEnginePort`.
2. Construct a fixed Anthropic model through Chirality-owned config.
3. Disable Pi registry/resource/model discovery.
4. Reject non-Anthropic providers, custom base URLs, broad ambient credentials, OAuth, custom headers, and project-loaded config.
5. Map Pi stream events into Chirality `UIEvent` and `HarnessEvent`.
6. Persist Chirality accepted/started/terminal events independently of Pi sessions.

`pi-coding-agent` has a programmatic SDK, and its docs show `createAgentSession()` plus `AgentSession` with prompt, steer, followUp, event subscription, tree navigation, compaction, abort, and dispose (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/sdk.md:50` and `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/sdk.md:70`). That surface is too broad for a first shipped adapter because it brings resource loading, extensions, built-in tools, sessions, and cwd-bound services.

## Backend Adapter Matrix

| Candidate | Session ownership | Tool ownership | Provider control | Safety fit | Recommendation |
| --- | --- | --- | --- | --- | --- |
| Claude Agent SDK | SDK transcript plus Chirality audit mirror | SDK tools plus Chirality overlay/MCP | Anthropic-specific | Best current fit if hooks prove sufficient | Continue current R0/R1 path |
| `pi-ai` narrow Anthropic adapter | Chirality-owned; Pi context transient | Chirality-owned tools only | Must hard-allowlist Anthropic | Possible with strict wrapper | Candidate for later spike |
| `pi-agent-core` | Chirality-owned if injected context/session used | Chirality-owned tools via `AgentTool` | Via injected `streamFn` | Possible but more custom work | Candidate after event/session schema hardens |
| `pi-coding-agent` SDK | Pi session/resource system dominates | Pi built-ins unless carefully disabled | Very broad registry/config surface | Poor default fit | Avoid for shipped runtime |
| Fork Pi | Fork owns everything | Fork inherits Pi assumptions | Broad unless heavily changed | High maintenance | Do not pursue |

## Required Contract Changes For A Future Spike

No code should be changed during this assessment, but a future spike would need:

- Add a non-Claude `EngineAdapterSubject`.
- Generalize public session metadata away from `claudeSessionId`.
- Add provider-neutral `HarnessEvent` names for model, message, tool, compaction, queue, and interruption events.
- Extract a real `TurnEngine` so routes stop owning runtime lifecycle.
- Add conformance tests using scripted provider streams before adding a Pi package dependency.

## Recommendation

Verdict: **Pi is conditionally viable as a narrow backend-adapter research path, but not as a direct replacement for Claude Agent SDK.**

The safest future experiment is a no-tools, read-only, sidecar or isolated `pi-ai` Anthropic stream adapter that emits Chirality events and uses Chirality-owned session storage. Do not adopt `pi-coding-agent` as the runtime adapter for production Chirality.
