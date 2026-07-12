# Assessment INSP-03: DEL-05-05 ToolResultStore and Session Artifacts

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-05 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | ADQ-10 working tree after `43b039ba4e40ee6a06d5527129e885c06bc74881` |
| Spec source | `Specification.md` lines 5-64 |

## Scope

DEL-05-05 covers tool result artifact storage under session folders, output budgets, redacted artifact persistence, metadata references in runtime events, replayability under malformed logs, deterministic ordering under tool activity, product-owned store boundaries, thresholds, naming, checksums, retention, and threshold-boundary validation. ADQ-10 specifically closes artifact metadata, SHA-256 checksum, session-lifetime retention, and interleaved replay evidence under D-APP-42.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-05-REQ001 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 93-118. Focused validation passed. | Artifact storage is secondary to canonical `events.jsonl`; SDK transcripts do not become canonical. |
| DEL-05-05-REQ002 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 38-118; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 455-495. Focused validation passed. | Over-inline tool results are persisted as artifacts and referenced in event metadata. |
| DEL-05-05-REQ003 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 93-118; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 44-99. Focused validation passed. | Large result artifacts live under `.chirality/sessions/<sessionId>/artifacts/tools/` after redaction/truncation processing. |
| DEL-05-05-REQ004 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 22-39 and 132-172; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 36-75. Focused validation passed. | Inline skip and artifact/truncated cases exist; medium preview is not a distinct accepted behavior beyond metadata and truncated preview. |
| DEL-05-05-REQ005 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 8-19 and 107-118; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 455-495; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 44-99; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 451-479. Focused validation passed. | Returned metadata includes relative path, original/stored byte counts, redaction, truncation, SHA-256, `toolName`, optional `turnId` where available, and `session-lifetime` retention. |
| DEL-05-05-REQ006 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-57; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-63. Focused validation passed. | Artifact payloads are redacted before write. |
| DEL-05-05-REQ007 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-75; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-83. Focused validation passed. | Redaction runs before storage, but no separate sensitive-value classification/withheld result policy exists. |
| DEL-05-05-REQ008 | PASS | `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1289. Focused validation passed. | Artifact references survive replay even with malformed JSONL lines. |
| DEL-05-05-REQ009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 234-325. Focused validation passed. | Interleaved tool starts/completions replay in JSONL append order with checksum and retention metadata preserved. |
| DEL-05-05-REQ010 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 132-172; `frontend/src/__tests__/lib/tool-evidence.test.ts` lines 33-73; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 25-83. Focused validation passed. | Output-budget tests exist for inline/artifact/huge results; medium preview/link behavior is still not fully specified. |
| DEL-05-05-REQ011 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 1-98; `frontend/src/lib/harness/tool-evidence.ts` lines 1-241. Focused validation passed. | Store/evidence interfaces are Chirality-owned and not SDK-shaped. |
| DEL-05-05-REQ012 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 61-65 and 178-194; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 93-118; D-APP-42. | Thresholds and naming remain the existing descriptor/artifact-writer policy; checksum is SHA-256 and retention is session-lifetime only. |
| DEL-05-05-REQ013 | PASS | `frontend/src/__tests__/lib/session-events.test.ts` lines 234-325. Focused validation passed. | Interleaved artifact events assert JSONL append order as the accepted ordering signal. |
| DEL-05-05-REQ014 | PARTIAL | `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 30-99; `frontend/src/__tests__/lib/tool-evidence.test.ts` lines 33-73. Focused validation passed. | Boundary-style tests exist for inline and huge cases under current thresholds. Distinct medium-preview boundary behavior remains outside ADQ-10. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Distinct medium-preview behavior is not yet separated from artifact-overflow metadata. | Medium | `frontend/src/lib/harness/tool-evidence.ts` lines 22-39 and 132-172. | Handle as future output-budget product policy if medium preview requires a different runtime representation from current descriptor-defined overflow metadata. |
| Sensitive-value classification beyond redaction is not a separate policy. | Medium | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 51-91. | Add a withheld-result classification only if a later governance decision requires blocking raw artifact storage beyond redaction/truncation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: D-APP-38 authority corpus v2 records REF-006 as `MATCH` in `_REFERENCES.md`. Historical source-state warnings in run records remain historical only.

## Dependency Closure Note

ADQ-10 satisfies the active dependency rows for REF-006 source state, ToolResultStore implementation path, and D-APP-42 checksum/retention policy. Remaining threshold/preview/naming behavior is the existing descriptor policy and is unchanged by this tranche.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Consider whether medium-preview output needs a distinct runtime representation beyond current artifact-overflow metadata. | code/docs | S | FIT | Future output-budget policy change. |
| Consider whether sensitive-result withholding is needed in addition to redaction. | governance/code | S | FIT | Future redaction/storage policy change. |

## Issuance-Gate-Process Observations

ADQ-10 closes the metadata/concurrency/checksum/retention surface targeted by the autonomous queue. The gate should still treat the remaining medium-preview and sensitive-withholding notes as future output-budget policy questions rather than release or issuance acceptance.

## D-APP-56 R5 P44 pointer annotation (2026-07-12)

The REQ012 evidence citation above preserves the `frontend/src/lib/harness/tool-descriptor.ts` path inspected at assessment time. D-APP-48 subsequently relocated that contract to `frontend/packages/harness-contract/src/tool-descriptor.ts`. The PASS conclusion is unchanged; this is an evidence-pointer annotation only.
