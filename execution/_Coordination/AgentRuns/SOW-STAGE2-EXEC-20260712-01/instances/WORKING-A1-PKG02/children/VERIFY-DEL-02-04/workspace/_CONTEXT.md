# Context: DEL-02-04 Toolkit Options and Local UI State

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Desktop Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-04 |
| DeliverableName | Toolkit Options and Local UI State |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** User-facing shell, matrix routing, file tree, toolkit, API key UI, local UI state.

**InclusionCriteria:** UI and operator workflow behavior.

**Exclusions:** Runtime engine internals.

## Deliverable Scope

Expose runtime options and preserve pane layout, drafts, and local presets as non-authoritative convenience state.

## Anticipated Artifacts

Toolkit controls; pane resize/collapse state; draft/preset storage guards

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-004, SOW-008, SOW-016 |
| SupportsObjectives | OBJ-001, OBJ-004 |
| ContextEnvelopeNotes | Focused local UI state slice. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
