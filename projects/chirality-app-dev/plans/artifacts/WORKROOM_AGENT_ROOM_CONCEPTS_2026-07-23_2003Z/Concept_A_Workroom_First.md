# Concept A — Workroom First

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

## Thesis

Chirality opens onto the work itself. Files, deliverables, Markdown, diffs,
validation results, agent returns, and replay evidence occupy the persistent
canvas. Chat is a supporting conversation dock. Agent Room is a deliberate
secondary view reconstructed from canonical session and event evidence.

## Region model

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Chirality  [Workroom] [Agent Room]   Project / breadcrumb      runtime  ⚙  │
├──────────────────┬───────────────────────────────────────┬───────────────────┤
│ PROJECT          │ ARTIFACT WORKING SET                  │ CONTEXT / ACTIONS │
│ NAVIGATOR        │ [status.md] [diff] [return]           │ Context           │
│ Deliverables     │                                       │ Workbench         │
│ Files            │ Markdown / diff / validation          │ Pipeline          │
│ Changes          │ deliverable / agent evidence          │ Toolkit           │
├──────────────────┴───────────────────────────────────────┴───────────────────┤
│ Agent: WORKING_ITEMS · running · provider/model       Open chat · Interrupt │
│ conversation dock expands here without unmounting an active turn             │
└──────────────────────────────────────────────────────────────────────────────┘
```

Desktop defaults reserve 260–320 px for navigation and 340–460 px for
context/actions. The canvas receives the remaining width. Chat collapses to a
status strip and expands vertically. Compact layouts show one accessible
region at a time with the artifact canvas as default.

## Artifact and context model

An `ArtifactRef` identifies a canonical project/evidence source and its
read-only presentation kind. Tabs are a working set, not copies. The active
tab supplies contextual metadata; users may pin one deliverable context during
comparison. Compare mode contains at most two source views.

Initial kinds: Markdown/text, deliverable, materialized Git diff, validation,
agent return, and transcript/replay.

## Primary journeys

- Select a deliverable in the Navigator and open status, context,
  dependencies, or production documents as persistent tabs.
- Start a turn from the conversation dock, collapse it, and continue reading
  while the status strip retains interruption and meaningful activity.
- Select a deliverable, choose Run, and open Pipeline with existing TASK scope
  parameters prefilled from explicit context.
- Switch deliberately to Agent Room to inspect the selected session, recorded
  parentage, actual model attribution, permissions, evidence, and outcome.
- Restore project root, tabs, active artifact, geometry, dock state, and drafts
  after restart while rebuilding Agent Room from canonical data.

## Existing functions

| Function | Placement |
|---|---|
| Workbench | Context/Actions dock, with optional centre focus view. |
| Pipeline | Context/Actions dock or centre utility view. |
| Chat | Persistent bottom conversation dock; collapsed by default. |
| Settings | Top-right dialog/drawer using existing secure bridges. |
| Agent Room | Secondary top-level shell view; global header and conversation status remain mounted. |
| Activity detail | Agent Room evidence inspector and expandable conversation/session details. |

## Agent Room

```text
┌──────────────────┬──────────────────────────────────┬───────────────────────┐
│ Sessions         │ Observed Session                 │ Evidence Inspector    │
│ active/replayed  │ Agent 1                          │ attribution           │
│                  │   └ Agent 2, if recorded         │ permissions           │
│                  │ meaningful activity/outcome      │ tools/artifacts       │
└──────────────────┴──────────────────────────────────┴───────────────────────┘
```

It is a semantic list/lane, not a graph editor. Missing evidence is labelled
“not recorded.” Only the current Agent 1 / optional bounded Agent 2 pilot is
represented.

## Component posture

- Reuse provider composition and current API clients.
- Rework `app-shell.tsx` resizing and persistence mechanics.
- Retain loop shells and `AgentMatrix` for compatibility only.
- Promote `DocumentView`, Markdown rendering, file tree, and deliverable
  scanning into the canvas/navigation model.
- Rehost Workbench, Pipeline, Toolkit, ChatPanel, settings, sessions, and event
  detail without changing their contracts.
- Adapt published diff parsing/context collapsing and deliverable roster ideas;
  reject published browser-local credential handling and command-centre skin.

## Runtime, state, and compatibility

No new runtime contract is required. Preserve `/`, `/chat`, `/workbench`,
`/pipeline`, all query parameters and unknown parameters, browser APIs, SSE
frames, and provider singletons. A future accepted `/` switch would open
Workroom; compatibility deep links would open the appropriate dock/view.

Introduce a separate versioned Workroom layout/working-set record. Import
useful values from `chirality.layout.v1` without overwriting it. Preserve
project-root, toolkit, and mode/persona-scoped draft keys. Do not persist
Agent Room conclusions.

## Accessibility and performance

- Landmarks, skip links, F6 region traversal, real tree/tab semantics,
  keyboard resizers, dialog focus restoration, text status, reduced motion,
  accessible diffs, and WCAG AA contrast.
- One working-root refresh coordinator, lazy/abortable loading, bounded working
  set, incremental event projection, and virtualized large trees/diffs/replay.
- Keep ChatPanel mounted during active work while making collapsed rendering
  lightweight.

## Staged implementation

1. Feature-gated Workroom shell and versioned convenience state.
2. Read-only Navigator, deliverable roster, artifact tabs, Markdown/text.
3. Rehost Workbench, Pipeline, Toolkit, and settings.
4. Rehost ChatPanel as persistent dock.
5. Add session-scoped Agent Room projection.
6. Add diff, validation, return, transcript, responsive and accessibility
   hardening.
7. Run parity, runtime, build, packaging, and independent evaluation.

## Tradeoffs

Artifact primacy best matches the owner's stated priority and gives the
calmest default. Conversational initiation is less visually prominent, and
the right context dock must resist overcrowding. Agent supervision takes a
deliberate view switch.

## Decomposition recommendation

- `SOW-005`: **RETIRE non-destructively** as a target-shell requirement; keep
  matrix presentation through compatibility until separately retired.
- `DEL-08-02`: **MODIFY** to preserve persona aliases, query compatibility,
  validation, role meaning, and launch guards without owning a fixed matrix.

## Acceptance evidence

The six Gate-2 journeys, deep-link/query compatibility, unchanged API/SSE
contracts, mounted active turn, correct projection/attribution, state
migration, keyboard/a11y, large-data bounds, runtime regression, build,
`desktop:pack`, and packaged Desktop smoke must pass. Old UI remains available.
