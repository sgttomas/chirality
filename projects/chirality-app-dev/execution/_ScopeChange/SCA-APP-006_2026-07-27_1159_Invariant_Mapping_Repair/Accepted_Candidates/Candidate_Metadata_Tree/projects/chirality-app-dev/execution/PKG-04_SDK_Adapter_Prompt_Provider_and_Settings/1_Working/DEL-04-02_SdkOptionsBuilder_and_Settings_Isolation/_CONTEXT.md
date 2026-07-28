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

**ScopeDescription:** App integration, project-input composition, packaged-daemon credential-boundary participation, provider-adapter compatibility, settings isolation, and conformance evidence.

**InclusionCriteria:** First-adapter probe; App client/packaging integration; prompt/project inputs; provider and settings conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

Supply deterministic App/project option inputs and verify Root-runtime adapter isolation for session, persona, mode, requested tools, hooks, project MCP acts, subagents, resume, and settings policy.

## Anticipated Artifacts

App option-input adapter; settings-isolation conformance tests; visible tool metadata

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052, SOW-076 |
| SupportsObjectives | OBJ-004, OBJ-005 |
| ContextEnvelopeNotes | App configuration/conformance slice; generic option mapping and credentials remain Root-owned. SOW-076 is a boundary-only trace: ambient settings and shipped bypass remain OUT. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Options/settings work must generalize to adapter settings policy while preserving current Claude SDK isolation.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
