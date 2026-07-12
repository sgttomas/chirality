# Context: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-01 |
| DeliverableName | First-Adapter Probe and Version-Pinned Adoption Decision |
| ResponsibleParty | TBD |
| Type | REQ_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Provider-adapter adoption probe, first-adapter SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** First-adapter/provider-boundary implementation.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Confirm provider-adapter viability and Claude Agent SDK / Anthropic as first concrete adapter, including package version, message sequence, permissions, hooks, MCP, sessions, storage, interrupts, packaging, fallback triggers, and future-provider criteria.

## Anticipated Artifacts

First-adapter probe notes; version decision; fallback criteria; future-provider criteria; residual-risk notes

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-018, SOW-044, SOW-046 |
| SupportsObjectives | OBJ-004 |
| ContextEnvelopeNotes | Documentation/probe slice with no new user tool exposure. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: First-adapter probe must be framed as Claude Agent SDK / Anthropic within provider-adapter architecture, not permanent provider scope.

Package-local review status: `SCA-APP-001-CLOSURE-002` refreshed the base context fields and reviewed or updated targeted local kit wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` against the accepted SCA. Remaining `TBD` values and non-SCA dependency lifecycle states retain their prior status.

This package-local refresh does not change runtime source, package manifests, lockfiles, desktop wrapper files, provider implementation, Pi implementation, or release-readiness posture.

## D-APP-56 approving-role deferral (2026-07-12)

R4-P47 explicitly defers assignment of the adoption-verdict approving role. The field remains `TBD` until an accountable human assigns it; no agent role is inferred.
