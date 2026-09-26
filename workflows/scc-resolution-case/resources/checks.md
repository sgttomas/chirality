# QA CHECKS — scc-resolution-case

## Required Checks

- Required case files exist.
- Required CSV columns are present.
- `CaseState` is one of the canonical lifecycle states.
- Every candidate remedy has evidence or a `TBD` reason.
- Every owner handoff names an owning workflow.
- Case text does not claim SCC closure unless cited DepClosure evidence proves it.
- The case is in the project's one case home (`_DAG/cases/<SCC-ID>/`, or the legacy PKG-00 control deliverable that already holds its cases).
- Neither `_DAG/cases/` nor a PKG-00 control deliverable contains a `Dependencies.csv`.
- Seed packets, when present, are labeled seed evidence and not active WORKING_ITEMS (workflow: scope-change) intake.

## Closure Boundary

`CLOSED_BY_DEPCLOSURE` is valid only when `Case_QA.md` cites a follow-up DepClosure snapshot proving the SCC is absent or otherwise formally accepted by the owning reconciliation workflow.
