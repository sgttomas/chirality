# BRIEF SCHEMA — scc-resolution-case

Use this workflow when WORKING_ITEMS needs to create or update an SCC case in the project's case home: `{EXECUTION_ROOT}/_DAG/cases/<CASE-ID>/` by default, or a legacy PKG-00 control deliverable that already holds the project's cases.

## Required Fields

```yaml
PURPOSE: Create or update one SCC resolution case.
RequestedBy: WORKING_ITEMS
ScopePath: /abs/path/to/execution/_DAG/cases/SCC-CASE-001
Workflow: scc-resolution-case
ApplyEdits: true
AllowedWriteTargets:
  - /abs/path/to/execution/_DAG/cases/SCC-CASE-001/
RuntimeOverrides:
  CASE_ID: SCC-CASE-001
  CASE_PATH: /abs/path/to/execution/_DAG/cases/SCC-CASE-001
  CASE_TITLE: PKG-10 Policy Proposal cycle
  SCC_ID: SCC-002
  DEPCLOSURE_SNAPSHOT: /abs/path/to/execution/_Reconciliation/DepClosure/CLOSURE_...
  AFFECTED_DELIVERABLES: DEL-10-02;DEL-10-03
  CASE_STATE: OPEN_FOR_TASK_WORK
ExpectedOutputs:
  - Case_Contract.md
  - Case_Datasheet.md
  - Task_Findings.csv
  - Evidence_Register.csv
  - Candidate_Remedies.csv
  - Ruling_Register.csv
  - Open_Questions.md
  - Owner_Workflow_Handoff.md
  - Case_QA.md
```

`CASE_ID` is the stable case identity (`SCC-CASE-NNN`, the next unused number
in the case home when the case opens); `SCC_ID` is the positional ID in
`DEPCLOSURE_SNAPSHOT` and may differ in a later snapshot. To open a case,
`ScopePath` may be `{EXECUTION_ROOT}/_DAG/cases/`; `AllowedWriteTargets` is
still the case folder, and run records go to `{CASE_PATH}/_run_records/`, not
`_DAG/cases/_run_records/`.

For the legacy home, `ScopePath` is the PKG-00 control deliverable folder, and
`AllowedWriteTargets` are `{control-deliverable}/scc-cases/<case-folder>/` and
`{control-deliverable}/_run_records/`.

## Optional Runtime Overrides

- `SEED_PACKET_PATHS` — semicolon-separated paths to prior packets to preserve under `case-seeds/`.
- `SCC_NODE_SET` — semicolon-separated SCC member node set; read from `DEPCLOSURE_SNAPSHOT` when absent. It is recorded in `Case_Datasheet.md` and used to match later closure snapshots to the case.
- `FOCUS_PAIRS` — semicolon-separated bidirectional pairs.

## Required Custom Instructions

- Treat existing scope-change packets as seed evidence, not active WORKING_ITEMS (workflow: scope-change) intake.
- Do not edit product deliverables, dependency registers, decomposition files, `_ScopeChange/`, or `_Reconciliation/`.
- Do not report SCC closure or project-wide blocked/unblocked status.
