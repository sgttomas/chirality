# Assessment INSP-03: DEL-08-05 Subagent Child Run Records and Artifacts

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-08-05 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `d92ef1253b37cd29423672acb146a9e9c91087d5` |
| Spec source | `Specification.md` lines 1-74 |

## Scope

DEL-08-05 covers subagent child-run records, runtime event mapping, JSONL event persistence, child output/artifact references, redaction, provider-neutral metadata boundaries, and the denied-attempt allocation boundary now ruled by D-APP-40.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-05-001 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 138-183; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 68-117; D-APP-40. | `ChildRunRecord` with `childRunId` is the canonical shape. |
| REQ-08-05-002 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 27-33; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 102-117 and 119-173. | Statuses include queued, denied, running, completed, failed, and cancelled. |
| REQ-08-05-003 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 185-225; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 646-720; D-APP-40. | Parent turn, adapter IDs, and output artifact path are represented under the canonical `ChildRunRecord` shape. |
| REQ-08-05-004 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 41-44; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1053-1169; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 558-644; D-APP-40. | D-APP-40 accepts `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed` as provider-neutral child lifecycle categories. |
| REQ-08-05-005 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1053-1169; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 688-719; D-APP-40. | Harness events include canonical `childRunId` linkage. |
| REQ-08-05-006 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22 and 50-84; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. | Harness events append one JSON record per line and replay in file order with malformed-line counting. |
| REQ-08-05-007 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1114-1139 and 1145-1169; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98. | Child output file paths are carried when the SDK message provides them. Large child-output materialization under session artifacts was not proven separately. |
| REQ-08-05-008 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 7-14 and 77-98; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-83. | Tool-result artifact metadata carries relative path, byte counts, and truncation. It does not explicitly include parent turn ID, and the test is for tool artifacts rather than child-run output artifacts. |
| REQ-08-05-009 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-63. | Event and tool-artifact redaction paths are covered. Child-output artifact redaction was not separately proven. |
| REQ-08-05-010 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 62-69 and 228-239; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 119-150. | Adapter-specific identifiers stay under adapter metadata and are stripped from provider-neutral records. |
| REQ-08-05-011 | PASS | `plans/artifacts/runtime_capability_matrix.md` lines 45-46; `frontend/src/lib/harness/agent-runtime-contract.ts` lines 10-25. | Current implementation uses the new contract and does not reactivate retired pipeline run-record mechanics. |
| REQ-08-05-012 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 138-183; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 102-117; D-APP-40. | Denied child records are required only after the runtime reaches the child-run record layer; earlier denials may remain permission/hook evidence. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Child-output artifact guarantees are partial. | Medium | Tool artifact persistence is tested, but child-output materialization/redaction is mostly adapter-path metadata. | Add a child-output artifact fixture that proves storage path, byte counts, truncation, redaction, and replay linkage. |

## Source-State Caveat

D-APP-38 established the authority-corpus reference model. Current `_REFERENCES.md` records REF-006 as `MATCH`; future authority-document edits require a corpus bump/apply before acceptance. No semantic files were used or produced.

## Dependency Closure Note

This ADQ-05 supersession does not claim lifecycle issuance. DEL-08-05 no longer has a child-run naming or denied-allocation ruling blocker; child-output artifact proof remains a separate residual.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add child-output artifact fixtures covering redaction, byte counts, truncation, relative paths, and replay linkage. | code/test | M | FIT | Canonical child-run contract. |

## Issuance-Gate-Process Observations

DEL-08-05 still needs child-output artifact proof before any issue-readiness claim, but D-APP-40 and ADQ-05 resolve the public contract name, event taxonomy, and denied-allocation decision findings.
