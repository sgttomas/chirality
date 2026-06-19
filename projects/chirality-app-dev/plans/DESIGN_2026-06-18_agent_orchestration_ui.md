# DESIGN — Agent-Orchestration UI & Information Architecture

- Date: 2026-06-18
- Status: LIVING DESIGN DOC (drives an incremental build; not a governed deliverable)
- Owner intent: the desktop app should be organized around **the abilities of the agent harness** — orchestration, feedback, input, and systematic control — **not** around the filesystem. The current UI is good and stays, but it is *tertiary*.

This document captures the target information architecture (IA), the honest current-vs-target gap (grounded in the real codebase), and the build sequence. It is the durable reference for the work that follows.

---

## 1. Reframing (decided with the owner)

The pivot: stop treating the filesystem (file tree, working-root path, file scope) as the skeleton of the UI. Organize the UI around what the harness can actually do. Nothing existing is deleted or removed — it is demoted to tertiary.

### Tier model (confirmed)

- **PRIMARY — the live loop.** The harness event stream (feedback) + the prompt (input) + permission / interrupt / governance (systematic control). This is what the app is *about*.
- **SECONDARY — run setup.** Assembling a run: persona, scope, opts/tools, provider. *Deferred phase:* this grows into agent+human **task management / workflow co-composition** (human-alone authoring → loose plan + ongoing Type-1 session → a composable, non-programmatic agent todo-list). It nucleates *thin* now via the sidebar's "workflow design" view; the full surface is a later phase.
- **TERTIARY — everything that exists today.** The agent matrix portal, PIPELINE, WORKBENCH, file tree, deliverable contracts/transitions, Tool Kit presets. Reachable, still working, not the focus.

### How the tiers connect

The PRIMARY (and later SECONDARY) screen carries a **collapsible multi-view sidebar**. That sidebar **is the normal modality** for reaching the tertiary screens — but it is not comprehensive of them. Tertiary screens, at minimum:

- an **evolved agent portal** (descended from today's matrix, not identical),
- a **direct chat with any agent persona**,
- a **document-editing-with-copilot** screen (the thing the owner thinks of as "the workflows page"),
- plus the existing PIPELINE / WORKBENCH / file tree.

---

## 2. Grounded current state (what the sweep + critic established)

A six-mapper sweep with an adversarial completeness critic mapped the real codebase. Critic-corrected facts (grep-verified against live source) are authoritative here.

1. **The harness already produces a rich event vocabulary; the UI throws most of it away.** `HARNESS_EVENT_TYPES` has **42** members (`tool.*`, `subagent.*`, `hook.*`, `model.*`, `context.compaction.*`, `interruption.*`, `branch.*`, `turn.*`, `queue.*`, `runtime.mirror.error`) — `event-schema.ts`. The mapper (`sdk-message-mapper.ts`) derives these from real SDK messages.
2. **Two channels, by design.**
   - **Live → browser: thin & provider-neutral.** `RunningHarnessTurn.events` is `AsyncIterable<UIEvent>` (`turn-engine.ts`). The public union has 7 members: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit` (`types.ts`). A conformance contract (`engine-conformance.ts` + `agent-engine-port.ts:PUBLIC_UI_EVENT_NAMES`) enforces this set, rejects provider-shaped event *names* (e.g. `sdk:delta`), and requires `process:exit` to be terminal. `RuntimeEngineContract.providerMetadataAllowed: true` — provider data is allowed in payloads.
   - **Persisted → disk: the rich truth.** Full `HarnessEvent`s are written to `.chirality/sessions/<id>/events.jsonl`, redacted, **replayable with typed summaries** (`session-events.ts`).
   - The bridge between them is **lossy**: the manager persists every `HarnessEvent` but only `yield`s the thin `uiEvents` (`claude-agent-sdk-manager.ts` loop). ~12 rich tool/subagent events collapse to a single thin `tool:result`.
3. **The rich stream lives under the `agentSdk` provider.** `resolveHarnessProviderMode` defaults to `stub` (`runtime.ts`); `stub`→`StubAgentSdkManager`, `anthropic`→`AnthropicAgentSdkManager`, `agentSdk`→`ClaudeAgentSdkManager` (the only one using the mapper). The provider badge in the UI is therefore load-bearing: it tells you whether you see the rich or thin stream. Ties to the pending **D-APP-18** default-provider cutover.
4. **Operator modes are real but un-surfaced and session-fixed.** `permission-overlay.ts` normalizes `readOnly` / `ask` (plan) / `workspaceWrite` (gated-write) / `bypass` (autonomous, env-gated `CHIRALITY_ALLOW_SDK_BYPASS=1`) / `dontAsk`, mapped to SDK permission modes in `sdk-options-builder.ts`. Network/danger tool classes are hard-denied in **all** modes. Two gaps: (a) mode is baked into the `SessionRecord` at session-create with no live switcher; (b) **`ask` currently resolves to DENY+escalation** — there is no human approve/deny pause UI, so `ask` is "deny-until-UI-built".
5. **The persona engine is ahead of the UI.** `persona-manager.buildSystemPrompt()` composes a full system prompt for **any of 38 agents** (`agents/AGENT_*.md`). But `chat-panel.resolvePersona()` exposes only 5 aliases and is **route-gated**: it honors `?agent=` only on `/workbench`; on `/pipeline` and `/` it hardcodes `WORKING_ITEMS`. "Direct chat with any persona" is a `resolvePersona` rewrite, not a dropdown.
6. **Known bug to fix during the portal evolution.** The matrix EVALUATIVE cells route `agent=DEPENDENCIES` and `agent=CHANGE`, which have no alias and resolve to invalid persona strings — those two cells do not work today.
7. **The session list data layer exists** (`/api/harness/session/list` + `sessionManager.list()`); only the UI is missing.
8. **The doc/copilot screen is greenfield — but not from zero.** No `/workflows`, `/documents`, `/editor` route (only `/`, `/pipeline`, `/workbench`). No content API for the four doc-type bodies (`Datasheet`/`Specification`/`Guidance`/`Procedure.md`). The "workflows page" the owner remembers is `/pipeline` (a task-launch form). However, `workbench` already reads file bodies (`_STATUS.md`, `Dependencies.csv`) via `deliverable-contracts.ts:readRequiredFile` → the status/dependencies APIs — that read pattern is the reuse path. `CoordinationMode` + scaffold templates (`scaffold.ts`) are a real, minimal coordination model (NOT dead code — the synthesis erred; the critic corrected it).

---

## 3. Target IA

### 3.1 Primary screen — the live loop

A single agent session is the unit. Left/main: the **live event stream** (operator messages, assistant prose, tool calls, subagent fan-out, hooks, permission gates, cost) rendered from the harness event vocabulary. The control points are inline: prompt input, interrupt, an operator **mode** selector (`read-only` / `plan` / `gated-write` / `autonomous`), and the `opts` chips (model, tools, maxTurns, subagentGovernance) promoted out of the hidden Tool Kit sidebar.

Gated actions surface as **approval cards** rather than blind forms: the agent proposes a `CHECKING`/`ISSUED` transition (which governance requires be `actor=HUMAN` + `approvalSha`, K-GATE-1) or a tool that needs permission, and the human approves/denies inline.

### 3.2 The collapsible multi-view sidebar (the keystone UX element)

Right side of the primary (and later secondary) screen. Tabbed views; the sidebar is the gateway to tertiary screens (each view can open its full-screen tertiary form). Honest data-source status:

| View | Data source | Status today |
|---|---|---|
| **Files** | `GET /api/working-root/tree` → `file-tree-panel.tsx` | **Live.** Lowest-effort: fold the existing left pane into a tab. |
| **Subagents** | `subagent.*` harness events + `ChildRunRecord` (`agent-runtime-contract.ts`), persisted to `events.jsonl` | Data real; **needs the event bridge** + UI. |
| **Tools** | `tool.*` harness events + evidence (`tool-evidence.ts`) + descriptors (`tool-descriptor.ts`) | Data real; stream shows final-only; **needs the event bridge** + UI. |
| **Document** | roster `GET /api/project/deliverables`; **no content endpoint** | Roster real; **needs content API + viewer** (shared with the doc-copilot tertiary). |
| **Workflow** | none (seed: `CoordinationMode` + scaffold templates) | **Greenfield.** Keep the peek thin; the full surface is the deferred secondary phase. |

### 3.3 Tertiary screens

| Screen | Route today | Evolution |
|---|---|---|
| Evolved agent portal | `/` (matrix) | Multi-lens home: matrix + persona omni-picker (38 agents) + direct-chat entry + session list (data exists). Fix broken EVALUATIVE cells. |
| Direct chat with any persona | none (proposed `/chat`) | Rewrite route-gated `resolvePersona`; independent mode selector; pass mode to `buildSystemPrompt`. |
| Document + copilot editor | none (proposed `/documents/[key]` or `/workbench/deliverable/[key]`) | Content API → markdown viewer (reuse `chat-markdown`) → editor → embedded scoped chat (`WORKING_ITEMS`) reusing the turn engine. |
| Pipeline | `/pipeline` | Stays the OPERATIVE launch surface; surface task-agent choice explicitly. |
| Workbench | `/workbench` | Stays the NORMATIVE/EVALUATIVE persona + contract surface; natural host for the embedded deliverable doc view. |

### 3.4 Operator modes (characterized by how tools are used)

`read-only` (safe tools auto, writes denied) · `plan/ask` (read auto, writes/shell pause for approval) · `gated-write` (read+shell+workspace-write under path/shell policy) · `autonomous` (env-gated bypass; Chirality hard-denies still apply). Network/danger classes hard-denied in all modes. Decisions to make: live switcher vs session-fixed; build the `ask` approval-pause UI.

---

## 4. The keystone — rich harness-event → UIEvent bridge

**Problem:** the live stream is lossy (12→1). Three of the five sidebar views (Subagents, Tools) and the live loop itself depend on the rich events that exist but never reach the browser.

**Decision: a filtered, redacted passthrough.** Add ONE provider-neutral public event type, `harness:event`, carrying the (redacted) `HarnessEvent`. The Claude SDK manager, which already persists every `HarnessEvent`, also `yield`s it as a `harness:event` UIEvent — *before* the thin `uiEvents` of the same SDK message, so the terminal `process:exit` stays last.

Rationale over per-type semantic events:
- **Live == replay.** The browser sees the same event shape that `events.jsonl` stores, so the console renders live *and* historical state with one renderer ("replay is free").
- **Minimal, stable contract surface.** One new public type instead of ~11; new harness event types flow to the UI automatically.
- **Contract-legal.** `harness:event` is a provider-neutral *name* (passes the conformance no-`sdk|claude|anthropic` check); `providerMetadataAllowed: true` sanctions provider fields in the payload.
- **Safe.** Bridged payloads are run through `redactJsonLike` (same as the persisted form).

Filtering: skip `model.delta` and `message.delta` (per-token text already covered by `chat:delta`) and `adapter.initialized` (redundant with `session:init`). Everything else passes through — tool lifecycle, subagent fan-out, hooks, permissions, context compaction, cost (`turn.completed`/`model.completed`), turn lifecycle.

Scope of increment 1: the `agentSdk` provider only (`ClaudeAgentSdkManager`). Manager-level lifecycle events emitted directly by the manager (`turn.accepted`/`turn.started`/`turn.cancelled`/`turn.failed`/`interruption.*`) stay persisted-only for now; the UI gets cost via the mapper's `turn.completed` and terminal/error state via the existing `turn:error`/`process:exit`. `AnthropicAgentSdkManager` parity is a follow-on. The existing thin `UIEvent`s remain for backward compatibility — `chat-panel` ignores unknown types, so nothing breaks.

Contract/test impact (all expected, all updated): add `harness:event` to `PUBLIC_UI_EVENT_NAMES`; update exact-sequence assertions in `claude-agent-sdk-manager.test.ts`, `engine-conformance.test.ts`, and `agent-sdk-dev-turn.test.ts`; new unit test `harness-ui-bridge.test.ts`. The stub-provider `routes.test.ts` and the mock-manager `turn-engine.test.ts` are unaffected.

---

## 5. Build sequence

1. **Event bridge (keystone, DONE — commit `64940ad65`).** `harness:event` passthrough → lights up the live loop + Subagents + Tools views under `agentSdk`. Additive, low-risk.
2. **Shell refactor (DONE).** Fixed 3-pane shell → event-loop + collapsible multi-view sidebar; fold the live file tree in as the "Files" tab; mount bridge-fed Subagents/Tools tabs.
   - **What shipped:** `WorkspaceSidebar` (`components/shell/workspace-sidebar.tsx`) — one collapsible, tabbed pane: Files (existing tree) · Tools · Subagents · Document (placeholder) · Workflow (placeholder) · Tool Kit. The Tool Kit folded from its former dedicated pane + "Show Tool Kit" checkbox into a tab (nothing deleted). A shared `HarnessEventsProvider` (`components/workspace/harness-events-provider.tsx`) buffers the live `harness:event` stream; the chat panel (producer) appends/clears it and the Tools/Subagents views (consumers) read it. Pure, DOM-free derivations (`lib/shell/harness-event-views.ts`) collapse the `tool.*` / `subagent.*` lifecycle into rows — so live and replay render identically.
   - **Transitional placement decision:** the sidebar evolves *in place from the current left file-tree pane* (lowest churn, keeps all three routes working with `children` still the main execution surface and Chat the live loop on the right). The design's eventual "sidebar on the right of the primary screen" assumes the later routing phase where main = the loop; that is the open decision in §6 (portal launch model) and is intentionally not forced here.
3. **Control: the permission pause + live mode switcher (DONE).** Make `ask` mode pause-and-approve and surface the operator mode selector.
   - **Decisions (owner):** live mode switcher (mode sent per-turn via `opts.mode`, no re-create) + inline approval cards in the live loop.
   - **What shipped:** the operator-mode selector lives in the chat panel and sends `opts.mode` (`readOnly`/`ask`/`workspaceWrite`/`bypass`) per turn — `opts.mode` is the single operator-mode lever (permission overlay + tool pool + persona posture + SDK `permissionMode`), resolved per turn (falls back to `session.mode`). When `canUseTool` resolves to `ask`, it suspends on a process-singleton **`PermissionBroker`** (keyed `sessionId+toolUseId`, 5-min auto-deny) and is released by `POST /api/harness/permission`; interrupt clears pending. Path/shell policy and hard-denies still evaluate **before** `ask`, so an operator can never approve a hard-denied tool.
   - **Key architecture note — the out-of-band channel.** `tool.permission` events are emitted by the permission overlay *while the SDK iterator is suspended* awaiting the verdict, so they are not part of the SDK message stream the mapper bridges. The manager therefore **merges a `SessionPermissionChannel` into its live stream** via `Promise.race(sdkNext, permNext)`, bridging permission events to the browser as `harness:event`s in real time (live == replay holds). Inline cards derive from that stream (`derivePermissionRequests`); approve/deny posts the verdict and the follow-up human event removes the card.
   - **Hardening applied (from adversarial review):** no addressable `toolUseID` → deny instead of an unreachable pending entry; the manager `finally` releases any pending broker entry (covers SSE-cancel/abort leaks beyond the interrupt path); inline-card transient state is pruned per turn; approval cards use `role=group` inside a labelled `role=region` (not multiple `alertdialog`s).
   - **Deferred hardening (Phase 3.1 backlog — review surfaced, not yet fixed):** (a) on interrupt the card is removed only on the next turn, not live; (b) navigating routes / changing the Working Root while an `ask` is pending nulls `activeSession`, so the card can't be actioned until the 5-min timeout (fix: capture `sessionId` per request); (c) `PermissionEventChannelRegistry.open` does not close a pre-existing same-session channel — currently safe under the one-active-turn lock.
4. **Document content API + viewer.** `GET /api/working-root/deliverable/content` (copy `readRequiredFile`) + markdown viewer (reuse `chat-markdown`). Serves both the Document sidebar view and the doc-copilot tertiary screen.
5. **Personas + evolved portal.** Rewrite route-gated `resolvePersona`; persona picker (38); fix the broken EVALUATIVE cells; direct-chat screen; session list UI.

The Workflow view stays a thin peek throughout; the full task-management surface is the deferred secondary phase.

---

## 6. Open decisions

- Live mode switcher vs session-fixed mode (mode is baked at session-create today).
- Where the `ask` approve/deny pause lives (inline in the loop vs the Tools sidebar view).
- Whether the live stream also tails `events.jsonl` for historical/replay state, or stays live-only.
- Document content API contract (stream vs batch; by doc-type; read-only vs editable) — shared by the sidebar view and the tertiary editor.
- Document editor tech: markdown-source (monaco/codemirror) vs WYSIWYG (prosemirror).
- Type-2 task-agent interaction in direct-chat: free chat vs INIT-TASK brief form vs restrict the picker to Type-0/Type-1.
- Portal launch model: matrix-cell `router.push` (today) vs in-place session provisioning.
- Whether to bridge manager-level turn-lifecycle events and `AnthropicAgentSdkManager` to `harness:event` (follow-on to increment 1).
