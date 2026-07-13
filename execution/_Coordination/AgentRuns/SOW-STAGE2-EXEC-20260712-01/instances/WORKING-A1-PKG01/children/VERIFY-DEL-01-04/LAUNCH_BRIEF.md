# VERIFY-DEL-01-04 Sealed TASK Brief — v1

PURPOSE: Independently verify the accepted author candidate for App DEL-01-04 without repair.
RequestedBy: WORKING-A1-PKG01
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG01
ChildInstanceID: VERIFY-DEL-01-04
PackageID: APP-PKG-01
DeliverableID: DEL-01-04
Dependency: manager-accepted terminal AUTHOR-DEL-01-04 return and candidate hash

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-04/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-04/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG01/children/VERIFY-DEL-01-04/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-065, SOW-076, SOW-077, SOW-078
  PACKAGE_OBJECTIVE_REFS: OBJ-009
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-01-04 A1 manifest row and A1-B0 acceptance
  - exact nine manifest hashes stated in AUTHOR-DEL-01-04/LAUNCH_BRIEF.md
  - exact candidate hash recorded in manager-accepted author return

Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work files; do not delegate, contact author, or repair.
  - Confirm exact read-only seeded sources/status/control and accepted candidate; reproduce live/dual formats, identities, schema/map/parity/coverage, checklist twice, render twice.
  - Independently inspect all transformed text and seed IDs for unauthorized additions; separately classify schema/content-authority/preservation/substrate.
  - Prove checklist/render stability/linkage/safety and partial/unauthorized-dual fail-closed fixtures.
  - Emit portable evidence, exact five-path replacement manifest, run record, CHECKS.md, RETURN.md, STATUS.json only here. Fail on discrepancy; no repair.

ExpectedOutputs:
  - independent evidence and terminal RETURN.md/STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
