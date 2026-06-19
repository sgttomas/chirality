# Resume — Agent-Orchestration UI redesign

Minimalist resume prompt for the next session. Continues an iterative UI/workflow design that pivoted the app to be organized around **harness abilities**, not the filesystem.

## Read first (source of truth)
`projects/chirality-app-dev/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` — target IA, grounded current-vs-target gap, keystone decision, and the 5-phase build sequence. Do not re-derive what's in there.

## One-line model
PRIMARY = live harness-event-stream loop + collapsible multi-view sidebar (Files / Subagents / Tools / Document / Workflow). SECONDARY = run setup → later task-management phase (deferred). TERTIARY = all current UI (matrix portal, pipeline, workbench, file tree) — kept, reachable via the sidebar, not the focus.

## Done
- **Phase 1 keystone** (committed `64940ad65`, pushed) — rich `harness:event` passthrough bridging the persisted `HarnessEvent` vocabulary to the live UIEvent stream under the `agentSdk` provider. Files: `lib/harness/{types,agent-engine-port,harness-ui-bridge,claude-agent-sdk-manager}.ts` + tests.
- **Phase 2 shell refactor** (committed `94335d08e`, pushed) — `app-shell.tsx` left pane is `WorkspaceSidebar`: one collapsible tabbed pane (Files · Tools · Subagents · Document · Workflow · Tool Kit) with the WAI-ARIA tabs pattern; active tab lifted to AppShell. `HarnessEventsProvider` split into stable actions + data contexts; views memo-derive via pure `lib/shell/harness-event-views.ts`. Sidebar transitionally on the LEFT (DESIGN §5.2). Hardened against a 12-finding review.
- **Phase 3 permission pause + live mode switcher** (uncommitted on `main`) — operator-mode selector in the chat panel sends `opts.mode` per turn (live switch; `opts.mode` is the single operator-mode lever for permissions/tool-pool/persona/SDK mode). `ask` now suspends `canUseTool` on the singleton `PermissionBroker` (keyed `sessionId+toolUseId`, 5-min auto-deny) until `POST /api/harness/permission`; hard-denies + path/shell policy gate before `ask`. Because `tool.permission` events fire while the SDK iterator is suspended, the manager **merges a `SessionPermissionChannel`** into its live stream via `Promise.race` so they bridge live as `harness:event`s; inline cards (`permission-requests.tsx`) derive from the stream. 4 review findings fixed; 3 deferred to a Phase 3.1 backlog (DESIGN §5.3). Full typecheck + 422 tests green.

## Next — Phase 4: document content API + viewer
`GET /api/working-root/deliverable/content` (copy `deliverable-contracts.ts:readRequiredFile`) + a markdown viewer reusing `chat-markdown`; serves the sidebar Document tab and the doc-copilot tertiary screen (DESIGN §3.2, §5.4). Optionally first clear the Phase 3.1 deferred-hardening backlog in DESIGN §5.3.

## Must-not-break facts
- Public UIEvent contract is enforced by `engine-conformance.ts` + `PUBLIC_UI_EVENT_NAMES`; `process:exit` must stay the terminal event; provider-shaped event *names* are rejected (payload metadata is allowed).
- Rich events only flow under `agentSdk` (default provider is `stub`) — ties to pending D-APP-18.
- `harness:event` payloads are redacted; keep it that way.
- Don't touch unrelated dirty files under `projects/chirality-piping/`.

## Verify before resuming
From `projects/chirality-app-dev/frontend`: `npx vitest run` (expect 422 pass) and `npm run typecheck` (expect exit 0).

## Open decisions (owner's call — see DESIGN §6)
Live mode-switcher vs session-fixed; where the `ask` approve/deny pause lives; document content-API contract; editor tech (markdown-source vs WYSIWYG); whether to also bridge manager-level turn-lifecycle events + the Anthropic manager.
