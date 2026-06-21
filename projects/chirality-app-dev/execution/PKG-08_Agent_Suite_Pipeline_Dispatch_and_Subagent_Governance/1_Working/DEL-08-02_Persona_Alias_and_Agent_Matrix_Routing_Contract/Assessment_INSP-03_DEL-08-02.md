# Assessment INSP-03: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-08-02 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `d92ef1253b37cd29423672acb146a9e9c91087d5` |
| Spec source | `Specification.md` lines 1-75 |

## Scope

DEL-08-02 covers matrix labels, persona alias resolution, row/column routing, fallback behavior, and deterministic handling of unsupported or unknown persona/route states.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-02-001 | PASS | `frontend/src/lib/shell/persona-resolution.ts` lines 34-39; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 22-26. | `HELP` resolves to `HELP_HUMAN`. |
| REQ-08-02-002 | PASS | `frontend/src/lib/shell/persona-resolution.ts` lines 34-39; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 22-26. | `ORCHESTRATE` resolves to `ORCHESTRATOR`. |
| REQ-08-02-003 | PASS | `Specification.md` alias requirements; `frontend/src/lib/shell/persona-resolution.ts`; `frontend/src/__tests__/lib/persona-resolution.test.ts`. | `AGGREGATE -> AGGREGATION` is no longer a compatibility alias. This preserves the Type 0/1 top-level persona boundary instead of routing a Type 2 task agent as a persona. |
| REQ-08-02-004 | PASS | `Specification.md` alias requirements; `frontend/src/lib/shell/persona-resolution.ts`; `frontend/src/__tests__/lib/persona-resolution.test.ts`. | `RECONCILING -> RECONCILIATION` is no longer a compatibility alias. The EVALUATIVE/REVIEWING matrix cell uses `RESEARCH` under the accepted matrix contract. |
| REQ-08-02-005 | PASS | `frontend/src/lib/shell/persona-resolution.ts` lines 34-39; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 22-26. | `AGENTS` resolves to `HELPS_HUMANS`. |
| REQ-08-02-006 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-18 and 42-135; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | The matrix encodes the required row set. |
| REQ-08-02-007 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-18 and 42-135; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | The matrix encodes the required column set. |
| REQ-08-02-008 | PASS | `Specification.md` routing requirements; `frontend/src/lib/portal/agent-matrix-cells.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`. | NORMATIVE cells route to loop-persona intent in the mounted shell. |
| REQ-08-02-009 | PASS | `Specification.md` routing requirements; `frontend/src/lib/portal/agent-matrix-cells.ts`; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`. | EVALUATIVE cells route to loop-persona intent and are guarded to Type 0/1 personas. |
| REQ-08-02-010 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 78-105; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | OPERATIVE cells route to `/pipeline?category=...`. |
| REQ-08-02-011 | PASS | `frontend/src/lib/portal/agent-matrix-launch.ts` lines 10-31; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts` lines 4-25. | Matrix launches preserve row/column/persona intent while folding into the mounted shell URL. |
| REQ-08-02-012 | PASS | `frontend/src/lib/harness/agent-instruction.ts` lines 208-243; `frontend/src/__tests__/lib/harness-options.test.ts` lines 314-324. | Persona names resolve to `agents/AGENT_<name>.md` and missing files throw typed errors. |
| REQ-08-02-013 | PASS | `frontend/src/lib/harness/agent-instruction.ts` lines 221-235; `frontend/src/__tests__/lib/harness-options.test.ts` lines 314-324. | Missing personas produce `PERSONA_NOT_FOUND`. |
| REQ-08-02-014 | PASS | `Specification.md` fallback requirements; `frontend/src/lib/shell/persona-resolution.ts`; `frontend/src/__tests__/lib/persona-resolution.test.ts`. | Empty persona selection defaults deterministically to `WORKING_ITEMS`. Unknown non-empty personas pass through normalized and fail later at instruction-file lookup if no matching agent exists. |
| REQ-08-02-015 | PASS | `frontend/src/lib/harness/options.ts` lines 17-24 and 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264. | Unknown runtime option keys warn and are ignored. |
| REQ-08-02-016 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-83 and 104-106. | Unsupported pipeline variants remain visible as disabled "coming soon" options. |
| REQ-08-02-017 | PASS | `Specification.md`; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/lib/persona-resolution.test.ts`. | The spec, matrix guard tests, and alias fixtures now agree that Type 2 agents are not top-level personas. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Removed Type 2 persona aliases needed source/spec reconciliation. | Closed by ADQ-12 | `Specification.md`; `Guidance.md`; `Procedure.md`; `Datasheet.md`; `persona-resolution.test.ts`. | The stable long-term contract forbids `AGGREGATE -> AGGREGATION` and `RECONCILING -> RECONCILIATION` top-level persona aliases. |
| Workbench wording was stale. | Closed by ADQ-12 | `Specification.md`; `Guidance.md`; `Procedure.md`; `agent-matrix-launch.test.ts`. | Normative and evaluative cells now document loop-persona routing through the mounted shell. |
| Fallback semantics needed one accepted statement. | Closed by ADQ-12 | `Specification.md`; `resolvePersona`; `persona-resolution.test.ts`. | Empty persona defaults to `WORKING_ITEMS`; unknown non-empty labels remain deferred to instruction-file resolution. |

## Source-State Caveat

`docs/PRD.md` is current under the D-APP-38 authority corpus for this deliverable; `_REFERENCES.md` records REF-006 as `MATCH`. No semantic files were used or produced.

## Dependency Closure Note

This ADQ-12 supersession updates current evidence and local dependency notes but does not advance lifecycle state. The DEL-08-03 interface remains an inspection input for Pipeline selector behavior.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Keep persona alias, matrix-cell, and launch tests in the PKG-08 regression suite. | test | S | FIT | Current loop-persona contract. |
| Route any future Type 2 execution through Pipeline/TASK governance rather than top-level persona aliases. | code/doc | S | FIT | Current Type 0/1 persona boundary. |

## Lifecycle-Gate-Process Observations

ADQ-12 reconciles the older alias specification with the safer Type 0/1 top-level persona boundary. No lifecycle state is advanced by this assessment.
