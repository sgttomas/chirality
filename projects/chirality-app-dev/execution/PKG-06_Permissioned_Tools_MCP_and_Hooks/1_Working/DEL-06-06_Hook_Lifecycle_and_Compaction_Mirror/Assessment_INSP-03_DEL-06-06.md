# Assessment INSP-03: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-06 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-74 |

## Scope

DEL-06-06 covers provider-neutral hook lifecycle events, fail-closed hook behavior, compaction boundary mirroring, replay after compaction, terminal/finalization evidence, redaction, and validation fixtures for hook and compaction event handling.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-06-REQ001 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 281-305; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 963-1012. | Hook mapper emits Chirality-owned `hook.*` event types rather than SDK names as public types. |
| DEL-06-06-REQ002 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 50-78; `frontend/src/lib/harness/chirality-hooks.ts` lines 291-304. | Hook lifecycle records conform to the generic `HarnessEvent` shape. |
| DEL-06-06-REQ003 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. | Hook and compaction events append to canonical per-session JSONL with unique event IDs. |
| DEL-06-06-REQ004 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 359-421 and 480-595; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 101-165 and 321-449. | Controlled hooks emit started/completed/failed lifecycle evidence where the adapter invokes the hook callbacks. |
| DEL-06-06-REQ005 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 462-477; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-259 and 370-449. | Hook policy failures block governed write/shell/subagent execution. |
| DEL-06-06-REQ006 | PARTIAL | `frontend/src/lib/harness/chirality-hooks.ts` lines 598-617; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 963-1012. | `PreToolUse`, `PostToolUse`, and `PostToolUseFailure` are wired. PreCompact and Stop/finalization are represented through mapper/status paths, not through a dedicated hook callback registration. |
| DEL-06-06-REQ007 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 1023-1037; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 123-153 and 591-637. | `context.compacted` is mirrored from adapter compact-boundary/status messages; dedicated PreCompact hook lifecycle persistence is not implemented. |
| DEL-06-06-REQ008 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 1023-1037. | Compacted events include replay implication metadata when knowable. |
| DEL-06-06-REQ009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. | Event replay is JSONL-based and does not rely on SDK transcript as canonical state. |
| DEL-06-06-REQ010 | PARTIAL | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 800-835 and 1014-1050; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 580-637. | Terminal/failed turn and compaction status events are mapped, but Stop/finalization hook semantics are not separately captured as a dedicated lifecycle fixture. |
| DEL-06-06-REQ011 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 507-548; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-75; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-368. | Large/sensitive hook/tool payloads are redacted and persisted as artifacts instead of raw event payloads. |
| DEL-06-06-REQ012 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-46; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 963-1012. | Public event types are provider-neutral; SDK-specific names live in event data as adapter metadata. |
| DEL-06-06-REQ013 | PASS | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 123-153 and 580-637; `frontend/src/__tests__/lib/session-events.test.ts` lines 20-42. | Tests cover `context.compacted`, `context.compaction.started`, hook started/failed, and event-type representability. |
| DEL-06-06-REQ014 | PASS | `_REFERENCES.md` REF-006 hash mismatch; this assessment's Source-State Caveat. | PRD-only compaction/hook behavior is warning-qualified until source-state closure. |
| DEL-06-06-REQ015 | PARTIAL | `frontend/src/lib/harness/chirality-hooks.ts` lines 331-617; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 963-1050; `frontend/scripts/validate-harness-section9.mjs` lines 84-90. | Mapper paths, schema tests, replay/redaction checks, and Section 9 IDs are identifiable; terminal fixtures and dedicated PreCompact/Stop hook callback paths remain incomplete. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| PreCompact hook lifecycle is represented through adapter messages, not a dedicated hook callback registration. | Medium | `frontend/src/lib/harness/chirality-hooks.ts` lines 598-617; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893. | Add a dedicated PreCompact/compaction hook path if the SDK exposes it, or record the adapter-message mirror as the accepted implementation. |
| Stop/finalization hook semantics are not separately fixture-tested. | Medium | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 800-835 and 1014-1050. | Add terminal hook/status fixtures or explicitly keep terminal outcome ownership with DEL-03-04/DEL-05-02. |
| REF-006 remains warning-limited for PRD-only hook and compaction behavior. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive the PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for DEL-05-02 event JSONL, DEL-06-04 governed hooks, DEL-03-04 terminal outcome handling, DEL-09-02 release evidence, and REF-006 source-state closure.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Decide whether adapter-message compaction mirror is sufficient or implement a dedicated PreCompact hook path. | architecture/code | S | FIT | SDK hook availability confirmed. |
| Add Stop/finalization fixtures that connect terminal adapter status to Chirality terminal events. | test | S | FIT | DEL-03-04 terminal taxonomy accepted. |
| Close REF-006 before issuance. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-06-06 has usable hook lifecycle and compaction mirror evidence, but it is not complete for dedicated PreCompact and Stop/finalization semantics. Issuance should require either implementation or an explicit acceptance of the adapter-message mirror boundary.
