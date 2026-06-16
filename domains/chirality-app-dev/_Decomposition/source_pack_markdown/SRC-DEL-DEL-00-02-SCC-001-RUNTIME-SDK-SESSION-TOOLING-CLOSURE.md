# Source Pack: SRC-DEL-DEL-00-02-SCC-001-RUNTIME-SDK-SESSION-TOOLING-CLOSURE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/Datasheet.md

### Datasheet: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

#### Identification

| Field | Value |
|---|---|
| PackageID | PKG-00 |
| PackageName | DAG Closure and Project Control |
| DeliverableID | DEL-00-02 |
| DeliverableName | SCC-001 Runtime SDK Session Tooling Closure |
| Type | CONTROL_RECONCILIATION |
| ResponsibleParty | TBD - HumanRuling required for the owning human/agent authorized to accept SCC-001 rulings. |
| DecompositionVariant | CONTROL_PACKAGE |
| DecompositionRevision | PKG-00 overlay |
| CurrentLifecycleState | SEMANTIC_READY |

Sources: `_CONTEXT.md` (Identity), `_STATUS.md` (Current State after this run).

#### Attributes

| Attribute | Value |
|---|---|
| ControlScopeItem | CONTROL-SCC-001 |
| ControlPurpose | Coordinate source-grounded SCC-001 reconciliation for the runtime, SDK, session, and tooling closure area. |
| GraphParticipation | EXCLUDED_CONTROL_DELIVERABLE |
| StructuredDependencyRegister | Intentionally absent; do not create `Dependencies.csv` for this control deliverable. |
| CurrentClosureSnapshot | `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/` |
| StrictFullGraphStatus | CYCLIC |
| StrictSCCCount | 2 |
| BlockerSubsetStatus | ACYCLIC |
| SCC_ID | SCC-001 |
| SCC_Size | 18 |
| SCC_Nodes | `DEL-03-01`; `DEL-03-02`; `DEL-03-03`; `DEL-03-04`; `DEL-04-01`; `DEL-04-02`; `DEL-04-03`; `DEL-04-04`; `DEL-04-05`; `DEL-05-01`; `DEL-05-02`; `DEL-05-03`; `DEL-05-05`; `DEL-06-01`; `DEL-06-02`; `DEL-06-03`; `DEL-06-04`; `DEL-06-06` |
| SCC_001_BidirectionalPairs | 12 pairs listed in `Evidence/bidirectional_pairs.csv`; the snapshot reports 13 total bidirectional pairs including SCC-002. |
| AnticipatedArtifacts | Focused SCC-001 ruling workbook; dependency row decision records; follow-up DepClosure evidence. |

Sources: `DAG_CLOSURE_CONTROL.md` (Control Status, Current Queue), `_DEPENDENCIES.md` (Dependency Tracking), `Dependency_Closure_Report.md` (Evidence Summary, Remaining SCCs), `Evidence/scc_summary.csv`, `Evidence/bidirectional_pairs.csv`, `SCC_Triage_Workbook.csv`.

#### Conditions

- This deliverable is a PKG-00 control artifact, not a product implementation deliverable.
- PKG-00 and DEL-00-* control deliverables are outside the strict product dependency graph.
- DepClosure and dependency extraction must continue to read product registers under PKG-01 through PKG-10.
- SCC-001 closure decisions are not made by this four-document kit. They remain TBD until a source-grounded reconciliation workflow inspects the owning product dependency rows and cited evidence.
- Any approved row change must be applied in the owning product deliverable register, not in this control deliverable.
- Project-wide `BLOCKED/UNBLOCKED` must not be reported until DepClosure reports a strict acyclic FULL_GRAPH.

Sources: `README.md` (Boundary, Non-Goals), `_CONTEXT.md` (Source Authority), `_DEPENDENCIES.md` (Boundary), `DAG_CLOSURE_CONTROL.md` (Workflow, Acceptance Condition), `Dependency_Closure_Report.md` (Ruling).

#### Construction

| Component | Status | Notes |
|---|---|---|
| Control package scaffold | Present | PKG-00 owns DAG/SCC closure workflow notes and SCC closure control deliverables. |
| Current evidence pointer | Present | `_REFERENCES.md` points to the 2026-05-24 14:31 DepClosure snapshot. |
| SCC-001 node set | Present | Captured in `Evidence/scc_summary.csv`. |
| Initial bidirectional-pair evidence | Present | Captured in `Evidence/bidirectional_pairs.csv`. |
| Initial triage directive | Present | Captured in `SCC_Triage_Workbook.csv`; recommends a focused ruling workbook for SCC-001. |
| Workbook output contract | Partially defined | Focused SCC-001 workbook path/name is TBD; minimum record columns are defined in `Procedure.md` Records pending the future workbook artifact. |
| Dependency row rulings | TBD | Handoff to RECONCILIATION / later source-grounded workflow. |
| Follow-up closure evidence | TBD | Requires a subsequent DepClosure scan after accepted row rulings, if any. |

#### Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| A-001 | Converted to TBD / HumanRuling. | ResponsibleParty remains unresolved because `_CONTEXT.md` lists `ResponsibleParty` as TBD and no authoritative owner is named in `DAG_CLOSURE_CONTROL.md` or the DepClosure snapshot. |

#### References

- `execution/PKG-00_DAG_Closure_and_Project_Control/README.md`
- `execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/Dependency_Closure_Report.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/RUN_SUMMARY.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/SCC_Triage_Notes.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/SCC_Triage_Workbook.csv`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/Evidence/scc_summary.csv`
- `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/Evidence/bidirectional_pairs.csv`

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/Guidance.md

### Guidance: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

#### Purpose

DEL-00-02 exists to keep SCC-001 closure work visible as a governed PKG-00 control deliverable while preserving the boundary between control-plane reconciliation and product dependency data. The current evidence says strict FULL_GRAPH is still cyclic, blocker-subset is acyclic, and SCC-001 remains the large runtime / SDK / session / tooling SCC to address after the smaller SCC-002 queue item.

Sources: `_CONTEXT.md` (Deliverable Scope), `README.md` (Purpose, Boundary), `DAG_CLOSURE_CONTROL.md` (Control Status, Current Queue), `Dependency_Closure_Report.md` (Verdict, Ruling).

#### Principles

- Treat the DepClosure snapshot as evidence of current graph state, not as authority to mutate rows by itself.
- Keep DEL-00-02 outside product dependency graph discovery.
- Preserve source-grounding: any row decision must cite the owning product dependency row and the evidence that justifies the ruling.
- Use existing dependency schema semantics only.
- Keep unresolved edge decisions as `TBD` / handoff items until RECONCILIATION or another approved workflow records evidence-backed rulings.

Sources: `DAG_CLOSURE_CONTROL.md` (Workflow), `SCC_Triage_Workbook.csv` (RecommendedAction, DoNotDo), `_DEPENDENCIES.md` (Boundary).

#### Considerations

- SCC-001 contains 18 nodes across PKG-03, PKG-04, PKG-05, and PKG-06 deliverables. The node list must be copied from the accepted DepClosure snapshot, not reconstructed from memory.
- `Evidence/bidirectional_pairs.csv` lists 13 bidirectional pairs overall; 12 are in SCC-001 and one is the separate SCC-002 pair.
- The current DepClosure report states that the canonical dependency ID migration was graph-neutral and that no dependency edge semantics were changed by the snapshot.
- `SCC_Triage_Workbook.csv` gives a default reading for SCC-001: generate a focused ruling workbook and classify each edge as hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only.
- The classification list is a triage vocabulary for the ruling workbook. It is not permission to invent new dependency schema values; every classification must be normalized into an allowed existing dependency-schema action or left `TBD` / `NEEDS_HUMAN_RULING` when the schema action is not evidenced.

Sources: `Evidence/scc_summary.csv`, `Evidence/bidirectional_pairs.csv`, `Dependency_Closure_Report.md` (Evidence Summary, Ruling), `SCC_Triage_Workbook.csv`.

#### Trade-offs

| Topic | Preferred Direction | Reason |
|---|---|---|
| Fast graph closure vs. evidence fidelity | Prefer evidence fidelity. | PKG-00 non-goals forbid inventing or deleting dependency edges merely to force DAG closure. |
| Control deliverable dependencies vs. product dependencies | Keep control dependencies unregistered in DEL-00-02. | Adding `Dependencies.csv` would promote the control deliverable into analyzer discovery. |
| Immediate mutation vs. ruling workbook | Produce the ruling workbook first. | The accepted workflow requires inspecting source-grounded rows before mutation. |
| Reporting project status vs. waiting for DepClosure | Wait for strict acyclic FULL_GRAPH evidence. | Current DepClosure evidence remains CYCLIC. |

#### Examples

- If a bidirectional pair represents duplicate reciprocal interface evidence, the ruling workbook may propose retiring or satisfying one side only after the owning row and source evidence support that decision.
- If a pair represents true hard sequencing in both directions, the ruling should remain `CONFLICT` or `TBD` until a human or RECONCILIATION resolves the model.
- If evidence shows a dependency is co-development-only and not a strict execution blocker, the ruling must still use existing schema fields and cite the source for that interpretation.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-DEL-00-02-001 | `DAG_CLOSURE_CONTROL.md` current queue labels DEL-00-02 as `SEMANTIC_READY`, but `_STATUS.md` was reset to `OPEN` before TASK regeneration because the prior semantic-ready state was provisional. | `DAG_CLOSURE_CONTROL.md` (Current Queue) | `_STATUS.md` (History) | Datasheet Identification; status handoff | Treat `_STATUS.md` as current lifecycle authority: P1/P2 evidence restored `INITIALIZED`, and successful Pass 3 may advance document-kit state to `SEMANTIC_READY`. | TBD |
| CONFLICT-DEL-00-02-002 | After Pass 3, `_STATUS.md` may be advanced to `SEMANTIC_READY`, but the owner for accepting SCC-001 rulings and the source location for existing dependency schema actions remain unresolved. | `_STATUS.md` (Current State after Pass 3) | `Datasheet.md` (ResponsibleParty); `Specification.md` (Standards) | Handoff state; future SCC-001 ruling workflow | Treat `SEMANTIC_READY` as document-kit readiness only; row rulings remain TBD until the owner and schema-action authority are resolved. | TBD |

#### Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Surfaced as conflict. | Conflict table now distinguishes document-kit lifecycle readiness from unresolved ruling authority, using `_STATUS.md`, `DAG_CLOSURE_CONTROL.md`, Datasheet Identification, and Specification Standards. |
| E-002 | Incorporated. | Considerations now state that triage categories must be normalized into existing dependency-schema actions or left `TBD` / `NEEDS_HUMAN_RULING`; supported by `SCC_Triage_Workbook.csv`, `SCC_Triage_Notes.md`, and Specification requirements. |

#### References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `README.md`
- `DAG_CLOSURE_CONTROL.md`
- `Dependency_Closure_Report.md`
- `SCC_Triage_Notes.md`
- `SCC_Triage_Workbook.csv`
- `Evidence/scc_summary.csv`
- `Evidence/bidirectional_pairs.csv`

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/Procedure.md

### Procedure: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

#### Purpose

Define the operational workflow for producing SCC-001 control records from the accepted DepClosure snapshot without mutating dependency edges during this four-document generation task.

#### Prerequisites

- Current accepted upstream snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/`.
- Required evidence files:
  - `Evidence/scc_summary.csv`
  - `Evidence/bidirectional_pairs.csv`
  - `SCC_Triage_Workbook.csv`
  - `Dependency_Closure_Report.md`
