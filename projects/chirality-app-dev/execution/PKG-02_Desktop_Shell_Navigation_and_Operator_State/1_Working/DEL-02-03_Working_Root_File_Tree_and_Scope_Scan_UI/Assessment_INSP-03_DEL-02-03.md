# Assessment INSP-03: DEL-02-03 Working Root File Tree and Scope Scan UI

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-02-03 |
| Package | PKG-02 Desktop Shell Navigation and Operator State |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` |
| Spec source | `Specification.md` lines 5-93 |

## Scope

DEL-02-03 connects the shell to working-root selection, validation, bounded file-tree browsing, scope scans, deliverable routing widgets, and read-only status/dependency contract snapshots.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-02-03-REQ-001 | PASS | `frontend/src/components/shell/shell-frame.tsx` lines 103-140; `frontend/src/components/workspace/workspace-provider.tsx` lines 27-49 and 84-133. Focused validation passed. | Path entry, apply, Electron folder picker, and clear controls are exposed globally. |
| DEL-02-03-REQ-002 | PASS | `frontend/src/app/api/working-root/validate/route.ts` lines 11-20; `frontend/src/lib/workspace/filesystem.ts` lines 163-207 and 565-590; `frontend/src/components/workspace/workspace-provider.tsx` lines 84-95. Focused validation passed. | Invalid/missing/non-directory paths return typed workspace errors and are surfaced in UI state. Instruction-root containment appears owned by deeper PKG-07 contract checks, not this route. |
| DEL-02-03-REQ-003 | PASS | `frontend/src/components/workspace/workspace-provider.tsx` lines 100-103; `frontend/src/components/shell/file-tree-panel.tsx` lines 116-120 and 226-240; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 869-878. Focused validation passed. | Clearing root clears local state and root-dependent views/actions present empty/disabled states. |
| DEL-02-03-REQ-004 | PASS | `frontend/src/components/shell/file-tree-panel.tsx` lines 12, 116-168, and 226-258; `frontend/src/app/api/working-root/tree/route.ts` lines 21-42; `frontend/src/__tests__/api/working-root/tree-route.test.ts` lines 58-94. Focused validation passed. | File tree consumes `/api/working-root/tree` with bounded depth and refresh behavior. |
| DEL-02-03-REQ-005 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 5-14 and 231-234; `frontend/src/app/api/working-root/tree/route.ts` lines 8-19. Focused validation passed. | Skip-directory names are encoded in the tree scanner. |
| DEL-02-03-REQ-006 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 221-229 and 265-267; `frontend/src/components/shell/file-tree-panel.tsx` lines 75-77 and 235-237. Focused validation passed. | API marks unreadable/truncated directories with `truncated`, and UI displays truncation or errors. There is no separate inaccessible-directory marker beyond typed error/truncated behavior. |
| DEL-02-03-REQ-007 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 399-470 and 473-563; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 555-684. Focused validation passed. | Scope scan presents deliverables and knowledge-type options from API results. This assessment did not use semantic files. |
| DEL-02-03-REQ-008 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 145-190 and 192-222; `frontend/src/lib/workspace/task-scope.ts` lines 18-83; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 22-120. Focused validation passed. | Invalid dynamic selections clear on root, scan, deliverable, marker, and target changes. |
| DEL-02-03-REQ-009 | PASS | `frontend/src/components/portal/agent-matrix.tsx` lines 127-160 and 229-250; `frontend/src/lib/workspace/task-scope.ts` lines 14-16; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 8-13. Focused validation passed. | Deliverable widgets route to Pipeline TASK preselection through stable `pkg::id` keys. |
| DEL-02-03-REQ-010 | PASS | `frontend/src/components/workbench/workbench-surface.tsx` lines 129-171 and 320-379; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 243-285 and 851-929; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 69-199. Focused validation passed. | Status and dependency snapshots are read from contract APIs. Transition controls exist only in Workbench/Pipeline contract forms. |
| DEL-02-03-REQ-011 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 16-39 and 565-590; `frontend/src/__tests__/api/working-root/tree-route.test.ts` lines 134-144; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts` lines 177-199. Focused validation passed. | API clients preserve typed error code/status/message in thrown or rendered states. |
| DEL-02-03-REQ-012 | PASS | `frontend/src/app/api/working-root/tree/route.ts` lines 8-19; `frontend/src/lib/workspace/filesystem.ts` lines 5-6, 272-275, 406-419, and 481-493. Focused validation passed. | Tree depth is clamped and scope scans have directory caps/depth caps. |
| DEL-02-03-REQ-013 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 277-297 and 506-516; `frontend/src/lib/workspace/task-scope.ts` lines 14-16; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 8-13. Focused validation passed. | Deliverable identity uses stable ID extraction and `pkg::id` route keys rather than folder label text alone. |
| DEL-02-03-REQ-014 | PASS | `Specification.md` lines 15-20 and 69; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 851-929. Focused validation passed. | UI reads dependency snapshots but does not expose dependency extraction or create `Dependencies.csv`. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Exact skipped-directory and inaccessible-directory response shape remains underdocumented. | Low | `Specification.md` lines 80-84; `frontend/src/lib/workspace/filesystem.ts` lines 221-229 and 265-267. | Document current `truncated` behavior and whether separate inaccessible markers are required. |
| Component/browser render coverage is still not settled. | Medium | `Specification.md` lines 56-68; focused tests are route/helper/static coverage, not full browser interaction. | Resolve AMD-01 and add render tests if required. |
| REF-006 PRD hash mismatch remains open. | Low | `_REFERENCES.md` line 12. | Retain warning-limited source status until project-wide ruling. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-02-03 has 9 active dependency rows; `_DEPENDENCIES.md` lines 72-82 report 3 `NOT_APPLICABLE` anchors and 6 `TBD` execution rows.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Document the exact tree API behavior for skipped, unreadable, and truncated directories. | doc | S | FIT | None. |
| Add a component/browser test for working-root clear disabling root-dependent actions and file tree states. | test | S | FIT | AMD-01 decision on render-test bar. |
| Add a fixture for scope-scan truncation UI if issuance requires UI proof beyond API/helper coverage. | test | S | FIT | AMD-01 decision. |

## Issuance-Gate-Process Observations

DEL-02-03 has strong API/helper evidence, but the gate needs a clear policy for whether route/helper tests can satisfy UI acceptance or whether browser-level interaction evidence is required for shell controls.
