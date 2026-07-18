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
| REQ-08-04-011 | PASS | `frontend/src/lib/harness/agent-runtime-contract.ts` lines 71-85 and 185-239; `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` lines 119-173; DEL-08-05 ADQ-05 updates. | The child-run handoff uses `ChildRunRecord.childRunId`, and DEL-08-05 now aligns naming and denied-allocation semantics with D-APP-40. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Child-output artifact proof remained separate. | Closed by ADQ-12 | DEL-08-05 now persists over-inline child summaries as child-output artifacts with parent-turn, task, child-run, tool-use, redaction, checksum, byte, and truncation metadata. | Keep the ADQ-12 artifact fixtures in the PKG-08 regression suite. |
| Governance metadata has no persisted decision artifact beyond logs/options. | Low | `evaluateSubagentGovernance` logs decisions and passes delegated names; child-run records are separate. | If later audit policy requires decision replay per denied/allowed attempt, add event emission or record linkage. |
| REF-006 source state is governed by D-APP-38. | Low | D-APP-38 accepts the current authority corpus for PRD-derived subagent governance text. | Keep implementation proof separate from source-state proof. |

## Source-State Caveat

`docs/PRD.md` is current under the D-APP-38 authority corpus for this deliverable. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-08-04 is functionally landed enough for roadmap synthesis, and ADQ-05 reconciles the DEL-08-05 child-run interface naming and denied-allocation boundary.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add event/record linkage for governance decisions if audit needs allowed/denied decision replay independent of console logs. | code/test | M | FIT | Child-run contract decision. |
| Keep SDK Agent exposure limited to delegated, requested Agent tool usage. | test | S | FIT | Existing `sdk-options-builder` guard. |

## Lifecycle-Gate-Process Observations

DEL-08-04 has strong fail-closed runtime evidence, and ADQ-12 closes the package-level child-output artifact evidence residual through DEL-08-05. No additional executable subagent capability is introduced.

---

**Correction note (2026-07-18 — identifier qualification):** The requirement
identifiers in this assessment use the reversed qualification form
`REQ-08-04-NNN`. The canonical qualified form under the Deliverable
Scope-of-Work Standard §4 is `DEL-08-04-REQ-NNN`. Each `REQ-08-04-NNN` above maps
to `DEL-08-04-REQ-NNN` with the same three-digit NNN. Recorded assessment rows
are unchanged; this appended note governs interpretation of the identifiers.
