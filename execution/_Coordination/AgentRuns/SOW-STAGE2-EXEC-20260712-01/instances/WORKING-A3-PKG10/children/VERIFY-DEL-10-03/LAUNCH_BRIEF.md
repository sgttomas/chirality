# VERIFY-DEL-10-03 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-10-03 candidate without repair.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: VERIFY-DEL-10-03
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-03
Dependency: accepted AUTHOR-DEL-10-03 manager evidence-only closeout; candidate SHA-256 2f8abf603425a53161f41d0b67b9c590832af3daee97794de876430340c6b677; author self-excluding manifest 54 rows including header SHA-256 f15ccf3c49109e5838ee0174b158198a902e08ab97fbecb2657575b5fb89e3d8
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-03/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-069
  PACKAGE_OBJECTIVE_REFS: OBJ-010
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-10-03 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author substantive PASS and exact candidate/manifest above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; no delegation/contact/repair.
  - Remove only workspace `.keep`; reconstruct exact live source/control plus candidate. Independently reproduce standalone SOW_V1 and authorized MIGRATION_DUAL validity, 30 mappings/341 source lines, parity, checklist twice, render twice, content authority and proposal/human-gate/domain-boundary safety, and correctly constructed missing/unruled/padded-authority fixtures.
  - Confirm candidate adds no operation approval, protected-path mutation, solver reliance, lifecycle meaning, or semantic obligation beyond SOW-069/OBJ-010 and exact source.
  - Preserve/inventory immutable accepted literals; generated metadata portable. Emit exact five-path replacement manifest, self-excluding manifest, run record, CHECKS, RETURN, terminal STATUS only here.
  - Terminalize immediately; fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
