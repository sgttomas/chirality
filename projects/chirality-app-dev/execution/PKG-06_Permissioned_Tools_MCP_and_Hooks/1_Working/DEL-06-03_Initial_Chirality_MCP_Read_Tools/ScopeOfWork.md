---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-03
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-048, SOW-050]
package_objective_refs: [OBJ-005, OBJ-006]
---

# Scope of Work — DEL-06-03

## Purpose and Objective Traceability

This migration candidate defines `DEL-06-03` in service of project scope [SOW-048, SOW-050] and package objectives [OBJ-005, OBJ-006].

- **OUT-001** — Initial Chirality MCP read-tool slice comprising deterministic descriptors, wrapper metadata, status read, dependency read, bounded scope scan, scaffold preview/dry-run behavior, and associated verification evidence.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-03 Initial Chirality MCP Read Tools

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-001"} -->
#### Datasheet: DEL-06-03 Initial Chirality MCP Read Tools

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":19,"line_start":5,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":32,"line_start":20,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-003"} -->
##### Attributes

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

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":44,"line_start":33,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Permission mode compatibility | `readOnly` exposes or allows read-only tools only; write/edit/bash/network-capable tools are unavailable or hard-denied. | `docs/PRD.md` Section 8.14 FR-091; `docs/TYPES.md` Section 8.1 |
| Deny precedence | Explicit denies from policy, path containment, hook, governance, SDK deny rule, or human gate block execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/PRD.md` Section 8.14 FR-089 |
| `allowedTools` limitation | `allowedTools` is not a restriction boundary by itself. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| Status truth source | `_STATUS.md` is canonical human-readable lifecycle state. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1 |
| Dependency truth source | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative for dependencies. | `docs/CONTRACT.md` Section 1.7 K-DEP-1 |
| Scaffold posture | `mcp__chirality__scaffold` is gated; this deliverable should cover preview/dry-run behavior where appropriate, not uncontrolled scaffold writes. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Source-state warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; task brief — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":56,"line_start":45,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-005"} -->
##### Construction

| Construct | Expected Shape | Source |
|---|---|---|
| MCP definitions | In-process SDK MCP tool definitions using `createSdkMcpServer()` / `tool()` or equivalent SDK APIs. | `docs/PRD.md` Section 8.13 FR-119 |
| Wrapper contract | Shared wrapper metadata for tool descriptors, permission classification, execution, result summarization, and event/redaction behavior. | `docs/PRD.md` Section 8.13 FR-079; `docs/CONTRACT.md` Section 1.6 K-MCP-1 |
| Status read | Read `_STATUS.md` snapshot. Exact parser/API adapter TBD and should align with the status lifecycle API owner. | `docs/SPEC.md` Sections 14.2 and 17.2 |
| Dependency read | Read and validate `Dependencies.csv` when present. If only `_DEPENDENCIES.md` exists, return an explicit secondary-summary / not-structured-tracked result rather than inventing rows; final API shape remains TBD pending DEL-07-05. | `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` Extracted Dependency Register |
| Scope scan | Run bounded workspace scope scan. Exact scanner interface TBD and should align with workspace scope API. | `docs/SPEC.md` Sections 14.2 and 17.2 |
| Scaffold preview/dry-run | Wrap scaffold service or dry-run preview without opening uncontrolled write behavior. Exact preview schema TBD. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Tests | MCP tool definitions and wrapper metadata are unit-tested and deterministic. | `docs/PRD.md` Section 8.13 FR-079 |

<!-- sow-source-end -->

### CLM-006 — Pass 3 Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":62,"line_start":57,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-006"} -->
##### Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Incorporated with TBD boundary | Dependency read fallback now states the safe executable behavior for `_DEPENDENCIES.md`-only state and keeps final API shape `TBD` pending DEL-07-05. Source reread: `docs/SPEC.md` Sections 14.2 and 17.2; `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` Extracted Dependency Register. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":73,"line_start":63,"source_sha256":"ced04d0a44f3aa580cfcb4f9b9052c7775c1eb3b8e5a7c441768e3b6daef3650","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` for deliverable identity, package scope, and anticipated artifacts.
- `_REFERENCES.md` for source corpus and source-state warning.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6, 7, 9, and 10A for objective, deliverable, SOW, and invariant-family mapping.
- `docs/DIRECTIVE.md` Sections 13-14 for runtime integration boundaries and capability-forward MCP posture with explicit hard-deny precedence.
- `docs/CONTRACT.md` Sections 1.6-1.7 for binding tool, MCP, permission, status, dependency, and invention invariants.
- `docs/SPEC.md` Sections 14, 15, 17.2, and 19.3 for tool names, modes, API surfaces, and validation IDs.
- `docs/TYPES.md` Sections 8.1-8.4 for permission and MCP vocabulary.
- `docs/PLAN.md` R2 and R6 for sequencing and MCP extension boundaries.
- `docs/PRD.md` Sections 8.13-8.14 and R2 traceability; MATCH status recorded in `_REFERENCES.md`. (reconciled under D-APP-38).
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-03 Initial Chirality MCP Read Tools

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-008"} -->
#### Specification: DEL-06-03 Initial Chirality MCP Read Tools

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":5,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-009"} -->
##### Scope

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

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":44,"line_start":25,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-010"} -->
##### Requirements

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
| REQ-06-03-015 | Dependency-read behavior MUST expose explicit structured absence or secondary-summary status when `Dependencies.csv` is absent and `_DEPENDENCIES.md` exists; it MUST NOT infer structured dependency rows from prose. Final result schema remains TBD pending DEL-07-05. | `docs/CONTRACT.md` Section 1.7 K-DEP-1; `docs/SPEC.md` Sections 14.2 and 17.2; `_DEPENDENCIES.md` Extracted Dependency Register |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":55,"line_start":45,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-011"} -->
##### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| SDK tool surface and Chirality MCP contract | Governs tool naming, initial tool set, deterministic ordering, and tool-surface rules. | `docs/SPEC.md` Section 14 |
| Permission modes and hooks | Governs readOnly, workspaceWrite, dontAsk, ask, and bypass mapping to overlay policy. | `docs/SPEC.md` Section 15 |
| Permission/tool/MCP invariants | Binding constraints for explicit hard-deny precedence, tool exposure, and MCP wrapper enforcement. | `docs/CONTRACT.md` Section 1.6 |
| Lifecycle/dependency invariants | Binding constraints for `_STATUS.md`, dependency truth, provenance, and no-invention posture. | `docs/CONTRACT.md` Section 1.7 |
| Permission and tool vocabulary | Defines permission modes, decision records, tool-surface terms, and MCP names. | `docs/TYPES.md` Section 8 |
| R2 roadmap sequence | Requires permission-gated read surface and first MCP tools before write/bash expansion. | `docs/PLAN.md` R2; `docs/PRD.md` roadmap row R2 |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":56,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-012"} -->
##### Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-06-03-001 through REQ-06-03-004 | Unit-test exported MCP descriptors/wrapper metadata for names, schemas, permission class, read/write classification, concurrency/interruption declarations, execution binding, and summarization metadata. Proposed tests: `chirality-mcp-descriptor-schema`, `chirality-mcp-permission-class`, `chirality-mcp-readonly-classification`, `chirality-mcp-concurrency-interruption`, `chirality-mcp-execution-binding`, and `chirality-mcp-summarization-metadata`; final file paths TBD. |
| REQ-06-03-005 | Snapshot or table-driven tests proving deterministic ordering for a fixed session/persona/mode/option set. |
| REQ-06-03-006 through REQ-06-03-010 | Integration or adapter tests proving tools pass through permission overlay/hook/path/redaction/event paths and denied tools do not execute. Acceptance evidence should include permission decision records, hook invocation records, path-containment rejection fixtures, redaction assertions, event mirror records, and denied-execution assertions; final fixture paths TBD. |
| REQ-06-03-011 | Status read tests using `_STATUS.md` fixtures, including missing/malformed status handling. |
| REQ-06-03-012 and REQ-06-03-015 | Dependency read tests using absent, valid, and malformed `Dependencies.csv` fixtures, plus `_DEPENDENCIES.md`-only fixtures that assert explicit secondary-summary / not-structured-tracked behavior without invented rows. Final behavior must align with DEL-07-05 when its dependency API contract is accepted. |
| REQ-06-03-013 | Scope scan tests proving bounded root behavior and rejection of out-of-root scan requests. |
| REQ-06-03-014 | Unknown-tool validation tests asserting structured errors. |
| Section 9 marker | Add or map runtime validation coverage to `section9.chirality_mcp_status_dependencies` when the Section 9 runner is active. |

