# Specification: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

## Scope

This deliverable specifies the control-plane work needed to prepare and record source-grounded rulings for SCC-001, the large strict FULL_GRAPH cycle spanning runtime, SDK, session, and tooling deliverables.

In scope:

- Consume the current DepClosure snapshot named in `_REFERENCES.md`.
- Use `Evidence/scc_summary.csv` to preserve the SCC-001 node set.
- Use `Evidence/bidirectional_pairs.csv` and `SCC_Triage_Workbook.csv` as the initial evidence queue for a focused SCC-001 ruling workbook.
- Record dependency row decisions and follow-up DepClosure evidence after source-grounded reconciliation work.

Out of scope:

- Creating `Dependencies.csv` for this DEL-00 control deliverable.
- Mutating dependency rows as part of this four-document generation task.
- Inventing new dependency types or edge semantics.
- Reporting project-wide `BLOCKED/UNBLOCKED` before strict FULL_GRAPH is acyclic.

Sources: `_CONTEXT.md` (Deliverable Scope, Source Authority), `_DEPENDENCIES.md` (Boundary), `README.md` (Boundary, Non-Goals), `DAG_CLOSURE_CONTROL.md` (Workflow, Acceptance Condition).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-DEL-00-02-001 | The deliverable MUST remain a PKG-00 control artifact and MUST NOT be promoted into the product dependency graph by adding a deliverable-local `Dependencies.csv`. | `_CONTEXT.md` (Source Authority); `_DEPENDENCIES.md` (Boundary); `README.md` (Boundary) |
| REQ-DEL-00-02-002 | The SCC-001 workflow MUST consume the current DepClosure snapshot identified as `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431`. | `_REFERENCES.md` (Authoritative Source Corpus); `DAG_CLOSURE_CONTROL.md` (Control Status) |
| REQ-DEL-00-02-003 | The SCC-001 node set MUST be treated as the 18 nodes listed for SCC-001 in `Evidence/scc_summary.csv` unless superseded by a later accepted DepClosure snapshot. | `Evidence/scc_summary.csv`; `Dependency_Closure_Report.md` (Remaining SCCs) |
| REQ-DEL-00-02-004 | The next SCC-001 control output SHOULD be a focused ruling workbook generated from current bidirectional-pair evidence. | `DAG_CLOSURE_CONTROL.md` (Current Queue); `SCC_Triage_Workbook.csv` (SCC-001 row); `SCC_Triage_Notes.md` (SCC-001 Initial Reading) |
| REQ-DEL-00-02-005 | Dependency row decisions MUST inspect owning product deliverable dependency registers and cited source evidence before any row mutation. | `DAG_CLOSURE_CONTROL.md` (Workflow); `SCC_Triage_Workbook.csv` (RecommendedAction); `_DEPENDENCIES.md` (Declared Upstream) |
| REQ-DEL-00-02-006 | Edge classifications MUST use existing dependency schema semantics only; new dependency types MUST NOT be invented. | `SCC_Triage_Workbook.csv` (RecommendedAction); `SCC_Triage_Notes.md` (SCC-001 Initial Reading) |
| REQ-DEL-00-02-007 | Closure MUST be evidenced by a follow-up DepClosure scan showing strict `scc_count = 0`, strict FULL_GRAPH acyclic, and blocker state reportable by ORCHESTRATOR. | `DAG_CLOSURE_CONTROL.md` (Acceptance Condition); `Dependency_Closure_Report.md` (Ruling) |
| REQ-DEL-00-02-008 | Current dependency closure decisions for SCC-001 remain TBD / handoff until source-grounded evidence supports explicit rulings. | INIT-TASK CustomInstructions; `SCC_Triage_Workbook.csv` (RecommendedAction) |
| REQ-DEL-00-02-009 | The focused SCC-001 ruling workbook MUST include the 12 bidirectional pairs whose nodes are both in SCC-001 and MUST exclude the SCC-002 pair. | `Evidence/scc_summary.csv`; `Evidence/bidirectional_pairs.csv`; `SCC_Triage_Workbook.csv` (SCC-001 row) |
| REQ-DEL-00-02-010 | The handoff record MUST name the accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers. | `AGENTS.md` (Handoff-state rule, Closure rule); `Procedure.md` (Records) |

## Standards

| Standard / Control | Applicability | Location |
|---|---|---|
| PKG-00 control package boundary | Governs this deliverable's control-only status and exclusion from product graph discovery. | `README.md` (Boundary) |
| DepClosure snapshot evidence | Governs current SCC status, node set, bidirectional-pair queue, and acyclic/cyclic verdicts. | `Dependency_Closure_Report.md`; `Evidence/*.csv`; `closure_summary.json` |
| Existing dependency schema actions and fields | Governs future row decisions in owning product deliverable registers. | Source location TBD / HumanRuling required before row-classification work; cited by `DAG_CLOSURE_CONTROL.md` workflow and `SCC_Triage_Workbook.csv` directive |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-DEL-00-02-001 | Confirm this folder still has no `Dependencies.csv` and remains marked `EXCLUDED_CONTROL_DELIVERABLE` in `_DEPENDENCIES.md`. |
| REQ-DEL-00-02-002 | Confirm `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md` point to the same current DepClosure snapshot. |
| REQ-DEL-00-02-003 | Compare the focused ruling workbook node set to `Evidence/scc_summary.csv`. |
| REQ-DEL-00-02-004 | Confirm ruling workbook rows are derived from `Evidence/bidirectional_pairs.csv` and `SCC_Triage_Workbook.csv`. |
| REQ-DEL-00-02-005 | For each proposed row decision, record the owning product dependency row and cited source evidence. |
| REQ-DEL-00-02-006 | Review each classification against existing dependency schema values before applying product-register changes. |
| REQ-DEL-00-02-007 | Run DepClosure after accepted row updates and verify strict SCC count is 0 before project-wide reporting. |
| REQ-DEL-00-02-008 | Treat unresolved SCC-001 decisions as handoff items until RECONCILIATION or an approved task records source-grounded rulings. |
| REQ-DEL-00-02-009 | Count workbook input pairs against `Evidence/bidirectional_pairs.csv`: accept only the 12 pairs whose endpoints both appear in the SCC-001 node set from `Evidence/scc_summary.csv`; confirm the `DEL-10-02` / `DEL-10-03` SCC-002 pair is excluded. |
| REQ-DEL-00-02-010 | Confirm the handoff state explicitly records accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers before downstream use. |

## Documentation

Required records:

- Focused SCC-001 ruling workbook.
- Per-row decision records citing owning product registers and source evidence.
- Updated product `Dependencies.csv` rows only where evidence supports change.
- Follow-up DepClosure snapshot and closure report.
- Handoff state naming accepted upstream snapshot, derivative status, closure verdict, rerun requirements, and remaining blockers.

## Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| B-001 | Incorporated. | Added `REQ-DEL-00-02-009` and matching verification from `Evidence/scc_summary.csv`, `Evidence/bidirectional_pairs.csv`, and `SCC_Triage_Workbook.csv`. |
| F-001 | Converted to TBD / HumanRuling. | Standards now preserve the unresolved source location for existing dependency schema actions and fields; no local source slice identified the governing schema location in this run. |
| X-001 | Incorporated. | Added `REQ-DEL-00-02-010` and matching verification for handoff-state fields using the governance rules supplied in the task instructions and the existing Procedure Records section. |
