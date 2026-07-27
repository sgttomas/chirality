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

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

Maintain App-client compatibility for daemon-centralized sessions, including lazy non-destructive access to and migration of legacy project-local session records while preserving list, resume, and delete behavior.

## Anticipated Artifacts

App session-client compatibility layer; legacy-read/migration fixtures; daemon-session conformance evidence

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-009, SOW-043, SOW-046 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | App compatibility and migration-participation slice; daemon sessions remain Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
