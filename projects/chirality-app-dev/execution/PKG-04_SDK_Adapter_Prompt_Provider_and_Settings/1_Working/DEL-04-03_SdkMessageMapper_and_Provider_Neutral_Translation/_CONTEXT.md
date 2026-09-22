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

**ScopeDescription:** App integration, project-input composition, Codex-custodied private authentication, current shared configuration, retained adapter compatibility and conformance evidence under D-GOV-43/A2.

**InclusionCriteria:** Current Codex observation; App client/service-child packaging; additive project instructions; credential separation and configuration conformance.

**Exclusions:** Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification.

## Deliverable Scope

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-040, SOW-044, SOW-051 |
| SupportsObjectives | OBJ-002, OBJ-004 |
| ContextEnvelopeNotes | App client mapping surface; generic adapter/event semantics remain Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Message mapping must translate provider/SDK messages into Chirality contracts and avoid Claude/SDK leakage.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
