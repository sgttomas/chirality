# Chirality App Future Development Plan

Date: 2026-05-18

Status: Draft roadmap seed

Workspace: `chirality/projects/chirality-app-dev/`

Planning surface note: this plan intentionally lives in `chirality/plans/` during the migration phase. The current `chirality/plans/README.md` archival wording is stale for this use and should not be treated as authority for this document. After the migration settles, this plan may be promoted, superseded, or linked from the final roadmap authority.

Source: `chirality/projects/chirality-app-dev/plans/agent-harness-patterns-from-claw-code-assessment.md`

Next owner: Chirality App implementation planning in `chirality/projects/chirality-app-dev/`

## Summary

This plan defines the future development path for the Chirality App harness. It uses the local assessment in `chirality/projects/chirality-app-dev/plans/agent-harness-patterns-from-claw-code-assessment.md` as seed material, but it is not a parity plan and it must not reproduce leaked source, prompts, or implementation text.

The current Chirality App has a useful harness shell: typed API routes, session records, attachment validation, provider selection, subagent governance, and Section 8 validation scripts. The next development step is to turn that shell into a real agent runtime. The runtime should be local-first, auditable, permissioned, resumable, and aligned with Chirality's professional-work governance model.

The primary roadmap sequence is:

1. Establish a `TurnEngine`, append-only session event log, and durable runtime event schema.
2. Define a first-class tool contract, tool registry, and tool pool resolver.
3. Add a permission policy engine before any powerful local tools.
4. Add read-only tool execution, then write/edit tools.
5. Add hooks, tool result storage, context budgeting, and compaction.
6. Add bash, governed subagent runtime, deferred tool search, and MCP/plugin boundaries later.

## Current State

The app workspace already contains the relevant harness boundary:

- `frontend/src/lib/harness/types.ts` defines API-facing session, option, attachment, and `UIEvent` contracts.
- `frontend/src/app/api/harness/turn/route.ts` owns turn request handling, SSE streaming, turn locking, attachment warnings, option resolution, governance evaluation, and mid-stream error mapping.
- `frontend/src/lib/harness/session-manager.ts` persists session metadata JSON records.
- `frontend/src/lib/harness/options.ts` resolves model, tools, max turns, persona, mode, and subagent governance.
- `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` streams Anthropic text responses, handles interrupts, validates outbound API policy, and redacts configured API keys.
- `frontend/src/lib/harness/subagent-governance.ts` implements explicit delegation gates.
- `frontend/src/lib/harness/attachment-resolver.ts` provides careful local attachment validation.

The main architectural gap is that the harness is still mostly a provider streaming adapter. It does not yet have:

- an internal turn lifecycle engine,
- append-only transcript and run records,
- a model/tool loop,
- a tool registry and executable local tool contract,
- a general permission policy engine,
- hook execution,
- tool result storage,
- context window management,
- resumable runtime state,
- governed subagent execution records.

## Design Principles

Use these principles for all future implementation:

- Build Chirality-native runtime components. Do not chase feature parity with any external or leaked codebase.
- Keep routes thin. Routes parse HTTP, handle transport, and forward events; runtime services own behavior.
- Persist accepted user input before calling the model.
- Separate browser `UIEvent`s from richer persisted runtime events.
- Expose only permitted tools to the model.
- Enforce safety in runtime code, not only in prompt text.
- Deny rules override all allow decisions.
- Keep full transcript on disk even when model context is compacted.
- Treat subagents as governed runtime entities, not plain recursive prompts.
- Delay bash, MCP, plugin systems, and remote execution until the local runtime spine is reliable.

## Roadmap Phases

### Phase 1 - Turn Engine, Session Event Log, And Runtime Event Schema

Goal: create the runtime spine without changing the visible app behavior.

Planned capabilities:

- Add a `TurnEngine` that owns the harness turn lifecycle.
- Keep `/api/harness/turn` as an SSE transport adapter.
- Add append-only per-session runtime events.
- Add a run logger with secret redaction and stable event schema versioning.
- Persist `turn.accepted` before provider calls.
- Persist terminal outcomes for success, interruption, and failure.
- Preserve current stub and Anthropic provider behavior.
- Keep browser `UIEvent`s stable while persisting richer runtime records.

