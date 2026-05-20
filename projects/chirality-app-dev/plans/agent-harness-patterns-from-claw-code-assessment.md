# Agent Harness Patterns From `claw-code-parity/` and `clawd-code/`

Date: 2026-05-18

Author: Codex assessment pass

Scope:
- Source observations from `/Users/ryan/ai-env/projects/claw-code-parity/`
- Source observations from `/Users/ryan/ai-env/projects/clawd-code/`
- Fit analysis for `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/`

## Executive Summary

`clawd-code/` is valuable as a dense example of a mature agent harness. The strongest reusable ideas are not individual tools or commands, but the architecture:

1. A rich `Tool` contract that makes each tool responsible for schema, prompt text, input validation, permission behavior, concurrency safety, interruption semantics, UI rendering, result serialization, and telemetry-safe summaries.
2. A layered turn loop where model streaming, tool execution, permission checks, hooks, compaction, and transcript persistence are explicit lifecycle phases.
3. A permission pipeline that separates static rules, mode gates, per-tool checks, hook decisions, interactive prompting, and automated classification.
4. A tool pool assembly path that filters tools before the model sees them, including deny rules, feature gates, MCP tools, and deferred tool discovery.
5. Session and transcript machinery that writes enough state early enough to make interruption and resume trustworthy.
6. Subagent handling that treats delegation as a governed, typed runtime feature rather than a plain prompt convention.
7. Operational polish: progress events, cancellability, background tasks, streaming fallback handling, result truncation, and structured error surfacing.

`claw-code-parity/` is less useful as a direct implementation model. Its Python side is mostly an inventory and parity workspace, while its Rust side is a simplified runtime sketch. The Rust modules are useful because they show a cleaner, smaller expression of the same conceptual runtime: session, conversation loop, permission policy, hook runner, compaction, usage, and tool registry. The Rust implementation demonstrates a useful direction for Chirality: design the harness core as small, testable runtime services instead of letting the web route own the whole turn lifecycle.

Chirality already has a good skeleton:

- `frontend/src/lib/harness/types.ts` defines clear contracts.
- `frontend/src/app/api/harness/turn/route.ts` owns SSE turn delivery and turn locking.
- `frontend/src/lib/harness/session-manager.ts` persists basic session records.
- `frontend/src/lib/harness/options.ts` resolves persona, mode, tools, model, and max turns.
- `frontend/src/lib/harness/subagent-governance.ts` already implements explicit delegation gates.
- `frontend/src/lib/harness/attachment-resolver.ts` has careful local attachment validation.
- `docs/harness/*` and validation scripts define a local test matrix.

The main gap is that Chirality's current harness is still more of a thin Anthropic streaming adapter than an agent harness. It does not yet have a first-class tool runtime, permission policy engine, hook pipeline, event mapper, transcript/run record, context budget manager, or resumable model/tool loop. Those should be designed as Chirality-native components.

## Source Inventory

### `clawd-code/`

High-signal areas inspected:

- `src/Tool.ts`
- `src/tools.ts`
- `src/query.ts`
- `src/QueryEngine.ts`
- `src/services/tools/StreamingToolExecutor.ts`
- `src/services/tools/toolExecution.ts`
- `src/services/tools/toolHooks.ts`
- `src/hooks/toolPermission/PermissionContext.ts`
- `src/hooks/useCanUseTool.tsx`
- `src/utils/permissions/*`
- `src/tools/BashTool/*`
- `src/tools/AgentTool/*`
- `src/tools/ToolSearchTool/*`
- `src/tasks/*`
- `src/commands.ts`
- `src/commands/*`
- `src/services/*`
- `src/remote/*`
- `src/bridge/*`
- `src/assistant/sessionHistory.ts`

Observed character:
- Large TypeScript/React terminal application.
- Many files appear built or transformed, with source maps and feature gates.
- The harness is deeply productized: commands, plugins, skills, analytics, remote bridges, MCP, LSP, background tasks, session persistence, prompt cache management, and terminal UI are all integrated.

### `claw-code-parity/`

High-signal areas inspected:

- `README.md`
- `PARITY.md`
- `src/runtime.py`
- `src/query_engine.py`
- `src/tools.py`
- `src/tool_pool.py`
- `src/permissions.py`
- `src/session_store.py`
- `src/transcript.py`
- `rust/crates/runtime/src/conversation.rs`
- `rust/crates/runtime/src/session.rs`
- `rust/crates/runtime/src/permissions.rs`
- `rust/crates/runtime/src/hooks.rs`
- `rust/crates/runtime/src/compact.rs`
- `rust/crates/tools/src/lib.rs`

Observed character:
- Python side is mostly a clean-room parity/inventory harness, not a full agent runtime.
- Rust side is closer to a minimal harness runtime and is useful as a simpler conceptual model.
- `PARITY.md` is useful because it names design gaps between a small runtime and a mature harness.

