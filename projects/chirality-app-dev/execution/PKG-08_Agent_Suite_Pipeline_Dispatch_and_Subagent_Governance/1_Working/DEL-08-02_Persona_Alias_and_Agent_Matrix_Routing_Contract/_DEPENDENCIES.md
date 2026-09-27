# Dependencies: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-08-02-001`, `DEP-08-02-002`, `DEP-08-02-003`, `DEP-08-02-004`, `DEP-08-02-005`, `DEP-08-02-006`, `DEP-08-02-007`, `DEP-08-02-008`, `DEP-08-02-009`, `DEP-08-02-010`, `DEP-08-02-011`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-08-02-012`, `DEP-08-02-013`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 6 |
| ACTIVE EXECUTION rows | 7 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-08-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-08 | ACTIVE | SATISFIED |
| DEP-08-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-005 | ACTIVE | SATISFIED |
| DEP-08-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-006 | ACTIVE | SATISFIED |
| DEP-08-02-004 | ANCHOR | UPSTREAM | OTHER | SOW-017 | ACTIVE | SATISFIED |
| DEP-08-02-005 | ANCHOR | UPSTREAM | OTHER | OBJ-001 | ACTIVE | SATISFIED |
| DEP-08-02-006 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | SATISFIED |
| DEP-08-02-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | PENDING |
| DEP-08-02-008 | EXECUTION | UPSTREAM | PREREQUISITE | REF-006 | ACTIVE | PENDING |
| DEP-08-02-009 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | PENDING |
| DEP-08-02-010 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | PENDING |
| DEP-08-02-011 | EXECUTION | UPSTREAM | PREREQUISITE | REF-001 | ACTIVE | PENDING |
| DEP-08-02-012 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-04-04 | ACTIVE | TBD |
| DEP-08-02-013 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-08-03 | ACTIVE | TBD |

## Run Notes

- Run timestamp: 2026-05-20T20:54:44-0600.
- TaskSkill: `dependency-extract`; mode `UPDATE`; strictness `CONSERVATIVE`; consumer context `NONE`.
- Decomposition authority: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Defaults applied: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Specification.md -> Guidance.md -> Procedure.md -> _REFERENCES.md`.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 authority corpus v2 supersedes the prior PRD hash warning; `_REFERENCES.md` now records REF-006 as MATCH.
- `[RESOLVED] LOOP_FIRST_CONTRACT`: ADQ-12 records the current Type 0/1 loop-persona alias and matrix contract; old `AGGREGATE`/`RECONCILING` alias requirements are not preserved as compatibility behavior.
- `[RESOLVED] IMPLEMENTATION_PATHS`: ADQ-12 evidence records the persona-resolution, matrix-cell, matrix-launch, and Pipeline component/test paths used for this tranche.
- Non-emitted edge note: shared SOW ownership with DEL-02-01 and DEL-02-02 was not converted into execution edges because the allowed source documents do not state a concrete handoff or interface contract to those deliverables.
- Non-emitted edge note: REF-005 `docs/PLAN.md` and REF-007 `AGENT_SOFTWARE_DECOMP.md` were not emitted as dependency rows because evidence only identifies them as context/method references, not execution prerequisites for this deliverable.

## Run Notes - 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-08-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `2a9dc258d8e79627b8fb36ed7dc72dc8ea0b22b396b80260942289fe6389c607`; `_CONTEXT.md` `2b21d30cf974a1c3c416d7e3208a8a5ce2454f5d4b237d879d0fe090f2950e29`; `_REFERENCES.md` `19169ef712856d0dba1fda0c0f7081df59efe713637fb6cf51fc74f84cb79d8b`; `_STATUS.md` `afe911057cf3d8086b7ad6f758b6937cd89f5d67f6cacc0833b5a85cca2cf380`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `26837466f07ac9798c9f63e9058b68ca3eb6ebe0293b6a124d4ba483289519a6`, `_DEPENDENCIES.md` `3f0bffa71dc9877caed6f07fd57d3b052a6549258d8e5b192cb7b5477790e5bc`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 11 (`LastSeen=2026-09-27`); restated in place 2; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RESTATED DEP-08-02-003 (ANCHOR UPSTREAM OTHER -> SOW-006) DX-13; see the row `Notes`.
  - RESTATED DEP-08-02-005 (ANCHOR UPSTREAM OTHER -> OBJ-001) DX-14; see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Validator | ACTIVE Rows | Warnings |
|---|---|---|---|---|---:|---|
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, loop-first alias contract, and implementation-path evidence applied | PASS: focused PKG-08 tests | 13 | none |
| 2026-05-20T20:54:44-0600 | UPDATE | CONSERVATIVE | v3.2 found | PASS: 29 columns, 13 rows | 13 | superseded PRD_HASH_MISMATCH; superseded implementation-path TBDs |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | — | ACTIVE=13 (ANCHOR=6; EXECUTION=7) | none |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 13 |
| SatisfactionStatus | PENDING | 5 |
| SatisfactionStatus | SATISFIED | 6 |
| SatisfactionStatus | TBD | 2 |
| RequiredMaturity | SEMANTIC_READY | 13 |
| DependencyClass | ANCHOR | 6 |
| DependencyClass | EXECUTION | 7 |
| DependencyType | INTERFACE | 2 |
| DependencyType | OTHER | 6 |
| DependencyType | PREREQUISITE | 5 |

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

9 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