Target modules:

- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/session-events.ts`
- `frontend/src/lib/harness/run-logger.ts`
- `frontend/src/lib/harness/event-schema.ts`

Target persisted event shape:

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

Initial event types:

- `session.created`
- `session.resumed`
- `turn.accepted`
- `turn.started`
- `model.request.started`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`

Acceptance criteria:

- Existing Section 8 validation continues to pass.
- A unit test can run `TurnEngine.runTurn()` without HTTP.
- A killed or interrupted turn leaves a recoverable accepted-turn record.
- `/api/harness/turn` is reduced to request validation, turn locking, SSE forwarding, and error response handling.
- Runtime events can be replayed into a transcript view.
- Event JSONL tolerates malformed trailing writes without breaking session listing.

Later runtime event types, introduced by later phases:

- `tool.queued`
- `tool.permission`
- `tool.started`
- `tool.progress`
- `tool.completed`
- `tool.failed`
- `hook.started`
- `hook.completed`
- `context.compacted`
- `subagent.started`
- `subagent.completed`

### Phase 2 - Tool Contract And Tool Pool

Goal: make `opts.tools` meaningful and safe.

Planned interface target. This is a target shape for implementation planning, not a frozen public API:

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

Planned capabilities:

- Add a built-in tool registry.
- Add deterministic tool pool resolution from persona defaults, `opts.tools`, mode, and permission policy.
- Filter denied tools before provider request construction.
- Keep dynamic/MCP tools out of scope for the first version.

Initial tool set:

- `read_file`
- `list_files`

Next tool set:

- `write_file`
- `edit_file`

Deferred tool set:

- `bash`
- `tool_search`
- MCP-backed tools

Acceptance criteria:

- Tool order is deterministic.
- Unknown tool names produce structured validation errors.
- Denied tools are not sent to the model.
- Tool descriptors are covered by unit tests.

### Phase 3 - Permission Policy Engine

Goal: enforce local action safety before adding write or shell tools.

Planned decision target. This is a target shape for implementation planning, not a frozen public API:

```ts
type HarnessPermissionDecision =
  | { behavior: 'allow'; reason: string; source: string; updatedInput?: unknown }
  | { behavior: 'deny'; reason: string; source: string }
  | { behavior: 'ask'; reason: string; source: string; suggestions?: HarnessPermissionRule[] };
```

Planned modes:

- `readOnly`: read-only tools only.
- `workspaceWrite`: approved project-root writes allowed.
- `dontAsk`: deny actions not already allowed.
- `ask`: require UI confirmation for unknown writes.
- `bypass`: optional local-only escape hatch, not default.

Planned rule behavior:

- `deny` overrides every other source.
- `ask` requires confirmation unless a stronger deny applies.
- `allow` can be scoped by source, tool, and optional pattern.
- Rules carry source metadata: persona, project, session, or operator.

Acceptance criteria:

- `dontAsk` denies unapproved write or bash actions.
- `readOnly` cannot write.
- Explicit deny blocks a session allow.
- Permission decisions are emitted as runtime events.

### Phase 4 - Model/Tool Loop

Goal: support actual agentic tool use.

Planned capabilities:

- Convert provider tool-use events into internal tool requests.
- Validate tool input against tool descriptor schema.
- Run permission checks before execution.
- Execute local tools and append tool results to the next model request.
- Continue until completion or max turns.
- Emit browser UI events and persisted runtime events for each tool phase.

Execution order for each tool call:

1. Find descriptor.
2. Parse input.
3. Validate tool-specific constraints.
4. Resolve permission.
5. Execute.
6. Store or summarize result.
7. Append tool result to model context.
8. Emit completion or failure events.

Acceptance criteria:

- A read-file request can complete through model tool use.
- Tool results appear in SSE and persisted session events.
- Max-turn guard stops runaway loops.
- Interrupted tool execution emits a terminal cancellation event.

