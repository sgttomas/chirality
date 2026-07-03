# Evidence - CODEV-001 Runtime Engine Conformance

Date: 2026-05-24

## ADQ-04 Superseding Note - 2026-06-21

This CODEV-001 record remains historical evidence for the first runtime-boundary tranche.
It is superseded for current default-provider, Section 9 validation, `harness:event`, and
REF-006 source-state posture by `docs/harness/runtime_evidence_reconciliation.md` and the
refreshed `frontend/docs/harness/runtime_engine_contract.md`.

Current posture:

- D-APP-18 Option A made the Claude Agent SDK / Anthropic first adapter the key-aware
  default: `agentSdk` when an Anthropic key is configured, otherwise `stub`.
- `PUBLIC_UI_EVENT_NAMES` now includes `harness:event` as a provider-neutral redacted
  `HarnessEvent` passthrough, not an SDK/provider event namespace.
- Section 9 runtime validation uses the current deterministic IDs
  `section9.runtime_engine_contract`, `section9.adapter_turn_engine_event_log`, and
  `section9.adapter_message_mapper`.
- D-APP-38 authority corpus `v1` resolves the earlier REF-006 hash-mismatch caveat for
  this evidence refresh; no authority document is edited by ADQ-04.

This note does not satisfy dependency rows, advance lifecycle state, authorize provider
expansion, or make release, professional, certification, sealing, authentication, or
code-compliance claims.

## D-APP-46 Package-Extraction Forward Note - 2026-07-03

The source-path rows below remain historical evidence for the first CODEV-001
implementation tranche. D-APP-46 later extracted the dependency-free contract spine into
`@chirality/harness-contract`, with back-compat re-exports preserved under
`frontend/src/lib/harness/`.

Package-owned homes for extracted CODEV-001 surfaces:

| Historical surface | Current package-owned source | Back-compat shim |
|---|---|---|
| Product-owned runtime boundary | `frontend/packages/harness-contract/src/agent-engine-port.ts` | `frontend/src/lib/harness/agent-engine-port.ts` |
| Stable browser event names | `frontend/packages/harness-contract/src/agent-engine-port.ts` | `frontend/src/lib/harness/agent-engine-port.ts` |
| Versioned persisted runtime event schema | `frontend/packages/harness-contract/src/event-schema.ts` | `frontend/src/lib/harness/event-schema.ts` |
| SDK message / UI event shared types | `frontend/packages/harness-contract/src/types.ts` | `frontend/src/lib/harness/types.ts` |
| Engine conformance helpers | `frontend/packages/harness-contract/src/engine-conformance.ts` | `frontend/src/lib/harness/engine-conformance.ts` |

Current package-consumption readiness is recorded in
`Evidence_CODEV-002_Harness_Contract_Package_Consumption_Readiness.md`. This forward note
does not claim package publishability, piping consumption, F2/F3/F4 crossing, dependency
satisfaction, or lifecycle advancement.

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

Historical note: this section recorded the 2026-05-24 REF-006 `HASH_MISMATCH` state.
D-APP-38 later established authority corpus `v1`, and current reconciliation status reports
REF-006 as `MATCH`. This historical caveat no longer describes current ADQ-04 evidence
posture, but it is retained to preserve the original run record.

## Dependency Closure Note

This record does not mark any `Dependencies.csv` row satisfied, waived, retired, or not
applicable. Follow-up dependency closure remains required after tranche evidence review.
