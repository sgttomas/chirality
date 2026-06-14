# Pi Backend Adapter Feasibility

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863`.

SCA-APP-001 status: historical/reference assessment. Pi is now a pattern corpus and reference source only. D-APP-01 and D-APP-02 rule out a Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, and immediate spike work unless a future human ruling explicitly reverses those boundaries.

## Scope

Assess whether Pi could sit behind Chirality's owned runtime contract as a backend adapter alongside the Claude Agent SDK. This assessment is retained for pattern-corpus evidence only and does not authorize implementation.

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

This breadth is useful as reference material but dangerous as a shipped Chirality default. Chirality's current product scope maintains the shipped loopback plus Anthropic outbound policy and already depends on `@anthropic-ai/claude-agent-sdk` plus `@anthropic-ai/sdk` (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/package.json:23`).

The previously assessed narrow adapter shape was:

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
| `pi-ai` narrow Anthropic adapter | Chirality-owned; Pi context transient | Chirality-owned tools only | Must hard-allowlist Anthropic | Possible with strict wrapper | Not approved under D-APP-01/D-APP-02 |
| `pi-agent-core` | Chirality-owned if injected context/session used | Chirality-owned tools via `AgentTool` | Via injected `streamFn` | Possible but more custom work | Not approved under D-APP-01/D-APP-02 |
| `pi-coding-agent` SDK | Pi session/resource system dominates | Pi built-ins unless carefully disabled | Very broad registry/config surface | Poor default fit | Avoid for shipped runtime |
| Fork Pi | Fork owns everything | Fork inherits Pi assumptions | Broad unless heavily changed | High maintenance | Do not pursue |

## Superseded Future-Spike Notes

No code should be changed during this assessment. The prior future-spike notes are superseded by D-APP-01 and D-APP-02, but they remain useful as pattern evidence for provider-adapter architecture:

- Add a non-Claude `EngineAdapterSubject`.
- Generalize public session metadata away from `claudeSessionId`.
- Add provider-neutral `HarnessEvent` names for model, message, tool, compaction, queue, and interruption events.
- Extract a real `TurnEngine` so routes stop owning runtime lifecycle.
- Add conformance tests using scripted provider streams before any future provider package dependency.

## Recommendation

Verdict: **Pi is a useful backend-adapter pattern corpus, but not an approved Chirality runtime dependency, adapter target, fork, or spike.**

Do not run a Pi adapter experiment under current scope. Concrete non-Anthropic provider work and any reversal of the Pi package boundary require a bounded future tranche and human ruling.