<!-- sow-source-end -->

### CLM-013 — Acceptance Evidence Register

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":77,"line_start":69,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-013"} -->
###### Acceptance Evidence Register

| Evidence Area | Required Evidence | Status |
|---|---|---|
| Descriptor and wrapper metadata | Named tests or fixtures for schema, permission class, read-only behavior, concurrency, interruption, execution binding, and summarization metadata. | TBD - proposed test names listed above; implementation file paths not assigned. |
| Policy traversal | Permission decision records, hook traversal records, path-containment evidence, redaction assertions, and event mirror records for Chirality MCP tool execution. | TBD - requires implementation and runtime event path availability. |
| Section 9 coverage | Mapping to `section9.chirality_mcp_status_dependencies` for status/dependency MCP behavior. | TBD - active when Section 9 runner accepts this validation ID. |
| Dependency fallback | Fixture proving `_DEPENDENCIES.md`-only state returns explicit non-structured / secondary-summary status and does not synthesize `Dependencies.csv` rows. | TBD - final schema depends on DEL-07-05. |

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":86,"line_start":78,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-014"} -->
##### Documentation

Required artifacts:

- `mcp__chirality__*` tool definitions for the read-tool slice.
- Wrapper metadata documenting schema, permissions, read-only behavior, concurrency, interruption, execution, and summarization behavior.
- MCP tool tests and fixtures for status read, dependency read, bounded scope scan, scaffold preview/dry-run, deterministic ordering, and denial behavior.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-015 — Conflict Table

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":90,"line_start":87,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-015"} -->
##### Conflict Table

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-016 — Pass 3 Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":97,"line_start":91,"source_sha256":"f6e519ac392f3d5eba0217044f0fcf47e2b0059c1850e7fd98ab3285e1b14080","target_id":"CLM-016"} -->
##### Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| F-001 | Converted to named TBD evidence | Concrete descriptor/wrapper metadata test names were added, while final implementation paths remain `TBD`. Source reread: `docs/PRD.md` Section 8.13 FR-079; `docs/SPEC.md` Section 14. |
| F-002 | Incorporated with TBD artifact paths | Acceptance evidence for permission, hook, path, redaction, and event-policy traversal is now explicit. Source reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.3. |
| X-002 | Incorporated with TBD closure paths | Verification now names concrete evidence categories and Section 9 mapping while preserving implementation paths as `TBD`. Source reread: `docs/SPEC.md` Section 19.3; `docs/PRD.md` Section 8.13 FR-079 and FR-083. |
<!-- sow-source-end -->