### Phase 5 - Write/Edit Tools And Result Storage

Goal: enable controlled file modification.

Planned write behavior:

- All paths resolve inside the active project root.
- Instruction root writes are blocked.
- Symlinks are rejected initially.
- Writes are atomic where practical.
- Edit operations require exact old content unless explicitly configured otherwise.
- Diffs or compact summaries are emitted as tool results.

Planned result storage:

- Inline small tool results.
- Preview medium or large results.
- Persist raw output under session artifacts.
- Store result metadata in runtime events.

Acceptance criteria:

- `write_file` cannot write outside project root.
- `edit_file` fails on ambiguous old content.
- Large outputs do not flood chat.
- Stored artifacts can be found from session event records.

### Phase 6 - Hooks

Goal: connect runtime actions to Chirality governance, provenance, and validation.

Initial hooks:

- `beforeToolUse`: enforce project-root containment.
- `beforeToolUse`: block instruction-root writes.
- `beforeToolUse`: reject symlink writes.
- `afterToolUse`: append provenance/run-record events.
- `onToolFailure`: record triage data for failed write or command tools.

Hook principles:

- Hooks are local and deterministic in the first version.
- Hook failures fail closed for write and shell tools.
- Hook input mutation is not allowed in the first version.
- Hook duration is recorded.

Acceptance criteria:

- Hook-denied tools do not execute.
- Hook outcomes are visible in persisted events.
- Hook failures produce structured errors.

### Phase 7 - Context Window And Compaction

Goal: support long sessions without losing auditability.

Planned behavior:

- Keep full append-only transcript on disk.
- Estimate context size before model requests.
- Preserve recent turns verbatim.
- Add deterministic summary boundaries for older context.
- Record compaction boundaries as runtime events.

Later behavior:

- Model-generated summaries with validation.
- Tool-result budget integration.
- Replay from compacted context plus full transcript.

Acceptance criteria:

- Full transcript remains available after compaction.
- Model context can be rebuilt from compacted state.
- Recent turns are preserved.
- Compaction is deterministic in tests.

### Phase 8 - Bash Tool

Goal: add shell execution only after permission, hooks, and result storage exist.

Planned behavior:

- Default deny in `readOnly` and `dontAsk`.
- Require explicit allow or interactive approval.
- Enforce timeout.
- Capture stdout and stderr separately.
- Persist large outputs.
- Emit progress and terminal events.
- Treat read-only command detection as a display hint, not the security boundary.

Acceptance criteria:

- Timeout terminates the command and records failure.
- Denied bash does not spawn a process.
- Large output is stored, previewed, and linked from events.
- Interrupt cancels running process when possible.

### Phase 9 - Governed Subagent Runtime

Goal: extend current subagent governance into executable runtime records.

Planned record target. This is a target shape for implementation planning, not a frozen public API:

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

Planned behavior:

- Keep `evaluateSubagentGovernance` as the authoritative gate.
- Allow only approved, allowlisted Type 2 task agents.
- Persist parent-child relationships.
- Restrict child tools and working directory.
- Stream child lifecycle to parent session.
- Store child output as an artifact.

Acceptance criteria:

- Delegation without governance metadata is denied.
- Delegation to non-allowlisted agents is denied.
- Parent session records child lifecycle and output path.

### Phase 10 - Deferred Tool Search, MCP, And Plugin Boundaries

Goal: add extensibility only after the local runtime is stable.

Deferred tool search:

- Add only when the tool catalog is large enough to justify it.
- Return only currently allowed deferred tools.
- Keep deterministic results.

MCP:

- Treat MCP tools as dynamic entries in the same tool registry and permission engine.
- Preserve server metadata in tool records.
- Prevent name collisions.
- Filter before model exposure.

Plugins:

- Treat plugins as out of scope until permission, hooks, tool registry, and event logging are mature.
- Prefer local skill/persona registries before plugin systems.

## Public Interfaces And Type Targets

The following are planned design targets, not immediate code changes and not frozen API contracts:

