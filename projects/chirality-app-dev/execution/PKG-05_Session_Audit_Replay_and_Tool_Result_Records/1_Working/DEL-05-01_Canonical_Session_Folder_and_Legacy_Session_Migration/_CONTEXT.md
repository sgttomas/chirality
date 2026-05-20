# Context: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-01 |
| DeliverableName | Canonical Session Folder and Legacy Session Migration |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts.

**InclusionCriteria:** Runtime audit records and replay surfaces.

**Exclusions:** Tool permission semantics.

## Deliverable Scope

Introduce `.chirality/sessions/<id>/` layout while keeping legacy `.json` session records listable, resumable, and deletable.

## Anticipated Artifacts

Session folder layout; migration helpers; legacy-read tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-009, SOW-043, SOW-046 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | Data layout slice with compatibility constraints. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
