# VERIFY-DEL-02-01 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted author candidate for App DEL-02-01 without repair.
RequestedBy: WORKING-A1-PKG02
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG02
ChildInstanceID: VERIFY-DEL-02-01
PackageID: APP-PKG-02
ManifestPackageID: PKG-02
DeliverableID: DEL-02-01
Dependency: manager-accepted terminal AUTHOR-DEL-02-01; candidate SHA-256 6e47e1c1e7528f13f8ed0240a9c3f1c425999d70b70ddb83a2c4a6dc9893e378

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-01/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-001, SOW-005
  PACKAGE_OBJECTIVE_REFS: OBJ-001
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-02-01 A1 manifest row and A1-B0 acceptance
  - exact nine source/status/control hashes in the manifest row
  - manager-accepted author candidate SHA-256 6e47e1c1e7528f13f8ed0240a9c3f1c425999d70b70ddb83a2c4a6dc9893e378

Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work files; do not delegate, contact author, or repair.
  - Reconstruct an isolated workspace from the exact live nine inputs and byte-identical accepted candidate at candidates/W_A1/APP-PKG02/DEL-02-01/ScopeOfWork.md. All inputs are read-only.
  - Reproduce live LEGACY_FOUR_DOC and isolated authorized MIGRATION_DUAL resolution, all identities, schema/map/parity/line coverage, checklist twice, render twice.
  - Independently inspect OUT-001/AC-001/VER-001 and transformed text for additions beyond the manifest row, deliverable identity, and legacy source; separately classify schema/content-authority/preservation/substrate.
  - Prove checklist/render stability/linkage/safety; run isolated partial and unauthorized-dual fail-closed fixtures.
  - Inventory/classify accepted machine-specific source/control and marker-bound candidate/render strings as PRESERVED_SOURCE_LITERAL. Do not normalize them. Require zero such strings in genuinely generated metadata/evidence outside explicit inventory.
  - Emit portable verifier evidence, exact five-path replacement manifest, complete reproducible MANIFEST.tsv, terminal run record, CHECKS.md, RETURN.md, STATUS.json only here. Fail on discrepancy; no candidate repair.

ExpectedOutputs:
  - independent evidence and terminal RETURN.md/STATUS.json
  - exact five-row replacement manifest and reproducible evidence manifest

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
