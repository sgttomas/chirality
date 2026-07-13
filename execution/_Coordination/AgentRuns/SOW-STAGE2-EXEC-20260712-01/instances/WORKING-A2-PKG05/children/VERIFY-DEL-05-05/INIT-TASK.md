PURPOSE: Independently verify the accepted DEL-05-05 ScopeOfWork.md candidate against the exact live legacy source kit and accepted A2 manifest row.
RequestedBy: WORKING-A2-PKG05
ScopePath: execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-05
DeliverablePath: projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-05/**
RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: [SOW-053, SOW-059]
  PACKAGE_OBJECTIVE_REFS: [OBJ-003, OBJ-005]
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
Tasks:
  - Reconstruct an isolated workspace from exact live legacy sources/status/control and the accepted candidate.
  - Independently run validation, claim mapping, parity, REVIEW checklist derivation twice, rendering twice, and negative fail-closed tests.
  - Verify source/status identity, authority, conservative semantic additions, portability, containment, and exact replacement manifest.
ExpectedOutputs:
  - Portable verifier evidence, self-excluding manifest, terminal status, and structured return.
EXCLUSIONS:
  - Candidate repair, live project writes, Git mutation, other deliverables or packages, H1/H2, lifecycle, integration, release, retirement, and .claude-worktrees.
