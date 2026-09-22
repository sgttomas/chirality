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

**ScopeDescription:** App integration, project-input composition, Codex-custodied private authentication, current shared configuration, retained adapter compatibility and conformance evidence under D-GOV-43/A2.

**InclusionCriteria:** Current Codex observation; App client/service-child packaging; additive project instructions; credential separation and configuration conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-019, SOW-020, SOW-021 |
| SupportsObjectives | OBJ-004, OBJ-008 |
| ContextEnvelopeNotes | App security/conformance slice; the daemon exclusively owns runtime credentials and generic network semantics. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Anthropic network/key bridge remains current shipped adapter only; future providers require bounded tranches.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
