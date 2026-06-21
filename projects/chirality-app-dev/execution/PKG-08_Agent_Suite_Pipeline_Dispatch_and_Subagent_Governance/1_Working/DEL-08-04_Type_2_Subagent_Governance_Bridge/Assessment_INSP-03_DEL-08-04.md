# Assessment INSP-03: DEL-08-04 Type 2 Subagent Governance Bridge

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-08-04 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `d92ef1253b37cd29423672acb146a9e9c91087d5` |
| Spec source | `Specification.md` lines 1-92 |

## Scope

DEL-08-04 covers the fail-closed Type 2 subagent governance gate, the allowlist and metadata requirements for executable delegation, and the SDK Agent bridge that must not expand child capabilities.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-04-001 | PASS | `frontend/src/lib/harness/turn-engine.ts` lines 262-274; `frontend/src/lib/harness/subagent-governance.ts` lines 172-272; `frontend/src/__tests__/api/harness/routes.test.ts` lines 575-729. | `TurnEngine` evaluates subagent governance before effective options carry delegated subagents into runtime execution. |
| REQ-08-04-002 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 187-245; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 83-209. | Environment, allowlist, metadata, context-sealed, pipeline-approved, and approval-ref gates all fail closed. |
| REQ-08-04-003 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 207-215; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 124-145. | Missing or invalid governance metadata denies delegation. |
| REQ-08-04-004 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 197-205; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 109-122. | Personas without a subagent allowlist deny delegation. |
| REQ-08-04-005 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 133-170; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 211-267. | Non-Type 2 candidates are rejected from delegated subagents. |
| REQ-08-04-006 | PASS | `frontend/src/lib/harness/subagent-bridge.ts` lines 64-98; `frontend/src/__tests__/lib/subagent-bridge.test.ts` lines 32-71; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 321-359. | SDK `agents` are created only from delegated Type 2 candidates and only when Agent is requested. |
| REQ-08-04-007 | PASS | `frontend/src/lib/harness/subagent-bridge.ts` lines 64-75 and 100-128; `frontend/src/__tests__/lib/subagent-bridge.test.ts` lines 32-45 and 73-115. | Child definitions have empty tools, disallowed parent-like tools, max one turn, no capability inheritance, and hard-deny preflight for ineligible children. |
| REQ-08-04-008 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 337-384 and 467-476; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 470-519. | Subagent Agent calls get hook preflight approval/denial, and governed hook failures fail closed. |
| REQ-08-04-009 | PASS | `frontend/src/lib/harness/subagent-bridge.ts` lines 5-12 and 64-75; `frontend/src/lib/harness/sdk-options-builder.ts` lines 92-121. | The bridge records Chirality policy/ruling metadata and constructs SDK options from Chirality-owned delegated-subagent state. |
| REQ-08-04-010 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 265-272; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 364-387. | Internal errors and unknown invalid states deny rather than falling through. |
| REQ-08-04-011 | PARTIAL | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 185-239; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 119-173. | The child-run record interface exists, but DEL-08-05 records naming and event-contract mismatches. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| DEL-08-05 interface remains partly unresolved. | Medium | `ChildRunRecord` exists with `childRunId`, while DEL-08-05 still asks for a different `runId` shape. | Reconcile the child-run contract before issuance of the PKG-08 package. |
| Governance metadata has no persisted decision artifact beyond logs/options. | Low | `evaluateSubagentGovernance` logs decisions and passes delegated names; child-run records are separate. | If issuance requires auditable governance decisions per denied/allowed attempt, add event emission or record linkage. |
| REF-006 remains warning-limited. | Low | `_REFERENCES.md` records the PRD hash mismatch. | Close or waive the PRD hash warning before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-08-04 is functionally landed enough for roadmap synthesis, but package closure depends on reconciling the DEL-08-05 child-run interface.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile DEL-08-05 child-run API naming with the implemented bridge and mapper. | reconcile | S | FIT | Decide whether `childRunId` or `runId` is authoritative. |
| Add event/record linkage for governance decisions if audit needs allowed/denied decision replay independent of console logs. | code/test | M | FIT | Child-run contract decision. |
| Keep SDK Agent exposure limited to delegated, requested Agent tool usage. | test | S | FIT | Existing `sdk-options-builder` guard. |

## Issuance-Gate-Process Observations

DEL-08-04 has strong fail-closed runtime evidence. The issuance gate should require child-run contract reconciliation at the package level, not additional executable subagent capability.
