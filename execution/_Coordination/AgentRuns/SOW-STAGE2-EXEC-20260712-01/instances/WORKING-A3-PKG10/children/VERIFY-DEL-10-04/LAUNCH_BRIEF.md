# VERIFY-DEL-10-04 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-10-04 candidate without repair.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: VERIFY-DEL-10-04
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-04
Dependency: accepted AUTHOR-DEL-10-04 manager evidence-only closeout; candidate SHA-256 13378ea31a55e2d425bd054391627c34094c2a0cab7556a801a683e400b70f3f; author manifest 39 rows including header SHA-256 99a17a042434ae2099389d1b457423fc1c3bf8a61e07f55f3b32c173e65574e2
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-04/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-04/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-04/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-070
  PACKAGE_OBJECTIVE_REFS: OBJ-010
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-10-04 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author substantive PASS and exact candidate/manifest above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; no delegation/contact/repair.
  - Remove only `.keep`; reconstruct exact live inputs plus candidate. Independently reproduce SOW_V1/authorized-dual validity, 34 mappings/309 lines, parity, checklist/render twice, content authority and fixture-vs-solver-truth safety, and correctly constructed partial/missing, unruled, and padded-authority fail-closed fixtures.
  - Confirm no solver certification/reliance, protected-path write, operation approval, lifecycle meaning, or semantic obligation beyond SOW-070/OBJ-010/exact source.
  - Preserve/inventory accepted literals; portable metadata. Emit exact five-path plan, self-excluding manifest, run record, CHECKS, RETURN, terminal STATUS only here.
  - Terminalize immediately; fail discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
