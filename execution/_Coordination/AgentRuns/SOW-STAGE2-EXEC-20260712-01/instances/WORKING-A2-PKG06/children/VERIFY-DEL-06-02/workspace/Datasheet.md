# Datasheet: DEL-06-02 SDK Read Tool Surface and Tool Validation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-02 |
| Deliverable name | SDK Read Tool Surface and Tool Validation |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Type | BACKEND_FEATURE_SLICE |
| Responsible party | TBD |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Context envelope | M |
| Scope items | SOW-047, SOW-049, SOW-050 |
| Objective context | OBJ-005 |
| Anticipated artifacts | Tool resolver; unknown-tool tests; deterministic ordering fixtures |

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-047 through SOW-050.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary feature | Resolve `opts.tools` to registered SDK built-ins or Chirality MCP names. | `_CONTEXT.md`; decomposition DEL-06-02 |
| Unknown-tool behavior | Unknown tool names produce structured validation errors and are not silently passed through. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, MATCH status — reconciled under D-APP-38 |
| SDK built-in candidates | `Read`, `LS`, `Glob`, `Grep`, `Write`, `Edit`, `Bash` where available. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.3 |
| Initial read surface | SDK read tools plus Chirality read MCP tools are enabled before write/edit/bash capability. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2 — reconciled under D-APP-38 |
| Chirality MCP namespace | Chirality-specific deterministic tools use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.4 |
| Initial Chirality MCP read candidates | `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and scaffold preview/dry-run where appropriate. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Determinism condition | Tool-surface ordering, naming, MCP server IDs, and allow/deny lists are stable for a given session, persona, mode, and option set. | `docs/PRD.md` Section 8.13, MATCH status; decomposition SOW-049 — reconciled under D-APP-38 |
| Exposure boundary | Tool implementation availability does not imply model exposure. | decomposition SOW-049; `docs/CONTRACT.md` Section 1.6 K-TOOL-2 |
| Restriction boundary | `allowedTools` alone is not a restriction boundary. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |

## Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| Package boundary | DEL-06-02 is bounded to tool exposure and validation; domain-engine operation semantics are excluded except protected-path hooks in adjacent scopes. | `_CONTEXT.md`; decomposition PKG-06 |
| Permission overlay dependency | Capability-forward policy with explicit hard-deny precedence mode semantics and `canUseTool` mediation are adjacent policy inputs, primarily owned by DEL-06-01. | decomposition DEL-06-01 and DEL-06-02 |
| MCP implementation boundary | Chirality MCP tool definitions are adjacent to this resolver, primarily owned by DEL-06-03. | decomposition DEL-06-03 |
| Write/bash sequencing | Write/edit and bash capability remain later-phase surfaces and must not be exposed by the read-first resolver until the required hooks and governance land. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2/R3 — reconciled under D-APP-38 |
| Shipped runtime posture | `readOnly` mode exposes or allows read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/PRD.md` Section 8.14, MATCH status; `docs/TYPES.md` Section 8.1 — reconciled under D-APP-38 |

## Construction

| Component | Construction note | Source |
|---|---|---|
| Tool registry | Maintain an explicit registry of SDK built-ins and Chirality MCP tool names eligible for resolution. Exact registry file path: TBD. | `docs/SPEC.md` Sections 14.1 and 14.2 |
| Resolver input | Consume resolved runtime options, including `opts.tools`, plus session/persona/mode/policy context needed for deterministic exposure. Exact interface shape: TBD. | `docs/PRD.md` FR-023 and Section 8.13, MATCH status — reconciled under D-APP-38 |
| Name validation | Reject unknown `opts.tools` entries with structured validation errors before SDK request construction. | `docs/SPEC.md` Section 14.3; decomposition SOW-047 |
| Deterministic ordering | Normalize the visible tool list into stable order for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` Section 1.6 K-TOOL-1; `docs/PRD.md` FR-080, MATCH status — reconciled under D-APP-38 |
| Read-first filtering | Build the initial exposed surface from SDK read tools and Chirality read MCP tools; exclude or deny write/edit/bash until later phases. | `docs/PRD.md` Section 8.13, MATCH status; `docs/PLAN.md` R2 — reconciled under D-APP-38 |
| Permission handoff | Feed the resolved tool surface into the Chirality permission overlay; do not rely on `allowedTools` alone for restriction. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| Tests | Include unknown-tool tests and deterministic ordering fixtures. Exact test paths: TBD. | `_CONTEXT.md`; decomposition DEL-06-02 |

### Pending Implementation Evidence

| Evidence slot | Current disposition | Source |
|---|---|---|
| Implementation, registry, metadata, and fixture paths | TBD until implementation ownership assigns concrete files; do not infer paths from planned artifact names. (P3: B-001) | `_CONTEXT.md` Anticipated Artifacts; `docs/CONTRACT.md` K-INVENT-1 |
| Terminology boundary | Use "read-first" for sequencing, "read-only" for capability class, and `readOnly` only for the runtime mode token. (P3: B-002) | `docs/TYPES.md` Section 8.1; `docs/PLAN.md` R2 |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2 and 4 | Product-owned runtime governance, filesystem truth, read-before-powerful-tool posture | MATCH |
| REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, and MCP invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, surface rules, mode mapping | MATCH |
| REF-004 | `docs/TYPES.md` Section 8 | Permission modes and tool-surface vocabulary | MATCH |
| REF-005 | `docs/PLAN.md` R2/R3 | Implementation sequencing and acceptance context | MATCH |
| REF-006 | `docs/PRD.md` Sections 8.13, 8.14, R2, KG-005, KG-023 | Product requirements and implementation direction | MATCH status — reconciled under D-APP-38 |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
