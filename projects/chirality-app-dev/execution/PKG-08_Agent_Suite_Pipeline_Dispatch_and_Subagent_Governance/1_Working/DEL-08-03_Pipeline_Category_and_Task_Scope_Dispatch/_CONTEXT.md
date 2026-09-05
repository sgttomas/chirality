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

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, project delegation authority, daemon-client dispatch, sealed child context, and checkout-contained AgentRuns.

**InclusionCriteria:** Agent OS authority, instructions, approval references, client dispatch, and project evidence.

**Exclusions:** Generic provider/SDK mechanics and daemon-owned operational delegation execution/state.

## Deliverable Scope

Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics,
category/task-scope interpretation, dynamic scope, and disabled-option rules for
contextual Run consumers.

Applied decomposition row L370 (SCA-APP-010 Gate 5, 2026-09-04) notes: Semantic
dispatch owner; the contextual Pipeline presentation is retired from the active
shell by SCA-APP-010 (code retained), so no active presentation consumer exists;
any later consumer may not infer plans/tasks from conversational prose.

## Anticipated Artifacts

Dispatch contract tests; Pipeline selector tests; knowledge-type discovery;
dynamic-scope and disabled-option handling

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-007, SOW-026 |
| SupportsObjectives | OBJ-001, OBJ-007 |
| ContextEnvelopeNotes | Semantic dispatch slice consumed by UI presentation without authority transfer. |

## Ownership Boundary (SCA-APP-004 as amended by SCA-APP-010)

- DEL-08-03 owns DECOMP/PREP/TASK/AUDIT lane and dynamic task-scope semantics.
- DEL-02-02 owns the right-panel Who is working view, Workflows view, and
  proposal card presentation (applied row L308); the contextual Pipeline
  presentation is retired from the active shell by SCA-APP-010 (DEC-025; code,
  routes, and tests retained), so DEL-08-03's dispatch semantics have no
  presentation consumer until a separate amendment re-hosts one.
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
