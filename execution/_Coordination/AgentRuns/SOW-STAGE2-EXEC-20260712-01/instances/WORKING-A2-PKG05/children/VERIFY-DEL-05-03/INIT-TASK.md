PURPOSE: VERIFY one accepted isolated SOW_V1 migration candidate independently against its exact live legacy source kit and frozen authority.
RequestedBy: WORKING-A2-PKG05
InitTaskPath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-03/INIT-TASK.md
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-03
DeliverablePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-03/workspace/DEL-05-03
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-03/**
RuntimeOverrides:
  DELIVERABLE_PATH: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-03/workspace/DEL-05-03
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-021, SOW-041
  PACKAGE_OBJECTIVE_REFS: OBJ-003, OBJ-008
  MODE: VERIFY
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  DISPATCH_BASIS: main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa
  RENDER_HTML: true
Tasks:
  - Reconstruct an isolated workspace from exact live source/control files plus the accepted candidate.
  - Reproduce format resolution, hashes, schema validation, claim map, parity, checklist twice, renderer twice, identity, authority, conservative semantic-addition review, negative fail-closed behavior, portability, and containment.
  - Do not repair or modify the candidate or live project.
ExpectedOutputs:
  - Isolated source/candidate workspace and _run_records.
  - SOURCE_HASHES.tsv, VALIDATION.json, CLAIM_MAP.csv, PARITY.json, PARITY.md.
  - REVIEW_CHECKLIST_1.json, REVIEW_CHECKLIST_2.json, ScopeOfWork_1.html, ScopeOfWork_2.html.
  - Negative-test evidence, CHECKS.md, exact five-row REPLACEMENT_MANIFEST.tsv, self-excluding MANIFEST.tsv, STATUS.json, and RETURN.md.
EXCLUSIONS:
  - Candidate repair or writes, live project writes, Git operations, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle, integration, release, and retirement.
