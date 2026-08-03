# A2 Implementation Brief Amendment 01 — Run-record containment

Status: `EFFECTIVE`

Date: `2026-08-02`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ChildInstanceID: `TASK-DAPP89-MIGRATION-01`

Reason: the TASK shell's default direct
`DEL-03-01/_run_records/TASK_RUN_*.md` location is not inside the narrower
activation write target. The parent activation authorizes only the named
nested run directory.

Effective clarification:

- All durable child run records must be written under
  `DEL-03-01/_run_records/APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02/**`.
- The direct untracked file
  `DEL-03-01/_run_records/TASK_RUN_2026-08-02_2305.md` is not accepted output.
  The child must stop writing it and leave cleanup to the manager.
- No objective, implementation path, test, acceptance criterion, or other
  authority changes.
- All remaining original brief fields and exclusions remain effective.
