# Context: DEL-06-03 Initial Chirality MCP Read Tools

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-03 |
| DeliverableName | Initial Chirality MCP Read Tools |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance.

**InclusionCriteria:** Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence.

**Exclusions:** Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics.

## Deliverable Scope

Expose accepted deterministic Chirality read operations through the current Runtime application-tool interface, with descriptor ownership in DEL-06-02 and handler/composition ownership here. The old in-process SDK MCP assembly remains compatibility evidence.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `tests/application-tools-composition.test.ts`; App `frontend/src/lib/harness/mcp/**` retained read/propose surface and project readers.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-048, SOW-050, SOW-064, SOW-082 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | In-process wrapper and extension-boundary share of SOW-064; catalog validation and collision prevention remain DEL-06-02. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: MCP read tools must remain Chirality-owned and provider-adapter-safe.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve status_read, deps_read and scope_scan semantics, bounded workspace scans, schema/read-only/concurrency/interruption/summarization descriptors, structured unknown-name failure and safe permission/start/completion/failure evidence. _STATUS.md remains lifecycle truth; Dependencies.csv is structured dependency truth, with explicit absence or secondary prose summary when absent, never invented rows. Scaffold remains preview-only in this slice. SOW-082 propose validates the folder/role/delegation/workflow/policy tuple, plan references and once-per-chat decline, emitting proposal.offered without automatic activation.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
