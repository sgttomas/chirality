# Context: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-02 |
| DeliverableName | SDK Read Tool Surface and Tool Validation |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance.

**InclusionCriteria:** Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence.

**Exclusions:** Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics.

## Deliverable Scope

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-047, SOW-049, SOW-050, SOW-064 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Catalog, validation, and collision-prevention share of SOW-064; no MCP wrapper implementation or remote MCP, plugin, or marketplace scope. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment — historical basis

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Read tool exposure remains early capability work under policy and evidence, not suppressive default denial.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## Current interface applicability — 2026-09-22

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
