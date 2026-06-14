# Context: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-01 |
| DeliverableName | Governance Alignment, Human Authority, and Project Truth |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline.

**InclusionCriteria:** Governance docs, acceptance checks, product identity, scope boundaries.

**Exclusions:** Runtime implementation details except as required for boundary enforcement.

## Deliverable Scope

Keep PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and active decomposition mutually consistent while preserving human authority, filesystem project truth, accepted git history, and runtime-audit boundaries as the runtime evolves.

## Anticipated Artifacts

Governance consistency notes; human-authority checklist; project-truth checklist; doc diff checklist; acceptance checklist

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-074, SOW-075 |
| SupportsObjectives | OBJ-009 |
| ContextEnvelopeNotes | Cross-document review is broad but bounded to governance alignment and reliance-boundary preservation. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Governance alignment must reflect provider-adapter strategy, Pi pattern-corpus posture, and capability-forward policy mediation.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
