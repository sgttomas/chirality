# VERIFY-DEL-09-02 Sealed TASK Brief — v1

PURPOSE: Independently verify manager-accepted App DEL-09-02 candidate without repair.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: VERIFY-DEL-09-02
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-02
Dependency: accepted terminal AUTHOR-DEL-09-02 with manager evidence-only closeout; candidate SHA-256 c38c4fbe628b9f086cdc2be4e0cd9be6d86de0ee28b89c1b06a4d79cf49524c4; author manifest 39 rows SHA-256 741b679c83cb757a2ade2e36a207070d24554f393850ccf769a1fbfc48df579d
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-02/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/VERIFY-DEL-09-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063
  PACKAGE_OBJECTIVE_REFS: OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - accepted W-A3 preflight exact DEL-09-02 row; synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1
  - manager-reproduced author substantive PASS, terminal status/manifest and exact candidate hash above
Tasks:
  - Act as fresh Agent 2 TASK verifier; read complete AGENT_TASK and all scope-of-work files; do not delegate/contact author/repair.
  - Remove the workspace .keep anchor; reconstruct from exact live source/control plus accepted candidate. Independently reproduce identity, schema/map/parity/full 282-line coverage, checklist twice, render twice, content authority, safety, and partial/unauthorized-dual fail-closed fixtures.
  - Inventory immutable accepted literals; generated metadata must be portable. Emit exact five-path future replacement manifest and complete self-excluding MANIFEST.tsv plus run record, CHECKS.md, RETURN.md, terminal STATUS.json only here.
  - Terminalize immediately after checks; fail on discrepancy; no candidate/project/Git/lifecycle/package/sibling/author write.
ExpectedOutputs: independent terminal verifier evidence; exact five-row replacement manifest; reproducible manifest/status/return.
EXCLUSIONS: .claude-worktrees/**; projects/** writes; candidate/author/sibling/package writes; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
