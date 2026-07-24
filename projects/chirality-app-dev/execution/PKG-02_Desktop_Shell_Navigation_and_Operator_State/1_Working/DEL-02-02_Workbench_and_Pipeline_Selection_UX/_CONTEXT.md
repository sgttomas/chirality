# Context: DEL-02-02 Work/Agents Coordination, Workbench, and Pipeline UX

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-02 |
| DeliverableName | Work/Agents Coordination, Workbench, and Pipeline UX |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Dialogue-centred shell, Woven Dialogue artifact
presentation, Navigator, Work/Agents Coordination Panel, Activity Shelf,
re-hosted Workbench/Pipeline/toolkit/settings, compatibility surfaces, and
non-authoritative local UI state.

**InclusionCriteria:** Human-agent dialogue, artifact collaboration,
coordination presentation, and operator workflow behavior.

**Exclusions:** Runtime engine internals, canonical session/evidence ownership,
arbitrary orchestration graphs, automatic intent inference, and
project-control-plane authority.

## Deliverable Scope

Re-host Workbench and Pipeline around the central dialogue and present
explicitly recorded plans/tasks and agent/session selections with source,
authority class, responsible reference, status basis, currency, and evidence.
Preserve disabled states, stale/empty/conflict disclosure, and deep-link
intent. DEL-08-02 retains routing and guarded selection, DEL-08-03 retains
dispatch, DEL-08-05 retains child records, and DEL-05-04 retains
replay/projection semantics.

## Anticipated Artifacts

Workbench/Pipeline views; Work/Agents coordination presentation; provenance
labels; stale/empty-state and query compatibility tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-006, SOW-007 |
| SupportsObjectives | OBJ-001, OBJ-007 |
| ContextEnvelopeNotes | This deliverable composes presentation over admitted sources; it does not create plan, dispatch, parentage, lifecycle, approval, or runtime authority. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2
SOFTWARE_DECOMP working surface and retains its physical name for compatibility.
SCA-APP-004 and its owner-approved amendment prospectively control the current
presentation target. Downstream TASK work must preserve `ResponsibleParty:
TBD` until a human assigns ownership. Work and Agents remain rebuildable,
evidence-conditional projections; conversational prose and panel-local state
must not be converted into project truth.
