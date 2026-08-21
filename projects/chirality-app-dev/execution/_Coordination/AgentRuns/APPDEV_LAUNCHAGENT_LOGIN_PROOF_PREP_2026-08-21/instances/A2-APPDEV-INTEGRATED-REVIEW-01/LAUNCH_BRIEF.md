# TASK launch brief — fresh complete-tranche integrated review

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02` under Agent 0 direction
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-APPDEV-INTEGRATED-REVIEW-01`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID accepted by parent: `PKG-09`; cross-package PKG-08/TM surfaces are
  read-only integrated context and any finding on them is reported upward.
- TaskSkill: `software-code-review`; ApplyEdits: `false`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- DiffBasis: `INTEGRATED_DIFF_BASIS.md` plus current `git status`/tracked diff;
  review 100% of every current-tranche changed/untracked file except this
  reviewer's own RETURN/STATUS.
- AcceptedBasis: owner rulings, all App tranche coordination records, frozen
  diff 04, prior review/remediation chain, final registered JSON evidence, and
  PREPARATION_COMPLETE records.
- AllowedWriteTargets: none; runtime-owned RETURN.md/STATUS.json only.
- VerificationEvidence:
  `REGISTERED_CHECKS_FINAL.json`,
  `REGISTERED_CHECKS_FRONTEND_TEST_HOST.json`,
  `REGISTERED_CHECKS_PREMERGE_AGENT0.json`, focused 35/35 manager evidence,
  product hashes, APP-HOLD and TM check evidence.
- Review objective: complete integrated diff review for correctness, scope,
  consistency, security/fail-closed behavior, governance claim calibration,
  cross-surface owner-ruling fidelity, evidence accuracy, and check coverage.
- Required calibration: local premerge is not PASS; it is PR-CI-owned because
  the managed Next service was READY but shared runtime daemon/project
  registration were absent (HTTP 503). Local build/typecheck/full Vitest pass.
- EXCLUSIONS: no edits, setup/install, live harness, LaunchAgent/host action,
  Git/receipt/PR, root write, unrelated App mock, node_modules write, lifecycle,
  proof, publication, or delegation.
- ExpectedReturn: exact reviewed-path inventory, evidence/hash validation,
  actionable findings with exact locations, cross-package findings routed
  upward, residual risk, and terminal PASS only with zero actionable findings.
