# VERIFY-DEL-03-03 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted author candidate for App DEL-03-03 without repair.
RequestedBy: WORKING-A1-PKG03
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG03
ChildInstanceID: VERIFY-DEL-03-03
PackageID: APP-PKG-03
ManifestPackageID: PKG-03
DeliverableID: DEL-03-03
Dependency: manager-accepted terminal AUTHOR-DEL-03-03; candidate SHA-256 9231e130a981f58a58bd1f0e87bab2dbc417f2121263e4aa425e2a40109e0d40

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG03/children/VERIFY-DEL-03-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG03/children/VERIFY-DEL-03-03/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG03/children/VERIFY-DEL-03-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-011, SOW-040
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-002
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-03-03 A1 manifest row and A1-B0 acceptance
  - exact source/status/control hashes in the frozen manifest row
  - manager-accepted author candidate SHA-256 9231e130a981f58a58bd1f0e87bab2dbc417f2121263e4aa425e2a40109e0d40

Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work files; do not delegate, contact author, or repair.
  - Reconstruct an isolated workspace from exact live source/control inputs and byte-identical candidate at candidates/W_A1/APP-PKG03/DEL-03-03/ScopeOfWork.md.
  - Reproduce live LEGACY_FOUR_DOC and authorized isolated MIGRATION_DUAL resolution, identity, schema/map/parity/line coverage, checklist twice, render twice.
  - Independently inspect OUT-001/AC-001/VER-001 and transformed text for additions beyond frozen scope/objectives, identity, and legacy source; separately classify schema/content-authority/preservation/substrate.
  - Prove checklist/render stability/linkage/safety; run isolated partial and unauthorized-dual fail-closed fixtures.
  - Inventory accepted machine-specific source/control and marker-bound candidate/render strings as PRESERVED_SOURCE_LITERAL; require zero in genuinely generated metadata/evidence.
  - Emit portable verifier evidence, exact five-path replacement manifest, reproducible MANIFEST.tsv, terminal run record, CHECKS.md, RETURN.md, STATUS.json only here. Avoid zsh special variable `path`. Fail on discrepancy; no candidate repair.

ExpectedOutputs:
  - independent evidence and terminal RETURN.md/STATUS.json
  - exact five-row replacement manifest and reproducible evidence MANIFEST.tsv

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation

