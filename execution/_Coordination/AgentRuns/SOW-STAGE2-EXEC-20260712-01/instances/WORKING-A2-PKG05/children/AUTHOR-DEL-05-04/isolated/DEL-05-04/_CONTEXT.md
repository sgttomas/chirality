# Context: DEL-05-04 Runtime Replay and Transcript View

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-04 |
| DeliverableName | Runtime Replay and Transcript View |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts.

**InclusionCriteria:** Runtime audit records and replay surfaces.

**Exclusions:** Tool permission semantics.

## Deliverable Scope

Reconstruct accepted turns, assistant output, tool summaries, terminal states, and SDK transcript links from Chirality events.

## Anticipated Artifacts

Replay parser; transcript reconstruction tests; malformed-tail tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-042, SOW-046 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | Replay/reporting slice over one event store. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
