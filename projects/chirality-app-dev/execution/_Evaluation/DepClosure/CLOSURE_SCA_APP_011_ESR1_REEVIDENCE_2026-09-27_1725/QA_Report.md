# QA Report

- **Inventory and exemptions.** The same as the 1656 snapshot: 54 workspace
  units, with DEL-00-01 and DEL-00-02 as CONTROL and DEL-09-07 as RETIRED.
- **Schema.** All 51 current registers are readable and schema-valid.
- **Declared entries.** None exist in scope. The `declared_only`,
  `declared_disagreements` and `declared_unread` outputs are empty.
- **Tool and inputs.** `Tool_Run.json` records the analyzer SHA-256, the exact
  arguments and every input register and index with its SHA-256. The inputs
  were hash-stable across both runs.
- **Output paths.** Analyzer outputs use repository-relative paths and LF line
  endings.
- **Run order.** Documented in the report: one command regenerates all
  outputs, with the edge delta last.
- **Limits.**
  - This is an observation, not an accepted basis.
  - The four ESR-1 retire candidates are counted as ACTIVE until the owner
    decides.
