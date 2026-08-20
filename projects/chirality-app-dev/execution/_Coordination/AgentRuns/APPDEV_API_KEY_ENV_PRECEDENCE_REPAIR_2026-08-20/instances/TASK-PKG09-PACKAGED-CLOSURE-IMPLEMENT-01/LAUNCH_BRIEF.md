# INIT-TASK — N3 packaged-security execution and closure

PURPOSE: Execute the exact N3 objective and return a review-ready candidate.
RequestedBy: `WI-PKG09-API-KEY-PRECEDENCE-01`
RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
ParentInstanceID: `WI-PKG09-API-KEY-PRECEDENCE-01`
ChildInstanceID: `TASK-PKG09-PACKAGED-CLOSURE-IMPLEMENT-01`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
DeliverablePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
TaskSkill: `software-bounded-implementation`
PackageID: `PKG-09`
DeliverableIDs: `DEL-09-06, DEL-09-04`
Objective: Build and prove the fixed packaged artifact, retain compact evidence, and calibrate only the proved packaged-security residuals.
AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38` plus Agent 0-accepted N1/N2 identities in the parent launch brief.
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: true

Tasks:
  - Read the parent N3 launch brief, v2 graph/plan, accepted N1/N2 handoffs, both selected SOW/status/memory/assessment sets, prior proof implementation/evidence, D-APP-97, D-APP-99, software profile, and proof scripts/tests.
  - Revalidate predecessor hashes and APP-HOLD dispatch before reliance.
  - Run the focused and registered deterministic gates with normalized evidence.
  - Request exact host escalation for a fresh `npm run desktop:dist` and then the existing packaged-security proof against that artifact.
  - Run the secret scan and retain only compact redacted identity-bound evidence in the repository; preserve raw host output in an isolated temporary directory through review.
  - If every criterion passes, calibrate the relevant assessment rows and remove only the two named packaged-security Remaining items; preserve all fences and unrelated residuals.
  - Validate write containment, parseability, hashes, whitespace, and return exact outputs, checks, host commands, blockers, residuals, and rerun triggers.

AllowedWriteTargets:
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/**`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Assessment_INSP-03_DEL-09-06.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/MEMORY.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/**`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Assessment_INSP-03_DEL-09-04.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/MEMORY.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
  - `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/**`
  - `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-PKG09-PACKAGED-CLOSURE-IMPLEMENT-01/**`

AllowedTools:
  - `tools/software_workflow/select_affected_checks.py`
  - `tools/software_workflow/run_registered_checks.py`
  - `tools/software_workflow/validate_change_scope.py`
  - `tools/software_workflow/verify_generated_manifest.py`
  - `tools/software_workflow/compare_structured.py`

CustomInstructions:
  - Agent 2 does not delegate.
  - Use `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` for root self-check and registered Python gates where the system interpreter lacks PyYAML.
  - Do not edit product, tests, scripts, workflow, dependencies, lockfile, SOW, decisions, receipts, completion logs, or Git state.
  - Do not use a real credential. Ensure all provider credential environment variables are scrubbed or replaced only by unmistakable non-secret fixtures through the existing proof.
  - A failed proof or new product defect returns precisely; do not infer acceptance or widen scope.

AcceptanceCriteria:
  - Every item in the parent N3 launch brief's Checks and acceptance section passes.

ExpectedOutputs:
  - TASK run record, compact closure evidence, normalized checks, exact host proof result and raw-output location, calibrated DEL-09-06 and DEL-09-04 state if proved, write containment, status and structured return.

EXCLUSIONS:
  - All exclusions in the parent N3 launch brief.
