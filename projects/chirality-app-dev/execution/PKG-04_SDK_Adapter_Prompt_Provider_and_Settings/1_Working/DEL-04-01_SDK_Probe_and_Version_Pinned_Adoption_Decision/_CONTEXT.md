# Context: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-01 |
| DeliverableName | SDK Probe and Version-Pinned Adoption Decision |
| ResponsibleParty | TBD |
| Type | REQ_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** SDK-facing implementation and provider boundary.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Confirm SDK package version, message sequence, permissions, hooks, MCP, sessions, storage, interrupts, packaging, and fallback triggers.

## Anticipated Artifacts

SDK probe notes; version decision; fallback criteria; residual-risk notes

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

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
