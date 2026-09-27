# Dependencies: DEL-09-02 Section 9 Runtime Validation Additions

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-09-02-001`, `DEP-09-02-002`, `DEP-09-02-003`, `DEP-09-02-004`, `DEP-09-02-005`, `DEP-09-02-006`, `DEP-09-02-007`, `DEP-09-02-008`, `DEP-09-02-009`, `DEP-09-02-010`, `DEP-09-02-011`, `DEP-09-02-012`, `DEP-09-02-013`, `DEP-09-02-014`, `DEP-09-02-015`, `DEP-09-02-016`, `DEP-09-02-017`, `DEP-09-02-018`, `DEP-09-02-019`, `DEP-09-02-020`, `DEP-09-02-021`, `DEP-09-02-022`, `DEP-09-02-023`, `DEP-09-02-024`, `DEP-09-02-025`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority loaded: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation and target-label resolution were available.
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- Defaults applied: SOURCE_DOCS=AUTO, DOC_ROLE_MAP=DEFAULT, ANCHOR_DOC=Datasheet.md, EXECUTION_DOC_ORDER=Specification.md then Guidance.md then Procedure.md then Datasheet.md.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- [WARNING] TBD_SURFACES: exact validation registry path, runner entrypoint, local validation command, summary schema path, and summary fields remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one active `IMPLEMENTS_NODE` anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one active `IMPLEMENTS_NODE` anchor was extracted.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-09-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `ca76704effce155d6468722dac107bc62aa4c962ad1dec93affa7f59d329f516`; `_CONTEXT.md` `61e57646e2418b04bf43faae5ea4b21241b6f929b985258fe3a0d551218ddeff`; `_REFERENCES.md` `9fb2360eb265a583051470ce635fcc5abb13ee1b20dd2d80ef5f7814c50959c6`; `_STATUS.md` `063984ebc5838896e317ce223e51bcb548a072fa88c31b2af7cf76b1874b2eb3`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `cff709e7a99696701b6fae5d2009ba6d6a805e9f6a462da322140e1946b02094`, `_DEPENDENCIES.md` `ecb5e959c0dd724fefc25870df6cf30d48daf2f3ddc13eef2c984c396e25c0f3`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 25 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-09-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `ca76704effce155d6468722dac107bc62aa4c962ad1dec93affa7f59d329f516`; `_CONTEXT.md` `61e57646e2418b04bf43faae5ea4b21241b6f929b985258fe3a0d551218ddeff`; `_REFERENCES.md` `9fb2360eb265a583051470ce635fcc5abb13ee1b20dd2d80ef5f7814c50959c6`; `_STATUS.md` `063984ebc5838896e317ce223e51bcb548a072fa88c31b2af7cf76b1874b2eb3`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `6ea8736b17d06f532ea5f665b2562fa1c5fe4cfd3404d322520ba58dd96d746c`, `_DEPENDENCIES.md` `ac9ee54f1c52c5e6e6fd7fb7f7fdd9bb862edb82d3e5ebc91d9ff0cb63f7e4dc`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; no source text changed since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 25 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 25 |
| ACTIVE rows | 25 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 13 |
| ACTIVE EXECUTION rows | 12 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-09-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-09 | ACTIVE | TBD |
| DEP-09-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-036 | ACTIVE | TBD |
| DEP-09-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-037 | ACTIVE | TBD |
| DEP-09-02-004 | ANCHOR | UPSTREAM | OTHER | SOW-039 | ACTIVE | TBD |
| DEP-09-02-005 | ANCHOR | UPSTREAM | OTHER | SOW-045 | ACTIVE | TBD |
| DEP-09-02-006 | ANCHOR | UPSTREAM | OTHER | SOW-054 | ACTIVE | TBD |
| DEP-09-02-007 | ANCHOR | UPSTREAM | OTHER | SOW-057 | ACTIVE | TBD |
| DEP-09-02-008 | ANCHOR | UPSTREAM | OTHER | SOW-063 | ACTIVE | TBD |
| DEP-09-02-009 | ANCHOR | UPSTREAM | OTHER | OBJ-002 | ACTIVE | TBD |
| DEP-09-02-010 | ANCHOR | UPSTREAM | OTHER | OBJ-003 | ACTIVE | TBD |
| DEP-09-02-011 | ANCHOR | UPSTREAM | OTHER | OBJ-005 | ACTIVE | TBD |
| DEP-09-02-012 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | TBD |
| DEP-09-02-013 | ANCHOR | UPSTREAM | OTHER | OBJ-008 | ACTIVE | TBD |
| DEP-09-02-014 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-09-01 | ACTIVE | TBD |
| DEP-09-02-015 | EXECUTION | UPSTREAM | INTERFACE | DEL-03-01 | ACTIVE | TBD |
| DEP-09-02-016 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-03 | ACTIVE | TBD |
| DEP-09-02-017 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-02 | ACTIVE | TBD |
| DEP-09-02-018 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-02 | ACTIVE | TBD |
| DEP-09-02-019 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-01 | ACTIVE | TBD |
| DEP-09-02-020 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-03 | ACTIVE | TBD |
| DEP-09-02-021 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-04 | ACTIVE | TBD |
| DEP-09-02-022 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-06 | ACTIVE | TBD |
| DEP-09-02-023 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-05 | ACTIVE | TBD |
| DEP-09-02-024 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-04 | ACTIVE | TBD |
| DEP-09-02-025 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-05 | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ActiveRows |
|---|---|---|---|---|---:|
| 2026-05-20T20:54:54-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` loaded | PRD_HASH_MISMATCH; TBD_SURFACES | 25 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=25 (ANCHOR=13; EXECUTION=12) |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=25 (ANCHOR=13; EXECUTION=12) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 25 |
| SatisfactionStatus | TBD | 25 |
| RequiredMaturity | SEMANTIC_READY | 25 |
| DependencyClass | ANCHOR | 13 |
| DependencyClass | EXECUTION | 12 |
| DependencyType | INTERFACE | 11 |
| DependencyType | OTHER | 13 |
| DependencyType | PREREQUISITE | 1 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current residual-specific interpretation — 2026-09-22

TBD_SURFACES is an obsolete extraction warning for selected paths; ScopeOfWork.md now names current harness manifest/runner hooks. Actual satisfaction of the Runtime/Codex coverage still requires candidate-bound results against governing ScopeOfWork.md.

## Current evidence-locator refresh — 2026-09-22

19 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=25; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_09_PREVIEW.csv`; current rows: ACTIVE=25, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