- **AC-001** — The converted contract preserves every legacy source line with hash-bound migration markers, retains the initial read-tool scope and exclusions, and provides verification coverage for naming, wrapper metadata, permission and deny behavior, lifecycle and dependency reads, bounded scans, no-write scaffold preview, and unresolved dependency closure.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-06-03 Initial Chirality MCP Read Tools

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":4,"line_start":1,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-017"} -->
#### Procedure: DEL-06-03 Initial Chirality MCP Read Tools

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":8,"line_start":5,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-018"} -->
##### Purpose

Define the working procedure for producing and verifying the DEL-06-03 MCP read-tool implementation artifacts. The procedure is constrained to the read-tool slice: status read, dependency read, bounded scope scan, and scaffold preview/dry-run.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":19,"line_start":9,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-019"} -->
##### Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Accepted decomposition scope for DEL-06-03 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 7.6 and Section 9. |
| Source contracts for MCP tools and permissions | Available in `docs/SPEC.md` Sections 14-15, `docs/CONTRACT.md` Section 1.6, and `docs/PRD.md` Sections 8.13-8.14. |
| Runtime sequence context | R2 requires permission-gated read surface before writes/bash; see `docs/PLAN.md` R2. |
| Declared upstream dependencies | Active unresolved interfaces are recorded in `_DEPENDENCIES.md`: DEL-06-01 permission overlay integration, DEL-07-05 dependency reader behavior, UNKNOWN/TBD status lifecycle API owner, and UNKNOWN/TBD Chirality runtime event path. Closure requires human or upstream acceptance of these states. |
| Implementation module locations | TBD - no implementation path is specified in the accessible sources for this deliverable. |
| PRD source state | `docs/PRD.md` is `MATCH` in `_REFERENCES.md` under D-APP-38. |

