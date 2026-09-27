# Dependencies: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-03-001`, `DEP-07-03-002`, `DEP-07-03-003`, `DEP-07-03-004`, `DEP-07-03-005`, `DEP-07-03-006`, `DEP-07-03-007`, `DEP-07-03-008`, `DEP-07-03-009`, `DEP-07-03-010`, `DEP-07-03-011`, `DEP-07-03-014`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-07-03-012`, `DEP-07-03-013`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 3 |
| ACTIVE EXECUTION rows | 11 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-07-03-001 | ANCHOR | UPSTREAM | OTHER | SOW-026 | ACTIVE | TBD |
| DEP-07-03-002 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | TBD |
| DEP-07-03-003 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-07-03 decomposition entry | ACTIVE | TBD |
| DEP-07-03-004 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | TBD |
| DEP-07-03-005 | EXECUTION | UPSTREAM | PREREQUISITE | REF-006 | ACTIVE | TBD |
| DEP-07-03-006 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | TBD |
| DEP-07-03-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-001 | ACTIVE | TBD |
| DEP-07-03-008 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | TBD |
| DEP-07-03-009 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-07-04 | ACTIVE | TBD |
| DEP-07-03-010 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-07-05 | ACTIVE | TBD |
| DEP-07-03-011 | ANCHOR | UPSTREAM | OTHER | SOW-081 | ACTIVE | TBD |
| DEP-07-03-012 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-02-02 | ACTIVE | PENDING |
| DEP-07-03-013 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-04-04 | ACTIVE | PENDING |
| DEP-07-03-014 | EXECUTION | UPSTREAM | CONSTRAINT | K-PATH-2 | ACTIVE | PENDING |

## Run Notes

- Run timestamp: 2026-05-20T19:54:16-0600.
- Mode: UPDATE.
- Strictness: CONSERVATIVE.
- Consumer context: NONE.
- Scope: DEL-07-03.
- Decomposition path: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor/target validation.
- Source documents read for extraction: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed as dependency evidence.
- Anchor document selected: `Datasheet.md`.
- Execution document order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Existing `Dependencies.csv`: absent before this run; created with v3.1 schema.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- Implementation location remains TBD in source procedure; no dependency edge was inferred from that unknown.
- Scanner output schema remains TBD in source procedure; no dependency edge was inferred from that unknown.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-07-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `78b7aaef7d238cb22fb71fbb39b4299747b056ba58403dde8d3fcf5dff9a578f`; `_CONTEXT.md` `a5df2116fe90bb6f7ba4ac1e93d3bbfb71994478b8ff749f0026c4a648ec3534`; `_REFERENCES.md` `f53b9d25013b8182953ed70aa4fe4ec861cc69b99dc8b256bdb0123e3b48d835`; `_STATUS.md` `01b3bb94ffc346fc2b7dd8b304641b8e75ffba3f255fae44eda418a69a874981`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `93587eaf711147af53f7032eacb9f030b2bfd2a4deafc2267840c033595cb86f`, `_DEPENDENCIES.md` `37f2b40ec0af7c5a675332037dc504e48cdfbb264d1d4f629871f9ab4f3156c4`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 14 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-012 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-07-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `ca5f99ac4e660b379c4b90440b2dd9d220b22c72c52ed668ef7242b86fb93dcd`; `_CONTEXT.md` `a5df2116fe90bb6f7ba4ac1e93d3bbfb71994478b8ff749f0026c4a648ec3534`; `_REFERENCES.md` `f53b9d25013b8182953ed70aa4fe4ec861cc69b99dc8b256bdb0123e3b48d835`; `_STATUS.md` `01b3bb94ffc346fc2b7dd8b304641b8e75ffba3f255fae44eda418a69a874981`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `93e6cdc5db9932df7ad4b8edc25ea2def11ebd05c6b53ea7ee2b6375f961a778`, `_DEPENDENCIES.md` `4771e8776ed0f13b985e8ecb9e19d66720683f88063f859181fde25f7703b26e`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; the accepted SCA-APP-012 scope text is the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 14 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (UPDATE)