- `RUN_SUMMARY.md`
- DEL-00-02 remains a control deliverable with no `Dependencies.csv`.
- Access to owning product deliverable dependency registers and cited source evidence is required before any future row decision can be accepted; access owner/acquisition path remains TBD / HumanRuling.

Sources: `_REFERENCES.md`, `_DEPENDENCIES.md`, `DAG_CLOSURE_CONTROL.md` (Workflow), `SCC_Triage_Workbook.csv` (RecommendedAction).

#### Steps

1. Confirm the accepted upstream DepClosure snapshot path from `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md`.
2. Read `Dependency_Closure_Report.md` and `RUN_SUMMARY.md` to confirm strict FULL_GRAPH remains CYCLIC and blocker-subset remains ACYCLIC.
3. Read `Evidence/scc_summary.csv` and extract only the SCC-001 node set.
4. Read `Evidence/bidirectional_pairs.csv` and select the 12 pairs whose nodes are both in the SCC-001 node set.
5. Create the focused SCC-001 ruling workbook using the current bidirectional-pair evidence and the `SCC_Triage_Workbook.csv` directive. The workbook output path/name is TBD; until a human or approved workflow chooses a path, use a proposed record name of `SCC-001_Ruling_Workbook.csv` inside the DEL-00-02 control records without treating that proposal as authoritative.
6. For each workbook row, identify the owning product dependency row(s) and cited evidence source(s).
7. Classify each edge using the triage categories from `SCC_Triage_Workbook.csv`: hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only.
8. Convert each classification into an allowed existing dependency-schema action only when source evidence supports it. Otherwise mark the row `TBD` or `NEEDS_HUMAN_RULING`.
9. Apply accepted row changes only in the owning product deliverable registers, not in DEL-00-02.
10. Run a new DepClosure scan after accepted row changes.
11. Record the follow-up snapshot path, strict SCC verdict, remaining blockers, and handoff state in DEL-00-02 control records.

#### Verification

| Check | Expected Result |
|---|---|
| DEL-00-02 dependency register check | No `Dependencies.csv` exists in this folder. |
| Snapshot alignment | `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md` point to the same accepted DepClosure snapshot before workbook generation. |
| SCC node fidelity | Workbook SCC-001 nodes match `Evidence/scc_summary.csv`. |
| Bidirectional pair fidelity | Workbook input pairs are drawn from `Evidence/bidirectional_pairs.csv`; SCC-002 pair is excluded from SCC-001 rulings. |
| Source-grounding | Each proposed dependency row decision cites the owning row and supporting source evidence. |
| Schema discipline | No new dependency type or schema value is introduced. |
| Closure evidence | Follow-up DepClosure reports `scc_count = 0` and strict FULL_GRAPH acyclic before project-wide blocker state is reportable. |
| Follow-up snapshot record | Records include the immutable follow-up DepClosure snapshot path and strict FULL_GRAPH result after accepted row changes. |

#### Records

- Focused SCC-001 ruling workbook.
- Minimum workbook columns: `PairID`, `NodeA`, `NodeB`, `OwningRegisterPath`, `DependencyID`, `CurrentDependencyType`, `CurrentStatus`, `EvidenceCitation`, `TriageClassification`, `AllowedSchemaAction`, `Ruling`, `HumanRuling`, `RemainingBlockerStatus`, `Notes`.
- Per-row decision records with owning register path, dependency ID, source citation, ruling, and remaining blocker status.
- Product-register diffs for any accepted row changes.
- New immutable DepClosure snapshot, including the snapshot path and strict FULL_GRAPH result.
- Handoff state naming accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers.

#### Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| F-002 | Converted to TBD / HumanRuling. | Prerequisites now state that access owner/acquisition path for product registers and cited evidence remains unresolved; `_CONTEXT.md` has ResponsibleParty TBD. |
| D-001 | Incorporated with TBD authority boundary. | Steps and Records now define a proposed workbook name and minimum columns while preserving the authoritative output path/name as TBD. |
| E-001 | Incorporated. | Verification and Records now require recording the follow-up DepClosure snapshot path and strict FULL_GRAPH result; supported by `DAG_CLOSURE_CONTROL.md` Acceptance Condition and `Dependency_Closure_Report.md` Ruling. |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/Specification.md

### Specification: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

#### Scope

This deliverable specifies the control-plane work needed to prepare and record source-grounded rulings for SCC-001, the large strict FULL_GRAPH cycle spanning runtime, SDK, session, and tooling deliverables.

In scope:

- Consume the current DepClosure snapshot named in `_REFERENCES.md`.
- Use `Evidence/scc_summary.csv` to preserve the SCC-001 node set.
- Use `Evidence/bidirectional_pairs.csv` and `SCC_Triage_Workbook.csv` as the initial evidence queue for a focused SCC-001 ruling workbook.
- Record dependency row decisions and follow-up DepClosure evidence after source-grounded reconciliation work.

Out of scope:

- Creating `Dependencies.csv` for this DEL-00 control deliverable.
- Mutating dependency rows as part of this four-document generation task.
- Inventing new dependency types or edge semantics.
- Reporting project-wide `BLOCKED/UNBLOCKED` before strict FULL_GRAPH is acyclic.

