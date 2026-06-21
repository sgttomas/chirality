# Assessment INSP-03: DEL-02-02 Workbench and Pipeline Selection UX

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-02-02 |
| Package | PKG-02 Desktop Shell Navigation and Operator State |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` |
| Spec source | `Specification.md` lines 5-70 |

## Scope

DEL-02-02 covers Workbench active-agent context, Workbench read-only deliverable contract summaries, Pipeline operative category controls, TASK split selectors, and stale-selection reset behavior.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-02-02-REQ-001 | PASS | `frontend/src/components/workbench/workbench-surface.tsx` lines 47-60 and 293-318. Focused validation passed. | Workbench reads query parameters with defaults and renders agent, matrix row, and matrix column. |
| DEL-02-02-REQ-002 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 1-13; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40 and 42-71. Focused validation passed. | The implemented rule preserves NORMATIVE/EVALUATIVE as loop-persona intent and OPERATIVE as Pipeline intent. This is correct for loop-first, but not the older "open WORKBENCH" wording. |
| DEL-02-02-REQ-003 | PASS | `frontend/src/components/workbench/workbench-surface.tsx` lines 129-171, 320-379; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 148-199. Focused validation passed. | Workbench fetches lifecycle and dependency snapshots from contract APIs rather than UI convenience state. |
| DEL-02-02-REQ-004 | PARTIAL | `frontend/src/components/workbench/workbench-surface.tsx` lines 173-180, 320-329, and 440-522; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 141-146. Focused validation passed. | Actor gating and disabled transition controls exist, but the spec still says the source-of-truth registry is TBD and there is no Workbench component render test for unsupported agents. |
| DEL-02-02-REQ-005 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 27-35, 52-82, 104-106, 486-530, 532-553, and 687-708. Focused validation passed. | Pipeline exposes `DECOMP`, `PREP`, `TASK`, and `AUDIT`, with unsupported options visible and disabled. |
| DEL-02-02-REQ-006 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 532-553 and 555-622; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 8-41. Focused validation passed. | TASK has split task-agent and dynamic scope selectors. |
| DEL-02-02-REQ-007 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 555-647 and 674-684; `frontend/src/lib/workspace/task-scope.ts` lines 18-83; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 15-120. Focused validation passed. | Scope modes normalize to `DELIVERABLES` unless knowledge mode is enabled; knowledge mode requires a target deliverable. |
| DEL-02-02-REQ-008 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 145-190 and 192-222; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 22-120. Focused validation passed. | Project-root changes, scan errors, removed deliverables, missing knowledge markers, and stale targets clear invalid selections. |
| DEL-02-02-REQ-009 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-82 and 500-504, 547-550, 701-704. Focused validation passed. | Unsupported variants remain visible and non-selectable. |
| DEL-02-02-REQ-010 | PASS | `frontend/src/components/workbench/workbench-surface.tsx` lines 129-171; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 243-285 and 851-929; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 148-230. Focused validation passed. | UI consumes project contract snapshots; it does not author project truth from selection state. |
| DEL-02-02-REQ-011 | PASS | `frontend/src/components/workbench/workbench-surface.tsx` lines 320-379; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 851-929; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 69-126 and 177-199. Focused validation passed. | Status/dependency summaries are populated from deliverable contract APIs and missing/error states remain explicit. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Matrix destination language has loop-first drift. | Medium | `Specification.md` line 26; `frontend/src/lib/portal/agent-matrix-cells.ts` lines 1-13. | Reconcile DEL-02-02 with the accepted loop-first routing convention. |
| Workbench lifecycle-control render coverage is thin. | Medium | `Specification.md` lines 52-53; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 141-146. | Add a Workbench render test for unsupported agents and approval-SHA-required transitions. |
| SOW-007 ownership overlap remains unresolved. | Medium | `_DEPENDENCIES.md` lines 28-30 and 43-47. | Resolve or explicitly defer overlap with DEL-08-03 before issuance. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-02-02 has 9 active extracted rows, all `TBD` per `_DEPENDENCIES.md` lines 33-66. The open `SOW_007_OWNER_OVERLAP` warning is preserved as a finding, not resolved here.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile matrix routing wording with loop-first behavior. | doc/reconcile | S | FIT | DEL-02-01 route-language reconciliation. |
| Add Workbench component tests for unsupported lifecycle actors and approval-SHA gating. | test | S | FIT | AMD-01 decision on render-test bar. |
| Decide or document SOW-007 ownership split between PKG-02 Pipeline UI and PKG-08 dispatch semantics. | governance/reconcile | S | FIT | INSP-03 PKG-08 wave or earlier human ruling. |

## Issuance-Gate-Process Observations

DEL-02-02 has broad runnable evidence, but issuance would still need to decide whether API/helper tests plus static render tests meet the UI acceptance bar or whether browser-level component tests are mandatory for lifecycle-control disabling.
