# TASK launch brief — cleanup refusal evidence remediation

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-02`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- PackageID: `PKG-09`; DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-bounded-implementation`; ApplyEdits: `true`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- Objective: fix only review-02 P2 so cleanup evidence truthfully records
  mutation refusal for every path where a loaded job's proof ownership cannot
  be established, including launchctl parse ambiguity and executable-inspection
  failure, while preserving the safe no-bootout behavior.
- AllowedWriteTargets:
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
  - this instance RETURN.md/STATUS.json
- Acceptance: remove message-prefix-dependent evidence classification; add
  focused regressions for parse and inspection failure showing no bootout and
  `jobMutationRefused: true`; preserve all existing 11 tests/safety behavior.
- Checks: syntax, focused Vitest, exact two-path containment.
- EXCLUSIONS: no other edit, live harness/host/LaunchAgent action, Git, scope
  expansion, lifecycle or proof claim.
- ExpectedReturn: exact fix, regression/check evidence, containment, and
  explicit unexecuted owner-gated proof state.
