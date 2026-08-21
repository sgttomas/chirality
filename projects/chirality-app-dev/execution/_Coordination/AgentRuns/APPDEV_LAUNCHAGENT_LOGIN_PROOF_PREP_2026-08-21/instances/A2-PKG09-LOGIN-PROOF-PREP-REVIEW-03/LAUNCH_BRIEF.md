# TASK launch brief — final fresh login-proof review

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-03`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`; DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-code-review`; ApplyEdits: `false`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- DiffBasis: `FROZEN_PRODUCT_DIFF_03.md`; verify hashes and read 100% of both
  full new files against `/dev/null`.
- AcceptedBasis: activation, amendments through 05, prior FAIL reviews and both
  successful remediation returns, DEL-09-04 kit, R10/R11.
- AllowedWriteTargets: none; runtime RETURN.md/STATUS.json only.
- VerificationEvidence: syntax PASS; focused Vitest 13/13 PASS; exact two-path
  scope PASS.
- Objective: final independent correctness/security/fail-closed review of all
  acceptance boundaries and every P1/P2 remediation, including truthful cleanup
  evidence for parse/inspection failure.
- EXCLUSIONS: no edits, live harness/LaunchAgent/host action, Git, scope
  expansion, lifecycle/proof claim, or delegation.
- ExpectedReturn: prompt terminal hash/scope/100%-coverage evidence; actionable
  findings or PASS only with zero findings; owner-gated proof boundary.
