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
| REQ-08-02-003 | FAIL | `frontend/src/lib/shell/persona-resolution.ts` lines 26-32 and 34-39; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 28-38. | The current implementation deliberately removed `AGGREGATE -> AGGREGATION` because that routed a Type 2 task agent as a top-level persona. The spec is stale against the accepted loop-first routing. |
| REQ-08-02-004 | FAIL | `frontend/src/lib/shell/persona-resolution.ts` lines 26-32; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 28-38. | `RECONCILING -> RECONCILIATION` was deliberately removed; the matrix now uses `RESEARCH` for the EVALUATIVE/REVIEWING cell. |
| REQ-08-02-005 | PASS | `frontend/src/lib/shell/persona-resolution.ts` lines 34-39; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 22-26. | `AGENTS` resolves to `HELPS_HUMANS`. |
| REQ-08-02-006 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-18 and 42-135; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | The matrix encodes the required row set. |
| REQ-08-02-007 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-18 and 42-135; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | The matrix encodes the required column set. |
| REQ-08-02-008 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 1-13 and 34-36; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts` lines 4-25. | NORMATIVE cells route to loop-persona intent in the mounted shell, not the older Workbench-only route. |
| REQ-08-02-009 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 107-135; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 42-71. | EVALUATIVE cells also route to loop-persona intent and are guarded to Type 0/1 personas. This is consistent with current loop-first design but not the older Workbench wording. |
| REQ-08-02-010 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 78-105; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | OPERATIVE cells route to `/pipeline?category=...`. |
| REQ-08-02-011 | PASS | `frontend/src/lib/portal/agent-matrix-launch.ts` lines 10-31; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts` lines 4-25. | Matrix launches preserve row/column/persona intent while folding into the mounted shell URL. |
| REQ-08-02-012 | PASS | `frontend/src/lib/harness/agent-instruction.ts` lines 208-243; `frontend/src/__tests__/lib/harness-options.test.ts` lines 314-324. | Persona names resolve to `agents/AGENT_<name>.md` and missing files throw typed errors. |
| REQ-08-02-013 | PASS | `frontend/src/lib/harness/agent-instruction.ts` lines 221-235; `frontend/src/__tests__/lib/harness-options.test.ts` lines 314-324. | Missing personas produce `PERSONA_NOT_FOUND`. |
| REQ-08-02-014 | PARTIAL | `frontend/src/lib/shell/persona-resolution.ts` lines 12 and 45-53; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 8-15 and 49-53. | Empty persona selection defaults deterministically to `WORKING_ITEMS`, not `HELP_HUMAN`. Unknown non-empty personas pass through and can fail later. |
| REQ-08-02-015 | PASS | `frontend/src/lib/harness/options.ts` lines 17-24 and 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264. | Unknown runtime option keys warn and are ignored. |
| REQ-08-02-016 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-83 and 104-106. | Unsupported pipeline variants remain visible as disabled "coming soon" options. |
| REQ-08-02-017 | PARTIAL | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 42-82; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 28-38. | The implementation has guard tests against Type 2 persona routing, but the spec still names two removed aliases. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G5: DEL-08-02 spec is stale against loop-first matrix routing and removed aliases. | Medium | `persona-resolution.ts` lines 26-32 and `agent-matrix-cells.ts` lines 68-74 and 129-132. | Update DEL-08-02 to make the Type 0/1 persona guard authoritative and remove the old alias requirements. |
| Workbench wording is stale. | Low | `agent-matrix-launch.ts` lines 5-31 folds targets into the mounted shell route. | Replace Workbench-only language with loop-persona route-state language. |
| Fallback semantics need one accepted statement. | Low | `resolvePersona` defaults empty input to `WORKING_ITEMS`; unknown non-empty personas pass through. | Decide whether unknown non-empty persona labels should fail early or remain deferred to instruction-file resolution. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. The DEL-04-04 and DEL-08-03 interface dependencies remain inspection inputs rather than closed dependency rows.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Amend DEL-08-02 requirements to match loop-first routing and the Type 0/1 persona guard. | reconcile | S | FIT | Human acceptance that the Type 2 alias removals are the desired contract. |
| Add one doc note explaining empty default vs unknown-persona behavior. | doc/test | S | FIT | Fallback decision. |
| Keep the matrix guard test as the issuance-critical regression fixture. | test | S | FIT | Spec amendment. |

## Issuance-Gate-Process Observations

The code is safer than the older alias specification because it prevents Type 2 task agents from booting as top-level personas. The gate should treat the current spec as the problem to reconcile, not the implementation.
