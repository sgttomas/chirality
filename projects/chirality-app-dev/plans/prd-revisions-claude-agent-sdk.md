# PRD Revisions to Adopt the Claude Agent SDK as the Harness Runtime

**Status:** Proposal — strategic/architectural changes to `docs/PRD.md` if vNext development pivots from a custom-built harness runtime to the Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`, formerly the Claude Code SDK).
**Date:** 2026-05-19
**Author:** working session
**Authority:** This document only proposes changes. The PRD remains authoritative until edited and reviewed. Higher-authority sources (`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, accepted decomposition, scope-change records) still control.

---

## 1. Why a revision is warranted

The current PRD (2026-05-20 revision) describes evolving the harness from a thin provider-streaming adapter into a Chirality-native agent runtime by **building** the following primitives in `frontend/src/lib/harness/`:

- `TurnEngine`, `SessionEvents` (append-only JSONL), `RunLogger`, `HarnessEvent` schema
- `ModelAdapter` with tool-use mapping
- `HarnessToolDescriptor`, `ToolRegistry`, `ToolPoolResolver`
- `PermissionPolicy` with deny/ask/allow and modes (`readOnly`, `workspaceWrite`, `dontAsk`, `ask`, optional `bypass`)
- `HookRunner` with before/after/failure hooks
- `ToolResultStore` with inline/preview/artifact policy
- `ContextWindowManager` with deterministic compaction
- `SubagentRuntime` with parent-child linkage and restricted tools
- Read/write/edit/bash tool implementations

The Claude Agent SDK already provides functional equivalents of every item on that list. It is embeddable in a Node/Electron host (`import { query } from '@anthropic-ai/claude-agent-sdk'`), exposes a streaming async-iterable interface that aligns one-to-one with the existing `IAgentSdkManager.startTurn()` contract in `frontend/src/lib/harness/types.ts`, and is programmable enough to enforce Chirality's specific invariants through hooks and tool-allowlists rather than through a custom-built runtime.

What the SDK does **not** provide is the Chirality-specific layer: instruction-root vs. working-root separation, governed subagent allowlisting (`evaluateSubagentGovernance`), `_STATUS.md` lifecycle authority, `Dependencies.csv` contract validation, scaffolding from decomposition markdown, persona-driven system prompt composition, professional-boundary copy/UX, working-root selection and validation, attachment resolution with per-turn budgets, working-root path containment, instruction-root write blocking, redaction policy, provenance/run-evidence appending, and the harness-level audit JSONL that mirrors SDK transcripts into the Chirality session layout.

A successful pivot keeps the entire **governance shell** (everything Chirality-specific) and replaces the **runtime spine** (everything generic) with SDK adoption. The PRD therefore needs to be revised so that:

- The runtime is described as **SDK-hosted**, with Chirality providing config, hooks, custom tools/MCP, persona prompt composition, audit mirroring, and governance.
- The runtime development sequence collapses: many R-phases stop being build phases and become **SDK-integration + Chirality-hook** phases.
- New cross-cutting constraints are added (notably `settingSources` isolation so the host SDK does not silently load `~/.claude/` settings into the harness).
- Several Known Gaps (KG-002 through KG-010) are reframed because the SDK closes most of them.

This proposal does not change Chirality's principles, non-goals, professional-boundary posture, or governed scope. It changes **how the runtime is implemented**, not **what the product is for**.

---

## 2. Summary of proposed PRD changes

