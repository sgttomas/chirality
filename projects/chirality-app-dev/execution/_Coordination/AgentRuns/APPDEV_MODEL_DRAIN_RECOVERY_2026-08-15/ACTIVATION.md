# WORKING_ITEMS activation — PKG-03 model-drain recovery proof

- RunID: `APPDEV_MODEL_DRAIN_RECOVERY_2026-08-15`
- InstanceID: `WI-PKG03-MODEL-DRAIN`
- PackageID: `PKG-03`
- Selected deliverable: `DEL-03-04`
- Objective: add an App-owned integration case that arms an in-flight model drain, restarts the shared runtime daemon through public seams, and proves exactly one durable terminal outcome.
- Accepted basis: branch `codex/app-dev-model-drain-recovery` at `910c02129811a005da9b180c31e3c18dd365df6f`; Receipt 165 validated by the supervising run; authority corpus v18, App status, dependency DAG, and decision register reported clean. This package run independently passed the `DEL-03-04` APP-HOLD-1 dispatch preflight.
- Profile: `projects/chirality-app-dev/software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- Write boundary: `projects/chirality-app-dev/frontend/**`, selected-deliverable `_STATUS.md`, `MEMORY.md`, one minimal deliverable `_run_records/**` file, and this managed run root.
- Exclusions: root `runtime/**` is read-only; no PKG-09, `_DomainEngines`, decisions, receipts, release, issuance, provider, network, or lifecycle-state changes; no Git closeout.
