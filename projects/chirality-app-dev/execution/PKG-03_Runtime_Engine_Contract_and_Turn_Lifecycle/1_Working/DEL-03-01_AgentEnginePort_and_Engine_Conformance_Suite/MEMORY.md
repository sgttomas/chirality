# MEMORY - DEL-03-01

## Decisions And Evidence

- 2026-05-24 - CODEV-001 tranche implemented the initial product-owned runtime boundary in `frontend/src/lib/harness/agent-engine-port.ts`.
- 2026-05-24 - Stable browser `UIEvent` names remain unchanged and provider-neutral.
- 2026-05-24 - Runtime evidence JSONL support added through `frontend/src/lib/harness/event-schema.ts` and `frontend/src/lib/harness/session-events.ts`.
- 2026-05-24 - Runtime contract documentation added at `frontend/docs/harness/runtime_engine_contract.md`.
- 2026-05-24 - Conformance evidence recorded in `Evidence_CODEV-001_Runtime_Engine_Conformance.md`.
- 2026-05-24 - Dependency closure assessment left `DEP-03-01-003` unchanged because exact SDK-backed fixture details still require live SDK probe evidence.

## Open Items

- SDK-backed live query conformance remains `BLOCKED_TBD` pending controlled API-key/subprocess probe.
- Electron packaged SDK subprocess evidence remains `BLOCKED_TBD`.
- Section 9 validation linkage remains `BLOCKED_TBD` until DEL-09-02 is available.
- REF-006 `docs/PRD.md` hash mismatch remains a closure caveat.
- Strict all-active FULL_GRAPH closure remains open outside this deliverable.

## Dependency Note

No DEL-03-01 `Dependencies.csv` rows were marked satisfied, waived, retired, or not applicable during the CODEV-001 closure assessment.
