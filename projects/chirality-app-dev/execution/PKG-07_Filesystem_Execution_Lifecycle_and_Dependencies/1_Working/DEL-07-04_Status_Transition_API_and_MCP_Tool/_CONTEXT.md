# Context: DEL-07-04 Status Transition API and MCP Tool

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DeliverableID | DEL-07-04 |
| DeliverableName | Status Transition API and MCP Tool |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Working-root truth, execution-root scaffolding, deliverable files, `_STATUS.md`, `Dependencies.csv`, snapshots.

**InclusionCriteria:** Project file mechanics and deterministic filesystem APIs.

**Exclusions:** UI presentation except scope scan results.

## Deliverable Scope

Parse `_STATUS.md` and enforce forward-only actor-authorized transitions with approval SHA for human gates.

## Anticipated Artifacts

Status parser; transition API/tool; approval SHA tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-028 |
| SupportsObjectives | OBJ-006 |
| ContextEnvelopeNotes | Lifecycle contract slice with known state machine. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
