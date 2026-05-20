# Context: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-01 |
| DeliverableName | ChiralityPermissionOverlay and Mode Mapping |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Implement structured permission decisions, deny-overrides-allow semantics, mode mapping, and `canUseTool` approval mediation.

## Anticipated Artifacts

Permission overlay module; decision records; readOnly/dontAsk/ask tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-054, SOW-055, SOW-056, SOW-058 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Permission-policy slice; hooks are separated. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
