# Context: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-02 |
| DeliverableName | SdkOptionsBuilder and Settings Isolation |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** SDK-facing implementation and provider boundary.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Build deterministic SDK options from session, persona, mode, tools, hooks, MCP, subagents, resume, and settings policy.

## Anticipated Artifacts

`sdk-options-builder.ts`; settings isolation tests; visible tool metadata

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052 |
| SupportsObjectives | OBJ-004, OBJ-005 |
| ContextEnvelopeNotes | Configuration/security slice; permissions deepen in PKG-06. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Options/settings work must generalize to adapter settings policy while preserving current Claude SDK isolation.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
