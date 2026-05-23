# Specification: DEL-06-03 Initial Chirality MCP Read Tools

## Scope

This deliverable specifies the initial in-process Chirality MCP read-tool slice for PKG-06. It covers deterministic MCP tool descriptors, wrapper metadata, execution behavior, and tests for status read, dependency read, bounded scope scan, and scaffold preview/dry-run behavior.

In scope:

- Define Chirality MCP tools using the `mcp__chirality__*` naming convention.
- Implement or expose read-safe deterministic operations for status read, dependency read, bounded scope scan, and scaffold preview/dry-run.
- Route the tools through the same permission, hook, path, redaction, and event logging policy as SDK built-ins.
- Preserve read-before-write sequencing by excluding write/edit/bash capability from this deliverable.
- Provide deterministic wrapper metadata and MCP tool tests.

Out of scope:

- Status transition and dependency write execution except as adjacent naming/context for exclusion.
- General SDK built-in read-tool resolver behavior owned by DEL-06-02.
- Write/edit path hooks owned by DEL-06-04.
- Bash governance owned by DEL-06-05.
- Remote MCP, plugins, and domain-engine operations.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-06-03-001 | Chirality-specific deterministic operations in this slice MUST use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.1; `docs/TYPES.md` Section 8.4 |
| REQ-06-03-002 | The initial read-tool set MUST include `mcp__chirality__status_read`, `mcp__chirality__deps_read`, and `mcp__chirality__scope_scan`. | `docs/SPEC.md` Section 14.2; `docs/PRD.md` Section 8.13 FR-119 |
| REQ-06-03-003 | The scaffold surface in this deliverable MUST be limited to preview/dry-run behavior where applicable and MUST NOT open uncontrolled scaffold writes. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| REQ-06-03-004 | Chirality-owned tool definitions MUST declare schema, permissions, read-only behavior, concurrency behavior, interruption behavior, execution behavior, and summarization behavior. | `docs/PRD.md` Section 8.13 FR-079 |
| REQ-06-03-005 | Tool-surface construction MUST be deterministic for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` Section 1.6 K-TOOL-1; `docs/PRD.md` Section 8.13 FR-080 |
| REQ-06-03-006 | MCP tools MUST pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/PRD.md` Section 8.13 FR-119 |
| REQ-06-03-007 | Denied tools MUST NOT execute and SHOULD be omitted from model context where possible. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13 FR-081 |
| REQ-06-03-008 | `allowedTools` MUST NOT be treated as a restriction boundary by itself; restriction MUST rely on deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| REQ-06-03-009 | In `readOnly` mode, these tools MUST NOT expose or allow write/edit/bash/network-capable actions. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/PRD.md` Section 8.14 FR-091 |
| REQ-06-03-010 | Tool permission/start/completion/failure activity SHOULD be persisted as Chirality runtime events when the runtime event plumbing is available. | `docs/PLAN.md` R2; `docs/PRD.md` Section 8.13 FR-083 |
| REQ-06-03-011 | Status read behavior MUST treat `_STATUS.md` as the canonical lifecycle state source. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 14.2 |
| REQ-06-03-012 | Dependency read behavior MUST treat deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` as dependency truth sources, with `Dependencies.csv` read/validation behavior where present. | `docs/CONTRACT.md` Section 1.7 K-DEP-1; `docs/SPEC.md` Section 14.2 |
| REQ-06-03-013 | Scope scan behavior MUST be bounded to the workspace/project root contract and must not scan arbitrary external locations. | `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.6 K-PATH-2 |
| REQ-06-03-014 | Unknown or unsupported MCP tool names MUST fail with structured validation errors rather than silent pass-through. | `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13 FR-078 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| SDK tool surface and Chirality MCP contract | Governs tool naming, initial tool set, deterministic ordering, and tool-surface rules. | `docs/SPEC.md` Section 14 |
| Permission modes and hooks | Governs readOnly, workspaceWrite, dontAsk, ask, and bypass mapping to overlay policy. | `docs/SPEC.md` Section 15 |
| Permission/tool/MCP invariants | Binding constraints for deny-first behavior, tool exposure, and MCP wrapper enforcement. | `docs/CONTRACT.md` Section 1.6 |
| Lifecycle/dependency invariants | Binding constraints for `_STATUS.md`, dependency truth, provenance, and no-invention posture. | `docs/CONTRACT.md` Section 1.7 |
| Permission and tool vocabulary | Defines permission modes, decision records, tool-surface terms, and MCP names. | `docs/TYPES.md` Section 8 |
| R2 roadmap sequence | Requires permission-gated read surface and first MCP tools before write/bash expansion. | `docs/PLAN.md` R2; `docs/PRD.md` roadmap row R2 |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-06-03-001 through REQ-06-03-004 | Unit-test exported MCP descriptors/wrapper metadata for names, schemas, permission class, read/write classification, concurrency/interruption declarations, execution binding, and summarization metadata. |
| REQ-06-03-005 | Snapshot or table-driven tests proving deterministic ordering for a fixed session/persona/mode/option set. |
| REQ-06-03-006 through REQ-06-03-010 | Integration or adapter tests proving tools pass through permission overlay/hook/event/redaction paths and denied tools do not execute. |
| REQ-06-03-011 | Status read tests using `_STATUS.md` fixtures, including missing/malformed status handling. |
| REQ-06-03-012 | Dependency read tests using absent, valid, and malformed `Dependencies.csv` fixtures; behavior for `_DEPENDENCIES.md`-only state remains TBD until dependency API contract is finalized. |
| REQ-06-03-013 | Scope scan tests proving bounded root behavior and rejection of out-of-root scan requests. |
| REQ-06-03-014 | Unknown-tool validation tests asserting structured errors. |
| Section 9 marker | Add or map runtime validation coverage to `section9.chirality_mcp_status_dependencies` when the Section 9 runner is active. |

## Documentation

Required artifacts:

- `mcp__chirality__*` tool definitions for the read-tool slice.
- Wrapper metadata documenting schema, permissions, read-only behavior, concurrency, interruption, execution, and summarization behavior.
- MCP tool tests and fixtures for status read, dependency read, bounded scope scan, scaffold preview/dry-run, deterministic ordering, and denial behavior.
- Notes documenting source-state warning for `docs/PRD.md` HASH_MISMATCH if this deliverable consumes the current PRD text during implementation.

## Conflict Table

No source-content conflict was identified during Pass 1/2 drafting. Source-state warning remains: `_REFERENCES.md` reports `docs/PRD.md` HASH_MISMATCH; per task brief this was treated as a warning rather than a blocker.
