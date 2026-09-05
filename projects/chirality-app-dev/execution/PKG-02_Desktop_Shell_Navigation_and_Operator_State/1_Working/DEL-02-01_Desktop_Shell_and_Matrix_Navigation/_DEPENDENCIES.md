# Dependencies: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted declared dependency edges have been provided.

## Declared Downstream

TBD - no accepted declared dependency edges have been provided.

## Extracted Dependency Register

Summary:

| Count Type | Value |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ANCHOR rows | 4 |
| EXECUTION rows | 10 |

Compact register:

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-02-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-02 Woven Dialogue Shell, Navigation, and Operator State | ACTIVE |
| DEP-02-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-001 Dialogue-centred shell: invariant centre dialogue, left chat navigator, one-view-at-a-time right panel, no header row | ACTIVE |
| DEP-02-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-005 Semantic persona/agent/session routing, guarded dialogue selection, and legacy route/query/alias/matrix compatibility | ACTIVE |
| DEP-02-01-004 | ANCHOR | OTHER | UPSTREAM | OBJ-001 Governed local desktop harness centred on human-agent dialogue as the invariant primary surface | ACTIVE |
| DEP-02-01-005 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN/TBD existing implementation workspace | ACTIVE |
| DEP-02-01-006 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract | ACTIVE |
| DEP-02-01-007 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX | ACTIVE |
| DEP-02-01-008 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-08-03 Pipeline Category and Task Scope Dispatch | ACTIVE |
| DEP-02-01-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-01 Working Root Validation and Instruction Root Protection | ACTIVE |
| DEP-02-01-010 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 Additive v1 workspace-state field contract (per-view widths, expand state, chat annotations, known folders, chat rung, declined triggers) | ACTIVE |
| DEP-02-01-011 | EXECUTION | INTERFACE | UPSTREAM | EXTERNAL/TBD Root-owned daemon session record (registered project identity/root; delegation-policy field, OI-008) | ACTIVE |
| DEP-02-01-012 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN/TBD existing redaction helper for derived chat titles (Q6) | ACTIVE |
| DEP-02-01-013 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-04 macOS DMG Packaging and Instruction Root Integrity | ACTIVE |
| DEP-02-01-014 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-01-03 Product Identity and Professional Boundary Copy | ACTIVE |

## Run Notes

