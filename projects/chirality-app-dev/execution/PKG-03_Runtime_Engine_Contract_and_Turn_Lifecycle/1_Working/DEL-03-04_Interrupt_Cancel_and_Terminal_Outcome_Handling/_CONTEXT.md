# Context: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DeliverableID | DEL-03-04 |
| DeliverableName | Interrupt, Cancel, and Terminal Outcome Handling |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App-side runtime-client integration for the Runtime-owned turn lifecycle, including thin Desktop/HTTP proxy behavior, session request binding, route/SSE compatibility, interrupt/cancel presentation, and conformance evidence.

**InclusionCriteria:** App-owned Runtime service client/proxy, contract compatibility, API/SSE transport, affected-client evidence.

**Exclusions:** Generic runtime contracts, Runtime/session/lock/interruption/persistence semantics, and provider-specific message translation details.

## Deliverable Scope

Forward explicit App interrupts and verify Runtime-owned terminal persistence and true-terminal lock release. Renderer disconnect only unsubscribes; verify continuity and sequence-based reattachment without resending the prompt (D-GOV-43/D-APP-127).

## Anticipated Artifacts

Client interrupt forwarding tests; Runtime terminal/lock and disconnect-continuity conformance evidence; current event fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-012, SOW-015 |
| SupportsObjectives | OBJ-002, OBJ-003 |
| ContextEnvelopeNotes | App client lifecycle-integration slice with explicit Runtime ownership. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
