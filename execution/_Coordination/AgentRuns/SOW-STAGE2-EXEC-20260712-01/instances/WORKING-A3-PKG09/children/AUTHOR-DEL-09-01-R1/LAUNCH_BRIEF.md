# AUTHOR-DEL-09-01-R1 Sealed TASK Brief — v1

PURPOSE: Fresh execution of the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-09-01 after predecessor AUTHOR-DEL-09-01 failed normalization without task execution or candidate/project writes because its workspace anchor was absent.
RequestedBy: WORKING-A3-PKG09
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A3-PKG09
ChildInstanceID: AUTHOR-DEL-09-01-R1
PackageID: APP-PKG-09
ManifestPackageID: PKG-09
DeliverableID: DEL-09-01

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01-R1/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01-R1/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A3/APP-PKG09/DEL-09-01/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01-R1/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
  PROJECT_SCOPE_REFS: SOW-035, SOW-036
  PACKAGE_OBJECTIVE_REFS: OBJ-008
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - synchronized main@193663b1d93299c18d64f59b543b36a0dd5f0ee1, evidence-only successor to exact row basis main@ff59428ff27d929bc1172e6c049a5e274d487fc0
  - accepted W-A3 preflight exact DEL-09-01 row and predecessor fail-closed terminal record
  - exact frozen source/status/control hashes, refs, path, dependencies, and unchanged candidate/project surfaces

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and every scope-of-work method file; do not delegate or contact siblings.
  - Confirm the exact manifest row, remove only the workspace `.keep` anchor, then seed the workspace from live with byte-equal Datasheet.md, Specification.md, Guidance.md, Procedure.md, _STATUS.md, _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and Dependencies.csv.
  - Resolve exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, no live ScopeOfWork.md. Invoke the converter first with PKG-09. Ground OUT-001, AC-001, VER-001 only in SOW-035/SOW-036, OBJ-008, deliverable identity, and exact legacy source.
  - Preserve every marker; validate authorized MIGRATION_DUAL; emit map/parity; derive checklist twice; render twice; run fail-closed negative fixtures; prove complete line disposition, bindings, checklist, deterministic safe render, and separate verdicts.
  - Copy only exact ScopeOfWork.md to candidates/W_A3/APP-PKG09/DEL-09-01/ScopeOfWork.md.
  - Write only portable generated evidence and terminal run record, RETURN.md, STATUS.json, reproducible MANIFEST.tsv. Preserve/inventory accepted source/control machine literals; never normalize source/candidate/render bytes. Stop before after-the-fact repair.
  - Any discrepancy fails. Never write project or Git/lifecycle surfaces.

ExpectedOutputs: exact candidate, author evidence, preserved-literal inventory, reproducible MANIFEST.tsv, terminal RETURN.md and STATUS.json

EXCLUSIONS: `.claude-worktrees/**`; every `projects/**` write; other candidate/package/sibling paths; Git/integration/lifecycle/H1/H2/ISSUED/release/retirement/delegation.