### Chirality Current Harness

High-signal areas inspected:

- `docs/harness/chirality_harness_graphs_and_sequence.md`
- `docs/harness/harness_manual_validation.md`
- `frontend/src/lib/harness/types.ts`
- `frontend/src/lib/harness/runtime.ts`
- `frontend/src/lib/harness/session-manager.ts`
- `frontend/src/lib/harness/options.ts`
- `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`
- `frontend/src/lib/harness/agent-sdk-manager.ts`
- `frontend/src/lib/harness/subagent-governance.ts`
- `frontend/src/lib/harness/attachment-resolver.ts`
- `frontend/src/lib/harness/instruction-root.ts`
- `frontend/src/lib/harness/agent-instruction.ts`
- `frontend/src/app/api/harness/turn/route.ts`
- `frontend/src/app/api/harness/session/boot/route.ts`
- `frontend/src/app/api/harness/interrupt/route.ts`
- `frontend/src/__tests__/lib/harness-*.test.ts`

Observed character:
- The system is intentionally local, document-driven, and validation-heavy.
- The app has strong shell around a harness, but the runtime core is early.
- There is no mature internal tool execution model yet.

## Most Transferable Patterns

### 1. Tool Contract As The Harness Boundary

`clawd-code/src/Tool.ts` defines a large, explicit contract for tools. The important pattern is not the exact shape. The important pattern is that tools are not just callables. A tool owns:

- Input schema
- Optional output schema
- Prompt text shown to the model
- User-facing name and compact activity description
- Tool-specific input validation
- Permission check behavior
- Read-only vs write/destructive classification
- Concurrency safety
- Interrupt behavior
- Result mapping to model-facing blocks
- UI rendering and transcript text extraction
- Result size policy
- Optional hook matching support
- MCP metadata when applicable

Chirality implication:
- Replace the current `opts.tools: string[]` idea with a real `HarnessTool` contract.
- Keep the first version smaller than `clawd-code`, but include enough metadata to support safety, UI, and execution.
- Tool metadata should be consumed before the model request is built, not only after a tool call is requested.

Recommended Chirality-native minimal contract:

```ts
type HarnessToolPermission = 'read' | 'workspace-write' | 'network' | 'danger';

type HarnessToolDescriptor<Input, Output> = {
  name: string;
  aliases?: string[];
  description: string;
  inputSchema: unknown;
  outputSchema?: unknown;
  permissions: HarnessToolPermission[];
  isReadOnly(input: Input): boolean;
  isConcurrencySafe(input: Input): boolean;
  interruptBehavior?: 'cancel' | 'block';
  validateInput?(input: Input, context: HarnessToolContext): Promise<void>;
  checkPermissions?(input: Input, context: HarnessToolContext): Promise<HarnessPermissionDecision>;
  execute(input: Input, context: HarnessToolContext): Promise<HarnessToolResult<Output>>;
  summarize?(input: Partial<Input>): string;
};
```

Do not import this from `clawd-code`. Design it from Chirality's own needs.

### 2. Tool Pool Assembly Before Model Exposure

`clawd-code/src/tools.ts` has a central tool pool assembly path. It:

- Collects built-in tools.
- Applies feature gates.
- Applies permission-context deny filtering before tools reach the model.
- Merges MCP tools.
- Deduplicates names.
- Preserves deterministic ordering for cache stability.
- Supports a simplified mode where only core tools are exposed.
- Supports deferred tools through a search tool.

Chirality implication:
- Tool selection should be a runtime service, not a loose array of strings in `HarnessOpts`.
- A `ToolRegistry` plus `ToolPoolResolver` should decide what the model sees.
- Denied tools should be removed before prompt construction whenever possible.
- Ordering should be deterministic to keep model prompts and tests stable.

Seed modules:

- `frontend/src/lib/harness/tool-registry.ts`
- `frontend/src/lib/harness/tool-pool.ts`
- `frontend/src/lib/harness/tool-contracts.ts`

Initial behavior:

- Built-ins: `read_file`, `write_file`, `edit_file`, `bash`, maybe `list_files`.
- Filter by persona defaults from `AGENT_*.md`.
- Filter by `opts.tools`.
- Filter by permission mode and deny rules.
- Sort by stable built-in order, then alphabetically for dynamic tools.

### 3. Deferred Tool Discovery

`clawd-code/src/tools/ToolSearchTool/ToolSearchTool.ts` shows a pattern for reducing initial prompt surface. Rare tools are deferred and located by keyword or direct selection.

Chirality implication:
- This is useful later, not first.
- Chirality should first get a small tool set working correctly.
- Once tools expand, add a Chirality-native `tool_search` that returns allowed deferred tool names and short descriptions.

