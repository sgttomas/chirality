# Proposed Codex interactions

Status: owner approved all three additions AND native steering in the campaign
reply. The text below retains the reviewed scope and initial sequencing advice,
now superseded by that steering approval. Separate from already approved activity,
message formatting, quiet Plan refresh and Skills hiding. Design return by
HELPS_HUMANS gpt-6-astra medium; parent source review confirms the described
existing surfaces. No new interaction implementation is claimed.

Recommended release additions:

1. Put questions and approval requests in the conversation as one actionable
   card each, with the Plan panel linking to the same request. Retain option
   descriptions and free text. Collapse answered requests into readable history.
   Show a small chat-list indication when an answer is needed. Reconcile pending
   and resolved states after switching chats or reconnecting; a resolved request
   must never become actionable again. No new permission policy or notification
   centre.
2. Make delegated work readable in the existing conversation and Agents panel:
   assignment, actual working/waiting/finished/failed state, and returned result
   when available. Group by actual child thread identity. Completion of a spawn,
   wait or message tool call does not prove the child finished its assignment.
   No additional agent-management workspace.
3. Where the pinned supplier supplies plan-progress events, show an expandable
   work checklist beside the active response. Keep it distinct from saved Plan
   revisions and human acceptance. Reflect changed or unfinished steps truthfully
   in both live display and replay.

Separately, native steering would let a person submit a correction while work
runs. It requires a new Runtime/App operation bound to the active turn, clear
receipt, stale-target handling that preserves the draft, and uncertain-delivery
reconciliation. Recommend deferring this until after the above experience unless
the owner explicitly wants this additional cross-layer slice now. Stop remains
separate. Do not simply enable Send or silently queue a new turn.

Pin-specific protocol shapes are verified before implementation. The inspected
client uses stock 0.154.0; current online documentation alone cannot qualify a
feature. Existing question/approval components and full notification records
provide useful starting points. These are Chirality renderings of Codex protocol,
not embedded Codex desktop widgets. Only supplied reasoning summaries can be
shown; do not invent or claim hidden reasoning.

Existing Plan revision history, Revise/Execute/Run again/Save plan/Turn into
workflow actions and Stop are already implemented, so they are not counted as
new features. Child messaging, elaborate dashboards and configurable queues
remain outside this proposal.

Source anchors: frontend/src/components/shell/chat-panel.tsx (planning-question
suppression and disabled running composer), native-plan-panel.tsx,
request-card.tsx, permission-requests.tsx; Runtime core
delegated-engine-adapter.ts (collab call completion projection), daemon
codex-supervisor.ts (questions and interrupt), frontend turn-activity.ts.
