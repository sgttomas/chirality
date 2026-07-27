# Context: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-03 |
| DeliverableName | Redacted RunLogger and Secret Hygiene |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

Redact App-originated provider/client presentation and verify that Root-runtime operational records exclude credentials and secrets.

## Anticipated Artifacts

App redaction helper; daemon redaction conformance tests; provider/client error fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-021, SOW-041 |
| SupportsObjectives | OBJ-003, OBJ-008 |
| ContextEnvelopeNotes | App source/presentation security and conformance; no generic run-logger ownership. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
