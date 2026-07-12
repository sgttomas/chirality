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
| ADQ-09 update | Runtime transcript view, read-time replay redaction, replay API transcript payload, sidebar tab, and Section 9 SDK link/resume validation ID added 2026-06-21. |

## Scope

DEL-05-04 covers replay from canonical `events.jsonl`, ordered parsing, malformed-tail tolerance, accepted turns and terminal outcomes, assistant/tool/artifact/SDK linkage display, legacy discovery, fixtures, and final parser/route/component ownership for a transcript view.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-04-REQ001 | PASS | `frontend/src/lib/harness/session-events.ts`; `frontend/src/app/api/harness/session/[id]/events/route.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`. Focused ADQ-09 replay validation passed. | Replay reads canonical per-session `events.jsonl` and the route enriches replay with session and transcript data. |
| DEL-05-04-REQ002 | PASS | `frontend/src/lib/harness/session-events.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts`. Focused ADQ-09 replay validation passed. | Valid records are returned and projected in file/write order. |
| DEL-05-04-REQ003 | PASS | `frontend/src/lib/harness/session-events.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`. Focused ADQ-09 replay validation passed. | Malformed lines are ignored with an honest count while preserving valid events. |
| DEL-05-04-REQ004 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22 and 50-85; `frontend/src/lib/harness/types.ts` lines 30-35. Focused validation passed. | SDK transcripts are metadata only unless an explicit import path is later accepted. |
| DEL-05-04-REQ005 | PASS | `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`. Focused ADQ-09 transcript validation passed. | Transcript projection includes user/assistant message events and terminal outcomes, including `turn.interrupted`. |
| DEL-05-04-REQ006 | PASS | `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/components/shell/transcript-stream-view.tsx`; `frontend/src/__tests__/components/harness-stream-views.test.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts`. Focused ADQ-09 transcript validation passed. | Assistant deltas/completions, tool summaries, artifact links, and SDK transcript/store linkage are represented when available. |
| DEL-05-04-REQ007 | PASS | `frontend/src/lib/harness/types.ts`; `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts`. Focused ADQ-09 transcript validation passed. | SDK session IDs, transcript paths, store keys, package versions, and model remain adapter metadata under `sdkLinkage`. |
| DEL-05-04-REQ008 | PASS | `frontend/src/lib/harness/session-events.ts`; `frontend/src/__tests__/lib/session-events.test.ts`. Focused ADQ-09 replay validation passed. | Replay now redacts parsed JSONL at read time, including manually imported raw secret lines. |
| DEL-05-04-REQ009 | PASS | `frontend/src/lib/harness/session-manager.ts`; `frontend/src/app/api/harness/session/[id]/events/route.ts`; `frontend/src/__tests__/lib/session-manager.test.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`; D-APP-41. | Legacy flat sessions are read through eager conversion, and replay lookup now loads the canonical session record before transcript projection. |
| DEL-05-04-REQ010 | PASS | `frontend/src/__tests__/api/harness/routes.test.ts`; `frontend/src/__tests__/lib/session-events.test.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts`; `frontend/src/__tests__/lib/session-manager.test.ts`; `frontend/scripts/validate-harness-section9.mjs`. | Append/replay, malformed JSONL, SDK link/resume metadata, and transcript projection are fixture-covered; Section 9 includes `section9.session_event_replay` and `section9.sdk_session_link_resume`. |
| DEL-05-04-REQ011 | PASS | `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/components/shell/transcript-stream-view.tsx`; `frontend/src/__tests__/components/harness-stream-views.test.ts`. | Tool results are represented by compact summary and artifact metadata/path, not raw large payloads. |
| DEL-05-04-REQ012 | PASS | `frontend/src/lib/harness/session-events.ts`; `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/app/api/harness/session/[id]/events/route.ts`; `frontend/src/components/shell/transcript-stream-view.tsx`. | Parser, model/interface, API, and component ownership paths are assigned by ADQ-09. |
| DEL-05-04-REQ013 | PASS | `Specification.md`; `Procedure.md`; `Datasheet.md`; `Evidence_ADQ-09_Runtime_Transcript_View.md`. | Accepted replay parser, transcript model/interface, route/component, and fixture paths are recorded. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| None for ADQ-09 scope. | N/A | Runtime transcript model/view, read-time redaction, replay API transcript payload, focused fixtures, and Section 9 SDK link/resume validation ID are implemented. | ADQ-10 remains a separate queue item for DEL-05-05 checksum/retention policy and does not block ADQ-09 transcript replay closure. |

## Source-State Caveat

D-APP-38 authority corpus v2 is current for this deliverable: `_REFERENCES.md` records `MATCH` for `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and `docs/PRD.md`. The previous PRD source-state warning is retired for ADQ-09.

## Dependency Closure Note

ADQ-09 satisfies the DEL-05-04 replay/transcript dependency rows for canonical session layout, event schema/writer availability, SDK linkage metadata, read-time redaction, and artifact-link projection. DEL-05-05 checksum/retention policy remains scoped to ADQ-10.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Execute ADQ-10 DEL-05-05 artifact checksum/retention residuals. | code/test | M | FIT | D-APP-42 Option A. |

## Issuance-Gate-Process Observations

DEL-05-04 now has a product-owned transcript projection and sidebar view over canonical event replay. Keep the distinction between ADQ-09 transcript replay closure and ADQ-10 artifact checksum/retention policy.

## D-APP-56 R5 P44 pointer annotation (2026-07-12)

The REQ004 and REQ007 evidence citations above preserve the paths inspected at assessment time. D-APP-48 subsequently relocated `types.ts` and `transcript-replay.ts` to `frontend/packages/harness-contract/src/`; the current paths are `frontend/packages/harness-contract/src/types.ts` and `frontend/packages/harness-contract/src/transcript-replay.ts`. The PASS conclusions are unchanged; this is an evidence-pointer annotation only.
