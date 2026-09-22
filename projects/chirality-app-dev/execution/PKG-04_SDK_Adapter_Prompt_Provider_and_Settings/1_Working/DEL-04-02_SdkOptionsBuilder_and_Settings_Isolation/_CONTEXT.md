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

**ScopeDescription:** App integration, project-input composition, Codex-custodied private authentication, current shared configuration, retained adapter compatibility and conformance evidence under D-GOV-43/A2.

**InclusionCriteria:** Current Codex observation; App client/service-child packaging; additive project instructions; credential separation and configuration conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052, SOW-076 |
| SupportsObjectives | OBJ-004, OBJ-005 |
| ContextEnvelopeNotes | App configuration/conformance slice; generic option mapping and credentials remain Root-owned. SOW-076 is a boundary-only trace: ambient settings and shipped bypass remain OUT. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Options/settings work must generalize to adapter settings policy while preserving current Claude SDK isolation.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
