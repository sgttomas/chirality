# Assessment INSP-03: DEL-02-01 Desktop Shell and Matrix Navigation

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-02-01 |
| Package | PKG-02 Desktop Shell Navigation and Operator State |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` |
| Spec source | `Specification.md` lines 5-67 |

## Scope

DEL-02-01 covers desktop shell navigation and canonical matrix routing. The current implementation has intentionally moved to the accepted loop-first product shape: the live loop is primary, the header keeps only Portal as primary navigation, and Portal/Workbench/Pipeline forms are also reachable as right-sidebar tertiary tabs and deep-link routes.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-02-01-REQ-001 | PARTIAL | `frontend/src/components/shell/portal-loop-shell.tsx` lines 18-54; `frontend/src/components/shell/loop-tertiary-shell.tsx` lines 21-49; `frontend/src/components/shell/tertiary-sidebar-tabs.tsx` lines 7-16; `frontend/src/__tests__/components/workspace-sidebar.test.ts` lines 7-24. Focused validation: `npm run test -- ...` (22 files / 203 tests) passed. | All three surfaces are reachable, but not as equal primary header navigation after the loop-first pivot. |
| DEL-02-01-REQ-002 | PARTIAL | `frontend/src/components/shell/shell-frame.tsx` lines 16-20 and 87-100; `frontend/src/app/workbench/workbench-client.tsx` lines 5-14; `frontend/src/app/pipeline/pipeline-client.tsx` lines 5-14. Focused validation passed. | Deep-link route entry points remain, but header navigation no longer exposes `/pipeline` and `/workbench`. This is spec drift from the older baseline wording. |
| DEL-02-01-REQ-003 | PARTIAL | `frontend/src/components/shell/shell-frame.tsx` lines 87-100. | Active-state code exists for rendered header links, but only Portal is in the primary header list, so the requirement is no longer fully testable across all three original routes. |
| DEL-02-01-REQ-004 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 42-135; `frontend/src/components/portal/agent-matrix.tsx` lines 95-125; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. Focused validation passed. | Matrix data and rendering preserve the 3x4 structure. |
| DEL-02-01-REQ-005 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 42-135; `frontend/src/components/portal/agent-matrix.tsx` lines 102-124; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. Focused validation passed. | Rows are `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`. |
| DEL-02-01-REQ-006 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-18 and 42-135; `frontend/src/components/portal/agent-matrix.tsx` lines 95-100; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. Focused validation passed. | Columns are `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`. |
| DEL-02-01-REQ-007 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 1-13 and 47-76; `frontend/src/components/portal/agent-matrix.tsx` lines 200-214; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 42-71. Focused validation passed. | NORMATIVE cells focus a mounted loop persona context, not a separate primary Workbench page. This matches the loop-first pivot but not the old route wording. |
| DEL-02-01-REQ-008 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 107-134; `frontend/src/components/portal/agent-matrix.tsx` lines 200-214; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 42-82. Focused validation passed. | EVALUATIVE cells likewise focus loop persona context; Workbench remains a sidebar/deep-link form. |
| DEL-02-01-REQ-009 | PASS | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 78-105; `frontend/src/components/portal/agent-matrix.tsx` lines 217-223; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts` lines 15-25. Focused validation passed. | OPERATIVE matrix targets open Pipeline intent in the sidebar with stale pipeline scope query cleared. |
| DEL-02-01-REQ-010 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-82, 104-106, 500-504, 547-550, and 701-704; `frontend/src/__tests__/components/agent-matrix-panel.test.ts` lines 21-38. Focused validation passed. | Matrix-adjacent Pipeline controls keep unsupported variants visible as disabled coming-soon options; matrix launches also disable during streaming. |
| DEL-02-01-REQ-011 | PARTIAL | `frontend/src/lib/portal/agent-matrix-cells.ts` lines 16-31; `frontend/src/lib/workspace/task-scope.ts` lines 14-16; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 8-13. Focused validation passed. | Stable agent/row/column and `pkg::deliverable` keys exist, but the specification itself still marks exact assertion names and route-state key disposition as TBD. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Header-navigation requirements are stale after the loop-first pivot. | Medium | `Specification.md` lines 9-13 and 26-28; `frontend/src/components/shell/shell-frame.tsx` lines 16-20. | Reconcile DEL-02-01 wording to distinguish primary header nav, sidebar tertiary forms, and deep-link route entries. |
| NORMATIVE/EVALUATIVE matrix destination language still says WORKBENCH while code now focuses loop persona context. | Medium | `Specification.md` lines 32-33; `frontend/src/lib/portal/agent-matrix-cells.ts` lines 1-13. | Amend route semantics to the accepted loop-first convention; keep Workbench as contract-review form. |
| UI render-test acceptance bar remains unresolved. | Medium | `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` lines 69 and 227-229. | Resolve AMD-01 before issuance review: decide whether server-render/static markup tests are enough or browser/component render tests are required. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Keep as warning-limited source input pending project-wide REF-006 ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. This assessment also records accepted loop-first drift against older baseline spec wording. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-02-01 has 8 active dependency rows; `_DEPENDENCIES.md` records 4 `NOT_APPLICABLE` anchor rows and 4 `TBD` execution rows, including `DEP-02-01-005` for the implementation workspace unknown. The accepted project-level DepClosure snapshot remains acyclic for dependency-closure discovery only.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Reconcile DEL-02-01 spec/procedure text to the loop-first shell: primary header Portal only, sidebar tertiary Portal/Workbench/Pipeline, and deep-link route entries. | doc/reconcile | S | FIT | Keep D-APP-28/D-APP-30/D-APP-31/D-APP-32 rulings as accepted basis. |
| Add a small route/shell test that asserts Workbench and Pipeline deep links open their sidebar tabs under `LoopTertiaryShell`. | test | S | FIT | AMD-01 decision on render-test bar. |
| Add an explicit matrix identity test for agent/row/column query keys and `pkg::id` deliverable keys. | test | S | FIT | Spec key-name reconciliation. |

## Issuance-Gate-Process Observations

DEL-02-01 is functionally strong but should not be issued against unreconciled pre-pivot route wording. The gate needs a way to accept governed product pivots without marking correct newer behavior as a failure against obsolete baseline text.