- `TurnEngine`: runtime owner for a single turn lifecycle.
- `HarnessEvent`: persisted runtime event schema.
- `HarnessToolDescriptor`: executable local tool contract.
- `HarnessPermissionDecision`: structured permission result.
- `HarnessSubagentRun`: governed child execution record.
- `UIEvent`: browser transport event that remains smaller than persisted runtime events.

Compatibility target:

- Existing `/api/harness/*` routes remain stable during Phase 1.
- Existing Section 8 validation remains the minimum regression gate.
- Existing stub provider remains available for deterministic tests.

## Test Strategy

Unit tests:

- Turn engine lifecycle without HTTP.
- Session event append and replay.
- Event schema serialization.
- Tool descriptor validation.
- Tool pool filtering and ordering.
- Permission rule precedence.
- Path containment and symlink rejection.
- Tool result storage thresholds.
- Hook allow, deny, and failure behavior.
- Context compaction boundaries.

Integration tests:

- `/api/harness/turn` streams as before after `TurnEngine` extraction.
- Accepted turn persists before provider response.
- Interrupt during model stream records cancellation.
- Read-file tool call completes through model/tool loop.
- Denied write under `dontAsk`.
- Allowed write with explicit rule.
- Bash timeout after Phase 8.
- Subagent governance denial and allowed child run after Phase 9.

Validation script additions:

- `section9.turn_engine_event_log`
- `section9.tool_runtime_read_file`
- `section9.permission_rule_precedence`
- `section9.tool_result_budget`
- `section9.context_compaction_boundary`
- `section9.subagent_lifecycle`

## Development Defaults

- Use `chirality/projects/chirality-app-dev/` as the app development workspace.
- Keep top-level `chirality/frontend/` as the public-export harness snapshot unless a separate export update is planned.
- Use `chirality/plans/` for this migration-phase forward plan.
- Do not revise `chirality/plans/README.md` as part of this plan.
- Keep the first implementation slice small: `TurnEngine`, session events, and run logger.
- Add local tools only after the turn engine and persisted event log exist.
- Add write/edit tools only after the permission engine exists.
- Add bash only after permission, hooks, and result storage exist.
- Add subagent execution only after parent turn records and tool permissions are stable.

## First Implementation Slice

Title: Harness Turn Engine And Session Event Log

Purpose:
- Establish a stable runtime spine without changing user-visible harness behavior.

Implementation targets:

- Add `TurnEngine` for lifecycle ownership.
- Add `session-events` for append-only JSONL records.
- Add `run-logger` for redacted structured logging.
- Refactor `/api/harness/turn` to call the engine and forward events.
- Preserve current provider behavior and existing `UIEvent` stream shape.

Acceptance criteria:

- Existing harness tests pass.
- Section 8 validation passes.
- `turn.accepted` is persisted before model request.
- Success, failure, and interruption terminal events are persisted.
- No local tool execution is introduced in this slice.

## Next Concrete Action

Create an implementation plan for the first slice, `Harness Turn Engine And Session Event Log`, inside `chirality/projects/chirality-app-dev/`. That implementation plan should identify the exact route refactor, event file layout, event writer API, replay behavior, tests, and Section 8 validation updates before any code changes begin.

## Non-Goals

- Do not reproduce or port any external source tree.
- Do not add a plugin system in the near term.
- Do not add MCP before the local tool registry and permission policy are complete.
- Do not add bash as the first tool.
- Do not rely on prompt instructions as the only safety boundary.
- Do not make root `frontend/` the long-term app-development source of truth.

## References

- Seed assessment: `chirality/projects/chirality-app-dev/plans/agent-harness-patterns-from-claw-code-assessment.md`
- App workspace: `chirality/projects/chirality-app-dev/`
- Current harness contracts: `chirality/projects/chirality-app-dev/frontend/src/lib/harness/types.ts`
- Current turn route: `chirality/projects/chirality-app-dev/frontend/src/app/api/harness/turn/route.ts`
- Current harness validation: `chirality/projects/chirality-app-dev/docs/harness/harness_manual_validation.md`