| PRD section | Proposed change | Rationale |
|---|---|---|
| §2 Product Summary | Add a sentence: "Runtime spine is provided by the Claude Agent SDK; Chirality wraps it with governance, persona/instruction composition, permission/hook policy specific to Chirality invariants, and an append-only audit log under `.chirality/sessions/<id>/`." | Make the architectural choice explicit at the top of the document. |
| §3.1 Goals | Reframe goals 9–16. The product still owns a thin `TurnEngine`, audit JSONL, prompt builder, tool registry mapping, permission mapping, hook policy, and subagent allowlist gate — but as **SDK integration** rather than **from-scratch primitives**. | Goals should describe outcomes, not assume custom implementation. |
| §3.2 Non-Goals | Add: "Re-implement the agent loop, tool registry, permission policy, hook dispatch, subagent runtime, or context compaction when the Claude Agent SDK already provides them." Keep the rest. | Codify the build-vs-buy decision so future PRDs don't drift back. |
| §5 Product Principles | Add a new principle: "**SDK isolation.** When embedded, the harness must not load ambient user/global SDK settings (`~/.claude/`). Permission, hook, allowedTools, and persona configuration come from Chirality's instruction root and per-session options only." Strengthen principle 8 ("Routes stay thin") to specify "routes call a thin `TurnEngine` wrapper around the Agent SDK." | New principle prevents host-machine state from polluting the harness. |
| §6.1 In Scope — "New harness-runtime scope" | Rewrite the bullet list: keep the outcomes, drop the "build it" framing. See §3 below for the replacement list. | The current list reads like a build manifest; SDK adoption changes the verbs. |
| §6.4 Out of Scope | Add: "Re-implementing primitives that the Claude Agent SDK provides." | Discourages future drift. |
| §8.12 Turn Engine, Event Log, Runtime Event Schema | Keep all FR-070 through FR-077, but reframe acceptance text: `TurnEngine` becomes a thin orchestrator over `query()`; persisted events are mirrored from SDK message types into Chirality's `HarnessEvent` schema. | The product requirements (auditability, separate UI/runtime event contracts, replay, redaction) still hold; the implementation source changes. |
| §8.13 Tool Contract, Registry, Tool Pool, Model/Tool Loop | Rewrite. `opts.tools` maps to SDK `allowedTools`. The "tool contract" is the SDK's tool definition (built-in or custom via `tool()` / MCP). The tool pool resolver is configuration assembly, not custom execution. Initial built-ins (`read_file`, `list_files`, `write_file`, `edit_file`, `bash`) become SDK's `Read`, `Glob`/`LS`, `Write`, `Edit`, `Bash`, all enabled or denied via `allowedTools`/`disallowedTools` from day one rather than introduced in separate R-phases. Chirality-specific tools (status transitions, dependency-CSV writes, scaffold) ship as **MCP servers** registered through `mcpServers` config. | The original sequencing (read tools first, write later, bash last) is sensible as a **rollout / policy posture**, not as an implementation phasing — because the SDK ships all of them at once. The PRD should reflect that the gate is permission policy, not tool availability. |
| §8.14 Permission Policy and Hooks | Rewrite. Permission decisions come from SDK `permissionMode` + `allowedTools`/`disallowedTools` + a `canUseTool` callback (or `PreToolUse` hook) that implements Chirality's deny-first overlay. Chirality modes (`readOnly`, `workspaceWrite`, `dontAsk`, `ask`) map to SDK modes plus `disallowedTools` and a Chirality `canUseTool`. Hooks (FR-093–FR-095) become SDK `PreToolUse`/`PostToolUse`/`PostToolUseFailure` callbacks. | All acceptance criteria can be met via SDK config + hooks; no custom `HookRunner` required. |
| §8.15 Tool Result Storage, Context, Bash, Subagents, Extensibility | Mostly retained. Bash (FR-100) is no longer phased — it is gated by `disallowedTools` until policy work is complete. Subagents (FR-101/FR-102) use SDK's `agents` config; `evaluateSubagentGovernance` becomes a `PreToolUse` hook on the `Agent` tool that fails closed for non-allowlisted subagent names. MCP (FR-104) drops from "future" to "available from R3" because the SDK natively supports it and Chirality-specific tools are best implemented as MCP servers. | Reflects what the SDK actually enables and how Chirality's invariants are best layered in. |
| §9.3 SSE Event Contract | Unchanged in shape; reaffirm that the browser-facing event names are stable while the **mapper** between SDK message types (`SDKAssistantMessage`, `SDKResultMessage`, etc.) and `UIEvent` lives in the thin TurnEngine wrapper. | Public contract preservation is already a stated requirement; this just notes where the mapping code lives. |
| §9.4 Internal Runtime Interfaces | Shrink the list. Keep: `TurnEngine` (thin), `HarnessEvent`, `SessionEvents` (append-only JSONL mirror), `RunLogger`, `ChiralityCanUseTool` (deny-first overlay), `ChiralityHooks` (path containment, instruction-root protection, provenance, redaction). Remove from the "internal interfaces we build" list: `ModelAdapter`, `HarnessToolDescriptor`, `ToolRegistry`, `ToolPoolResolver`, `PermissionPolicy`, `HookRunner`, `ToolResultStore`, `ContextWindowManager`, `SubagentRuntime` — these are provided by the SDK and configured by Chirality. | The internal-interface inventory needs to match what we actually own. |
| §10.3 Session Store | Reconcile with SDK persistence. Proposal: SDK transcripts continue to be written by the SDK (under `~/.claude/projects/<encoded-cwd>/<sdk-session-id>.jsonl`); Chirality keeps `.chirality/sessions/<chiralitySessionId>/session.json` for harness-level metadata (projectRoot, persona, mode, model, bootFingerprint, **plus** `sdkSessionId` cross-reference) and `.chirality/sessions/<chiralitySessionId>/events.jsonl` as the Chirality audit mirror. Replay reconstructs from Chirality's JSONL primarily; SDK transcripts are the secondary, richer source. Optional: configure the SDK to point at a custom path via env/options if available; otherwise mirror. | The product requirement that "the full transcript stays on disk even after compaction" is met by either source; we make the canonical relationship explicit. |
| §10.4 Runtime Event Schema | Keep schema. Define the mapping from SDK message types to `HarnessEvent` types. | Schema is product-owned; the source of events is what changes. |
| §12.4 Section 9 Runtime Validation | Retain the validation IDs, retarget them: now they validate **SDK integration behavior plus Chirality hook behavior**, not custom-runtime behavior. E.g., `section9.permission_rule_precedence` validates that Chirality's `canUseTool` overlay denies even when SDK `permissionMode` would allow. | Test surface should reflect actual product responsibilities. |
| §13 Runtime Development Sequence | Major rewrite. See §4 below for the proposed replacement sequence. | Phasing collapses significantly; ordering changes; bash moves out of being its own phase. |
| §15 Known Gaps and Risks | Mark KG-002, KG-003, KG-004, KG-005, KG-006, KG-008, KG-009, KG-010 as **mitigated by SDK adoption pending implementation work**, with new residual risks added: (a) `settingSources` leakage risk, (b) SDK CLI subprocess packaging risk inside Electron asar, (c) SDK session-ID/path coupling risk on app upgrade, (d) compaction control surface is limited (PreCompact hook only — no knob for boundaries). | The risk register needs to track the new risks the pivot introduces. |
| §16 Execution Package Traceability | Update the runtime-roadmap table to match the new R-sequence (see §4 below). | Traceability summary must match the body. |

