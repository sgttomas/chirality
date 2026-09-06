# Dependencies: DEL-02-04 Dialogue Toolkit, Context, and Local UI State

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared upstream dependency edges have been accepted outside the extracted register.

## Declared Downstream

TBD - no declared downstream dependency edges have been accepted outside the extracted register.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total ACTIVE rows | 21 |
| ANCHOR rows | 6 |
| EXECUTION rows | 15 |
| RETIRED rows | 0 |
| Cycle-participating rows (non-gating) | 0 (the five D-APP-109 rows DEP-02-04-015..019 were resolved by decompose under D-APP-110 on 2026-09-05; DEP-02-04-017..019 now target the DOCUMENT contract node) |
| DOCUMENT-target rows | 10 (REF-001..006, DECOMP-v3.2, and the three D-APP-110 contract rows DEP-02-04-017..019) |

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-02-04-001 | ANCHOR | OTHER | PKG-02 | ACTIVE | `_CONTEXT.md#Identity` |
| DEP-02-04-002 | ANCHOR | OTHER | SOW-004 | ACTIVE | `ScopeOfWork.md#Purpose and Objective Traceability` |
| DEP-02-04-003 | ANCHOR | OTHER | SOW-008 | ACTIVE | `ScopeOfWork.md#Purpose and Objective Traceability` |
| DEP-02-04-004 | ANCHOR | OTHER | SOW-016 | ACTIVE | `ScopeOfWork.md#Purpose and Objective Traceability` |
| DEP-02-04-005 | ANCHOR | OTHER | OBJ-001 | ACTIVE | `ScopeOfWork.md#Purpose and Objective Traceability` |
| DEP-02-04-006 | ANCHOR | OTHER | OBJ-004 | ACTIVE | `ScopeOfWork.md#Purpose and Objective Traceability` |
| DEP-02-04-007 | EXECUTION | PREREQUISITE | REF-001 `docs/DIRECTIVE.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-008 | EXECUTION | PREREQUISITE | REF-002 `docs/CONTRACT.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-009 | EXECUTION | PREREQUISITE | REF-003 `docs/SPEC.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-010 | EXECUTION | PREREQUISITE | REF-004 `docs/TYPES.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-011 | EXECUTION | PREREQUISITE | REF-005 `docs/PLAN.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-012 | EXECUTION | PREREQUISITE | REF-006 `docs/PRD.md` | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-013 | EXECUTION | PREREQUISITE | DECOMP-v3.2 | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-014 | EXECUTION | PREREQUISITE | TBD adjacent deliverables | ACTIVE | `ScopeOfWork.md#CLM-018` |
| DEP-02-04-015 | EXECUTION | PREREQUISITE | DEL-02-02 (seated item DEL-02-02-V3-03 landed; SCC resolved under D-APP-110, gates per SatisfactionStatus) | ACTIVE | `_STATUS.md#Remaining` |
| DEP-02-04-016 | EXECUTION | PREREQUISITE | DEL-02-03 (right-panel view switcher from DEL-02-03-V3-01; SCC resolved under D-APP-110, gates per SatisfactionStatus) | ACTIVE | `_STATUS.md#Remaining` |
| DEP-02-04-017 | EXECUTION | HANDOVER | DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (DOCUMENT contract at `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; consumed by DEL-02-01-V3-02, DEL-02-01-V3-03; decomposed under D-APP-110 SD-003, deliverable relation to DEL-02-01 preserved in Notes) | ACTIVE | `_STATUS.md#Remaining` |
| DEP-02-04-018 | EXECUTION | HANDOVER | DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (DOCUMENT contract at `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; consumed by DEL-02-02-V3-04; decomposed under D-APP-110 SD-006, deliverable relation to DEL-02-02 preserved in Notes) | ACTIVE | `_STATUS.md#Remaining` |
| DEP-02-04-019 | EXECUTION | HANDOVER | DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (DOCUMENT contract at `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; consumed by DEL-02-03-V3-01; decomposed under D-APP-110 SD-004, deliverable relation to DEL-02-03 preserved in Notes) | ACTIVE | `_STATUS.md#Remaining` |
| DEP-02-04-020 | EXECUTION | CONSTRAINT | DEL-07-03 (governed workflow file owns rung-related truth) | ACTIVE | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` |
| DEP-02-04-021 | EXECUTION | CONSTRAINT | EXTERNAL Root-owned daemon session record (TargetLocation TBD) | ACTIVE | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Runtime overrides used: `SCOPE=DEL-02-04`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling honored: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the specified decomposition authority.
- `Dependencies.csv` did not previously exist in this deliverable folder; all rows in this run are new extracted rows.
- Objective traces `OBJ-001` and `OBJ-004` are encoded with `TargetType=WBS_NODE` because the v3.1 target enum has no `OBJECTIVE` value.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor was found.
- No `[WARNING] MISSING_DECOMPOSITION`: the runtime override decomposition file was available and used.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (DEP-005, DEP-006)

- Run: `TASK + dependency-extract`, instance `N1-TASK-DEL-02-04` of `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/` (report-only preview first; these bytes reach the carrier only as the reviewed post-image authorized by SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-005 and DEP-006 after owner acceptance of the WORKING_ITEMS alignment).
- Runtime overrides: `SCOPE=DEL-02-04_Toolkit_Options_and_Local_UI_State`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `DOC_ROLE_MAP=DEFAULT` (unused because the docs were named explicitly).
- Basis: `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`; decomposition found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, the `ScopeOfWork.md` `decomposition_basis`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010; authority corpus v20, all seven `_REFERENCES.md` rows MATCH. Pre-images verified: `Dependencies.csv` `7f986d37a117f3e9812dd978a4ab00031878be50f2c351c4693713ae087c1010` (14 rows); `_DEPENDENCIES.md` `a81ae0ee95103979cfd923f6666e74680d3d69c66a43a86418d9a55424251b1d`.
- Sources: `ScopeOfWork.md` (front matter, Purpose line, SCA-APP-010 Gate-5 Current Contract, CLM-002, CLM-018, CLM-023, OUT-001 matrix), `_CONTEXT.md`, `_STATUS.md` `## Remaining` only (seated item `DEL-02-04-V3-01` gate, Depends, and write-locus lines as owner-adopted information-flow signals), `_REFERENCES.md` for pointer resolution, and the applied decomposition at L174, L178, L186, L262, L265, L280, L307-L310, L359, L404-L487, L602, L634. Excluded: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `_run_records/**`. Other deliverable folders were read only to confirm that DEL-02-01, DEL-02-02, DEL-02-03, DEL-07-03 and the seated items named in the Depends line exist.
- Legacy kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` no longer exist in this carrier. Every row that cited them was re-evidenced to live bytes (`ScopeOfWork.md#Purpose and Objective Traceability` for anchors; `ScopeOfWork.md#CLM-018` for prerequisites) with `LastSeen=2026-09-05`; each relation is still stated, so no row was retired.
- Pass 1 - ANCHOR: one `IMPLEMENTS_NODE` row (DEP-02-04-001) preserved with its package label resolved to the applied name and its SourceRef moved to the live `## Identity` heading; trace anchors DEP-02-04-002..004 preserved for SOW-004, SOW-008, SOW-016 (all still on applied row L310) with labels resolved to the reverse-view statements (L407, L411, L419); DEP-02-04-005..006 preserved for OBJ-001, OBJ-004 keeping the carrier's `TargetType=WBS_NODE` objective convention. SOW-081..SOW-084 are not carried by DEL-02-04, so no new anchor was added and none was retired.
- Pass 2 - EXECUTION: DEP-02-04-007..013 re-evidenced (REF-006 stale mismatch wording removed from DEP-02-04-012); DEP-02-04-014 re-evidenced and kept `TargetType=UNKNOWN` because the live source still says TBD. New rows emitted: DEP-02-04-020 (constraint: the governed workflow file whose contract DEL-07-03 owns holds rung-related truth); DEP-02-04-021 (constraint: Root-owned daemon session record, `TargetType=EXTERNAL`, `TargetLocation=TBD`, no Root path). The five seated-item deliverable edges first proposed as DEP-02-04-015..019 (upstream prerequisites DEL-02-02-V3-03 and DEL-02-03-V3-01; downstream handover of the additive v1 workspace-state fields to DEL-02-01, DEL-02-02, DEL-02-03) are held non-emitted under brief amendment v1.1 (see the HELD bullets below); their IDs stay reserved and no row was renumbered.
- Fence F1 (SCC-001: DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05): NONE; no row targets an SCC-001 member and no other register carries a row back to DEL-02-04 (baseline orphan).
- Fence F2 (Root path): NONE emitted; every `TargetLocation` is under `execution/**` of the App project, a repo-root file pinned by `_REFERENCES.md`, or `TBD`. Candidates listed and not emitted: the design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`, cited by the seated item only for what the tranche means when complete, never as a queue) and the `loop/LOOP_INIT.md` section 7 Evidence contract; both are repo-root paths not pinned by this carrier's `_REFERENCES.md`.
- Fence F3 (permitted effect): NONE; every new row comes from the amended SOW-004/SOW-008 rows, the applied row L310 prose and Notes, or the seated Depends and gate lines. Considered and not emitted for lack of an explicit transfer in this carrier's sources: DEL-05-04 replay semantics, DEL-07-01 known-folder policy (SOW-002), `proposal.*` event consumption (SOW-082; Root DEL-02-10), DEL-04-02 and DEL-06-01 resolution of DEP-02-04-014, the SCA-APP-004/SCA-APP-010 instruments REF-008..REF-013, `docs/ui/UI_POLISH_EXECUTION_PLAN.md`, and the seated item's registered check gates.
- NEEDS_HUMAN_GRAPH_DECISION: none open in this post-image. The two deliverable-level pairs the 00:39 preview surfaced (DEL-02-04 <-> DEL-02-02 via DEP-02-04-015/018; DEL-02-04 <-> DEL-02-03 via DEP-02-04-016/019) are thereby held rather than open: every participating row is a held non-emitted proposal under amendment v1.1, so the register carries no cycle-participating edge and nothing was linearized. The cycle questions travel with the held proposals to the owner's separate transaction (decompose / invert / merge / cut; cut and merge are human-gated per `docs/CYCLE_DRIVEN_RESOLUTION.md`).
- Brief amendment v1.1 (HELP_HUMAN, after fan-in of the thirteen N1 returns; `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`): the fan-in simulation with all thirteen post-images substituted (`Evidence/fanin_simulation_v1/`) showed that 15 of the 25 newly proposed deliverable edges lie on cycles collectively and would merge SCC-001 into a 20-node SCC; SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3 requires SCC unchanged unless separately ruled, and choosing which to keep would be a cut. The five DEL-02-04 rows below were removed from this post-image before any carrier write (they were never written to the carrier, so this is not a register deletion); IDs remain reserved.
- EMITTED under D-APP-109 (H-008): DEP-02-04-015 — DEL-02-04 -> DEL-02-02 UPSTREAM PREREQUISITE (seated item DEL-02-04-V3-01 not selectable until DEL-02-02-V3-03 has landed; `_STATUS.md#Remaining`) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-009): DEP-02-04-016 — DEL-02-04 -> DEL-02-03 UPSTREAM PREREQUISITE (the Activity view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it; `_STATUS.md#Remaining`) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-010): DEP-02-04-017 — DEL-02-01 <- DEL-02-04 DOWNSTREAM HANDOVER (additive v1 workspace-state fields consumed by DEL-02-01-V3-02 and DEL-02-01-V3-03; `_STATUS.md#Remaining`) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-011): DEP-02-04-018 — DEL-02-02 <- DEL-02-04 DOWNSTREAM HANDOVER (additive v1 workspace-state fields consumed by DEL-02-02-V3-04; `_STATUS.md#Remaining`) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-012): DEP-02-04-019 — DEL-02-03 <- DEL-02-04 DOWNSTREAM HANDOVER (additive v1 workspace-state fields consumed by DEL-02-03-V3-01; `_STATUS.md#Remaining`) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` three-digit profile rejects the accepted App two-digit `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN` identities (OBJ IDs pass). No accepted ID was changed.
- [WARNING] INSTRUCTION_ROOT_DECLARED_BY_BRIEF: `CHIRALITY_INSTRUCTION_ROOT` was not exported to the subagent shell; the sealed brief names the repository root as the location of `AGENTS.md`, `agents/`, `skills/`, and `tools/`, so `INSTRUCTION_ROOT=REPO_ROOT` was taken from the brief and recorded as an ASSUMPTION in the TASK run record.
- No `[WARNING] FLOATING_NODE`, `[WARNING] AMBIGUOUS_ANCHOR`, or `[WARNING] MISSING_DECOMPOSITION`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor; decomposition present at the pinned identity.
- Function 5 (re-run on the amended post-image): `validate_dependencies_schema.py` VALID (29 columns, 16 data rows); every emitted enum value VALID; exactly one ACTIVE `IMPLEMENTS_NODE`; every ACTIVE row's `EvidenceFile#SourceRef` resolves to a live heading, CLM id, or front-matter-backed section and every `EvidenceQuote` is found verbatim; `FromDeliverableID=DEL-02-04` on every row; `DependencyID` unique (16 emitted plus 5 reserved, no collision); counts in this file reconciled to `Dependencies.csv`.

## Run Notes - 2026-09-05 D-APP-109 emission (N9-TASK-DEL-02-04)

- Run: `TASK + dependency-extract` (apply mode), instance `N9-TASK-DEL-02-04` of `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/` (plan amendment v1.2), authorized by owner ruling D-APP-109 (`execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`) on SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-005 and DEP-006.
- Runtime overrides: `SCOPE=DEL-02-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[_STATUS.md]` (`## Remaining` only; the held proposals' evidence) plus `instances/N1-TASK-DEL-02-04/PREVIEW.md` section 2a and `HELD_EDGE_PROPOSALS.csv` H-008..H-012 as the row-content sources named by the sealed brief; no new extraction from prose.
- Basis: candidate branch HEAD `f38f1448675b8e9f40f33932a11b7ffa4126fe69`; decomposition found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; pre-images verified before writing: `Dependencies.csv` `c6bdffd1aef83f0c04764a8f8f01d5f67abc1928c9630866f6f48dd83d16ac62` (16 rows); `_DEPENDENCIES.md` `1fffa1ec5e37709dcb26f0c1b0cd611e3ae474690db63593a85e6bd2c50ba35e`.
- Emitted: DEP-02-04-015..019 (H-008..H-012) at their numeric positions with the evidence, statements, confidence, and `SatisfactionStatus=PENDING` each held proposal recorded; every pre-existing row byte-identical; no row retired or renumbered. Each new row's `Notes` carries the D-APP-109 `CYCLE_PARTICIPATING` non-gating clause (the enlarged SCC-001).
- `TargetRefID` on the five DELIVERABLE rows follows the carrier's only DELIVERABLE sibling (DEP-02-04-020, scope ID): SOW-001 for the two gates (the retirement and the one-view-at-a-time right panel cited by the target items' Trace lines), SOW-008 for the DEL-02-01 and DEL-02-02 handovers, SOW-004 for the DEL-02-03 handover; each row's `Notes` states the basis. Convention note only (the closure analyzer ignores the field; REVIEW.md R-006).
- Graph effect (recorded, not linearized): DEL-02-04 now carries edges into DEL-02-01, DEL-02-02, and DEL-02-03; with the sibling emissions these join SCC-001 into the enlarged SCC. The two deliverable-level pairs (DEL-02-04 <-> DEL-02-02 via 015/018; DEL-02-04 <-> DEL-02-03 via 016/019) are open NEEDS_HUMAN_GRAPH_DECISION items whose resolution is an owner act under `docs/CYCLE_DRIVEN_RESOLUTION.md`; until then the five rows are non-gating. The seated item's own `Depends` line and gate remain the executable ordering.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit profile rejects the accepted App two-digit identities; no ID changed).
- [WARNING] INSTRUCTION_ROOT_DECLARED_BY_BRIEF: `CHIRALITY_INSTRUCTION_ROOT` not exported; `INSTRUCTION_ROOT=REPO_ROOT` taken from the sealed brief (ASSUMPTION recorded in the run record).
- No `[WARNING] FLOATING_NODE`, `[WARNING] AMBIGUOUS_ANCHOR`, or `[WARNING] MISSING_DECOMPOSITION`.
- Function 5: see the run record `_run_records/TASK_RUN_2026-09-05_0802.md` (schema VALID, 29 columns, 21 data rows; every emitted enum VALID; one ACTIVE `IMPLEMENTS_NODE`; 21 unique IDs; `FromDeliverableID=DEL-02-04` on every row; every emitted `EvidenceFile#SourceRef` resolves to live bytes and the quote is present; counts in this file reconciled to `Dependencies.csv`).

## Run Notes - 2026-09-05 D-APP-110 decompose (N14-TASK-DEL-02-04)

- Run: `TASK + dependency-extract` (apply mode), instance `N14-TASK-DEL-02-04` of `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/` (plan amendment v1.3, node N14), authorized by owner ruling D-APP-110 (`execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`) and the per-row workbook `SCC_DECOMPOSE_RULINGS.csv` rows SD-003, SD-004, SD-006. Move: `decompose` (`docs/CYCLE_DRIVEN_RESOLUTION.md` section 2.3) in the `SCC-SAFE-MOVES-001` form; no row retired, cut, merged, or inverted; no `PREREQUISITE` row re-targeted.
- Runtime overrides: `SCOPE=DEL-02-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md]` read only to verify the contract anchor (no new extraction from prose); row values taken exactly from the workbook.
- Basis: candidate branch HEAD `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985`; decomposition found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); pre-images verified before writing: `Dependencies.csv` `abaf816695c2c6f13adfe03ad85b31ff0cbdef2db06b36873e519060f306bcb2` (21 rows); `_DEPENDENCIES.md` `1cefdede31815de94d3f18b2e5033fbc1ebf17722f4a4d53c8e22f5eb0ec23ca`.
- Contract anchor verified in the live carrier bytes before writing: `ScopeOfWork.md` heading `## SCA-APP-010 Gate-5 Current Contract (Controlling)` (L68), applied row outputs "workspace-state schema (additive v1 fields)" (L94-L96), and acceptance obligation 1 "Workspace-state changes are additive v1 fields under the existing schema string" (L100).
- DECOMPOSE under D-APP-110 (SD-003): DEP-02-04-017 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (`TargetType=DOCUMENT`, `TargetLocation` = `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`); the coarse edge DEL-02-01->DEL-02-04 is replaced by the document-scoped contract and the deliverable relation to DEL-02-01 is preserved in `Notes`.
- DECOMPOSE under D-APP-110 (SD-004): DEP-02-04-019 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (`TargetType=DOCUMENT`, `TargetLocation` = `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`); the coarse edge DEL-02-03->DEL-02-04 is replaced by the document-scoped contract and the deliverable relation to DEL-02-03 is preserved in `Notes`.
- DECOMPOSE under D-APP-110 (SD-006): DEP-02-04-018 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (`TargetType=DOCUMENT`, `TargetLocation` = `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`); the coarse edge DEL-02-02->DEL-02-04 is replaced by the document-scoped contract and the deliverable relation to DEL-02-02 is preserved in `Notes`.
- RESOLVED under D-APP-110: DEP-02-04-015 and DEP-02-04-016 (the carrier's other D-APP-109 rows; `PREREQUISITE`, strict deliverable edges to DEL-02-02 and DEL-02-03) keep every field and gain a `Notes` clause stating that the SCC they participated in was decomposed and that each is a strict edge of the acyclic approved graph gating per its `SatisfactionStatus` (both `PENDING`). Their earlier `CYCLE_PARTICIPATING` and `NEEDS_HUMAN_GRAPH_DECISION` clauses remain as dated history.
- Graph effect: DEL-02-04 now carries no deliverable edge into DEL-02-01, DEL-02-02, or DEL-02-03 in the strict deliverable graph (the three handovers point at the DOCUMENT node DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1); the two deliverable-level pairs recorded under D-APP-109 (DEL-02-04 <-> DEL-02-02 via 015/018; DEL-02-04 <-> DEL-02-03 via 016/019) are dissolved; the carrier's remaining deliverable rows (015, 016, 020) are strict edges of the acyclic graph. Per D-APP-110 ruling 2 the resulting strict graph is acyclic; the fresh `AUDIT_DEP_CLOSURE` snapshot (N16) records it.
- Counts: ACTIVE 21, ANCHOR 6, EXECUTION 15, RETIRED 0 unchanged; `TargetType` tallies move DELIVERABLE 6 -> 3 and DOCUMENT 7 -> 10; satisfaction tallies unchanged (6 NOT_APPLICABLE / 7 SATISFIED / 7 PENDING / 1 TBD). Every other row byte-identical; no row added, retired, or renumbered.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit profile rejects the accepted App two-digit identities; no ID changed).
- [WARNING] INSTRUCTION_ROOT_DECLARED_BY_BRIEF: `CHIRALITY_INSTRUCTION_ROOT` not exported; `INSTRUCTION_ROOT=REPO_ROOT` taken from the sealed brief (ASSUMPTION recorded in the run record).
- No `[WARNING] FLOATING_NODE`, `[WARNING] AMBIGUOUS_ANCHOR`, or `[WARNING] MISSING_DECOMPOSITION`.
- Function 5: see the run record `_run_records/TASK_RUN_2026-09-05_1012.md` (schema VALID, 29 columns, 21 data rows; `TARGET_TYPE DOCUMENT` and every other distinct enum value VALID; DOCUMENT rows leave `TargetPackageID` and `TargetDeliverableID` empty; one ACTIVE `IMPLEMENTS_NODE`; 21 unique ordered IDs; `FromDeliverableID=DEL-02-04` on every row; `git diff --check` clean; counts in this file reconciled to `Dependencies.csv`).

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:30:43-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PRD_HASH_MISMATCH | 14 |
| 2026-09-05T00:39:59-0600 (amended v1.1 at 2026-09-05T01:02-0600) | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at pinned identity `c7c05169` (content commit `dbd812a5`) | PROJECT_ID_FORMAT_PROFILE; INSTRUCTION_ROOT_DECLARED_BY_BRIEF; HELD_EDGE_PROPOSALS x5 (DEP-02-04-015..019 reserved, amendment v1.1) | 16 |
| 2026-09-05T08:02-0600 (D-APP-109 emission) | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at pinned identity `c7c05169` (content commit `dbd812a5`) | PROJECT_ID_FORMAT_PROFILE; INSTRUCTION_ROOT_DECLARED_BY_BRIEF; CYCLE_PARTICIPATING x5 (DEP-02-04-015..019 emitted under D-APP-109, non-gating until the SCC is resolved) | 21 |
| 2026-09-05T10:12-0600 (D-APP-110 decompose) | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at pinned identity `c7c05169` (content commit `dbd812a5`) | PROJECT_ID_FORMAT_PROFILE; INSTRUCTION_ROOT_DECLARED_BY_BRIEF; DECOMPOSE x3 (DEP-02-04-017, -018, -019 re-targeted to the DOCUMENT contract DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 under D-APP-110 SD-003, SD-006, SD-004); RESOLVED x2 (DEP-02-04-015, -016 Notes only) | 21 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 21 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 6 |
| SATISFIED | 8 |
| PENDING | 6 |
| TBD | 1 |

Closure notes:

- The extracted register is schema-valid and evidence-first; project-level availability still follows the FULL_GRAPH closure snapshot. The five seated-item rows emitted under D-APP-109 (DEP-02-04-015..019; formerly held H-008..H-012) were resolved on 2026-09-05 by the owner-ruled `decompose` move (D-APP-110): the three handovers DEP-02-04-017..019 now target the DOCUMENT contract node DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 at `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` with their deliverable relations to DEL-02-01, DEL-02-02, DEL-02-03 preserved in `Notes`, and the two prerequisites DEP-02-04-015..016 stay strict deliverable edges. The carrier holds no cycle-participating row; every row gates per its `SatisfactionStatus`. The seated item's `Depends` line and gate remain the executable ordering at item level.
- DEP-02-04-015 is SATISFIED by committed DEL-02-02-V3-03 at `03e61f38f7b20145552023abd1cf673c2b2a3f61` and actual configured CI `33991362689` PASS at that head. WORKING_ITEMS records this evidence-against-existing-Statement judgment under D-APP-59 S1 Reach 2 and D-APP-60/64; LOOP_INIT Step 1 recognizes committed run-branch predecessors. See `_run_records/DEPENDENCY_SATISFACTION_2026-09-05_DEP015.md`. No lifecycle or owner acceptance is inferred.
- DEP-02-04-016..019 remain PENDING: the seated items they gate on or hand over to (DEL-02-03-V3-01, DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-02-V3-04) have not landed.
- DEP-02-04-007..013 are SATISFIED: all `_REFERENCES.md` authority-corpus rows report MATCH (v20) and the decomposition is present at the pinned identity.
- DEP-02-04-014 remains `TBD` because the source explicitly leaves adjacent runtime option contracts and permission policy integration points unresolved.
- DEP-02-04-020 and DEP-02-04-021 are PENDING: the DEL-07-03 workflow file contract is not yet accepted, and the Root session-record semantics await the OI-008 return.

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor, three scope-item trace anchors (SOW-004, SOW-008, SOW-016), two objective trace anchors, seven SATISFIED source-basis prerequisites, one TBD-target prerequisite (DEP-02-04-014), two seated-item prerequisites (DEP-02-04-015 to DEL-02-02; DEP-02-04-016 to DEL-02-03), three additive-field handovers (DEP-02-04-017..019, DOCUMENT-targeted at the DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 contract under D-APP-110; deliverable relations to DEL-02-01, DEL-02-02, DEL-02-03 preserved in `Notes`), and two rung-truth constraints (DEP-02-04-020 to DEL-07-03; DEP-02-04-021 EXTERNAL Root).
- The carrier no longer holds cycle-participating rows: the SCC that DEP-02-04-015..019 participated in was decomposed under D-APP-110 (2026-09-05), the two deliverable-level pairs (DEL-02-04 <-> DEL-02-02 via 015/018; DEL-02-04 <-> DEL-02-03 via 016/019) are dissolved by the DOCUMENT re-targeting of 017..019, and every row gates per its `SatisfactionStatus` like any other strict edge (015 is `SATISFIED` by the recorded T1 evidence; 016..019 remain `PENDING` until the named seated items land). Read the three DOCUMENT rows as contract consumption, not build sequencing; the deliverable relation each records is evidence in `Notes`, not a strict edge.
- Keep DEP-02-04-021 at `TargetLocation=TBD` until the OI-008 Root return is routed to App; do not resolve it to a Root path.
- The two F2 candidates (design basis plan; `loop/LOOP_INIT.md` section 7) are deliberately absent from the register; reconcile against the seated item's Plan and Return lines rather than against register rows.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
