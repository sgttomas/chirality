# Resume — Agent-Orchestration UI redesign

Minimalist resume prompt for the next session. Continues an iterative UI/workflow design that pivoted the app to be organized around **harness abilities**, not the filesystem.

## Read first (source of truth)
`projects/chirality-app-dev/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` — target IA, grounded current-vs-target gap, keystone decision, and the 5-phase build sequence. Do not re-derive what's in there.

## One-line model
PRIMARY = live harness-event-stream loop + collapsible multi-view sidebar (Files / Subagents / Tools / Document / Workflow). SECONDARY = run setup → later task-management phase (deferred). TERTIARY = all current UI (matrix portal, pipeline, workbench, file tree) — kept, reachable via the sidebar, not the focus.

## Done
- **Phase 1 keystone** (committed `64940ad65`, pushed) — rich `harness:event` passthrough bridging the persisted `HarnessEvent` vocabulary to the live UIEvent stream under the `agentSdk` provider. Files: `lib/harness/{types,agent-engine-port,harness-ui-bridge,claude-agent-sdk-manager}.ts` + tests.
- **Phase 2 shell refactor** (uncommitted on `main`) — `app-shell.tsx` left pane is now `WorkspaceSidebar`: one collapsible tabbed pane (Files · Tools · Subagents · Document · Workflow · Tool Kit) implementing the WAI-ARIA tabs pattern (roving tabindex, arrow nav, tabpanel); active tab lifted to AppShell so it survives collapse. Tool Kit folded from a dedicated pane + checkbox into a tab. `HarnessEventsProvider` split into stable actions + data contexts (producer doesn't re-render on appends); chat panel appends/clears via the actions hook; `ToolStreamView`/`SubagentStreamView` memo-derive via pure `lib/shell/harness-event-views.ts` (subagent rows keyed by `taskId`, tool summary-completions folded onto preceding rows). Sidebar placed transitionally on the LEFT (main = route `children`, Chat = live loop on right) — see DESIGN §5.2. Hardened against a 12-finding adversarial review. Full typecheck + 401 tests green.

## Next — Phase 3: the permission pause + operator mode selector
Make `ask` mode pause-and-approve. Needs the bridge's `tool.permission` event surfaced as an inline approval card + a decision channel back to the SDK (today `ask` resolves to DENY — see DESIGN §2.4 and §3.4). Then surface the session-fixed operator mode selector (open decision §6: live switcher vs session-fixed). See DESIGN §5.3.

## Must-not-break facts
- Public UIEvent contract is enforced by `engine-conformance.ts` + `PUBLIC_UI_EVENT_NAMES`; `process:exit` must stay the terminal event; provider-shaped event *names* are rejected (payload metadata is allowed).
- Rich events only flow under `agentSdk` (default provider is `stub`) — ties to pending D-APP-18.
- `harness:event` payloads are redacted; keep it that way.
- Don't touch unrelated dirty files under `projects/chirality-piping/`.

## Verify before resuming
From `projects/chirality-app-dev/frontend`: `npx vitest run` (expect 401 pass) and `npm run typecheck` (expect exit 0).

## Open decisions (owner's call — see DESIGN §6)
Live mode-switcher vs session-fixed; where the `ask` approve/deny pause lives; document content-API contract; editor tech (markdown-source vs WYSIWYG); whether to also bridge manager-level turn-lifecycle events + the Anthropic manager.
