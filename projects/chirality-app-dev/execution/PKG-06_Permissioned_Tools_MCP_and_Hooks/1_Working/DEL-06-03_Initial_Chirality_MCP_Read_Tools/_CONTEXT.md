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

Expose in-process deterministic MCP wrappers for status read, dependency read,
scope scan, scaffold preview/dry-run, and the `propose` specification-ladder
tool, and document their in-process extension boundary without opening remote
MCP, plugins, or marketplace scope.

Applied decomposition row L348 (SCA-APP-010 Gate 5, 2026-09-04) notes:
In-process wrapper and extension-boundary share of SOW-064; catalog validation
and collision prevention remain DEL-06-02.

## Anticipated Artifacts

`mcp__chirality__*` definitions; wrapper metadata; in-process extension-boundary
notes; `propose` tool schema, validation, and once-per-chat tests; MCP tool
tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-048, SOW-050, SOW-064, SOW-082 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | In-process wrapper and extension-boundary share of SOW-064; catalog validation and collision prevention remain DEL-06-02. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: MCP read tools must remain Chirality-owned and provider-adapter-safe.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
