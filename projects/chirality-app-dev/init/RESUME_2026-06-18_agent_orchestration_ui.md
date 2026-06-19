# Resume — Agent-Orchestration UI redesign

Minimalist resume prompt for the next session. Continues an iterative UI/workflow design that pivoted the app to be organized around **harness abilities**, not the filesystem.

## Read first (source of truth)
`projects/chirality-app-dev/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` — target IA, grounded current-vs-target gap, keystone decision, and the 5-phase build sequence. Do not re-derive what's in there.

## One-line model
PRIMARY = live harness-event-stream loop + collapsible multi-view sidebar (Files / Subagents / Tools / Document / Workflow). SECONDARY = run setup → later task-management phase (deferred). TERTIARY = all current UI (matrix portal, pipeline, workbench, file tree) — kept, reachable via the sidebar, not the focus.

## Done (committed `64940ad65`, on `main`, not pushed)
Phase 1 keystone — rich `harness:event` passthrough bridging the persisted `HarnessEvent` vocabulary to the live UIEvent stream under the `agentSdk` provider. Files: `lib/harness/{types,agent-engine-port,harness-ui-bridge,claude-agent-sdk-manager}.ts` + tests. Full typecheck + 387 tests green.

## Next — Phase 2: shell refactor
Turn the fixed 3-pane shell (`components/shell/app-shell.tsx`) into the event-loop + collapsible multi-view sidebar. Fold the live file tree in as the "Files" tab; add Subagents and Tools tabs that render the now-bridged `harness:event` stream (consume it in `components/shell/chat-panel.tsx` / a new event-stream renderer — today it ignores unknown types). See DESIGN §3.2 and §5.

## Must-not-break facts
- Public UIEvent contract is enforced by `engine-conformance.ts` + `PUBLIC_UI_EVENT_NAMES`; `process:exit` must stay the terminal event; provider-shaped event *names* are rejected (payload metadata is allowed).
- Rich events only flow under `agentSdk` (default provider is `stub`) — ties to pending D-APP-18.
- `harness:event` payloads are redacted; keep it that way.
- Don't touch unrelated dirty files under `projects/chirality-piping/`.

## Verify before resuming
From `projects/chirality-app-dev/frontend`: `npx vitest run` (expect 387 pass) and `npm run typecheck` (expect exit 0).

## Open decisions (owner's call — see DESIGN §6)
Live mode-switcher vs session-fixed; where the `ask` approve/deny pause lives; document content-API contract; editor tech (markdown-source vs WYSIWYG); whether to also bridge manager-level turn-lifecycle events + the Anthropic manager.
