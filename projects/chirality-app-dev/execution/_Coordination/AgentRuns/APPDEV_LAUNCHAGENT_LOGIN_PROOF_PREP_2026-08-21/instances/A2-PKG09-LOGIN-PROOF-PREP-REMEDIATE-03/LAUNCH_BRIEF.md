# TASK launch brief — prepare failure cleanup remediation

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-03`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- PackageID: `PKG-09`; DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-bounded-implementation`; ApplyEdits: `true`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- Objective: remediate only REVIEW-03 P1 so every install-attempt failure,
  including timeout after side effects and later validation rejection, performs
  bounded identity-gated cleanup of proof-owned state and surfaces accurate
  cleanup/residual evidence rather than silently leaving login-autostart state.
- AllowedWriteTargets: exact login-proof script, exact focused test, and this
  instance RETURN/STATUS only.
- Acceptance: set cleanup responsibility before invoking CLI; never bootout an
  ambiguous job; inspect possible plist/runtime side effects; report cleanup
  outcome/residuals on failure; add timeout-after-plist-write and post-install
  validation-failure regressions; preserve prior 13 tests and all fences.
- Checks: syntax, focused Vitest, exact two-path scope.
- EXCLUSIONS: no live harness/host/LaunchAgent, no other edits, Git, scope
  expansion, proof/lifecycle claim.
- ExpectedReturn: minimal fix, focused regressions/checks, containment, and
  owner-gated proof boundary.
