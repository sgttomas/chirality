# Concept 2 — Collaborative Bench

> **NON_AUTHORITATIVE — REVISED CONCEPT EVIDENCE**

## Thesis

The focal point is the durable visual pairing of human–agent dialogue and the
artifact currently being worked on. Shared intent is neither a pointer nor a
summary object; it emerges through conversation and is expressed and tested in
artifacts, decisions, evidence, and validation.

Design maxim: **the conversation stays; the work changes beside it.**

## Balanced bench

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Project │ BENCH · Files · Pipeline · Workbench · Agent Room │ Runtime · ⚙  │
├──────┬────────────────────────────┬───────────────────────────────┬──────────┤
│ ACT. │ DIALOGUE — anchored        │ ACTIVE WORKING AREA           │ SUPERV.  │
│ RAIL │ persona / mode             │ artifact navigator + canvas   │ RAIL     │
│      │ human + agent transcript   │ deliverable / Markdown / text │ collapsed│
│ Bench│ permission prompts         │ evidence / validation         │ status   │
│ Files│ composer / attachments     │                               │ markers  │
│ Pipe │ Send · Interrupt           │                               │          │
└──────┴────────────────────────────┴───────────────────────────────┴──────────┘
```

Dialogue receives roughly 40–44% of desktop width. The working area receives
the rest. The supervisory rail is 48–56 px collapsed. Expanding supervision
shrinks working area before dialogue.

## Artifact focus

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Project │ Back to balanced bench │ artifact path/status │ settings          │
├──────┬───────────────────┬─────────────────────────────────────────┬─────────┤
│ ACT. │ DIALOGUE          │ ARTIFACT FOCUS                          │ SUPERV. │
│ RAIL │ anchored compact  │ large canvas / compare / evidence      │ collapsed│
│      │ transcript        │ deliverable context and validation      │ status  │
│      │ composer          │                                         │         │
│      │ Interrupt         │                                         │         │
└──────┴───────────────────┴─────────────────────────────────────────┴─────────┘
```

Dialogue narrows to a tested 320–360 px minimum but never becomes an icon,
hidden drawer, or unmounted tree. Permission state and interruption remain
usable.

