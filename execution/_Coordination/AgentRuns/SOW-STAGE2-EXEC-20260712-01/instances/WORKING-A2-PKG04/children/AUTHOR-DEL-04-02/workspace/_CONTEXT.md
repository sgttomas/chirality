# Context: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-02 |
| DeliverableName | SdkOptionsBuilder and Settings Isolation |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Provider-adapter adoption probe, first-adapter SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** First-adapter/provider-boundary implementation.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Build deterministic first-adapter SDK options from session, persona, mode, tools, hooks, MCP, subagents, resume, and settings policy.

## Anticipated Artifacts

`sdk-options-builder.ts`; settings isolation tests; visible tool metadata

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052 |
| SupportsObjectives | OBJ-004, OBJ-005 |
| ContextEnvelopeNotes | Configuration/security slice; permissions deepen in PKG-06. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Options/settings work must generalize to adapter settings policy while preserving current Claude SDK isolation.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
