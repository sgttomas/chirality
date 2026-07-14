# VERIFY-DEL-08-02 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-08-02 candidate without repair.
RequestedBy: WORKING-A3-PKG08
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG08
ChildInstanceID: VERIFY-DEL-08-02
PackageID: APP-PKG-08
ManifestPackageID: PKG-08
DeliverableID: DEL-08-02
Dependency: accepted terminal AUTHOR-DEL-08-02; candidate SHA-256 4d5b3d296511edf1285bc953fe6777c439585e2a0be74121fe282e39a4626550
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-02/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/VERIFY-DEL-08-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-005, SOW-006, SOW-017
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-007
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-08-02 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author terminal status/manifest and exact accepted candidate hash above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Reconstruct isolated workspace from exact live source/control plus accepted candidate. Reproduce formats, identities, schema/map/parity/full line coverage, checklist twice, render twice, content authority, safety, and partial/unauthorized-dual fail-closed fixtures.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path future replacement manifest, complete reproducible MANIFEST.tsv, run record, evidence, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling write.
ExpectedOutputs:
  - independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return
EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
