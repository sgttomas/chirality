PURPOSE: CONVERT one accepted legacy four-document kit into an isolated SOW_V1 candidate with complete preservation evidence.
RequestedBy: WORKING-A2-PKG05
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-03
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-03/workspace/DEL-05-03
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG05/DEL-05-03/ScopeOfWork.md
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-03/**
RuntimeOverrides:
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-03/workspace/DEL-05-03
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-021, SOW-041
  PACKAGE_OBJECTIVE_REFS: OBJ-003, OBJ-008
  MODE: CONVERT
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  DISPATCH_BASIS: main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa
  RENDER_HTML: true
Tasks:
  - Verify all accepted live and isolated source/control hashes.
  - Convert the isolated legacy kit conservatively without removing source markers.
  - Run validator, claim mapper, parity, deterministic checklist, and script-free renderer twice where required.
  - Copy only the final ScopeOfWork.md to the candidate path.
  - Produce portable evidence, containment proof, terminal status, and structured return.
ExpectedOutputs:
  - Isolated ScopeOfWork.md and final candidate ScopeOfWork.md.
  - SOURCE_HASHES.tsv, VALIDATION.json, CLAIM_MAP.csv, PARITY.json, PARITY.md.
  - REVIEW_CHECKLIST_1.json, REVIEW_CHECKLIST_2.json, ScopeOfWork_1.html, ScopeOfWork_2.html.
  - CHECKS.md, self-excluding MANIFEST.tsv, STATUS.json, RETURN.md, and TASK run record.
EXCLUSIONS:
  - Live project writes, Git operations, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, and retirement.
