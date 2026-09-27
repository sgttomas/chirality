# QA Report

- **Inventory and exemptions.** Unchanged from the 2234 snapshot: 54 workspace
  units, with DEL-00-01 and DEL-00-02 as CONTROL and DEL-09-07 as RETIRED.
- **Schema.** All 51 current registers are readable and schema-valid.
- **Declared entries.** There are none in scope.
- **Tool and inputs.** `Tool_Run.json` records the analyzer SHA-256, the exact
  arguments and the SHA-256 of every input. The inputs were hash-stable across
  both runs. Against 2234's `accepted_input_basis`, only the DEL-05-03 and
  DEL-06-01 `_DEPENDENCIES.md` hashes differ.
- **Evidence.** Apart from the prior-summary basis and the zero deltas in
  `closure_summary.json` and `analyzer_stdout.json`, every `Evidence/` file is
  byte-identical to 2234's, including `edge_delta.csv`.
- **Output paths.** Outputs use repository-relative paths and LF line endings.
- **Reproducibility.** A rerun of `closure_run.py` reproduces this snapshot
  byte-for-byte.
- **Limits.** This snapshot is an observation, not an accepted basis.
