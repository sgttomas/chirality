# Context: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DeliverableID | DEL-04-05 |
| DeliverableName | Anthropic Provider Key, Base URL, and Network Bridge |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation.

**InclusionCriteria:** SDK-facing implementation and provider boundary.

**Exclusions:** Chirality event store internals beyond metadata handoff.

## Deliverable Scope

Preserve API key precedence, Anthropic-only network policy, provider error classification, and redacted SDK environment handoff.

## Anticipated Artifacts

Provider wrapper; key handoff tests; base URL/network tests; redaction fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-019, SOW-020, SOW-021 |
| SupportsObjectives | OBJ-004, OBJ-008 |
| ContextEnvelopeNotes | Security/privacy slice spanning provider boundary. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: Anthropic network/key bridge remains current shipped adapter only; future providers require bounded tranches.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
