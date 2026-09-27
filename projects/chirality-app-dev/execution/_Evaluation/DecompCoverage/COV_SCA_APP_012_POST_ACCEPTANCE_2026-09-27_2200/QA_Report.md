# QA Report

- Inputs: decomposition `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577`; companion register `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`; `_LATEST.md` `3d7e0352b4ce271535d801d86706142481845227bdfe87f4693f1ce10bc95d8b`.
- Parser (heading-text binding): 10 package rows, 52 deliverable rows, 84 ledger rows, 10 objective rows.
- `tools/evaluation/audit_structure.py --root projects/chirality-app-dev/execution/ --variant SOFTWARE --inventory inventory.json --output structure.json`: exit 0; run_status COMPLETE; summary {'fail': 0, 'lifecycle_states': {'IN_PROGRESS': 53, 'OPEN': 1}, 'partitions': 11, 'pass': 54, 'production_formats': {'SOW_V1': 54}, 'units': 54}; issues ['partition directory contract is incomplete', 'required tool roots are missing'].
- `tools/scope_of_work/validate_scope_of_work.py` per physical deliverable folder: 54/54 pass.
- Artifact presence is a path and filename screen (backticked paths resolved against the App root, the frontend root and the repository root; otherwise at least two long tokens of the description in one file name in the deliverable folder). Absence of a match is not proof the behavior is absent.
- Limits: no semantic product verification; no file outside this snapshot folder was written; no decomposition, Scope of Work, dependency, lifecycle or pointer change. The DecompCoverage `_LATEST.md` pointer is not moved (not authorized by the brief).
- Reproducibility: this script is the SCA-APP-011 post-acceptance run script with its SCA-specific constants and texts updated; the checks are unchanged. The one checkout-dependent field, `basis_commit` in `coverage_summary.json`, is read from HEAD, so it matches only on the basis commit `bc1ea504d`.