Avoid:
- Do not build a complex tool search system before the core tool runtime exists.
- Do not expose deferred tools that the permission engine would later deny.

### 4. Layered Permission Pipeline

`clawd-code` separates several concerns:

- Permission modes
- Rule-based allow, deny, and ask entries
- Per-tool validation and permission checks
- Hook decisions
- Interactive prompts
- Automated classifier checks
- Coordinator and subagent-specific permission handling
- Decision logging

The key pattern is the order:

1. Validate schema.
2. Validate tool-specific semantics.
3. Run pre-tool hooks.
4. Resolve hook decision against deny and ask rules.
5. Resolve permission mode and per-tool permission.
6. Ask the user or caller only if necessary.
7. Execute the tool.
8. Run post-tool or failure hooks.
9. Emit a model-facing tool result and UI-facing events.

Chirality current state:
- `subagent-governance.ts` has explicit gates.
- `turn/route.ts` handles `dontAsk` only through test markers.
- There is no generic permission policy engine.

Chirality implication:
- Add a permission engine before adding powerful tools.
- Keep it simple and auditable.
- Make permission decisions structured records, not free-form booleans.

Recommended modes:

- `readOnly`: read-only tools only.
- `workspaceWrite`: local project writes allowed through approved tools.
- `dontAsk`: deny any action not already allowed by rule.
- `ask`: pause and require UI confirmation for unknown writes.
- `bypass`: available only behind explicit local configuration, not default.

Recommended rule model:

```ts
type HarnessPermissionRule = {
  source: 'persona' | 'session' | 'project' | 'operator';
  behavior: 'allow' | 'deny' | 'ask';
  toolName: string;
  pattern?: string;
};
```

Important implementation rule:
- Deny rules should override hook or classifier allow decisions.

### 5. Hooks As Runtime Extension Points

`clawd-code/src/services/tools/toolHooks.ts` and `claw-code-parity/rust/crates/runtime/src/hooks.rs` both expose a useful idea:

- `PreToolUse`
- `PostToolUse`
- `PostToolUseFailure`
- Permission request hooks
- Progress events from hook execution
- Hook-provided additional context
- Hook-updated input
- Hook cancellation

Chirality implication:
- Hooks would fit Chirality's professional engineering workflow well because they can connect validation, provenance, dependency tracking, and deliverable status updates to agent actions.
- Hooks should be local and deterministic at first. Avoid remote or marketplace-style hooks until the trust model is mature.

First useful hooks for Chirality:

- `beforeToolUse`: validate file paths stay inside current project root.
- `beforeToolUse`: block writes to instruction root and protected execution metadata unless explicitly approved.
- `afterToolUse`: update run record.
- `afterToolUse`: append provenance event.
- `onToolFailure`: add triage record for failed command or write.

Avoid:
- Do not let hooks mutate arbitrary inputs silently in early versions.
- If input mutation is allowed, require explicit event logging.

### 6. Streaming Tool Execution And Concurrency

`clawd-code/src/services/tools/StreamingToolExecutor.ts` and `toolOrchestration.ts` show two related patterns:

- Read-only or concurrency-safe tools can run in parallel.
- Non-concurrency-safe tools run serially.
- Tool results are emitted in a predictable order.
- Sibling tools can be cancelled if one errors.
- User interruption can cancel only tools that declare cancellability.
- Streaming fallback can discard partial tool results safely.

Chirality current state:
- The stream is only model text events plus coarse process events.
- No internal tool execution exists yet.

Chirality implication:
- Build serial execution first.
- Add concurrent execution only after each tool can declare read-only/concurrency behavior.
- Event order should be stable and testable.

Recommended event types:

- `tool:queued`
- `tool:start`
- `tool:progress`
- `tool:result`
- `tool:error`
- `tool:cancelled`
- `tool:permission`

### 7. Query Engine As Conversation Owner

`clawd-code/src/QueryEngine.ts` centralizes headless conversation state:

- Mutable messages
- Read-file cache
- Permission denials
- Usage totals
- Session persistence
- Prompt assembly
- Slash command processing
- System init event
- Streaming SDK events
- Transcript recording

`claw-code-parity/src/query_engine.py` and Rust `conversation.rs` show simpler versions of this.

Chirality current state:
- `turn/route.ts` owns too much of the lifecycle.
- `AnthropicAgentSdkManager` directly calls `messages.create` for a single user message.
- Session records persist only metadata, not a transcript or turn log.

Chirality implication:
- Introduce a `TurnEngine` or `ConversationEngine`.
- Keep Next.js routes as transport adapters.
- Make the engine testable without HTTP.

Candidate boundary:

