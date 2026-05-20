# Context: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-06 |
| DeliverableName | Hook Lifecycle and Compaction Mirror |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Record hook start/stop/failure, stop/finalization, and SDK compaction boundaries into Chirality events.

## Anticipated Artifacts

Hook lifecycle mapper; `context.compacted` tests; terminal hook fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-057, SOW-061 |
| SupportsObjectives | OBJ-003, OBJ-005 |
| ContextEnvelopeNotes | Hook event mirror slice. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
