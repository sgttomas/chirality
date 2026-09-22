# Context: DEL-07-02 Execution Root Scaffolding from Decomposition

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DeliverableID | DEL-07-02 |
| DeliverableName | Execution Root Scaffolding from Decomposition |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Working-root truth, execution-root scaffolding, deliverable files, `_STATUS.md`, `Dependencies.csv`, snapshots.

**InclusionCriteria:** Project file mechanics and deterministic filesystem APIs.

**Exclusions:** UI presentation except scope scan results.

## Deliverable Scope

Scaffold SPEC-conformant execution roots from decomposition markdown idempotently and recoverably.

## Anticipated Artifacts

Scaffold parser; `INIT.md`; `_COORDINATION.md`; package/deliverable folders; idempotence tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-024, SOW-025 |
| SupportsObjectives | OBJ-006 |
| ContextEnvelopeNotes | Existing service domain with multiple file outputs. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current execution basis — 2026-09-22

Codex is the sole current MVP engine, hosted as stock app-server under the application-owned Runtime service (D-GOV-43/D-APP-127). ScopeOfWork.md carries the current production claims. Legacy provider/daemon/four-document statements above retain their historical basis and do not qualify the live path. Existing scope, decomposition identity, responsible-party assignment and domain/professional boundaries are unchanged; current obligations and gaps are in `_STATUS.md`.
