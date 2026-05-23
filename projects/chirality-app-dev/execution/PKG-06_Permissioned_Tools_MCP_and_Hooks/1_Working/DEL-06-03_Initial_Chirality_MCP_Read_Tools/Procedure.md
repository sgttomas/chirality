# Procedure: DEL-06-03 Initial Chirality MCP Read Tools

## Purpose

Define the working procedure for producing and verifying the DEL-06-03 MCP read-tool implementation artifacts. The procedure is constrained to the read-tool slice: status read, dependency read, bounded scope scan, and scaffold preview/dry-run.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Accepted decomposition scope for DEL-06-03 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 7.6 and Section 9. |
| Source contracts for MCP tools and permissions | Available in `docs/SPEC.md` Sections 14-15, `docs/CONTRACT.md` Section 1.6, and `docs/PRD.md` Sections 8.13-8.14. |
| Runtime sequence context | R2 requires permission-gated read surface before writes/bash; see `docs/PLAN.md` R2. |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. |
| Implementation module locations | TBD - no implementation path is specified in the accessible sources for this deliverable. |
| PRD source-state warning | `docs/PRD.md` has HASH_MISMATCH in `_REFERENCES.md`; treat as warning per task brief. |

## Steps

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

   Persist or adapt permission, started, completed, and failed tool events through the Chirality runtime event path when the runtime event plumbing is active. If unavailable, leave an explicit `TBD` integration point and tests around the expected contract.

10. Add tests.

   Cover descriptors, deterministic ordering, permission denial, readOnly behavior, unknown-tool errors, status fixtures, dependency fixtures, bounded scan rejection, scaffold preview/no-write behavior, and relevant Section 9 validation mapping.

11. Re-check cross-deliverable boundaries.

   Confirm the implementation has not absorbed DEL-06-01 permission policy ownership, DEL-06-02 SDK built-in tool resolver ownership, DEL-06-04 write/path hook ownership, DEL-06-05 bash governance, or remote/domain MCP scope.

## Verification

| Check | Expected Result |
|---|---|
| Tool names | Only accepted Chirality MCP names use the `mcp__chirality__*` namespace; unknown names fail with structured errors. |
| Descriptor completeness | Each Chirality-owned tool declares schema, permissions, read-only behavior, concurrency, interruption, execution, and summarization behavior. |
| Deterministic surface | Tool ordering and metadata are stable for fixed session/persona/mode/option input. |
| Deny-first policy | Denied tools do not execute; `allowedTools` alone is not treated as restriction. |
| Read-only mode | Write/edit/bash/network-capable behavior is unavailable or hard-denied. |
| Status read | `_STATUS.md` is the only lifecycle truth source. |
| Dependency read | `Dependencies.csv` is read/validated when present; absence is explicit rather than inferred. |
| Scope scan | Out-of-root scans are rejected. |
| Scaffold preview | Dry-run/preview does not apply filesystem writes. |
| Runtime events | Permission/start/completion/failure events are persisted or an explicit pending integration contract is tested. |
| Source-state warning | `docs/PRD.md` HASH_MISMATCH is recorded until reference hashes are refreshed or human accepted. |

## Records

- MCP tool definitions.
- Wrapper metadata.
- Unit/API/integration test fixtures.
- Validation output for deterministic ordering and denial behavior.
- Status/dependency/scope/scaffold preview test results.
- Section 9 validation mapping, including `section9.chirality_mcp_status_dependencies` where applicable.
- Source-state note for `docs/PRD.md` HASH_MISMATCH until resolved.
