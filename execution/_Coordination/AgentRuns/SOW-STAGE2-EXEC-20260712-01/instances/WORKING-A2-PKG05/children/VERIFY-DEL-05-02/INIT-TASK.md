PURPOSE: Independently verify the accepted DEL-05-02 SOW_V1 replacement candidate without changing candidate or live state.
RequestedBy: WORKING-A2-PKG05
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-02
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-02/workspace/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL
TaskSkill: scope-of-work
Tasks:
  - Bind the accepted A2 manifest row, main commit, governance authority, and exact candidate.
  - Reconstruct an isolated workspace from the live legacy sources, status/control files, and accepted candidate.
  - Independently validate, map, report parity, derive the review checklist twice, render HTML twice, and exercise fail-closed negative cases.
  - Confirm source/status identity, conservative semantic authority, portability, and write containment without repairing the candidate.
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-02/**
RuntimeOverrides:
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-02/workspace/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-014, SOW-015, SOW-039
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  MODE: VERIFY
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
CustomInstructions:
  - Preserve all four live legacy documents and all status/control inputs byte-for-byte in the isolated workspace.
  - Keep generated evidence portable; inventory immutable copied absolute literals separately.
  - Candidate and live project are read-only; do not repair candidate content.
ExpectedOutputs:
  - Independent source hashes, validation, claim map, parity reports, repeated checklist and HTML derivatives.
  - Negative partial/unauthorized-dual fail-closed evidence.
  - Exact five-row replacement manifest, run record, checks, self-excluding manifest, terminal status, and structured return.
EXCLUSIONS:
  - Candidate edits, live project writes, Git operations, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, retirement, and repair.
