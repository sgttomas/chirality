PURPOSE: Convert DEL-05-01 legacy four-document scope into one isolated SOW_V1 candidate without changing accepted project state.
RequestedBy: WORKING-A2-PKG05
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-01
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-01/workspace
TaskSkill: scope-of-work
Tasks:
  - Verify the accepted DEL-05-01 row hashes and create a lossless isolated conversion candidate.
  - Run validation, claim mapping, parity, checklist, and rendering twice where required.
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG05/DEL-05-01/ScopeOfWork.md
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-01/**
RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-009, SOW-043, SOW-046
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
ExpectedOutputs:
  - Isolated ScopeOfWork.md and copied candidate ScopeOfWork.md.
  - Validation, claim map, parity report, repeated review checklists, and repeated HTML render evidence.
  - Source hashes, checks, complete self-excluding manifest, terminal status, and structured return.
EXCLUSIONS:
  - Live project writes, Git, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, and retirement.
