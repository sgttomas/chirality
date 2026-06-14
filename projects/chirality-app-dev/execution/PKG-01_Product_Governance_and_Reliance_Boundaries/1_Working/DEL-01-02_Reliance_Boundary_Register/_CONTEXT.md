# Context: DEL-01-02 Reliance Boundary Register

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-02 |
| DeliverableName | Reliance Boundary Register |
| ResponsibleParty | TBD |
| Type | REQ_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline.

**InclusionCriteria:** Governance docs, acceptance checks, product identity, scope boundaries.

**Exclusions:** Runtime implementation details except as required for boundary enforcement.

## Deliverable Scope

Map every P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundary to a concrete enforcement surface.

## Anticipated Artifacts

`docs/harness/reliance_boundary_register.md`; enforcement matrix; test index

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-037, SOW-045, SOW-054, SOW-057, SOW-074 |
| SupportsObjectives | OBJ-002, OBJ-005, OBJ-009 |
| ContextEnvelopeNotes | A documentation/requirements slice with strong implementation implications. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Reliance-boundary mapping must distinguish useful agent tool use from explicit hard-deny boundaries.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
