# Assessment INSP-03: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-01 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-84 |

## Scope

DEL-06-01 covers the product-owned permission overlay over SDK tool callbacks, Chirality mode mapping, deny precedence, interactive ask handling, bypass constraints, and `tool.permission` evidence before tool execution continues.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-01-REQ001 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 30-40; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 43-60. | `HarnessPermissionDecision` is structured with decision ID, session, tool, decision, source, reason, timestamp, and safe metadata. |
| DEL-06-01-REQ002 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 13-28 and 399-447; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 391-431 and 468-486. | `allow`, `deny`, and `ask` are explicit. Ask-mode callbacks suspend on an addressable broker request and return the human verdict before the SDK result is produced. |
| DEL-06-01-REQ003 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 117-123 and 354-381; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 137-151. | Explicit policy/path/shell denies override otherwise-allowed tools before SDK execution. |
| DEL-06-01-REQ004 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-116; `frontend/src/lib/harness/permission-overlay.ts` lines 338-447; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87 and 290-319. | `allowedTools` is paired with `disallowedTools`, `canUseTool`, and hooks; it is not the only boundary. |
| DEL-06-01-REQ005 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87 and 290-319. | Read-only/default exposure allows only requested read tools and keeps write/edit/bash/network/subagent surfaces disallowed. |
| DEL-06-01-REQ006 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 140-168 and 222-254; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 153-180. | `dontAsk` denies unapproved write, shell, network, subagent, and unknown tools without prompting. |
| DEL-06-01-REQ007 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 399-447; `frontend/src/lib/harness/permission-broker.ts` lines 1-94; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 391-431. | Ask-mode gated tool calls are mediated through the broker and persisted as permission events before returning the final SDK result. |
| DEL-06-01-REQ008 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 222-232 and 338-381; `frontend/src/lib/harness/chirality-hooks.ts` lines 424-461; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 45-165. | Workspace writes are allowed only at the overlay layer after path policy metadata is accepted; mutation evidence is then captured by the hook layer. |
| DEL-06-01-REQ009 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 39-54; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 255-288; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 222-236. | SDK bypass requires `CHIRALITY_ALLOW_SDK_BYPASS=1`, and Chirality hard-deny logic still applies to bypass-mode tool decisions. |
| DEL-06-01-REQ010 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 288-315 and 383-389; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 309-337 and 378-411. | Governed attempts append `tool.permission` events with behavior, source, reason, descriptor, mode, and safe metadata. |
| DEL-06-01-REQ011 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 129-188; `frontend/src/lib/harness/permission-overlay.ts` lines 111-265. | Prompt text can describe posture, but execution policy is enforced in code through descriptor, path, shell, and callback decisions. |
| DEL-06-01-REQ012 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-297 and 299-388; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-204. | In-process Chirality MCP mutating tools pass through handler-level permission, path, event, and evidence policy. |
| DEL-06-01-REQ013 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 13-40; `frontend/src/lib/harness/sdk-options-builder.ts` lines 39-54. | Public permission decision and normalized modes are Chirality-owned; SDK mode strings are adapter metadata in the options builder. |
| DEL-06-01-REQ014 | PASS | `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 153-180, 238-337, and 414-511; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 361-516. | Tests cover read-only, `dontAsk`, ask denial/approval, hard denies, and event persistence for denied non-execution. |
| DEL-06-01-REQ015 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 42-54, 325-337, and 369-380. | Overlay input includes product-owned session, turn, mode, project-root, delegated-subagent, descriptor, tool-input, and safe metadata fields. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Permission overlay is strong, but mode naming remains split across product modes and SDK adapter values. | Low | `frontend/src/lib/harness/sdk-options-builder.ts` lines 39-54. | Keep public docs on Chirality mode names and treat SDK mode names as adapter implementation details. |
| Workspace-write correctness depends on DEL-06-04 hook/path policy remaining attached in every adapter execution path. | Medium | `frontend/src/lib/harness/sdk-options-builder.ts` lines 116-138. | Add a release gate assertion that SDK options always include both `canUseTool` and hooks when write/shell tools can be exposed. |
| PRD-derived policy wording remains warning-limited. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Refresh or rule the PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active dependency posture remains anchored on event writer/session JSONL ownership, downstream path/write hooks, read MCP tool exposure, and REF-006 warning closure.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add an SDK-options invariant test proving every exposed write/shell surface has both callback and hook enforcement attached. | test | S | FIT | Current permission and hook tests remain green. |
| Keep bypass mode behind the explicit development environment gate and document it as non-release posture. | docs | S | FIT | Release policy review. |
| Close REF-006 by refreshing the accepted PRD hash or recording an explicit warning waiver. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-06-01 is substantially issuance-ready on code and test evidence. The remaining gate should focus on source-state warning closure and proving the overlay remains wired into every runtime options path, not on redesigning the permission model.