## Visible workflow and parent–child hierarchy

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Project │ BENCH │ AGENT ROOM │ refreshed at … │ settings                    │
├──────┬────────────────────────────┬───────────────────────────────────────────┤
│ ACT. │ DIALOGUE — anchored        │ SUPERVISORY AGENT ROOM                   │
│ RAIL │ same conversation          │ Agent 1 · recorded session              │
│      │ same composer/interrupt    │      │ parentSessionId only              │
│      │                            │ Agent 2 · recorded bounded child         │
│      │                            │ replay · tools · return · attribution    │
└──────┴────────────────────────────┴───────────────────────────────────────────┘
```

The Supervisory Rail has three scales:

- collapsed markers for running, permission-needed, terminal, or interrupted;
- expanded compact cards for the current/selected session and recorded child;
- Agent Room mode with deterministic role lanes and selected evidence.

Every edge equals recorded `parentSessionId`. There are no empty spawn nodes,
editable edges, arbitrary children, scheduling, model controls, or inferred
hierarchy.

## Context model

The UI separates:

1. project context;
2. stable dialogue identity;
3. the current working referent;
4. adjacent activity surface;
5. selected canonical evidence.

None is shared intent. Changing the right-side surface does not redefine the
dialogue or its draft identity. A hard compatibility route still initializes
logical mode as today; in-shell surface changes do not silently rewrite it.
Artifact inclusion remains explicit through existing attachment/context
behavior.

## Placement of existing functions

| Function | Placement |
|---|---|
| Dialogue, persona, attachments, permissions, interrupt | Permanently anchored dialogue pane. |
| Files and deliverables | Adjacent working-area navigator/canvas. |
| Pipeline | Right working area, centre-primary, dialogue retained. |
| Workbench | Right working area, centre-primary, dialogue retained. |
| Toolkit | Dialogue footer/drawer; per-turn semantics unchanged. |
| Sessions/history | Supervisory Rail; action labelled `Load replay`, never Resume. |
| Tools, permissions, delegation returns, transcript | Evidence tabs for selected supervisory card. |
| Agent Room | Expanded right-side supervision with anchored dialogue. |
| Settings | Header cluster using existing secure IPC. |
| Matrix | Legacy compatibility presentation only; routing semantics retained. |

## Journeys

1. Continue dialogue, select a deliverable, and open its allowed document beside
   the transcript.
2. Enter artifact focus during streaming while dialogue, permission, and
   interruption remain visible.
3. Inspect/compare governed material reachable through current content/evidence
   contracts.
4. Open TASK Pipeline on the working side with existing query scope.
5. Open Workbench on the working side with existing role/lifecycle gates.
6. Expand Supervisory Rail while talking to see current status and recorded
   parent–child hierarchy.
7. Enter Agent Room for replay/tools/return/model evidence without displacing
   the dialogue.
8. Restore geometry/root/state and rebuild supervision after restart.

## Runtime truth

Cards use only role, status, `parentSessionId`, timestamps, engine/provider/
model, optional residency epoch, and canonical events. There is no browser
global AgentRun discovery or global live subscription. Other-client state is
timestamped and refresh/replay based. Bounded event projections are disclosed.
Standalone sessions remain unconnected. Models never determine roles.

The initial Artifact Canvas is limited to documents/evidence available through
current browser contracts; it does not promise arbitrary files, editing, or
live Git diff execution.

## Component posture

- Preserve one mounted ChatPanel, persona resolution, providers, secure
  settings, API clients, and daemon boundary.
- Rework AppShell/SidebarRightLoopLayout geometry while preserving their
  mounted-child and keyboard-resize lessons.
- Promote FileTree/DocumentView into the working area.
- Rehost Pipeline/Workbench in full adjacent space.
- Split WorkspaceSidebar into activity, project, and supervisory surfaces.
- Rework session/event views into a provider-neutral bounded projection.
- Keep AgentMatrix target presentation out of the new shell; reuse its routing
  guards and compatibility behavior.
- Retain calm CSS tokens.

## State and compatibility

Preserve all existing keys untouched. Add a rollback-safe, versioned
Collaborative Bench layout for balanced/focus splits, rail state, adjacent
surface, and navigator visibility. Keep stable dialogue identity above
right-side composition. Preserve `/`, `/chat`, `/pipeline`, `/workbench`,
known/unknown query parameters, APIs, SSE, providers, and legacy UI.

## Accessibility and performance

- Dialogue is primary `main`; working area and supervision are named regions.
- F6 traversal, skip links, keyboard separators, focus restoration, semantic
  list-based hierarchy, decorative connectors, text status, restrained live
  announcements, reduced motion, accessible evidence, WCAG AA.
- Collapse supervision before compromising dialogue at narrower widths; stack
  dialogue first when necessary.
- Incremental pure supervisory projection, selected-session replay only,
  explicit event bound, no N-way replay, centralized tree polling, bounded/
  virtualized large content, and stable token streaming.

## Tradeoffs

This is the strongest expression of human and agent working on an artifact
together and is the only option that keeps recorded workflow hierarchy visibly
available beside the conversation. It has the most demanding responsive layout
and requires careful separation of stable dialogue identity from adjacent route
surface. The persistent hierarchy can look like a control plane unless kept
quiet, evidence-labelled, and non-interactive.

## Decomposition recommendation

`SOW-005` and `DEL-08-02`: **MODIFY**, not retire. Preserve persona/intent
routing, query mapping, aliases, unavailable-persona handling, and mid-turn
guards. The 3x4 matrix becomes compatibility presentation. DEL-05-04 owns the
read-only Agent Room projection; DEL-08-02 does not acquire graph ownership.
No topology, runtime, or lifecycle change.

## Acceptance evidence

Dialogue stays mounted in balanced, artifact-focus, Pipeline, Workbench, rail,
and Agent Room states; no intent object/summary exists; routes/modes/drafts and
guards remain compatible; every hierarchy edge is canonical; stale/bounded
state is honest; supported artifact limits are explicit; state is rollback-
safe; all journeys, accessibility, responsiveness, large-data, API/SSE/runtime,
build, packaging, and Electron security checks pass. Old UI remains.
