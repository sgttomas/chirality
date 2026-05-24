# NEXT INSTANCE STATE - Chirality App vNext

**Last Updated:** 2026-05-24
**Updated By:** WORKING_ITEMS

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
| Active deliverable execution edges | 114 unique / 129 rows |
| Concrete dependency graph acyclic | NO |
| Strict active execution SCCs | 2 (sizes 18, 2) |
| Blocker-subset SCCs | 0 |
| Accepted co-development clusters | 1 (DEL-03-01 / DEL-04-01) |
| CODEV-001 tranche evidence | implemented; blocker-subset closure scan passed |
| Stale interrupted PENDING run records retained as incomplete evidence | 5 |

## Data-Quality Notes

REF-006 docs/PRD.md=HASH_MISMATCH

## Package Folders

| PackageID | Name | Path |
|---|---|---|
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
- Strict project-wide `BLOCKED/UNBLOCKED` remains unavailable while the strict all-active execution graph is cyclic.

## Immediate Next Actions

1. Review follow-up DepClosure snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_WORKING_ITEMS_CODEV_FOLLOWUP_2026-05-24_1348/`.
2. Continue strict FULL_GRAPH reconciliation; strict all-active SCCs remain 2 (sizes 18, 2).
3. Resolve remaining CODEV-001 `BLOCKED_TBD` evidence items: live SDK query/init probe, Claude Code subprocess version, interrupt/cancel subprocess behavior, Electron packaging behavior, Section 9 linkage, and adoption verdict.
4. Do not run `lens-register` or `four-documents` P3; semantic enrichment remains skipped by human ruling.
5. Do not report strict project-wide `BLOCKED/UNBLOCKED` until strict FULL_GRAPH closure passes.

## Handoff Payload

- Stable invariant instructions: `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- Mutable state and queue: this file
- Deliverable-local continuity: `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Dependency state: extraction complete; graph cyclic; co-development ruling recorded
- CODEV-001 implementation evidence: runtime boundary, opt-in SDK probe provider, SDK options isolation, message mapping, session event JSONL, and deliverable evidence records created
- Latest dependency closure ruling: `execution/_Reconciliation/DepClosure/CLOSURE_WORKING_ITEMS_CODEV_FOLLOWUP_2026-05-24_1348/`

## Update Protocol

WORKING_ITEMS or TASK handoff should update this file when lifecycle distribution, active blockers, or immediate next actions change. ORCHESTRATOR should update it only when explicitly performing a scan or setup-state refresh.
