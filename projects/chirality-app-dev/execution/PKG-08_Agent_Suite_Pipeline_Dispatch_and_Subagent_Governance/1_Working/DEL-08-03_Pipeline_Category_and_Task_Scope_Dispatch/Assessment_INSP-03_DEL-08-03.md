# Assessment INSP-03: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-08-03 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `d92ef1253b37cd29423672acb146a9e9c91087d5` |
| Spec source | `Specification.md` lines 1-83 |

## Scope

DEL-08-03 covers Pipeline category routing, category-specific options, TASK split selectors, dynamic working-root scope discovery, knowledge-type target selection, and reset behavior for stale selections.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-03-001 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 27-35, 91-102, and 483-708; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` lines 29-40. | Pipeline categories are `DECOMP`, `PREP`, `TASK`, and `AUDIT`, and operative matrix cells route by category. |
| REQ-08-03-002 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-83 and 486-708. | Category-specific option lists exist for decomposition, preparation, task, and audit lanes. |
| REQ-08-03-003 | PARTIAL | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 52-83 and 104-106. | Disabled "coming soon" options are visible in source. No dedicated render test for those disabled options was found. |
| REQ-08-03-004 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 532-647. | TASK has separate task-agent, scope-mode, dynamic-scope, and required target-deliverable selectors. |
| REQ-08-03-005 | PASS | `frontend/src/lib/workspace/task-scope.ts` lines 1-27; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 555-574. | Scope modes are `DELIVERABLES` and `KNOWLEDGE_TYPES`, gated by root marker state. |
| REQ-08-03-006 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 224-240 and 624-647; `frontend/src/lib/workspace/task-scope.ts` lines 39-76. | Knowledge-type mode requires and sanitizes a target deliverable key. |
| REQ-08-03-007 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 149-180 and 182-222; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 15-119. | Root changes, missing markers, stale deliverables, and stale knowledge targets reset invalid selections. |
| REQ-08-03-008 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 94-118; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | Required document-kit buckets include Datasheet, Specification, Guidance, and Procedure, and route tests prove mapping for representative buckets. |
| REQ-08-03-009 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 71-84 and 336-365. | `KnowledgeTypeOption` is canonicalized with id, label, and matching deliverable keys. |
| REQ-08-03-010 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 473-563; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 108-112 and 300-323. | Pipeline consumes active working-root scan data and summarizes deliverable/knowledge-type counts. |
| REQ-08-03-011 | PARTIAL | `frontend/src/lib/harness/turn-engine.ts` lines 262-274; `frontend/src/lib/harness/sdk-options-builder.ts` lines 92-121. | Runtime delegation still goes through Type 2 governance, but no direct test links the Pipeline TASK selector to that governance path. |
| REQ-08-03-012 | PARTIAL | `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 15-119; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-171. | Helper and API tests cover selection and discovery. No Pipeline component render test was found for disabled/reset UI states. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Pipeline surface has limited component-level regression coverage. | Medium | Helper and route tests exist; `rg` found no `PipelineSurface` render test. | Add one focused render test covering category selection, disabled options, and knowledge-target reset. |
| TASK selector to runtime governance is only indirectly proven. | Medium | Governance enforcement exists in `TurnEngine` and SDK options, not in a Pipeline integration test. | Add an integration or route-state test proving Pipeline TASK intent does not produce delegated subagents without governance. |
| Scope scanner includes extra knowledge buckets beyond the spec minimum. | Low | `filesystem.ts` builds a broader set than the four required document-kit buckets. | Document that extra buckets are discovery conveniences and not issuance requirements for this deliverable. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. The downstream dispatch/governance dependency remains open until Pipeline intent is tested against runtime delegation behavior.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a Pipeline render test for category controls, disabled options, and dynamic TASK target selection. | test | M | FIT | Current provider fixtures or a small mocked deliverables provider. |
| Add an integration assertion that Pipeline TASK intent cannot bypass Type 2 governance. | test | S | FIT | Decide the narrowest surface: URL-state, route, or runtime options. |
| Document extra scope buckets as non-normative discovery aids. | doc | S | FIT | None. |

## Issuance-Gate-Process Observations

DEL-08-03 is close to issuance on functionality but should not be treated as fully proven until a component-level Pipeline test covers the disabled/reset states that operators actually use.
