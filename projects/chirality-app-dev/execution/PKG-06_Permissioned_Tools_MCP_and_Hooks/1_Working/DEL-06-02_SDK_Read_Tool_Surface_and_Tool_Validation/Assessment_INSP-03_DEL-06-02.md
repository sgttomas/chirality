# Assessment INSP-03: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-02 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-70 |

## Scope

DEL-06-02 covers read-first SDK tool surface construction, descriptor-backed tool validation, unknown-tool rejection, deterministic exposure ordering, read MCP introduction before write/bash surfaces, and runtime metadata for the first SDK/MCP tool plane.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-02-REQ001 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 347-878 and 963-1062; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 123-201. | The registry maps only known SDK built-ins and Chirality MCP adapter names. |
| DEL-06-02-REQ002 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 1005-1022; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 317-357. | Unknown tools produce structured `UNKNOWN_TOOL` issues and deny decisions rather than reaching SDK options. |
| DEL-06-02-REQ003 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 15-29, 347-410, and 568-775; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 123-201. | `Read`, `LS`, `Glob`, `Grep`, `Write`, `Edit`, and `Bash` names are modeled; later write/bash exposure is governed by mode and policy. |
| DEL-06-02-REQ004 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 411-567; `frontend/src/lib/harness/mcp/tool-names.ts` lines 1-15. | Chirality MCP adapter names use the `mcp__chirality__*` namespace. |
| DEL-06-02-REQ005 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 89-145. | Tool-pool construction follows descriptor order and returns stable allowed/disallowed sets. |
| DEL-06-02-REQ006 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 74-82, 142-176, and 160-170; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 123-201. | Runtime availability is separate from model exposure and current phase decisions. |
| DEL-06-02-REQ007 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 347-490; `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 242-277. | Initial visible read capability includes read-only SDK built-ins and read-only Chirality MCP descriptors before writes. |
| DEL-06-02-REQ008 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 290-319. | Write/Edit/Bash are excluded in read-only and ask-mode exposure until workspaceWrite policy allows them. |
| DEL-06-02-REQ009 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-116; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87. | `allowedTools` is accompanied by disallowed names, permission callback, and hooks; it is not treated as the restriction boundary. |
| DEL-06-02-REQ010 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-146; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 147-192 and 290-319. | Denied/unrequested tools are omitted where possible and also remain in `disallowedTools`. |
| DEL-06-02-REQ011 | PASS | `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 242-277; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-114. | Read-only exposure allows only explicitly requested read tools and disallows write, bash, network, subagent, and mutating MCP tools. |
| DEL-06-02-REQ012 | PASS | `frontend/src/lib/harness/runtime-fingerprint.ts` lines 20-40; `frontend/src/app/api/harness/session/boot/route.ts` lines 57-78; `frontend/src/__tests__/api/harness/routes.test.ts` lines 301-315. | Session boot persists a safe runtime fingerprint containing tool registry, permission/subagent policy, SDK package version, MCP server version/tool names, and SHA-256 digest. |
| DEL-06-02-REQ013 | PASS | `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 317-398; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 89-145 and 290-319. | Tests cover unknown tools, deterministic ordering, read-only exposure, and read-before-write/bash policy. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Runtime boot/version fingerprint residual is closed by ADQ-11. | Low | `frontend/src/lib/harness/runtime-fingerprint.ts` lines 20-40; `frontend/src/__tests__/api/harness/routes.test.ts` lines 301-315. | Keep the fingerprint schema versioned when tool, policy, SDK, or MCP version fields change. |
| Read surface is descriptor-driven, but public docs should keep SDK names adapter-local. | Low | `frontend/src/lib/harness/tool-descriptor.ts` lines 97-101. | Document Chirality descriptor names as the product contract and SDK names as adapter metadata. |
| Historical REF-006 warning text in older run records is retired for active review. | Low | `_REFERENCES.md` REF-006 is `MATCH` under the D-APP-38 authority corpus v2. | Keep the D-APP-38 reference status check in closeout validation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as
`MATCH` under the D-APP-38 authority corpus v2. Historical HASH_MISMATCH notes in `_run_records`
remain archival only.

## Dependency Closure Note

ADQ-11 satisfies the runtime/version fingerprint and REF-006 source-state residuals for this
deliverable. Other active rows remain pending on DEL-06-01 permission overlay and DEL-06-03 MCP tool
interface posture unless separately closed by their owning deliverables.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Keep the startup/tool-surface fingerprint schema versioned as registry, SDK, MCP, or permission-policy fields change. | code/test | S | FIT | Future fingerprint field change. |
| Keep descriptor order as the canonical ordering contract and add a short docs note for public/product names. | docs | S | FIT | Tool descriptor registry stable. |
| Keep D-APP-38 authority-corpus status clean during future authority-document edits. | governance | S | FIT | Authority-document edits occur. |

## Issuance-Gate-Process Observations

DEL-06-02 has strong implementation and test evidence for deterministic read-first exposure. ADQ-11
closes the boot/version fingerprint and PRD source-state residuals. This does not advance lifecycle
state or make an issuance claim.
