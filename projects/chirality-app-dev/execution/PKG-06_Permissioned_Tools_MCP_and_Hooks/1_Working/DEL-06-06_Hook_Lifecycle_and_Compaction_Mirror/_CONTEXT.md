# Context: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-06 |
| DeliverableName | Hook Lifecycle and Compaction Mirror |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance.

**InclusionCriteria:** Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence.

**Exclusions:** Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics.

## Deliverable Scope

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-057, SOW-061 |
| SupportsObjectives | OBJ-003, OBJ-005 |
| ContextEnvelopeNotes | App project-hook and conformance slice; generic hook execution remains Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Hook lifecycle evidence must support provider-adapter events and capability-policy decisions.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
