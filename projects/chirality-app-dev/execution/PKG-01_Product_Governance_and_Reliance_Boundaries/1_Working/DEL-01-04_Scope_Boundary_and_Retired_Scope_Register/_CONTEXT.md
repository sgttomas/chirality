# Context: DEL-01-04 Scope Boundary and Retired Scope Register

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-04 |
| DeliverableName | Scope Boundary and Retired Scope Register |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline.

**InclusionCriteria:** Governance docs, acceptance checks, product identity, scope boundaries.

**Exclusions:** Runtime implementation details except as required for boundary enforcement.

## Deliverable Scope

Keep remote MCP, plugins, shipped bypass, non-macOS packaging, domain operations, and retired PKG-08 items outside active scope unless amended.

## Anticipated Artifacts

Out-of-scope register; retired-scope notes; amendment triggers

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-065, SOW-076, SOW-077, SOW-078 |
| SupportsObjectives | OBJ-009 |
| ContextEnvelopeNotes | Focused scope guard. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Scope boundary register must prohibit Pi adapter/import/spike and concrete provider expansion without future tranche approval.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
