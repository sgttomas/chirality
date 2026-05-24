# Evidence - CODEV-001 Runtime Engine Conformance

Date: 2026-05-24

## Scope

This evidence record covers the first CODEV-001 implementation tranche for DEL-03-01.
It records the product-owned runtime boundary and initial conformance evidence for the
stub and opt-in Claude Agent SDK probe adapter.

## Implemented Evidence

| Evidence Area | Artifact |
|---|---|
| Product-owned runtime boundary | `frontend/src/lib/harness/agent-engine-port.ts` |
| Stable browser event names | `frontend/src/lib/harness/agent-engine-port.ts`; `frontend/src/__tests__/lib/agent-engine-port.test.ts` |
| Versioned persisted runtime event schema | `frontend/src/lib/harness/event-schema.ts` |
| Append-only session event JSONL helper | `frontend/src/lib/harness/session-events.ts`; `frontend/src/__tests__/lib/session-events.test.ts` |
| SDK message to UI/Harness event mapping | `frontend/src/lib/harness/sdk-message-mapper.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` |
| Opt-in SDK probe adapter | `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` |
| Runtime contract documentation | `frontend/docs/harness/runtime_engine_contract.md` |

## Conformance Matrix

| Case | Subject | Status | Evidence |
|---|---|---|---|
| Stable SSE event names | Public browser stream | PASS | `agent-engine-port.test.ts` |
| Provider-neutral public event names | Public browser stream | PASS | `agent-engine-port.test.ts` |
| Stub provider remains default | Stub adapter | PASS | `harness-runtime.test.ts` |
| Existing direct Anthropic provider remains selectable | Direct adapter | PASS | `harness-runtime.test.ts` |
| SDK probe provider is non-default and explicit | Claude Agent SDK adapter | PASS | `harness-runtime.test.ts` |
| SDK message mapping preserves UI event names | Claude Agent SDK adapter | PASS | `sdk-message-mapper.test.ts` |
| SDK turn evidence appends HarnessEvent JSONL | Claude Agent SDK adapter | PASS | `claude-agent-sdk-manager.test.ts`; `session-events.test.ts` |
| SDK-backed live query behavior | Claude Agent SDK adapter | BLOCKED_TBD | Requires controlled live probe with API key and subprocess environment. |
| Electron packaged SDK subprocess | Claude Agent SDK adapter | BLOCKED_TBD | Packaging run not executed in this tranche. |
| Section 9 validation linkage | Runtime validation surface | BLOCKED_TBD | DEL-09-02 validation linkage remains unavailable. |

## Source-State Caveat

REF-006 `docs/PRD.md` remains `HASH_MISMATCH` in `_REFERENCES.md`. This evidence uses the
accessible PRD and corroborating SPEC/CONTRACT/TYPES material as implementation guidance, but
acceptance closure still requires source-state confirmation or a human ruling.

## Dependency Closure Note

This record does not mark any `Dependencies.csv` row satisfied, waived, retired, or not
applicable. Follow-up dependency closure remains required after tranche evidence review.
