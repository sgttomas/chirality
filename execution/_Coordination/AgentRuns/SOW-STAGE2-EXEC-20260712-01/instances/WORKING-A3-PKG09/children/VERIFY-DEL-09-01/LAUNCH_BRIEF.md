# VERIFY-DEL-09-01 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-09-01 candidate without repair.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: VERIFY-DEL-09-01
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-01
Dependency: accepted terminal AUTHOR-DEL-09-01-R1 plus manager mechanical manifest closeout; candidate SHA-256 8b77da5d79a8e3c165771c9bfb4971d5fd671c86ab664a4a9faa269142bb38c3
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-01/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-035, SOW-036
  PACKAGE_OBJECTIVE_REFS: OBJ-008
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-09-01 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced fresh author terminal status and exact accepted candidate hash above; predecessor normalization failure preserved and made no task/candidate/project writes
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Remove only workspace `.keep`; reconstruct isolated workspace from exact live source/control plus accepted candidate. Reproduce formats, identities, schema/map/parity/full line coverage, checklist twice, render twice, content authority, safety, and partial/unauthorized-dual fail-closed fixtures.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path future replacement manifest, complete reproducible MANIFEST.tsv, run record, evidence, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling write.
ExpectedOutputs:
  - independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return
EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
