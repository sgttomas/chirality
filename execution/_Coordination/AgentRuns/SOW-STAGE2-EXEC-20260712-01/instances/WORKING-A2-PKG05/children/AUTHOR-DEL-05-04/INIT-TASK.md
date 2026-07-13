PURPOSE: Convert DEL-05-04 from LEGACY_FOUR_DOC to one isolated, lossless SOW_V1 candidate under the accepted Stage-2 migration authority.
RequestedBy: WORKING-A2-PKG05
ScopePath: execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-04/isolated/DEL-05-04
DeliverablePath: projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View
TaskSkill: scope-of-work
Tasks:
  - Verify the accepted source and control hashes and preserve an isolated byte-identical copy.
  - Convert the four legacy production documents into a traceable SOW_V1 candidate without changing source meaning or lifecycle state.
  - Validate, map, parity-check, derive the REVIEW checklist, and render deterministic HTML twice.
ApplyEdits: true
AllowedWriteTargets:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG05/DEL-05-04/ScopeOfWork.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-04/**
RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-04/isolated/DEL-05-04
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-042, SOW-046
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  SOURCE_COMMIT: 0af23f4709e1c95f6b2e0f19db80779bd4c968fa
  RENDER_HTML: true
CustomInstructions:
  - Preserve all source markers and all 296 legacy source lines exactly through mapping and parity evidence.
  - Keep SDK transcript linkage secondary to Chirality HarnessEvent records.
  - Keep substantive uncertainty labeled and do not invent new scope.
ExpectedOutputs:
  - Isolated ScopeOfWork.md and copied source/control kit.
  - Source hashes, validation, claim map, parity reports, two deterministic checklists, and two deterministic HTML renders.
  - Portable run record, checks, manifest, terminal status, return, and candidate ScopeOfWork.md.
EXCLUSIONS:
  - Live project writes, Git operations, lifecycle changes, integration, release, retirement, H1/H2, other deliverables/packages, and .claude-worktrees.
