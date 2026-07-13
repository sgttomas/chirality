PURPOSE: Convert DEL-05-05 legacy production documents to a lossless isolated ScopeOfWork.md candidate.
RequestedBy: WORKING-A2-PKG05
ScopePath: execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-05
DeliverablePath: projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG05/DEL-05-05/ScopeOfWork.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-05/**
RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: [SOW-053, SOW-059]
  PACKAGE_OBJECTIVE_REFS: [OBJ-003, OBJ-005]
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
Tasks:
  - Hash-bind the accepted source kit and create an isolated derivative workspace.
  - Convert conservatively, then validate, map, check parity, derive the REVIEW checklist twice, and render twice.
  - Copy only the accepted ScopeOfWork.md candidate to the candidate target.
ExpectedOutputs:
  - Candidate ScopeOfWork.md plus portable source, validation, claim-map, parity, checklist, render, preservation, and return evidence.
EXCLUSIONS:
  - Live project writes, Git, other deliverables or packages, H1/H2, lifecycle, integration, release, retirement, and .claude-worktrees.
