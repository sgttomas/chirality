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
- Neither `_DAG/cases/` nor a PKG-00 control deliverable contains a `Dependencies.csv`. `tools/validation/validate_scc_resolution_case.py` checks the whole of `_DAG/cases/` for a case there, and the legacy `PKG-00_DAG_Closure_and_Project_Control` path for a legacy case.
- Seed packets, when present, are labeled seed evidence and not active WORKING_ITEMS (workflow: scope-change) intake.

For a case under `_DAG/cases/`, the validator also checks that the case folder sits directly under `_DAG/cases/`, that its name has the `SCC-CASE-NNN` form, and that `Case_Datasheet.md` records that ID. It checks that no other folder there uses the same number and that `_DAG/cases/_run_records/` does not exist. It also checks that the project holds no cases in a legacy PKG-00 home. Whether the datasheet records the originating snapshot, SCC ID and member node set, and each later matched snapshot, is still checked by hand. A legacy case is validated as before, without these checks.

## Closure Boundary

`CLOSED_BY_DEPCLOSURE` is valid only when `Case_QA.md` cites a follow-up DepClosure snapshot proving the SCC is absent or otherwise formally accepted by the owning reconciliation workflow.
