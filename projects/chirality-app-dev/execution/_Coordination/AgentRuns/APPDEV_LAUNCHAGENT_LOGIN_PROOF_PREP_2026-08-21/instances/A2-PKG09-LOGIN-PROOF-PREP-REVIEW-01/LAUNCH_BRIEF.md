# TASK launch brief — fresh login-proof product review

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-01`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-code-review`
- ApplyEdits: `false`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- ImplementationBrief: owner `PREPARE-THEN-OWNER` ruling and the unchanged
  acceptance criteria in IMPLEMENT-03 launch brief; implementation was returned
  by fresh direct bounded Agent 2 `/root/login_proof_direct_fix`.
- AcceptedBasis: D-APP-97 C1; DEL-09-04 live kit/state; R10/R11; existing
  packaged RunAtLoad proof; manager takeover/work-graph amendments; direct
  child terminal return relayed by Agent 0.
- DiffBasis: `FROZEN_PRODUCT_DIFF_01.md`; both candidate files are new against
  `/dev/null`. Read every line of both files and verify the recorded SHA-256
  before review.
- AllowedWriteTargets: none. Runtime-owned `RETURN.md` / `STATUS.json` are the
  only durable reviewer records.
- VerificationEvidence: manager-reproduced `node --check` PASS; focused Vitest
  1 file / 7 tests PASS; deterministic exact two-path scope validation PASS.
- Review objective: review 100% of the frozen product/test diff for correctness,
  regressions, fail-closed safety, default/operator isolation, stale/ambiguous
  evidence rejection, exact login-session/job/process/executable/source binding,
  redaction, bounded proof-only cleanup, and adequate tests.
- Required boundary checks: preparation must not prove or perform logout/login;
  prepare/capture must contain no bootstrap/kickstart; the default label/plist
  and CLI launcher are never mutated; unsafe cleanup paths or missing identity
  evidence fail closed; evidence contains no private host paths.
- EXCLUSIONS: no edits, no live harness/LaunchAgent invocation, no host action,
  no Git, no root/piping/provider/network/release expansion, no lifecycle or
  proof acceptance.
- ExpectedReturn: hash verification; scope/evidence audit; actionable findings
  with exact locations and severity; residual risks; terminal `PASS` only with
  zero actionable findings and explicit statement that on-host proof remains
  unexecuted and owner-gated.
