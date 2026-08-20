# INIT-TASK — integrated review remediation 01

PURPOSE: Close exactly integrated-review findings F1-F3 without changing product or rerunning host product proof.
RequestedBy: `WI-PKG09-API-KEY-PRECEDENCE-01`
RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
ParentInstanceID: `WI-PKG09-API-KEY-PRECEDENCE-01`
ChildInstanceID: `TASK-INTEGRATED-REMEDIATION-01`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}`
TaskSkill: `software-bounded-implementation`
PackageID: `PKG-09` integration remediation
DeliverableIDs: `DEL-09-06, DEL-09-04`
Objective: mechanically close F1 whitespace, calibrate the F2 REQ015 evidence citation, and persist normalized passing mise-Python evidence for F3.
AcceptedBasis: frozen review-01 identity `ee2623a620af684ed6b67a678466d46db186b4e590c9dd606f61542ff322acec`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: true

Tasks:
  - Read integrated Review 01 RETURN.md and touch only the exact targets below.
  - Remove the 15 trailing blanks identified by F1 without changing wording.
  - Amend DEL-09-06 REQ015 so compact summary binds artifact hashes/assertions/results while exact commands are cited to `TASK_RUN_2026-08-20_1630.md`.
  - Run `harness-pytest` and `harness-self-check` through `run_registered_checks.py` with PATH resolving `python3` to `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3`; persist normalized command/cwd/exit/duration/output JSON.
  - Run candidate-wide tracked-plus-untracked whitespace, JSON parse, exact-path containment, APP-HOLD reliance, and predecessor/product hash preservation checks.
  - Return exact before/after identities and confirm no product, test, state, compact proof, host artifact, or raw packaged-proof byte changed.

AllowedWriteTargets:
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/WORK_GRAPH.md`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/WORK_GRAPH_V2.md`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_VALIDATION_V2.md`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/RETURN_V2.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Assessment_INSP-03_DEL-09-06.md`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG09-API-KEY-PRECEDENCE-01/N3_MANAGER_REGISTERED_CHECKS.json`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-INTEGRATED-REMEDIATION-01/**`

AllowedTools:
  - `tools/software_workflow/run_registered_checks.py`
  - `tools/software_workflow/validate_change_scope.py`

AcceptanceCriteria:
  - Exact F1 locations contain no trailing blanks and the complete candidate has zero whitespace findings, including untracked paths.
  - F2 statement is factually supported by its exact citations.
  - Normalized JSON records PASS for 350 harness tests and root self-check exit 0 with exact command/cwd/duration/output.
  - Product/test hashes remain `d810b1ef...`, `c9cadac3...`, `3293cbf1...`, `818b7424...`; compact proof identities and raw host proof remain unchanged.
  - No product/host proof rerun, state/Remaining/lifecycle change, Git action, or scope violation.

ExpectedOutputs:
  - Six bounded evidence/control edits, normalized evidence JSON, final STATUS.json and RETURN.md.

CustomInstructions:
  - Agent 2 does not delegate.
  - Do not edit compact proof evidence, product/test, status/memory, run record, dependency, lockfile, SOW, receipt, completion log, or Git state.

EXCLUSIONS:
  - Product, host dist/proof reruns, release/lifecycle/Git actions, and all paths not explicitly listed.
