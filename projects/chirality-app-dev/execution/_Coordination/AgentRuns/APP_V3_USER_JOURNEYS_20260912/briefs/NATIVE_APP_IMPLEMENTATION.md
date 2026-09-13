# TASK: native conversation experience

Type 2 gpt-6-astra medium, no delegation. Read Root/App AGENTS, TASK, PLAN,
NATIVE_INTERACTIONS_PROPOSAL (all approved, including steering), and
returns/NATIVE_PROTOCOL_MAPPING.md. Parent is direct baseline tester. Live
baseline reproduced concatenated distinct commentary/final text; file link to a
first-level artifact successfully opened native viewer. Plan refresh quieting
and a compact current-message activity display are explicitly approved.

Own frontend/src changes and directly affected tests for conversation message
identity/live/replay, approved native question/approval interaction, readable
children/checklist, native steering, quiet Plan refresh, and correct contained
workflow-file links. Exclude components/woven-dialogue/right-panel.tsx,
method-library-view.tsx, lib/woven-dialogue/woven-workspace-state.ts and
electron/main.ts, owned by library author. Request scope additions. No Runtime,
Root/instruction/catalog changes, Git mutations, builds, live UI/model/supplier
operations or protected state reads. Read-only Git is allowed.

Preserve typography/palette/one conversation, native Plan revision actions,
attachments/default-app PDF, view roots bound to retained transcripts, explicit
Stop, model/effort/permissions, and Activity sidebar. Remove the verbose composer
running banner. Put useful supplied progress at the current assistant item;
keep separate commentary and final boundaries and the same result on replay.
Use supplied summaries only, not hidden reasoning, guesses or percentages.
Quiet Plan background polling must not toggle manual Refresh's busy indicator.

Questions/approvals: one actionable conversation card, Plan panel can reference
it. Preserve answer descriptions/free text, resolved record, drafts where safe,
live status checks and reconnect. Small per-chat pending badges using existing
authorized session request listings; don't make historic pending rows actionable.
Do not widen permission or silently interrupt to navigate. If existing one-live-
conversation UI needs a broader change for cross-chat attention, raise concrete
scope/behavior choice before redesigning state ownership.

Children: readable task, actual native child state/result, expandable detail;
completed spawn/send/wait call is not completed assignment. Checklist uses native
turn/plan/updated, separate from saved plan revisions and acceptance. Projection
must use actual params thread/turn IDs, not parent routing envelope identity.

Runtime author will add SessionSteerRequest { operationId, expectedTurnId, text }
and SessionSteerResponse { operationId, turnId, status: accepted|rejected|unknown,
message?, providerTurnId? }. Expected ID is Runtime turn. App request carries
session identity through existing port routing, never arbitrary provider IDs.
Implement session /turn/steer route, harness-port adapters/client, composer update
action, acknowledgment/rejection/uncertainty presentation and preserved draft.
Do not auto resend after uncertain delivery or silently queue/start a new turn.
Parent will confirm exact exports once Runtime author returns interface details.

Workflow href hypothesis: catalog defaults depth 3 but canonical WORKFLOW.md is
at depth 4; retain containment/traversal safeguards and no arbitrary localhost-
URL conversion. Check actual path evidence before correcting link projection.

Focused tests exercise true behavioral changes and live/replay agreement, not
incidental UI wording. Coordinate interface gaps through parent. Return exact
files/checks and uncertainties. Parent integrates and obtains fresh full review.
