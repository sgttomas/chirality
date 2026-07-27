# Context: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-02 |
| DeliverableName | Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, project delegation authority, daemon-client dispatch, sealed child context, and checkout-contained AgentRuns.

**InclusionCriteria:** Agent OS authority, instructions, approval references, client dispatch, and project evidence.

**Exclusions:** Generic provider/SDK mechanics and daemon-owned operational delegation execution/state.

## Deliverable Scope

Keep UI aliases, canonical agent names, persona resolution, guarded
dialogue/session selection, route/query mappings, and legacy matrix behavior
consistent. The fixed matrix is a compatibility surface, not target shell
architecture.

## Anticipated Artifacts

Alias resolver tests; guarded session-selection tests; route/query fixtures;
legacy matrix compatibility and unavailable-persona tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-005, SOW-006, SOW-017 |
| SupportsObjectives | OBJ-001, OBJ-007 |
| ContextEnvelopeNotes | Focused routing/alias/selection slice; legacy matrix retained only for compatibility. |

## SCA-APP-004 Ownership Boundary

- DEL-08-02 owns alias resolution, navigation intent, guarded
  dialogue/session selection, persona resolution, and legacy route/query/matrix
  compatibility.
- DEL-02-01 and DEL-02-02 own shell and Coordination Panel presentation.
- DEL-05-04 owns transcript/replay and selected-session projection.
- DEL-08-03 owns DECOMP/PREP/TASK/AUDIT dispatch semantics.
- DEL-08-05 remains the unchanged owner of canonical child-run records and
  exact parentage/return references.
- DEL-08-02 does not own Work status, lifecycle, approval, dispatch,
  transcript persistence, parentage, scheduling, direct child messaging, or
  shell layout.

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
