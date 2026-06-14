# Context: DEL-01-03 Product Identity and Professional Boundary Copy

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-03 |
| DeliverableName | Product Identity and Professional Boundary Copy |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline.

**InclusionCriteria:** Governance docs, acceptance checks, product identity, scope boundaries.

**Exclusions:** Runtime implementation details except as required for boundary enforcement.

## Deliverable Scope

Preserve Chirality identity and human-only professional authority across UI, docs, packaging, runtime messages, and future domain notices.

## Anticipated Artifacts

UI copy guidelines; release review checklist; boundary notice examples

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-071, SOW-074 |
| SupportsObjectives | OBJ-009, OBJ-010 |
| ContextEnvelopeNotes | Focused copy and review deliverable. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Product identity and professional-boundary copy must remain Chirality-owned and provider-neutral.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.
