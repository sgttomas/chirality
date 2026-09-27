# Dependencies: DEL-09-03 Unit and Integration Test Expansion

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-09-03-001`, `DEP-09-03-002`, `DEP-09-03-003`, `DEP-09-03-004`, `DEP-09-03-005`, `DEP-09-03-006`, `DEP-09-03-007`, `DEP-09-03-008`, `DEP-09-03-009`, `DEP-09-03-010`, `DEP-09-03-011`, `DEP-09-03-012`, `DEP-09-03-013`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract update applied current human ruling: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Defaults and overrides: `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO`; `DOC_ROLE_MAP=DEFAULT`; `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Procedure.md, Guidance.md, Specification.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` reports REF-006 expected SHA does not match observed SHA. Existing source files treat this as a warning, not a blocker.
- [WARNING] SOURCE_CONFLICT_SUPERSEDED: earlier four-document initialization text said `Dependencies.csv` must not be created yet; current human dependency-recording ruling superseded that deferral for this run.
- Conservative extraction emitted explicit anchors and one explicit execution interface only. Implementation-surface prerequisites remain `TBD` where not directly stated as accepted dependency edges.
- 2026-07-10 correction (D-APP-53 reconciliation): the 2026-05-20 `[WARNING] PRD_HASH_MISMATCH` above is stale and no longer describes live state — `_REFERENCES.md` line 12 now records REF-006 (`docs/PRD.md`) expected SHA `ac35fba4...` matching observed SHA, Status MATCH. The historical warning is retained above for provenance; it should not be relied on.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 12 |
| ACTIVE EXECUTION rows | 1 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-09-03-001 | ANCHOR | UPSTREAM | OTHER | PKG-09 | ACTIVE | SATISFIED |
| DEP-09-03-002 | ANCHOR | UPSTREAM | OTHER | SOW-011 | ACTIVE | SATISFIED |
| DEP-09-03-003 | ANCHOR | UPSTREAM | OTHER | SOW-012 | ACTIVE | SATISFIED |
| DEP-09-03-004 | ANCHOR | UPSTREAM | OTHER | SOW-014 | ACTIVE | SATISFIED |
| DEP-09-03-005 | ANCHOR | UPSTREAM | OTHER | SOW-015 | ACTIVE | SATISFIED |
| DEP-09-03-006 | ANCHOR | UPSTREAM | OTHER | SOW-022 | ACTIVE | SATISFIED |
| DEP-09-03-007 | ANCHOR | UPSTREAM | OTHER | SOW-028 | ACTIVE | SATISFIED |
| DEP-09-03-008 | ANCHOR | UPSTREAM | OTHER | SOW-029 | ACTIVE | SATISFIED |
| DEP-09-03-009 | ANCHOR | UPSTREAM | OTHER | OBJ-002 | ACTIVE | SATISFIED |
| DEP-09-03-010 | ANCHOR | UPSTREAM | OTHER | OBJ-003 | ACTIVE | SATISFIED |
| DEP-09-03-011 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | SATISFIED |
| DEP-09-03-012 | ANCHOR | UPSTREAM | OTHER | OBJ-008 | ACTIVE | SATISFIED |
| DEP-09-03-013 | EXECUTION | UPSTREAM | INTERFACE | DEL-09-02 | ACTIVE | SATISFIED |

## Run Notes - 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-09-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `bc704dc50f386286f947da1fc4ff0fbef21bd6afa8fe2aa8bbe75d4837e83d76`; `_CONTEXT.md` `5d9002d4beb2756c5cd453922aaab73c75a3a59b4dfd97d41b08fc44a8d85f24`; `_REFERENCES.md` `08e17cc4a83dc4824ac37dceb04b53285771e58566f88149997e77e335d59886`; `_STATUS.md` `4be3a817bdd53205652a7db48e1b875cf922ee2aa794f368ecd75dd63becaded`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `1b78d95f3e83c79ff6e80ca16dab5ad92f27c8f85b1be9439fcaa412aea309f5`, `_DEPENDENCIES.md` `eaee3b45079fbe32fb816c3a60a7f6bc3ef2bb48a48e15b2aa6a77ca0e3e651f`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 13 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

- 2026-05-20 21:02 MDT — `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition found and used at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; warnings: PRD hash mismatch, superseded dependency deferral note; ACTIVE counts: ANCHOR 12, EXECUTION 1.
- 2026-07-10 — D-APP-53 reconciliation (DRQ-05, `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`): all 13 rows re-verified against live evidence and moved `SatisfactionStatus` TBD -> SATISFIED; 12 stale decomposition line pointers refreshed (+6 offset; PKG-09 anchor 350->269); stale PRD_HASH_MISMATCH warning corrected with dated note. Reconciliation record: `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. Linter PASS (13 rows, 0 errors, 0 warnings). No lifecycle transition; `_STATUS.md` untouched.
- 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`): `dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`; decomposition found, SHA-256 `cf6e56ebb147…` (SCA-APP-011 amended); warnings: none; ACTIVE=13 (ANCHOR=12, EXECUTION=1); RETIRED=0.

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 13 |
| SatisfactionStatus | SATISFIED | 13 |
| RequiredMaturity | TBD | 13 |
| DependencyClass | ANCHOR | 12 |
| DependencyClass | EXECUTION | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 12 |

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

11 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
