# QA Report

- **Inventory and exemptions.** The same as the earlier snapshots: 54
  workspace units, with DEL-00-01 and DEL-00-02 as CONTROL and DEL-09-07 as
  RETIRED.
- **Schema.** All 51 current registers are readable and schema-valid.
- **Declared entries.** None exist in scope.
- **Tool and inputs.** `Tool_Run.json` records the analyzer SHA-256, the exact
  arguments and every input with its SHA-256. The inputs were hash-stable
  across both runs.
- **Comparison basis.** The 1725 snapshot's 106 input hashes match the
  registers and indexes at commit `1485271da`. So `edge_delta.csv` against that
  commit is the delta against 1725.
- **Limits.** This is an observation, not an accepted basis.
