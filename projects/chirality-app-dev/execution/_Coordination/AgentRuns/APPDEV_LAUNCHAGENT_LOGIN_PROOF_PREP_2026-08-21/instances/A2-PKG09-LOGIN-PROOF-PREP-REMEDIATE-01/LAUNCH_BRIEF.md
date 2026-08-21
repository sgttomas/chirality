# TASK launch brief — login-proof blocking review remediation

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-01`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- Objective: remediate exactly the two blocking P1 findings in review 01 while
  preserving every already-implemented prepare/capture safety boundary.
- AcceptedBasis: owner `PREPARE-THEN-OWNER`; activation and amendments 01-04;
  frozen diff 01; reviewer RETURN.md/STATUS.json; current two-file candidate.
- AllowedWriteTargets:
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
  - this child instance `RETURN.md` / `STATUS.json`
- Required remediation:
  1. Require a non-empty, non-placeholder source revision at prepare and ensure
     missing/placeholder/inconsistent source identity cannot reach capture
     `PASS`; add focused regressions.
  2. Before any `bootout`, prove the currently loaded same-label service is the
     prepared proof-owned exact program and argv (and executable identity where
     available). On missing/mismatched/ambiguous identity, fail closed without
     mutating that loaded job; bounded cleanup may remove only state proven
     proof-owned and must accurately record the residual. Add focused
     regressions demonstrating no bootout of an ambiguous service.
- Preserve: redacted public evidence, private one-shot capture binding, GUI
  session transition, stale/reuse rejection, exact cleanup containment,
  default/operator/launcher exclusion, no bootstrap/kickstart/logout/login.
- Checks: `node --check`, focused Vitest for this file, exact two-path scope
  validation. Do not invoke the live harness.
- EXCLUSIONS: no other edits, no host/LaunchAgent action, no default label/plist
  mutation, no launcher mutation, no root/piping/provider/network/release/Git
  expansion, no proof claim.
- ExpectedReturn: exact diff summary, regression evidence, check results,
  containment, residual risk, and explicit unexecuted owner-gated proof state.
