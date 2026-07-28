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

Maintain deterministic App/project tool catalog and requested tool names, reject unknown or colliding client tool names, and verify daemon read-tool exposure before writes/bash.

## Anticipated Artifacts

App tool catalog/request resolver; catalog metadata; unknown-tool and name-collision tests; daemon visible-surface conformance fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-047, SOW-049, SOW-050, SOW-064 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Catalog, validation, and collision-prevention share of SOW-064; no MCP wrapper implementation or remote MCP, plugin, or marketplace scope. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Read tool exposure remains early capability work under policy and evidence, not suppressive default denial.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