- Run timestamp: 2026-09-05T00:37:52-0600. Produced as report-only preview `N1-TASK-DEL-07-03` under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`; applied to this folder only by the reviewed write step (SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-019, DEP-020).
- Runtime overrides: `SCOPE=DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`. No default was left to auto-discovery.
- Decomposition: found at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches `ScopeOfWork.md` front matter `decomposition_basis`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010. Applied row L359; amended Scope Ledger row SOW-081 L251; reverse view L429 (SOW-026) and L484 (SOW-081); OI-008 L602; DEC-025 L634.
- Sources: `ScopeOfWork.md` (anchor and execution), `_CONTEXT.md`, `_STATUS.md` `## Remaining` only (`Depends`, `Write locus`, gate lines); `_REFERENCES.md` for pointer resolution. Excluded as evidence: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, `_run_records/**`. Source documents were read-only.
- Legacy four-document kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` no longer exist in this folder. Every pre-existing row that cited them (DEP-07-03-001 to DEP-07-03-010) is restated in live `ScopeOfWork.md` bytes and was re-evidenced with `LastSeen=2026-09-05`; no row was retired.
- Pass 1 - ANCHOR: parent anchor DEP-07-03-001 (SOW-026, `IMPLEMENTS_NODE`) preserved; objective trace anchor DEP-07-03-002 (OBJ-006) preserved with `TargetType=REQUIREMENT` as this register's existing convention; new trace anchor DEP-07-03-011 for SOW-081, which SCA-APP-010 added to applied row L359 (DEC-025). No scope ref left the applied row, so no anchor was retired.
- Pass 2 - EXECUTION: three new rows from SOW-081. DEP-07-03-012 (DOWNSTREAM INTERFACE to DEL-02-02: the Workflows view, roadmap, forms, library, and bind act over the file contract this carrier owns; L484, L308). DEP-07-03-013 (DOWNSTREAM INTERFACE to DEL-04-04: the delimited roadmap-injection block consumes the roadmap grammar, `roadmapSource`, and hash; L484, L329, L251). DEP-07-03-014 (UPSTREAM CONSTRAINT, `TargetType=EXTERNAL`, `TargetLocation=TBD`: "Writes obey K-PATH-2 containment", L251, L329, REQ-008).
- Considered and not emitted (CONSERVATIVE; F3 permitted effect): SOW-026 co-carrier DEL-08-03 (structural adjacency; unchanged by SCA-APP-010); DEL-08-01 skill-declared workflow templates and the app-scoped known-folder set behind the library (not stated for this carrier); the workflow file's front-matter delegation-policy declaration as a consumer of the Root DEL-02-11 session-record field (not stated for this carrier; the seated item records `Depends: none`); the `plans/shell-redesign_2026-09-04/` design-basis pins in the seated item (cited "only for what the tranche means when complete, never as a queue"; not on the applied or amended rows); the seated item's gates and checks (schedule/verification, not information flow).
- Fences: F1 NONE (DEL-07-03 is not an SCC-001 member; DEL-02-02 and DEL-04-04 are not SCC-001 members; no SCC-001 member holds an active row back to DEL-07-03). F2 NONE (every `TargetLocation` is under `execution/**`, a `_REFERENCES.md`-pinned `docs/*.md`, or `TBD`; no Root path). F3 NONE (new rows derive only from SOW-081 L251/L484 and applied row L359 prose).
- NEEDS_HUMAN_GRAPH_DECISION: none.
- CONFLICT: decomposition L251 and OI-008 L602 state that Q16 (shared-folder position advance) remains an OI-008 owner question, while `_STATUS.md` `## Remaining` DEL-07-03-V3-01 and `ScopeOfWork.md` Current acceptance obligations record Q16 as ruled under D-APP-108 (2026-09-04). No graph edge hinges on it; surfaced for RECONCILIATION and the OI-008 register, not resolved here.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` expects `PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, and `SOW-NNNN`; this accepted App decomposition uses `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN`. The helper reports those IDs invalid by its generic profile (OBJ-006 validates). No accepted ID was rewritten or invented.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- Schema validation: `validate_dependencies_schema.py` VALID, 29 columns, 14 data rows; all 23 distinct emitted enum values VALID; `DependencyID` unique; `FromDeliverableID=DEL-07-03` on every row; `Status=CANDIDATE` absent.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:16-0600 | UPDATE | CONSERVATIVE | located: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH REF-006 | 10 |
| 2026-09-05T00:37:52-0600 | UPDATE | CONSERVATIVE | located at pinned identity: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169…771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` | PROJECT_ID_FORMAT_PROFILE; CONFLICT Q16 (L251/L602 vs D-APP-108 seating) | 14 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=14 (ANCHOR=3; EXECUTION=11) |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=14 (ANCHOR=3; EXECUTION=11) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 14 |
| SatisfactionStatus | PENDING | 3 |
| SatisfactionStatus | TBD | 11 |
| RequiredMaturity | SEMANTIC_READY | 14 |
| DependencyClass | ANCHOR | 3 |
| DependencyClass | EXECUTION | 11 |
| DependencyType | CONSTRAINT | 3 |
| DependencyType | INTERFACE | 2 |
| DependencyType | OTHER | 3 |
| DependencyType | PREREQUISITE | 6 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (SOW-026), two trace anchors (OBJ-006, SOW-081), eight retained UPSTREAM prerequisite/constraint rows re-evidenced to `ScopeOfWork.md`, two new DOWNSTREAM interface rows (DEL-02-02, DEL-04-04) that correspond to the SOW-081 ownership split on L484, and one new EXTERNAL constraint row (K-PATH-2) whose owning document is unresolved.
- Expect reciprocal UPSTREAM rows in the DEL-02-02 and DEL-04-04 registers from their own SCA-APP-010 extraction passes; this register does not assert them.
- Carry the Q16 CONFLICT (decomposition L251/L602 versus D-APP-108 seating) to the OI-008 register owner; it is documentary, not a graph edge.
- DEP-07-03-012, DEP-07-03-013, and DEP-07-03-014 remain PENDING until DEL-07-03-V3-01 lands the workflow file contract and validator; no lifecycle, dependency-acceptance, or Root act is implied.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=14; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

7 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
