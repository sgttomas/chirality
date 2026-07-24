# Concept C — Hybrid Workroom with Peer Agent Room

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

## Thesis

Chirality is one project workspace with two equal professional surfaces:

- **Workroom:** what am I making or reviewing?
- **Agent Room:** what governed work is happening, why, and what returned?

They share project, artifact, session, and context selection. Neither is a
dashboard, command centre, permanent chat shell, or model taxonomy. The
workspace restores the operator's last surface.

## Region model

### Workroom

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Project / Breadcrumbs      Search          Workroom | Agent Room  ⚙ │
├────────────────┬────────────────────────────────┬────────────────────┤
│ NAVIGATOR      │ ARTIFACT CANVAS                │ CONTEXT INSPECTOR  │
│ Recent/Pinned  │ [Brief.md] [Diff] [Return]     │ Metadata           │
│ Files          │                                │ Explicit context   │
│ Deliverables   │ Markdown / diff / evidence     │ Related run        │
│ Packages       │                                │ Ask / Run actions  │
├────────────────┴────────────────────────────────┴────────────────────┤
│ ACTIVITY SHELF  tools · tests · events · evidence · diagnostics     │
└──────────────────────────────────────────────────────────────────────┘
```

### Agent Room

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Project / Breadcrumbs      Search          Workroom | Agent Room  ⚙ │
├────────────────┬────────────────────────────────┬────────────────────┤
│ RUN NAVIGATOR  │ AGENT CANVAS                   │ RETURN / EVIDENCE  │
│ Active         │ Agent 1 — objective / status   │ Reviewed return    │
│ Recent         │   └ Agent 2 — bounded task     │ Attribution        │
│ By artifact    │ Meaningful activity, not       │ Permissions        │
│ By session     │ token-stream spectacle         │ Replay / artifacts │
├────────────────┴────────────────────────────────┴────────────────────┤
│ ACTIVITY SHELF  tools · tests · events · evidence · diagnostics     │
└──────────────────────────────────────────────────────────────────────┘
```

## Artifact and context model

- `ArtifactRef` points to canonical project or evidence material.
- `WorkspaceTab` is a non-authoritative view of an artifact.
- `ContextSet` is an explicit ordered set of references the operator intends
  to expose to an agent. Selecting an artifact never transmits it silently.
- `WorkspaceLink` rebuildably connects an artifact, session, validation, or
  AgentRun evidence reference.
- `OperatorProjection` derives calm semantic activity from canonical events.

Initial kinds: Markdown/text, Git diff, deliverable, agent return/evidence,
validation result, and session/replay.

## Primary journeys

### Resume and work on a deliverable

The Workroom restores open references. A deliverable exposes its control
documents and related files. The user can compare a diff or validation result
and deliberately assemble a context set.

### Work with an agent

The user invokes contextual chat or a bounded Run action from selected
artifacts. Workroom remains visible while the shelf shows meaningful activity.
A linked session opens in Agent Room when supervision is useful.

### Configure and supervise Pipeline work

`Run` opens a sheet containing existing DECOMP/PREP/TASK/AUDIT choices and
query semantics. The real session appears in Agent Room. Returned artifacts
link back to Workroom.

### Review and interrupt

Agent Room shows only parentage supported by canonical evidence. Selecting a
session exposes its objective, actual selection, permission evidence, return,
and replay. Existing interruption acts on that session and terminal state is
projected from canonical events.

## Existing functions

| Function | Placement |
|---|---|
| Workbench | Contextual preparation surface from the Workroom inspector or command palette. |
| Pipeline | `Run` sheet or secondary workspace; existing route and query semantics retained. |
| Chat | Contextual right panel or artifact/session tab; persists across peer switches but never owns the canvas. |
| Settings | Top-bar modal/drawer for runtime, credential, model, and UI settings. |
| Agent Room | Peer top-level surface, not a Portal/sidebar tab. |
| Activity | Shared collapsible shelf; raw operational detail remains secondary. |

## Calmness rules

- Ordinary two-option surface switch, not a glowing mode deck.
- Preserve restrained light-first tokens, readable objectives, whitespace, and
  quiet status markers.
- No agent seats, token waterfalls, model logos, hexagons, or global metrics.
- Cards default to objective, role, status, meaningful activity, elapsed time,
  and actual attribution.

## Runtime truth

The Agent Room consumes only existing sessions, turns, replay, interruption,
canonical events, permissions, model attribution, and the current bounded
Agent 1 / optional read-only Agent 2 behavior. It does not depict arbitrary
graphs, multiple children, scheduling, cross-project orchestration, or model
residency control.

## Responsive model

- Wide: three regions plus shelf.
- Medium: secondary inspector collapses to rail/drawer.
- Compact: one primary region at a time using accessible region tabs; current
  artifact/session selection survives.
- Provider singletons remain mounted through surface/layout changes.

## State and compatibility

Introduce a versioned local `WorkspaceLayoutV2` for selected peer, geometry,
tabs, pins, and shelf. Read and retain `chirality.layout.v1`; keep existing
project-root, toolkit, and draft keys. Preserve `/`, `/chat`, `/pipeline`,
`/workbench`, browser APIs, SSE frames, and query parameters.

## Accessibility and performance

- Landmarks for frame, navigator, main, inspector, and shelf.
- Keyboard trees, tabs, cards, dialogs, surface switch, and resizers.
- Focus restoration, text status, restrained live announcements, AA contrast,
  and reduced motion.
- Centralized workspace polling, incremental projection, lazy viewers, and
  bounded/virtualized trees, diffs, replay, and session lists.

## Staged implementation

1. Freeze `ArtifactRef`, `ContextSet`, `WorkspaceLayoutV2`, and pure
   `OperatorProjection`.
2. Add an opt-in hybrid frame using existing providers.
3. Build read-only Workroom navigation/canvas.
4. Build the runtime-constrained Agent Room and evidence inspector.
5. Re-host Workbench, Pipeline, chat, and settings.
6. Validate responsiveness, accessibility, migration, runtime regression, and
   packaged Desktop behavior.

## Tradeoffs

The hybrid costs more than a single dominant surface and could feel like two
products. A shared frame, cross-links, one activity shelf, and consistent
selection model mitigate that risk. Its benefit is that artifacts and
governed agents remain distinct without forcing either to masquerade as the
other.

## Decomposition recommendation

`SOW-005` and `DEL-08-02`: **MODIFY**, not repurpose. Remove the fixed 3x4
visual requirement while preserving provider-neutral routing, aliases, role
meaning, and legacy query compatibility. PKG-02/DEL-02-01 owns shell
composition; DEL-08-02 retains routing/alias semantics.

## Acceptance evidence

- All six Gate-2 scenarios complete without relying on the old shell.
- Artifact/session cross-links resolve to real project/runtime evidence.
- Agent Room handles running, meaningful activity, tool use, denial,
  interruption, failure, completion, replay, and actual model attribution.
- No unsupported orchestration capability is implied.
- Routes, APIs, SSE, queries, storage, providers, and packaged startup remain
  compatible.
- Keyboard, screen-reader, migration, large-data, runtime, and packaged smoke
  checks pass.

Passing establishes preview parity only. It does not retire the existing UI.
