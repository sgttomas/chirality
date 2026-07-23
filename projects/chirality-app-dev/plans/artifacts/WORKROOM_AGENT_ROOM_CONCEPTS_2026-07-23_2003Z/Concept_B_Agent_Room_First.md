# Concept B — Agent Room First

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

## Thesis

Make Agent Room the home surface, but define “room” as a deterministic operator
projection over existing session records, the current turn’s SSE, and
selected-session replay. It is an evidence-aware foyer—not a graph editor,
scheduler, run registry, or second runtime.

Design maxim: **spatialize legible evidence, never spatialize unsupported
authority.**

## Region model

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ Project / Root │ ROOM  ARTIFACT  PIPELINE  WORKBENCH │ Runtime / Settings │
├───────────────┬──────────────────────────────────────┬──────────────────────┤
│ PROJECT       │ CENTRE: AGENT ROOM                   │ EVIDENCE INSPECTOR   │
│ LIBRARY       │ Agent 1 session                     │ Overview             │
│ Files         │  status · actual model · epoch      │ Transcript           │
│ Deliverables  │        │ recorded parentSessionId   │ Tools / permissions  │
│ Recent        │ Agent 2, only when recorded          │ Return / attribution │
├───────────────┴──────────────────────────────────────┴──────────────────────┤
│ OPERATOR DOCK — mounted chat · persona · toolkit · permission · interrupt │
└─────────────────────────────────────────────────────────────────────────────┘
```

The left Project Library contains Files, Deliverables, and Recent—not an
AgentRun tree. The centre changes between Room, Artifact, Pipeline, and
Workbench. The right inspector shows evidence for the selected session or
artifact. The mounted Operator Dock preserves live turn state.

## Runtime-truth rules

- Cards use recorded role, status, timestamps, engine selection, residency
  epoch, and canonical events.
- A connector appears only for recorded `parentSessionId`.
- No empty Agent 2 slot, add-agent affordance, drag/connect behavior,
  multiple-child display, scheduling, or model activation.
- Standalone sessions are not attached to a manager.
- No global AgentRun browser or start-run button: current browser contracts do
  not expose global run discovery.
- Other-client activity is refreshed/replayed, not falsely called live.
- Current `Open` session behavior is relabelled `Load replay`; it does not
  resume ChatPanel.
- Bounded/truncated event projections are disclosed.

## Artifact relationship

Agent Room is the foyer; artifacts remain the work product. Selecting a
session reveals only evidence-linked paths. Selecting a file/deliverable
changes the centre to Artifact Canvas while a compact room strip retains
current session status and interruption.

Initial kinds: Markdown/text, Git diff, deliverable, return/evidence,
validation, and transcript. An artifact is marked related to a session only
when canonical evidence says so.

## Primary journeys

- Open Deliverables in the library and inspect the selected artifact without
  requiring a session.
- Start/send from the Operator Dock, then inspect an artifact while the room
  card/status strip updates from the initiating SSE.
- Open centre-stage Pipeline with existing TASK query intent.
- Select a manager session, explicitly load replay, inspect transcript/tools/
  permissions/attribution, and select its child only when parentage exists.
- Open Workbench centre-stage with its existing authorization and query state.
- Restore layout, refresh sessions, and lazily replay selection after restart.
- Interrupt from the persistent active-turn control and project terminal state
  only from canonical evidence.

## Existing functions

| Function | Placement |
|---|---|
| Workbench | Centre-stage selector and `/workbench` compatibility route. |
| Pipeline | Centre-stage selector and `/pipeline` compatibility route. |
| Chat | Persistent bottom Operator Dock; `/chat` expands it while retaining logical CHAT mode. |
| Settings | Header controls using existing origin-bound Electron IPC. |
| Artifact canvas | Alternate centre stage reached from project library or evidence link. |
| Agent Room | Default `/` centre stage. |

## Component posture

- Preserve provider singletons.
- Rehost one `ChatPanel` controller in the Operator Dock.
- Elevate file tree and deliverables to Project Library.
- Split `WorkspaceSidebar` into Project Library and Evidence Inspector.
- Rework session, transcript, tool, and subagent views as honest replay/
  projection surfaces.
- Rehost Pipeline/Workbench in the centre.
- Preserve persona resolution and guards.
- Reject AgentMatrix as the home; retain routing builders/guards.
- Rework dormant AppShell mechanics and retain calm CSS tokens.

## State and compatibility

Use a distinct versioned Workroom layout key; preserve and never reinterpret
or delete `chirality.layout.v1`. Preserve project root, toolkit, and chat-draft
keys exactly. Derive logical mode from the compatibility route, not the visual
centre stage.

Keep `/`, `/chat`, `/pipeline`, `/workbench`, known and unknown query
parameters, API shapes, and SSE names. Keep the old presentation available
behind a compatibility adapter/switch.

## Accessibility and performance

- Semantic lists/groups rather than ARIA canvas; connector lines are
  decorative and relationship text is explicit.
- Logical DOM/landmark order, region shortcuts, real tree/tabs, keyboard
  separators, visible focus, text status, restrained announcements, reduced
  motion, accessible diffs, responsive drawers, and WCAG AA.
- Session cards come from records; replay only the selected session.
- Disclose the 2000-event in-memory projection bound.
- Incremental current-session projection, centralized refresh/polling, lazy
  evidence, and bounded/virtualized large views.

## Staged implementation

1. Feature-gated parallel shell and compatibility/state tests.
2. Read-only session projection with deterministic lanes and lazy replay.
3. Project Library and Artifact Canvas.
4. Rehost one mounted ChatPanel in the Operator Dock.
5. Rehost Pipeline, Workbench, settings, and inspectors.
6. Accessibility, responsive, state, and performance hardening.
7. Task parity and packaged proof.

## Tradeoffs

The home surface makes governance and attribution exceptionally legible, but
risks emphasizing process over product and can feel sparse on a new project.
It is also the concept most constrained by the current lack of global run
discovery and live cross-client updates.

## Decomposition recommendation

`SOW-005` and `DEL-08-02`: **MODIFY**, not retire. Preserve governed persona/
intent routing, aliases, query compatibility, unavailable-persona handling,
and mid-turn guards. Make the 3x4 matrix a compatibility presentation, not the
Agent Room or home IA. DEL-05-04 owns evidence projection.

## Acceptance evidence

All compatibility, singleton-provider, mounted-turn, canonical-card/parentage,
replay-versus-resume, bounded projection, six-journey, state, accessibility,
large-data, runtime, build, Electron-security, `desktop:pack`, and owner-review
checks must pass. No current UI retirement is authorized.
