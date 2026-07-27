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

**ScopeDescription:** App-side runtime-client integration for the Root-owned turn lifecycle, including thin Desktop/HTTP proxy behavior, session request binding, route/SSE compatibility, interrupt/cancel presentation, and conformance evidence.

**InclusionCriteria:** App daemon client/proxy, contract compatibility, API/SSE transport, affected-client evidence.

**Exclusions:** Generic runtime contracts, daemon/session/lock/interruption/persistence semantics, and provider-specific message translation details.

## Deliverable Scope

Verify the App client against Root-owned runtime contracts, preserve the compatibility re-export and App-facing API/UI compatibility, and produce conformance evidence without redefining generic runtime semantics.

## Anticipated Artifacts

`@chirality/harness-contract` compatibility re-export; App client conformance tests; API/UI compatibility evidence

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-037 |
| SupportsObjectives | OBJ-002 |
| ContextEnvelopeNotes | App client contract-compatibility and conformance surface. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
