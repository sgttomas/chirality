# Dependencies: DEL-08-03 Pipeline Category and Task Scope Dispatch

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-08-03-001`, `DEP-08-03-002`, `DEP-08-03-003`, `DEP-08-03-004`, `DEP-08-03-005`, `DEP-08-03-006`, `DEP-08-03-007`, `DEP-08-03-008`, `DEP-08-03-009`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-08-03-010`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-08-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `cf968ae8134e690f22d35a702666a7f704f2a16f39fdbce4549258685a2e0651`; `_CONTEXT.md` `c5e3d5f87e180fca28831f2a3d15ce16761eff0988f4ed7e2680300b315baf59`; `_REFERENCES.md` `3f0d1039ae0d28622bb095bcceab1cad871f8add3423bac7679a95bfd44bdc4d`; `_STATUS.md` `00fca38507561ab1fb7204e77cb6acb16ee8fbe9f7b3baed9290b12bf9b07f1c`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `226f430b03edcd2b98f34ee754ebabb0b859e68e14396d59e22317f596276bc2`, `_DEPENDENCIES.md` `a36aa191ae28ac2af8665a0839b6752a0ef03b642bb071b9086777ac72bf1930`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 9 (`LastSeen=2026-09-27`); restated in place 1; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RESTATED DEP-08-03-010 (EXECUTION DOWNSTREAM HANDOVER -> Task-scope selection, knowledge-type discovery, and disabled) DX-11,DX-12; see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-012 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-08-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `c8918801ff2bf0846556fbd055fab90d9dbb0260a3ab44be3ec3db93b10dfb03`; `_CONTEXT.md` `c5e3d5f87e180fca28831f2a3d15ce16761eff0988f4ed7e2680300b315baf59`; `_REFERENCES.md` `3f0d1039ae0d28622bb095bcceab1cad871f8add3423bac7679a95bfd44bdc4d`; `_STATUS.md` `00fca38507561ab1fb7204e77cb6acb16ee8fbe9f7b3baed9290b12bf9b07f1c`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `fa48f3683fa805aa521df3c5c8d7e3b18cd39deaa222840bc386b1cb8ddc349e`, `_DEPENDENCIES.md` `c8c0bda4a99a8ddba754733996cf4d586dca54131e6d77ec734f913deab80302`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; the accepted SCA-APP-012 scope text is the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 9 (`LastSeen=2026-09-27`); restated in place 1; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RESTATED DEP-08-03-007 (EXECUTION UPSTREAM INTERFACE -> REF-003) DX-03; see the row `Notes`.
- DX-03: DEP-08-03-007 `TargetName` now names the deliverable scan API (CLM-004 'Deliverable scan API', line 124). The source no longer names the retired scope route, so the 2026-09-05 source-endpoint label conflict no longer reproduces and is not reported by this run.
- Inbound DEP-02-03-009 (DEL-02-03 -> DEL-08-03) is RETIRED in the DEL-02-03 register (DX-01).
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 5 |
| ACTIVE EXECUTION rows | 5 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-08-03-001 | ANCHOR | UPSTREAM | OTHER | PKG-08 | ACTIVE | TBD |
| DEP-08-03-002 | ANCHOR | UPSTREAM | OTHER | SOW-007 | ACTIVE | TBD |
| DEP-08-03-003 | ANCHOR | UPSTREAM | OTHER | SOW-026 | ACTIVE | TBD |
| DEP-08-03-004 | ANCHOR | UPSTREAM | OTHER | OBJ-001 | ACTIVE | TBD |
| DEP-08-03-005 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | TBD |
| DEP-08-03-006 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | TBD |
| DEP-08-03-007 | EXECUTION | UPSTREAM | INTERFACE | REF-003 | ACTIVE | TBD |
| DEP-08-03-008 | EXECUTION | UPSTREAM | CONSTRAINT | REF-002 | ACTIVE | TBD |
| DEP-08-03-009 | EXECUTION | UPSTREAM | PREREQUISITE | REF-006 | ACTIVE | TBD |
| DEP-08-03-010 | EXECUTION | DOWNSTREAM | HANDOVER | Task-scope selection, knowledge-type discovery, and disabled… | ACTIVE | TBD |

## Run Notes — 2026-09-05 00:37 (SCA-APP-010 DEP-023/DEP-024 pass)

