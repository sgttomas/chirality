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

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