### 2026-09-05 D-APP-110 decompose of DEP-02-01-010 (UPDATE)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N14-TASK-DEL-02-01` (TASK + dependency-extract, apply mode, dispatched by HELP_HUMAN under owner ruling D-APP-110, `execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`; `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.3_SCC_DECOMPOSE.md` node N14; workbook `SCC_DECOMPOSE_RULINGS.csv` row SD-002). Pre-images verified before the write: `Dependencies.csv` `8d5315713a86732e44b4a9287e8632be03347d50ceb1d2ed7889c2b90cc8883e`, `_DEPENDENCIES.md` `f6a50a4513cc2d5895d81fe93a4b9ee45e43714f1a16234adf7c188b52e2c517`.
- Runtime overrides: as the D-APP-109 emission run (`SCOPE=DEL-02-01_Desktop_Shell_and_Matrix_Navigation`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`) with `ApplyEdits=true`. No extraction from prose: the run applies the recorded `decompose` move (`docs/CYCLE_DRIVEN_RESOLUTION.md` section 2.3, in the `SCC-SAFE-MOVES-001` form of `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/`) to the one workbook row this carrier holds.
- DECOMPOSE under D-APP-110 (SD-002): DEP-02-01-010 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (`TargetType=DOCUMENT`; `TargetPackageID` and `TargetDeliverableID` cleared; `TargetName` "Additive v1 workspace-state field contract (per-view widths, expand state, chat annotations, known folders, chat rung, declined triggers)"; `TargetLocation` `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; `LastSeen=2026-09-05`; the decompose clause appended to `Notes`). The coarse deliverable edge DEL-02-01->DEL-02-04 is replaced by the document-scoped contract; the deliverable relation to DEL-02-04 is preserved in `Notes` as evidence; the row stays `ACTIVE` with its evidence, class, direction, type, and `SatisfactionStatus=TBD` unchanged; every other row is byte-identical; no row added, retired, cut, merged, or inverted.
- Contract anchor verified before the write: DEL-02-04 `ScopeOfWork.md` (SHA-256 `2ebfe14aa3bf354b79111c5e0d4bc81b3e10e8292195d8c8aad5464a7f99cc8c`, read-only) carries `## SCA-APP-010 Gate-5 Current Contract (Controlling)` at L68 and `### Current acceptance obligations` item 1 (additive v1 fields under the existing schema string with rollback-safe migration) at L99; the applied row outputs there name the workspace-state schema (additive v1 fields).
- Resolution note on other D-APP-109 rows this carrier holds: none required (DEP-02-01-010 was this carrier's only D-APP-109 emission, and it is the re-targeted row).
- Decomposition authority: FOUND at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); DEL-02-04 applied row L310 unchanged.
- Source-preservation gate: `ScopeOfWork.md` `0e64cb085ee7032844f3b09f05c5a3f29ba02344e3ce9369a8535657c793406b` read-only and unchanged; the row's evidence `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling); Current acceptance obligations 4` (L73 / L102 / L107) still carries the `EvidenceQuote` verbatim.
- Graph effect: per D-APP-110 the strict active deliverable execution graph is acyclic after the five-edge decompose set (workbook SD-001 to SD-007, seven rows across six carriers); this carrier no longer holds a cycle-participating row, and every row gates per its `SatisfactionStatus`. The fresh AUDIT_DEP_CLOSURE run (amendment v1.3 node N16) records the acyclic graph and the move basis; acceptance of that snapshot as the loop's DepClosure pointer remains a separate owner act.
- HGD-1, HGD-2, HGD-3 and fenced candidates FC-1 to FC-3 are unchanged by this run; D-APP-110 rules none of them.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit `validate_id_format.sh` profile rejects the accepted App two-digit identities; no ID changed).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row.
- Schema validation: PASS (`validate_dependencies_schema.py`: 29 columns, 14 data rows; the DOCUMENT row leaves `TargetDeliverableID` blank as the schema requires). Enum validation: `TARGET_TYPE DOCUMENT` VALID (the only changed enum value); the other nine enum values on the row are unchanged and re-checked VALID. Counts: this file keeps no target-type tally; ACTIVE, class, type, and satisfaction counts are unchanged (14 ACTIVE / 4 ANCHOR / 10 EXECUTION).

