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

**ScopeDescription:** App integration, project-input composition, packaged-daemon credential-boundary participation, provider-adapter compatibility, settings isolation, and conformance evidence.

**InclusionCriteria:** First-adapter probe; App client/packaging integration; prompt/project inputs; provider and settings conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

Preserve App credential entry/status and packaged-daemon `safeStorage` boundary participation, verify ruled provider/network behavior and redacted client handoff, and prevent unauthorized expansion without creating a second credential owner.

## Anticipated Artifacts

App credential UI/client bridge; packaged-daemon safeStorage conformance; network and provider-expansion tests; redaction fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-019, SOW-020, SOW-021 |
| SupportsObjectives | OBJ-004, OBJ-008 |
| ContextEnvelopeNotes | App security/conformance slice; the daemon exclusively owns runtime credentials and generic network semantics. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Anthropic network/key bridge remains current shipped adapter only; future providers require bounded tranches.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
