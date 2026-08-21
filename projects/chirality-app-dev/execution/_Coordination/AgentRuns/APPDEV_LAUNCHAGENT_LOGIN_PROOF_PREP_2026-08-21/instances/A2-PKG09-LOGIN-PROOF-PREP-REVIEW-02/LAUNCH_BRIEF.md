# TASK launch brief — fresh post-remediation login-proof review

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-02`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`; DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-code-review`; ApplyEdits: `false`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- ImplementationBrief: unchanged owner `PREPARE-THEN-OWNER` objective and
  acceptance criteria, plus exact remediation brief for review-01 P1 findings.
- AcceptedBasis: activation/amendments through 04; review-01 FAIL return;
  remediation-01 SUCCESS return; DEL-09-04 kit and R10/R11.
- DiffBasis: `FROZEN_PRODUCT_DIFF_02.md`; verify hashes and read 100% of both
  files as new against `/dev/null`.
- AllowedWriteTargets: none; only runtime RETURN.md/STATUS.json.
- VerificationEvidence: syntax PASS; focused Vitest 1 file / 11 tests PASS;
  exact two-path scope PASS.
- Review objective: fresh independent review of all prior acceptance and safety
  boundaries, with special regression focus on mandatory exact source revision
  and proof-ownership validation before every bootout.
- EXCLUSIONS: no edits, commands beyond read-only skill policy, live harness,
  LaunchAgent/host action, Git, scope expansion, lifecycle acceptance, or proof
  claim.
- ExpectedReturn: hash/scope/coverage evidence; exact actionable findings;
  residual risk; PASS only with zero actionable findings and explicit
  owner-gated/unexecuted on-host proof.
