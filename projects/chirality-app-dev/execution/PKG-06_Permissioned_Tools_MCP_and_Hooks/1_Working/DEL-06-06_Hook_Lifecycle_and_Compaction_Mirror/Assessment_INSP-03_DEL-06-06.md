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
| DEL-06-06-REQ006 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 598-617; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 963-1050; D-APP-43. | `PreToolUse`, `PostToolUse`, and `PostToolUseFailure` are wired; PreCompact and Stop/finalization are accepted through adapter message/status/result lifecycle mapping rather than synthetic SDK hook callbacks. |
| DEL-06-06-REQ007 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 1023-1037; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 718-792. | `context.compacted`, `context.compaction.started`, and `context.compaction.failed` are mirrored from adapter compact-boundary/status messages as the accepted PreCompact closure surface. |
| DEL-06-06-REQ008 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 1023-1037. | Compacted events include replay implication metadata when knowable. |
| DEL-06-06-REQ009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. | Event replay is JSONL-based and does not rely on SDK transcript as canonical state. |
| DEL-06-06-REQ010 | PASS | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 800-835 and 1014-1050; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 744-802; D-APP-40; D-APP-43. | Terminal success/failure result messages map to durable `turn.completed`/`turn.failed`, and explicit user interruption maps to `turn.interrupted`; no dedicated Stop hook callback is required. |
| DEL-06-06-REQ011 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 507-548; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-75; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-368. | Large/sensitive hook/tool payloads are redacted and persisted as artifacts instead of raw event payloads. |
| DEL-06-06-REQ012 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-46; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 963-1012. | Public event types are provider-neutral; SDK-specific names live in event data as adapter metadata. |
| DEL-06-06-REQ013 | PASS | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 123-153 and 580-637; `frontend/src/__tests__/lib/session-events.test.ts` lines 20-42. | Tests cover `context.compacted`, `context.compaction.started`, hook started/failed, and event-type representability. |
| DEL-06-06-REQ014 | PASS | `_REFERENCES.md` REF-006 `MATCH`; this assessment's Source-State Caveat. | PRD-only compaction/hook behavior is no longer warning-limited in active review records. |
| DEL-06-06-REQ015 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 331-617; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 881-893 and 963-1050; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 718-802; `frontend/scripts/validate-harness-section9.mjs` lines 84-90. | Mapper paths, schema tests, replay/redaction checks, Section 9 IDs, and terminal/compaction fixtures are identifiable; D-APP-43 removes the need for dedicated synthetic PreCompact/Stop callbacks. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| PreCompact lifecycle residual is closed through adapter-message/status mapping. | Low | D-APP-43; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 718-792. | Do not add synthetic SDK hook callbacks unless a later SDK/API surface requires a governed change. |
| Stop/finalization fixture residual is closed through terminal adapter result mapping. | Low | D-APP-43; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 744-802. | Preserve TurnEngine/session terminal event ownership and avoid duplicate terminal records. |
| Historical REF-006 warning text in older run records is retired for active review. | Low | `_REFERENCES.md` REF-006 is `MATCH` under the D-APP-38 authority corpus v2. | Keep the D-APP-38 reference status check in closeout validation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as
`MATCH` under the D-APP-38 authority corpus v2. Historical HASH_MISMATCH notes in `_run_records`
remain archival only.

## Dependency Closure Note

ADQ-11 satisfies the PreCompact/Stop mapping fixture and REF-006 source-state residuals for this
deliverable. Other active rows remain pending for DEL-05-02 event JSONL, DEL-06-04 governed hooks,
DEL-03-04 terminal outcome handling, and DEL-09-02 validation evidence unless separately closed by
their owning deliverables.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Preserve adapter-message compaction mirror as the accepted implementation unless the SDK exposes new governed hooks. | architecture/code | S | FIT | Future SDK lifecycle surface change. |
| Keep terminal adapter-result fixtures aligned with D-APP-40/D-APP-43 terminal taxonomy. | test | S | FIT | Future terminal result-shape change. |
| Keep D-APP-38 authority-corpus status clean during future authority-document edits. | governance | S | FIT | Authority-document edits occur. |

## Issuance-Gate-Process Observations

DEL-06-06 has usable hook lifecycle, compaction mirror, and terminal lifecycle evidence. D-APP-43
accepts adapter-message/status/result mapping for PreCompact and Stop/finalization closure and rejects
synthetic SDK hook callbacks for this slice. This does not advance lifecycle state or make an issuance
claim.