### 2026-09-05 D-APP-109 emission of the held row H-001 (UPDATE)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N9-TASK-DEL-02-01` (TASK + dependency-extract, apply mode, dispatched by HELP_HUMAN under owner ruling D-APP-109, `execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`, and `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.2_OWNER_RULING.md` node N9; SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-001/DEP-002). Pre-images verified before the write: `Dependencies.csv` `4af3d115b79d403c190661ba57050abe9bda04539cadf09cf9b07edf2d49c254`, `_DEPENDENCIES.md` `26a99f29ef68e00a9cc02839802142f099f67f7c5816cb461971a9ccb9a3ef49`.
- Runtime overrides: as the 2026-09-05 preview run (`SCOPE=DEL-02-01_Desktop_Shell_and_Matrix_Navigation`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`) with `ApplyEdits=true`. No new extraction from prose: the run authors only the reserved row DEP-02-01-010 from the held proposal H-001 (`instances/N1-TASK-DEL-02-01/PREVIEW.md` section "Held proposals (amendment v1.1)"; `HELD_EDGE_PROPOSALS.csv` H-001), with the epistemic note preserved verbatim and the D-APP-109 non-gating clause appended.
- Decomposition authority: FOUND at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); DEL-02-04 applied row L310 supplies `TargetName` "Dialogue Toolkit, Context, and Local UI State"; reverse view L407 (SOW-004) and L411 (SOW-008) map DEL-02-04. `TargetLocation` follows this register's sibling DELIVERABLE rows (plain decomposition path, no line pointer).
- Emitted: DEP-02-01-010 (DEL-02-01 UPSTREAM INTERFACE on DEL-02-04) inserted at its numeric position; every existing row byte-identical; no row retired; `Status=CANDIDATE` not emitted; `FromDeliverableID=DEL-02-01` on every row.
- Source-preservation gate: `ScopeOfWork.md` `0e64cb085ee7032844f3b09f05c5a3f29ba02344e3ce9369a8535657c793406b` read-only and unchanged; the evidence `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` (L73), `### Current acceptance obligations` (L102), item 4 (L107) carries the `EvidenceQuote` verbatim.
- Graph effect (recorded, not resolved): per D-APP-109 and the fan-in simulation `Evidence/fanin_simulation_v1/`, emitting the nineteen held rows across nine carriers merges the nine-node SCC-001 into an enlarged SCC that includes DEL-02-01 (through DEP-02-01-010 -> DEL-02-04 and the reciprocal DEP-02-04-017). DEP-02-01-010 is cycle-participating and non-gating (no blocker queue, wave placement, dispatch-readiness, or implementation-readiness effect) until that SCC is resolved by a recorded decompose, invert, merge, or cut move (`docs/CYCLE_DRIVEN_RESOLUTION.md`); the fresh AUDIT_DEP_CLOSURE run (amendment v1.2 node N11) records the post-emission picture. The "F1: DEL-02-04 reaches no SCC-001 member" statement in the row's `Notes` is the held proposal's pre-emission finding, preserved verbatim; the [INFO] SCC_EXPOSURE bullet below is dated to the preview.
- HGD-1, HGD-2, HGD-3 and fenced candidates FC-1 to FC-3 are unchanged by this run; D-APP-109 rules none of them.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit `validate_id_format.sh` profile rejects the accepted App two-digit identities; no ID changed).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row.
- Schema validation: PASS (`validate_dependencies_schema.py`: 29 columns, 14 data rows). Enum validation: all 10 enum values on the emitted row VALID. Evidence: the emitted `EvidenceFile#SourceRef` resolves to live bytes and the quote appears there.

