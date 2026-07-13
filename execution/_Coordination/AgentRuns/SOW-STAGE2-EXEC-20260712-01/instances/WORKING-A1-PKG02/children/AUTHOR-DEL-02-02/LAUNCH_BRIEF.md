# AUTHOR-DEL-02-02 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-02-02 and complete author evidence.
RequestedBy: WORKING-A1-PKG02
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG02
ChildInstanceID: AUTHOR-DEL-02-02
PackageID: APP-PKG-02
ManifestPackageID: PKG-02
DeliverableID: DEL-02-02

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/AUTHOR-DEL-02-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/AUTHOR-DEL-02-02/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG02/DEL-02-02/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG02/children/AUTHOR-DEL-02-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: SOW-006, SOW-007
  PACKAGE_OBJECTIVE_REFS: OBJ-001
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and the exact DEL-02-02 row in snapshots/W_A1/preflight/A1_MANIFEST.tsv
  - all source/status/control hashes, refs, paths, and dependencies in that exact frozen row

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm the exact manifest row, then seed the workspace from its live path with byte-equal Datasheet.md, Specification.md, Guidance.md, Procedure.md, _STATUS.md, _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and Dependencies.csv where present. Keep all seeded inputs byte-identical.
  - Resolve live state as exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, with no live ScopeOfWork.md.
  - Invoke the deterministic converter first using exact manifest package-id PKG-02, never APP-PKG-02. Ground OUT-001, AC-001, and VER-001 only in the row's SOW-006, SOW-007; OBJ-001; deliverable identity; and exact legacy source. Add no scope, reliance claim, lifecycle meaning, or semantic obligation.
  - Preserve every source marker; validate MIGRATION_DUAL; emit map/parity; derive checklist twice; render twice under exact authority.
  - Prove complete line disposition, marker/hash/target bindings, checklist exactness, stable script-free render, and separate schema/content-authority/preservation/substrate verdicts.
  - Copy only exact ScopeOfWork.md to candidates/W_A1/APP-PKG02/DEL-02-02/ScopeOfWork.md.
  - Write only portable generated evidence and terminal TASK run record, RETURN.md, and STATUS.json. Machine-specific absolute checkout strings already embedded in accepted source/control bytes and marker-bound verbatim candidate/render text are PRESERVED_SOURCE_LITERAL and must remain exact; inventory/classify them. Never normalize source/candidate/render bytes. Generated run/evidence metadata must be portable. Stop and notify the manager before any generated-evidence repair.
  - Any discrepancy fails with rerun requirements. Never write project or Git/lifecycle surfaces.

ExpectedOutputs:
  - exact candidate candidates/W_A1/APP-PKG02/DEL-02-02/ScopeOfWork.md
  - author run record and evidence under this child instance
  - preserved-source-literal inventory where applicable
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, sibling paths
  - Git/integration/lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation
