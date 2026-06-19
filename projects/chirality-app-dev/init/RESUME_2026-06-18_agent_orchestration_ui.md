# Resume — Agent-Orchestration UI redesign

Minimalist resume prompt for the next session. Continues an iterative UI/workflow design that pivoted the app to be organized around **harness abilities**, not the filesystem.

## Read first (source of truth)
`projects/chirality-app-dev/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` — target IA, grounded current-vs-target gap, keystone decision, and the 5-phase build sequence. Do not re-derive what's in there.

## One-line model
PRIMARY = live harness-event-stream loop + collapsible multi-view sidebar (Files / Subagents / Tools / Document / Workflow). SECONDARY = run setup → later task-management phase (deferred). TERTIARY = all current UI (matrix portal, pipeline, workbench, file tree) — kept, reachable via the sidebar, not the focus.

## Done
- **Phase 1 keystone** (committed `64940ad65`, pushed) — rich `harness:event` passthrough bridging the persisted `HarnessEvent` vocabulary to the live UIEvent stream under the `agentSdk` provider. Files: `lib/harness/{types,agent-engine-port,harness-ui-bridge,claude-agent-sdk-manager}.ts` + tests.
- **Phase 2 shell refactor** (committed `94335d08e`, pushed) — `app-shell.tsx` left pane is `WorkspaceSidebar`: one collapsible tabbed pane (Files · Tools · Subagents · Document · Workflow · Tool Kit) with the WAI-ARIA tabs pattern; active tab lifted to AppShell. `HarnessEventsProvider` split into stable actions + data contexts; views memo-derive via pure `lib/shell/harness-event-views.ts`. Sidebar transitionally on the LEFT (DESIGN §5.2). Hardened against a 12-finding review.
- **Phase 3 permission pause + live mode switcher** (committed `3f5eac37e`, pushed) — operator-mode selector in the chat panel sends `opts.mode` per turn (live switch; `opts.mode` is the single operator-mode lever for permissions/tool-pool/persona/SDK mode). `ask` now suspends `canUseTool` on the singleton `PermissionBroker` (keyed `sessionId+toolUseId`, 5-min auto-deny) until `POST /api/harness/permission`; hard-denies + path/shell policy gate before `ask`. Because `tool.permission` events fire while the SDK iterator is suspended, the manager **merges a `SessionPermissionChannel`** into its live stream via `Promise.race` so they bridge live as `harness:event`s; inline cards (`permission-requests.tsx`) derive from the stream. 4 review findings fixed; 3 deferred to a Phase 3.1 backlog (DESIGN §5.3). Full typecheck + 422 tests green.

## Phase 3.1 hardening (DONE — committed `01dbcf778`, pushed)
Cleared the deferred backlog + an identity-guard race an adversarial review surfaced (DESIGN §5.3): (a) cards hide on turn-end via `PermissionRequests active={isRunning}` + pure `selectPendingPermissionRequests`; (b) each `PermissionRequestRow` carries its own `sessionId` so a pending approval survives navigation; (c) `open()` closes a pre-existing same-session channel. Plus **identity-guarded teardown** — registry `close(sessionId, channel?)`, broker `clearSession(sessionId, verdict, turnToken?)`, and `activeTurns.delete` are scoped to the owning turn's `AbortController`/channel instance, closing a TOCTOU race on the SSE-cancel path.

## Owner rulings on the §6 open decisions (2026-06-19, all RULED — committed `bd253da64`, pushed)
Six decision packets prepared + ruled (records + `_REGISTER.md` under `execution/_Coordination/_DECISIONS/`): **D-APP-20** content API → read-only batch, relative-path-within-deliverable (Option B); **D-APP-21** editor → defer, CodeMirror markdown-source later; **D-APP-22** loop history → live-only now, hydrate-on-open with Phase 5; **D-APP-23** portal → hybrid (routes + loop-first entry, sidebar right only for that surface); **D-APP-24** direct chat → restrict picker to Type-0/Type-1, INIT-TASK brief later; **D-APP-25** bridge → **both** manager-lifecycle events + AnthropicManager parity (bounded tranche).

## Phase 4 document content API + viewer (DONE — committed `91c28682a`, pushed)
Per D-APP-20 Option B: `readDeliverableContent` + `GET /api/working-root/deliverable/content?projectRoot&deliverablePath&file` (read-only; `file` validated inside the canonical deliverable dir via lexical + post-realpath re-check, typed-404 stat guard) + `DocumentView` sidebar tab reusing `chat-markdown`, body-state via pure `lib/shell/document-view-state.ts`. Hardened against a 7-finding review. Typecheck clean, 452 tests.

