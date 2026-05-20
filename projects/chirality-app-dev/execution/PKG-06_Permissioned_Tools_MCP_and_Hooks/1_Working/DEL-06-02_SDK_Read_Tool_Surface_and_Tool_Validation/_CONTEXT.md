# Context: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-02 |
| DeliverableName | SDK Read Tool Surface and Tool Validation |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Resolve `opts.tools` to registered SDK built-ins or Chirality MCP names, reject unknowns, and expose read tools before writes/bash.

## Anticipated Artifacts

Tool resolver; unknown-tool tests; deterministic ordering fixtures

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-047, SOW-049, SOW-050 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Tool exposure slice bounded to read-first behavior. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
