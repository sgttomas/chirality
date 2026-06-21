# Assessment INSP-03: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-01 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `18511e933233b90ff2a84dd41f5b40041719c300` |
| Spec source | `Specification.md` lines 5-68 |

## Scope

DEL-05-01 covers canonical `.chirality/sessions/<sessionId>/` layout, legacy flat-session compatibility, normalized session CRUD, SDK linkage metadata, safe migration posture, and session-root override behavior.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-01-R001 | FAIL | `frontend/src/lib/harness/session-manager.ts` lines 67-101. Focused validation passed for existing behavior. | New session records are still written as flat `{sessionId}.json`, not as canonical folders with `session.json`. |
| DEL-05-01-R002 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98. Focused validation passed. | `events.jsonl` and `artifacts/tools/*` are folder-backed, but `session.json`, `turns/`, and `sdk/` are not created by the primary session manager. |
| DEL-05-01-R003 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 71-82 and 103-110; `frontend/src/__tests__/api/harness/routes.test.ts` lines 151-189. Focused validation passed. | Existing flat session records remain readable through get/resume routes. |
| DEL-05-01-R004 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 127-164; `frontend/src/__tests__/api/harness/routes.test.ts` lines 151-189. Focused validation passed. | Flat records list, resume, get, and delete under the current store. |
| DEL-05-01-R005 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 12-14, 84-101, and 127-152; `frontend/src/app/api/harness/session/create/route.ts` lines 12-32; `frontend/src/app/api/harness/session/list/route.ts` lines 8-16. Focused validation passed. | CRUD remains bound to the normalized session root and project-root filter. |
| DEL-05-01-R006 | PARTIAL | `frontend/src/lib/harness/types.ts` lines 23-42; `frontend/src/lib/harness/turn-engine.ts` lines 329-341; `frontend/src/__tests__/api/harness/routes.test.ts` lines 251-282. Focused validation passed. | Stable session metadata and SDK linkage fields exist, but the storage carrier is still flat JSON, not canonical `session.json`. |
| DEL-05-01-R007 | PASS | `frontend/src/lib/harness/types.ts` lines 30-40; `frontend/src/lib/harness/turn-engine.ts` lines 329-341. Focused validation passed. | SDK IDs and boot metadata are adapter metadata, not Chirality identity replacements. |
| DEL-05-01-R008 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | Runtime audit events append to canonical per-session `events.jsonl`. |
| DEL-05-01-R009 | PARTIAL | `frontend/src/lib/harness/types.ts` lines 30-35; `frontend/src/lib/harness/sdk-message-mapper.ts` records transcript-linkage implications in mapped metadata. Focused validation passed. | SDK transcript path/store-key fields exist, but transcript placement and replay linkage are not fully closed. |
| DEL-05-01-R010 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 154-164; `Dependencies.csv` rows for duplicate folder/flat delete semantics. | There is no destructive conversion, but duplicate folder/flat semantics and tested migration behavior remain unresolved. |
| DEL-05-01-R011 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 84-101; `frontend/src/__tests__/api/harness/routes.test.ts` lines 151-189. Focused validation passed. | Session IDs are stable and generated once at create. |
| DEL-05-01-R012 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 67-110; `Specification.md` lines 39-40. | The current flat path preserves IDs, but path-changing migration has not been implemented or fixture-tested. |
| DEL-05-01-R013 | PARTIAL | `frontend/src/lib/harness/run-logger.ts` lines 64-109; `frontend/src/lib/harness/session-events.ts` lines 14-22. Focused validation passed. | Event and tool paths redact configured keys, but whole-product session/transcript/artifact secret proof remains shared with DEL-05-03 and release gates. |
| DEL-05-01-R014 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 12-14; `frontend/src/lib/harness/session-events.ts` lines 6-8; test setup in `frontend/src/__tests__/api/harness/routes.test.ts` lines 129-130. Focused validation passed. | `CHIRALITY_SESSION_ROOT` override is honored by session and event stores. |
| DEL-05-01-R015 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 67-164; `frontend/src/lib/harness/session-events.ts` lines 6-85. | Current implementation paths are discoverable, but canonical-folder migration APIs and final helper names remain TBD. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Canonical folder-backed session record storage is not implemented. | High | `frontend/src/lib/harness/session-manager.ts` lines 67-101. | Add canonical folder create/read/write with `session.json`, then keep flat records as legacy read/list/resume/delete inputs until migration is deliberately closed. |
| Duplicate folder/flat delete and list semantics are unresolved. | Medium | `Dependencies.csv` active duplicate semantics row; `frontend/src/lib/harness/session-manager.ts` lines 127-164. | Define deterministic precedence and deletion behavior before enabling destructive migration. |
| SDK transcript/store placement is metadata-only and not replay-closed. | Medium | `frontend/src/lib/harness/types.ts` lines 30-35; DEL-04-01/DEL-05-04 dependency handoffs. | Carry transcript placement into DEL-05-04 and avoid treating SDK transcripts as project truth. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for canonical session-folder implementation, OI-002 SDK transcript placement, duplicate flat/folder semantics, and downstream DEL-05-02/DEL-05-04/DEL-05-05 handoffs.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Implement folder-backed session records with `session.json` while preserving flat legacy reads. | code | M | FIT | Keep current session route tests green. |
| Add explicit migration fixtures for flat-only, folder-only, duplicate flat/folder, delete, list, and resume cases. | test | M | FIT | Canonical folder API landed. |
| Record SDK transcript/store placement as secondary adapter metadata, not authoritative session truth. | reconcile | S | FIT | DEL-05-04 replay assessment complete. |

## Issuance-Gate-Process Observations

DEL-05-01 is not issuance-ready because the central canonical-session-layout requirement is still absent in code. The gate process is useful here: it separates working event/artifact folders from the unimplemented primary session-folder migration.
