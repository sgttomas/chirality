# VERIFY-DEL-04-02 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted DEL-04-02 candidate without repair.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: VERIFY-DEL-04-02
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-02
Dependency: manager-accepted AUTHOR-DEL-04-02; candidate SHA-256 15796b93739a7a3481c288aafc8550baae34a440b159f4d80adbe7698c17428d

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-02/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-016, SOW-045, SOW-047, SOW-052
  PACKAGE_OBJECTIVE_REFS: OBJ-004, OBJ-005
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-04-02 A2 manifest row/W-A2 acceptance and manager-accepted candidate SHA above

Tasks:
  - Act as fresh Agent 2 TASK verifier; load complete TASK/scope-of-work/App contracts; do not delegate, contact author, or repair.
  - Reconstruct exact isolated live inputs plus accepted candidate; reproduce LEGACY_FOUR_DOC and authorized MIGRATION_DUAL, source/status/control identity, schema/map/parity/line coverage, checklist twice, render twice.
  - Independently inspect seed/transformed content authority; separately classify schema/content-authority/preservation/substrate; prove checklist/render linkage/stability/safety and partial/unauthorized-dual fail-closed fixtures.
  - Emit portable verifier evidence, exact five-path replacement, self-excluding reproducible MANIFEST, terminal run record/RETURN/STATUS only here. Candidate/project/author are read-only; fail without repair.

ExpectedOutputs:
  - independent terminal evidence/RETURN/STATUS; exact 5-row replacement; portable manifest

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
