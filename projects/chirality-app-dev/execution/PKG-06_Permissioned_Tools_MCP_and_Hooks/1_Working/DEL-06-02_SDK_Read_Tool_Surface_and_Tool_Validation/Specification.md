# Specification: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Scope

DEL-06-02 specifies the read-first SDK tool-surface resolver and validation behavior for PKG-06. It covers mapping `opts.tools` to registered SDK built-ins or Chirality MCP names, rejecting unknown names, producing deterministic tool exposure for a resolved runtime context, and enabling read tools before write/edit/bash capability.

In scope:

- Resolve requested tool names against explicit SDK built-in and Chirality MCP registries.
- Reject unknown tool names with structured validation errors before SDK request construction.
- Produce deterministic tool-surface ordering for stable session/persona/mode/policy inputs.
- Expose SDK read tools and Chirality read MCP tools as the initial user-visible tool surface.
- Ensure implementation availability does not itself imply model exposure.
- Add unknown-tool tests and deterministic ordering fixtures.

Out of scope:

- Capability-forward policy with explicit hard-deny precedence permission decision semantics, mode mapping, and `canUseTool` approval mediation, except where this resolver consumes or forwards their policy outputs. Those are primarily DEL-06-01.
- In-process MCP tool implementation details and wrapper metadata, which are primarily DEL-06-03.
- Write/edit path hooks and provenance capture, which are DEL-06-04.
- Bash enablement and timeout/capture policy, which are DEL-06-05.
- Remote MCP, plugins, broad tool search, marketplace extension, and remote execution, which remain out of current scope without governed amendment.

Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 14 and 15; `docs/CONTRACT.md` Section 1.6; `docs/PRD.md` Section 8.13 with HASH_MISMATCH warning.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-02-REQ-001 | The resolver MUST map `opts.tools` entries only to registered SDK built-ins or registered Chirality MCP tool names. | decomposition SOW-047; `docs/PRD.md` FR-078, HASH_MISMATCH warning |
| DEL-06-02-REQ-002 | Unknown `opts.tools` names MUST produce structured validation errors and MUST NOT be silently passed through to SDK configuration or model context. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` FR-078, HASH_MISMATCH warning |
| DEL-06-02-REQ-003 | SDK built-in mappings MUST use SDK names where available, including read candidates `Read`, `LS`, `Glob`, and `Grep`, and later powerful candidates `Write`, `Edit`, and `Bash`. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.3 |
| DEL-06-02-REQ-004 | Chirality-specific deterministic tools MUST use the `mcp__chirality__*` naming convention and resolve only from the accepted Chirality MCP registry. | `docs/SPEC.md` Sections 14.1 and 14.2; `docs/TYPES.md` Section 8.4 |
| DEL-06-02-REQ-005 | Tool-surface construction MUST be deterministic for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` Section 1.6 K-TOOL-1; `docs/PRD.md` FR-080, HASH_MISMATCH warning |
| DEL-06-02-REQ-006 | Tool implementation availability MUST NOT imply model exposure; a tool must pass resolver and permission-surface checks before exposure. | `docs/CONTRACT.md` Section 1.6 K-TOOL-2; decomposition SOW-049 |
| DEL-06-02-REQ-007 | Initial user-visible capability MUST expose read-only SDK tools and Chirality read MCP tools before write/edit/bash capability. | decomposition SOW-050; `docs/PRD.md` FR-082, HASH_MISMATCH warning |
| DEL-06-02-REQ-008 | Write/edit and bash tools MUST remain excluded or denied by the read-first surface until the later write/bash governance phases activate them. | `docs/PRD.md` Section 8.13, HASH_MISMATCH warning; `docs/PLAN.md` R2/R3 |
| DEL-06-02-REQ-009 | The resolver MUST NOT treat SDK `allowedTools` alone as a restriction boundary. Restriction requires disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture from the permission layer. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-06-02-REQ-010 | Denied tools SHOULD be omitted from model context where possible, while runtime denial remains required for safety. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` FR-081, HASH_MISMATCH warning |
| DEL-06-02-REQ-011 | In `readOnly` mode, the resolved surface MUST expose or allow read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/TYPES.md` Section 8.1; `docs/PRD.md` FR-091, HASH_MISMATCH warning |
| DEL-06-02-REQ-012 | Resolver outputs SHOULD be represented in safe runtime metadata or boot fingerprints, including actual SDK tool names/versions and MCP server versions where available. | `docs/SPEC.md` Section 13; `docs/PRD.md` FR-029, HASH_MISMATCH warning |
| DEL-06-02-REQ-013 | Tests MUST cover unknown tool names, deterministic ordering, and read-before-write/bash sequencing. | `_CONTEXT.md`; decomposition DEL-06-02; `docs/PLAN.md` R2 acceptance |

## Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Section 1.6 | Binding permission/tool/MCP invariants, including deterministic exposure, implementation-vs-exposure separation, and `allowedTools` limitation. |
| `docs/SPEC.md` Section 14 | SDK built-in names, Chirality MCP names, initial tool set, and surface rules. |
| `docs/SPEC.md` Section 15 | Mode mapping and hook context consumed by tool-surface filtering. |
| `docs/TYPES.md` Section 8 | Tool-surface vocabulary, permission modes, and initial MCP names. |
| `docs/PLAN.md` R2/R3 | Sequencing: permission-gated read surface before controlled writes and bash. |
| `docs/PRD.md` Section 8.13 | Product requirements for tool-surface behavior; use with HASH_MISMATCH warning from `_REFERENCES.md`. |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-02-REQ-001, REQ-003, REQ-004 | Unit tests feed known SDK built-in and `mcp__chirality__*` names and assert canonical resolver outputs. |
| DEL-06-02-REQ-002 | Unknown-tool tests assert structured validation error shape and assert unknown names are absent from emitted SDK options/model context. |
| DEL-06-02-REQ-005 | Deterministic ordering fixtures vary input order and assert stable normalized output for the same session/persona/mode/policy context. |
| DEL-06-02-REQ-006 | Tests assert registered implementation availability is insufficient unless resolver and permission-surface checks include the tool. |
| DEL-06-02-REQ-007, REQ-008, REQ-011 | Read-first sequencing tests assert read tools can resolve in initial mode and write/edit/bash tools remain excluded or hard-denied until later policies are active. |
| DEL-06-02-REQ-009 | Tests assert `allowedTools` is not treated as containment and cannot bypass deny inputs from the permission layer. |
| DEL-06-02-REQ-010 | Surface-filtering tests assert denied tools are omitted where possible and still rejected if called. |
| DEL-06-02-REQ-012 | Metadata or boot-fingerprint tests assert resolved tool names/versions and MCP server identifiers are stable and safe to record. Exact metadata path: TBD. |
| DEL-06-02-REQ-013 | Test suite includes DEL-06-02 traceability markers or fixture names. Exact test paths: TBD. |

### Pass 3 Verification Evidence Disposition

| ItemID | Disposition | Source reread evidence |
|---|---|---|
| C-001 | Incorporated as a verification-evidence requirement while concrete implementation paths remain TBD. Resolver, registry, deterministic-ordering, and read-first evidence must be named before closure. | `docs/CONTRACT.md` K-TOOL-1/K-TOOL-2; `docs/SPEC.md` Sections 13 and 14.3 |
| D-001 | Incorporated as explicit tests for permission-boundary bypass cases: `allowedTools` cannot override deny inputs, and implementation availability alone cannot expose a tool. | `docs/CONTRACT.md` K-PERM-3 and K-TOOL-2; `docs/SPEC.md` Section 14.3 |
| E-001 | Converted to a metadata-path TBD. Safe metadata or boot-fingerprint evidence is required, but the exact record path is not assigned in the current sources. | `docs/SPEC.md` Section 13; `docs/PRD.md` FR-128 with HASH_MISMATCH warning |

## Documentation

Required implementation evidence:

- Tool resolver or equivalent deterministic tool-surface builder.
- Registry of supported SDK built-ins and Chirality MCP names.
- Structured validation error contract for unknown tool names.
- Deterministic ordering fixtures.
- Read-first sequencing tests.
- Residual-risk note for `docs/PRD.md` HASH_MISMATCH until source state is reconciled.

Concrete evidence locations remain TBD until implementation ownership assigns files. The documentation package must not close DEL-06-02 solely on planned artifact names or decomposition prose. (P3: B-001, C-001, E-001)

## Traceability

| Source item | Covered by |
|---|---|
| SOW-047 Tool option mapping | DEL-06-02-REQ-001 through REQ-004 |
| SOW-049 Deterministic tool surface | DEL-06-02-REQ-005, REQ-006, REQ-010, REQ-012 |
| SOW-050 Read tools before writes/bash | DEL-06-02-REQ-007, REQ-008, REQ-011, REQ-013 |
| OBJ-005 Tool governance objective | DEL-06-02-REQ-001 through REQ-013 |