<!-- sow-source-end -->

### CLM-020 — Implementation Location Worklist

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":30,"line_start":20,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-020"} -->
###### Implementation Location Worklist

| Component | Expected Location Evidence | Status |
|---|---|---|
| MCP definitions | Module exporting `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and scaffold preview/dry-run descriptor. | TBD - owner/path not assigned in accessible sources. |
| Wrapper metadata | Shared metadata table or builder for schema, permissions, read-only class, concurrency, interruption, execution, summarization, redaction, and events. | TBD - owner/path not assigned in accessible sources. |
| Status reader | Adapter/parser for `_STATUS.md` snapshot read; final ownership should align with DEL-07-04. | TBD - status lifecycle API owner unresolved in `_DEPENDENCIES.md`. |
| Dependency reader | Adapter/parser for `Dependencies.csv` plus `_DEPENDENCIES.md`-only absence/secondary-summary behavior; final ownership should align with DEL-07-05. | TBD - DEL-07-05 alignment unresolved in `_DEPENDENCIES.md`. |
| Scope scan | Bounded workspace scope scanner or adapter. | TBD - owner/path not assigned in accessible sources. |
| Scaffold preview | Dry-run/preview adapter that does not apply filesystem writes. | TBD - owner/path not assigned in accessible sources. |

<!-- sow-source-end -->

### CLM-021 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":76,"line_start":31,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-021"} -->
##### Steps

1. Confirm the active scope.

   Read `_CONTEXT.md`, `_REFERENCES.md`, and the DEL-06-03 decomposition row. Confirm the scope remains "Expose in-process deterministic MCP tools for status read, dependency read, scope scan, and scaffold preview/dry-run."

2. Establish the tool inventory.

   Include `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and scaffold preview/dry-run behavior for `mcp__chirality__scaffold` where applicable. Exclude write/gated operations unless they are represented only as denied or adjacent metadata.

3. Define wrapper metadata.

   For each tool, declare schema, permissions, read-only behavior, concurrency behavior, interruption behavior, execution behavior, summarization behavior, redaction/event metadata, and denial behavior.

4. Wire permission evaluation.

   Route each tool through the Chirality permission overlay, deny rules, relevant hooks, and mode policy. Confirm `allowedTools` is not used as a standalone restriction boundary.

5. Implement status read.

   Read `_STATUS.md` as canonical lifecycle truth. Return a structured result with source path, parsed state, warnings, and malformed/missing handling. Do not apply lifecycle transitions in this tool.

6. Implement dependency read.

   Read and validate `Dependencies.csv` when present. If it is absent but `_DEPENDENCIES.md` exists, return an explicit missing/not-tracked status and do not infer dependency rows. Align final behavior with the dependency contract owner when available.

