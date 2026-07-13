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

**ScopeDescription:** Provider-adapter adoption probe, first-adapter SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** First-adapter/provider-boundary implementation.

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

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Prompt/persona composition must support provider-neutral runtime contracts and policy-mediated tool posture.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
