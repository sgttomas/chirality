# VERIFY-DEL-08-03 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-08-03 candidate without repair.
RequestedBy: WORKING-A3-PKG08
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG08
ChildInstanceID: VERIFY-DEL-08-03
PackageID: APP-PKG-08
ManifestPackageID: PKG-08
DeliverableID: DEL-08-03
Dependency: manager-reproduced terminal AUTHOR-DEL-08-03; candidate SHA-256 3c0f7e68aaebcb4a92c2a48e017c310277d353c7894db66fcd4faceb8d9305bd
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-03/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-007, SOW-026
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-007
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-08-03 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced 52-entry author manifest, terminal status, and candidate hash above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Reconstruct isolated workspace from exact live source/control plus accepted candidate. Reproduce formats, identities, schema/map/parity/full line coverage, checklist/render twice, conservative content authority, safety, containment, and partial/unauthorized-dual fail-closed fixtures.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path replacement manifest, complete self-excluding reproducible MANIFEST.tsv, run record, evidence, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling write.
ExpectedOutputs:
  - independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return
EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
