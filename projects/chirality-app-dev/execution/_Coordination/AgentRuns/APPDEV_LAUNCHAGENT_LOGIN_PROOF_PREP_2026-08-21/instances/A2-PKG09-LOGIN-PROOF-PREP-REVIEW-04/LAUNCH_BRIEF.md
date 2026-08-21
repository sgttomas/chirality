# TASK launch brief — final fresh full-diff review 04

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-04`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- PackageID: `PKG-09`; DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-code-review`; ApplyEdits: `false`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- DiffBasis: `FROZEN_PRODUCT_DIFF_04.md`, full files new against `/dev/null`.
- AcceptedBasis: all activation/amendment/review/remediation records through 06,
  DEL-09-04 kit and R10/R11.
- AllowedWriteTargets: none; runtime RETURN/STATUS only.
- VerificationEvidence: syntax PASS; focused Vitest 15/15 PASS; exact scope PASS.
- Objective: final 100% independent review of all functional/security/fail-closed
  boundaries and P1/P2 fixes, especially install-attempt failure cleanup and
  truthful residual evidence.
- EXCLUSIONS: no edits, live harness/host/LaunchAgent, Git, scope expansion,
  proof/lifecycle claim, unregistered commands, or delegation.
- ExpectedReturn: terminal promptly after hash/scope/100% review; PASS only with
  zero actionable findings; owner proof remains unexecuted.
