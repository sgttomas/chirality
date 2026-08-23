# Task Management candidate — target-OS host-output fixtures

- Status: `HARVESTED ONLY`; no register row, owner disposition, schedule, or closure act.
- Source run: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- Candidate: every parser of host-tool output, including `launchctl`, `stat`, and `ps`, should be fixture-tested against captured output from the target operating-system version before a proof procedure is staged.
- Rationale: macOS 26.6.2 emits the valid launchd state `last exit code = (never exited)` for a job that started once and has not exited. The R19 proof harness lacked that target-OS fixture and rejected the healthy form during cleanup.
- Detection boundary: the R19 direct packaged-daemon precheck could not catch this defect because it starts the daemon directly and never routes through launchd or the `launchctl print` cleanup parser.
- Proposed owner triage: decide whether to establish a project-wide proof-staging gate requiring exact target-OS fixtures and malformed-form rejection tests for every consumed host-tool field.

This file is a candidate for later TASK_MANAGEMENT harvesting only. It does not amend any register or accepted workflow contract.