7. Implement bounded scope scan.

   Run a workspace/project-root bounded scan that reports package/deliverable identities and rejects out-of-root or non-project scan targets. Preserve stable IDs as identity.

8. Implement scaffold preview/dry-run.

   Produce a preview of scaffold effects without applying filesystem writes. If the underlying scaffold service can write, enforce dry-run mode or deny write execution in this deliverable.

9. Emit runtime events where available.

   Persist or adapt permission, started, completed, and failed tool events through the Chirality runtime event path. The runtime event path owner is currently `UNKNOWN/TBD` in `_DEPENDENCIES.md`; until accepted upstream ownership exists, keep this as a tracked closure blocker and add tests around the expected event contract rather than silently treating event persistence as complete.

10. Add tests.

   Cover descriptors, deterministic ordering, permission denial, readOnly behavior, unknown-tool errors, status fixtures, dependency fixtures, bounded scan rejection, scaffold preview/no-write behavior, and relevant Section 9 validation mapping.

11. Re-check cross-deliverable boundaries.

   Confirm the implementation has not absorbed DEL-06-01 permission policy ownership, DEL-06-02 SDK built-in tool resolver ownership, DEL-06-04 write/path hook ownership, DEL-06-05 bash governance, or remote/domain MCP scope.

<!-- sow-source-end -->

### CLM-022 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":93,"line_start":77,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-022"} -->
##### Verification

| Check | Expected Result |
|---|---|
| Tool names | Only accepted Chirality MCP names use the `mcp__chirality__*` namespace; unknown names fail with structured errors. |
| Descriptor completeness | Each Chirality-owned tool declares schema, permissions, read-only behavior, concurrency, interruption, execution, and summarization behavior. |
| Deterministic surface | Tool ordering and metadata are stable for fixed session/persona/mode/option input. |
| Capability policy with explicit hard-deny precedence | Denied tools do not execute; `allowedTools` alone is not treated as restriction. |
| Read-only mode | Write/edit/bash/network-capable behavior is unavailable or hard-denied. |
| Status read | `_STATUS.md` is the only lifecycle truth source. |
| Dependency read | `Dependencies.csv` is read/validated when present; absence is explicit rather than inferred. |
| Scope scan | Out-of-root scans are rejected. |
| Scaffold preview | Dry-run/preview does not apply filesystem writes. |
| Runtime events | Permission/start/completion/failure events are persisted or an explicit pending integration contract is tested. |
| Upstream dependency closure | DEL-06-01, DEL-07-05, status lifecycle API ownership, and runtime event path ownership are accepted or recorded as closure blockers. |
| Source-state status | `docs/PRD.md` REF-006 is `MATCH` under D-APP-38. |

<!-- sow-source-end -->

### CLM-023 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":106,"line_start":94,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-023"} -->
##### Records

- MCP tool definitions.
- Wrapper metadata.
- Unit/API/integration test fixtures.
- Validation output for deterministic ordering and denial behavior.
- Status/dependency/scope/scaffold preview test results.
- Section 9 validation mapping, including `section9.chirality_mcp_status_dependencies` where applicable.
- Source-state note: `docs/PRD.md` REF-006 is `MATCH` under D-APP-38; dated mismatch history remains in prior run records.
- Implementation location map for MCP definitions, wrapper metadata, status reader, dependency reader, scope scan, and scaffold preview.
- Upstream closure record for DEL-06-01, DEL-07-05, status lifecycle API ownership, and runtime event path ownership.
- Runtime event contract blocker record if the Chirality runtime event path remains unavailable.

<!-- sow-source-end -->

