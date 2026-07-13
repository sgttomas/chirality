# TASK-APP-DEL-07-01-R1 Replacement Sealed Brief — v1

PURPOSE: Independently verify the exact App DEL-07-01 Stage-2 pilot replacement candidate without repair.
RequestedBy: WORKING-P-A
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-P-A
ChildInstanceID: TASK-APP-DEL-07-01-R1
PackageID: APP-PKG-07
DeliverableID: DEL-07-01

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0d260eb024d8b8dada0df477b70ac880a6906ffa
  PROJECT_SCOPE_REFS: projects/chirality-app-dev/docs/PRD.md; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/_CONTEXT.md
  PACKAGE_OBJECTIVE_REFS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md PKG-07; projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/_CONTEXT.md
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@0d260eb024d8b8dada0df477b70ac880a6906ffa
  - P3_MANIFEST B1/G3 PASS exact row for DEL-07-01
  - Stage-1 App evidence commit fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26
  - PILOT-VALIDATION-001 active cross-lane correction
  - V-01-A FAILED_SUBSTRATE_NONTERMINAL disposition; partial outputs unaccepted and excluded
  - candidate SHA-256 9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744
  - Datasheet c22fbd0afa9d838732fb33aba7b685712c13c746e6c146643b2d567305df3fc9
  - Specification 3e78a9556a0c6172e2edf0d02bc3112fda57d8e101ea604d0434e9ed78150f9a
  - Guidance 9a1abe8570b4fc5de259277b1666aee0cc1b3b144f0962719c53ef3f576d2de9
  - Procedure c3f91a8f79ae1252ec5f5def529a1f0d9bb3352056e990aaafe843e3b4c84335
  - _STATUS dc020e8f14e991d951b1759d6b6a5c7e499b3f983ca77a3654f246f6e734f495

Tasks:
  - Read complete agents/AGENT_TASK.md and all live skills/scope-of-work method files before acting. Do not delegate.
  - Read exactly the named P3 DEL-07-01 row, the named live four sources and _STATUS/control references, the extracted candidate under candidates/P4_PILOTS/APP-PKG07/DEL-07-01/, active SOW tools, Stage-1 inventory, and Stage-1 evidence/DEL-07 evidence.
  - Confirm `target_state/legacy_source` is byte-equal to the live four sources/_STATUS and `target_state/ScopeOfWork.md` is byte-equal to the extracted candidate; do not edit those seeded truth copies.
  - Under PILOT-VALIDATION-001, validate the current live/P3-bound legacy-only state as `LEGACY_FOUR_DOC` with no SOW, and validate `target_state` as target-only `SOW_V1` with no legacy production files at its root. Do not invoke isolated-dual validation.
  - Reproduce the remaining full pilot gate: exact hashes/current-base equality; claim map and every target resolution; parity and source-line preservation; deterministic checklist twice; HTML render twice with byte stability/script/external-resource safety; lifecycle/control containment; Stage-1 evidence identity; separate schema/content, preservation, and substrate verdicts.
  - Emit an exact five-path future replacement manifest: ADD ScopeOfWork.md at candidate hash and DELETE the four legacy production paths at their P3 hashes. This is evidence only; do not modify the live project.
  - Write detailed evidence and terminal RETURN.md/STATUS.json only in this child instance. Any discrepancy returns FAIL; never repair.
  - Do not insert a D-GOV-16 marker, invoke conversion, overlay the legacy and target formats, treat the D-GOV-15 provenance marker as migration authority, or modify the candidate.

ExpectedOutputs:
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state/_run_records/TASK_RUN_*.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state/evidence/**
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/RETURN.md
  - execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/STATUS.json
  - evidence includes SOURCE_HASHES.tsv, validation/map/parity/checklist/render artifacts, REPLACEMENT_MANIFEST.tsv, and CHECKS.md

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/chirality-app-dev/** write
  - candidate edits or regeneration
  - Git/index/ref/branch/PR writes
  - lifecycle/control/receipt/release/H1/H2/retirement writes
  - delegation
  - reads from TASK-APP-DEL-07-01 failed-attempt partial evidence except its FAILED_ATTEMPT_HANDOFF.md disposition
