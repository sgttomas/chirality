# Context: DEL-02-05 API Key UI and Runtime Feedback

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-05 |
| DeliverableName | API Key UI and Runtime Feedback |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Dialogue-centred shell, Woven Dialogue artifact presentation, Navigator, Work/Agents Coordination Panel, activity shelf, re-hosted Workbench/Pipeline/toolkit/settings, compatibility surfaces, and non-authoritative local UI state.

**InclusionCriteria:** Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior.

**Exclusions:** Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority.

## Deliverable Scope

Provide API key entry/status UI, secure-storage feedback, selected-working-root attachment selection with multi-select preview and remove/clear controls, typed runtime errors, and retry-preserving draft and attachment failure states.

## Anticipated Artifacts

API key settings panel; attachment picker and preview chips; remove/clear controls; typed error display; secure-storage error UI; retry-state preservation tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-013, SOW-019, SOW-023 |
| SupportsObjectives | OBJ-001, OBJ-008 |
| ContextEnvelopeNotes | Cohesive dialogue-input and runtime-feedback UI slice; DEL-09-06 retains server-side attachment, network, key, and renderer security validation. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-112 resolves the SOW-023 traceability delta in favor of inclusion because decomposition v3.2 explicitly maps SOW-023 to DEL-02-05; the new anchor is derivative traceability, not a lifecycle decision.
