# AUTHOR-DEL-00-02 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-00-02 and complete author evidence.
RequestedBy: WORKING-A1-PKG00
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG00
ChildInstanceID: AUTHOR-DEL-00-02
PackageID: APP-PKG-00
DeliverableID: DEL-00-02

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-02/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-02/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG00/DEL-00-02/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-02/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: CONTROL-SCC-001
  PACKAGE_OBJECTIVE_REFS: DAG-CLOSURE
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-00-02 manifest row
  - Datasheet 9cf01dea61a47adf6c0006e185d14933d317a8cc400af7e36dd028816c86492d
  - Specification ae28eeb57685d19646b05688b27a6fa5d571500c1e9803417144706ffc36c1f9
  - Guidance e80c3d0ed6363670a9deb009aba31abe961a884142360a0042b7576251363ab0
  - Procedure a6c1628c3f1f1156bc6dcee5812ae99157d000ef93c5ccb23ad8744d1b64a28c
  - _STATUS 2d86b9a502936d285436d70a83145ede6721e85c1ff07806e5129a7f50291d3d
  - _CONTEXT d33ea8679f12a5ba00ca5f9ae73a3b8299a5ae3f169b65e0a41f1c2ca8e95caa
  - _REFERENCES 2b377598def3402fe921ad72d83026edbe49f4e45f756fc6fcd0d5071d867c7a
  - _DEPENDENCIES 984a05562ad20b3ff08c5d34456da50dc2e4ddbf992099b0c89efd7b5f421232

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm the manager-seeded workspace is byte-equal to the exact live four sources and _STATUS/control inputs. Keep all seeded inputs byte-identical.
  - Resolve the live state as exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, with no live ScopeOfWork.md and intentionally no Dependencies.csv.
  - Invoke the deterministic converter first for authoring under exact isolated-migration authority. Seed OUT-001 as a conservative statement that the output is the source-grounded SCC-001 ruling workbook, dependency-row decision records, and follow-up DepClosure evidence; seed AC-001 only as preservation/traceability to CONTROL-SCC-001 and DAG-CLOSURE; seed VER-001 as deterministic validation, claim mapping, parity, checklist derivation, and human review against the accepted legacy basis. Add no scope, reliance, lifecycle meaning, or semantic obligation.
  - Preserve every converter source marker. Validate the isolated MIGRATION_DUAL candidate, emit the claim map and parity report, derive the checklist twice, and render HTML twice, always with exact migration authority.
  - Prove every source line is disposed, every marker binds the current source hash and a defined target, checklist order/text/linkage is exact, repeated checklist and render bytes are stable, and render is script-free with no external resource.
  - Copy only the exact resulting ScopeOfWork.md to `candidates/W_A1/APP-PKG00/DEL-00-02/ScopeOfWork.md`. Do not place legacy/control copies or other files in the candidate directory.
  - Write portable evidence including SOURCE_HASHES.tsv, validation JSON, CLAIM_MAP.csv, PARITY.json/.md, two checklist JSONs, two HTML renders, candidate SHA-256, separate schema/content-authority/preservation/substrate verdicts, CHECKS.md, RETURN.md, and terminal STATUS.json.
  - Any discrepancy returns FAIL with exact rerun requirements. Never write live project paths, Git state, lifecycle/control state, H1/H2, release, or retirement state.

ExpectedOutputs:
  - exact candidate `candidates/W_A1/APP-PKG00/DEL-00-02/ScopeOfWork.md`
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, and sibling paths
  - Git/index/ref/branch/PR/integration writes
  - lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation

