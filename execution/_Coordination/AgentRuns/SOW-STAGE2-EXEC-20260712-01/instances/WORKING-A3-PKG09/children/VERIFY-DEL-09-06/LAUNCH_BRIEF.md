# VERIFY-DEL-09-06 Sealed TASK Brief — v1

PURPOSE: Fresh independent verification of accepted DEL-09-06 candidate without repair.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: VERIFY-DEL-09-06
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-06
Dependency: candidate 940a5b70a194c390909739f2a85ecdbe7856ee27483cfc24738146a2eb555e48; author manifest 43 rows SHA be1ae3466b0eee486f8178000363009dac83db0be0daab1097ea3f440aa0430d.
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-06/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-06/**
RuntimeOverrides: {MODE: VERIFY, DELIVERABLE_PATH: "{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-06/workspace", DECOMPOSITION_BASIS: "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0", PROJECT_SCOPE_REFS: "SOW-019, SOW-020, SOW-022, SOW-023", PACKAGE_OBJECTIVE_REFS: "OBJ-008", FORMAT_AUTHORITY_REF: "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176", SOURCE_STATE: IN_PROGRESS, RENDER_HTML: true}
AcceptedBasis: accepted W-A3 exact row; main@193663b1d93299c18d64f59b543b36a0dd5f0ee1; reproduced author.
Tasks: Read TASK/skill; remove only .keep; reconstruct exact nine inputs+candidate; reproduce validation/map/parity 305 lines/checklist/render twice and fail-closed fixtures; emit exact five-row plan plus portable terminal evidence/self-excluding manifest immediately; no repair/delegation/candidate/project/Git/lifecycle/sibling writes.
EXCLUSIONS: all paths except this verifier subtree; H1/H2/ISSUED/release/retirement.
