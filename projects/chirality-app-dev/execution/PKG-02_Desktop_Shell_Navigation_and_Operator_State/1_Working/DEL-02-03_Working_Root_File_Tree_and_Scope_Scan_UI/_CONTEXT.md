# Context: DEL-02-03 Working Root File Tree and Scope Scan UI

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-03 |
| DeliverableName | Working Root File Tree and Scope Scan UI |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Dialogue-centred shell, per-chat folders, file/document presentation, current account feedback and non-authoritative local state.

**InclusionCriteria:** UI and operator workflow behavior.

**Exclusions:** Runtime engine internals.

## Deliverable Scope

Provide per-chat folder selection before the first message and fixed identity thereafter, bounded file-tree/document presentation and typed scan/validation feedback. D-APP-120 governs no-folder restrictions; D-APP-121 governs PDF presentation/security qualification. Exact scope-scan/deliverable-summary carrier differences remain keyed; their absence does not silently retire stable identity or read-only project-truth obligations.

## Anticipated Artifacts

File tree panel; deliverable summary widgets; scope scan integration

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-002, SOW-003 |
| SupportsObjectives | OBJ-001, OBJ-006 |
| ContextEnvelopeNotes | UI consumes workspace APIs but remains presentation-focused. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
