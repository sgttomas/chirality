# Context: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-03 |
| DeliverableName | SdkMessageMapper and Provider-Neutral Translation |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** SDK-facing implementation and provider boundary.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Translate SDK stream messages into stable `UIEvent`s and provider-neutral `HarnessEvent`s without leaking SDK shape into core contracts.

## Anticipated Artifacts

`sdk-message-mapper.ts`; mapper tests; provider-neutral leakage tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-040, SOW-044, SOW-051 |
| SupportsObjectives | OBJ-002, OBJ-004 |
| ContextEnvelopeNotes | Focused adapter mapping surface. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
