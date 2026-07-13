# Context: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-02 |
| DeliverableName | HarnessEvent Schema and Append-Only JSONL |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts.

**InclusionCriteria:** Runtime audit records and replay surfaces.

**Exclusions:** Tool permission semantics.

## Deliverable Scope

Persist `turn.accepted`, runtime events, and terminal outcomes as ordered, append-only JSONL.

## Anticipated Artifacts

Event schema; JSONL writer; accepted-turn and terminal-event tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-014, SOW-015, SOW-039 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | Audit-log core slice. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
