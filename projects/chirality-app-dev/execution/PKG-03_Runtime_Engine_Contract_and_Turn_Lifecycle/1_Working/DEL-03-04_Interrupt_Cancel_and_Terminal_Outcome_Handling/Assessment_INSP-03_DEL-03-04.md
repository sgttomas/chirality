# Assessment INSP-03: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-03-04 |
| Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `0e1ba9a1eef03f1b9e2daa33d3d6c0c5b0f42f7c` |
| Spec source | `Specification.md` lines 5-78 |

## Scope

DEL-03-04 covers public interrupt handling, client disconnect cleanup, runtime failure, cancellation, active-turn lock release, and durable terminal outcome behavior for accepted turns.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-03-04-REQ-001 | PASS | `frontend/src/app/api/harness/interrupt/route.ts` lines 11-25; `frontend/src/lib/harness/client.ts` lines 238-248; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1039-1088. Focused validation passed. | `/api/harness/interrupt` remains the public endpoint. |
| DEL-03-04-REQ-002 | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 87-108; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 696-716; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 410-449. Focused validation passed. | Active SDK/Anthropic turns are interrupted/aborted through adapter state. |
| DEL-03-04-REQ-003 | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 279-288 and 342-352; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 863-874 and 918-930; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1039-1088. Focused validation passed. | Active interrupts produce terminal `process:exit` with `interrupted: true`. |
| DEL-03-04-REQ-004 | PARTIAL | `frontend/src/app/api/harness/turn/route.ts` lines 30-32; `frontend/src/lib/harness/turn-engine.ts` lines 291-303 and 374-376; `frontend/src/__tests__/api/harness/routes.test.ts` lines 992-1036. Focused validation passed. | Disconnect/cancel cleanup can release locks, but explicit durable cancellation on client disconnect remains incomplete. |
| DEL-03-04-REQ-005 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-218 and 356-367; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 249-267; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 371-408. Focused validation passed. | Failure after acceptance persists `turn.failed`, but accepted raw user input is not fully recoverable from the terminal event evidence alone. |
| DEL-03-04-REQ-006 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 279-288, 334-352, and 356-367; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` lines 897-956; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 371-449. Focused validation passed. | SDK/Anthropic paths have durable terminal outcomes; the stub path has UI terminal events but not persisted `HarnessEvent` terminal records. |
| DEL-03-04-REQ-007 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 750-836; `frontend/src/lib/harness/event-schema.ts` lines 3-59; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 66-110. Focused validation passed. | Terminal outcomes map into Chirality UI/Harness terms rather than SDK public semantics. |
| DEL-03-04-REQ-008 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 50-78; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | `HarnessEvent` schema contains required version, id, session, optional turn/parent, timestamp, type, and data fields. |
| DEL-03-04-REQ-009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-21 and 50-85; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. Focused validation passed. | Events append as redacted JSONL and replay tolerates malformed trailing lines. |
| DEL-03-04-REQ-010 | PASS | `frontend/src/lib/harness/types.ts` lines 187-252; `frontend/src/__tests__/api/harness/routes.test.ts` lines 520-547, 731-756, and 1039-1088. Focused validation passed. | Browser event names remain compatible; `harness:event` is an additive provider-neutral bridge. |
| DEL-03-04-REQ-011 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 206-223 and 374-376; `frontend/src/__tests__/api/harness/routes.test.ts` lines 992-1036; `frontend/src/__tests__/lib/turn-engine.test.ts` lines 207-231. Focused validation passed. | Interrupt/cancel paths release active-turn state sufficiently for subsequent turns. |
| DEL-03-04-REQ-012 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-21; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 15-33; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 356-367; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. Focused validation passed. | Runtime events and bridged events use redaction helpers and tests cover configured key redaction. |
| DEL-03-04-REQ-013 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 750-836; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 371-449; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 66-110. Focused validation passed. | Provider terminal result/failure paths map to Chirality-owned UI/Harness outputs. |
| DEL-03-04-REQ-014 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 206-223 and 307-309; `frontend/src/__tests__/api/harness/routes.test.ts` lines 980-1088; `Guidance.md` lines 85-89. Focused validation passed. | Observable recovery proves lock release, but exact cleanup hook/state API and terminal taxonomy remain `TBD`. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Interruption taxonomy is still unresolved. | High | `Guidance.md` lines 36, 45-50, and 85-89; `Dependencies.csv` line 11. | Prepare a human-ruling packet or resolve in INSP-04/05 whether interruption remains `turn.cancelled` with metadata or gains a new terminal event type. |
| Client-disconnect durable cancellation is not fully proved. | Medium | `frontend/src/app/api/harness/turn/route.ts` lines 30-32; `Specification.md` lines 31 and 58. | Add a disconnect/cancel terminal persistence test once event ownership is settled. |
| Accepted raw user input recovery is weaker than accepted-turn metadata recovery. | Medium | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-218; `rg` found no `message.accepted` writer beyond schema availability. | Decide whether raw/summary input belongs in `HarnessEvent`, session records, or another redacted artifact. |
| Stub terminal outcomes are UI-visible but not persisted as `HarnessEvent`s. | Low | `frontend/src/lib/harness/agent-sdk-manager.ts` lines 57-188. | Either add stub event persistence for parity or document stub as deterministic UI-only test adapter. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active rows remain for DEL-03-01/DEL-03-02 prerequisites, PKG-05 append-only JSONL ownership, and DEL-03-04-CONFLICT-001 terminal taxonomy.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Resolve DEL-03-04-CONFLICT-001 interruption taxonomy. | governance/reconcile | M | FIT | INSP-04 gate-process and roadmap synthesis. |
| Add explicit client-disconnect cancellation persistence coverage. | test | M | FIT | Event ownership decision with PKG-05. |
| Decide and document accepted-input recovery semantics for failed/interrupted turns. | architecture/doc | M | FIT | PKG-05 session-event assessment. |

## Issuance-Gate-Process Observations

DEL-03-04 has strong interrupt and terminal SSE evidence, but the gate should not treat interruption taxonomy, client-disconnect cancellation persistence, or accepted-input recovery as closed until a human ruling or a focused runtime-event tranche resolves them.
