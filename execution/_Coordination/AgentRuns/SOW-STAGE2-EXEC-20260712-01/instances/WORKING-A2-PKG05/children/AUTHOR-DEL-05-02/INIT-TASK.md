PURPOSE: Convert DEL-05-02 from LEGACY_FOUR_DOC to an isolated SOW_V1 replacement candidate without changing live state.
RequestedBy: WORKING-A2-PKG05
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-02
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-02/workspace/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL
TaskSkill: scope-of-work
Tasks:
  - Verify the accepted A2 manifest row and its nine bound live hashes.
  - Create a lossless isolated migration candidate with conservative grounded OUT-001, AC-001, and VER-001 seed text.
  - Validate, map, report parity, derive the review checklist twice, and render HTML twice.
  - Copy only the accepted ScopeOfWork.md candidate to the declared package candidate target.
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG05/DEL-05-02/ScopeOfWork.md
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-02/**
RuntimeOverrides:
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/AUTHOR-DEL-05-02/workspace/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-014, SOW-015, SOW-039
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  MODE: CONVERT
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
CustomInstructions:
  - Preserve all four legacy documents and all underscore/control inputs byte-for-byte inside the isolated workspace.
  - Keep generated evidence portable with repo-relative paths or ${REPO_ROOT} tokens; inventory immutable copied literals separately.
ExpectedOutputs:
  - ScopeOfWork.md replacement candidate and SHA-256.
  - Source hashes, validation, claim map, parity reports, repeated checklist and HTML derivatives.
  - Run record, checks, self-excluding manifest, terminal status, and structured return.
EXCLUSIONS:
  - Live project writes, Git operations, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, and retirement.
