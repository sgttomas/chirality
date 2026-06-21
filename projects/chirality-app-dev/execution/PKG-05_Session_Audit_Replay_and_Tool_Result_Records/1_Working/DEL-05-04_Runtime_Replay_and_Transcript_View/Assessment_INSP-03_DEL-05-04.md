# Assessment INSP-03: DEL-05-04 Runtime Replay and Transcript View

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-04 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `18511e933233b90ff2a84dd41f5b40041719c300` |
| Spec source | `Specification.md` lines 5-66 |

## Scope

DEL-05-04 covers replay from canonical `events.jsonl`, ordered parsing, malformed-tail tolerance, accepted turns and terminal outcomes, assistant/tool/artifact/SDK linkage display, legacy discovery, fixtures, and final parser/route/component ownership for a transcript view.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-04-REQ001 | PASS | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/app/api/harness/session/[id]/events/route.ts` lines 12-28; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1322. Focused validation passed. | Replay reads canonical per-session `events.jsonl`. |
| DEL-05-04-REQ002 | PASS | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1289. Focused validation passed. | Valid records are returned in file/write order. |
| DEL-05-04-REQ003 | PASS | `frontend/src/lib/harness/session-events.ts` lines 62-76; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1289. Focused validation passed. | Malformed lines are ignored with an honest count while preserving valid events. |
| DEL-05-04-REQ004 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22 and 50-85; `frontend/src/lib/harness/types.ts` lines 30-35. Focused validation passed. | SDK transcripts are metadata only unless an explicit import path is later accepted. |
| DEL-05-04-REQ005 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-230 and 279-363; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. Focused validation passed. | Accepted turns and terminal events are persisted, but no complete transcript reconstruction model is present. |
| DEL-05-04-REQ006 | PARTIAL | `frontend/src/lib/shell/harness-event-views.ts` lines 137-188 and 287-324; `frontend/src/__tests__/lib/harness-event-views.test.ts` lines 28-185. Focused validation passed. | Tool/subagent rows derive from replayable events; full assistant transcript, artifact-link view, and SDK-link presentation are incomplete. |
| DEL-05-04-REQ007 | PASS | `frontend/src/lib/harness/types.ts` lines 30-40; `frontend/src/lib/harness/sdk-message-mapper.ts` metadata mapping references; focused SDK mapper tests passed. | SDK session IDs, names, transcript implications, and store keys are adapter metadata. |
| DEL-05-04-REQ008 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 25-33. Focused validation passed. | Appended and bridged events are redacted, but replay of a preexisting manually written raw secret line would return stored data as-is. |
| DEL-05-04-REQ009 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 71-82 and 127-152; `frontend/src/app/api/harness/session/[id]/events/route.ts` lines 18-28. Focused validation passed. | Legacy flat sessions are discoverable through session APIs, but replay discovery itself is event-log based and not a full migration view. |
| DEL-05-04-REQ010 | PARTIAL | `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1322; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197; `frontend/scripts/validate-harness-section9.mjs` includes `section9.session_event_replay` but not `section9.sdk_session_link_resume`. | Append/replay/malformed/artifact fixtures exist; SDK link/resume validation ID is missing. |
| DEL-05-04-REQ011 | PARTIAL | `frontend/src/lib/shell/harness-event-views.ts` lines 137-188; `frontend/src/__tests__/lib/harness-event-views.test.ts` lines 28-110. Focused validation passed. | Tool summaries and artifact metadata can be derived, but there is not yet a first-class transcript view with artifact links. |
| DEL-05-04-REQ012 | FAIL | `frontend/src/app/api/harness/session/[id]/events/route.ts` lines 12-28; `frontend/src/lib/shell/harness-event-views.ts` lines 1-324. | Parser and replay route exist, but the requested runtime transcript view/component model is not implemented as a complete product surface. |
| DEL-05-04-REQ013 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/app/api/harness/session/[id]/events/route.ts` lines 12-28; `frontend/src/lib/shell/harness-event-views.ts` lines 1-324. | Accepted paths can be named for event replay and derived activity rows; transcript-model/component/SDK-link paths remain TBD. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Full runtime transcript view is absent. | High | `Specification.md` lines 5-13 and 56-66; `frontend/src/app/api/harness/session/[id]/events/route.ts` lines 12-28. | Build a bounded transcript model/view over replayed events, with assistant output, terminal outcome, tool summaries, artifact links, and SDK metadata. |
| Replay redaction relies on redacted write paths, not read-time sanitization. | Medium | `frontend/src/lib/harness/session-events.ts` lines 50-85. | Either assert persisted-log trust after redaction proof, or add read-time redaction defense for legacy/imported logs. |
| Section 9 validation lacks SDK session link/resume replay coverage. | Medium | `frontend/scripts/validate-harness-section9.mjs` validation IDs; DEL-04/DEL-05 specs. | Add or rename the Section 9 proof ID after transcript/linkage behavior is implemented. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for DEL-05-01 canonical session layout, DEL-05-02 event schema, DEL-04-01 SDK transcript placement, DEL-05-03 redaction, and DEL-05-05 artifact-link replay.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Implement a product-owned replay transcript model and component over canonical events. | code | M | FIT | Keep event replay route stable. |
| Add read-time redaction or an explicit legacy/import trust boundary for replayed logs. | code/test | S | FIT | Redaction matrix accepted. |
| Add Section 9 validation for SDK session link/resume and artifact-link replay once the view exists. | validation | S | FIT | Transcript view landed. |

## Issuance-Gate-Process Observations

DEL-05-04 is a clear gate failure for the transcript-view portion while the lower-level replay parser is healthy. The process should keep the distinction: event replay is implemented; product transcript replay is not.
