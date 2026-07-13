# VERIFY-DEL-04-04 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted DEL-04-04 candidate without repair.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: VERIFY-DEL-04-04
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-04
Dependency: accepted AUTHOR-DEL-04-04 candidate SHA-256 9d7a5de67db2b656f86246b1f2f466862ae60e53102d011be6910555afab15b6; terminal metadata repair closed at manifest ba356a74616d659e4b566804a9d8a03b2a0ef6525502d4d37804dd72724c3c2b

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-017, SOW-030
  PACKAGE_OBJECTIVE_REFS: OBJ-004, OBJ-007
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

Tasks:
  - Fresh TASK verifier; load complete named contracts/A2 row; no delegation/author contact/repair.
  - Reconstruct exact inputs/candidate; reproduce format/hashes/schema/map/parity/coverage, duplicate checklist/render, content authority, four separate verdicts, safety, partial + unauthorized-dual fail-closed, containment.
  - After PASS, first write terminal RETURN/STATUS/run-record, then mechanically generate exact five-row replacement and portable self-excluding MANIFEST; require status terminal:true and manifest COMPLETE; exit immediately. Candidate/project/author read-only.

ExpectedOutputs:
  - independent portable evidence/terminal files; exact 5-row replacement; self-excluding manifest

EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
