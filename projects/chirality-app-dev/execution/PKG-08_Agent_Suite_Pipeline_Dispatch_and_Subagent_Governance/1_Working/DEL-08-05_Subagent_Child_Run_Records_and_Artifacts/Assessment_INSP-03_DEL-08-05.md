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

DEL-08-05 covers subagent child-run records, runtime event mapping, JSONL event persistence, child output/artifact references, redaction, provider-neutral metadata boundaries, and the open denied-attempt allocation ruling.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-05-001 | PARTIAL | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 138-183; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 68-117. | The implemented record is `ChildRunRecord` with `childRunId`, not `HarnessSubagentRun` with `runId`. Core fields are present, but naming does not match the spec. |
| REQ-08-05-002 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 27-33; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 102-117 and 119-173. | Statuses include queued, denied, running, completed, failed, and cancelled. |
| REQ-08-05-003 | PARTIAL | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 185-225; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 646-720. | Parent turn, adapter IDs, and output artifact path are represented. Model, startedAt, and completedAt are not fields on the child-run record. |
| REQ-08-05-004 | PARTIAL | `frontend/src/lib/harness/event-schema.ts` lines 41-44; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1053-1169; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 558-644. | The implementation emits `subagent.progress` and `subagent.failed` in addition to started/completed. That is useful behavior, but it conflicts with the narrower sourced-event wording in the spec. |
| REQ-08-05-005 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1053-1169; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 688-719. | Harness events include child-run data, but the envelope uses `childRunId` rather than `runId`. |
| REQ-08-05-006 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22 and 50-84; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. | Harness events append one JSON record per line and replay in file order with malformed-line counting. |
| REQ-08-05-007 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 1114-1139 and 1145-1169; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98. | Child output file paths are carried when the SDK message provides them. Large child-output materialization under session artifacts was not proven separately. |
| REQ-08-05-008 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 7-14 and 77-98; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-83. | Tool-result artifact metadata carries relative path, byte counts, and truncation. It does not explicitly include parent turn ID, and the test is for tool artifacts rather than child-run output artifacts. |
| REQ-08-05-009 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-63. | Event and tool-artifact redaction paths are covered. Child-output artifact redaction was not separately proven. |
| REQ-08-05-010 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 62-69 and 228-239; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 119-150. | Adapter-specific identifiers stay under adapter metadata and are stripped from provider-neutral records. |
| REQ-08-05-011 | PASS | `plans/artifacts/runtime_capability_matrix.md` lines 45-46; `frontend/src/lib/harness/agent-runtime-contract.ts` lines 10-25. | Current implementation uses the new contract and does not reactivate retired pipeline run-record mechanics. |
| REQ-08-05-012 | PARTIAL | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 138-183; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 102-117. | Denied delegation records are possible, but the human ruling about pre-allocation denial as child record vs permission event remains open. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G5: child-run contract naming mismatch remains. | High | Spec asks for `HarnessSubagentRun`/`runId`; implementation uses `ChildRunRecord`/`childRunId`. | Choose one canonical shape and amend either the code/types or DEL-08-05 before issuance. |
| Event taxonomy is broader than the spec. | Medium | `event-schema.ts` includes progress/failed; mapper emits them. | Amend the spec if progress/failed are accepted, or collapse terminal failures into the sourced completed-event pattern. |
| Child output artifact guarantees are partial. | Medium | Tool artifact persistence is tested, but child-output materialization/redaction is mostly adapter-path metadata. | Add a child-output artifact fixture that proves storage path, byte counts, truncation, redaction, and replay linkage. |
| Denied-attempt allocation ruling remains open. | Low | `createDelegationChildRunRecord` can record denied state, but the spec still calls for human ruling on pre-allocation denial. | Raise or fold this into the INSP-04/05 gate-process and roadmap decisions. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-08-05 remains the main PKG-08 package reconciliation item because the child-run record exists but does not match the spec shape exactly.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Resolve `runId` vs `childRunId` and `HarnessSubagentRun` vs `ChildRunRecord` as the canonical contract. | reconcile | S | FIT | INSP-04 or roadmap decision. |
| Add child-output artifact fixtures covering redaction, byte counts, truncation, relative paths, and replay linkage. | code/test | M | FIT | Canonical child-run contract. |
| Decide whether `subagent.progress` and `subagent.failed` are accepted product event categories. | reconcile | S | FIT | Event taxonomy decision. |
| Record the denied-attempt allocation rule. | decision/doc | S | FIT | Human ruling. |

## Issuance-Gate-Process Observations

DEL-08-05 is the strongest PKG-08 evidence that inspection should feed a reconciliation roadmap before issuance. The runtime substrate exists, but the public contract name, event taxonomy, and child-output artifact proof need one canonical decision.
