# Datasheet: DEL-06-03 Initial Chirality MCP Read Tools

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-06-03 |
| DeliverableName | Initial Chirality MCP Read Tools |
| PackageID | PKG-06 |
| PackageName | Permissioned Tools, MCP, and Hooks |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Scope | Expose in-process deterministic MCP tools for status read, dependency read, scope scan, and scaffold preview/dry-run. |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| MCP naming namespace | `mcp__chirality__*` | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.4 |
| Initial tool names in scope | `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, `mcp__chirality__scaffold` preview/dry-run behavior where applicable | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Adjacent tool names not implemented as read-tool scope | `mcp__chirality__status_transition` and `mcp__chirality__deps_write` are write/gated tools and belong to later or adjacent write/lifecycle surfaces. | `docs/SPEC.md` Section 14.2; `docs/PRD.md` Sections 8.13 and 8.14 |
| Required wrapper metadata | Schema, permissions, read-only behavior, concurrency behavior, interruption behavior, execution behavior, and summarization behavior. | `docs/PRD.md` Section 8.13 FR-079 |
| Tool-surface ordering | Deterministic ordering, naming, MCP server IDs, and allow/deny lists for a given session/persona/mode/option set. | `docs/PRD.md` Section 8.13 FR-080; `docs/SPEC.md` Section 14.3 |
| Permission posture | MCP is a transport, not a bypass; tools pass through permission, hook, path, redaction, and event logging policy. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/DIRECTIVE.md` Section 14 |
| Read-before-write sequencing | Read-only capability lands before write/edit/shell capability; write/edit and bash stay denied until later phases activate them. | `docs/PRD.md` Section 8.13 FR-082; `docs/PLAN.md` R2 |
| Validation marker | `section9.chirality_mcp_status_dependencies` is a runtime validation ID for status/dependency MCP behavior. | `docs/SPEC.md` Section 19.3 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Permission mode compatibility | `readOnly` exposes or allows read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/PRD.md` Section 8.14 FR-091; `docs/TYPES.md` Section 8.1 |
| Deny precedence | Explicit denies from policy, path containment, hook, governance, SDK deny rule, or human gate block execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/PRD.md` Section 8.14 FR-089 |
| `allowedTools` limitation | `allowedTools` is not a restriction boundary by itself. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| Status truth source | `_STATUS.md` is canonical human-readable lifecycle state. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1 |
| Dependency truth source | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative for dependencies. | `docs/CONTRACT.md` Section 1.7 K-DEP-1 |
| Scaffold posture | `mcp__chirality__scaffold` is gated; this deliverable should cover preview/dry-run behavior where appropriate, not uncontrolled scaffold writes. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Source-state warning | `docs/PRD.md` is accessible but has a reference-hash mismatch in `_REFERENCES.md`; per task brief this is treated as a source-state warning, not a blocker. | `_REFERENCES.md` REF-006; task brief |

## Construction

| Construct | Expected Shape | Source |
|---|---|---|
| MCP definitions | In-process SDK MCP tool definitions using `createSdkMcpServer()` / `tool()` or equivalent SDK APIs. | `docs/PRD.md` Section 8.13 FR-119 |
| Wrapper contract | Shared wrapper metadata for tool descriptors, permission classification, execution, result summarization, and event/redaction behavior. | `docs/PRD.md` Section 8.13 FR-079; `docs/CONTRACT.md` Section 1.6 K-MCP-1 |
| Status read | Read `_STATUS.md` snapshot. Exact parser/API adapter TBD and should align with the status lifecycle API owner. | `docs/SPEC.md` Sections 14.2 and 17.2 |
| Dependency read | Read and validate `Dependencies.csv` when present. If only `_DEPENDENCIES.md` exists, return an explicit secondary-summary / not-structured-tracked result rather than inventing rows; final API shape remains TBD pending DEL-07-05. | `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` Extracted Dependency Register |
| Scope scan | Run bounded workspace scope scan. Exact scanner interface TBD and should align with workspace scope API. | `docs/SPEC.md` Sections 14.2 and 17.2 |
| Scaffold preview/dry-run | Wrap scaffold service or dry-run preview without opening uncontrolled write behavior. Exact preview schema TBD. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Tests | MCP tool definitions and wrapper metadata are unit-tested and deterministic. | `docs/PRD.md` Section 8.13 FR-079 |

## Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Incorporated with TBD boundary | Dependency read fallback now states the safe executable behavior for `_DEPENDENCIES.md`-only state and keeps final API shape `TBD` pending DEL-07-05. Source reread: `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` Extracted Dependency Register. |

## References

- `_CONTEXT.md` for deliverable identity, package scope, and anticipated artifacts.
- `_REFERENCES.md` for source corpus and source-state warning.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6, 7, 9, and 10A for objective, deliverable, SOW, and invariant-family mapping.
- `docs/DIRECTIVE.md` Sections 13-14 for runtime integration boundaries and capability-forward MCP posture with explicit hard-deny precedence.
- `docs/CONTRACT.md` Sections 1.6-1.7 for binding tool, MCP, permission, status, dependency, and invention invariants.
- `docs/SPEC.md` Sections 14, 15, 17.2, and 19.3 for tool names, modes, API surfaces, and validation IDs.
- `docs/TYPES.md` Sections 8.1-8.4 for permission and MCP vocabulary.
- `docs/PLAN.md` R2 and R6 for sequencing and MCP extension boundaries.
- `docs/PRD.md` Sections 8.13-8.14 and R2 traceability; HASH_MISMATCH warning recorded in `_REFERENCES.md`.
