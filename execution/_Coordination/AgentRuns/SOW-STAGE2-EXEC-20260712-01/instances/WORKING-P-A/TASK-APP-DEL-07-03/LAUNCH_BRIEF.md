# TASK-APP-DEL-07-03 Sealed Brief — v2

PURPOSE: Independently verify the exact App DEL-07-03 Stage-2 pilot replacement candidate without repair.
RequestedBy: WORKING-P-A
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-P-A
ChildInstanceID: TASK-APP-DEL-07-03
PackageID: APP-PKG-07
DeliverableID: DEL-07-03

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0d260eb024d8b8dada0df477b70ac880a6906ffa
  PROJECT_SCOPE_REFS: projects/chirality-app-dev/docs/PRD.md; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts/_CONTEXT.md
  PACKAGE_OBJECTIVE_REFS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md PKG-07; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts/_CONTEXT.md
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@0d260eb024d8b8dada0df477b70ac880a6906ffa
  - P3_MANIFEST B1/G3 PASS exact row for DEL-07-03
  - Stage-1 App evidence commit fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26
  - PILOT-VALIDATION-001 active cross-lane correction
  - candidate SHA-256 6fa7732954b95314176d81045edeb9492405785cf4568acf210968f903cc9ab0
  - Datasheet 7e277b21a927fa651c39f265f4fa6ef0bdad52c3b7019699d626106bccc76e8e
  - Specification 55bacb4c5429d81c5e51865cc10a94a51a053243f12cee95f9514e25feb50987
  - Guidance ab983e07dcbb2f5eea52362daff0bc04b3893d15cb8adc03596a5f0fd91e787c
  - Procedure 3b70803cc9a77c2010caa1dd55a73425dfb247fadb094a7b59ebd2180e3cdea0
  - _STATUS b05037aedcc6ef5e9d892a75fa176ef48693458a224734ca18a20061075794ce

Tasks:
  - Read complete agents/AGENT_TASK.md and all live skills/scope-of-work method files before acting. Do not delegate.
  - Read exactly the named P3 DEL-07-03 row, the named live four sources and _STATUS/control references, the extracted candidate under candidates/P4_PILOTS/APP-PKG07/DEL-07-03/, active SOW tools, Stage-1 inventory, and Stage-1 evidence/DEL-07 evidence.
  - Confirm `target_state/legacy_source` is byte-equal to the live four sources/_STATUS and `target_state/ScopeOfWork.md` is byte-equal to the extracted candidate; do not edit those seeded truth copies.
  - Under PILOT-VALIDATION-001, validate the current live/P3-bound legacy-only state as `LEGACY_FOUR_DOC` with no SOW, and validate `target_state` as target-only `SOW_V1` with no legacy production files at its root. Do not invoke isolated-dual validation.
  - Reproduce the remaining full pilot gate: exact hashes/current-base equality; claim map and every target resolution; parity and source-line preservation; deterministic checklist twice; HTML render twice with byte stability/script/external-resource safety; lifecycle/control containment; Stage-1 evidence identity; separate schema/content, preservation, and substrate verdicts.
  - Emit an exact five-path future replacement manifest: ADD ScopeOfWork.md at candidate hash and DELETE the four legacy production paths at their P3 hashes. This is evidence only; do not modify the live project.
  - Write detailed evidence and terminal RETURN.md/STATUS.json only in this child instance. Any discrepancy returns FAIL; never repair.
  - Do not insert a D-GOV-16 marker, invoke conversion, overlay the legacy and target formats, treat the D-GOV-15 provenance marker as migration authority, or modify the candidate.

ExpectedOutputs:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state/_run_records/TASK_RUN_*.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state/evidence/**
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/RETURN.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-03/STATUS.json
  - evidence includes SOURCE_HASHES.tsv, validation/map/parity/checklist/render artifacts, REPLACEMENT_MANIFEST.tsv, and CHECKS.md

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/chirality-app-dev/** write
  - candidate edits or regeneration
  - Git/index/ref/branch/PR writes
  - lifecycle/control/receipt/release/H1/H2/retirement writes
  - delegation