Sources: `_CONTEXT.md` (Deliverable Scope, Source Authority), `_DEPENDENCIES.md` (Boundary), `README.md` (Boundary, Non-Goals), `DAG_CLOSURE_CONTROL.md` (Workflow, Acceptance Condition).

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-DEL-00-02-001 | The deliverable MUST remain a PKG-00 control artifact and MUST NOT be promoted into the product dependency graph by adding a deliverable-local `Dependencies.csv`. | `_CONTEXT.md` (Source Authority); `_DEPENDENCIES.md` (Boundary); `README.md` (Boundary) |
| REQ-DEL-00-02-002 | The SCC-001 workflow MUST consume the current DepClosure snapshot identified as `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431`. | `_REFERENCES.md` (Authoritative Source Corpus); `DAG_CLOSURE_CONTROL.md` (Control Status) |
| REQ-DEL-00-02-003 | The SCC-001 node set MUST be treated as the 18 nodes listed for SCC-001 in `Evidence/scc_summary.csv` unless superseded by a later accepted DepClosure snapshot. | `Evidence/scc_summary.csv`; `Dependency_Closure_Report.md` (Remaining SCCs) |
| REQ-DEL-00-02-004 | The next SCC-001 control output SHOULD be a focused ruling workbook generated from current bidirectional-pair evidence. | `DAG_CLOSURE_CONTROL.md` (Current Queue); `SCC_Triage_Workbook.csv` (SCC-001 row); `SCC_Triage_Notes.md` (SCC-001 Initial Reading) |
| REQ-DEL-00-02-005 | Dependency row decisions MUST inspect owning product deliverable dependency registers and cited source evidence before any row mutation. | `DAG_CLOSURE_CONTROL.md` (Workflow); `SCC_Triage_Workbook.csv` (RecommendedAction); `_DEPENDENCIES.md` (Declared Upstream) |
| REQ-DEL-00-02-006 | Edge classifications MUST use existing dependency schema semantics only; new dependency types MUST NOT be invented. | `SCC_Triage_Workbook.csv` (RecommendedAction); `SCC_Triage_Notes.md` (SCC-001 Initial Reading) |
| REQ-DEL-00-02-007 | Closure MUST be evidenced by a follow-up DepClosure scan showing strict `scc_count = 0`, strict FULL_GRAPH acyclic, and blocker state reportable by ORCHESTRATOR. | `DAG_CLOSURE_CONTROL.md` (Acceptance Condition); `Dependency_Closure_Report.md` (Ruling) |
| REQ-DEL-00-02-008 | Current dependency closure decisions for SCC-001 remain TBD / handoff until source-grounded evidence supports explicit rulings. | INIT-TASK CustomInstructions; `SCC_Triage_Workbook.csv` (RecommendedAction) |
| REQ-DEL-00-02-009 | The focused SCC-001 ruling workbook MUST include the 12 bidirectional pairs whose nodes are both in SCC-001 and MUST exclude the SCC-002 pair. | `Evidence/scc_summary.csv`; `Evidence/bidirectional_pairs.csv`; `SCC_Triage_Workbook.csv` (SCC-001 row) |
| REQ-DEL-00-02-010 | The handoff record MUST name the accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers. | `AGENTS.md` (Handoff-state rule, Closure rule); `Procedure.md` (Records) |

#### Standards

| Standard / Control | Applicability | Location |
|---|---|---|
| PKG-00 control package boundary | Governs this deliverable's control-only status and exclusion from product graph discovery. | `README.md` (Boundary) |
| DepClosure snapshot evidence | Governs current SCC status, node set, bidirectional-pair queue, and acyclic/cyclic verdicts. | `Dependency_Closure_Report.md`; `Evidence/*.csv`; `closure_summary.json` |
| Existing dependency schema actions and fields | Governs future row decisions in owning product deliverable registers. | Source location TBD / HumanRuling required before row-classification work; cited by `DAG_CLOSURE_CONTROL.md` workflow and `SCC_Triage_Workbook.csv` directive |

#### Verification

| Requirement | Verification Approach |
|---|---|
| REQ-DEL-00-02-001 | Confirm this folder still has no `Dependencies.csv` and remains marked `EXCLUDED_CONTROL_DELIVERABLE` in `_DEPENDENCIES.md`. |
| REQ-DEL-00-02-002 | Confirm `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md` point to the same current DepClosure snapshot. |
| REQ-DEL-00-02-003 | Compare the focused ruling workbook node set to `Evidence/scc_summary.csv`. |
| REQ-DEL-00-02-004 | Confirm ruling workbook rows are derived from `Evidence/bidirectional_pairs.csv` and `SCC_Triage_Workbook.csv`. |
| REQ-DEL-00-02-005 | For each proposed row decision, record the owning product dependency row and cited source evidence. |
| REQ-DEL-00-02-006 | Review each classification against existing dependency schema values before applying product-register changes. |
| REQ-DEL-00-02-007 | Run DepClosure after accepted row updates and verify strict SCC count is 0 before project-wide reporting. |
| REQ-DEL-00-02-008 | Treat unresolved SCC-001 decisions as handoff items until RECONCILIATION or an approved task records source-grounded rulings. |
| REQ-DEL-00-02-009 | Count workbook input pairs against `Evidence/bidirectional_pairs.csv`: accept only the 12 pairs whose endpoints both appear in the SCC-001 node set from `Evidence/scc_summary.csv`; confirm the `DEL-10-02` / `DEL-10-03` SCC-002 pair is excluded. |
| REQ-DEL-00-02-010 | Confirm the handoff state explicitly records accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers before downstream use. |

#### Documentation

Required records:

- Focused SCC-001 ruling workbook.
- Per-row decision records citing owning product registers and source evidence.
- Updated product `Dependencies.csv` rows only where evidence supports change.
- Follow-up DepClosure snapshot and closure report.
- Handoff state naming accepted upstream snapshot, derivative status, closure verdict, rerun requirements, and remaining blockers.

#### Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| B-001 | Incorporated. | Added `REQ-DEL-00-02-009` and matching verification from `Evidence/scc_summary.csv`, `Evidence/bidirectional_pairs.csv`, and `SCC_Triage_Workbook.csv`. |
| F-001 | Converted to TBD / HumanRuling. | Standards now preserve the unresolved source location for existing dependency schema actions and fields; no local source slice identified the governing schema location in this run. |
| X-001 | Incorporated. | Added `REQ-DEL-00-02-010` and matching verification for handoff-state fields using the governance rules supplied in the task instructions and the existing Procedure Records section. |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/Case_Datasheet.md

### Case Datasheet: CASE-SCC-001 Runtime SDK Session Tooling

| Field | Value |
| --- | --- |
| CaseID | CASE-SCC-001 |
| CaseTitle | Runtime SDK Session Tooling |
| CaseState | DEP_CLOSURE_PENDING |
| OwningControlDeliverable | DEL-00-02 |
| SCCBaseline | SCC-001 from `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/` |
| AffectedDeliverables | DEL-03-01; DEL-03-02; DEL-03-03; DEL-03-04; DEL-04-01; DEL-04-02; DEL-04-03; DEL-04-04; DEL-04-05; DEL-05-01; DEL-05-02; DEL-05-03; DEL-05-05; DEL-06-01; DEL-06-02; DEL-06-03; DEL-06-04; DEL-06-06 |
| SeedEvidence | `case-seeds/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/`; `case-seeds/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/`; `case-seeds/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/` |
| WorkingModel | Living SCC resolution case; seed packets retained as prior evidence, normalized into a ruling workbook and dispatch plan |
| ClosureAuthority | Future accepted DepClosure snapshot with `scc_count = 0` only |
| LatestDepClosureSnapshot | `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320/` |
| LatestDepClosureVerdict | Graph reduction only; `scc_count = 1`, residual SCC size `6`, bidirectional pairs `0` |
| ResidualRulingPackage | `SCC-001_Residual_Ruling_Package.md` |
| LongerCycleRulingPackage | `SCC-001_Longer_Cycle_Ruling_Package.md` |

#### Evidence Baseline

The seed evidence records a large runtime, SDK, session, audit, permission, tooling, hook, and MCP SCC. This case reframes the packets as evidence categories rather than final remedies, because the work needs iterative TASK findings across affected deliverables and human rulings about which impacts require SCOPE_CHANGE, dependency workflow action, reconciliation, or no scope mutation.

#### Current Readiness

