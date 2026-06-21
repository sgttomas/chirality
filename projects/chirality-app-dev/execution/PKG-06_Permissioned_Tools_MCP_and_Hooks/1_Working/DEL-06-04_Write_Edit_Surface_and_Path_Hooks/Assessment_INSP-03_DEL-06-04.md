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
| DEL-06-04-REQ005 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 230-283; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-348. | The write hook independently rejects missing, unreadable, or stale `Edit.old_string` preconditions before SDK execution and records exact-edit allow/deny metadata. |
| DEL-06-04-REQ006 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 462-477; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-259 and 370-449. | Hook exceptions and policy denials fail closed with blocking hook output. |
| DEL-06-04-REQ007 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 117-123 and 354-381; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 137-151. | Explicit denies override allow/ask decisions. |
| DEL-06-04-REQ008 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-138; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 290-319. | `allowedTools` does not bypass callback and hook enforcement. |
| DEL-06-04-REQ009 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 987-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 147-192 and 290-319. | Read-only denies write/edit; workspaceWrite exposes them only through descriptor/permission/hook policy. |
| DEL-06-04-REQ010 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-388 and 511-586; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-309. | Mutating MCP tools use the same permission/path/evidence wrapper before status/dependency mutations. |
| DEL-06-04-REQ011 | PASS | `frontend/src/lib/atomic-write.ts` lines 10-35; `frontend/src/lib/lifecycle/transition.ts`; `frontend/src/lib/workspace/deliverable-contracts.ts`; `frontend/src/__tests__/lib/atomic-write.test.ts` lines 25-47. | Chirality-owned controlled status/dependency writes use same-directory temp-file rename and clean up temp files on failed rename; provenance summaries remain in the hook evidence path. |
| DEL-06-04-REQ012 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 288-315 and 383-389; `frontend/src/lib/harness/chirality-hooks.ts` lines 359-461. | Write attempts and denials create permission/hook evidence. |
| DEL-06-04-REQ013 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 444-459 and 527-548; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 101-165. | Provenance captures before/after file state, bounded diff summaries, artifacts, and redacted result metadata. |
| DEL-06-04-REQ014 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 121-190; `frontend/src/lib/harness/tool-path-policy.ts` lines 95-160. | Relevant paths are checked with lstat/regular-file/symlink-aware logic for write policy and evidence. |
| DEL-06-04-REQ015 | PASS | `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 45-259; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 414-511; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-309. | Tests cover allowed writes, outside-root/instruction-root/symlink denials, provenance/events, and mutating MCP denial before execution. |
| DEL-06-04-REQ016 | PASS | `_REFERENCES.md` REF-006 `MATCH`; this assessment's Source-State Caveat. | PRD-derived controlled-write behavior is no longer warning-limited in active review records. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Exact-edit precondition residual is closed by ADQ-11. | Low | `frontend/src/lib/harness/chirality-hooks.ts` lines 230-283; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-348. | Preserve hook-side stale-precondition denial as the canonical behavior for SDK `Edit`. |
| Atomic controlled-write residual is closed by ADQ-11. | Low | `frontend/src/lib/atomic-write.ts` lines 10-35; `frontend/src/__tests__/lib/atomic-write.test.ts` lines 25-47. | Keep controlled writer call sites on same-directory atomic rename where the writer owns the mutation. |
| Historical REF-006 warning text in older run records is retired for active review. | Low | `_REFERENCES.md` REF-006 is `MATCH` under the D-APP-38 authority corpus v2. | Keep the D-APP-38 reference status check in closeout validation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as
`MATCH` under the D-APP-38 authority corpus v2. Historical HASH_MISMATCH notes in `_run_records`
remain archival only.

## Dependency Closure Note

ADQ-11 satisfies the exact-edit, controlled-write atomicity, and REF-006 source-state residuals for
this deliverable. Other active rows remain pending for DEL-06-01 permission overlay, DEL-07-01
resolver/tool exposure, and DEL-06-06 hook lifecycle mirror unless separately closed by their owning
deliverables.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Preserve hook-side exact-edit stale-precondition checks as the canonical SDK `Edit` behavior. | code/docs | S | FIT | Future write/edit adapter change. |
| Preserve same-directory atomic rename for Chirality-owned controlled writes. | test | S | FIT | Future controlled-write call site. |
| Keep D-APP-38 authority-corpus status clean during future authority-document edits. | governance | S | FIT | Authority-document edits occur. |

## Issuance-Gate-Process Observations

DEL-06-04 is strong for path containment and provenance evidence. ADQ-11 closes the exact-edit
precondition ownership, controlled-write atomicity, and PRD source-state residuals. This does not
advance lifecycle state or make an issuance claim.