```text
API route
  -> read request and session
  -> call ConversationEngine.runTurn(...)
  -> stream UI events

ConversationEngine
  -> resolve options
  -> build prompt/instructions
  -> resolve tool pool
  -> run model/tool loop
  -> persist transcript/run records
  -> emit typed events
```

### 8. Session Persistence And Early Transcript Writes

`clawd-code` explicitly writes user input to transcript before model response so a killed process can resume from the accepted user turn. The Rust parity runtime also models session persistence, JSON/JSONL loading, log rotation, compaction records, and fork metadata.

Chirality current state:
- `FileSessionManager` stores a small JSON record per session.
- It persists `claudeSessionId`, `model`, `bootFingerprint`, and timestamps.
- There is no append-only transcript or structured run record for each turn.

Chirality implication:
- Add append-only session events in `.chirality/sessions/<id>/events.jsonl` or equivalent.
- Keep the existing session JSON as the summary/index record.
- Write the user request event before the model request starts.
- Write `session:init`, tool events, assistant deltas, completion, interruption, and errors.

Recommended files:

```text
.chirality/sessions/<sessionId>/session.json
.chirality/sessions/<sessionId>/events.jsonl
.chirality/sessions/<sessionId>/turns/<turnId>.json
.chirality/sessions/<sessionId>/artifacts/
```

Acceptance criteria:
- A process killed after accepting user input but before first model token still leaves a resumable record.
- A cancelled stream records interruption with a timestamp.
- Session listing can ignore malformed records without losing valid sessions.

### 9. Context Budget And Compaction

`clawd-code/src/query.ts` has a mature context flow:

- Tool result budgeting
- Microcompaction
- Snip/history projection
- Auto-compaction
- Reactive compaction after model errors
- Prompt-too-long handling
- Tool-use summaries

`claw-code-parity/rust/crates/runtime/src/compact.rs` shows a much smaller but understandable compaction pattern:

- Estimate tokens.
- Preserve recent messages.
- Summarize earlier messages.
- Add a continuation message.
- Track removed message count.

Chirality implication:
- Start with the Rust-shaped approach, not the full `clawd-code` machinery.
- Use a deterministic compaction record first, then add model-generated summaries later.
- Keep full transcript on disk even when the model context is compacted.

Recommended first version:

- A `ContextWindowManager` estimates context size.
- It preserves last N turns.
- It injects a deterministic summary of older turns.
- It records compaction boundaries in session events.

Later:
- Model-generated summary with validation.
- Tool result externalization for large outputs.
- Per-tool `maxResultSizeChars`.

### 10. Tool Result Storage

`clawd-code` treats large tool outputs as a budget problem. Tools can define result size limits. Large outputs may be persisted and replaced with previews.

Chirality implication:
- This is especially relevant because Chirality works with engineering documents and execution artifacts.
- Do not stream huge command output directly into chat.
- Store raw outputs under session artifacts and return summaries with paths.

Recommended policy:

- Inline small results.
- Truncate medium results with clear marker and artifact path.
- Persist large results and provide preview plus metadata.
- Never persist sensitive values without redaction pass.

### 11. Subagents As Governed Runtime Entities

`clawd-code/src/tools/AgentTool/*` is broad, but the transferable ideas are:

- Subagents have typed definitions.
- Subagents can be filtered by permission and required capabilities.
- Subagents have their own model, prompt, tools, cwd, isolation, and progress.
- Background and foreground lifecycles differ.
- Agent IDs and parent-child relationships matter.
- Delegation should be visible in UI and transcript.

Chirality current state:
- `subagent-governance.ts` already gates delegation by environment, persona allowlist, metadata, context sealing, pipeline approval, approval reference, and agent instruction type.
- This is stronger and more domain-specific than a generic agent spawn.

Chirality implication:
- Keep current governance as the top-level policy.
- Add a runtime agent registry only after the main turn engine can persist subagent events.
- Do not let model-generated delegation bypass `evaluateSubagentGovernance`.

Recommended subagent record:

```ts
type HarnessSubagentRun = {
  agentRunId: string;
  parentSessionId: string;
  parentTurnId: string;
  persona: string;
  agentName: string;
  model: string;
  projectRoot: string;
  status: 'queued' | 'running' | 'completed' | 'failed' | 'cancelled';
  startedAt?: string;
  completedAt?: string;
  outputArtifactPath?: string;
};
```

### 12. Slash Commands And Local Commands

`clawd-code/src/commands.ts` and `src/commands/*` show a huge command surface. The key pattern is that slash commands are not model tools. They are local UI/session operations that can:

- Mutate session state.
- Change model or permission mode.
- Trigger local views.
- Load context.
- Manage plugins, skills, MCP, memory, cost, status, and history.

Chirality implication:
- Do not rush to a huge slash command system.
- Chirality should distinguish:
  - Local commands that never go to the model.
  - Agent tools that the model may request.
  - Operator toolkit controls that map to request options.

