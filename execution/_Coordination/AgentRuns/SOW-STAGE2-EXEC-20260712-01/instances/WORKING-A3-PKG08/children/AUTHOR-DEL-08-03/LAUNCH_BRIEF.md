# AUTHOR-DEL-08-03 Sealed TASK Brief — v1

PURPOSE: Create exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-08-03 with author evidence.
RequestedBy: WORKING-A3-PKG08
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG08
ChildInstanceID: AUTHOR-DEL-08-03
PackageID: APP-PKG-08
ManifestPackageID: PKG-08
DeliverableID: DEL-08-03
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/AUTHOR-DEL-08-03/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/AUTHOR-DEL-08-03/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A3/APP-PKG08/DEL-08-03/**
RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG08/children/AUTHOR-DEL-08-03/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-007, SOW-026
  PACKAGE_OBJECTIVE_REFS: OBJ-001, OBJ-007
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
AcceptedBasis:
  - synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1, evidence-only successor to row basis main@ff59428ff27d929bc1172e6c049a5e274d487fc0
  - accepted W-A3 preflight and exact DEL-08-03 A3_MANIFEST row, including every frozen hash/ref/path/dependency
Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate/contact siblings.
  - Confirm exact row; seed workspace with byte-equal four legacy files, _STATUS.md, _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, Dependencies.csv. Keep inputs exact.
  - Prove live LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live SOW. Convert first with package PKG-08 and exact authority. Ground OUT-001/AC-001/VER-001 only in SOW-007, SOW-026; OBJ-001, OBJ-007; identity; legacy source. Add nothing semantic.
  - Preserve markers; validate MIGRATION_DUAL; map/parity; checklist twice; render twice; negative fixtures; prove line/hash/target bindings, exactness/safety, separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact candidate ScopeOfWork.md to authorized candidate path. Write portable evidence, run record, RETURN.md, STATUS.json, reproducible MANIFEST.tsv. Preserve/inventory immutable source literals; never normalize source/candidate/render. Stop before after-the-fact evidence repair.
  - Fail on discrepancy. Never write projects, Git, lifecycle, sibling/package surfaces.
ExpectedOutputs:
  - exact candidate; complete author evidence/inventory/manifest; terminal return/status
EXCLUSIONS:
  - .claude-worktrees/**; projects/** writes; other candidates/packages/siblings; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement; delegation