The case has indexed bounded WORKING_ITEMS/TASK evidence for runtime/SDK core packet `002`, session/audit records packet `003`, and tooling/permissions/MCP packet `004`. `SCC-001_Ruling_Workbook.csv` normalized the 12 bidirectional pairs and longer-cycle cross-links into row-level ruling candidates. CHANGE implemented the dependency-workflow-ready tranche for `REM-SCC-001-006`, `007`, `008`, `009`, `011`, `013`, `014`, and `016`; then CHANGE implemented the human-approved residual bidirectional-pair tranche for `REM-SCC-001-005`, `010`, `012`, and `015`. AUDIT_DEP_CLOSURE snapshot `CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320` proves all bidirectional pairs are removed, but a six-node longer-cycle SCC remains. `SCC-001_Longer_Cycle_Ruling_Package.md` records the next proposed row treatments and awaits human approval. The case is not closed and is not a SCOPE_CHANGE intake by itself.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Datasheet.md

### Packet Datasheet: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Identity

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-002 |
| PacketTitle | SCC-001 Runtime SDK Core |
| SCC_ID | SCC-001 |
| DecompositionVariant | SOFTWARE |
| PacketStatus | READY_FOR_HUMAN_REVIEW |
| DerivativePackage | Yes |
| AcceptedUpstreamSnapshot | `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |

#### SCC Baseline

DepClosure reports SCC-001 as an 18-node strict SCC in the runtime, SDK, session, and tooling area. This packet focuses on the requested runtime SDK core subset, not the full SCC-001 node set.

Focused affected deliverables:

`DEL-03-01`; `DEL-03-02`; `DEL-03-03`; `DEL-03-04`; `DEL-04-01`; `DEL-04-02`; `DEL-04-03`; `DEL-04-04`; `DEL-04-05`

Focused bidirectional pairs:

| Pair | Current Packet Reading |
|---|---|
| DEL-03-01 <-> DEL-03-04 | Runtime contract conformance and interrupt terminal outcome handling are mutually referenced. |
| DEL-03-01 <-> DEL-04-01 | SDK probe evidence and product-owned runtime contract expectations are mutually referenced. |
| DEL-03-03 <-> DEL-03-04 | SSE/API compatibility and interrupt terminal handling are mutually referenced. |
| DEL-03-03 <-> DEL-04-03 | Browser-facing UI events and SDK message mapping are mutually referenced. |
| DEL-04-02 <-> DEL-04-04 | SDK options/settings and persona composition exchange interface inputs. |

#### Evidence Inventory

Primary evidence is indexed in `Evidence_Index.csv`. Owning product registers identify concrete candidate rows such as `DEP-03-01-003`, `DEP-03-01-006`, `DEP-03-04-006`, `DEP-03-03-007`, `DEP-03-03-009`, `DEP-04-03-009`, `DEP-04-02-007`, and `DEP-04-04-004`.

#### Current Rulings

| Topic | Ruling |
|---|---|
| Focus rows | TBD until SCOPE_CHANGE or RECONCILIATION selects row-level rulings. |
| Dependency-edge treatment | Insufficient by itself because several rows encode interface evidence or handoff evidence rather than hard sequencing. |
| Product-register mutation | Out of scope for this packet. |
| Closure verdict | TBD; requires later accepted amendments and DepClosure rerun. |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Intake Procedure

1. Human reviews this packet and decides whether to initiate SCOPE_CHANGE.
2. If initiated, use `SCOPE_CHANGE_INIT.md` as the seed request.
3. Load the accepted upstream DepClosure snapshot and decomposition authority named in the datasheet.
4. Review `Evidence_Index.csv` and the owning product dependency registers listed in `Affected_Surfaces.csv`.
5. For each action in `Proposed_SCA_Actions.csv`, decide whether it is accepted, rejected, split, merged, or left `TBD`.

#### Gate-by-Gate Use

| Gate | Required Packet Use |
|---|---|
| Intake | Confirm the request is human-initiated and bounded to SCC-001 runtime SDK core. |
| Evidence | Verify each proposed action has cited evidence. |
| Impact | Check all affected deliverables and files before any amendment. |
| Amendment | Apply only accepted SCOPE_CHANGE actions through the owning workflow. |
| Verification | Run dependency validation and DepClosure after accepted changes. |
| Handoff | Record accepted snapshot, derivative-package status, closure verdict, rerun requirements, and blockers. |

#### Required Reviews

- Runtime contract owner review for `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, and `DEL-03-04`.
- SDK adapter owner review for `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-04`, and `DEL-04-05`.
- RECONCILIATION or SCOPE_CHANGE review for row-level direction and dependency-type rulings.

#### Stop Conditions

- Missing owning register evidence.
- Disagreement between decomposition authority and product deliverable registers.
- Attempt to report SCC closure or project-wide blocker state from this packet.
- Attempt to alter product dependency rows outside an accepted SCOPE_CHANGE workflow.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Specification.md

### Packet Specification: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Scope

This packet specifies conservative candidate amendments for runtime engine, SDK adapter, provider/settings, mapper/options, and turn lifecycle integration concerns in the SCC-001 runtime SDK core subset.

#### Proposed Amendment Requirements

| ID | Requirement | Evidence |
|---|---|---|
| REQ-PKT-002-001 | SCOPE_CHANGE intake must distinguish hard sequencing prerequisites from interface evidence in runtime contract, SDK probe, mapper, options, and lifecycle rows. | E-001; E-002; E-004 |
| REQ-PKT-002-002 | Any amendment must preserve `AgentEnginePort` / `RuntimeEngineContract` as the product-owned boundary while allowing SDK probe evidence to inform adapter fixtures. | E-003; E-005; E-008 |
| REQ-PKT-002-003 | Any amendment must preserve stable `/api/harness/*` and SSE/UIEvent compatibility while SDK message mapping remains adapter-owned. | E-003; E-009; E-010 |
| REQ-PKT-002-004 | Any amendment must clarify the options/persona boundary so `SdkOptionsBuilder` owns settings isolation while `PersonaComposer` owns prompt material. | E-003; E-011 |
| REQ-PKT-002-005 | Provider key, base URL, and provider error handoff must remain redacted and provider-neutral where crossing mapper/runtime surfaces. | E-003; E-012 |

#### Action Candidates

The authoritative action table is `Proposed_SCA_Actions.csv`. Candidate actions are intentionally conservative. Rows marked `TBD` require human or SCOPE_CHANGE gate rulings before implementation.

#### Acceptance Criteria

- The SCOPE_CHANGE intake names the accepted DepClosure snapshot and decomposition authority.
- Proposed row-level changes cite owning product registers.
- Interface evidence is not converted into prerequisite sequencing without source-grounded ruling.
- Provider/settings and mapper/options concerns remain scoped to PKG-04 boundaries unless SCOPE_CHANGE approves a structural amendment.
- Any accepted amendment is followed by a DepClosure rerun before closure reporting.

#### Invariant Checks

- This packet remains derivative and non-authoritative.
- Product deliverables and `Dependencies.csv` files are not modified by this packet.
- `_ScopeChange`, `_Reconciliation`, and decomposition files are not modified by this packet.
- Unknown row disposition remains `TBD`.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Datasheet.md

### Packet Datasheet: SCC-001 Session Audit Records

#### Identification

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-003 |
| SCC_ID | SCC-001 |
| FocusRows | TBD |
| BidirectionalPairs | DEL-03-04<->DEL-05-02; DEL-04-05<->DEL-05-03; DEL-05-02<->DEL-05-03 |
| ReadinessTarget | READY_FOR_HUMAN_REVIEW |

#### SCC Baseline

DepClosure evidence records SCC-001 as an 18-node strict-cycle set. The requested packet subset focuses on six affected deliverables and three bidirectional pairs. The packet uses the accepted snapshot as evidence only and does not update graph state.

#### Affected Deliverables

| Deliverable | Role In Packet | Evidence |
|---|---|---|
| DEL-03-04 | Interrupt, cancel, failure cleanup, and terminal outcome semantics. | E-006; E-007 |
| DEL-04-05 | Provider key/base URL/network bridge and provider-boundary error redaction. | E-006; E-009 |
| DEL-05-01 | Canonical session folder, legacy session migration, SDK session link, transcript placement. | E-006; E-011 |
| DEL-05-02 | HarnessEvent schema, accepted-turn and terminal-event JSONL, session event placement. | E-006; E-008 |
| DEL-05-03 | Redacted run logging, secret hygiene, redaction before persistence. | E-006; E-010 |
| DEL-05-05 | ToolResultStore, session artifacts, output budget policy, artifact references. | E-006; E-012 |

#### Evidence Inventory

Evidence is indexed in `Evidence_Index.csv`. The core evidence set is:

- DepClosure SCC and bidirectional-pair files for SCC-001.
- The SOFTWARE v3.2 decomposition authority.
- Affected product deliverable dependency registers.
- Affected deliverable context/status surfaces confirming scope identity and current SEMANTIC_READY state.