Good early local commands:

- `/clear`
- `/compact`
- `/status`
- `/mode`
- `/persona`
- `/sessions`
- `/run-record`

### 13. Skills And Plugins

`clawd-code` has skills and plugins. `claw-code-parity/PARITY.md` identifies these as major parity gaps in smaller ports.

Chirality implication:
- Skills are a good match if they map to local `agents/AGENT_*.md`, domain procedures, or deliverable templates.
- Plugins are likely too broad for near-term work.

Recommended sequence:

1. Treat existing agent instructions as a first-class skill/persona registry.
2. Add local read-only skill discovery.
3. Add tool adapters only for built-in local tools.
4. Consider plugin boundaries only after permission and hook models are mature.

### 14. MCP And External Integrations

`clawd-code` integrates MCP heavily. Patterns worth learning:

- Dynamic tools should carry server metadata.
- Tool names must avoid collisions.
- Permission rules need server-level matching.
- Dynamic tools should be filtered before prompt exposure.
- Connection state should be visible to users.

Chirality implication:
- MCP can be useful later, but the first harness runtime should not depend on it.
- If added, MCP tools must pass through the same `ToolRegistry`, `ToolPoolResolver`, and permission policy as built-ins.

### 15. Observability And Error Taxonomy

`clawd-code` has broad analytics and telemetry. Chirality should not copy that product instrumentation, but the pattern is useful:

- Distinguish user-facing errors from diagnostic records.
- Use stable error categories.
- Redact secrets.
- Log lifecycle phases.
- Measure slow permission or hook phases.
- Record whether an error happened before, during, or after streaming.

Chirality current state:
- `HarnessError` is a good start.
- `turn/route.ts` emits `turn:error` and `process:exit`.
- `anthropic-agent-sdk-manager.ts` has careful API key redaction and network policy enforcement.

Recommended additions:

- `HarnessRunLogger` that writes JSONL events.
- Stable event schema version.
- Redaction helper shared by model, tools, and logs.
- Phase-level timings.

## What To Avoid

Do not carry these patterns forward directly:

1. Do not build feature-gate complexity before the core runtime exists.
2. Do not mix route code, model streaming, permissions, tools, and persistence in one module.
3. Do not make a generic plugin marketplace before permission and provenance are strong.
4. Do not rely on model-only instructions for filesystem safety.
5. Do not let tool allow decisions override explicit deny rules.
6. Do not stream unbounded tool output into chat.
7. Do not treat subagents as plain recursive prompts.
8. Do not add remote execution until local run records, cancellation, and path policies are reliable.

## Chirality Gap Analysis

### Current Strengths

1. Clear API contracts
   - `frontend/src/lib/harness/types.ts` is compact and readable.
   - `UIEvent` is already a good transport-level abstraction.

2. Local filesystem boundary
   - `session-manager.ts` validates absolute project roots.
   - `instruction-root.ts` prevents project root conflicts with instruction root.
   - `attachment-resolver.ts` rejects symlinks, unsupported types, over-budget files, and unreadable paths.

3. Governance culture
   - `subagent-governance.ts` is explicit and domain-aware.
   - The app already treats delegation as a controlled activity.

4. Validation artifacts
   - `docs/harness/harness_manual_validation.md`
   - `frontend/scripts/validate-harness-section8.mjs`
   - `frontend/scripts/validate-harness-premerge.mjs`
   - Existing tests under `frontend/src/__tests__/lib/harness-*.test.ts`

5. Provider mode abstraction
   - `runtime.ts` supports stub and Anthropic providers.
   - This is useful for testing without live API calls.

### Current Weaknesses

1. No real internal tool runtime
   - `opts.tools` exists but is not backed by a local tool registry and execution loop.
   - The Anthropic manager streams plain assistant text from `messages.create`.

2. No model/tool loop
   - There is no loop that handles assistant tool requests, executes tools, appends tool results, and continues until completion.

3. Route owns too much lifecycle
   - `turn/route.ts` handles session lock, option resolution, attachment warnings, prompt validation, persona prompt call, governance, stream construction, session persistence, and error event mapping.

4. No append-only transcript
   - Session metadata exists, but not a robust per-turn event log.

5. Weak permission model
   - Test markers cover `dontAsk`; no generic permission engine exists.

6. Persona prompt is a stub
   - `persona-manager.ts` verifies persona existence but does not yet compose a real system prompt from instruction root resources.

7. No context budgeting
   - `maxTurns` exists in options but not as a full conversation control.

8. Limited observability
   - Errors are structured, but there is no run logger or event replay.

## Recommended Development Plan Seed

### Phase 0 - Decide Harness Runtime Scope

Purpose:
- Establish what the local harness is responsible for versus what the provider SDK owns.

