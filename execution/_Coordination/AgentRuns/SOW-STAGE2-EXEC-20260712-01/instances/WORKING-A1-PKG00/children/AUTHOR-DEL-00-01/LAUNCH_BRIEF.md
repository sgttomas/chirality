# AUTHOR-DEL-00-01 Sealed TASK Brief — v1

PURPOSE: Create the exact isolated Stage-2 SOW_V1 conversion candidate for App DEL-00-01 and complete author evidence.
RequestedBy: WORKING-A1-PKG00
RunID: SOW-STAGE2-EXEC-20260712-01
ParentInstanceID: WORKING-A1-PKG00
ChildInstanceID: AUTHOR-DEL-00-01
PackageID: APP-PKG-00
DeliverableID: DEL-00-01

WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-01/workspace
DeliverablePath: {REPO_ROOT}/projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure
TaskSkill: scope-of-work
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-01/**
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A1/APP-PKG00/DEL-00-01/**

RuntimeOverrides:
  MODE: CONVERT
  DELIVERABLE_PATH: {REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A1-PKG00/children/AUTHOR-DEL-00-01/workspace
  DECOMPOSITION_BASIS: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  PROJECT_SCOPE_REFS: CONTROL-SCC-002
  PACKAGE_OBJECTIVE_REFS: DAG-CLOSURE
  MODE_AUTHORITY: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true

AcceptedBasis:
  - main@34b87ec77010035eeaa76f0fa65981ec57e78933, evidence-only successor to exact row basis main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
  - accepted W-A1 A1-B0 preflight and exact DEL-00-01 manifest row
  - Datasheet 3d1e9a25b7b1bf23eb5e53322bfa71c3d270ab2ec43d8586ff787f5637db32e7
  - Specification 53497eb81380778c6df7c32d9d0d7bf0a8cfac378b5462d426a42897dae4f444
  - Guidance a9f61a5afd6f26c2ee6be21286b27c2ae7f552bf1f367995bee6a26f1cfd78fe
  - Procedure d5cb3050489df100a7cb1ebe3815aa77b74e47c193ab98e559c63ce67e3ad9ff
  - _STATUS 7d8e0d99d5371986257bc9165cd50733d1fb9d72691066c84e5765ac08c8c46f
  - _CONTEXT 55048244e0466dba8cdd2d977bc5cebd600420b782037ed437af15b0a082310f
  - _REFERENCES ff8f2cc144d4962cab9e12ab2eba37c61ff5db042b94de9e2f52623c1443322e
  - _DEPENDENCIES 80ab150bba95a13211bd74fe8392582e01d6d23c0293a096f8f33e4241e33c30

Tasks:
  - Act strictly as Agent 2 TASK; read complete AGENT_TASK and all scope-of-work method files; do not delegate or contact siblings.
  - Confirm the manager-seeded workspace is byte-equal to the exact live four sources and _STATUS/control inputs. Keep all seeded inputs byte-identical.
  - Resolve the live state as exact LEGACY_FOUR_DOC, IN_PROGRESS, non-ISSUED, with no live ScopeOfWork.md and intentionally no Dependencies.csv.
  - Invoke the deterministic converter first for authoring under exact isolated-migration authority. Seed OUT-001 as a conservative statement that the output is the source-grounded SCC-002 ruling and follow-up DepClosure evidence; seed AC-001 only as preservation/traceability to CONTROL-SCC-002 and DAG-CLOSURE; seed VER-001 as deterministic validation, claim mapping, parity, checklist derivation, and human review against the accepted legacy basis. Add no scope, reliance, lifecycle meaning, or semantic obligation.
  - Preserve every converter source marker. Validate the isolated MIGRATION_DUAL candidate, emit the claim map and parity report, derive the checklist twice, and render HTML twice, always with exact migration authority.
  - Prove every source line is disposed, every marker binds the current source hash and a defined target, checklist order/text/linkage is exact, repeated checklist and render bytes are stable, and render is script-free with no external resource.
  - Copy only the exact resulting ScopeOfWork.md to `candidates/W_A1/APP-PKG00/DEL-00-01/ScopeOfWork.md`. Do not place legacy/control copies or other files in the candidate directory.
  - Write portable evidence including SOURCE_HASHES.tsv, validation JSON, CLAIM_MAP.csv, PARITY.json/.md, two checklist JSONs, two HTML renders, candidate SHA-256, separate schema/content-authority/preservation/substrate verdicts, CHECKS.md, RETURN.md, and terminal STATUS.json.
  - Any discrepancy returns FAIL with exact rerun requirements. Never write live project paths, Git state, lifecycle/control state, H1/H2, release, or retirement state.

ExpectedOutputs:
  - exact candidate `candidates/W_A1/APP-PKG00/DEL-00-01/ScopeOfWork.md`
  - author run record and evidence under this child instance
  - terminal RETURN.md and STATUS.json

EXCLUSIONS:
  - .claude-worktrees/**
  - every projects/** write
  - other candidates, package instances, and sibling paths
  - Git/index/ref/branch/PR/integration writes
  - lifecycle/H1/H2/ISSUED/release/retirement actions
  - delegation

