# VERIFY-DEL-10-05 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-10-05 candidate without repair.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: VERIFY-DEL-10-05
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-05
Dependency: accepted AUTHOR-DEL-10-05 manager evidence-only closeout; candidate SHA-256 0761ab08daee0d87e69b6efad3216e5228e34be8207a1483e335bfbb237e2c9a; author manifest 58 rows incl header SHA-256 2b03238c8c40a9c1241264ac5093243432ad4df34580968b88601304584c74c9
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-05/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-05/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-05/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-071
  PACKAGE_OBJECTIVE_REFS: OBJ-009, OBJ-010
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-10-05 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author PASS and exact candidate/manifest; preserved pre-copy non-acceptance attempt and two immutable accepted literal classifications
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; no delegation/contact/repair.
  - Remove only `.keep`; reconstruct exact live inputs plus candidate. Independently reproduce standalone/dual validity, 36 mappings/318 lines, parity, checklist/render twice, domain notices/proposal/solver-truth authority, and correctly constructed missing/unruled/padded-authority fail-closed fixtures.
  - Confirm no solver reliance/certification, protected-path mutation, operation approval, lifecycle meaning, or semantic obligation beyond SOW-071/OBJ-009/OBJ-010/exact source.
  - Preserve and inventory the two immutable accepted `_DEPENDENCIES.md` checkout literals; portable generated metadata. Emit exact five-path plan, self-excluding manifest, run record, CHECKS, RETURN, terminal STATUS only here.
  - Terminalize immediately; fail discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
