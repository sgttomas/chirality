# Context: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-01 |
| DeliverableName | Instruction Root Packaging and Agent Conformance |
| ResponsibleParty | TBD |
| Type | TEST_SUITE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, project delegation authority, daemon-client dispatch, sealed child context, and checkout-contained AgentRuns.

**InclusionCriteria:** Agent OS authority, instructions, approval references, client dispatch, and project evidence.

**Exclusions:** Generic provider/SDK mechanics and daemon-owned operational delegation execution/state.

## Deliverable Scope

Verify required instruction-root assets, agent metadata, write scopes, naming,
section markers, the proposal clauses and named triggers in Agent 0 and Agent 1
packages, skill-declared workflow templates, and organisation-layer packaging
and pins.

Applied decomposition row L368 (SCA-APP-010 Gate 5, 2026-09-04) notes:
Governance assets and checks; no runtime capability expansion; instruction-file
changes under `agents/` or `skills/` ship the routed agent-index change notice.

## Anticipated Artifacts

Agent conformance validator; integrity fixtures; source-completeness checklist

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-030, SOW-031, SOW-073 |
| SupportsObjectives | OBJ-007, OBJ-008 |
| ContextEnvelopeNotes | Governance assets and checks; no runtime capability expansion. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
