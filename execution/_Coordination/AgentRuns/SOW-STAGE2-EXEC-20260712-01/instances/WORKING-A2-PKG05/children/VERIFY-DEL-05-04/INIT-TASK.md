PURPOSE: Independently verify the accepted DEL-05-04 ScopeOfWork.md candidate without modifying candidate or live production content.
RequestedBy: WORKING-A2-PKG05

WorkingRoot: ${REPO_ROOT}
ScopePath: ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-04/isolated/DEL-05-04
DeliverablePath: ${REPO_ROOT}/projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View
TaskSkill: scope-of-work

Tasks:
  - Independently reconstruct an isolated workspace from the exact live legacy sources/status/control files plus the accepted candidate.
  - Reproduce format resolution, source/control/candidate hashes, schema validation, claim mapping, parity, deterministic REVIEW checklist twice, deterministic renderer twice, source/status identity, authority, conservative semantic-addition review, negative partial and unauthorized-dual fail-closed behavior, portability, and write containment.
  - Do not repair or modify the accepted candidate.

ApplyEdits: true
AllowedWriteTargets:
  - ${REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-04/**

AllowedTools:
  - python3 tools/scope_of_work/validate_scope_of_work.py:{scope_path}/**
  - python3 tools/scope_of_work/render_scope_of_work.py:{scope_path}/**
  - python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py:{scope_path}/**
  - python3 tools/scope_of_work/map_scope_of_work_claims.py:{scope_path}/**
  - python3 tools/scope_of_work/report_scope_of_work_parity.py:{scope_path}/**
  - python3 tools/scope_of_work/derive_review_checklist.py:{scope_path}/**

RuntimeOverrides:
  DELIVERABLE_PATH: ${REPO_ROOT}/projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
  PROJECT_SCOPE_REFS: SOW-042, SOW-046
  PACKAGE_OBJECTIVE_REFS: OBJ-003
  MODE: VERIFY
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  DISPATCH_COMMIT: 0af23f4709e1c95f6b2e0f19db80779bd4c968fa
  RENDER_HTML: true

ExpectedOutputs:
  - Portable INIT-TASK.md and isolated verification workspace.
  - SOURCE_HASHES.tsv, VALIDATION.json, CLAIM_MAP.csv, PARITY.json/.md, two deterministic checklists, two deterministic HTML renders, negative-test evidence, CHECKS.md, exact five-row REPLACEMENT_MANIFEST.tsv, self-excluding MANIFEST.tsv, terminal STATUS.json, RETURN.md, and a TASK run record.

EXCLUSIONS:
  - Candidate repair or mutation.
  - Live project writes, Git operations, other deliverables/packages, .claude-worktrees, H1/H2, lifecycle/integration/release/retirement actions.
