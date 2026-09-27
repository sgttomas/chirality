# Dependencies: DEL-07-04 Status Transition API and MCP Tool

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-04-001`, `DEP-07-04-002`, `DEP-07-04-003`, `DEP-07-04-004`, `DEP-07-04-006`, `DEP-07-04-007`, `DEP-07-04-008`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- Source set used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source set excluded by human ruling: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment are skipped.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` traceability and decomposition validation.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available; DEL-07-04, SOW-028, OBJ-006, PKG-07, and referenced document metadata were validated against allowed evidence.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] IMPLEMENTATION_LOCATION_TBD`: allowed evidence names no implementation module path; dependency row DEP-07-04-008 preserves the target as `UNKNOWN` / `TBD`.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-07-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `df03ef53fe679a7e4a4e49f0959c1f49cf8d620afe872da800de55b3385107ba`; `_CONTEXT.md` `2826e3e4a85958fbbc2a5d8aab8285a88eabc2ff038d128ba59a7e437c38e225`; `_REFERENCES.md` `69289826fa0d126290dfab5249a161b3f2057cfde6670ed522e5300151bfe95c`; `_STATUS.md` `2bd550404ae2797d3cfa278934165501492b1db644de82d68ad14d3000abd56d`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `40800079ee62803b750671f17360e92cc33abb34d5843fa7883067523b07e592`, `_DEPENDENCIES.md` `fb9db9dc9a588d92fdc032db809b5a319d8df44f7bf134af59ed9b573481a7a4`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 7 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 1; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - ADDED DEP-07-04-009 (EXECUTION DOWNSTREAM INTERFACE -> DEL-06-03) (beyond DX); see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 9 |
| ACTIVE rows | 8 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 2 |
| ACTIVE EXECUTION rows | 6 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-07-04-001 | ANCHOR | UPSTREAM | OTHER | SOW-028 | ACTIVE | NOT_APPLICABLE |
| DEP-07-04-002 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | NOT_APPLICABLE |
| DEP-07-04-003 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | PENDING |
| DEP-07-04-004 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | PENDING |
| DEP-07-04-005 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | RETIRED | NOT_APPLICABLE |
| DEP-07-04-006 | EXECUTION | UPSTREAM | CONSTRAINT | REF-001 | ACTIVE | PENDING |
| DEP-07-04-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | PENDING |
| DEP-07-04-008 | EXECUTION | UPSTREAM | PREREQUISITE | TBD | ACTIVE | SATISFIED |
| DEP-07-04-009 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-06-03 | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | PRD_HASH_MISMATCH; IMPLEMENTATION_LOCATION_TBD | 8 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | none | ACTIVE=8 (ANCHOR=2; EXECUTION=6) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 8 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 3 |
| SatisfactionStatus | PENDING | 4 |
| SatisfactionStatus | SATISFIED | 1 |
| SatisfactionStatus | TBD | 1 |
| RequiredMaturity | SEMANTIC_READY | 8 |
| RequiredMaturity | TBD | 1 |
| DependencyClass | ANCHOR | 2 |
| DependencyClass | EXECUTION | 7 |
| DependencyType | CONSTRAINT | 2 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 2 |
| DependencyType | PREREQUISITE | 4 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-132
- **Current counts:** ACTIVE 7; RETIRED 1; NOT_APPLICABLE=3; PENDING=4; SATISFIED=1.
- **Correction:** DEP-07-04-008 resolves to landed implementation modules and is SATISFIED; ResponsibleParty remains separate.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