---

## 3. Replacement text for §6.1 "New harness-runtime scope"

Proposed list (replaces the existing bullet list under "New harness-runtime scope"):

- Adopt the Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) as the runtime spine, embedded in the Next.js server / Electron main process.
- Configure the SDK with `settingSources: ["project"]` (or `[]`) so ambient `~/.claude/` settings never modify harness behavior.
- Implement a thin `TurnEngine` wrapper around `query()` that:
  - resolves runtime options into SDK options (model, allowedTools, disallowedTools, hooks, mcpServers, agents);
  - composes the system prompt from instruction-root + active persona;
  - mirrors SDK message types into the `UIEvent` SSE contract;
  - persists `HarnessEvent`s to `.chirality/sessions/<id>/events.jsonl` in parallel with SDK's own transcript;
  - records `turn.accepted` before invoking `query()` so interrupted/killed turns leave recoverable evidence.
- Implement Chirality hooks as SDK hook callbacks:
  - `PreToolUse` enforces path containment (project root), blocks instruction-root writes, rejects symlink writes;
  - `PreToolUse` on the `Agent` tool gates subagent delegation via `evaluateSubagentGovernance` (fail closed);
  - `PostToolUse` appends provenance/run-evidence where policy requires;
  - `PreCompact` records compaction boundary in Chirality's audit JSONL;
  - `Stop` finalizes the terminal turn event.
