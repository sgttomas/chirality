# VERIFY-DEL-04-05 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted DEL-04-05 candidate without repair.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: VERIFY-DEL-04-05
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-05
Dependency: accepted AUTHOR-DEL-04-05 candidate SHA-256 1095591a196fb61fbfbe30aaa779e3eaeba99c27c79864da428a74ac70c25157

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-019, SOW-020, SOW-021
  PACKAGE_OBJECTIVE_REFS: OBJ-004, OBJ-008
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

Tasks:
  - Fresh TASK verifier; load complete named contracts/A2 row; no delegation/contact/repair.
  - Reconstruct exact inputs/candidate; reproduce format/hashes/schema/map/parity/coverage, duplicate checklist/render, content authority, four verdicts, safety, partial + unauthorized-dual fail-closed, containment.
  - After PASS write terminal RETURN/STATUS/run-record first, then mechanically generate exact 5-row replacement and portable self-excluding manifest with terminal:true/manifest COMPLETE; exit immediately. Candidate/project/author read-only.

ExpectedOutputs:
  - independent portable verifier evidence/terminal files; exact replacement/manifest

EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
