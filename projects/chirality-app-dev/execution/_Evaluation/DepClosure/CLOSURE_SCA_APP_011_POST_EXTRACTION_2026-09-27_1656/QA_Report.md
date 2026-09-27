# QA Report

- **Scope inventory.** The inventory was taken from the workspace folders:
  every `PKG-*/1_Working/DEL-*` directory, 54 units. That is the same basis as
  the 2026-09-22 snapshot. The App has no `_Decomposition/checkpoint_snapshots/_LATEST_ACCEPTED.md`,
  so the accepted decomposition's Deliverables section was used to classify the
  retired unit.
- **Exemptions.** There are three:
  - DEL-00-01 (CONTROL);
  - DEL-00-02 (CONTROL);
  - DEL-09-07 (RETIRED).

  Each is reported with its authority in `Brief.md`. None is counted as FAIL
  or BLOCKER in the current conclusion.
- **Schema.** All 51 current registers are readable and schema-valid. In the
  ALL census, the two CONTROL units have no `Dependencies.csv` by design.
- **Declared entries.** `declared_only`, `declared_disagreements` and
  `declared_unread` are empty. No in-scope `_DEPENDENCIES.md` carries a SPEC
  §5.2 declared entry.
- **Tool and inputs.** `Tool_Run.json` records the analyzer path and SHA-256,
  the exact arguments and every input with its SHA-256. It also records that
  the inputs were hash-stable across both runs.
- **Output paths.** Analyzer outputs had absolute workspace paths replaced by
  repository-relative ones. Line endings are normalized to LF.
- **Limits.**
  - This is an observation of recorded registers, not an accepted project
    basis.
  - Topology alone does not establish readiness.
  - The eight held edges (ESR-1) are counted as ACTIVE until the owner
    decides.
