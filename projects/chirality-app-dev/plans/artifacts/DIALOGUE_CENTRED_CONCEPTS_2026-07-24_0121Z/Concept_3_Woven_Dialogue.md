# Concept 3 — Woven Dialogue

> **NON_AUTHORITATIVE — REVISED CONCEPT EVIDENCE**

## Thesis

Dialogue is the stable centre. Files, proposed changes, diffs, validation,
permission decisions, returns, and evidence appear as provenance-bearing
objects within the chronological conversation. They can expand inline or open
into focused inspection while preserving the exact originating dialogue
anchor.

The design has three scales:

- **Dialogue** — where understanding and action develop.
- **Artifact focus** — where one proposal/evidence object receives sustained
  attention.
- **Agent Room** — where governed sessions and recorded parentage are
  supervised.

## Default region map

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Project / Breadcrumbs       Search        Dialogue · Agent Room   ⚙ │
├───────────────┬──────────────────────────────────────┬───────────────┤
│ NAVIGATOR     │ WOVEN DIALOGUE                       │ INSPECTOR     │
│ Threads       │ Human question                       │ Thread/session│
│ Recent        │ Agent interpretation                 │ Explicit ctx  │
│ Files         │ ┌ Proposed diff / validation / ... ┐ │ References    │
│ Deliverables  │ └ inline object: inspect · focus   ┘ │ Attribution   │
│ Packages      │ Human correction                     │ Permissions   │
├───────────────┴──────────────────────────────────────┴───────────────┤
│ ACTIVITY SHELF  tools · tests · canonical events · diagnostics      │
└──────────────────────────────────────────────────────────────────────┘
```

## Artifact focus

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Project / Thread / Turn / Artifact   Back to dialogue anchor      ⚙ │
├───────────────┬──────────────────────────────────────┬───────────────┤
│ RELATED       │ FOCUSED ARTIFACT VIEWER              │ PROVENANCE    │
│ References    │ Markdown / diff / return / evidence  │ Origin turn   │
│ Neighbors     │ compare / inspect / navigate         │ Session/model │
│               │                                      │ Validation    │
├───────────────┴──────────────────────────────────────┴───────────────┤
│ THREAD ANCHOR  surrounding exchange · reopen full dialogue          │
└──────────────────────────────────────────────────────────────────────┘
```

Returning restores the same thread position, draft, selection, and expanded
objects. The thread anchor prevents artifact focus from becoming a disconnected
document application.

## Dialogue objects and context

UI-local object families are reference, proposal, diff, validation, return,
permission, and session/evidence objects. They originate from explicit runtime
or project data and cannot infer that prose is an accepted proposal or a test
was successful.

Every object has a concise preview, expand/collapse, Focus, provenance, and
return-to-anchor behavior. Referencing it does not transmit its content. A
visible next-turn Context Set lists exact references to expose, and the outgoing
turn shows a scope receipt.

An automatic current-intent summary is excluded. A future local-model
experiment would need to be provisional, attributable, rebuildable, and
separately governed.

## Placement of existing functions

| Function | Placement |
|---|---|
| Chat | Becomes central Woven Dialogue. |
| Navigator | Threads, recent work, files, deliverables, and packages. |
| Inspector | Selected thread/object provenance, explicit next-turn context, attribution, permissions, evidence. |
| Workbench | Contextual preparation sheet/focus view from Inspector/composer. |
| Pipeline | Run action near composer or selected object; current dispatch semantics retained. |
| Settings | Top-right modal/drawer. |
| Artifact viewer | Focused centre reached from inline objects; compact thread anchor remains. |
| Agent Room | Peer supervisory surface showing supported sessions and recorded parentage. |
| Activity | Shared collapsed shelf for tools, tests, raw events, evidence, diagnostics. |

## Six journeys

1. Select a deliverable, introduce a reference object, explicitly add eligible
   content to next-turn context, and discuss it in place.
2. Open Markdown/diff focus while a turn runs; return to the exact originating
   exchange when the return object arrives.
3. Invoke Pipeline from dialogue, review TASK scope/context/permissions, and
   receive the real session/return back as canonical objects.
4. Inspect Agent 1/Agent 2 evidence in Agent Room, focus its return, and navigate
   back to the requesting dialogue.
5. Restore thread, anchors, expanded objects, draft, focused artifact, and pane
   geometry after restart using references and replay.
6. Interrupt from dialogue, Agent Room, or Inspector; show the canonical
   interruption as a distinct system object and retain raw detail in the shelf.

## Component posture

- Rehost ChatPanel centrally while preserving its contracts.
- Rework AppShell mechanics and layout-state through v2 migration.
- Split WorkspaceSidebar into Navigator/Inspector/Activity.
- Rework file, deliverable, DocumentView, event, Pipeline, and Workbench
  surfaces as object/focus sources.
- Retain calm tokens and route compatibility; reject the matrix and
  command-centre visual language as target IA.
- Adapt published diff/Markdown ideas for inline/focused objects.

## State and compatibility

Versioned workspace state may store thread/session reference, dialogue anchor,
expanded object IDs, focused artifact and origin, compare references, explicit
next-turn context references, and geometry. Persist references, not content or
outcomes. Preserve layout v1, project root, toolkit, drafts, routes, query
parameters, API shapes, SSE ordering, providers, and compatibility UI.

## Accessibility and performance

- Ordered conversation with clear authorship; avoid feed semantics unless fully
  implemented.
- Streaming never steals focus or forces scroll. A New Activity control returns
  to the latest turn.
- Inline objects expose type, state, provenance, expansion, Focus, and text
  status. Focus returns to the originating turn.
- Keyboard-operable context, tree, objects, peer view, shelf and resizers;
  restrained announcements; reduced motion; AA contrast.
- Virtualized long threads with stable anchors, batched event projection,
  streamed active response isolation, lazy heavy viewers, bounded previews,
  centralized project caches, and long-thread/large-diff testing.

## Tradeoffs

This most directly shows work emerging from dialogue. It also carries the
highest interaction and rendering complexity: inline objects can become a
noisy feed, proposal status can be over-inferred, long-thread virtualization
and anchor restoration are difficult, and focused artifacts can fragment
attention. Provenance, restrained summaries, explicit status, and stable
anchors are mandatory.

## Decomposition recommendation

`SOW-005` and `DEL-08-02`: **MODIFY**, not retire. Remove the fixed visual
matrix but preserve provider-neutral routing, aliases, and legacy query/matrix
compatibility. DEL-05-04 receives the narrow projection change; PKG-02 owns the
dialogue shell. No topology, runtime, or lifecycle change.

## Acceptance evidence

Central dialogue distinguishes human, agent, runtime, and evidence authorship;
objects never invent status; focus returns exactly to origin; next-turn context
is explicit; current runtime states and parentage project truthfully; all
compatibility, state, accessibility, long-thread, large-object, runtime,
packaging, independent evaluation, and six-journey checks pass. Old UI and
automatic summarization remain out of scope.