- Produced as the report-only preview `N1-TASK-DEL-08-03` under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`; this file becomes live only through the reviewed write that SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-023 and DEP-024 authorize after the N2 review.
- Mode: `UPDATE`
- Strictness: `CONSERVATIVE`
- Consumer context: `RECONCILIATION`
- Decomposition path: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Decomposition status: found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; SCA-APP-010 Gate 5 applied; DEC-025); companion register SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`; authority corpus v20, no drift. Used for anchor validation against applied row L370, amended Scope Ledger row L177, reverse view L410 and L429, objective rows L262 and L268, OI-008 (L602), and DEC-025 (L634).
- Anchor doc: `ScopeOfWork.md` (front matter `decomposition_basis`, `project_scope_refs`, `package_objective_refs`; `## Purpose and Objective Traceability`; `### Current responsibility`; CLM-002; CLM-003), with `_CONTEXT.md` for identity confirmation.
- Execution docs scanned in order: `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md` (`## Remaining` only; it is empty, so no seated-item signal exists). `_REFERENCES.md` was read to resolve document pointers only. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, and `_run_records/**` were excluded as sources.
- Pre-image identities: `Dependencies.csv` SHA-256 `263656d18eee89339ceeca1f3cde386f88b98ba8369a7f21d96248eedd35d3fe` (10 data rows); `_DEPENDENCIES.md` SHA-256 `ec4d6861aa2662326a7ede29c920825a8df9e299d307a4487d604dbb2d2a7b3f`.
- Legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this carrier. Every row whose `EvidenceFile` named one of them is still stated in the live SOW_V1 sources and was re-evidenced to `ScopeOfWork.md#<heading or REQ id>` with `LastSeen=2026-09-05`; no row retired and no row deleted.
- Applied row L370 carries exactly SOW-007, SOW-026, OBJ-001, OBJ-007; no SOW-081 to SOW-084 anchor applies to this carrier, and no scope ref left the applied row, so no anchor was added or retired.
- SOW-007 (DEP-08-03-002) is the one relation SCA-APP-010 revised for this carrier: the ledger label and statement were refreshed to the amended row L177/L410 text (legacy label `Pipeline selectors` preserved in `Notes`), and the presentation half is recorded as retired by owner ruling (G2-CONFIRM; DEC-025).
- Considered and not emitted: `DEL-08-03 -> DEL-02-02` presentation-consumer INTERFACE edge. The older compatibility clauses (CLM-004 `Presentation ownership`, CLM-012, DEL-08-03-REQ-013, CLM-023 step 9, `_CONTEXT.md#SCA-APP-004 Ownership Boundary`) still name DEL-02-02 as consumer, but the controlling `## SCA-APP-010 Gate-5 Current Contract` section, applied row L370, reverse view L410 (`no presentation consumer is mapped`), and DEL-02-02's own applied row L308 (`Workbench and Pipeline are retired from the active shell`) supersede them. No new row was born `RETIRED` because no prior row existed. DEL-02-02 is not an SCC-001 member, so this is not an F1 candidate; it is withheld under F3 and the controlling contract.
- Considered and not emitted: ownership-partition statements toward DEL-08-05 (child records), DEL-05-04 (replay/projection), DEL-08-02 (aliases/routing), and the `any later consumer may not infer plans/tasks from conversational prose` clause. None names an artifact, contract, tool, event, or policy this carrier consumes or supplies; they are coordination or boundary statements, not information-flow edges.
- No Root-owned semantics are consumed by this carrier, so no `TargetType=EXTERNAL` / `TargetLocation=TBD` row was needed and no Root path was proposed (F2 NONE).
- Satisfaction lifecycle left unchanged (`SatisfactionStatus=TBD`, `ProposedMaturity=TBD` on every row): CLM-007 states satisfaction remains TBD until dependency closure accepts the register, and the SCA-APP-010 seating text implies no dependency-acceptance act.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `tools/validation/validate_id_format.sh` three-digit profile rejects the accepted App two-digit IDs (`DEL-08-03`, `PKG-08`, `DEP-08-03-nnn`, `SOW-nnn`); no ID was changed.
- `[WARNING] SOURCE_ENDPOINT_LABEL_CONFLICT`: `ScopeOfWork.md` names `/api/project/deliverables` (CLM-004, DEL-08-03-REQ-010) and `/api/working-root/scope` (CLM-016, CLM-023, CLM-024) for the same scope-scan surface; DEP-08-03-007 keeps its target at `docs/SPEC.md` Section 17.2.
- `[WARNING] UNKNOWN_DOWNSTREAM_TARGET`: the downstream test/record handoff (DEP-08-03-010) is explicit, but the applied row states no active presentation consumer exists after SCA-APP-010; the consumer target remains `UNKNOWN`/`TBD`. Minor label drift: `_CONTEXT.md#Anticipated Artifacts` still reads `Pipeline selector and contextual-consumer tests` while applied row L370 reads `Pipeline selector tests`.
- `[OBSERVATION]` Objective row L268 (OBJ-007) lists SOW-005 to SOW-006, SOW-017, SOW-030 to SOW-031, and SOW-063 but not SOW-007 or SOW-026, while reverse-view rows L410 and L429 map both to OBJ-007; the applied row and Scope Ledger control the anchor. Reported for RECONCILIATION; no action taken.
- Fence results: F1 NONE; F2 NONE; F3 NONE. `NEEDS_HUMAN_GRAPH_DECISION`: none.
- Objective anchors keep this carrier's existing `TargetType=REQUIREMENT` convention (rows 004 and 005); no re-typing was performed.

