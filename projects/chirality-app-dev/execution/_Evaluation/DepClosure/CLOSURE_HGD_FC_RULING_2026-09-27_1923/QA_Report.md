# QA Report

- **Inventory and exemptions.** Unchanged from the 1739 snapshot: 54 workspace
  units, with DEL-00-01 and DEL-00-02 as CONTROL and DEL-09-07 as RETIRED.
- **Schema.** All 51 current registers are readable and schema-valid.
- **Declared entries.** There are none in scope.
- **Tool and inputs.** `Tool_Run.json` records the analyzer SHA-256, the exact
  arguments and the SHA-256 of every input. The inputs were hash-stable across
  both runs.
- **Comparison basis.** `adc8bdae1` holds the registers that the 1739 snapshot
  hashed. Only DEL-02-01's `Dependencies.csv` and `_DEPENDENCIES.md` differ
  from that commit.
- **Limits.** This snapshot is an observation, not an accepted basis.
