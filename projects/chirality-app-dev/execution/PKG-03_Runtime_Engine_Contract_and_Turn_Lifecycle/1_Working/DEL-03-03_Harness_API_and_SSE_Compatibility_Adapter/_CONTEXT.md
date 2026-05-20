# Context: DEL-03-03 Harness API and SSE Compatibility Adapter

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DeliverableID | DEL-03-03 |
| DeliverableName | Harness API and SSE Compatibility Adapter |
| ResponsibleParty | TBD |
| Type | API_CONTRACT |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Product-owned turn lifecycle, route boundary, session locking, SSE compatibility, interrupts.

**InclusionCriteria:** `AgentEnginePort`, `TurnEngine`, API transport shape.

**Exclusions:** SDK-specific message translation details.

## Deliverable Scope

Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services.

## Anticipated Artifacts

Route adapter tests; SSE compatibility fixtures; UI event contract docs

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-011, SOW-040 |
| SupportsObjectives | OBJ-001, OBJ-002 |
| ContextEnvelopeNotes | Focused compatibility slice. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