#### Unresolved Fields

- `FOCUS_ROWS`: TBD in the brief.
- Terminal taxonomy ruling for interruption versus cancellation metadata: TBD.
- Exact SDK transcript placement and store linkage details: TBD.
- Final redaction helper/run logger module paths and configured-secret schema: TBD.
- ToolResultStore implementation location and budget policy parameters: TBD.

#### Substantiation Boundary

This datasheet substantiates packet structure, affected surfaces, and evidence pointers. It does not substantiate row-level rulings, a SCOPE_CHANGE amendment, SCC closure, or project-wide blocker state.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-003

#### Intake Use

1. Confirm the human wants to initiate SCOPE_CHANGE for SCC-001 session/audit records.
2. Use `SCOPE_CHANGE_INIT.md` as a seed, not as an active request before that confirmation.
3. Load `Evidence_Index.csv` first, then `Affected_Surfaces.csv`, then `Proposed_SCA_Actions.csv`.
4. Preserve this packet as a derivative package tied to the cited DepClosure snapshot.

#### Gate-by-Gate Procedure

##### Gate 1: Intake

- Verify packet identity and requested SCC.
- Confirm write authority for any later SCOPE_CHANGE workflow.
- Preserve all unresolved rulings as `TBD`.

##### Gate 2: Impact Analysis

- Inspect the three bidirectional pairs cited by the brief.
- Confirm affected deliverable ownership in the decomposition authority.
- Inspect product dependency registers as read-only evidence unless SCOPE_CHANGE explicitly authorizes mutation.

##### Gate 3: Amendment Design

- Consider candidate `MODIFY` actions only as conservative proposals.
- Decide whether pair evidence should remain sequencing, become interface-only, be marked satisfied, or require a different action type.
- Keep secret hygiene and audit durability as invariant constraints.

##### Gate 4: Validation

- After any accepted upstream changes, run DepClosure again from the owning workflow.
- Record the new immutable snapshot and link it in the SCOPE_CHANGE handoff.
- Do not use this packet as a substitute for a new closure scan.

##### Gate 5: Handoff

- State accepted upstream snapshot(s), derivative package status, unresolved blockers, and rerun requirements.
- Record whether packet actions were accepted, revised, rejected, or deferred.

#### Records

- Packet folder: `scope-change-packets/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/`
- Run record: `_run_records/TASK_RUN_2026-05-24_1600.md`
- Validation command: `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_scope_change_packet.py "$PACKET_PATH"`


## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Specification.md

### Packet Specification: SCC-001 Session Audit Records

#### Proposed Amendment Requirements

1. Preserve Chirality-owned `HarnessEvent` JSONL as the canonical product audit surface for accepted turns, runtime events, and terminal outcomes.
2. Preserve SDK transcripts as secondary artifacts unless SCOPE_CHANGE explicitly accepts imported transcript material as `HarnessEvent` evidence.
3. Clarify that terminal outcome semantics owned by DEL-03-04 must be representable in DEL-05-02 JSONL without forcing final implementation sequencing before SCOPE_CHANGE rulings.
4. Clarify that DEL-05-03 redaction constraints apply before provider errors, SDK messages, run logs, and sensitive tool-result previews enter persistent audit or artifact records.
5. Clarify that DEL-05-01 owns canonical session folder/storage linkage, while DEL-05-02 owns event JSONL semantics and DEL-05-05 owns large tool-result artifact storage.
6. Leave unresolved row-level and design rulings as `TBD` until SCOPE_CHANGE review accepts, rejects, or revises the candidate actions.

#### Action Candidates

The normative candidate list is `Proposed_SCA_Actions.csv`. All candidates are `MODIFY` actions because current evidence supports clarification and ruling preparation, not direct structural removal, merge, split, or row mutation by this packet.

#### Interface Invariants

| Invariant | Affected Deliverables | Evidence |
|---|---|---|
| Terminal outcomes must be durable and replayable. | DEL-03-04; DEL-05-02 | E-002; E-007; E-008 |
| Event persistence must not leak secrets. | DEL-05-02; DEL-05-03 | E-004; E-008; E-010 |
| Provider-boundary failures must be classified and redacted. | DEL-04-05; DEL-05-03 | E-003; E-009; E-010 |
| Session JSONL placement depends on canonical session folder layout. | DEL-05-01; DEL-05-02 | E-008; E-011 |
| Large tool outputs should be artifact-referenced rather than flooding chat/model context. | DEL-05-02; DEL-05-03; DEL-05-05 | E-008; E-010; E-012 |

#### Acceptance Criteria For Later SCOPE_CHANGE

- Human explicitly initiates SCOPE_CHANGE using or revising `SCOPE_CHANGE_INIT.md`.
- Each affected edge or metadata clarification receives a source-grounded ruling.
- Any accepted mutation is applied by the owning workflow, not by this packet.
- A follow-up DepClosure snapshot is generated after accepted upstream changes.
- Residual `TBD` items are carried into the handoff state rather than silently resolved.


## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Datasheet.md

### Packet Datasheet: PKG00-SCA-PACKET-004

#### Baseline

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-004 |
| PacketTitle | SCC-001 Tooling Permissions MCP |
| SCC_ID | SCC-001 |
| DepClosure Snapshot | `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Decomposition Authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Focus Rows | TBD |

#### SCC Evidence Summary

DepClosure evidence identifies SCC-001 as an 18-node runtime/SDK/session/tooling SCC. The focused packet surface covers the PKG-06 subset: `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`, and `DEL-06-06`.

The current bidirectional-pair evidence includes these packet-relevant pairs:

| Pair | Packet Concern |
|---|---|
| DEL-06-01 <-> DEL-06-02 | Permission overlay versus SDK read tool resolver exposure. |
| DEL-06-01 <-> DEL-06-03 | Permission overlay versus in-process Chirality MCP read tools. |
| DEL-06-01 <-> DEL-06-04 | Permission overlay versus write/edit gate and path hook results. |
| DEL-06-04 <-> DEL-06-06 | Write/edit hook enforcement versus hook lifecycle and compaction mirror evidence. |

#### Affected Deliverables

| Deliverable | Decomposition Role | Current Local State |
|---|---|---|
| DEL-06-01 | ChiralityPermissionOverlay and Mode Mapping | SEMANTIC_READY |
| DEL-06-02 | SDK Read Tool Surface and Tool Validation | SEMANTIC_READY |
| DEL-06-03 | Initial Chirality MCP Read Tools | SEMANTIC_READY |
| DEL-06-04 | Write/Edit Surface and Path Hooks | SEMANTIC_READY |
| DEL-06-06 | Hook Lifecycle and Compaction Mirror | SEMANTIC_READY |

#### Evidence Inventory

| EvidenceID | Short Description |
|---|---|
| E-001 | Decomposition PKG-06 and DEL-06-01 through DEL-06-06 scope rows. |
| E-002 | DepClosure SCC summary identifying SCC-001 membership. |
| E-003 | DepClosure bidirectional-pair evidence for PKG-06 pairs. |
| E-004 | SCC triage recommendation to classify SCC-001 edges without inventing new dependency types. |
| E-005 | DEL-06-01 dependency register rows for permission overlay interfaces. |
| E-006 | DEL-06-02 dependency register rows for read surface dependency on overlay and MCP definitions. |
| E-007 | DEL-06-03 dependency register rows for MCP read tools and permission/event integration. |
| E-008 | DEL-06-04 dependency register rows for write/edit path hooks and lifecycle handoff. |
| E-009 | DEL-06-06 dependency register rows for hook lifecycle, JSONL event dependency, and compaction mirror. |
| E-010 | Affected deliverable statuses showing SEMANTIC_READY without dependency closure. |

#### Open Rulings

- Whether SCC-001 pair treatment can be resolved by dependency-row classification alone or requires decomposition amendment: TBD.
- Exact runtime event writer/session JSONL append API owner for permission and MCP tool events: TBD.
- Exact status lifecycle API owner for MCP status read behavior: TBD.
- Exact hook lifecycle mapper module path, payload fields, and validation fixture paths: TBD.
- REF-006 `docs/PRD.md` hash mismatch disposition for PRD-only tool, write, hook, and compaction details: TBD.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-004

#### Intake Procedure

1. Confirm a human explicitly initiates SCOPE_CHANGE using or adapting `SCOPE_CHANGE_INIT.md`.
2. Load the cited decomposition authority and DepClosure snapshot.
3. Verify SCC-001 membership and the packet-relevant bidirectional pairs.
4. Review affected product deliverable `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and four-doc kit files before accepting any action.
5. Decide whether the issue is decomposition text, dependency classification, handoff-state wording, or no amendment.
6. Record unresolved rulings as `TBD`; do not infer approval from this packet.

