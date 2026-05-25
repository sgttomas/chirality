# NEXT INSTANCE STATE - Chirality App vNext

**Last Updated:** 2026-05-24
**Updated By:** WORKING_ITEMS / TASK + scc-resolution-case

## Current Pointers

| Artifact | Path |
|---|---|
| Coordination policy | `execution/_Coordination/_COORDINATION.md` |
| Stable startup prompt | `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` |
| Decomposition authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Source corpus | `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md` |

## Current Program State

| Metric | Value |
|---|---:|
| Packages scaffolded | 10 |
| Control packages scaffolded | 1 (`PKG-00`) |
| Control deliverables scaffolded | 2 (`DEL-00-01`, `DEL-00-02`) |
| Control deliverables SEMANTIC_READY | 2 (`DEL-00-01`, `DEL-00-02`) |
| PKG-00 TASK provenance repair | complete; 5 TASK run records per control deliverable |
| PKG-00 SCC resolution cases | SCC-002 `CLOSED_BY_DEPCLOSURE`; SCC-001 `DEP_CLOSURE_PENDING`; ready-tranche CHANGE handoff applied and verified by DepClosure as graph reduction only; residual human-ruling-needed remedies are `REM-SCC-001-005`, `010`, `012`, `015`; 4 prior packets preserved as seed evidence; 0 selected for SCOPE_CHANGE intake |
| Deliverables scaffolded | 51 |
| OPEN | 0 |
| INITIALIZED | 0 |
| SEMANTIC_READY | 51 |
| IN_PROGRESS | 0 |
| CHECKING | 0 |
| ISSUED | 0 |
| Four-document kits complete | 51 |
| TASK four-documents P1/P2 success records | 51 |
| Semantic matrices validated | 51 |
| TASK semantic-matrix-build success records | 51 |
| Semantic matrices remaining | 0 |
| Semantic lensing skipped by human ruling | yes |
| P3 enrichment skipped by human ruling | yes |
| Dependencies.csv files created | 51 |
| Dependency register rows extracted | 554 |
| Dependency schema validation | 51/51 PASS |
| Dependency ID canonicalization | complete; `DEP-XX-YY-NNN`; 0 DepClosure ID normalizations |
| Active deliverable execution edges | 105 unique / 120 rows |
| Concrete dependency graph acyclic | NO |
| Strict active execution SCCs | 2 (sizes 2 and 8) |
| Blocker-subset SCCs | 0 |
| Accepted co-development clusters | 1 (DEL-03-01 / DEL-04-01) |
| CODEV-001 tranche evidence | implemented; blocker-subset closure scan passed |
| Stale interrupted PENDING run records retained as incomplete evidence | 5 |

## Data-Quality Notes

REF-006 docs/PRD.md=HASH_MISMATCH

## Package Folders

| PackageID | Name | Path |
|---|---|---|
| PKG-00 | DAG Closure and Project Control | `execution/PKG-00_DAG_Closure_and_Project_Control` |
| PKG-01 | Product Governance and Reliance Boundaries | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries` |
| PKG-02 | Desktop Shell, Navigation, and Operator State | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State` |
| PKG-03 | Runtime Engine Contract and Turn Lifecycle | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle` |
| PKG-04 | SDK Adapter, Prompt, Provider, and Settings | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings` |
| PKG-05 | Session Audit, Replay, and Tool Result Records | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records` |
| PKG-06 | Permissioned Tools, MCP, and Hooks | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks` |
| PKG-07 | Filesystem Execution, Lifecycle, and Dependencies | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies` |
| PKG-08 | Agent Suite, Pipeline Dispatch, and Subagent Governance | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance` |
| PKG-09 | Validation, Packaging, Security, and Release | `execution/PKG-09_Validation_Packaging_Security_and_Release` |
| PKG-10 | Domain Engine Future Boundary | `execution/PKG-10_Domain_Engine_Future_Boundary` |

## Active Human Rulings

