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
| DEL-06-02-REQ012 | PARTIAL | `frontend/src/lib/harness/tool-descriptor.ts` lines 13-14; `frontend/src/lib/harness/sdk-options-builder.ts` lines 147-157; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87. | Registry version and option fields are available, but an explicit boot fingerprint containing SDK/MCP versions remains thin and overlaps DEL-04-01/DEL-04-02. |
| DEL-06-02-REQ013 | PASS | `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 317-398; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 89-145 and 290-319. | Tests cover unknown tools, deterministic ordering, read-only exposure, and read-before-write/bash policy. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Runtime boot/version fingerprint is not yet a first-class artifact for the tool surface. | Medium | `frontend/src/lib/harness/tool-descriptor.ts` lines 13-14; DEL-04-01 residual evidence. | Add a compact runtime fingerprint that records tool registry version, SDK package version, and MCP server version in session metadata or startup evidence. |
| Read surface is descriptor-driven, but public docs should keep SDK names adapter-local. | Low | `frontend/src/lib/harness/tool-descriptor.ts` lines 97-101. | Document Chirality descriptor names as the product contract and SDK names as adapter metadata. |
| REF-006 warning still applies to PRD-derived tool-surface assumptions. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Refresh or explicitly waive the PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active rows remain pending on DEL-06-01 permission overlay, DEL-06-03 MCP tool interface, runtime/version evidence, and REF-006 source-state closure.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a startup/tool-surface fingerprint artifact covering registry version, SDK version, and MCP server version. | code/test | S | FIT | DEL-04-01 version evidence location accepted. |
| Keep descriptor order as the canonical ordering contract and add a short docs note for public/product names. | docs | S | FIT | Tool descriptor registry stable. |
| Close REF-006 before issuance. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-06-02 has strong implementation and test evidence for deterministic read-first exposure. The issuance gate should require a small boot/version fingerprint addition or an explicit deferral, plus PRD hash closure.
