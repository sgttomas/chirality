# VERIFY-DEL-02-05 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted DEL-02-05 candidate without repair.
RequestedBy: WORKING-A1-PKG02
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG02
ChildInstanceID: VERIFY-DEL-02-05
PackageID: APP-PKG-02
ManifestPackageID: PKG-02
DeliverableID: DEL-02-05
Dependency: manager-accepted terminal AUTHOR-DEL-02-05; candidate SHA-256 5b158b9ef5f6922abe8a56bf84b55dd6af55df42ea5546b4caa42d3487742446

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-05/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-05/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/VERIFY-DEL-02-05/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-013, SOW-019
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-008
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - exact DEL-02-05 A1 manifest row, its nine source/status/control hashes, A1-B0 acceptance, and candidate SHA above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work method files; do not delegate, contact author, or repair.
  - Reconstruct from exact live nine inputs plus byte-identical accepted candidate. Reproduce live LEGACY_FOUR_DOC and authorized isolated MIGRATION_DUAL, identities, schema/map/parity/line coverage, checklist twice, render twice, and conservative OUT/AC/VER authority.
  - Run partial and unauthorized-dual fail-closed fixtures; prove render/checklist stability and safety; separately classify schema/content-authority/preservation/substrate.
  - Preserve and inventory accepted source/control or marker-bound candidate/render absolute strings as PRESERVED_SOURCE_LITERAL; require portable generated metadata/evidence.
  - Emit exact five-path replacement manifest, complete reproducible MANIFEST.tsv, portable evidence, terminal run record, CHECKS.md, RETURN.md, STATUS.json only in this verifier scope.
ExpectedOutputs:
  - independent terminal verification package with exact five-row replacement and reproducible manifest
EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
