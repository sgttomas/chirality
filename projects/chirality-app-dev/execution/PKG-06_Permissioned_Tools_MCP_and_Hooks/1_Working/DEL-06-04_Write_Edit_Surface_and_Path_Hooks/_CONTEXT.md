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

Gate write/edit execution with project-root containment, instruction-root block, symlink rejection, exact edit preconditions, and provenance hooks.

## Anticipated Artifacts

PreToolUse hooks; write/edit tests; provenance metadata; path policy fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-027, SOW-057, SOW-060 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | Spans filesystem policy and SDK tool use but remains one tool-governance domain. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Write/edit hooks remain gated by path containment and explicit hard-deny boundaries after read surface is proven.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