- Decomposition authority: v3.2 SOFTWARE_DECOMP.
- Coordination representation: FULL_GRAPH.
- Dependency satisfaction threshold: SEMANTIC_READY.
- Dependency extraction is permitted after four-document authoring by human ruling on 2026-05-20.
- Existing `_SEMANTIC.md` outputs are invalid evidence and must not be consumed for dependency recording.
- `DEL-03-01` and `DEL-04-01` are accepted as co-development cluster `CODEV-001`; WORKING_ITEMS may proceed with them iteratively as a paired tranche.
- CODEV-001 follow-up closure satisfied `DEP-04-01-008`; blocker-subset SCC count is now 0.
- Post-ID-canonicalization closure verified canonical dependency IDs and made no dependency edge state changes.
- SCC-002 closure is accepted by DepClosure snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCC002_CHANGE_HANDOFF_2026-05-24_2020/`: `DEP-10-02-004` is retired as non-blocking interface/reference evidence; `DEP-10-03-006` remains the hard prerequisite; SCC-002 is absent.
- SCC-001 runtime/SDK core, session/audit, and tooling/permissions/MCP evidence have been indexed and candidate remedies bucketed in `CASE-SCC-001_Runtime_SDK_Session_Tooling` through bounded `TASK + scc-resolution-case` work; `SCC-001_Ruling_Workbook.csv` and `SCC-001_Dispatch_Plan.md` are the current decision surfaces. Ready-tranche CHANGE edits retired selected non-blocking or already-satisfied rows for `REM-SCC-001-006`, `007`, `008`, `009`, `011`, `013`, `014`, and `016`; DepClosure snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301/` proves graph reduction only with `scc_count = 2`. No SCOPE_CHANGE workflow was initiated.
- `PKG-00` is the meta/control package for DAG closure and project-level reconciliation; it is excluded from deliverable dependency graph participation by default.
- `DEL-00-01` owns SCC-002 closure control; `DEL-00-02` owns SCC-001 closure control.
- PKG-00 control deliverable readiness is backed by bounded TASK run records after invalidating the earlier direct ORCHESTRATOR-authored readiness state.
- PKG-00 SCC Resolution Cases are living WORKING_ITEMS/TASK receptacles for SCC evidence, human rulings, candidate remedies, and owner-workflow handoffs; prior scope-change packets are seed evidence only.
- The human must explicitly initiate SCOPE_CHANGE before any case or packet material becomes an intake request, and SCOPE_CHANGE gates still govern any amendment.
- Strict project-wide `BLOCKED/UNBLOCKED` remains unavailable while the strict all-active execution graph is cyclic.

## Immediate Next Actions

1. Use accepted DepClosure snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301/` as the current dependency closure ruling.
2. Use `execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md` as the project-control record for DAG closure workflow.
3. Continue `CASE-SCC-001_Runtime_SDK_Session_Tooling` using `SCC-001_Ruling_Workbook.csv`, `SCC-001_Dispatch_Plan.md`, and `CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301`: residual human-ruling-needed remedies are `REM-SCC-001-005`, `010`, `012`, `015`; no SCOPE_CHANGE candidate is selected unless the human explicitly initiates one.
4. Continue strict FULL_GRAPH reconciliation; strict all-active SCCs remain 2 (sizes 2 and 8).
5. Keep `CASE-SCC-002_PKG-10_Policy_Proposal` closed unless later accepted evidence changes the ruling.
6. Resolve remaining CODEV-001 `BLOCKED_TBD` evidence items: live SDK query/init probe, Claude Code subprocess version, interrupt/cancel subprocess behavior, Electron packaging behavior, Section 9 linkage, and adoption verdict.
7. Do not run product-deliverable `lens-register` or `four-documents` P3; the prior skip ruling remains applicable to product deliverables, while PKG-00 control deliverables have completed their own TASK-backed semantic pipeline.
8. Do not report strict project-wide `BLOCKED/UNBLOCKED` until strict FULL_GRAPH closure passes.

## Handoff Payload

- Stable invariant instructions: `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- Mutable state and queue: this file
- Deliverable-local continuity: `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Dependency state: extraction complete; graph cyclic; co-development ruling recorded
- CODEV-001 implementation evidence: runtime boundary, opt-in SDK probe provider, SDK options isolation, message mapping, session event JSONL, and deliverable evidence records created
- Latest dependency closure ruling: `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_READY_TRANCHE_001_2026-05-24_2301/`
- Control package: `execution/PKG-00_DAG_Closure_and_Project_Control/`
- SCC control deliverables: `DEL-00-01`, `DEL-00-02`
- SCC Resolution Cases: `CASE-SCC-002_PKG-10_Policy_Proposal`, `CASE-SCC-001_Runtime_SDK_Session_Tooling`
- Seed Scope Change Consumable Packets: `PKG00-SCA-PACKET-001` through `PKG00-SCA-PACKET-004`

## Update Protocol

WORKING_ITEMS or TASK handoff should update this file when lifecycle distribution, active blockers, or immediate next actions change. ORCHESTRATOR should update it only when explicitly performing a scan or setup-state refresh.