#### Gate-by-Gate Use

| Gate | Action |
|---|---|
| Gate 1 Evidence | Validate `Evidence_Index.csv` paths and references. |
| Gate 2 Impact | Compare `Affected_Surfaces.csv` against live affected deliverable files. |
| Gate 3 Amendment Design | Select or revise `Proposed_SCA_Actions.csv` rows. |
| Gate 4 Application | Apply changes only inside the authorized SCOPE_CHANGE write scope. |
| Gate 5 Verification | Re-run relevant dependency closure checks and record a new governed snapshot if accepted. |

#### Operator Notes

- If a later workflow mutates dependency registers, cite the exact row IDs and pre/post evidence in that workflow.
- If a later workflow amends decomposition scope, cite the accepted upstream decomposition and produce the required snapshot or pointer update.
- If REF-006 remains hash-mismatched, keep PRD-only implementation details warning-qualified.
- Do not use this packet to report a global graph state.

#### Packet Handoff State

| Field | Value |
|---|---|
| Accepted upstream snapshot | DepClosure `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Derivative package status | Derivative SCOPE_CHANGE consumable packet |
| Closure verdict | Not a closure artifact |
| Rerun requirements | Re-run packet validation after any manual edit; run dependency closure only in authorized workflow |
| Remaining blockers | Human SCOPE_CHANGE initiation and all `TBD` rulings |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/case-seeds/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Specification.md

### Packet Specification: PKG00-SCA-PACKET-004

#### Proposed Amendment Requirements

1. Preserve deny-first permission overlay ownership in DEL-06-01 while clarifying that read tool resolution, MCP wrapper metadata, write/edit path hooks, and hook lifecycle mirrors are adjacent integration surfaces, not substitutes for permission policy.
2. Classify the packet-relevant SCC-001 bidirectional pairs as hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only using existing dependency schema fields.
3. Keep read-first sequencing explicit: SDK read tools and initial Chirality MCP read tools may be exposed before write/edit/bash capability, but exposure does not bypass the permission overlay.
4. Keep write/edit capability gated by project-root containment, instruction-root block, symlink rejection, exact edit preconditions, provenance hooks, and accepted permission results.
5. Keep hook lifecycle and compaction mirror integration tied to HarnessEvent/JSONL event contracts, terminal outcome behavior, and validation handoff without embedding path-enforcement ownership in DEL-06-06.

#### Proposed Action Candidates

The action candidates are listed in `Proposed_SCA_Actions.csv`. They use `MODIFY` for clarification-oriented amendments and `TBD` where the action depends on a human or SCOPE_CHANGE ruling.

#### Acceptance Criteria For Later SCOPE_CHANGE

- Each accepted action cites current evidence and records any replacement or superseding snapshot.
- No action treats this packet as a direct edit authority.
- Any dependency-row changes, if approved later, are performed only by the authorized dependency or SCOPE_CHANGE workflow.
- Any decomposition amendment preserves accepted PKG-06 deliverable ownership unless SCOPE_CHANGE explicitly approves a different ownership boundary.
- PRD-only implementation details remain warning-qualified until REF-006 source-state reconciliation is resolved.

#### Invariant Checks

| Invariant | Required Treatment |
|---|---|
| Permission overlay is authoritative for allow/deny decisions | Preserve DEL-06-01 as the policy owner. |
| `allowedTools` is not a restriction boundary by itself | Keep overlay, hooks, callbacks, and event persistence in scope. |
| MCP tools are not bypasses | Route `mcp__chirality__*` through the same permission, hook, redaction, and event policy. |
| Read tools precede write/edit/bash capability | Keep DEL-06-02 and DEL-06-03 read-first boundaries explicit. |
| Write/edit needs path hooks | Preserve DEL-06-04 containment and precondition ownership. |
| Compaction and hook lifecycle are audit events | Preserve DEL-06-06 mirror ownership and event-contract dependency. |

#### Unresolved Specification Items

- Exact dependency rows requiring amendment: TBD.
- Whether pair evidence should be treated as duplicate reciprocal evidence or co-development-only for each edge: TBD.
- Exact implementation paths and test fixture names: TBD.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Datasheet.md

### Packet Datasheet: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Identity

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-002 |
| PacketTitle | SCC-001 Runtime SDK Core |
| SCC_ID | SCC-001 |
| DecompositionVariant | SOFTWARE |
| PacketStatus | READY_FOR_HUMAN_REVIEW |
| DerivativePackage | Yes |
| AcceptedUpstreamSnapshot | `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |

#### SCC Baseline

DepClosure reports SCC-001 as an 18-node strict SCC in the runtime, SDK, session, and tooling area. This packet focuses on the requested runtime SDK core subset, not the full SCC-001 node set.

Focused affected deliverables:

`DEL-03-01`; `DEL-03-02`; `DEL-03-03`; `DEL-03-04`; `DEL-04-01`; `DEL-04-02`; `DEL-04-03`; `DEL-04-04`; `DEL-04-05`

Focused bidirectional pairs:

| Pair | Current Packet Reading |
|---|---|
| DEL-03-01 <-> DEL-03-04 | Runtime contract conformance and interrupt terminal outcome handling are mutually referenced. |
| DEL-03-01 <-> DEL-04-01 | SDK probe evidence and product-owned runtime contract expectations are mutually referenced. |
| DEL-03-03 <-> DEL-03-04 | SSE/API compatibility and interrupt terminal handling are mutually referenced. |
| DEL-03-03 <-> DEL-04-03 | Browser-facing UI events and SDK message mapping are mutually referenced. |
| DEL-04-02 <-> DEL-04-04 | SDK options/settings and persona composition exchange interface inputs. |

#### Evidence Inventory

Primary evidence is indexed in `Evidence_Index.csv`. Owning product registers identify concrete candidate rows such as `DEP-03-01-003`, `DEP-03-01-006`, `DEP-03-04-006`, `DEP-03-03-007`, `DEP-03-03-009`, `DEP-04-03-009`, `DEP-04-02-007`, and `DEP-04-04-004`.

#### Current Rulings

| Topic | Ruling |
|---|---|
| Focus rows | TBD until SCOPE_CHANGE or RECONCILIATION selects row-level rulings. |
| Dependency-edge treatment | Insufficient by itself because several rows encode interface evidence or handoff evidence rather than hard sequencing. |
| Product-register mutation | Out of scope for this packet. |
| Closure verdict | TBD; requires later accepted amendments and DepClosure rerun. |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Intake Procedure

1. Human reviews this packet and decides whether to initiate SCOPE_CHANGE.
2. If initiated, use `SCOPE_CHANGE_INIT.md` as the seed request.
3. Load the accepted upstream DepClosure snapshot and decomposition authority named in the datasheet.
4. Review `Evidence_Index.csv` and the owning product dependency registers listed in `Affected_Surfaces.csv`.
5. For each action in `Proposed_SCA_Actions.csv`, decide whether it is accepted, rejected, split, merged, or left `TBD`.

#### Gate-by-Gate Use

| Gate | Required Packet Use |
|---|---|
| Intake | Confirm the request is human-initiated and bounded to SCC-001 runtime SDK core. |
| Evidence | Verify each proposed action has cited evidence. |
| Impact | Check all affected deliverables and files before any amendment. |
| Amendment | Apply only accepted SCOPE_CHANGE actions through the owning workflow. |
| Verification | Run dependency validation and DepClosure after accepted changes. |
| Handoff | Record accepted snapshot, derivative-package status, closure verdict, rerun requirements, and blockers. |

#### Required Reviews

