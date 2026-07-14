# VERIFY-DEL-09-03 Sealed TASK Brief — v1

PURPOSE: Fresh independent verification of accepted DEL-09-03 candidate without repair.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: VERIFY-DEL-09-03
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-03
Dependency: accepted AUTHOR-DEL-09-03 candidate 6b79194c67b73bbf85435ad5ceae221a68304c41f3294002825d4ad8917993a5; author manifest 42 rows SHA e38b9bf6b8baf9ee78ed0c53de4117a41c9dbf9674adf10e8cbfc038ac0df1db
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-03/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029
  PACKAGE_OBJECTIVE_REFS: OBJ-002, OBJ-003, OBJ-006, OBJ-008
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis: exact accepted W-A3 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1; reproduced author terminal/candidate/manifest.
Tasks:
  - Fresh Agent 2 verifier: read AGENT_TASK and scope-of-work files; remove only .keep; do not delegate/contact author/repair.
  - Reconstruct exact nine live inputs plus candidate; reproduce schema/map/parity/full 268-line coverage, checklist/render twice, content authority/safety, and partial/unauthorized-dual fail-closed fixtures.
  - Emit exact five-path plan, portable self-excluding manifest, run record, CHECKS, RETURN, terminal STATUS only here; terminalize immediately.
  - No candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence and exact five-row plan.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; all other subtrees; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
