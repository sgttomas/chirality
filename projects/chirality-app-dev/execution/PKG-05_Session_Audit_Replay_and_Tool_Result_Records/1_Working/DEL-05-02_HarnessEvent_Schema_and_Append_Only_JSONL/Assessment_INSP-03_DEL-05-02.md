# Assessment INSP-03: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-02 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `18511e933233b90ff2a84dd41f5b40041719c300` |
| Spec source | `Specification.md` lines 5-66 |

## Scope

DEL-05-02 covers the provider-neutral `HarnessEvent` schema, append-only per-session JSONL persistence, accepted-turn and terminal-outcome durability, malformed-line tolerance, event/tool payload hygiene, versioning, and future event-category representability.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-02-RQ001 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 50-59; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | Core fields include schema version, event ID, session ID, timestamp, type, and data. |
| DEL-05-02-RQ002 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 50-59. Focused validation passed. | Optional `turnId` and `parentEventId` are supported. |
| DEL-05-02-RQ003 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 61-78; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | `schemaVersion` is fixed to `1` for new events. |
| DEL-05-02-RQ004 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 61-78. Focused validation passed. | Event IDs are created per event with `randomUUID`. |
| DEL-05-02-RQ005 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | Events append one JSON object per newline in write order. |
| DEL-05-02-RQ006 | PASS | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 203-230; `frontend/src/__tests__/lib/engine-conformance.test.ts` lines 261-267. Focused validation passed. | `turn.accepted` is persisted before adapter/model lifecycle output. |
| DEL-05-02-RQ007 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 279-363; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` lines 194-291 and 322-561. Focused validation passed. | Completed, failed, and cancelled outcomes are represented, but terminal taxonomy/client-disconnect ownership remains shared with PKG-03/PKG-04. |
| DEL-05-02-RQ008 | PASS | `frontend/src/lib/harness/session-events.ts` lines 50-85; `frontend/src/__tests__/api/harness/routes.test.ts` lines 1247-1322. Focused validation passed. | Malformed lines are counted while valid lines before and after are preserved. The implementation tolerates any malformed line, not only a trailing tail. |
| DEL-05-02-RQ009 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/harness/run-logger.ts` lines 64-109; `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. Focused validation passed. | Appended events pass through recursive configured-key redaction. |
| DEL-05-02-RQ010 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98; `frontend/src/lib/harness/chirality-hooks.ts` lines 507-545. Focused validation passed. | Large tool results can be stored as artifacts and referenced from events, but schema-level large-payload enforcement is delegated to tool evidence/artifact code. |
| DEL-05-02-RQ011 | PASS | `frontend/src/lib/harness/harness-ui-bridge.ts` lines 1-34. Focused validation passed. | `HarnessEvent` remains distinct from public `UIEvent` and is bridged as provider-neutral `harness:event`. |
| DEL-05-02-RQ012 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-46; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 15-17. Focused validation passed. | Provider names and IDs live in event metadata, not event type taxonomy. |
| DEL-05-02-RQ013 | PARTIAL | `frontend/src/lib/harness/event-schema.ts` lines 50-78. | Schema versioning exists, but compatibility fixtures for older/future versions are not yet explicit. |
| DEL-05-02-RQ014 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/__tests__/lib/session-events.test.ts` lines 44-75. Focused validation passed. | Canonical event path is `.chirality/sessions/<sessionId>/events.jsonl`. |
| DEL-05-02-RQ015 | PASS | `frontend/src/lib/harness/event-schema.ts` lines 3-46; `frontend/src/__tests__/lib/session-events.test.ts` lines 20-42. Focused validation passed. | Later runtime categories, including tool, hook, permission, subagent, and compaction events, are representable. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Terminal outcome durability is implemented but still cross-owned with runtime cancellation taxonomy. | Medium | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 279-363; DEL-03-04 assessment residuals. | Keep DEL-05-02 focused on event persistence and close cancellation taxonomy with PKG-03/PKG-04/PKG-05 reconciliation. |
| Version-evolution fixtures are thin. | Low | `frontend/src/lib/harness/event-schema.ts` lines 50-78. | Add explicit fixture tests for unknown future `schemaVersion` handling once replay import policy is accepted. |
| Large-payload prevention is not embedded in the event schema itself. | Low | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98. | Treat result budgeting as ToolResultStore responsibility and cross-link to DEL-05-05. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active dependency posture remains: DEL-05-01 canonical folder interface, DEL-05-03 redaction breadth, DEL-05-05 artifact interface, DEL-04-03 mapper compatibility, and terminal outcome ownership remain cross-deliverable closure surfaces.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add schema-version compatibility fixtures for replay/import boundaries. | test | S | FIT | Current event schema held stable. |
| Cross-link accepted-turn and terminal-outcome event evidence into release Section 9 validation IDs. | evidence | S | FIT | Section 9 ID naming reconciled. |
| Keep payload-size enforcement in ToolResultStore and event producers rather than overloading the event-schema type. | architecture | S | FIT | DEL-05-05 thresholds accepted. |

## Issuance-Gate-Process Observations

DEL-05-02 has strong source and test coverage for the canonical event model. Issuance should focus on cross-deliverable terminal taxonomy, version fixtures, and source-state warning closure rather than redesigning the event vocabulary.

## D-APP-56 R5 P40 annotation (2026-07-12)

The source-state caveat above is preserved as historical assessment evidence. REF-006 now records `docs/PRD.md` expected and actual SHA-256 as `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` (`MATCH`) under D-APP-38; it is not a current warning or blocker. No assessment verdict or lifecycle state changes here.

## D-APP-56 R5 P44 pointer annotation (2026-07-12)

The event-schema citations above preserve the `frontend/src/lib/harness/event-schema.ts` path inspected at assessment time. D-APP-48 subsequently relocated that contract to `frontend/packages/harness-contract/src/event-schema.ts`. The assessment conclusions are unchanged; this is an evidence-pointer annotation only.