- Implement a Chirality `canUseTool` overlay that imposes deny-first semantics regardless of SDK `permissionMode` (deny overrides allow).
- Define the Chirality → SDK permission mode mapping:
  - Chirality `readOnly` → SDK `permissionMode: "default"` + `disallowedTools: [Write, Edit, Bash, ...]` (or only read tools in `allowedTools`);
  - Chirality `workspaceWrite` → SDK `permissionMode: "acceptEdits"` + Chirality `canUseTool` enforcing containment;
  - Chirality `dontAsk` → SDK `permissionMode: "default"` + `canUseTool` denying without prompt for any action lacking explicit approval;
  - Chirality `ask` → SDK `permissionMode: "default"` + `canUseTool` returning `"ask"` for governed write/shell actions;
  - Optional local-only `bypass` → SDK `permissionMode: "bypassPermissions"` (developer-only; never default).
- Register Chirality-specific tools as MCP servers (in-process where appropriate):
  - status-transition tool that enforces `_STATUS.md` lifecycle rules and approval SHA capture;
  - dependency-CSV reader/writer for `Dependencies.csv` v3.1;
  - scaffold tool wrapping the existing scaffold service;
  - workspace scope/scan tool exposing the working-root introspection already implemented;
  - any future Chirality deterministic tool (validators, aggregators).
- Configure subagents via SDK `agents` config: Type 2 task agents are declared with restricted tool lists; the `Agent` tool is allowlisted only when governance pre-conditions are met.
- Replace `StubPersonaManager.buildSystemPrompt()` with a real composer that reads `agents/AGENT_<persona>.md` plus relevant governance content (DIRECTIVE/CONTRACT/SPEC/TYPES headers, working-root summary, mode policy) and produces the SDK `systemPrompt` / `appendSystemPrompt`.
- Map SDK `SDKResultMessage.session_id` into the Chirality `SessionRecord.sdkSessionId` field; resume uses both Chirality session record (for projectRoot/persona/mode/audit log) and SDK `resume: sdkSessionId`.
- Preserve the `UIEvent` shape exposed in `frontend/src/lib/harness/types.ts` and the SSE event names so the UI does not regress.
- Maintain Anthropic-only outbound network policy (NFR-003) at the renderer guardrail level; the SDK's API call lives on the Node side and follows `ANTHROPIC_API_KEY` resolution rules.

---

## 4. Replacement Runtime Development Sequence (§13)

Proposed replacement for sections **R0** through **R11**. The same outcomes are met; phases collapse and bash stops being its own phase because the SDK ships it from day one (gated by policy).

### R0 — Runtime Scope Confirmation (SDK-adoption decision)

Purpose: record the architectural decision and update governance documents.

Deliverables:
- `docs/harness/runtime_scope.md` — restate: Chirality owns governance, prompt composition, hooks, custom MCP tools, audit log, session linkage. The SDK owns: agent loop, built-in tools, permission framework, hook dispatch, subagent execution, MCP transport, session JSONL transcripts, context compaction.
- Updated `docs/harness/chirality_harness_graphs_and_sequence.md`.

### R1 — SDK Adoption, Thin TurnEngine, Persona Prompt Builder, Audit JSONL

Purpose: replace the current `AnthropicAgentSdkManager` direct-SDK path with an SDK-hosted runtime; preserve all existing tests, SSE events, and APIs.

