# QA Report

- **Inventory and exemptions.** Unchanged from the 1923 snapshot: 54 workspace
  units, with DEL-00-01 and DEL-00-02 as CONTROL and DEL-09-07 as RETIRED.
- **Schema.** All 51 current registers are readable and schema-valid.
- **Declared entries.** There are none in scope.
- **Tool and inputs.** `Tool_Run.json` records the analyzer SHA-256, the exact
  arguments and the SHA-256 of every input. The inputs were hash-stable across
  both runs.
- **Comparison basis.** `63e5de1f2` holds the registers that the 1923 snapshot
  hashed. Against that commit, only the `Dependencies.csv` of DEL-02-03,
  DEL-08-03, DEL-05-03, DEL-06-01, DEL-06-02 and DEL-09-04 and the 24 refreshed
  `_DEPENDENCIES.md` differ.
- **Limits.** This snapshot is an observation, not an accepted basis.
