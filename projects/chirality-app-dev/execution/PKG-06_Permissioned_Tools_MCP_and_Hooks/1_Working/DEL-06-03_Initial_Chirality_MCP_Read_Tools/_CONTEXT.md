# Context: DEL-06-03 Initial Chirality MCP Read Tools

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-03 |
| DeliverableName | Initial Chirality MCP Read Tools |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Expose in-process deterministic MCP tools for status read, dependency read, scope scan, and scaffold preview/dry-run.

## Anticipated Artifacts

`mcp__chirality__*` definitions; wrapper metadata; MCP tool tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-048, SOW-050 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | Related tools share one MCP wrapper contract. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
## SCA-APP-001 Context Alignment

`SCA-APP-001` is accepted. This deliverable is aligned to the provider-adapter-general runtime strategy: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpus/reference only; permission governance is capability-forward with explicit hard-deny precedence.

Primary impact: MCP read tools must remain Chirality-owned and provider-adapter-safe.

Local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain `STALE_LOCAL_REVIEW_REQUIRED` where they encode prior Anthropic-only, Pi-spike, or blanket deny-first assumptions. Do not treat those local artifacts as refreshed until a bounded package-local review updates or confirms them.
