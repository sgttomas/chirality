# Context: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DeliverableID | DEL-03-01 |
| DeliverableName | AgentEnginePort and Engine Conformance Suite |
| ResponsibleParty | TBD |
| Type | API_CONTRACT |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Product-owned turn lifecycle, route boundary, session locking, SSE compatibility, interrupts.

**InclusionCriteria:** `AgentEnginePort`, `TurnEngine`, API transport shape.

**Exclusions:** SDK-specific message translation details.

## Deliverable Scope

Define the product-owned runtime boundary and conformance tests for stub and SDK-backed adapters.

## Anticipated Artifacts

`agent-engine-port.ts`; runtime contract docs; conformance tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-037 |
| SupportsObjectives | OBJ-002 |
| ContextEnvelopeNotes | Single contract/test surface. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