Decisions to record:
- Whether Chirality will execute local tools itself.
- Which provider API supports tool calling in the first implementation.
- Whether the first runtime supports only single-agent turns or includes subagent spawning.
- Whether tool outputs are persisted under `.chirality/sessions`.

Output:
- `docs/harness/runtime_scope.md`
- Updated `docs/harness/chirality_harness_graphs_and_sequence.md`

### Phase 1 - Extract Turn Engine From API Route

Purpose:
- Move lifecycle ownership out of `turn/route.ts`.

New modules:
- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/run-logger.ts`
- `frontend/src/lib/harness/event-schema.ts`

Behavior:
- Route validates HTTP shape and opens SSE.
- Engine owns turn lifecycle and yields `UIEvent`.
- Engine writes turn-start and turn-end records.
- Current stub and Anthropic streaming behavior remains compatible.

Acceptance criteria:
- Existing Section 8 validation still passes.
- Unit tests can run `TurnEngine.runTurn()` without HTTP.
- A stream cancellation releases the turn lock and writes an interruption record.

### Phase 2 - Add Append-Only Session Events

Purpose:
- Make turns resumable and auditable.

New modules:
- `frontend/src/lib/harness/session-events.ts`
- `frontend/src/lib/harness/session-transcript.ts`

Behavior:
- Keep existing `session.json`.
- Add JSONL event stream.
- Record:
  - `turn.accepted`
  - `session.init`
  - `model.request.start`
  - `chat.delta`
  - `chat.complete`
  - `tool.*`
  - `turn.error`
  - `turn.complete`
  - `turn.cancelled`

Acceptance criteria:
- Accepted user input is persisted before the model call.
- Malformed JSONL lines do not break session listing.
- Tests verify event ordering.

### Phase 3 - Define Tool Contract And Registry

Purpose:
- Give `opts.tools` real meaning.

New modules:
- `frontend/src/lib/harness/tool-contracts.ts`
- `frontend/src/lib/harness/tool-registry.ts`
- `frontend/src/lib/harness/tool-pool.ts`

Initial tools:
- `read_file`
- `list_files`
- `write_file`
- `edit_file`
- `bash` only if permission policy exists

Acceptance criteria:
- Tool pool can be resolved from session, persona defaults, opts, and mode.
- Denied tools are removed before provider request construction.
- Tool descriptors are deterministic and test-covered.

### Phase 4 - Permission Policy Engine

Purpose:
- Prevent local tool execution from becoming a prompt-only safety problem.

New modules:
- `frontend/src/lib/harness/permission-policy.ts`
- `frontend/src/lib/harness/permission-rules.ts`

Behavior:
- Modes: `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, optional `bypass`.
- Rules: allow, deny, ask.
- Deny overrides everything.
- Tool permission decisions emit structured events.

Acceptance criteria:
- `dontAsk` denies unapproved write/bash.
- `readOnly` cannot write.
- Explicit deny blocks even if a session allow exists.
- Permission decisions are written to session events.

### Phase 5 - Local Tool Execution Loop

Purpose:
- Convert from plain message streaming to agentic model/tool turns.

New modules:
- `frontend/src/lib/harness/model-adapter.ts`
- `frontend/src/lib/harness/tool-executor.ts`
- `frontend/src/lib/harness/tool-result-store.ts`

Behavior:
- Build provider request with tools.
- Detect provider tool-use events.
- Validate tool input.
- Resolve permission.
- Execute local tool.
- Append tool result to the next model request.
- Continue until no tool calls or max turns reached.

Acceptance criteria:
- A read-file request can be completed through a model tool call.
- Tool execution events appear in SSE and session JSONL.
- Max turns stops runaway loops.
- Tool result truncation is deterministic.

### Phase 6 - Hooks

Purpose:
- Connect agent actions to Chirality workflow policy and provenance.

New modules:
- `frontend/src/lib/harness/hooks.ts`
- `frontend/src/lib/harness/builtin-hooks.ts`

Initial hooks:
- Block instruction root writes.
- Block symlink target writes.
- Enforce project root containment.
- Append provenance/run-record events after write or bash tools.

Acceptance criteria:
- Hook block produces `tool:permission` or `tool:error` event.
- Hook failures fail closed for writes.
- Hook events include duration.

### Phase 7 - Context Budgeting And Compaction

Purpose:
- Keep long sessions stable without losing audit records.

New modules:
- `frontend/src/lib/harness/context-window.ts`
- `frontend/src/lib/harness/compaction.ts`

Behavior:
- Estimate context.
- Preserve recent events.
- Summarize older transcript deterministically at first.
- Record compaction boundaries.

Acceptance criteria:
- Full transcript remains on disk.
- Model request can use compacted context.
- Tests verify recent turns are preserved.

