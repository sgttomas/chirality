# Concept 1 — Dialogue Studio

> **NON_AUTHORITATIVE — REVISED CONCEPT EVIDENCE**

## Thesis

The centre of Chirality is the actual conversation between human and agent.
Dialogue Studio keeps transcript and composer persistently central, with a
project Navigator at left and an Artifact and Context Desk at right.

Artifacts inform the conversation only through explicit operator acts.
Previewing never sends content to the model. There is no synthesized shared-
intent object, ambient context, or hidden conversational memory.

## Region map

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│ Chirality  Dialogue Studio · Agent Room   Project / root   Runtime   Settings │
├──────────────────┬───────────────────────────────────┬────────────────────────┤
│ NAVIGATOR        │ HUMAN–AGENT DIALOGUE              │ ARTIFACT / CONTEXT DESK│
│ Deliverables     │ persona · mode · session status   │ Context Tray           │
│ Files            │                                   │ [file] [status] [×]    │
│ Changes          │ persistent transcript             │                        │
│                  │ human ↔ agent                     │ Artifact · Compare     │
│ project tree     │                                   │ Workbench · Pipeline   │
│ status / Git     │ permission and turn state         │ Toolkit · Activity     │
│                  │ explicit context + composer       │                        │
│                  │ Attach · Send · Interrupt         │ selected work/evidence │
└──────────────────┴───────────────────────────────────┴────────────────────────┘
```

Dialogue owns the flexible centre with a minimum readable width. The Desk may
widen for comparison but does not displace dialogue by default. On compact
screens, dialogue remains the default region; Navigator and Desk become
accessible sheets.

## Artifact and context lifecycle

The Desk distinguishes:

1. **Previewed artifact** — visible to the human only.
2. **Next-turn context** — explicitly added through existing attachment/context
   behavior.

Selecting a file opens a preview. `Add to next turn` places its exact path in a
visible Context Tray. The tray is the receipt for the next send. Removing an
item before send excludes it; later removal cannot rewrite a sent turn.
Changing previews never changes model context.

Agent returns, validation, and replay evidence may be previewed without being
retransmitted. Ineligible evidence remains citation-only. Diffs require
already materialized content; no new Git API is assumed.

## Placement of existing functions

| Function | Placement |
|---|---|
| Dialogue | Centre: persona, transcript, permissions, composer, context tray, Send, Interrupt, attribution. |
| Artifacts | Right Desk: Markdown, deliverables, diffs, validation, returns, replay; two-item compare. |
| Workbench | Right Desk tab tied to selected project/deliverable context. |
| Pipeline | Right Desk tab preserving DECOMP/PREP/TASK/AUDIT and query state. |
| Toolkit | Right Desk tab; remains explicitly non-authoritative. |
| Activity | Right Desk tab for active/replayed session tools, permissions, child lifecycle, and evidence. |
| Settings | Top-right modal/drawer using secure Electron bridges. |
| Agent Room | Separate secondary supervisory view; Dialogue remains mounted and restores exactly. |

Agent Room shows only recorded sessions, canonical events, actual attribution,
and recorded parentage. It does not imply arbitrary graphs, scheduling,
multi-child execution, global AgentRun discovery, routing, or residency
control.

## Six journeys

1. Select a deliverable; its status opens in the Desk while dialogue remains
   visible.
2. Preview `_CONTEXT.md`, explicitly add it to the next turn, and send with an
   exact attachment receipt.
3. Compare two artifacts while the centre dialogue continues streaming.
4. Configure TASK scope in the Pipeline Desk tab and submit through existing
   dispatch behavior.
5. Open Agent Room to inspect canonical manager/child evidence and attribution,
   then return to the unchanged dialogue.
6. Restore root, draft, attachments, geometry, selection, and Desk view after
   restart; rebuild run state from canonical replay.

## Component posture

- Recompose `ChatPanel` as the centre while preserving boot, streaming,
  drafts, attachments, permissions, error, mode, and interruption behavior.
- Rework `app-shell.tsx` mechanics; retain loop shells for compatibility.
- Split `WorkspaceSidebar`; promote FileTree and DocumentView into Navigator
  and Desk.
- Rehost Workbench, Pipeline, Toolkit, sessions, tool/subagent/transcript
  views, settings, and existing pure event projections.
- Keep AgentMatrix compatibility-only.
- Preserve the calm CSS token foundation.

## State and compatibility

Preserve project-root, toolkit, chat-draft/attachment, and layout-v1 values.
Introduce a versioned Dialogue Studio layout for pane geometry, active Desk
tab, and top-level view. Never delete or reinterpret v1; preview references are
root-bound. Persist no Agent Room conclusions.

Keep all existing routes, query parameters, unknown parameters, browser APIs,
SSE frames, provider singletons, and daemon-client ownership. Old loop-first
presentation remains available during compatibility.

## Accessibility and performance

- Landmarks, skip/F6 navigation, dialogue-first focus, keyboard tree/tabs/
  resizers, context announcements, inert hidden view, focus restoration,
  reduced motion, text status, accessible diffs, and WCAG AA.
- One mounted ChatPanel, centralized project polling, lazy/abortable previews,
  active-tab rendering, two-item compare limit, incremental projections, and
  bounded/virtualized large trees/diffs/sessions/transcripts.
- No summarization, semantic indexing, or automatic context compression.

## Tradeoffs

This is the simplest and most literal expression of the product thesis. The
right Desk can become crowded, and focused artifact reading is constrained by
keeping dialogue permanently central. It makes agent hierarchy available, but
only after entering Agent Room.

## Decomposition recommendation

- `SOW-005`: **RETIRE non-destructively** as a fixed 3x4 target-shell
  obligation.
- `DEL-08-02`: **MODIFY** to retain aliases, validation, query/routing
  compatibility, and launch guards.
- `DEL-05-04`: narrow modification for session-scoped Agent Room and activity
  projection.
- All other Gate-1 entities receive the presentation-neutral modifications
  already assessed; no topology or lifecycle change.

## Acceptance evidence

Dialogue and composer remain visibly central; preview and next-turn context are
provably distinct; all six journeys pass; Agent Room preserves active turn/
draft/attachments; compatibility and runtime truths hold; accessibility,
large-data, component, route/query, API/SSE, replay/interruption, migration,
build, premerge, packaging, and Desktop smoke checks pass. No old-UI retirement
is implied.
