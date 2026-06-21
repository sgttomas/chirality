# Assessment INSP-03: DEL-07-04 Status Transition API and MCP Tool

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-07-04 |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `210b5b7427471fc307ecbf6eecaab78ebf08398b` |
| Spec source | `Specification.md` lines 1-104 |

## Scope

DEL-07-04 covers parsing deliverable `_STATUS.md`, enforcing lifecycle transitions, exposing status read/transition APIs, and exposing Chirality MCP status tools with permission, path, event, and human-gate safeguards.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-07-04-REQ-001 | PASS | `frontend/src/lib/lifecycle/status-parser.ts` lines 123-160 and 212-237; `frontend/src/lib/workspace/deliverable-contracts.ts` lines 152-186. | `_STATUS.md` is parsed as the canonical deliverable lifecycle source. |
| DEL-07-04-REQ-002 | PASS | `frontend/src/lib/lifecycle/status-parser.ts` lines 80-110, 123-160, and 212-237; `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 51-74. | Current state, last updated date, and history entries are extracted from list and table formats. |
| DEL-07-04-REQ-003 | PASS | `frontend/src/lib/lifecycle/status-parser.ts` lines 3-10; `frontend/src/lib/lifecycle/transition.ts` lines 22-29. | The accepted lifecycle order is encoded in parser and transition modules. |
| DEL-07-04-REQ-004 | PASS | `frontend/src/lib/lifecycle/transition.ts` lines 152-176; `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 139-161. | Backward transitions are rejected. |
| DEL-07-04-REQ-005 | PASS | `frontend/src/lib/lifecycle/transition.ts` lines 66-72 and 152-176; `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 115-137. | Unauthorized actors are rejected. |
| DEL-07-04-REQ-006 | PASS | `frontend/src/lib/lifecycle/transition.ts` lines 64 and 178-193; `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 175-222. | Human-gate transitions require SHA-like approval evidence. |
| DEL-07-04-REQ-007 | PASS | `frontend/src/app/api/working-root/deliverable/status/route.ts` lines 5-17; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 130-144. | Status read route is implemented and tested. |
| DEL-07-04-REQ-008 | PASS | `frontend/src/app/api/working-root/deliverable/status/transition/route.ts` lines 52-70; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 146-173. | Status transition route is implemented and tested. |
| DEL-07-04-REQ-009 | PASS | `frontend/src/lib/harness/mcp/tool-names.ts` lines 1-29; `frontend/src/lib/harness/mcp/read-tools.ts` lines 434-457 and 511-551. | Status read and transition MCP tool names are registered. |
| DEL-07-04-REQ-010 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 491-533; `frontend/src/lib/harness/mcp/read-tools.ts` lines 511-551; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-204. | Status transition is write-gated and denied in read-only mode. |
| DEL-07-04-REQ-011 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-388 and 511-551; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-182. | MCP status tools share event/evidence, permission, and redaction handling. |
| DEL-07-04-REQ-012 | PASS | `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 184-204 and 284-309; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 175-211. | Policy, actor, and path denials block transitions. |
| DEL-07-04-REQ-013 | PASS | `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 120-182; `frontend/src/lib/harness/mcp/read-tools.ts` lines 299-388. | Events record tool execution metadata and do not claim agent approval. |
| DEL-07-04-REQ-014 | PARTIAL | `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 224-248; `frontend/src/lib/lifecycle/status-writer.ts` lines 125-160. | Approval SHA evidence is persisted, but content-change voiding is a governance/checklist rule rather than automatic enforcement. |
| DEL-07-04-REQ-015 | PASS | `frontend/src/__tests__/lib/lifecycle-status.test.ts` lines 51-262; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 130-328. | Parser, transition, invalid state, actor, approval SHA, and API cases are covered. |
| DEL-07-04-REQ-016 | PARTIAL | `frontend/src/app/api/working-root/deliverable/status/route.ts` lines 5-17; `frontend/src/app/api/working-root/deliverable/status/transition/route.ts` lines 52-70; `frontend/src/lib/harness/tool-descriptor.ts` lines 491-533. | Schemas are present in handlers/descriptors and tests, but no accepted standalone schema fixture pack was found. |
| DEL-07-04-REQ-017 | PARTIAL | `frontend/src/lib/lifecycle/transition.ts` lines 66-72 and 152-176. | Actor normalization is explicit and fail-closed for unsupported actors; full runtime identity mapping remains limited. |
| DEL-07-04-REQ-018 | PARTIAL | `_REFERENCES.md` REF-006 hash mismatch; `Specification.md` lines 102-104. | PRD-derived SHA criteria remain warning-bearing until REF-006 is reconciled or bypassed. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Standalone schema fixtures are not visible. | Medium | Route and descriptor code exists; `Specification.md` lines 40-43 leave exact schemas TBD. | Add accepted request/response fixture files or route-level golden shape tests. |
| Approval SHA binding is persisted but not automatically revalidated against content changes. | Medium | `frontend/src/lib/lifecycle/status-writer.ts` lines 125-160. | Keep as governance checklist unless a future accepted design adds content-hash validation. |
| Runtime actor identity mapping is narrow. | Low | `frontend/src/lib/lifecycle/transition.ts` lines 66-72. | Document or test all runtime caller identities that can invoke transitions. |
| REF-006 remains warning-limited. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-07-04 is a strong candidate for eventual issuance after source-warning and schema-fixture closure, but no lifecycle transition was performed here.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add accepted schema fixtures or golden route/MCP payload tests for status read and transition. | test | S | FIT | Current route/tool descriptors stable. |
| Document status approval SHA binding limits and content-change recheck responsibility. | docs/test | S | FIT | Governance decision to keep checklist-based binding. |
| Close REF-006 before issuance. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-07-04 is substantially implemented. The remaining gate issues are mostly fixture/source-state rigor rather than core lifecycle mechanics.
