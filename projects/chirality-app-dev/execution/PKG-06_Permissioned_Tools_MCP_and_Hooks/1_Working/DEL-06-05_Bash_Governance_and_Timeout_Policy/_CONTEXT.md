# Context: DEL-06-05 Bash Governance and Timeout Policy

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DeliverableID | DEL-06-05 |
| DeliverableName | Bash Governance and Timeout Policy |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks.

**InclusionCriteria:** Runtime tool execution governance.

**Exclusions:** Domain-engine operation semantics except protected-path hooks.

## Deliverable Scope

Keep Bash denied by default and require explicit mode, timeout, capture, output storage, interrupt, and audit behavior before enabling.

## Anticipated Artifacts

Bash deny/default tests; timeout/capture policy; output metadata tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-062 |
| SupportsObjectives | OBJ-005 |
| ContextEnvelopeNotes | Single powerful-tool guardrail. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.
