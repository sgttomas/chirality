# VERIFY-DEL-02-03 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted DEL-02-03 candidate without repair.
RequestedBy: WORKING-A1-PKG02
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG02
ChildInstanceID: VERIFY-DEL-02-03
PackageID: APP-PKG-02
ManifestPackageID: PKG-02
DeliverableID: DEL-02-03
Dependency: manager-accepted terminal AUTHOR-DEL-02-03; candidate SHA-256 090a041bfda14f2ff1397378d74c79e9b394d4986bc3356a6e5243547d90f173

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-03/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-002, SOW-003
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-006
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - exact DEL-02-03 A1 manifest row, its nine source/status/control hashes, A1-B0 acceptance, and candidate SHA above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work method files; do not delegate, contact author, or repair.
  - Reconstruct from exact live nine inputs plus byte-identical accepted candidate. Reproduce live LEGACY_FOUR_DOC and authorized isolated MIGRATION_DUAL, identities, schema/map/parity/line coverage, checklist twice, render twice, and conservative OUT/AC/VER authority.
  - Run partial and unauthorized-dual fail-closed fixtures; prove render/checklist stability and safety; separately classify schema/content-authority/preservation/substrate.
  - Preserve and inventory machine-specific accepted source/control or marker-bound candidate/render strings as PRESERVED_SOURCE_LITERAL; require portable generated metadata/evidence.
  - Emit exact five-path replacement manifest, complete reproducible MANIFEST.tsv, portable evidence, terminal run record, CHECKS.md, RETURN.md, STATUS.json only in this verifier scope.
ExpectedOutputs:
  - independent terminal verification package with exact five-row replacement and reproducible manifest
EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
