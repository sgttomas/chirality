# Context: DEL-04-04 PersonaComposer from Instruction Root

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-04 |
| DeliverableName | PersonaComposer from Instruction Root |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** SDK-facing implementation and provider boundary.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Replace stub prompt behavior with instruction-root governance, active persona, working-root policy, mode, and tool-surface composition.

## Anticipated Artifacts

`persona-composer.ts`; persona content hash tests; boot fingerprint updates

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-017, SOW-030 |
| SupportsObjectives | OBJ-004, OBJ-007 |
| ContextEnvelopeNotes | Prompt composition slice with bounded artifacts. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
