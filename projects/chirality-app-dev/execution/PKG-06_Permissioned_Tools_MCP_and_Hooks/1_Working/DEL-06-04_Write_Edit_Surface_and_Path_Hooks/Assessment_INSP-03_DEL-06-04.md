# Assessment INSP-03: DEL-06-04 Write/Edit Surface and Path Hooks

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-04 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-76 |

## Scope

DEL-06-04 covers governed Write/Edit and mutating MCP surfaces, project-root containment, instruction-root protection, symlink rejection, exact edit preconditions, fail-closed hook behavior, provenance and diff evidence, and write-attempt event records.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-04-REQ001 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 331-461; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 45-165. | A `PreToolUse` hook gates governed write/shell/subagent descriptors before mutation. |
| DEL-06-04-REQ002 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 162-225; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-259. | Write paths resolving outside the active project root are blocked. |
| DEL-06-04-REQ003 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 234-248; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-259. | Writes under the instruction root are denied. |
| DEL-06-04-REQ004 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 95-160 and 250-259; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 414-511. | Symlink write paths are rejected during policy evaluation before SDK execution continues. |
| DEL-06-04-REQ005 | PARTIAL | `frontend/src/lib/harness/tool-descriptor.ts` lines 609-651; `frontend/src/lib/harness/chirality-hooks.ts` lines 424-461. | `Edit` descriptor requires `old_string` and `new_string`, but exact edit precondition enforcement is delegated to SDK/tool execution rather than independently rechecking in the hook. |
| DEL-06-04-REQ006 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 462-477; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-259 and 370-449. | Hook exceptions and policy denials fail closed with blocking hook output. |
| DEL-06-04-REQ007 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 117-123 and 354-381; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 137-151. | Explicit denies override allow/ask decisions. |
| DEL-06-04-REQ008 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-138; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 290-319. | `allowedTools` does not bypass callback and hook enforcement. |
| DEL-06-04-REQ009 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 147-192 and 290-319. | Read-only denies write/edit; workspaceWrite exposes them only through descriptor/permission/hook policy. |
| DEL-06-04-REQ010 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-388 and 511-586; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-309. | Mutating MCP tools use the same permission/path/evidence wrapper before status/dependency mutations. |
| DEL-06-04-REQ011 | PARTIAL | `frontend/src/lib/harness/chirality-hooks.ts` lines 121-190 and 527-548; `frontend/src/lib/harness/mcp/read-tools.ts` lines 338-367; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 45-165. | Diff/provenance summaries exist and controlled MCP writes report before/after file evidence; atomic write guarantees are not separately proven. |
| DEL-06-04-REQ012 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 288-315 and 383-389; `frontend/src/lib/harness/chirality-hooks.ts` lines 359-461. | Write attempts and denials create permission/hook evidence. |
| DEL-06-04-REQ013 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 444-459 and 527-548; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 101-165. | Provenance captures before/after file state, bounded diff summaries, artifacts, and redacted result metadata. |
| DEL-06-04-REQ014 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 121-190; `frontend/src/lib/harness/tool-path-policy.ts` lines 95-160. | Relevant paths are checked with lstat/regular-file/symlink-aware logic for write policy and evidence. |
| DEL-06-04-REQ015 | PASS | `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 45-259; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 414-511; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-309. | Tests cover allowed writes, outside-root/instruction-root/symlink denials, provenance/events, and mutating MCP denial before execution. |
| DEL-06-04-REQ016 | PASS | `_REFERENCES.md` REF-006 hash mismatch; this assessment's Source-State Caveat. | PRD-derived controlled-write behavior is warning-qualified until source-state closure. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Exact edit precondition is not independently enforced by Chirality hook code. | Medium | `frontend/src/lib/harness/tool-descriptor.ts` lines 636-650; `frontend/src/lib/harness/chirality-hooks.ts` lines 424-461. | Add an optional hook-side stale/missing `old_string` precheck for `Edit` or explicitly document reliance on SDK exact-edit semantics. |
| Atomic write guarantees are not separately demonstrated. | Low | `frontend/src/lib/harness/chirality-hooks.ts` lines 527-548; mutating MCP uses workspace writer internals. | Add a small controlled-write atomicity note/test once write APIs are finalized. |
| REF-006 remains warning-limited for controlled-write behavior. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive the PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for DEL-06-01 permission overlay, DEL-07-01 resolver/tool exposure, DEL-06-06 hook lifecycle mirror, and REF-006 warning closure.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Decide whether Chirality must perform hook-side exact-edit stale-precondition checks or explicitly rely on SDK `Edit` semantics. | code/docs | S | FIT | Write/edit adapter contract accepted. |
| Add an atomicity or failure-mode fixture for controlled write paths if required by issuance. | test | S | FIT | Controlled-write implementation location finalized. |
| Close REF-006 before issuance. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-06-04 is strong for path containment and provenance evidence. Issuance should focus on the exact-edit precondition ownership decision, atomicity evidence if required, and PRD source-state closure.
