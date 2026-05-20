# Context: DEL-06-04 Write/Edit Surface and Path Hooks

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-04 |
| DeliverableName | Write/Edit Surface and Path Hooks |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | L |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Gate write/edit execution with project-root containment, instruction-root block, symlink rejection, exact edit preconditions, and provenance hooks.

## Anticipated Artifacts

PreToolUse hooks; write/edit tests; provenance metadata; path policy fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-027, SOW-057, SOW-060 |
| SupportsObjectives | OBJ-005, OBJ-006 |
| ContextEnvelopeNotes | Spans filesystem policy and SDK tool use but remains one tool-governance domain. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
