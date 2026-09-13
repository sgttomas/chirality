# TASK: questions from another active chat

Type 2, gpt-6-astra medium, no delegation. Read active checkout Root/App
AGENTS, agents/AGENT_TASK.md, this campaign PLAN and approved native-interaction
proposal. Parent is direct App tester. This assignment completes the approved
per-chat needs-answer indication without changing conversation ownership.

Own the workspace navigator and woven-dialogue-shell.tsx attention integration,
new narrowly scoped attention components/hooks if necessary, and their focused
tests. Do not edit chat-panel.tsx, request-card.tsx, permission-requests.tsx,
native-plan-panel.tsx, Runtime, right-panel.tsx, method-library-view.tsx, or
Electron. Other authors own those. Coordinate through parent. No Git mutations,
builds, supplier/UI/model operations, protected live-state access, or publication.

Current App disables chat navigation while a turn is running. Preserve that
ownership boundary. A needs-answer control on another chat opens a compact
dialog/popover titled with that chat and containing its live request card;
answer through its own existing session routes, without interrupting or
navigating away from the selected running conversation. For the selected chat,
direct attention to its inline request anchor, requests-${sessionId}. Do not
create another transcript surface or an active-work detach/resume architecture.

Reuse native App author's exports in components/shell/request-card.tsx:
LiveSessionRequests({sessionId, active=true, showHistory=true}); cross-chat
dialog uses showHistory=false. useLiveSessionRequests(sessionId,active) yields
ServerRequestRow[]; RequestCards can consume known requests. Questions are
identified by session plus request ID and revalidated before submission.
Do not present historical pending records as actionable. Avoid two polling
loops per open request, polling every historical chat, or one failed request
discarding other chats' attention state. Use existing live/running-session
information and a bounded cleanup-aware refresh as appropriate. If no truthful
efficient attention source exists, report the concrete gap before widening scope.

Keep the primary UI minimal, accessible names and keyboard/focus behavior intact.
Tests must cover answering a second chat while the first continues, correct
session routing, resolved/stale requests, cleanup and no accidental Stop.
Run APP-HOLD-1 for affected deliverables and record concise return with exact
files/checks and remaining limitations. Fresh full review belongs to parent.