### 2026-09-05 SCA-APP-010 dependency closure, report-only preview (UPDATE)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N1-TASK-DEL-02-01` (TASK + dependency-extract, dispatched by HELP_HUMAN; SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-001/DEP-002). This text is the proposed post-image written under the instance folder; the carrier register was not written by this run (pre-images `Dependencies.csv` `5ca2d96b48ac962d4a9f9afef8bc07957fcac81889fc1ba441b94d899bcacd99`, `_DEPENDENCIES.md` `f60ddd1687e169bf3c0904f361d09601f4c9e7fa6a0966f939a92e90f8c83109`).
- Runtime overrides: `SCOPE=DEL-02-01_Desktop_Shell_and_Matrix_Navigation`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ApplyEdits=false`.
- Decomposition authority: FOUND at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (the `ScopeOfWork.md` `decomposition_basis` pin); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (SCA-APP-010); authority corpus v20 with no drift per `_REFERENCES.md`. Basis commit `d66395d101143df68d956984f7ab93f5027418ec`.
- Source selection: `_STATUS.md` was read as an execution source only for `## Remaining` (seated items DEL-02-01-V3-01 to V3-04: Depends, Write locus, gate, and Return lines); `_REFERENCES.md` resolved pointers only; `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` were excluded. Other deliverable folders were opened only to confirm target existence and quote applied rows.
- Source-preservation gate: `ScopeOfWork.md` `0e64cb085ee7032844f3b09f05c5a3f29ba02344e3ce9369a8535657c793406b`, `_CONTEXT.md` `0d49f00c1970043e0143e2344256ccf27bd381f15326bdb994d49c29a8ddbb44`, `_STATUS.md` `95456161eb746267676eaf24759a542a3ec748980d863c49ced9fae343eca306`, `_REFERENCES.md` `97c89e3a36cdf3aff74f489312ac699617b49a33ac8e9903a8de5900759e9638` were read-only and unchanged.
- Pass 1 (ANCHOR): parent anchor DEP-02-01-001 preserved and refreshed to the applied PKG-02 label (L280). Trace anchors DEP-02-01-002 (SOW-001), DEP-02-01-003 (SOW-005), and DEP-02-01-004 (OBJ-001) preserved with applied labels (L404, L408, L262). The applied carrier row L307 carries only SOW-001 and SOW-005; SOW-081 to SOW-084 are not on this carrier, so no anchor was added and no anchor was retired. The existing `TargetType=REQUIREMENT` convention for the objective anchor is preserved.
- Pass 2 (EXECUTION): DEP-02-01-005 to DEP-02-01-008 re-evidenced from the retired legacy kit (`Procedure.md`, `Guidance.md`) to live `ScopeOfWork.md#CLM-018` and `#CLM-027`, `LastSeen=2026-09-05`; five rows added (DEP-02-01-009 and DEP-02-01-011 to DEP-02-01-014) from amended SOW-002/SOW-008/SOW-010, the applied row prose, and the owner-seated Remaining items; the ID DEP-02-01-010 is reserved for a held proposal (see the amendment v1.1 bullets below) and is not emitted. No row retired; every `DependencyID` preserved; `Status=CANDIDATE` not emitted; `FromDeliverableName` refreshed to the applied name on every row.
- Fence F1 (SCC-001 membership): PASS for the emitted rows; simulation S0 keeps SCC-001 at its nine nodes and DEL-02-01 outside it. Candidates not emitted: FC-1 redaction helper resolved to DEL-05-03; FC-2 session-record binding resolved to DEL-03-02; FC-3 account-row host interface to DEL-02-05 and the DEL-02-05-V3-05 gate. Each would merge DEL-02-01, DEL-04-02, DEL-04-04, and DEL-08-02 into a thirteen-node SCC because every SCC-001 member already reaches DEL-02-01 through DEP-02-01-006 (DEL-04-04 to DEL-08-02 to DEL-02-01).
- Fence F2 (Root path): NONE. Root-owned targets are `EXTERNAL` with `TargetLocation=TBD`; `frontend/**` implementation paths named by CLM-021 and the seated write loci are not placed in `TargetLocation`.
- Fence F3 (permitted effect): NONE. No row was derived from SCC ordering, schedule, or keep-aligned statements; the Electron/D-APP-98 IPC constraint and the SOW-002 DEL-02-03 touchpoint split were not emitted.
- NEEDS_HUMAN_GRAPH_DECISION: HGD-1 DEP-02-01-006 direction (recorded DOWNSTREAM HANDOVER versus UPSTREAM INTERFACE per reverse view L408 and CLM-015; inverting removes all SCC-001 reachability into DEL-02-01, simulation S1). HGD-2 DEP-02-01-007 and DEP-02-01-008 retire-or-keep after SCA-APP-010 retired Workbench and Pipeline presentation from the active shell (DEC-025; L171, L177, L308, L370, L410). HGD-3 the DEL-02-01-V3-01 prerequisite on DEL-02-02-V3-03 (woven route): emitting it with DEP-02-02-005 and DEP-02-01-007 present creates a new four-node SCC {DEL-02-01, DEL-02-02, DEL-08-02, DEL-08-03} (simulation S2); held non-gating and not emitted; resolution options decompose / invert / merge / cut per `docs/CYCLE_DRIVEN_RESOLUTION.md`.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` three-digit profile rejects the accepted App two-digit identities (`DEL-02-01`, `PKG-02`, `DEP-02-01-NNN`, `SOW-NNN`); no ID was changed.
- [WARNING] UNKNOWN_IMPLEMENTATION_WORKSPACE: DEP-02-01-005 keeps `TargetType=UNKNOWN`, `TargetLocation=TBD`.
- [WARNING] TARGET_UNRESOLVED: DEP-02-01-012 keeps `TargetType=UNKNOWN` because the only explicit resolution (DEL-05-03) is fenced by F1.
- [INFO] SCC_EXPOSURE: DEL-02-01 has no path into SCC-001, but all nine SCC-001 members reach DEL-02-01 through DEP-02-01-006; any UPSTREAM row into SCC-001 or into a node that reaches it makes DEL-02-01 a member.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row.
- Schema validation: PASS (`validate_dependencies_schema.py`: 29 columns, 14 data rows). Enum validation: 25 distinct (enum, value) pairs VALID. Evidence: every ACTIVE row resolves to a live heading or claim ID.
- Graph check disclosure: reachability and SCC simulations reused the functions of `tools/coordination/analyze_dep_closure.py` from the session scratchpad (read-only; not a skill-allowlisted tool; no repository write).
- Legacy warnings from 2026-05-20: PRD_HASH_MISMATCH resolved (REF-006 MATCH under D-APP-38); PACKAGE_PATH_MISMATCH resolved (physical folder name intentionally retained per `_REFERENCES.md` Notes); ROUTE_SEMANTICS_SOURCE_POINTER remains CLM-030 CONFLICT-003 for human ruling and is not a dependency edge.
- Amendment v1.1 (HELP_HUMAN, `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`, rerun instance `N1-TASK-DEL-02-01`): the fan-in simulation over all thirteen N1 post-images (`Evidence/fanin_simulation_v1/`) showed that the proposed DEL-02-01 -> DEL-02-04 edge lies on a cycle collectively with fourteen other newly proposed edges (with the DEL-02-04 preview's reciprocal DEP-02-04-017 it forms a new deliverable-level pair); choosing which to keep would be a cut, which `docs/CYCLE_DRIVEN_RESOLUTION.md` makes human-gated, so the row is held non-emitted and removed from this post-image. Counts in this file are reconciled to the thirteen-row post-image. HGD-1, HGD-2, and HGD-3 are unchanged and carried to the owner slate (amendment section C item 5).
- EMITTED under D-APP-109 (H-001): DEP-02-01-010 — DEL-02-01 UPSTREAM INTERFACE on DEL-02-04 (Dialogue Toolkit, Context, and Local UI State; chat navigator and composer read and write known folders, chat annotations, and the chat rung as DEL-02-04-owned local convenience state; `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling); Current acceptance obligations 4`; amended SOW-008 L178, SOW-004 L174; AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-001) — cycle-participating, non-gating until the SCC is resolved by a recorded move

### 2026-05-20 initial extraction (retained as dated history)

- Runtime overrides: `SCOPE=DEL-02-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- `_SEMANTIC.md` was not read or consumed. Semantic lensing and P3 enrichment were skipped by human ruling.
- Anchor doc selection: `Datasheet.md`, supplemented by `_CONTEXT.md` and decomposition validation.
- Execution doc order: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- No declared edges were found in the existing dependency index; all register rows in this run are `Origin=EXTRACTED`.
- Parent anchor check: PASS. Exactly one ACTIVE `IMPLEMENTS_NODE` row exists.
- Schema validation: PASS. `validate_dependencies_schema.py` reported 29 required columns and 8 data rows.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records `REF-006` with `Status=HASH_MISMATCH`; treated as a source warning, not a blocker, per local source instructions.
- [WARNING] PACKAGE_PATH_MISMATCH: `Guidance.md` records a package path mismatch requiring later human ruling; this run wrote only inside the assigned `ScopePath`.
- [WARNING] ROUTE_SEMANTICS_SOURCE_POINTER: `Guidance.md` records an unresolved PRD/SPEC/TYPES source-pointer issue; dependency extraction used only concrete local evidence and preserved open ruling status.
- [WARNING] UNKNOWN_IMPLEMENTATION_WORKSPACE: `Procedure.md` requires an implementation workspace, but exact implementation paths are `TBD`; row `DEP-02-01-005` preserves `TargetType=UNKNOWN`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Path | Decomposition Status | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|---|
| 2026-05-20T19:24:24-06:00 | UPDATE | CONSERVATIVE | `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND | PRD_HASH_MISMATCH; PACKAGE_PATH_MISMATCH; ROUTE_SEMANTICS_SOURCE_POINTER; UNKNOWN_IMPLEMENTATION_WORKSPACE | ANCHOR=4; EXECUTION=4; TOTAL=8 |
| 2026-09-05 | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND at pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`) | PROJECT_ID_FORMAT_PROFILE; UNKNOWN_IMPLEMENTATION_WORKSPACE; TARGET_UNRESOLVED; NEEDS_HUMAN_GRAPH_DECISION HGD-1..HGD-3; FENCE_F1_CANDIDATES FC-1..FC-3; HELD H-001 (DEP-02-01-010 reserved, amendment v1.1) (report-only preview) | ANCHOR=4; EXECUTION=9; TOTAL=13 |
| 2026-09-05T07:58-0600 (D-APP-109 emission) | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND at pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`) | PROJECT_ID_FORMAT_PROFILE; UNKNOWN_IMPLEMENTATION_WORKSPACE; TARGET_UNRESOLVED; NEEDS_HUMAN_GRAPH_DECISION HGD-1..HGD-3 (unchanged); FENCE_F1_CANDIDATES FC-1..FC-3 (unchanged); CYCLE_PARTICIPATING DEP-02-01-010 (H-001 emitted under D-APP-109; non-gating pending SCC resolution by a recorded move) | ANCHOR=4; EXECUTION=10; TOTAL=14 |
| 2026-09-05T10:14-0600 (D-APP-110 decompose) | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND at pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (`dbd812a52d5ed0cb3ed173f3aaaa68703a914291`) | PROJECT_ID_FORMAT_PROFILE; UNKNOWN_IMPLEMENTATION_WORKSPACE; TARGET_UNRESOLVED; NEEDS_HUMAN_GRAPH_DECISION HGD-1..HGD-3 (unchanged); FENCE_F1_CANDIDATES FC-1..FC-3 (unchanged); DECOMPOSED DEP-02-01-010 (SD-002 under D-APP-110; DOCUMENT target DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1; no cycle-participating row remains) | ANCHOR=4; EXECUTION=10; TOTAL=14 |

## Lifecycle Summary

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 14 |
| Status | RETIRED | 0 |
| SatisfactionStatus | NOT_APPLICABLE | 4 |
| SatisfactionStatus | TBD | 9 |
| SatisfactionStatus | PENDING | 1 |
| DependencyType | OTHER | 4 |
| DependencyType | PREREQUISITE | 1 |
| DependencyType | HANDOVER | 2 |
| DependencyType | INTERFACE | 6 |
| DependencyType | CONSTRAINT | 1 |
| DependencyClass | ANCHOR | 4 |
| DependencyClass | EXECUTION | 10 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor, three trace anchors, four legacy-kit rows re-evidenced to live `ScopeOfWork.md` claims (DEP-02-01-005 to 008), and six added rows (DEP-02-01-009 to 014); zero retired rows. DEP-02-01-010 (emitted under D-APP-109 from held proposal H-001) is decomposed under D-APP-110 (SD-002): its target is the DOCUMENT contract DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 at DEL-02-04 `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, and the deliverable relation to DEL-02-04 is preserved in its `Notes` as evidence.
- This carrier no longer holds a cycle-participating row: under D-APP-110 the strict active deliverable execution graph is acyclic, and every row in this register gates per its `SatisfactionStatus` exactly like every other strict edge (DEP-02-01-010 at `TBD`). The seated items' own Depends lines and named gates remain the executable ordering for LOOP_INIT Step 1.
- Owner rulings still open: HGD-1 (DEP-02-01-006 direction), HGD-2 (DEP-02-01-007/008 retire or keep as compatibility-only), HGD-3 (DEL-02-02-V3-03 prerequisite, held non-gating, not emitted). Fenced candidates FC-1 to FC-3 stay out of the register unless separately ruled.
- Reconcile with the DEL-02-02 register (its reverse row DEP-02-02-005 and this register's DEP-02-01-007 are the matrix-era pair that HGD-2 and HGD-3 turn on) and with the DEL-02-04 register (the reciprocal DEP-02-04-017, emitted under D-APP-109 as held proposal H-010, is ruled for the same decompose to DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 under D-APP-110 SD-003 on its own carrier).
- SCC picture: DEL-02-01 is outside any SCC after the D-APP-110 decompose (strict graph acyclic; no row retired, cut, merged, or inverted; no decomposition topology changed); the fresh AUDIT_DEP_CLOSURE snapshot (amendment v1.3 node N16) is the authoritative post-move record, and its acceptance as the loop's DepClosure pointer remains a separate owner act.
