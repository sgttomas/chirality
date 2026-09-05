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

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

Consume Root-owned daemon `HarnessEvent` records for App audit/replay surfaces
and verify accepted-turn and terminal-event persistence without owning the
generic event schema or writer; consume the additive `proposal.*` event types
for replay and the proposal card once Root accepts them (SOW-082).

Applied decomposition row L337 (SCA-APP-010 Gate 5, 2026-09-04) notes: App
event-consumption and conformance slice; generic persistence remains Root-owned.

## Anticipated Artifacts

App runtime-event compatibility fixtures; accepted-turn and terminal persistence conformance tests; daemon evidence samples

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-014, SOW-015, SOW-039 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | App event-consumption and conformance slice; generic persistence remains Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
