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
| REQ-08-03-003 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx`; `frontend/src/__tests__/components/pipeline-surface.test.ts`. | Disabled "coming soon" options are visible in source and covered by the Pipeline surface render test. |
| REQ-08-03-004 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 532-647. | TASK has separate task-agent, scope-mode, dynamic-scope, and required target-deliverable selectors. |
| REQ-08-03-005 | PASS | `frontend/src/lib/workspace/task-scope.ts` lines 1-27; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 555-574. | Scope modes are `DELIVERABLES` and `KNOWLEDGE_TYPES`, gated by root marker state. |
| REQ-08-03-006 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 224-240 and 624-647; `frontend/src/lib/workspace/task-scope.ts` lines 39-76. | Knowledge-type mode requires and sanitizes a target deliverable key. |
| REQ-08-03-007 | PASS | `frontend/src/components/pipeline/pipeline-surface.tsx` lines 149-180 and 182-222; `frontend/src/__tests__/lib/task-scope-selection.test.ts` lines 15-119. | Root changes, missing markers, stale deliverables, and stale knowledge targets reset invalid selections. |
| REQ-08-03-008 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 94-118; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | Required document-kit buckets include Datasheet, Specification, Guidance, and Procedure, and route tests prove mapping for representative buckets. |
| REQ-08-03-009 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 71-84 and 336-365. | `KnowledgeTypeOption` is canonicalized with id, label, and matching deliverable keys. |
| REQ-08-03-010 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 473-563; `frontend/src/components/pipeline/pipeline-surface.tsx` lines 108-112 and 300-323. | Pipeline consumes active working-root scan data and summarizes deliverable/knowledge-type counts. |
| REQ-08-03-011 | PASS | `frontend/src/lib/harness/turn-engine.ts`; `frontend/src/lib/harness/sdk-options-builder.ts`; `frontend/src/__tests__/api/harness/routes.test.ts`. | Runtime delegation still goes through Type 2 governance, and the route regression proves Pipeline TASK selector state is ignored as unknown options rather than converted into delegated subagents. |
| REQ-08-03-012 | PASS | `frontend/src/__tests__/lib/task-scope-selection.test.ts`; `frontend/src/__tests__/api/project/deliverables-route.test.ts`; `frontend/src/__tests__/components/pipeline-surface.test.ts`. | Helper, API, and Pipeline component tests cover category controls, disabled options, dynamic TASK target selection, and stale target reset during initial render. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Pipeline surface had limited component-level regression coverage. | Closed by ADQ-12 | `frontend/src/__tests__/components/pipeline-surface.test.ts`. | Focused render tests now cover category controls, disabled options, valid TASK deep links, and stale knowledge-target reset. |
| TASK selector to runtime governance was only indirectly proven. | Closed by ADQ-12 | `frontend/src/__tests__/api/harness/routes.test.ts`. | Pipeline TASK selector state is treated as unknown runtime options and cannot bypass Type 2 governance. |
| Scope scanner includes extra knowledge buckets beyond the spec minimum. | Low | `filesystem.ts` builds a broader set than the four required document-kit buckets. | Document that extra buckets are discovery conveniences and not additional acceptance requirements for this deliverable. |

## Source-State Caveat

`docs/PRD.md` is current under the D-APP-38 authority corpus for this deliverable; `_REFERENCES.md` records REF-006 as `MATCH`. No semantic files were used or produced.

## Dependency Closure Note

This ADQ-12 supersession updates current evidence and local dependency notes but does not advance lifecycle state. Pipeline intent is now tested against runtime delegation behavior.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Document extra scope buckets as non-normative discovery aids. | doc | S | FIT | None. |
| Keep Pipeline surface and route-state regressions in the PKG-08 validation suite. | test | S | FIT | Current selector contract. |

## Lifecycle-Gate-Process Observations

ADQ-12 closes the component-level Pipeline and TASK/governance linkage residuals. Extra scanner buckets remain non-normative discovery aids rather than additional acceptance requirements.

---

**Correction note (2026-07-18 — identifier qualification):** The requirement
identifiers in this assessment use the reversed qualification form
`REQ-08-03-NNN`. The canonical qualified form under the Deliverable
Scope-of-Work Standard §4 is `DEL-08-03-REQ-NNN`. Each `REQ-08-03-NNN` above maps
to `DEL-08-03-REQ-NNN` with the same three-digit NNN. Recorded assessment rows
are unchanged; this appended note governs interpretation of the identifiers.