Implementation targets:
- Add `@anthropic-ai/claude-agent-sdk` dependency.
- New `frontend/src/lib/harness/turn-engine.ts` exposing `runTurn(session, message, opts, contentBlocks)` returning `AsyncIterable<UIEvent>`, satisfying the existing `IAgentSdkManager` interface so the route does not change.
- New `frontend/src/lib/harness/sdk-options-builder.ts` mapping `ResolvedOpts` → SDK `Options`.
- New `frontend/src/lib/harness/session-events.ts` (append-only JSONL writer, replay reader).
- New `frontend/src/lib/harness/event-schema.ts` defining `HarnessEvent` and the SDK-message → `HarnessEvent` mapper.
- New `frontend/src/lib/harness/run-logger.ts` (redaction shared with provider/tool/audit paths).
- Replace `StubPersonaManager` with a real persona/system-prompt composer reading from instruction root and persona files.
- Update `runtime.ts` to wire the SDK-backed manager as the default in `anthropic` provider mode while preserving the stub path for tests.
- `settingSources` configured to `["project"]` (or `[]`); ambient `~/.claude/` ignored.
- `.chirality/sessions/<id>/session.json` extended with `sdkSessionId`.

Acceptance:
- All existing tests pass.
- Section 8 validation passes.
- `turn.accepted` persists before `query()` is invoked.
- Terminal success/failure/cancellation produce persisted `HarnessEvent`s.
- Route shape and SSE event names unchanged.
- No new tools exposed beyond what the current Anthropic SDK path exposed (effectively none — tools land in R2).

### R2 — Tool Surface (Permission-Gated Built-ins + First Custom MCP Tools)

Purpose: expose SDK built-in tools (Read, Glob, LS, Grep) and the first Chirality MCP tools, gated by permission policy.

Implementation targets:
- Define `ChiralityCanUseTool` — deny-first overlay; deny overrides allow.
- Map `opts.tools` (string array) to SDK `allowedTools`; unknown tool names produce structured validation errors.
- Register first Chirality MCP server(s): status reader/transition, dependency-CSV reader, scope scan exposed as MCP tools.
- Default `allowedTools` configuration for `readOnly` mode: SDK `Read`, `Glob`, `LS`, `Grep`, plus Chirality read-only MCP tools.

Acceptance:
- `opts.tools` validation errors are structured.
- Read-only tool calls execute through SDK and Chirality MCP.
- Denied tools never appear in the model's available tools.
- Tool calls produce `tool.queued`, `tool.permission`, `tool.started`, `tool.completed`, `tool.failed` events in JSONL and the existing `tool:result` SSE event for the UI.

### R3 — Write Surface and Chirality Hooks

Purpose: enable controlled writes through SDK `Write`/`Edit` plus Chirality MCP write tools (`Dependencies.csv` writer, `_STATUS.md` transition tool), guarded by `PreToolUse` containment hook.

Implementation targets:
- `PreToolUse` hook enforcing: write target under projectRoot; not under instruction root; no symlink writes initially.
- `PreToolUse` hook on Chirality MCP write tools enforcing schema and approval-SHA requirements (e.g., human-gate transitions).
- `PostToolUse` hook capturing diff/summary and writing provenance metadata.
- Map Chirality `workspaceWrite` mode to SDK `permissionMode: "acceptEdits"` + the containment hook.
- Map `dontAsk` to deny-write unless explicitly pre-approved via `allowedTools`.

Acceptance:
- Write outside project root denied.
- Write to instruction root denied.
- Symlink write rejected (initial policy).
- `_STATUS.md` transition requires approval SHA for human-gate states.
- Audit JSONL records `tool.permission` decisions for every write attempt.

### R4 — Bash, Tool Result Budgeting, Context Mirror

Purpose: unlock `Bash` (still default-denied), add result-size policy, mirror compaction boundaries.

Implementation targets:
- `Bash` added to allowed-tools list only for modes that explicitly permit it; `disallowedTools` lists it elsewhere.
- `PreToolUse` hook for `Bash` enforcing timeouts and capturing stdout/stderr separately.
- Tool-output budget enforcement in `PostToolUse`: inline if small, preview if medium, write artifact to `.chirality/sessions/<id>/artifacts/` if large.
- `PreCompact` hook records compaction boundary and summary metadata in audit JSONL.

Acceptance:
- `Bash` denied by default and in `readOnly`/`dontAsk`.
- Large outputs do not flood chat.
- Audit JSONL records `context.compacted` events with boundary metadata.
- Full transcript remains reconstructible from SDK transcript + Chirality JSONL even after compaction.

