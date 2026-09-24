# Concrete current-row interface request

Basis: merged `4555f6c13f4356d78eff2df9a4e077708af01944`, with activation shared-source hashes bound in BASIS_AND_DELEGATION.json. This is a proposed additive interface for ROOT to assign after current ownership handback. No App, ModelTree, EngineeringTable, selectionSessionState or workspaceSession edit is part of the active canvas tranche. LIVE_MANAGER retains workspaceSession/controller ownership.

## Canvas interface now

`PipeViewport` accepts `currentRowNodeKey?: EntityKey | null`, defaulting only to null. It passes that independently to `layoutViewportLabels`. Selection, tree fallback focus and a dormant table's first roving row are never used to invent it. The App currently does not provide the prop, so actual current-row inspection remains incomplete until this handoff is implemented. Other context roles continue to work.

## Smallest later writer request

The merged EngineeringTable already has `generation: string`, `rows`, actual `focused` cell and captured edit, plus `active`; it lacks a row-publication callback. Add an optional callback there:

```ts
onCurrentRowChange?: (publication: Readonly<{
  generation: string;
  rowKey: EntityKey | null;
}>) => void;
```

Emit after actual cell/row activation and valid edit-row transitions. Do not emit the automatic first-row `rovingFocus` fallback as if it were a user current row. Validate against live canonical rows; a removed retained draft must not resurrect its node. Clear that publisher on generation change/unmount or loss of its eligible active surface; filtered valid captured edits retain their established current row. Preserve existing direct-table selection behavior and review-table nonselection behavior (current `focusCell` only calls onSelect outside review).

EntityGrid/ModelTree wraps the callback for node fields and node review with stable publisher identity (`node-fields` or `node-review`). Current `tableGeneration` is exactly `JSON.stringify([model.project.id, projectSessionGeneration])` (ModelTree line 770). Forward an additive `onCurrentRowChange({generation, source, rowKey})` prop to App. If later tree current-row coverage is needed, use actual tree navigation/click publication under a distinct publisher; do not reuse ModelTree's automatic fallback effect as a real activation event. Non-node families must not infer a node or arbitrary pipe endpoint.

App already receives model/projectSessionGeneration/activeModelIndex and renders both ModelTree and PipeViewport. A small App-local presentation cell (or narrowly owned hook) can receive the publication and pass the resolved node key without editing workspaceSession or its live-controller contract. Accept only current `JSON.stringify([model.project.id, projectSessionGeneration])`; accept a non-null key only when current index resolves it to a live node. A source's clear applies only when that source owns the current publication, so a dormant node-review cleanup cannot erase a newer node-fields row. Ignore old-generation publications; derive null immediately on generation mismatch, then reset the presentation cell. Do not mutate orderedSelection, primary selection, operation queue, history, model, results or persistence.

This route avoids a workspaceSession/controller need. If the owning writer chooses shared session storage instead, that is an explicit new requested writer transfer through ROOT; canvas does not co-own it.

## Required connecting checks after assignment

Use a node review cell on row B while primary remains A: canvas receives B and both context roles deduplicate correctly when they later coincide. Exercise pointer and keyboard navigation, valid retained edit outside filter, deleted row, project replacement/reopen generation, direct/review surface switch and stale source cleanup. Confirm dormant fallback rows never publish and late old-generation callbacks cannot revive context. Hide still suppresses a valid current-row node. Existing fit/table geometry and Apply/review behavior remain covered on the handback revision.
