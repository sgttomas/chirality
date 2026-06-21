# Assessment INSP-03: DEL-03-02 Thin TurnEngine and Session Locking

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-03-02 |
| Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `0e1ba9a1eef03f1b9e2daa33d3d6c0c5b0f42f7c` |
| Spec source | `Specification.md` lines 5-84 |

## Scope

DEL-03-02 moves harness turn lifecycle, session binding, boot metadata forwarding, and active-turn locking behind a testable `TurnEngine` while keeping `/api/harness/turn` thin.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-03-02-REQ-001 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 167-186; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 160-205. Focused validation passed. | `TurnEngine.runTurn()` is unit-tested without invoking the HTTP route. |
| DEL-03-02-REQ-002 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 43-54 and 321-328; `frontend/src/lib/harness/agent-engine-port.ts` lines 12-22; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 451-475. Focused validation passed. | Runtime execution is behind an adapter interface, but `TurnEngine` depends on `IAgentSdkManager` rather than the named `AgentEnginePort` / `RuntimeEngineContract` type. |
| DEL-03-02-REQ-003 | PASS | `frontend/src/app/api/harness/turn/route.ts` lines 9-45; `frontend/src/lib/harness/turn-engine.ts` lines 186-305; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547 and 731-756. Focused validation passed. | The route parses, delegates, formats SSE, and returns pre-stream JSON errors through the shared error response path. |
| DEL-03-02-REQ-004 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 206-223; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 207-231; `frontend/src/__tests__/api/harness/routes.test.ts` lines 992-1007. Focused validation passed. | Same-session overlap returns `TURN_IN_PROGRESS` and later accepts a recovery turn. |
| DEL-03-02-REQ-005 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 215-223, 291-303, and 374-376; `frontend/src/app/api/harness/turn/route.ts` lines 16-32; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1009-1036. Focused validation passed. | Lock cleanup is covered for completion, cancellation/interrupt recovery, and errors, but durable client-disconnect cancellation evidence remains owned with DEL-03-04/PKG-05. |
| DEL-03-02-REQ-006 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 225-290; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 161-205. Focused validation passed. | Session, project root, persona/mode, runtime options, attachments, content blocks, and adapter input are bound before streaming. |
| DEL-03-02-REQ-007 | PASS | `frontend/src/lib/harness/types.ts` lines 187-252; `frontend/src/app/api/harness/turn/route.ts` lines 19-20 and 35-41; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547. Focused validation passed. | Existing SSE names and media type are preserved; newer `harness:event` is additive. |
| DEL-03-02-REQ-008 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-218; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 154-171; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 259-268. Focused validation passed. | `turn.accepted` is persisted before SDK query execution in the SDK manager, but the ownership is not centralized in `TurnEngine` itself. |
| DEL-03-02-REQ-009 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 279-288, 342-367; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 897-956; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 371-449. Focused validation passed. | SDK/Anthropic paths persist terminal events, but the deterministic stub path emits UI terminal events without persisted `HarnessEvent` records. |
| DEL-03-02-REQ-010 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-59; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 5-34; `frontend/src/__tests__/lib/session-events.test.ts` lines 19-42 and 77-197. Focused validation passed. | Browser `UIEvent` and persisted `HarnessEvent` are distinct, provider-neutral contracts. |
| DEL-03-02-REQ-011 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 329-341; `frontend/src/lib/harness/types.ts` lines 23-42; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 197-204. Focused validation passed. | Active session metadata is saved/readable, but canonical session-folder migration and broader legacy session readability remain PKG-05 scope. |
| DEL-03-02-REQ-012 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 149-165 and 262-274; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 233-253; `frontend/src/__tests__/api/harness/routes.test.ts` lines 615-729. Focused validation passed. | Unknown tools fail before adapter streaming and subagent delegation remains gate-controlled; this slice did not expose new write/bash/domain capability. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| `TurnEngine` depends on `IAgentSdkManager`, not the named `AgentEnginePort` contract. | Medium | `frontend/src/lib/harness/turn-engine.ts` lines 43-54; `frontend/src/lib/harness/agent-engine-port.ts` lines 12-22. | Reconcile type ownership in PKG-03 docs or refactor behind the named port in a future code tranche. |
| Accepted-turn and terminal persistence are adapter-owned rather than clearly TurnEngine-owned. | Medium | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-218 and 342-367; `frontend/src/lib/harness/turn-engine.ts` lines 321-376. | Decide whether this is acceptable adapter responsibility or should move into `TurnEngine`. |
| Client-disconnect durable cancellation remains weaker than lock-release evidence. | Medium | `frontend/src/app/api/harness/turn/route.ts` lines 30-32; `Specification.md` lines 61-62. | Add explicit disconnect/cancel persistence tests with DEL-03-04/PKG-05. |
| Legacy session readability and canonical folder migration remain out of scope here. | Low | `Specification.md` lines 20 and 39; `frontend/src/lib/harness/types.ts` lines 23-42. | Carry this into PKG-05 assessment and roadmap synthesis. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for the AgentEnginePort interface, PKG-05 event persistence, DEL-03-03 SSE compatibility, DEL-03-04 interrupt/cancel coordination, and DEL-09-03 test expansion.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile `TurnEngine` adapter interface naming/ownership with `AgentEnginePort`. | reconcile | S | FIT | Complete DEL-03-01 assessment follow-up. |
| Decide whether accepted-turn and terminal persistence belong centrally in `TurnEngine` or remain adapter-owned with conformance requirements. | architecture | M | FIT | PKG-05 event assessment. |
| Add a targeted disconnect/cancel persistence test once event-store ownership is settled. | test | M | FIT | DEL-03-04 taxonomy and PKG-05 event-store decisions. |

## Issuance-Gate-Process Observations

DEL-03-02 is implementation-substantial but not issuance-ready until adapter-interface wording, event-persistence ownership, and disconnect/cancel durability are either closed or explicitly accepted as cross-deliverable responsibilities.
