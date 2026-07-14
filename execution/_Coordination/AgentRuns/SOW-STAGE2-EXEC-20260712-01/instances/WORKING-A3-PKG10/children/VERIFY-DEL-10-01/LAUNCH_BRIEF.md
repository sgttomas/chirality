# VERIFY-DEL-10-01 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-10-01 candidate without repair.
RequestedBy: WORKING-A3-PKG10
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG10
ChildInstanceID: VERIFY-DEL-10-01
PackageID: APP-PKG-10
ManifestPackageID: PKG-10
DeliverableID: DEL-10-01
Dependency: accepted terminal AUTHOR-DEL-10-01 with manager evidence-only closeout; candidate SHA-256 2947f62aea6f7fe9b63708a713fa3cc769687cedb23a50507b07dc14e7579871; author manifest 30 rows including header SHA-256 eedf066006d0f0fe892a29a4b7db65b89ca6c34195e1ce2697a44ec6c3700a4b
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-01/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG10/children/VERIFY-DEL-10-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-066, SOW-067
  PACKAGE_OBJECTIVE_REFS: OBJ-010
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-10-01 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author substantive PASS, terminal status/manifest and exact candidate hash above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Remove only the workspace `.keep` anchor; reconstruct from exact live source/control plus accepted candidate. Independently reproduce identity, valid authorized MIGRATION_DUAL schema, map/parity/full 369-line coverage, checklist twice, render twice, content authority and domain-boundary safety, and missing/unruled/padded-authority fail-closed fixtures.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path future replacement manifest and complete self-excluding MANIFEST.tsv plus run record, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Terminalize immediately after checks; fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
