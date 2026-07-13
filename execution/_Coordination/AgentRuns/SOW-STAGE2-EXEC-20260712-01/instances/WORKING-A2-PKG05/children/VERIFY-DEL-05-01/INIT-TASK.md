PURPOSE: Independently verify the accepted DEL-05-01 SOW_V1 candidate against the exact accepted legacy source kit without changing candidate or project state.
RequestedBy: WORKING-A2-PKG05
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-01
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-01/workspace
TaskSkill: scope-of-work
Tasks:
  - Bind the accepted DEL-05-01 preflight row, candidate, live source/status/control hashes, D-GOV-16 format authority, and accepted main commit.
  - Independently reconstruct an isolated MIGRATION_DUAL workspace and reproduce validation, claim mapping, parity, checklist, rendering, negative fail-closed, portability, and containment evidence.
  - Do not repair or modify the candidate.
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-01/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-009, SOW-043, SOW-046
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
ExpectedOutputs:
  - Portable isolated workspace, run records, source hashes, validation, claim map, parity, repeated checklists, repeated HTML, and negative-test evidence.
  - Checks, exact five-row replacement manifest, self-excluding manifest, terminal status, and structured return.
EXCLUSIONS:
  - Candidate repair, live project writes, Git, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, and retirement.
