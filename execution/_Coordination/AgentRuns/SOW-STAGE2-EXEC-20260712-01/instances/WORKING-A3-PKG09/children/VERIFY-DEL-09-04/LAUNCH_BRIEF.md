# VERIFY-DEL-09-04 Sealed TASK Brief — v1

PURPOSE: Fresh independent verification of accepted DEL-09-04 candidate without repair.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: VERIFY-DEL-09-04
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-04
Dependency: candidate d94f72590fef8b5863b195bcf2e7cf4c04d126ad026eaaaf1655e2ece119977a; author manifest 42 rows SHA 5a8706a7536a1a3d1a932cec35a175d8353f95ba5503aaaab12a6fd1d8747ec7.
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-04/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-04/**
RuntimeOverrides: {MODE: VERIFY, DELIVERABLE_PATH: "{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-04/workspace", DECOMPOSITION_BASIS: "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0", PROJECT_SCOPE_REFS: "SOW-030, SOW-072, SOW-073", PACKAGE_OBJECTIVE_REFS: "OBJ-008", FORMAT_AUTHORITY_REF: "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176", SOURCE_STATE: IN_PROGRESS, RENDER_HTML: true}
AcceptedBasis: accepted W-A3 exact row; main@193663b1d93299c18d64f59b543b36a0dd5f0ee1; reproduced author.
Tasks: Read TASK/skill; remove only .keep; reconstruct exact nine inputs+candidate; reproduce validation/map/parity 256 lines/checklist/render twice and fail-closed fixtures; emit exact five-row plan plus portable terminal evidence/self-excluding manifest immediately; no repair/delegation/candidate/project/Git/lifecycle/sibling writes.
EXCLUSIONS: all paths except this verifier subtree; H1/H2/ISSUED/release/retirement.
