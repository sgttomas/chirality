# Dependencies: DEL-07-02 Execution Root Scaffolding from Decomposition

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-02-001`, `DEP-07-02-002`, `DEP-07-02-003`, `DEP-07-02-004`, `DEP-07-02-005`, `DEP-07-02-006`, `DEP-07-02-007`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 7 |
| ACTIVE rows | 7 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 3 |
| ACTIVE EXECUTION rows | 4 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-07-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-07 | ACTIVE | TBD |
| DEP-07-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-024 | ACTIVE | TBD |
| DEP-07-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-025 | ACTIVE | TBD |
| DEP-07-02-004 | EXECUTION | UPSTREAM | PREREQUISITE | execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md | ACTIVE | TBD |
| DEP-07-02-005 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-07-01 | ACTIVE | TBD |
| DEP-07-02-006 | EXECUTION | UPSTREAM | CONSTRAINT | REF-002 | ACTIVE | TBD |
| DEP-07-02-007 | EXECUTION | UPSTREAM | PREREQUISITE | _REFERENCES.md | ACTIVE | TBD |

## Run Notes

- Runtime overrides: `SCOPE=DEL-07-02`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selection: `Datasheet.md` with validation against the provided decomposition path.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition status: found and used for DEL-07-02, SOW-024, SOW-025, and DEL-07-01 target resolution.
- No `[WARNING] FLOATING_NODE`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one ACTIVE `IMPLEMENTS_NODE` anchor was extracted.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- Conservative extraction retained unresolved lifecycle values as `TBD` where source evidence does not prove satisfaction or proposed maturity.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-07-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `697754d4324058cc2b8aa27e30bd1a34b3b6383ea780fb1c22b0f0b263b121a4`; `_CONTEXT.md` `bd41b907e62b6a213c70b01a3cd2f22f3e47bbdbbe8035b7e6b5ca3ac05c92fa`; `_REFERENCES.md` `a92a0576cd2243cd5679ff17245c5f2e235af8132b9182bb1ea5aa0ff18c00e2`; `_STATUS.md` `23fee8e46f915b516f668995e3050cb9e310c130909ae4a5e39f365de75bd7e4`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `283b4b8136286e7ad466b4c6868ada54a5d05c46adc9e2935e56a1eb2233a76e`, `_DEPENDENCIES.md` `f2c53a122c7804e62260dafedc6b479b1bcc1fc39e02bab46498e0aadac15f10`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 7 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

- 2026-05-20 19:54 MDT - `TASK + dependency-extract`, mode `UPDATE`, strictness `CONSERVATIVE`, decomposition path found, semantic lensing skipped by human ruling, ACTIVE counts: ANCHOR 3, EXECUTION 4, warnings: REF-006 hash mismatch; no floating/ambiguous anchor.
- 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`): `dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`; decomposition found, SHA-256 `cf6e56ebb147…` (SCA-APP-011 amended); warnings: none; ACTIVE=7 (ANCHOR=3, EXECUTION=4); RETIRED=0.

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 7 |
| SatisfactionStatus | TBD | 7 |
| RequiredMaturity | SEMANTIC_READY | 4 |
| RequiredMaturity | TBD | 3 |
| DependencyClass | ANCHOR | 3 |
| DependencyClass | EXECUTION | 4 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | OTHER | 3 |
| DependencyType | PREREQUISITE | 3 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

6 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=7; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_EXTRA_3_PREVIEW.csv`; current rows: ACTIVE=7, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
