# Assessment INSP-03: DEL-06-03 Initial Chirality MCP Read Tools

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-03 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-72 |

## Scope

DEL-06-03 covers initial in-process Chirality MCP read tools for status, dependencies, bounded scope scanning, and scaffold preview, with path containment, permission/evidence handling, redaction, deterministic registration, and safe read-only behavior.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-03-REQ001 | PASS | `frontend/src/lib/harness/mcp/tool-names.ts` lines 1-15; `frontend/src/lib/harness/tool-descriptor.ts` lines 411-490. | Initial Chirality MCP tools are adapted under `mcp__chirality__*` names. |
| DEL-06-03-REQ002 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 411-490; `frontend/src/lib/harness/mcp/read-tools.ts` lines 434-477. | `status_read`, `deps_read`, and `scope_scan` are implemented. |
| DEL-06-03-REQ003 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 463-490; `frontend/src/lib/harness/mcp/read-tools.ts` lines 479-509; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 209-229. | `scaffold_preview` previews paths and does not create execution-root files. |
| DEL-06-03-REQ004 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 262-303 and 411-490; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 108-121. | Descriptors declare schemas, permissions, result budgets, concurrency, interrupt behavior, runtime, and provenance metadata. |
| DEL-06-03-REQ005 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 634-763; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 108-121. | MCP tool construction follows allowed descriptor order and is kept in parity with registry metadata. |
| DEL-06-03-REQ006 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 118-190 and 238-388; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 162-191. | Read tools append started/completed/failed events, summarize outputs, persist overflow artifacts, and use the same redaction/evidence utilities. |
| DEL-06-03-REQ007 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 103-146; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 117-145. | MCP tools are attached only when explicitly allowed; otherwise no MCP server is exposed. |
| DEL-06-03-REQ008 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-116; `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062. | MCP exposure is descriptor and permission based; `allowedTools` alone is not the only boundary. |
| DEL-06-03-REQ009 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 411-490; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 242-277. | Read-only MCP tools carry read permissions and do not expose write/edit/bash/network. |
| DEL-06-03-REQ010 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 135-189 and 299-388; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 162-191 and 231-257. | Tool started/completed/failed events are emitted where the in-process MCP plumbing is controlled by Chirality. |
| DEL-06-03-REQ011 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 434-444; `frontend/src/lib/workspace/deliverable-contracts.ts` lines 152-186; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 132-160. | Status reads parse canonical `_STATUS.md`. |
| DEL-06-03-REQ012 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 447-457; `frontend/src/lib/workspace/deliverable-contracts.ts` lines 381-408; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 132-160. | Dependency reads use `Dependencies.csv` and the dependency-register reader. |
| DEL-06-03-REQ013 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 460-477; `frontend/src/lib/workspace/filesystem.ts` lines 110-146; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 193-207. | Scope scan is bounded to the normalized project root and scans scope metadata without document bodies. |
| DEL-06-03-REQ014 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 1005-1022; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 317-357. | Unknown MCP names fail descriptor validation with structured issues before model exposure. |
| DEL-06-03-REQ015 | PASS | `frontend/src/lib/workspace/deliverable-contracts.ts` lines 401-459; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 372-385. | Missing `Dependencies.csv` now returns `registerPresent: false`, optional `_DEPENDENCIES.md` secondary-summary metadata, empty rows/headers, and a typed warning without inferring structured rows from prose. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Missing-`Dependencies.csv` fallback residual is closed by ADQ-11. | Low | `frontend/src/lib/workspace/deliverable-contracts.ts` lines 430-444; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 380-385. | Preserve non-inferential behavior if DEL-07-05 later expands dependency APIs. |
| MCP read output schemas exist in descriptors, but parser-level schema assertions are thin. | Low | `frontend/src/lib/harness/tool-descriptor.ts` lines 425-490. | Add lightweight output-shape tests for status/deps/scope/scaffold results. |
| Historical REF-006 warning text in older run records is retired for active review. | Low | `_REFERENCES.md` REF-006 is `MATCH` under the D-APP-38 authority corpus v2. | Keep the D-APP-38 reference status check in closeout validation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as
`MATCH` under the D-APP-38 authority corpus v2. Historical HASH_MISMATCH notes in `_run_records`
remain archival only.

## Dependency Closure Note

ADQ-11 satisfies the missing-register fallback and REF-006 source-state residuals for this deliverable.
Other active rows remain pending on DEL-06-01 permission overlay, DEL-07-05 dependency-reader
semantics, status lifecycle API ownership, and runtime event path ownership unless separately closed by
their owning deliverables.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Preserve absent-register handling as an explicit, non-inferential result if DEL-07-05 later expands dependency APIs. | code/test | S | FIT | Future dependency API change. |
| Add output-shape assertions for all four read MCP tools. | test | S | FIT | Current MCP handlers stable. |
| Keep D-APP-38 authority-corpus status clean during future authority-document edits. | governance | S | FIT | Authority-document edits occur. |

## Issuance-Gate-Process Observations

DEL-06-03 is strong for the primary read tools and event evidence. ADQ-11 closes the missing
dependency-register fallback targeted by the autonomous queue. This does not advance lifecycle state or
make an issuance claim.
