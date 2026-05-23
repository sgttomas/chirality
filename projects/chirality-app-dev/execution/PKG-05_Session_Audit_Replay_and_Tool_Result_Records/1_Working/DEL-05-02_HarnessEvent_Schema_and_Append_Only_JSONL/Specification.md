# Specification: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Scope

This deliverable specifies the product-owned `HarnessEvent` schema and append-only JSONL persistence surface for Chirality runtime audit records.

In scope:

- Persist accepted user input as `turn.accepted` before SDK/model execution begins.
- Persist runtime events and terminal turn outcomes as ordered append-only JSONL.
- Define event schema fields, event category baseline, writer rules, replay tolerance, and tests for accepted-turn and terminal-event durability.
- Preserve the separation between compact browser `UIEvent`s and richer persisted `HarnessEvent`s.

Out of scope:

- Tool permission semantics, except where event records must support future permission/tool event categories.
- Redaction implementation details owned by DEL-05-03, except this deliverable must not permit secrets in event payloads.
- Runtime replay/transcript view implementation owned by DEL-05-04, except this deliverable must provide replay-safe JSONL semantics.
- Tool-result artifact budget/storage implementation owned by DEL-05-05, except this deliverable must reference artifacts for large payloads.
- SDK transcript placement and migration details owned by adjacent session-layout/linkage deliverables, except Chirality `events.jsonl` remains canonical.

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| DEL-05-02-RQ-001 | The event record type shall be named `HarnessEvent` and include `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| DEL-05-02-RQ-002 | `HarnessEvent` may include `turnId` and `parentEventId` when applicable. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| DEL-05-02-RQ-003 | The initial schema version shall be `1`. | `docs/SPEC.md` Section 9.1 |
| DEL-05-02-RQ-004 | Event IDs shall be unique per event. | `docs/SPEC.md` Section 9.2 |
| DEL-05-02-RQ-005 | Session event storage shall append newline-delimited JSON records in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 (HASH_MISMATCH source warning) |
| DEL-05-02-RQ-006 | `turn.accepted` shall be persisted before SDK/model execution starts. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2 |
| DEL-05-02-RQ-007 | Every accepted turn shall persist a durable terminal success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
| DEL-05-02-RQ-008 | Replay shall ignore malformed trailing JSONL lines, preserve valid prior records, and surface diagnostics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| DEL-05-02-RQ-009 | Event payloads shall not store secrets or API keys. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6, K-KEY-1 |
| DEL-05-02-RQ-010 | Large event payloads shall be stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2 |
| DEL-05-02-RQ-011 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts. | `docs/CONTRACT.md` K-EVENT-1 |
| DEL-05-02-RQ-012 | Core runtime APIs, events, tests, and records shall use Chirality terms; provider/SDK-specific terms may appear only as adapter metadata. | `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4 |
| DEL-05-02-RQ-013 | Event schema evolution shall be backward-compatible or explicitly versioned. | `docs/SPEC.md` Section 9.2 |
| DEL-05-02-RQ-014 | The canonical runtime audit mirror shall be `.chirality/sessions/<sessionId>/events.jsonl` or an explicitly configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Section 2.3; `docs/SPEC.md` Section 8.2, 8.4 |
| DEL-05-02-RQ-015 | Event schema fixtures shall keep later tool, hook, compaction, subagent, and SDK mirror event categories representable without asserting payload-specific semantics before their owning deliverables mature. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality `HarnessEvent` type target | Governs the event record shape and event category vocabulary | `docs/TYPES.md` Section 7.3 |
| SPEC Runtime Event Schema | Governs JSONL append rules, event IDs, replay tolerance, secret exclusion, large payload references, and versioning | `docs/SPEC.md` Section 9 |
| CONTRACT K-EVENT invariants | Binding constraints for UI/runtime separation, accepted-turn persistence, terminal durability, canonical audit mirror, malformed-tail replay, redaction, and tool-result payload handling | `docs/CONTRACT.md` K-EVENT-1 through K-EVENT-7 |
| Runtime Engine Contract | Requires runtime boundary to persist accepted turns and terminal outcomes while yielding UI events | `docs/SPEC.md` Section 10.1 |
| PRD runtime requirements | Product requirements FR-072 through FR-076 and related SDK mapping requirements; use with hash warning | `docs/PRD.md` Section 9 / FR table; `_REFERENCES.md` REF-006 HASH_MISMATCH |

## Verification

| Requirement | Verification Approach |
|---|---|
| DEL-05-02-RQ-001 through RQ-004 | Event schema unit tests and serialization fixtures verify required/optional fields, `schemaVersion: 1`, and unique `eventId` behavior. |
| DEL-05-02-RQ-005 | JSONL writer tests verify append-only newline-delimited writes and write-sequence ordering. |
| DEL-05-02-RQ-006 | Accepted-turn lifecycle test verifies `turn.accepted` is written before the SDK/model request begins. |
| DEL-05-02-RQ-007 | Terminal-event tests cover success, failure, cancellation, and interruption outcomes. |
| DEL-05-02-RQ-008 | Replay tests include a malformed trailing line fixture and confirm valid prior records survive with diagnostics. |
| DEL-05-02-RQ-009 | Redaction/secret-safety tests or fixtures verify API keys and configured secrets are absent from event payloads. ASSUMPTION: detailed redaction helper tests are owned by DEL-05-03; exact helper or fixture contract remains TBD until that deliverable is accepted. |
| DEL-05-02-RQ-010 | Large-payload tests verify artifact references instead of inline oversized payloads. ASSUMPTION: storage thresholds are finalized by DEL-05-05; numeric threshold source remains TBD until that deliverable is accepted. |
| DEL-05-02-RQ-011 through RQ-012 | Mapper/API contract tests verify browser `UIEvent`s remain compact and SDK/provider terms do not leak into canonical event fields except adapter metadata. |
| DEL-05-02-RQ-013 | Compatibility tests verify older event fixtures replay after additive schema evolution, or require explicit version handling for breaking changes. |
| DEL-05-02-RQ-014 | Session layout tests verify `.chirality/sessions/<sessionId>/events.jsonl` placement or configured Chirality-controlled override. |
| DEL-05-02-RQ-015 | Fixture coverage plan verifies later event category names can serialize and replay as versioned `HarnessEvent`s while category-specific payload schemas remain TBD until source or implementation acceptance. |

## Documentation

Required deliverable artifacts:

- `event-schema.ts` or equivalent `HarnessEvent` type definition.
- `session-events.ts` or equivalent append/replay JSONL API.
- Serialization fixtures covering initial event categories.
- Accepted-turn persistence test.
- Terminal-event persistence test.
- Malformed-tail replay test.
- UI/runtime separation test.
- Later-category fixture coverage plan for tool, hook, compaction, subagent, and SDK mirror event names, with payload-specific fixtures marked TBD until owning deliverables mature.
- Redaction helper or fixture contract reference from DEL-05-03, currently TBD.
- Source notes documenting the `docs/PRD.md` HASH_MISMATCH warning if PRD text is used to justify implementation behavior not also present in matching sources.
