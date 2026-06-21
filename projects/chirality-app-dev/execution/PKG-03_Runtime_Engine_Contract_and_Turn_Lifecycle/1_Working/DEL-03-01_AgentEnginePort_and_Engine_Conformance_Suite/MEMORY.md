# MEMORY - DEL-03-01

## Decisions And Evidence

- 2026-06-21 - ADQ-05 applied D-APP-40 Option B to DEL-03-01: `AgentEnginePort.startTurn(input)` is the canonical adapter method; `TurnEngine.runTurn(request)` remains the route-independent product lifecycle method; `harness:event` is the public redacted bridge for rich `HarnessEvent` records. Evidence: `../Evidence_ADQ-05_G5_Runtime_Taxonomy.md`. No lifecycle issuance, provider expansion, release posture, professional approval, certification, sealing, authentication, or code-compliance claim changed.
- 2026-06-21 - ADQ-04 refreshed runtime evidence in `docs/harness/runtime_evidence_reconciliation.md` and `frontend/docs/harness/runtime_engine_contract.md`: D-APP-18 key-aware default supersedes the D-APP-12 hold wording, `harness:event` is part of the current public UIEvent list, current Section 9 IDs use `section9.adapter_*`, and D-APP-38 corpus `v1` supersedes the old REF-006 hash-mismatch caveat. No lifecycle state, dependency row, provider expansion, release posture, or professional/code-compliance claim changed.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-05-24 - CODEV-001 tranche implemented the initial product-owned runtime boundary in `frontend/src/lib/harness/agent-engine-port.ts`.
- 2026-05-24 - Stable browser `UIEvent` names remain unchanged and provider-neutral.
- 2026-05-24 - Runtime evidence JSONL support added through `frontend/src/lib/harness/event-schema.ts` and `frontend/src/lib/harness/session-events.ts`.
- 2026-05-24 - Runtime contract documentation added at `frontend/docs/harness/runtime_engine_contract.md`.
- 2026-05-24 - Conformance evidence recorded in `Evidence_CODEV-001_Runtime_Engine_Conformance.md`.
- 2026-05-24 - Dependency closure assessment left `DEP-03-01-003` unchanged because exact SDK-backed fixture details still require live SDK probe evidence.

## Open Items

- SDK-backed live query conformance now has D-APP-17 packaged read-tool proof history, D-APP-18 key-aware default approval, and D-APP-40 method/event taxonomy closure; broader route/SSE fixture capture and durable lifecycle evidence remain residuals.
- Broader packaged workflow evidence remains outside this deliverable and is queued separately.
- Section 9 validation linkage is now indexed through `frontend/scripts/validate-harness-section9.mjs`; deliverable closure remains separate from this evidence refresh.
- Historical REF-006 hash mismatch is superseded by D-APP-38 authority corpus `v1`; no closure claim is made by ADQ-04.
- Strict all-active FULL_GRAPH closure remains open outside this deliverable.

## Dependency Note

No DEL-03-01 `Dependencies.csv` rows were marked satisfied, waived, retired, or not applicable during the CODEV-001 closure assessment.
