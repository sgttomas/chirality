# VERIFY-DEL-04-03 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted DEL-04-03 candidate without repair.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: VERIFY-DEL-04-03
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-03
Dependency: accepted AUTHOR-DEL-04-03 candidate SHA-256 72c083f28a597583abf1b6e950f0ce0965221f9cd2fee0233408954336aaa100

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-040, SOW-044, SOW-051
  PACKAGE_OBJECTIVE_REFS: OBJ-002, OBJ-004
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

Tasks:
  - Fresh Agent 2 TASK verifier: load complete TASK/scope-of-work/App/A2 contracts; no delegation, author contact, or repair.
  - Reconstruct exact inputs/candidate; reproduce formats/hashes, schema/map/parity/coverage, duplicate checklist/render, seed/content authority, separate schema/content-authority/preservation/substrate, safety, partial and unauthorized-dual fail-closed fixtures.
  - Immediately after PASS, emit exact five-path replacement, portable self-excluding MANIFEST, terminal run-record/RETURN/STATUS and exit; do not linger in narrative. Candidate/project/author are read-only.

ExpectedOutputs:
  - portable independent verifier evidence/manifest/terminal files; exact 5-row replacement

EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
