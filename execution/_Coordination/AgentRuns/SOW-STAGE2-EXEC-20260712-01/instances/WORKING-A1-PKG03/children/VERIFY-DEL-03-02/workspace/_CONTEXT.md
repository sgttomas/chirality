# Context: DEL-03-02 Thin TurnEngine and Session Locking

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DeliverableID | DEL-03-02 |
| DeliverableName | Thin TurnEngine and Session Locking |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Product-owned turn lifecycle, route boundary, session locking, SSE compatibility, interrupts.

**InclusionCriteria:** `AgentEnginePort`, `TurnEngine`, API transport shape.

**Exclusions:** SDK-specific message translation details.

## Deliverable Scope

Move turn lifecycle, session binding, boot metadata, and active-turn locking behind `TurnEngine`.

## Anticipated Artifacts

`turn-engine.ts`; lock cleanup tests; session lifecycle tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-009, SOW-010, SOW-011, SOW-038 |
| SupportsObjectives | OBJ-002 |
| ContextEnvelopeNotes | Backend refactor with stable external route shape. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
