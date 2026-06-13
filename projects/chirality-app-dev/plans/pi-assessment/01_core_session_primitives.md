# Pi Core And Session Primitives

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863` (`fix(coding-agent): treat uppercase config values as literals`).

## Scope

Read-only assessment of Pi's generic agent/session layer as a source of Chirality harness primitives.

Primary sources:

- `/Users/ryan/ai-env/projects/pi/packages/agent/README.md`
- `/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md`
- `/Users/ryan/ai-env/projects/pi/packages/agent/docs/hooks.md`
- `/Users/ryan/ai-env/projects/pi/packages/agent/src/types.ts`
- `/Users/ryan/ai-env/projects/pi/packages/agent/src/agent-loop.ts`
- `/Users/ryan/ai-env/projects/pi/packages/agent/src/harness/session/`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/session-format.md`

## Findings

Pi's core package is a useful reference for a small, evented agent loop. The public README frames `@earendil-works/pi-agent-core` as a "stateful agent with tool execution and event streaming" built on `pi-ai` (`/Users/ryan/ai-env/projects/pi/packages/agent/README.md:1`). Its documented event sequence has explicit `agent_start`, `turn_start`, message start/update/end, tool execution start/update/end, `turn_end`, and `agent_end` phases (`/Users/ryan/ai-env/projects/pi/packages/agent/README.md:54` and `/Users/ryan/ai-env/projects/pi/packages/agent/README.md:142`).

The event vocabulary is directly relevant to Chirality's sparse current persisted event set, which stops at session, turn, model, SDK permission, and compaction events (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/src/lib/harness/event-schema.ts:3`). Chirality should borrow the lifecycle vocabulary as a design pattern, not the names as product contract.

The tool loop has two high-value ideas:

- Tool execution can be parallel while persisted tool-result messages remain in assistant source order. Pi documents this ordering guarantee in its core README (`/Users/ryan/ai-env/projects/pi/packages/agent/README.md:102`).
- `beforeToolCall` and `afterToolCall` hooks bracket execution after argument validation and before final result emission (`/Users/ryan/ai-env/projects/pi/packages/agent/README.md:111`).

Pi's semi-durable session design is the strongest primitive. The durable-harness notes state that fully durable runtime objects are unrealistic because tools, providers, extensions, hooks, resource loaders, and prompt callbacks are runtime JS dependencies (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:9`). The practical target is a durable append-only session tree plus host-provided runtime dependency rehydration (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:19`).

This maps well to Chirality because Chirality already treats runtime events as audit, not project truth, and keeps project truth in git-tracked files (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:21`). Pi's session format documents JSONL entries with `id` and `parentId`, enabling in-place branching without rewriting files (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/session-format.md:1`).

## Direct-Use Blockers

Pi's durable restore model is partly a design target, not a complete implemented guarantee. The durable-harness notes describe a future async builder/factory for restore (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:56`) and list required durable entries such as queues, pending writes, operation start/finish, provider request start/finish, and tool call start/finish (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:83`).

That means Pi's own current core should not be treated as satisfying Chirality's closure, handoff, and recovery rules. Pi's notes correctly say every accepted mutation must be durable before public API resolution (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:116`), but Chirality must implement that invariant itself.

Provider streams are not resumable; Pi says recovery can only retry from durable boundaries or mark work interrupted (`/Users/ryan/ai-env/projects/pi/packages/agent/docs/durable-harness.md:134`). That aligns with Chirality's audit posture but prevents any "transparent resume" assumption.

## Recommendation

Adopt these patterns into Chirality-native design:

| Pi primitive | Chirality use | Recommendation |
| --- | --- | --- |
| Event lifecycle | Expand `HarnessEvent` coverage for message/tool/turn phases | Adopt pattern |
| Tool hook bracket | Deny-first permission overlay and post-tool provenance | Adopt pattern |
| Ordered tool-result persistence | Audit replay determinism | Adopt pattern |
| Session tree with `id`/`parentId` | Branching, compaction, replay, turn lineage | Adopt pattern |
| Semi-durable restore | Rehydrate tools/models/hooks from host; validate IDs | Adopt pattern |
| Pi core code | Runtime implementation | Do not copy now |

Verdict: **borrow Pi's core/session architecture as a reference, but keep Chirality's session canonicality, event schema, restore rules, and tool governance product-owned.**
