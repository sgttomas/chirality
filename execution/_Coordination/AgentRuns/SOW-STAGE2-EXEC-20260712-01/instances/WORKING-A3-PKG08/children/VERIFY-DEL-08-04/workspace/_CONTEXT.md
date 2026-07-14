# Context: DEL-08-04 Type 2 Subagent Governance Bridge

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-04 |
| DeliverableName | Type 2 Subagent Governance Bridge |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, Type 2 subagent governance and child records.

**InclusionCriteria:** Agent OS behavior and delegation.

**Exclusions:** General SDK adapter mechanics.

## Deliverable Scope

Bridge fail-closed subagent governance to SDK agents with allowlists, sealed context, approval refs, and restricted child tools/cwd.

## Anticipated Artifacts

`evaluateSubagentGovernance` bridge; SDK agent definitions; `Agent` hook tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-063 |
| SupportsObjectives | OBJ-005, OBJ-007 |
| ContextEnvelopeNotes | Focused subagent governance execution. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
