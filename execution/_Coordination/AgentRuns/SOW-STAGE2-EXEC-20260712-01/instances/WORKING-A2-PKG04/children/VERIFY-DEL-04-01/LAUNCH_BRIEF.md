# VERIFY-DEL-04-01 Sealed TASK Brief — v1

PURPOSE: Independently verify the manager-accepted author candidate for App DEL-04-01 without repair.
RequestedBy: WORKING-A2-PKG04
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A2-PKG04
ChildInstanceID: VERIFY-DEL-04-01
PackageID: APP-PKG-04
ManifestPackageID: PKG-04
DeliverableID: DEL-04-01
Dependency: manager-accepted terminal AUTHOR-DEL-04-01; candidate SHA-256 45157c90dfbb088b522d8299d5b9df5c06acb04dd61bc7c6610ff9c33685cd75

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-01/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-018, SOW-044, SOW-046
  PACKAGE_OBJECTIVE_REFS: OBJ-004
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-04-01 A2 manifest row and W-A2-B0 acceptance
  - exact source/status/control hashes in the frozen manifest row
  - manager-accepted terminal author candidate SHA-256 45157c90dfbb088b522d8299d5b9df5c06acb04dd61bc7c6610ff9c33685cd75

Tasks:
  - Act as fresh Agent 2 TASK verifier; read AGENT_TASK and all scope-of-work files; do not delegate, contact author, or repair.
  - Reconstruct an isolated workspace from exact live source/control inputs and byte-identical accepted candidate at candidates/W_A2/APP-PKG04/DEL-04-01/ScopeOfWork.md. Inputs are read-only.
  - Reproduce live LEGACY_FOUR_DOC and authorized isolated MIGRATION_DUAL resolution, all identities, schema/map/parity/line coverage, checklist twice, render twice.
  - Independently inspect OUT-001/AC-001/VER-001 and transformed text for additions beyond the manifest row, deliverable identity, and legacy source; separately classify schema/content-authority/preservation/substrate.
  - Prove checklist/render stability/linkage/safety; run isolated partial and unauthorized-dual fail-closed fixtures.
  - Inventory/classify accepted machine-specific source/control and marker-bound candidate/render strings as PRESERVED_SOURCE_LITERAL. Do not normalize them. Require zero such strings in genuinely generated metadata/evidence outside explicit inventory.
  - Emit portable verifier evidence, exact five-path replacement manifest, complete reproducible MANIFEST.tsv, terminal run record, CHECKS.md, RETURN.md, STATUS.json only here. Fail on discrepancy; no candidate repair.

ExpectedOutputs:
  - independent evidence and terminal RETURN.md/STATUS.json
  - exact five-row replacement manifest and reproducible evidence MANIFEST.tsv

EXCLUSIONS:
  - .claude-worktrees/**; every projects/** write; candidate/author/sibling/package writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