### R5 — Governed Subagent Runtime

Purpose: connect existing `evaluateSubagentGovernance` to SDK subagent execution.

Implementation targets:
- Declare Type 2 task subagents in SDK `agents` config with restricted tool lists.
- `PreToolUse` hook on the `Agent` tool calls `evaluateSubagentGovernance` and denies on any negative condition.
- Audit JSONL records `subagent.started`, `subagent.completed`, parent/child linkage, output artifact paths.

Acceptance:
- Delegation without governance metadata denied.
- Delegation to non-allowlisted or non-Type-2 candidates denied.
- Parent session records child lifecycle.

### R6 — Extensibility and MCP Boundaries

Purpose: catalog Chirality MCP servers, document the contract for adding new ones, define plugin boundaries.

Implementation targets:
- Tool catalog with descriptions, allowed modes, and write-scope notes.
- Naming convention for `mcp__chirality__*` tools.
- Documentation of how a future tool author registers an MCP server without bypassing hooks or permission overlay.

Acceptance:
- New MCP tools pass through the same permission engine and hooks as built-ins.
- Tool collisions prevented.
- No remote/plugin marketplace introduced (still out of scope).

### R7 — Domain Engine Profiles and Operation Proposals — Future Amendment

Purpose: unchanged. Domain engines remain future-scope; when adopted, they integrate as MCP servers or custom tool surfaces with protected paths and operation-proposal records.

Acceptance: unchanged from current PRD §13 R11.

### Phases removed or consolidated

- Old R2 (Prompt Builder and Model Adapter Boundary) is **absorbed into new R1** because the SDK is the model adapter; only the prompt builder needs implementation.
- Old R3 (Tool Contract and Tool Pool) becomes new R2 (configuration of SDK + first MCP tools).
- Old R4 (Permission Policy Engine) becomes the **`canUseTool` overlay in new R2/R3**; no separate phase needed.
- Old R5 (Model/Tool Loop) is **provided by the SDK**; the milestone becomes "first read tool actually executes through the SDK loop end-to-end with a Chirality audit event for every step", merged into new R2.
- Old R6 (Write/Edit Tools and Result Store) becomes **new R3** combined with hooks.
- Old R7 (Hooks and Context Management) **merges into new R3 (hooks) and new R4 (context mirror)**.
- Old R8 (Bash) becomes a single milestone inside **new R4** rather than its own phase.
- Old R9 (Subagent Runtime) becomes **new R5**.
- Old R10 (Deferred Tool Search, MCP, Plugin Boundaries) becomes **new R6**.
- Old R11 (Domain Engines) is preserved as **new R7**.

---

## 5. Section-by-section impact list (concise checklist)

- §1 Source Basis — add `@anthropic-ai/claude-agent-sdk` as an authoritative dependency reference.
- §2 Product Summary — add explicit statement that the runtime spine is the Claude Agent SDK.
- §3.1 Goals — reword goals 9–16 from "establish/build/implement X" to "configure SDK / wrap SDK / overlay Chirality policy on SDK X".
- §3.2 Non-Goals — add: "Re-implement SDK-provided primitives."
- §5 Principles — add: SDK isolation principle.
- §6.1 In Scope — replace "New harness-runtime scope" list (proposed text in §3 above).
- §6.4 Out of Scope — add: re-implementing SDK primitives.
- §7 User Journeys — no journey changes; acceptance text mentioning custom permission/tool runtime should be updated to reference SDK + Chirality overlay where it appears (7.4, 7.5, 7.8, 7.9, 7.10, 7.11).
- §8.4 (FR-027/028/029) — provider mode `anthropic` resolves to SDK-hosted path, not direct Anthropic SDK request streaming.
- §8.5 (FR-030–FR-035) — `ModelAdapter` no longer custom; provider error classification now wraps SDK errors.
- §8.12 (FR-070–FR-077) — keep requirements; reframe `TurnEngine` as a thin orchestrator and `HarnessEvent` as a mirror schema.
- §8.13 (FR-078–FR-086) — rewrite for SDK-hosted tools + Chirality MCP.
- §8.14 (FR-087–FR-095) — rewrite for SDK permission framework + Chirality `canUseTool` overlay + SDK hooks.
- §8.15 (FR-096–FR-105) — keep, retarget. Bash is no longer phased.
- §9.1 — no API endpoint changes.
- §9.3 — SSE contract preserved.
- §9.4 — shrink internal interfaces list to what Chirality actually owns.
- §10.3 — define Chirality vs SDK session-store relationship explicitly.
- §10.4 — define mapping rules from SDK message types to `HarnessEvent`.
- §10.5 — artifact storage unchanged.
- §11.1 — add NFR for SDK settings isolation (no ambient `~/.claude/` load).
- §12.4 — retarget Section 9 IDs.
- §13 — full rewrite to new R-sequence.
- §15 — mark KG-002–KG-006, KG-008–KG-010 as mitigated; add four new KGs (settingSources leakage, CLI subprocess packaging, session-path coupling on upgrade, compaction control surface).
- §16 — update runtime traceability table to match new R-sequence.