- Runtime contract owner review for `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, and `DEL-03-04`.
- SDK adapter owner review for `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-04`, and `DEL-04-05`.
- RECONCILIATION or SCOPE_CHANGE review for row-level direction and dependency-type rulings.

#### Stop Conditions

- Missing owning register evidence.
- Disagreement between decomposition authority and product deliverable registers.
- Attempt to report SCC closure or project-wide blocker state from this packet.
- Attempt to alter product dependency rows outside an accepted SCOPE_CHANGE workflow.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-002_SCC-001_Runtime_SDK_Core/Packet_Specification.md

### Packet Specification: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

#### Scope

This packet specifies conservative candidate amendments for runtime engine, SDK adapter, provider/settings, mapper/options, and turn lifecycle integration concerns in the SCC-001 runtime SDK core subset.

#### Proposed Amendment Requirements

| ID | Requirement | Evidence |
|---|---|---|
| REQ-PKT-002-001 | SCOPE_CHANGE intake must distinguish hard sequencing prerequisites from interface evidence in runtime contract, SDK probe, mapper, options, and lifecycle rows. | E-001; E-002; E-004 |
| REQ-PKT-002-002 | Any amendment must preserve `AgentEnginePort` / `RuntimeEngineContract` as the product-owned boundary while allowing SDK probe evidence to inform adapter fixtures. | E-003; E-005; E-008 |
| REQ-PKT-002-003 | Any amendment must preserve stable `/api/harness/*` and SSE/UIEvent compatibility while SDK message mapping remains adapter-owned. | E-003; E-009; E-010 |
| REQ-PKT-002-004 | Any amendment must clarify the options/persona boundary so `SdkOptionsBuilder` owns settings isolation while `PersonaComposer` owns prompt material. | E-003; E-011 |
| REQ-PKT-002-005 | Provider key, base URL, and provider error handoff must remain redacted and provider-neutral where crossing mapper/runtime surfaces. | E-003; E-012 |

#### Action Candidates

The authoritative action table is `Proposed_SCA_Actions.csv`. Candidate actions are intentionally conservative. Rows marked `TBD` require human or SCOPE_CHANGE gate rulings before implementation.

#### Acceptance Criteria

- The SCOPE_CHANGE intake names the accepted DepClosure snapshot and decomposition authority.
- Proposed row-level changes cite owning product registers.
- Interface evidence is not converted into prerequisite sequencing without source-grounded ruling.
- Provider/settings and mapper/options concerns remain scoped to PKG-04 boundaries unless SCOPE_CHANGE approves a structural amendment.
- Any accepted amendment is followed by a DepClosure rerun before closure reporting.

#### Invariant Checks

- This packet remains derivative and non-authoritative.
- Product deliverables and `Dependencies.csv` files are not modified by this packet.
- `_ScopeChange`, `_Reconciliation`, and decomposition files are not modified by this packet.
- Unknown row disposition remains `TBD`.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Datasheet.md

### Packet Datasheet: SCC-001 Session Audit Records

#### Identification

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-003 |
| SCC_ID | SCC-001 |
| FocusRows | TBD |
| BidirectionalPairs | DEL-03-04<->DEL-05-02; DEL-04-05<->DEL-05-03; DEL-05-02<->DEL-05-03 |
| ReadinessTarget | READY_FOR_HUMAN_REVIEW |

#### SCC Baseline

DepClosure evidence records SCC-001 as an 18-node strict-cycle set. The requested packet subset focuses on six affected deliverables and three bidirectional pairs. The packet uses the accepted snapshot as evidence only and does not update graph state.

#### Affected Deliverables

| Deliverable | Role In Packet | Evidence |
|---|---|---|
| DEL-03-04 | Interrupt, cancel, failure cleanup, and terminal outcome semantics. | E-006; E-007 |
| DEL-04-05 | Provider key/base URL/network bridge and provider-boundary error redaction. | E-006; E-009 |
| DEL-05-01 | Canonical session folder, legacy session migration, SDK session link, transcript placement. | E-006; E-011 |
| DEL-05-02 | HarnessEvent schema, accepted-turn and terminal-event JSONL, session event placement. | E-006; E-008 |
| DEL-05-03 | Redacted run logging, secret hygiene, redaction before persistence. | E-006; E-010 |
| DEL-05-05 | ToolResultStore, session artifacts, output budget policy, artifact references. | E-006; E-012 |

#### Evidence Inventory

Evidence is indexed in `Evidence_Index.csv`. The core evidence set is:

- DepClosure SCC and bidirectional-pair files for SCC-001.
- The SOFTWARE v3.2 decomposition authority.
- Affected product deliverable dependency registers.
- Affected deliverable context/status surfaces confirming scope identity and current SEMANTIC_READY state.

#### Unresolved Fields

- `FOCUS_ROWS`: TBD in the brief.
- Terminal taxonomy ruling for interruption versus cancellation metadata: TBD.
- Exact SDK transcript placement and store linkage details: TBD.
- Final redaction helper/run logger module paths and configured-secret schema: TBD.
- ToolResultStore implementation location and budget policy parameters: TBD.

#### Substantiation Boundary

This datasheet substantiates packet structure, affected surfaces, and evidence pointers. It does not substantiate row-level rulings, a SCOPE_CHANGE amendment, SCC closure, or project-wide blocker state.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-003

#### Intake Use

1. Confirm the human wants to initiate SCOPE_CHANGE for SCC-001 session/audit records.
2. Use `SCOPE_CHANGE_INIT.md` as a seed, not as an active request before that confirmation.
3. Load `Evidence_Index.csv` first, then `Affected_Surfaces.csv`, then `Proposed_SCA_Actions.csv`.
4. Preserve this packet as a derivative package tied to the cited DepClosure snapshot.

#### Gate-by-Gate Procedure

##### Gate 1: Intake

- Verify packet identity and requested SCC.
- Confirm write authority for any later SCOPE_CHANGE workflow.
- Preserve all unresolved rulings as `TBD`.

##### Gate 2: Impact Analysis

- Inspect the three bidirectional pairs cited by the brief.
- Confirm affected deliverable ownership in the decomposition authority.
- Inspect product dependency registers as read-only evidence unless SCOPE_CHANGE explicitly authorizes mutation.

##### Gate 3: Amendment Design

- Consider candidate `MODIFY` actions only as conservative proposals.
- Decide whether pair evidence should remain sequencing, become interface-only, be marked satisfied, or require a different action type.
- Keep secret hygiene and audit durability as invariant constraints.

##### Gate 4: Validation

- After any accepted upstream changes, run DepClosure again from the owning workflow.
- Record the new immutable snapshot and link it in the SCOPE_CHANGE handoff.
- Do not use this packet as a substitute for a new closure scan.

##### Gate 5: Handoff

- State accepted upstream snapshot(s), derivative package status, unresolved blockers, and rerun requirements.
- Record whether packet actions were accepted, revised, rejected, or deferred.

#### Records

- Packet folder: `scope-change-packets/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/`
- Run record: `_run_records/TASK_RUN_2026-05-24_1600.md`
- Validation command: `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_scope_change_packet.py "$PACKET_PATH"`


## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-003_SCC-001_Session_Audit_Records/Packet_Specification.md

### Packet Specification: SCC-001 Session Audit Records

#### Proposed Amendment Requirements

1. Preserve Chirality-owned `HarnessEvent` JSONL as the canonical product audit surface for accepted turns, runtime events, and terminal outcomes.
2. Preserve SDK transcripts as secondary artifacts unless SCOPE_CHANGE explicitly accepts imported transcript material as `HarnessEvent` evidence.
3. Clarify that terminal outcome semantics owned by DEL-03-04 must be representable in DEL-05-02 JSONL without forcing final implementation sequencing before SCOPE_CHANGE rulings.
4. Clarify that DEL-05-03 redaction constraints apply before provider errors, SDK messages, run logs, and sensitive tool-result previews enter persistent audit or artifact records.
5. Clarify that DEL-05-01 owns canonical session folder/storage linkage, while DEL-05-02 owns event JSONL semantics and DEL-05-05 owns large tool-result artifact storage.
6. Leave unresolved row-level and design rulings as `TBD` until SCOPE_CHANGE review accepts, rejects, or revises the candidate actions.

#### Action Candidates

The normative candidate list is `Proposed_SCA_Actions.csv`. All candidates are `MODIFY` actions because current evidence supports clarification and ruling preparation, not direct structural removal, merge, split, or row mutation by this packet.

#### Interface Invariants

| Invariant | Affected Deliverables | Evidence |
|---|---|---|
| Terminal outcomes must be durable and replayable. | DEL-03-04; DEL-05-02 | E-002; E-007; E-008 |
| Event persistence must not leak secrets. | DEL-05-02; DEL-05-03 | E-004; E-008; E-010 |
| Provider-boundary failures must be classified and redacted. | DEL-04-05; DEL-05-03 | E-003; E-009; E-010 |
| Session JSONL placement depends on canonical session folder layout. | DEL-05-01; DEL-05-02 | E-008; E-011 |
| Large tool outputs should be artifact-referenced rather than flooding chat/model context. | DEL-05-02; DEL-05-03; DEL-05-05 | E-008; E-010; E-012 |

#### Acceptance Criteria For Later SCOPE_CHANGE

- Human explicitly initiates SCOPE_CHANGE using or revising `SCOPE_CHANGE_INIT.md`.
- Each affected edge or metadata clarification receives a source-grounded ruling.
- Any accepted mutation is applied by the owning workflow, not by this packet.
- A follow-up DepClosure snapshot is generated after accepted upstream changes.
- Residual `TBD` items are carried into the handoff state rather than silently resolved.


## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Datasheet.md

### Packet Datasheet: PKG00-SCA-PACKET-004

#### Baseline

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-004 |
| PacketTitle | SCC-001 Tooling Permissions MCP |
| SCC_ID | SCC-001 |
| DepClosure Snapshot | `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Decomposition Authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Focus Rows | TBD |

#### SCC Evidence Summary

DepClosure evidence identifies SCC-001 as an 18-node runtime/SDK/session/tooling SCC. The focused packet surface covers the PKG-06 subset: `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`, and `DEL-06-06`.

The current bidirectional-pair evidence includes these packet-relevant pairs:

| Pair | Packet Concern |
|---|---|
| DEL-06-01 <-> DEL-06-02 | Permission overlay versus SDK read tool resolver exposure. |
| DEL-06-01 <-> DEL-06-03 | Permission overlay versus in-process Chirality MCP read tools. |
| DEL-06-01 <-> DEL-06-04 | Permission overlay versus write/edit gate and path hook results. |
| DEL-06-04 <-> DEL-06-06 | Write/edit hook enforcement versus hook lifecycle and compaction mirror evidence. |

#### Affected Deliverables

| Deliverable | Decomposition Role | Current Local State |
|---|---|---|
| DEL-06-01 | ChiralityPermissionOverlay and Mode Mapping | SEMANTIC_READY |
| DEL-06-02 | SDK Read Tool Surface and Tool Validation | SEMANTIC_READY |
| DEL-06-03 | Initial Chirality MCP Read Tools | SEMANTIC_READY |
| DEL-06-04 | Write/Edit Surface and Path Hooks | SEMANTIC_READY |
| DEL-06-06 | Hook Lifecycle and Compaction Mirror | SEMANTIC_READY |

#### Evidence Inventory

| EvidenceID | Short Description |
|---|---|
| E-001 | Decomposition PKG-06 and DEL-06-01 through DEL-06-06 scope rows. |
| E-002 | DepClosure SCC summary identifying SCC-001 membership. |
| E-003 | DepClosure bidirectional-pair evidence for PKG-06 pairs. |
| E-004 | SCC triage recommendation to classify SCC-001 edges without inventing new dependency types. |
| E-005 | DEL-06-01 dependency register rows for permission overlay interfaces. |
| E-006 | DEL-06-02 dependency register rows for read surface dependency on overlay and MCP definitions. |
| E-007 | DEL-06-03 dependency register rows for MCP read tools and permission/event integration. |
| E-008 | DEL-06-04 dependency register rows for write/edit path hooks and lifecycle handoff. |
| E-009 | DEL-06-06 dependency register rows for hook lifecycle, JSONL event dependency, and compaction mirror. |
| E-010 | Affected deliverable statuses showing SEMANTIC_READY without dependency closure. |

#### Open Rulings

- Whether SCC-001 pair treatment can be resolved by dependency-row classification alone or requires decomposition amendment: TBD.
- Exact runtime event writer/session JSONL append API owner for permission and MCP tool events: TBD.
- Exact status lifecycle API owner for MCP status read behavior: TBD.
- Exact hook lifecycle mapper module path, payload fields, and validation fixture paths: TBD.
- REF-006 `docs/PRD.md` hash mismatch disposition for PRD-only tool, write, hook, and compaction details: TBD.

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Procedure.md

### Packet Procedure: PKG00-SCA-PACKET-004

#### Intake Procedure

1. Confirm a human explicitly initiates SCOPE_CHANGE using or adapting `SCOPE_CHANGE_INIT.md`.
2. Load the cited decomposition authority and DepClosure snapshot.
3. Verify SCC-001 membership and the packet-relevant bidirectional pairs.
4. Review affected product deliverable `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and four-doc kit files before accepting any action.
5. Decide whether the issue is decomposition text, dependency classification, handoff-state wording, or no amendment.
6. Record unresolved rulings as `TBD`; do not infer approval from this packet.

#### Gate-by-Gate Use

| Gate | Action |
|---|---|
| Gate 1 Evidence | Validate `Evidence_Index.csv` paths and references. |
| Gate 2 Impact | Compare `Affected_Surfaces.csv` against live affected deliverable files. |
| Gate 3 Amendment Design | Select or revise `Proposed_SCA_Actions.csv` rows. |
| Gate 4 Application | Apply changes only inside the authorized SCOPE_CHANGE write scope. |
| Gate 5 Verification | Re-run relevant dependency closure checks and record a new governed snapshot if accepted. |

#### Operator Notes

- If a later workflow mutates dependency registers, cite the exact row IDs and pre/post evidence in that workflow.
- If a later workflow amends decomposition scope, cite the accepted upstream decomposition and produce the required snapshot or pointer update.
- If REF-006 remains hash-mismatched, keep PRD-only implementation details warning-qualified.
- Do not use this packet to report a global graph state.

#### Packet Handoff State

| Field | Value |
|---|---|
| Accepted upstream snapshot | DepClosure `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Derivative package status | Derivative SCOPE_CHANGE consumable packet |
| Closure verdict | Not a closure artifact |
| Rerun requirements | Re-run packet validation after any manual edit; run dependency closure only in authorized workflow |
| Remaining blockers | Human SCOPE_CHANGE initiation and all `TBD` rulings |

## Component: execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scope-change-packets/PKG00-SCA-PACKET-004_SCC-001_Tooling_Permissions_MCP/Packet_Specification.md

### Packet Specification: PKG00-SCA-PACKET-004

#### Proposed Amendment Requirements

1. Preserve deny-first permission overlay ownership in DEL-06-01 while clarifying that read tool resolution, MCP wrapper metadata, write/edit path hooks, and hook lifecycle mirrors are adjacent integration surfaces, not substitutes for permission policy.
2. Classify the packet-relevant SCC-001 bidirectional pairs as hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only using existing dependency schema fields.
3. Keep read-first sequencing explicit: SDK read tools and initial Chirality MCP read tools may be exposed before write/edit/bash capability, but exposure does not bypass the permission overlay.
4. Keep write/edit capability gated by project-root containment, instruction-root block, symlink rejection, exact edit preconditions, provenance hooks, and accepted permission results.
5. Keep hook lifecycle and compaction mirror integration tied to HarnessEvent/JSONL event contracts, terminal outcome behavior, and validation handoff without embedding path-enforcement ownership in DEL-06-06.

#### Proposed Action Candidates

The action candidates are listed in `Proposed_SCA_Actions.csv`. They use `MODIFY` for clarification-oriented amendments and `TBD` where the action depends on a human or SCOPE_CHANGE ruling.

#### Acceptance Criteria For Later SCOPE_CHANGE

- Each accepted action cites current evidence and records any replacement or superseding snapshot.
- No action treats this packet as a direct edit authority.
- Any dependency-row changes, if approved later, are performed only by the authorized dependency or SCOPE_CHANGE workflow.
- Any decomposition amendment preserves accepted PKG-06 deliverable ownership unless SCOPE_CHANGE explicitly approves a different ownership boundary.
- PRD-only implementation details remain warning-qualified until REF-006 source-state reconciliation is resolved.

#### Invariant Checks

| Invariant | Required Treatment |
|---|---|
| Permission overlay is authoritative for allow/deny decisions | Preserve DEL-06-01 as the policy owner. |
| `allowedTools` is not a restriction boundary by itself | Keep overlay, hooks, callbacks, and event persistence in scope. |
| MCP tools are not bypasses | Route `mcp__chirality__*` through the same permission, hook, redaction, and event policy. |
| Read tools precede write/edit/bash capability | Keep DEL-06-02 and DEL-06-03 read-first boundaries explicit. |
| Write/edit needs path hooks | Preserve DEL-06-04 containment and precondition ownership. |
| Compaction and hook lifecycle are audit events | Preserve DEL-06-06 mirror ownership and event-contract dependency. |

#### Unresolved Specification Items

- Exact dependency rows requiring amendment: TBD.
- Whether pair evidence should be treated as duplicate reciprocal evidence or co-development-only for each edge: TBD.
- Exact implementation paths and test fixture names: TBD.
