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

**ScopeDescription:** App-side runtime-client integration for the Root-owned turn lifecycle, including thin Desktop/HTTP proxy behavior, session request binding, route/SSE compatibility, interrupt/cancel presentation, and conformance evidence.

**InclusionCriteria:** App daemon client/proxy, contract compatibility, API/SSE transport, affected-client evidence.

**Exclusions:** Generic runtime contracts, daemon/session/lock/interruption/persistence semantics, and provider-specific message translation details.

## Deliverable Scope

Keep App `/api/harness/*` and Desktop surfaces as daemon clients, bind
project/persona/mode/delegation-policy/options requests, and verify daemon-owned
session lifecycle and one-active-turn behavior.

Applied decomposition row L318 (SCA-APP-010 Gate 5, 2026-09-04) notes: App
backend-integration slice; generic TurnEngine and lock ownership remain
Root-owned; the stored delegation-policy field is Root-owned (SOW-083, OI-008).

## Anticipated Artifacts

Daemon-client turn proxy; App session integration tests; daemon locking/lifecycle conformance evidence

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-009, SOW-010, SOW-011, SOW-038 |
| SupportsObjectives | OBJ-002 |
| ContextEnvelopeNotes | App backend-integration slice; generic TurnEngine and lock ownership remain Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
