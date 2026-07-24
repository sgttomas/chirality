# Context: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-03 |
| DeliverableName | Pipeline Category and Task Scope Dispatch |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, Type 2 subagent governance and child records.

**InclusionCriteria:** Agent OS behavior and delegation.

**Exclusions:** General SDK adapter mechanics.

## Deliverable Scope

Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics,
category/task-scope interpretation, dynamic scope, and disabled-option rules
for contextual Run consumers. DEL-02-02 presents these semantics without
acquiring dispatch authority.

## Anticipated Artifacts

Dispatch contract tests; Pipeline selector and contextual-consumer tests;
knowledge-type discovery; dynamic-scope and disabled-option handling

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-007, SOW-026 |
| SupportsObjectives | OBJ-001, OBJ-007 |
| ContextEnvelopeNotes | Semantic dispatch slice consumed by UI presentation without authority transfer. |

## SCA-APP-004 Ownership Boundary

- DEL-08-03 owns DECOMP/PREP/TASK/AUDIT lane and dynamic task-scope semantics.
- DEL-02-02 owns re-hosted Workbench/Pipeline, contextual Run, and
  Coordination Panel presentation.
- DEL-08-05 remains the unchanged owner of canonical child-run parentage,
  assignments, returns, and artifact references.
- DEL-05-04 owns transcript/replay projection; DEL-08-02 owns aliases and
  guarded agent/session routing.
- DEL-08-03 does not own general project-plan authority, runtime checklist
  truth, lifecycle, approval, scheduling, direct child messaging, replay,
  child parentage, or shell layout.
- Work items may reflect only explicitly recorded sources with provenance,
  status basis, and currency. Conversational prose is never silently
  converted into a plan/task, and runtime completion is never project
  acceptance.

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