## Run Notes — 2026-05-20 20:54

- Mode: `UPDATE`
- Strictness: `CONSERVATIVE`
- Consumer context: `NONE`
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Decomposition status: found and used for anchor validation.
- Anchor doc: `Datasheet.md` plus `_CONTEXT.md` for identity confirmation.
- Execution docs scanned: `Specification.md`, `Guidance.md`, `Procedure.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- No existing `Dependencies.csv` was present, so all extracted rows were newly created.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 authority corpus v2 supersedes the prior REF-006 source warning; `_REFERENCES.md` now records REF-006 as MATCH and row DEP-08-03-009 is updated accordingly.
- `[RESOLVED] PIPELINE_COMPONENT_COVERAGE`: ADQ-12 records Pipeline surface render coverage for category controls, disabled options, valid TASK deep links, and stale knowledge-target reset.
- `[RESOLVED] TASK_GOVERNANCE_LINKAGE`: ADQ-12 route-state regression proves Pipeline TASK selector state is ignored as unknown runtime options rather than converted into delegated subagents.
- `[WARNING] UNKNOWN_DOWNSTREAM_TARGET`: downstream test/record handoff is explicit, but the consumer deliverable is not identified in the allowed evidence set; target remains `UNKNOWN`/`TBD`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Warnings | ACTIVE Count |
|---|---|---|---|---|---:|
| 2026-09-05 00:37 | UPDATE | CONSERVATIVE | found at pinned identity c7c05169 (content commit dbd812a5; SCA-APP-010 Gate 5; applied row L370) | PROJECT_ID_FORMAT_PROFILE; SOURCE_ENDPOINT_LABEL_CONFLICT; UNKNOWN_DOWNSTREAM_TARGET | 10 |
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, Pipeline component coverage, and TASK governance linkage applied | UNKNOWN_DOWNSTREAM_TARGET | 10 |
| 2026-05-20 20:54 | UPDATE | CONSERVATIVE | found | superseded PRD_HASH_MISMATCH; UNKNOWN_DOWNSTREAM_TARGET | 10 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=10 (ANCHOR=5; EXECUTION=5) |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=10 (ANCHOR=5; EXECUTION=5) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 10 |
| SatisfactionStatus | TBD | 10 |
| RequiredMaturity | SEMANTIC_READY | 10 |
| DependencyClass | ANCHOR | 5 |
| DependencyClass | EXECUTION | 5 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | HANDOVER | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 5 |
| DependencyType | PREREQUISITE | 2 |

## Downstream Handoff Notes

Consumer context: `RECONCILIATION`.

- Accepted upstream snapshot: applied decomposition `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (SCA-APP-010 Gate 5; DEC-025); the carrier `ScopeOfWork.md` front matter pins the same basis.
- Derivative-package status: this register is a derivative package regenerated from that snapshot; it is not decomposition truth and does not imply dependency acceptance, lifecycle change, or a Checking Approval SHA change.
- Graph position: DEL-08-03 is not a member of SCC-001 and no row in this register targets an SCC-001 member; no SCC edge, SCC-internal retirement, or Root path is proposed. Known inbound edges from other registers (DEP-02-02-009, DEP-02-03-009, DEP-08-02-013) are owned by their carriers and were not consulted as sources.
- Relations for RECONCILIATION attention: (1) DEP-08-03-002 now carries the amended SOW-007 label and records that the presentation consumer is retired; DEL-02-02's own register still holds DEP-02-02-009 (a CONSTRAINT toward DEL-08-03 evidenced by its legacy `Guidance.md`), which that carrier's SCA-APP-010 pass should reconcile. (2) DEP-08-03-010's consumer remains `UNKNOWN`/`TBD` by design after the presentation retirement. (3) The `/api/project/deliverables` versus `/api/working-root/scope` label conflict inside `ScopeOfWork.md` is a document-consistency item, not a graph item.
- Rerun requirements: rerun `TASK + dependency-extract` if the applied row L370, Scope Ledger row L177, or reverse view L410/L429 change, if `ScopeOfWork.md` acquires seated `## Remaining` items with `Depends` lines, or if a later amendment re-hosts a presentation consumer.
- Remaining blockers for closure: none local; register acceptance is a separate human act under the SCA-APP-010 downstream handoff (DEP-023/DEP-024 reviewed write, then closure analysis).

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=10; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_LUNA_17_APPROVED.csv`; current rows: ACTIVE=10, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
