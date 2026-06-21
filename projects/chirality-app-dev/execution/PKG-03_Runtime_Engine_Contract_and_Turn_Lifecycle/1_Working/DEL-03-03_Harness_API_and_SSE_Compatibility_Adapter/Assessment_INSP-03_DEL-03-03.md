# Assessment INSP-03: DEL-03-03 Harness API and SSE Compatibility Adapter

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-03-03 |
| Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `0e1ba9a1eef03f1b9e2daa33d3d6c0c5b0f42f7c` |
| Spec source | `Specification.md` lines 5-66 |

## Scope

DEL-03-03 defines the compatibility adapter contract for `/api/harness/*` routes and browser-facing SSE events while runtime policy moves behind `TurnEngine` and adapter boundaries.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-03-03-REQ-001 | PARTIAL | `frontend/src/app/api/harness/turn/route.ts` lines 9-45; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547, 731-780, and 980-1182. Focused validation passed. | Route behavior is covered by tests, but exact request/response fixture capture and baseline route-shape index are still missing. |
| DEL-03-03-REQ-002 | PASS | `frontend/src/app/api/harness/turn/route.ts` lines 9-45; `frontend/src/lib/harness/turn-engine.ts` lines 186-305 and 321-378; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547. Focused validation passed. | `/api/harness/turn` delegates lifecycle execution and encodes returned events as SSE. |
| DEL-03-03-REQ-003 | PASS | `frontend/src/lib/harness/types.ts` lines 187-252; `frontend/src/lib/harness/agent-engine-port.ts` lines 24-33; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547 and 731-756. Focused validation passed. | The original named events remain supported; `harness:event` is additive and provider-neutral. |
| DEL-03-03-REQ-004 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 346-376; `frontend/src/__tests__/api/harness/routes.test.ts` lines 731-756 and 1039-1088. Focused validation passed. | Normal/error/interrupt terminal stream behavior is covered; client-disconnect terminal persistence remains weaker than stream cleanup. |
| DEL-03-03-REQ-005 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-59; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 5-34; `frontend/src/components/shell/chat-panel.tsx` lines 313-326; `frontend/src/__tests__/lib/session-events.test.ts` lines 19-42. Focused validation passed. | UI events and persisted harness events remain separate; rich events bridge as `harness:event`. |
| DEL-03-03-REQ-006 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 624-870; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-110; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 451-475. Focused validation passed. | SDK messages map through a dedicated boundary and provider-shaped public event names are rejected. |
| DEL-03-03-REQ-007 | PASS | `frontend/src/lib/harness/harness-ui-bridge.ts` lines 5-34; `frontend/src/components/shell/chat-panel.tsx` lines 321-326; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 269-354. Focused validation passed. | Additional rich lifecycle/tool events use the documented `harness:event` path and are consumed separately from compact chat events. |
| DEL-03-03-REQ-008 | PARTIAL | `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547 and 980-1182; `frontend/src/__tests__/lib/harness-client.test.ts` lines 180-245. Focused validation passed. | Route and SSE tests exist, but required UI event contract docs, fixture README, and route adapter test index are not complete artifacts. |
| DEL-03-03-REQ-009 | PASS | `_REFERENCES.md` line 12; D-APP-38. | REF-006 is governed by the current authority corpus and records `MATCH`; future authority-doc edits require corpus bump/apply. |
| DEL-03-03-REQ-010 | PARTIAL | `_DEPENDENCIES.md` lines 44-55; `Specification.md` lines 33-35 and 60-66; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547 and 980-1182. Focused validation passed. | Tests cover key route behavior, but the required route-to-fixture index still has no accepted artifact. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Current route/SSE fixture capture remains explicit `TBD`. | Medium | `_DEPENDENCIES.md` lines 44-55; `Specification.md` lines 60-66. | Create a route adapter test index and fixture capture record before issuance. |
| Client-disconnect terminal persistence is not as strong as normal/error/interrupt stream evidence. | Medium | `frontend/src/app/api/harness/turn/route.ts` lines 30-32; `Specification.md` lines 29 and 55. | Add disconnect/cancel fixture coverage with DEL-03-04 and PKG-05. |
| UI event contract docs and SSE fixture README are not complete artifacts. | Low | `Specification.md` lines 60-66. | Add docs or explicitly defer them in a scoped evidence tranche. |

## Source-State Caveat

D-APP-38 established the authority-corpus reference model. Current `_REFERENCES.md` records REF-006 as `MATCH`; future authority-document edits require a corpus bump/apply before acceptance. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active rows remain for the runtime-engine document boundary, DEL-03-04 interrupt/cancel boundary, PKG-05 UIEvent/HarnessEvent separation, and current fixture capture.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a route adapter test index mapping each `/api/harness/*` route to current fixture coverage or explicit `TBD`. | doc/test | M | FIT | No provider expansion. |
| Add disconnect-path SSE/terminal cleanup coverage once terminal ownership is settled. | test | M | FIT | DEL-03-04/PKG-05 event ownership decision. |

## Issuance-Gate-Process Observations

DEL-03-03 demonstrates route/SSE compatibility through live unit tests, and ADQ-05 records `harness:event` as the additive compatibility bridge. The gate still needs artifact-level fixture capture before issue-readiness claims.
