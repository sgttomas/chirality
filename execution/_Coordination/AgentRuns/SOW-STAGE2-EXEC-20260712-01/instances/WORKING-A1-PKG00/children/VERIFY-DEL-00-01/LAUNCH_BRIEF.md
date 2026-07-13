# VERIFY-DEL-00-01 Sealed TASK Brief — v1

PURPOSE: Independently verify the accepted author candidate for App DEL-00-01 without repair.
RequestedBy: WORKING-A1-PKG00
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG00
ChildInstanceID: VERIFY-DEL-00-01
PackageID: APP-PKG-00
DeliverableID: DEL-00-01
Dependency: manager-accepted terminal AUTHOR-DEL-00-01 return and candidate hash

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/VERIFY-DEL-00-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/VERIFY-DEL-00-01/**

RuntimeOverrides:
  MODE: VERIFY
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/VERIFY-DEL-00-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: CONTROL-SCC-002
  PACKAGE_OBJECTIVE_REFS: DAG-CLOSURE
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - exact DEL-00-01 A1 manifest row and A1-B0 acceptance
  - exact eight manifest hashes stated in AUTHOR-DEL-00-01/LAUNCH_BRIEF.md
  - exact candidate hash recorded in the manager-accepted author return; any missing/mismatched author binding fails closed

Tasks:
  - Act as a fresh Agent 2 TASK verifier. Read complete AGENT_TASK and all scope-of-work method files. Do not delegate, contact the author, or repair anything.
  - Confirm the manager-seeded workspace reconstructs the exact live four legacy sources, _STATUS/control inputs, and the byte-identical accepted author candidate. All seeded truth is read-only.
  - Reproduce live exact LEGACY_FOUR_DOC and isolated exact authorized MIGRATION_DUAL format resolution, source/status/control hashes, candidate hash, schema validation, map, target resolution, parity, source-line preservation, checklist twice, and render twice.
  - Independently inspect OUT-001/AC-001/VER-001 and all transformed content for semantic additions beyond the accepted row, deliverable identity, and legacy text. Classify schema/content-authority, preservation, and execution substrate separately.
  - Prove deterministic checklist byte stability and exact AC order/text/source/hash/matrix linkage; prove render byte stability, candidate-hash binding, script-free output, and no external resource.
  - Run isolated negative fixtures proving partial and unauthorized-dual inputs fail closed without modifying the accepted workspace or candidate.
  - Emit verifier evidence, exact candidate/source/status identities, exact five-path replacement manifest, CHECKS.md, terminal RETURN.md and STATUS.json only under this verifier instance. Any discrepancy is FAIL; no repair.

ExpectedOutputs:
  - independent evidence under this verifier instance
  - terminal RETURN.md and STATUS.json with PASS or exact failure

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - candidate writes or repair
  - author/sibling/package output writes
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation

