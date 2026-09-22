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

**ScopeDescription:** App-side runtime-client integration for the Runtime-owned turn lifecycle, including thin Desktop/HTTP proxy behavior, session request binding, route/SSE compatibility, interrupt/cancel presentation, and conformance evidence.

**InclusionCriteria:** App-owned Runtime service client/proxy, contract compatibility, API/SSE transport, affected-client evidence.

**Exclusions:** Generic runtime contracts, Runtime/session/lock/interruption/persistence semantics, and provider-specific message translation details.

## Deliverable Scope

Preserve supported `/api/harness/*` operation shapes and the extensible upstream-preserving event representation, keepalives and renderer disconnect/reattach continuity against the application-owned Runtime service (D-GOV-43/D-APP-127).

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