### Phase 8 - Governed Subagent Runtime

Purpose:
- Extend existing subagent governance into real runtime support.

New modules:
- `frontend/src/lib/harness/subagent-runtime.ts`
- `frontend/src/lib/harness/subagent-store.ts`

Behavior:
- Use existing `evaluateSubagentGovernance`.
- Create subagent run record.
- Restrict tools and cwd.
- Stream progress to parent session.
- Persist output artifact.

Acceptance criteria:
- Delegation denied without governance metadata.
- Delegation allowed only to allowlisted TYPE 2 task agents.
- Parent transcript records child lifecycle.

## Proposed Module Map

```text
frontend/src/lib/harness/
  turn-engine.ts              # Main lifecycle owner
  model-adapter.ts            # Provider request/stream abstraction
  event-schema.ts             # Typed event versions and helpers
  run-logger.ts               # JSONL writer with redaction and rotation
  session-events.ts           # Append-only event API
  session-transcript.ts       # Conversation reconstruction and replay
  tool-contracts.ts           # Tool interfaces
  tool-registry.ts            # Built-in and future dynamic tool registry
  tool-pool.ts                # Filtering, ordering, permission exposure
  tool-executor.ts            # Tool execution orchestration
  tool-result-store.ts        # Large output persistence and preview
  permission-policy.ts        # Mode/rule decisions
  permission-rules.ts         # Rule parsing and matching
  hooks.ts                    # Hook interfaces and runner
  builtin-hooks.ts            # Project-root/instruction-root/provenance hooks
  context-window.ts           # Context selection
  compaction.ts               # Summary boundary handling
  subagent-runtime.ts         # Later
  subagent-store.ts           # Later
```

Keep existing modules:

- `types.ts`: split or re-export as contracts grow.
- `session-manager.ts`: keep summary/session index behavior.
- `options.ts`: keep option resolution, but feed `ToolPoolResolver`.
- `subagent-governance.ts`: keep as authoritative delegation gate.
- `attachment-resolver.ts`: keep and integrate with model adapter.
- `anthropic-agent-sdk-manager.ts`: either rename to `anthropic-model-adapter.ts` or wrap under the new engine.

## Suggested Event Schema

Current `UIEvent` is good for the browser, but the persisted run log should be richer.

Recommended persisted event shape:

```ts
type HarnessEvent = {
  schemaVersion: 1;
  eventId: string;
  sessionId: string;
  turnId?: string;
  parentEventId?: string;
  timestamp: string;
  type: string;
  data: Record<string, unknown>;
};
```

Map persisted events to UI events separately. This keeps the UI stable while allowing richer internal records.

Recommended event categories:

- `session.created`
- `session.resumed`
- `turn.accepted`
- `turn.started`
- `model.request.started`
- `model.delta`
- `model.completed`
- `tool.queued`
- `tool.permission`
- `tool.started`
- `tool.progress`
- `tool.completed`
- `tool.failed`
- `hook.started`
- `hook.completed`
- `context.compacted`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`

## Tool Runtime Design Notes

### Read Tools

Start with read tools because they exercise schema, permissions, result sizing, and events without high write risk.

`read_file`:
- Requires absolute or project-relative path.
- Resolves against session project root.
- Rejects symlinks initially.
- Rejects paths outside project root.
- Supports offset and limit.
- Never persists its own full output to a readable file by default, to avoid recursive read loops.

`list_files`:
- Uses bounded traversal.
- Supports depth and glob.
- Returns count plus capped entries.

### Write Tools

Add only after permission policy is in place.

`write_file`:
- Requires workspace-write permission.
- Rejects instruction root paths.
- Writes atomically where feasible.
- Emits before/after metadata.

`edit_file`:
- Requires exact old text.
- Rejects ambiguous replacements unless `replaceAll` is true.
- Emits a compact diff.

### Bash Tool

Add last among core tools.

Rules:
- Default deny in `dontAsk` and `readOnly`.
- Require explicit approval or allow rule.
- Use timeouts.
- Capture stdout/stderr separately.
- Persist large output.
- Detect common read-only commands only as UI hints, not as the only safety boundary.
- Network policy should be explicit and separate from shell classification.

Do not try to replicate the full `clawd-code` Bash security system. Build a smaller policy aligned with Chirality's engineering workflow.

## Permission Model Details

Recommended decision type:

```ts
type HarnessPermissionDecision =
  | { behavior: 'allow'; reason: string; source: string; updatedInput?: unknown }
  | { behavior: 'deny'; reason: string; source: string }
  | { behavior: 'ask'; reason: string; source: string; suggestions?: HarnessPermissionRule[] };
