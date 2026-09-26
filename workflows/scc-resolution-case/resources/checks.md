# QA CHECKS — scc-resolution-case

## Required Checks

- Required case files exist.
- Required CSV columns are present.
- `CaseState` is one of the canonical lifecycle states.
- Every candidate remedy has evidence or a `TBD` reason.
- Every owner handoff names an owning workflow.
- Case text does not claim SCC closure unless cited DepClosure evidence proves it.
- The case is in the project's one case home (`_DAG/cases/<CASE-ID>/`, or the legacy PKG-00 control deliverable that already holds its cases).
- Under `_DAG/cases/`, the folder name is the case's `CASE_ID` (`SCC-CASE-NNN`), not a closure run's SCC ID, and no other case uses that number.
- `Case_Datasheet.md` records the originating closure snapshot, its SCC ID, and the member node set, and each later matched snapshot with any membership change.
- Run records are under `{CASE_PATH}/_run_records/` (or the legacy control deliverable's `_run_records/`), not `_DAG/cases/_run_records/`.
- Neither `_DAG/cases/` nor a PKG-00 control deliverable contains a `Dependencies.csv`. `tools/validation/validate_scc_resolution_case.py` checks only the App's legacy `PKG-00_DAG_Closure_and_Project_Control` path; for `_DAG/cases/` this is a manual check until the validator is generalized.
- Seed packets, when present, are labeled seed evidence and not active WORKING_ITEMS (workflow: scope-change) intake.

## Closure Boundary

`CLOSED_BY_DEPCLOSURE` is valid only when `Case_QA.md` cites a follow-up DepClosure snapshot proving the SCC is absent or otherwise formally accepted by the owning reconciliation workflow.