---

## 6. What does NOT change

- Authority rules in §1 (DIRECTIVE/CONTRACT/SPEC/TYPES and accepted execution scope remain higher authority than the PRD).
- All 21 K-* invariants in `docs/CONTRACT.md` and how they are honored as a product.
- Product principles 1–7 (filesystem-as-state, git event store, human authority, evidence, no hidden memory, instruction/working root separation) — these are reinforced, not weakened, by SDK isolation.
- Non-goals around binding approval, financial action, professional reliance.
- Workspace APIs, scaffolding API, working-root validation, file tree, scope scan, lifecycle/dependency contract APIs.
- Persona aliasing and selection model.
- Anthropic-only network policy at the renderer layer (NFR-003).
- API key handling (NFR-002), attachment policy (FR-036–FR-040), Section 8 validation surface, instruction-root integrity verification (FR-067), macOS arm64 release target.
- Domain Engine Profile future-scope framing.

---

## 7. Open questions to resolve before editing the PRD

These are governance/policy questions for the owner, not implementation details:

1. **Session storage canonicalization.** Two viable options: (a) Chirality JSONL is canonical and SDK transcript is a secondary/richer source; (b) SDK transcript is canonical and Chirality maintains only a `session.json` cross-reference. The first is more aligned with K-PROV and existing `.chirality/sessions/` layout; the second is simpler. Proposal: option (a).
2. **`settingSources` posture.** `["project"]` (load `.claude/settings.json` from the working root if present) versus `[]` (ignore all SDK settings files). The former allows per-project overrides; the latter is stricter. Proposal: `[]` for shipped builds, `["project"]` opt-in via env for development.
3. **MCP server hosting.** In-process SDK MCP via `createSdkMcpServer()` vs. out-of-process stdio MCP. In-process is simpler and avoids subprocess management. Proposal: in-process for all Chirality MCP tools.
4. **Bash default.** Currently the PRD makes bash a deferred phase. With SDK adoption it's "available but denied by default". Reaffirm that the user-facing posture is still "deny unless an explicitly-enabled mode requests it"? Proposal: yes.
5. **Subagent declaration source.** Type 2 agents are declared in `agents/AGENT_*.md`. The SDK `agents` config should be **generated** from those files at boot (with their `tools:` frontmatter list as the SDK tool restriction). Proposal: yes.
6. **Compaction control.** The SDK does not expose a deterministic compaction-boundary knob; we only get `PreCompact`. Are we comfortable that NFR-018 ("recent turns preserved verbatim") is met by the SDK's default behavior plus our recording of boundaries, without owning the compaction algorithm? Proposal: yes for now, with KG-NEW-COMPACTION tracking the residual risk.

---

## 8. Companion document

Implementation-level work (concrete file changes, dependency version pin, build/packaging considerations, test surface updates, migration sequencing) is captured in `plans/claude-agent-sdk-implementation-followups.md`.
