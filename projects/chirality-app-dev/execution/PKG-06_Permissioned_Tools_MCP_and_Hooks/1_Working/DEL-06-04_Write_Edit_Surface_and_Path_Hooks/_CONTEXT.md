# Context: DEL-06-04 Write/Edit Surface and Path Hooks

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-04 |
| DeliverableName | Write/Edit Surface and Path Hooks |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | L |

## Package Scope

**ScopeDescription:** App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance.

**InclusionCriteria:** Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence.

**Exclusions:** Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics.

## Deliverable Scope

Preserve governed application write/edit controls and honestly verify native Codex enforcement under the selected policy. Legacy App write tools/hooks do not establish native-tool containment.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App governed mutation routes and retained `frontend/src/lib/harness/tool-path-policy.ts`, write/edit hooks and tests.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-027, SOW-057, SOW-060 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | Spans filesystem policy and SDK tool use but remains one tool-governance domain. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Write/edit hooks remain gated by path containment and explicit hard-deny boundaries after read surface is proven.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Chirality-owned writes retain pre-execution authorization, project containment, ordinary instruction-root protection, symlink rejection, exact edit preconditions, fail-closed hook/validation outcomes, practical atomicity, diff/summary, safe provenance and evidence for denials as well as success. Native fileChange approvals and sandbox provide conditional enforcement; Full access does not prove universal write prevention. Managed-child declared read/write scopes remain normative and their actual host enforcement must be verified. status_transition/deps_write are retained in-process operations; scaffold_preview is read-only. Attachment checks remain DEL-09-06-owned.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