```

Decision order:

1. Tool exists and schema parses.
2. Tool validates input.
3. Deny rules.
4. Hook deny.
5. Mode constraints.
6. Allow rules.
7. Ask rules.
8. Tool-specific permission.
9. Optional UI prompt.

Do not let hook allow skip deny rules.

## Persona And Instruction Prompting

`persona-manager.ts` currently proves the persona exists and returns a short stub. The source review suggests the system prompt builder should become a first-class module.

Recommended behavior:

- Read active `AGENT_<persona>.md`.
- Read global `AGENTS.md`.
- Read required docs from instruction root as configured.
- Include mode-specific instructions.
- Include project root and safety boundaries.
- Include available tools after tool pool resolution.
- Compute boot fingerprint from actual prompt inputs, not only persona/mode.

Fingerprint inputs:

- Persona instruction content hash.
- Global instruction content hash.
- Mode.
- Tool names and versions.
- Project root policy version.
- Subagent governance policy version.

## Security And Safety Posture

The highest-value lesson is that safety should be a runtime architecture, not just prompt text.

Chirality should enforce:

- Project root containment.
- Instruction root isolation.
- Symlink rejection or explicit symlink policy.
- Atomic write where possible.
- Deny-first permission order.
- Explicit network allowlist.
- Secret redaction in logs and errors.
- Bounded output sizes.
- Turn-level cancellation.
- Max turns.
- Tool timeout.

Existing good foundation:
- Attachment symlink rejection.
- Anthropic API host allowlist.
- API key redaction.
- Project root cannot be instruction root.

Add next:
- Tool path policy shared by read/write/bash.
- Session event redaction.
- Tool output budget.

## Testing Strategy

Reuse the existing test culture. Add tests in narrow layers.

Unit tests:

- Tool schema parsing and validation.
- Tool pool filtering and deterministic order.
- Permission rule precedence.
- Project root path resolution.
- Hook deny and hook failure behavior.
- Tool result truncation.
- Session event append/replay.
- Context compaction preservation.

Integration tests:

- `/api/harness/turn` streams model text as before.
- Read-file tool call completes and emits tool events.
- Denied write under `dontAsk`.
- Allowed write under explicit session rule.
- Bash timeout.
- Stream interruption during model response.
- Stream interruption during tool execution.
- Session resume reconstructs prior transcript.

Validation script additions:

- `section9.tool_runtime_read_file`
- `section9.permission_rule_precedence`
- `section9.session_event_replay`
- `section9.tool_result_budget`
- `section9.context_compaction_boundary`

## Priority Recommendations

Highest priority:

1. Extract `TurnEngine`.
2. Add append-only session events.
3. Define tool contract and registry.
4. Add permission policy engine.
5. Add read-only tool execution.

Medium priority:

6. Add write/edit tools.
7. Add hook runner.
8. Add tool result storage.
9. Add context window manager.

Later:

10. Add bash.
11. Add subagent runtime.
12. Add deferred tool search.
13. Add MCP.
14. Add plugin-like extension points.

## Concrete First Development Slice

A good first future implementation slice:

Name:
- `Harness Turn Engine And Session Event Log`

Files likely touched:
- `frontend/src/lib/harness/types.ts`
- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/session-events.ts`
- `frontend/src/lib/harness/run-logger.ts`
- `frontend/src/app/api/harness/turn/route.ts`
- `frontend/src/__tests__/lib/harness-turn-engine.test.ts`
- `frontend/src/__tests__/lib/harness-session-events.test.ts`

Goal:
- Move lifecycle out of route and persist accepted turns before provider call.

Non-goals:
- No local tools yet.
- No permission engine yet.
- No subagent execution yet.

Acceptance criteria:
- Existing harness tests pass.
- Section 8 validation passes.
- Turn accepted event is written before first provider event.
- Stream cancellation writes cancellation event.
- Route code becomes mostly request parsing, lock handling, and SSE forwarding.

## Final Assessment

`clawd-code/` is most useful as evidence that mature agent harnesses are built around explicit runtime contracts, not just prompt assembly. Its strongest design lessons are:

- Tool contracts need to cover safety, UI, concurrency, and result semantics.
- Permission is a pipeline, not a boolean.
- Hooks are powerful but need fail-closed boundaries.
- Session persistence must happen before and during a turn, not only after success.
- Context management and output budgeting are core runtime features.
- Subagents need governance, identity, lifecycle, and records.

`claw-code-parity/` is most useful as a simplified lens. The Python side shows inventory and reporting scaffolding. The Rust side shows a cleaner small-core structure that Chirality can emulate: `Session`, `ConversationRuntime`, `PermissionPolicy`, `HookRunner`, `Compaction`, `ToolRegistry`.

For Chirality, the pragmatic path is not parity with either source tree. The right path is a Chirality-native harness that borrows the shape of the mature architecture while staying aligned with the app's local, professional, provenance-heavy workflow.
