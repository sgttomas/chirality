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

**ScopeDescription:** Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts.

**InclusionCriteria:** Runtime audit records and replay surfaces.

**Exclusions:** Tool permission semantics.

## Deliverable Scope

Redact provider, SDK, tool, and run logs so key material and secrets do not enter runtime records.

## Anticipated Artifacts

Redaction helper; run logger tests; provider error fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-021, SOW-041 |
| SupportsObjectives | OBJ-003, OBJ-008 |
| ContextEnvelopeNotes | Focused security utility. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
