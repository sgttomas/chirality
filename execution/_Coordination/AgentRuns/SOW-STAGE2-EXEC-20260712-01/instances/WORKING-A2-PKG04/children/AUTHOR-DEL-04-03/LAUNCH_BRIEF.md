# AUTHOR-DEL-04-03 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-04-03 and complete author evidence.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: AUTHOR-DEL-04-03
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-03

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-03/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG04/DEL-04-03/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/AUTHOR-DEL-04-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-040, SOW-044, SOW-051
  PACKAGE_OBJECTIVE_REFS: OBJ-002, OBJ-004
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - synchronized main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa and exact DEL-04-03 A2 manifest row/W-A2 acceptance

Tasks:
  - Act strictly as Agent 2 TASK; load complete TASK/scope-of-work/App contracts; do not delegate/contact siblings.
  - Confirm exact frozen row; seed byte-equal legacy/control inputs; resolve LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, zero live SOW.
  - Converter first using PKG-04. Ground OUT-001/AC-001/VER-001 only in SOW-040/SOW-044/SOW-051, OBJ-002/OBJ-004, identity and source; add no semantic scope.
  - Preserve markers; validate authorized MIGRATION_DUAL; map/parity; duplicate checklist/render; prove complete disposition/bindings/safety and separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact candidate ScopeOfWork.md. Emit portable evidence, self-excluding manifest, terminal run record/RETURN/STATUS. Inventory preserved literals; never normalize source/candidate/render; stop before evidence repair. Fail on discrepancy; no project/Git/lifecycle write.

ExpectedOutputs:
  - exact DEL-04-03 candidate; portable author evidence/manifest; terminal RETURN/STATUS

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; other candidate/package/sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