### CLM-024 — Pass 3 Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":113,"line_start":107,"source_sha256":"0b231b934cb54462dc7aab7bb6194583c3eee6d78399bfd9614baa6670bc2382","target_id":"CLM-024"} -->
##### Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| D-001 | Converted to TBD worklist | Implementation module locations are named as required closure evidence, with all paths kept `TBD` because accessible sources do not assign ownership. Source reread: `_CONTEXT.md` Anticipated Artifacts; decomposition row `DEL-06-03`; `Procedure.md` Prerequisites and Records. |
| D-002 | Incorporated as closure blocker | Upstream dependency state now names DEL-06-01, DEL-07-05, status lifecycle API ownership, and runtime event path ownership as closure blockers or acceptance requirements. Source reread: `_DEPENDENCIES.md` Extracted Dependency Register and Open dependency closure items. |
| E-001 | Converted to tracked blocker | Runtime-event wording now requires a cited event path or explicit blocker/test contract rather than treating availability as optional. Source reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/PRD.md` Section 8.13 FR-083; `_DEPENDENCIES.md` open runtime event path item. |
<!-- sow-source-end -->

- **VER-001** — Validate the SOW schema and source parity; inspect deterministic descriptor, permission, hook, path, redaction, event, status, dependency, bounded-scan, scaffold-preview, and Section 9 evidence, with human review of unresolved TBD dependency interfaces.

## Governing Values and Decisions — Axiology

### CLM-025 — Guidance: DEL-06-03 Initial Chirality MCP Read Tools

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-025"} -->
#### Guidance: DEL-06-03 Initial Chirality MCP Read Tools

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-026 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-026"} -->
##### Purpose

DEL-06-03 provides the first Chirality-owned in-process MCP read tools so the runtime can expose deterministic project-state operations without opening write, edit, shell, remote MCP, plugin, or domain-operation capability. The deliverable supports OBJ-005 by keeping tool exposure behind capability policy with explicit hard-deny precedence and MCP wrappers, and OBJ-006 by reading filesystem-native project truth.

Source basis: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6-7 and 9; `docs/PLAN.md` R2; `docs/PRD.md` Sections 8.13-8.14.

<!-- sow-source-end -->

### CLM-027 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":32,"line_start":11,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-027"} -->
##### Principles

1. Read tools come first.

   The R2 slice enables SDK read tools and Chirality read MCP tools before write/edit/bash capability. Treat this deliverable as a read-surface and descriptor/wrapper contract, not a general tool expansion.

2. MCP is a transport, not a policy escape.

   In-process Chirality MCP tools must go through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. A tool being implemented locally does not make it safe to expose.

3. Determinism is part of the contract.

   Tool naming, ordering, server IDs, wrapper metadata, and allow/deny behavior should be table-driven or otherwise stable for a fixed runtime configuration.

4. Explicit hard-deny precedence is non-negotiable.

   `allowedTools` may auto-approve, but it is not a restriction boundary. Denies from policy, hooks, path containment, governance, SDK deny rules, or human gates must win.

5. Filesystem truth remains local and inspectable.

   Status and dependency tools should read the canonical project files, not hidden runtime state. Unknowns and malformed records should produce explicit results rather than inferred project truth.

<!-- sow-source-end -->

### CLM-028 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":44,"line_start":33,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-028"} -->
##### Considerations

| Topic | Guidance | Source |
|---|---|---|
| Tool boundaries | Keep `status_transition` and `deps_write` out of this read-tool slice except as excluded adjacent tools. | `docs/SPEC.md` Section 14.2 |
| Scaffold behavior | `mcp__chirality__scaffold` is listed as gated. For this deliverable, implement only preview/dry-run behavior where applicable unless a later write-surface gate authorizes more. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Dependency reads | Prefer a clear `Dependencies.csv` validation result. Behavior when the deliverable has `_DEPENDENCIES.md` but no `Dependencies.csv` is TBD and should align with DEL-07-05. | `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` |
| Status reads | Read `_STATUS.md` as canonical lifecycle state. Do not infer status from folder names, chat state, runtime events, or document presence. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1 |
| Scope scan | Scope scan should stay bounded to the selected working root and stable deliverable IDs. | `docs/SPEC.md` Sections 17.2 and 14.2; `docs/CONTRACT.md` K-PATH-2 |
| Runtime events | Permission/start/completion/failure event persistence may depend on R1/R2 runtime plumbing. If not available, expose a typed integration seam and tests around the expected behavior. | `docs/PLAN.md` R2; `docs/PRD.md` Section 8.13 FR-083 |
| PRD hash warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; task brief — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-029 — Source-State Posture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":48,"line_start":45,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-029"} -->
###### Source-State Posture

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-030 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":58,"line_start":49,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-030"} -->
##### Trade-offs

| Decision Area | Trade-off | Recommended Posture |
|---|---|---|
| Single wrapper vs per-tool wrappers | A shared wrapper improves consistent permission/event/redaction behavior; per-tool wrappers can drift. | Use a shared wrapper contract with per-tool metadata and execution handlers. |
| Scaffold included vs deferred | SPEC lists scaffold as gated; PLAN R2 calls for scaffold preview/dry-run where appropriate. | Include dry-run/preview only, with write execution denied or delegated to later gated surfaces. |
| Dependency file absence | `Dependencies.csv` may not exist early in a deliverable lifecycle. | Return an explicit "not present / not tracked yet" result; do not fabricate dependencies. |
| Event coupling | Full event persistence may not be complete when read tools are first drafted. | Keep event emission/adaptation explicit and testable; mark unavailable runtime pieces `TBD` instead of embedding hidden behavior. |
| SDK-specific APIs | PRD references SDK MCP APIs, but Chirality contracts must remain product-owned. | Use SDK APIs behind product-owned wrappers and tests; do not leak SDK-shaped public contracts. |

<!-- sow-source-end -->

### CLM-031 — Scaffold Boundary Rationale

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":62,"line_start":59,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-031"} -->
###### Scaffold Boundary Rationale

Scaffold preview belongs in this read-tool slice only as a non-mutating planning surface. `docs/SPEC.md` Section 14.2 classifies `mcp__chirality__scaffold` as gated, while `docs/PLAN.md` R2 sequences read and preview capability before write/edit/bash expansion. The practical boundary is therefore: allow a deterministic preview of intended scaffold effects, deny or defer filesystem mutation, and move any write-capable scaffold execution to the later governed write/path-hook surface.

<!-- sow-source-end -->

### CLM-032 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":87,"line_start":63,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-032"} -->
##### Examples

Example read-tool inventory:

| Tool | Expected Result Shape |
|---|---|
| `mcp__chirality__status_read` | Parsed `_STATUS.md` snapshot plus source path, parse warnings, and raw/normalized state fields. |
| `mcp__chirality__deps_read` | `Dependencies.csv` validation summary when present; explicit missing/not-tracked status when absent; warnings sourced to files. |
| `mcp__chirality__scope_scan` | Bounded package/deliverable scan summary with stable IDs and rejected out-of-root requests. |
| `mcp__chirality__scaffold` | Preview/dry-run plan showing intended scaffold effects without applying filesystem writes. |

Example wrapper metadata fields:

- Tool name.
- MCP server ID.
- Input schema.
- Permission class.
- Read/write classification.
- Concurrency policy.
- Interruption policy.
- Execution handler reference.
- Result summarization behavior.
- Redaction/event metadata.
- Denial behavior.

<!-- sow-source-end -->

### CLM-033 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":93,"line_start":88,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-033"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| N/A | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | Task brief | References and source confidence | Treat as warning per task brief; re-check hash before implementation closure. | TBD — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-034 — Pass 3 Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":99,"line_start":94,"source_sha256":"3be2d4db7184faf14299a04e513404488427735e0528e316153f6f7f5d6a91bc","target_id":"CLM-034"} -->
##### Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| X-001 | Incorporated as source-state posture | PRD MATCH handling is now explicit before PRD-only policy detail can be used for closure. Source reread: `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.13; `docs/CONTRACT.md` Section 1.6. — reconciled under D-APP-38 |
| E-002 | Incorporated | Scaffold preview rationale now explains why preview/dry-run is in scope while write-capable scaffold execution remains gated. Source reread: `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2. |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-048 SOW-050 OBJ-005 OBJ-006 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
