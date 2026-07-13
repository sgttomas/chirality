# VERIFY-DEL-01-01 Sealed TASK Brief — v1

PURPOSE: Independently verify the accepted author candidate for App DEL-01-01 without repair.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: VERIFY-DEL-01-01
PackageID: APP-PKG-01
DeliverableID: DEL-01-01
Dependency: manager-accepted terminal AUTHOR-DEL-01-01 return and candidate hash

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-01/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-074, SOW-075
  PACKAGE_OBJECTIVE_REFS: OBJ-009
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-01-01 A1 manifest row and A1-B0 acceptance
  - exact nine manifest hashes stated in AUTHOR-DEL-01-01/LAUNCH_BRIEF.md
  - exact candidate hash recorded in manager-accepted author return

Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work files; do not delegate, contact author, or repair.
  - Confirm manager-seeded exact live sources/status/control plus byte-identical accepted candidate; all inputs read-only.
  - Reproduce live LEGACY_FOUR_DOC and isolated authorized MIGRATION_DUAL resolution, all identities, schema/map/parity/line coverage, checklist twice, render twice.
  - Independently inspect OUT-001/AC-001/VER-001 and transformed text for additions beyond row, identity, and legacy source; separately classify schema/content-authority/preservation/substrate.
  - Prove checklist/render stability/linkage/safety; run isolated partial and unauthorized-dual fail-closed fixtures.
  - Emit portable verifier evidence, exact five-path replacement manifest, run record, CHECKS.md, RETURN.md, STATUS.json only here. Fail on discrepancy; no repair.

ExpectedOutputs:
  - independent evidence and terminal RETURN.md/STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
