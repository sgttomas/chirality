# Context: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-01 |
| DeliverableName | ChiralityPermissionOverlay and Mode Mapping |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Capability-forward permission policy with explicit deny precedence, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Implement structured permission decisions, explicit deny precedence, capability-policy mode mapping, and `canUseTool` approval mediation.

## Anticipated Artifacts

Permission overlay module; decision records; readOnly/dontAsk/ask tests; hard-deny precedence tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-054, SOW-055, SOW-056, SOW-058 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Permission-policy slice; hooks are separated. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Permission overlay must become capability-forward with explicit hard-deny precedence, not blanket denial.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
