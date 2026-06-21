# Assessment INSP-03: DEL-05-05 ToolResultStore and Session Artifacts

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-05 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `18511e933233b90ff2a84dd41f5b40041719c300` |
| Spec source | `Specification.md` lines 5-64 |

## Scope

DEL-05-05 covers tool result artifact storage under session folders, output budgets, redacted artifact persistence, metadata references in runtime events, replayability under malformed logs, deterministic ordering under tool activity, product-owned store boundaries, thresholds, naming, checksums, retention, and threshold-boundary validation.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-05-REQ001 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98. Focused validation passed. | Artifact storage is secondary to canonical `events.jsonl`; SDK transcripts do not become canonical. |
| DEL-05-05-REQ002 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98; `frontend/src/lib/harness/chirality-hooks.ts` lines 507-545. Focused validation passed. | Over-inline tool results are persisted as artifacts and referenced in event metadata. |
| DEL-05-05-REQ003 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-63. Focused validation passed. | Raw large result artifacts live under `.chirality/sessions/<sessionId>/artifacts/tools/` after redaction/truncation processing. |
| DEL-05-05-REQ004 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 22-39 and 132-172; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 36-75. Focused validation passed. | Inline skip and artifact/truncated cases exist; medium preview is not a distinct accepted behavior beyond metadata and truncated preview. |
| DEL-05-05-REQ005 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 86-98; `frontend/src/lib/harness/chirality-hooks.ts` lines 527-545. Focused validation passed. | Returned metadata includes relative path, byte counts, redaction, and truncation; explicit `turnId` and checksum are absent, and tool name lives in artifact content/event context. |
| DEL-05-05-REQ006 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-57; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-63. Focused validation passed. | Artifact payloads are redacted before write. |
| DEL-05-05-REQ007 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-75; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-83. Focused validation passed. | Redaction runs before storage, but no separate sensitive-value classification/withheld result policy exists. |
| DEL-05-05-REQ008 | PASS | `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1289. Focused validation passed. | Artifact references survive replay even with malformed JSONL lines. |
| DEL-05-05-REQ009 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/shell/harness-event-views.ts` lines 137-188; `frontend/src/__tests__/lib/harness-event-views.test.ts` lines 28-110. Focused validation passed. | Append order and first-seen tool rows are deterministic, but no explicit concurrent/interleaved artifact-write fixture proves accepted ordering metadata. |
| DEL-05-05-REQ010 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 132-172; `frontend/src/__tests__/lib/tool-evidence.test.ts` lines 33-73; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 25-83. Focused validation passed. | Output-budget tests exist for inline/artifact/huge results; medium preview/link behavior is still not fully specified. |
| DEL-05-05-REQ011 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 1-98; `frontend/src/lib/harness/tool-evidence.ts` lines 1-241. Focused validation passed. | Store/evidence interfaces are Chirality-owned and not SDK-shaped. |
| DEL-05-05-REQ012 | PARTIAL | `frontend/src/lib/harness/tool-descriptor.ts` lines 61-65 and 178-194; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98. | Thresholds and naming exist, but checksum and retention policy remain TBD. |
| DEL-05-05-REQ013 | PARTIAL | `frontend/src/lib/shell/harness-event-views.ts` lines 137-188; `frontend/src/__tests__/lib/harness-event-views.test.ts` lines 28-110. Focused validation passed. | Ordering derivation is tested, but not with concurrent/interleaved artifact persistence. |
| DEL-05-05-REQ014 | PARTIAL | `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 25-83; `frontend/src/__tests__/lib/tool-evidence.test.ts` lines 33-73. Focused validation passed. | Boundary-style tests exist for inline and huge cases, but final threshold-boundary verification awaits accepted threshold/checksum/retention decisions. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Metadata is useful but incomplete against the full spec. | Medium | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 86-98. | Add explicit `turnId` when available, checksum if accepted, and clarify whether tool name must be duplicated in returned metadata. |
| Concurrent/interleaved artifact ordering is not explicitly fixture-tested. | Medium | `Specification.md` lines 35 and 39. | Add a deterministic fixture with interleaved tool events, artifact writes, and accepted-turn ordering signal. |
| Retention/checksum policy remains TBD. | Low | `frontend/src/lib/harness/tool-descriptor.ts` lines 61-65 and 178-194. | Decide checksum/retention policy before issuance or explicitly defer it as non-blocking. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, final ToolResultStore implementation naming/location, output-budget policy parameters, checksum/retention policy, and concurrent-ordering fixture evidence.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Complete artifact metadata contract: optional `turnId`, checksum decision, and returned tool-name/path fields. | code/docs | S | FIT | Current artifact tests green. |
| Add concurrent/interleaved tool-result artifact replay fixture. | test | S | FIT | Event ordering policy accepted. |
| Decide retention and checksum requirements, or record an explicit deferral before issuance. | governance | S | FIT | Release-quality policy review. |

## Issuance-Gate-Process Observations

DEL-05-05 is close on core artifact mechanics but not on the complete metadata/concurrency/retention surface. The gate should treat the current store as functional evidence, not final acceptance.