## D-APP-25 bridge tranche (DONE — committed `a6c63f530`, pushed)
Manager-lifecycle bridging + Anthropic parity, bounded tranche. **Claude manager:** `turn.accepted`/`turn.started` bridge via a buffer flushed immediately after the first `session:init` (keeps `session:init` first so an early interrupt never drops it — the conformance harness interrupts after the first yielded event); `interruption.completed`/`turn.cancelled`/`turn.failed` bridge in place via a local `emitAndBridge`; mapper events not double-bridged. **Anthropic manager:** persists + bridges the same lifecycle vocab via the shared `harnessEventToUiEvent` (emits `session:init` first, so no buffer); `interruption.requested` persisted-only; `lifecycleOpened` gate keeps bootstrap lifecycle-free; catch cascade byte-identical to prior throw precedence; identity-guarded `activeTurns` teardown added for parity. Tests isolate `CHIRALITY_SESSION_ROOT` for the new persistence. Contract held: one public type (`harness:event`), `process:exit` terminal, redaction via `harnessEventToUiEvent`/`redactJsonLike`. Adversarially reviewed (37 agents; constraints 1–4 PASS; sole actionable finding — Anthropic identity guard — applied). Files: `lib/harness/{claude-agent-sdk-manager,anthropic-agent-sdk-manager}.ts` + 4 updated test files (claude/anthropic manager, engine-conformance, agent-sdk-dev-turn) with 2 new Anthropic parity tests. Typecheck clean, **454 tests**.

## Next — Phase 5
**Phase 5** (personas + hybrid portal per D-APP-23/24/22): rewrite route-gated `resolvePersona`; persona picker (restricted to Type-0/Type-1, D-APP-24); hybrid portal launch (routes + loop-first entry, sidebar right only there, D-APP-23); session-list with hydrate-on-open from `replayHarnessEvents` (D-APP-22); fix the broken EVALUATIVE cells. Note: an architectural asymmetry remains by design — the Claude manager does not emit `session:init` on a pre-init failure (the SDK hasn't reported a session yet) while the Anthropic manager synthesizes `session:init` up front; this is not a contract violation (the throw path yields `turn:error`+`process:exit` at the turn-engine) and was deliberately not "fixed" (would change Claude behavior + break tests).

## Must-not-break facts
- Public UIEvent contract is enforced by `engine-conformance.ts` + `PUBLIC_UI_EVENT_NAMES`; `process:exit` must stay the terminal event; provider-shaped event *names* are rejected (payload metadata is allowed).
- Rich events only flow under `agentSdk` (default provider is `stub`) — ties to pending D-APP-18.
- `harness:event` payloads are redacted; keep it that way.
- Permission plane: hard-denies + path/shell policy MUST evaluate before `ask` (an operator can never approve a hard-denied tool); `PermissionBroker` / `SessionPermissionChannel` are process singletons; the manager merge must keep `process:exit` last.
- **Shared repo / foreign changes:** a separate "Codex" agent and a heavy embeddings-DB build run concurrently in this repo. Do NOT commit files you didn't author — known strays: `tools/retrieval/build_source_index.py`, `projects/chirality-app-dev/plans/ASSESSMENT_2026-06-18_pi_rust_sdk_*.md`, anything under `projects/chirality-piping/`. Always stage explicitly (`git add projects/chirality-app-dev`) then `git diff --cached --name-only` and unstage strays before committing. Commits go to `main`; commit/push only when the owner asks.

## Verify before resuming
From `projects/chirality-app-dev/frontend`: `npx vitest run` (expect 454 pass) and `npm run typecheck` (expect exit 0).

## Open decisions
All §6 open calls are now RULED (D-APP-20..25 above). Remaining design latitude lives inside those rulings' "later" follow-ons (editable editor, hydrate-on-open, INIT-TASK brief, full loop-first pivot).

## Session status (2026-06-19)
All work committed + pushed; `main` in sync with `origin/main`, working tree clean. This session landed Phase 3.1 (`01dbcf778`), D-APP-20..25 rulings (`bd253da64`), Phase 4 document content API + viewer (`91c28682a`), and the **D-APP-25 bridge tranche** (`a6c63f530` — two managers + 4 test files + DESIGN; this resume refresh in the follow-up commit). D-APP-25 was adversarially reviewed (37 agents; constraints 1–4 PASS; one finding applied — Anthropic identity guard). Typecheck clean, **454 tests**. **Next: Phase 5** (personas + hybrid portal per D-APP-23/24/22).
