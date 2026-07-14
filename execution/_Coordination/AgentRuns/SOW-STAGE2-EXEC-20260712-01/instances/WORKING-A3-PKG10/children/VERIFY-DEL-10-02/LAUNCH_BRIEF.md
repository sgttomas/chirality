# VERIFY-DEL-10-02 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-10-02 candidate without repair.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: VERIFY-DEL-10-02
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-02
Dependency: accepted terminal AUTHOR-DEL-10-02; candidate SHA-256 204721c5221d1311ff94c93fa60ff3292d715ad2ab146032c7d6ba71f85582bb; author self-excluding manifest 56 rows including header SHA-256 2628a1ef582bc343d5edce52635a5e5e8c22300792fc7823ecd036775fe0f0be
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-02/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-068
  PACKAGE_OBJECTIVE_REFS: OBJ-010
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-10-02 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced terminal author evidence and exact candidate/manifest hashes above; malformed initial author fixture is preserved evidence but not a negative PASS
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Remove only workspace `.keep`; reconstruct from exact live source/control plus accepted candidate. Independently reproduce identity, standalone SOW_V1 and authorized MIGRATION_DUAL validation, map/parity full 282-line coverage, checklist twice, render twice, content authority/protected-path safety, and correctly constructed missing/unruled/padded-authority fail-closed fixtures.
  - Confirm candidate adds no protected-path write, proposal approval, operation authority, lifecycle meaning, or semantic obligation beyond SOW-068/OBJ-010 and exact source.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path future replacement manifest and complete self-excluding MANIFEST.tsv plus run record, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Terminalize immediately; fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
