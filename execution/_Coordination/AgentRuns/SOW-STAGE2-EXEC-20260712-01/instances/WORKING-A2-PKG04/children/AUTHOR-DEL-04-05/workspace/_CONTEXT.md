# Context: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-05 |
| DeliverableName | Anthropic Provider Key, Base URL, and Network Bridge |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Provider-adapter adoption probe, first-adapter SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** First-adapter/provider-boundary implementation.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Preserve API key precedence, current Anthropic network policy, provider error classification, no unauthorized provider/network expansion, and redacted adapter environment handoff.

## Anticipated Artifacts

Provider wrapper; key handoff tests; base URL/network tests; provider-expansion guard tests; redaction fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-019, SOW-020, SOW-021 |
| SupportsObjectives | OBJ-004, OBJ-008 |
| ContextEnvelopeNotes | Security/privacy slice spanning current provider boundary. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Anthropic network/key bridge remains current shipped adapter only; future providers require bounded tranches.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
