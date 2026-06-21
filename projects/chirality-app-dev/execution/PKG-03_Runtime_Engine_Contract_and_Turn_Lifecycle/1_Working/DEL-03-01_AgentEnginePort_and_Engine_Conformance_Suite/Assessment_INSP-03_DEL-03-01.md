# Assessment INSP-03: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-03-01 |
| Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `0e1ba9a1eef03f1b9e2daa33d3d6c0c5b0f42f7c` |
| Spec source | `Specification.md` lines 5-92 |

## Scope

DEL-03-01 defines the product-owned runtime boundary and conformance suite for harness turn execution before adapter behavior is treated as a production-default path.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-03-01-REQ-001 | PASS | `frontend/src/lib/harness/agent-engine-port.ts` lines 12-22; `frontend/docs/harness/runtime_engine_contract.md` lines 18-30; `frontend/src/__tests__/lib/agent-engine-port.test.ts` lines 5-17. Focused validation passed. | `AgentEnginePort` / `RuntimeEngineContract` exist as Chirality-owned types. |
| DEL-03-01-REQ-002 | PASS | `frontend/src/lib/harness/agent-engine-port.ts` lines 24-33; `frontend/src/lib/harness/types.ts` lines 187-252; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 451-475. Focused validation passed. | Public event names are provider-neutral and conformance rejects provider-shaped public event names. |
| DEL-03-01-REQ-003 | PASS | `Specification.md`; `frontend/src/lib/harness/agent-engine-port.ts`; `frontend/docs/harness/runtime_engine_contract.md`; D-APP-40. | `AgentEnginePort.startTurn(input)` is the canonical adapter stream method; `TurnEngine.runTurn(request)` remains the route-independent lifecycle method. |
| DEL-03-01-REQ-004 | PASS | `frontend/src/lib/harness/agent-engine-port.ts` line 15; `frontend/src/lib/harness/engine-conformance.ts` lines 175-211; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 410-449. Focused validation passed. | Interrupt is part of the port and the conformance helper verifies interrupted `process:exit` evidence. |
| DEL-03-01-REQ-005 | PARTIAL | `frontend/src/lib/harness/agent-engine-port.ts` lines 5-10; `frontend/src/lib/harness/types.ts` lines 23-42 and 148-156; `frontend/src/lib/harness/turn-engine.ts` lines 225-290. Focused validation passed. | Required input concepts are present across `SessionRecord`, `ResolvedOpts`, content blocks, and `TurnEngine`, but the port input does not explicitly carry every named field or a cancellation signal. |
| DEL-03-01-REQ-006 | PASS | `frontend/docs/harness/runtime_engine_contract.md` lines 32-155; `frontend/src/lib/harness/event-schema.ts` lines 3-59; `frontend/src/lib/harness/session-events.ts` lines 14-21; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 223-449. Focused validation passed. | Contract docs and tests cover UI events, persisted events, tool evidence, permission evidence, terminal outcomes, and interrupt paths. |
| DEL-03-01-REQ-007 | PASS | `frontend/src/lib/harness/types.ts` lines 30-39; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 633-660; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 23-64. Focused validation passed. | SDK IDs and versions are retained as metadata instead of public event names. |
| DEL-03-01-REQ-008 | PARTIAL | `frontend/src/lib/harness/runtime.ts` lines 65-72; `frontend/src/__tests__/lib/harness-runtime.test.ts` lines 57-87; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 223-269. Focused validation passed. | Key-aware `agentSdk` default has landed, but this deliverable's own evidence record still lists live/packaged SDK conformance as `BLOCKED_TBD` and should be refreshed against D-APP-17/D-APP-18 evidence before issuance. |
| DEL-03-01-REQ-009 | PASS | `frontend/src/lib/harness/agent-sdk-manager.ts` lines 29-188; `frontend/src/lib/harness/runtime.ts` lines 74-89; `frontend/src/__tests__/lib/harness-runtime.test.ts` lines 33-39 and 79-86. Focused validation passed. | Deterministic stub manager remains available and selectable. |
| DEL-03-01-REQ-010 | PARTIAL | `frontend/src/lib/harness/engine-conformance.ts` lines 60-172; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 223-502; `Evidence_CODEV-001_Runtime_Engine_Conformance.md` lines 23-36. Focused validation passed. | Current tests cover many conformance cases, but Section 9 linkage and older evidence-record `BLOCKED_TBD` rows remain unresolved. |
| DEL-03-01-REQ-011 | PASS | `frontend/src/lib/harness/agent-engine-port.ts` lines 24-33; `frontend/src/__tests__/lib/agent-engine-port.test.ts` lines 5-17; `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` lines 100-119; D-APP-40. Focused validation passed. | Existing compact names are preserved and `harness:event` is the additive redacted bridge for rich `HarnessEvent` records. |
| DEL-03-01-REQ-012 | PASS | `frontend/src/app/api/harness/turn/route.ts` lines 9-45; `frontend/src/lib/harness/turn-engine.ts` lines 167-378; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 160-253. Focused validation passed. | The route delegates to `TurnEngine`; lifecycle policy sits behind the transport adapter. |
| DEL-03-01-REQ-013 | PASS | `frontend/src/lib/harness/engine-conformance.ts` lines 76-145; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 451-502. Focused validation passed. | Conformance rejects unknown/provider-shaped public UI event names and missing terminal evidence. |
| DEL-03-01-REQ-014 | PARTIAL | `docs/CONTRACT.md` lines 95-96; `frontend/docs/harness/runtime_engine_contract.md` lines 1-16 and 157-190; `Dependencies.csv` line 8. | Fallback doctrine exists at contract level, but the runtime contract doc does not yet provide a crisp fallback-criteria section or reliance-boundary cross-link. |
| DEL-03-01-REQ-015 | PASS | `_REFERENCES.md` line 12; D-APP-38. | REF-006 is governed by the current authority corpus and records `MATCH`; future authority-doc edits require corpus bump/apply. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Evidence record is stale relative to later live/default-provider work. | Medium | `Evidence_CODEV-001_Runtime_Engine_Conformance.md` lines 34-36; D-APP-17/D-APP-18 are later accepted history. | Add a refreshed evidence note or superseding evidence record before issuance. |
| Section 9 runtime validation linkage remains unavailable. | Medium | `Specification.md` lines 73 and 88; `Dependencies.csv` line 9. | Close through DEL-09-02 / DEL-09-03 validation work, not inside this inspection wave. |

## Source-State Caveat

D-APP-38 established the authority-corpus reference model. Current `_REFERENCES.md` records REF-006 as `MATCH`; future authority-document edits require a corpus bump/apply before acceptance. No semantic files were used or produced.

## Dependency Closure Note

This ADQ-05 supersession does not claim lifecycle issuance. Active pending rows remain for DEL-04-01 SDK fixture detail, DEL-03-03 route/SSE interface evidence, DEL-01-02 reliance-boundary cross-link, and DEL-09-02 Section 9 linkage.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a superseding conformance evidence note that incorporates D-APP-17/D-APP-18 and current scripted conformance results. | evidence | M | FIT | Focused conformance tests remain green. |

## Issuance-Gate-Process Observations

DEL-03-01 has strong implementation and test evidence, but issuance should not rely on the stale CODEV-001 evidence record alone. ADQ-05 resolves method naming, `harness:event`, and REF-006 posture; the gate should still require current fallback-criteria and Section 9 linkage disposition.
