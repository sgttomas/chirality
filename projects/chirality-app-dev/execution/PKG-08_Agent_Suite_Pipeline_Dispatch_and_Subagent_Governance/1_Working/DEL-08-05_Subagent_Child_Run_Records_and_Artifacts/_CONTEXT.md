# Context: DEL-08-05 Subagent Child Run Records and Artifacts

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-05 |
| DeliverableName | Subagent Child Run Records and Artifacts |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Agent instruction conformance, matrix/pipeline dispatch, project delegation authority, daemon-client dispatch, sealed child context, and checkout-contained AgentRuns.

**InclusionCriteria:** Agent OS authority, instructions, approval references, client dispatch, and project evidence.

**Exclusions:** Generic provider/SDK mechanics and daemon-owned operational delegation execution/state.

## Deliverable Scope

Preserve checkout-contained parent-child AgentRuns, status, evidence, and accepted artifact paths linked to daemon operational delegation records.

## Anticipated Artifacts

Checkout AgentRun records; daemon linkage metadata; child output evidence paths; replay fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-063 |
| SupportsObjectives | OBJ-003, OBJ-007 |
| ContextEnvelopeNotes | Project evidence slice; daemon operational state is non-authoritative. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current execution basis — 2026-09-22

Codex is the sole current MVP engine, hosted as stock app-server under the application-owned Runtime service (D-GOV-43/D-APP-127). ScopeOfWork.md carries the current production claims. Legacy provider/daemon/four-document statements above retain their historical basis and do not qualify the live path. Existing scope, decomposition identity, responsible-party assignment and domain/professional boundaries are unchanged; current obligations and gaps are in `_STATUS.md`.
