# Dependencies: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-05-001`, `DEP-07-05-002`, `DEP-07-05-003`, `DEP-07-05-004`, `DEP-07-05-005`, `DEP-07-05-006`, `DEP-07-05-007`, `DEP-07-05-008`, `DEP-07-05-009`, `DEP-07-05-010`, `DEP-07-05-011`, `DEP-07-05-012`, `DEP-07-05-013`, `DEP-07-05-014`, `DEP-07-05-015`, `DEP-07-05-016`, `DEP-07-05-017`, `DEP-07-05-018`, `DEP-07-05-019`, `DEP-07-05-020`, `DEP-07-05-021`, `DEP-07-05-022`, `DEP-07-05-023`, `DEP-07-05-024`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-07-05-025`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 26 |
| ACTIVE rows | 25 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 20 |
| ACTIVE EXECUTION rows | 5 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-07-05-001 | ANCHOR | UPSTREAM | OTHER | SOW-029 | ACTIVE | TBD |
| DEP-07-05-002 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | TBD |
| DEP-07-05-003 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-001 | ACTIVE | TBD |
| DEP-07-05-004 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-002 | ACTIVE | TBD |
| DEP-07-05-005 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-003 | ACTIVE | TBD |
| DEP-07-05-006 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-004 | ACTIVE | TBD |
| DEP-07-05-007 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-005 | ACTIVE | TBD |
| DEP-07-05-008 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-006 | ACTIVE | TBD |
| DEP-07-05-009 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-007 | ACTIVE | TBD |
| DEP-07-05-010 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-008 | ACTIVE | TBD |
| DEP-07-05-011 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-009 | ACTIVE | TBD |
| DEP-07-05-012 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-010 | ACTIVE | TBD |
| DEP-07-05-013 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-011 | ACTIVE | TBD |
| DEP-07-05-014 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-012 | ACTIVE | TBD |
| DEP-07-05-015 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-013 | ACTIVE | TBD |
| DEP-07-05-016 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-014 | ACTIVE | TBD |
| DEP-07-05-017 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-015 | ACTIVE | TBD |
| DEP-07-05-018 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-016 | ACTIVE | TBD |
| DEP-07-05-019 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-017 | ACTIVE | TBD |
| DEP-07-05-020 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-018 | ACTIVE | TBD |
| DEP-07-05-021 | EXECUTION | UPSTREAM | PREREQUISITE | Accepted source references | ACTIVE | TBD |
| DEP-07-05-022 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003;REF-004 | ACTIVE | TBD |
| DEP-07-05-023 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002;REF-001 | ACTIVE | TBD |
| DEP-07-05-024 | EXECUTION | UPSTREAM | CONSTRAINT | REF-003;REF-002 | ACTIVE | TBD |
| DEP-07-05-025 | EXECUTION | DOWNSTREAM | INTERFACE | Dependency library and retained Chirality tool contracts | ACTIVE | TBD |
| DEP-07-05-026 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | RETIRED | NOT_APPLICABLE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK run `TASK_RUN_2026-05-20_1954.md` used `TaskSkill=dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source document selection: `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Specification.md, Guidance.md, Procedure.md`; `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md` were used for identity, reference, and declared-edge context.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was invalid evidence and was not read or consumed.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row was found for `SOW-029`.
- No declared rows were present to preserve or merge. All rows in this run are extracted rows.
- [WARNING] OBJECTIVE_TARGET_TYPE_UNAVAILABLE: `OBJ-006` is explicit evidence, but the v3.1 `TargetType` enum has no `OBJECTIVE`; the row preserves `TargetType=UNKNOWN`.
- [WARNING] UNKNOWN_INTERFACE_CONSUMER: the API/MCP dependency surface is explicit, but no consumer deliverable ID is explicitly named in the evidence; the row preserves `TargetType=UNKNOWN`.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-07-05`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `edd9377519617799f78c20433631390096b52b86236ee3710a501d25c1d095b8`; `_CONTEXT.md` `c4b7d418b00b1ff1c895ecc7274cce80bf20f24ca4a0759eea82169626394cd6`; `_REFERENCES.md` `bfc1a7455af88525e29ebefc290e05d2ce9fa7748604e307e4df0e954f32f421`; `_STATUS.md` `71b50f298f742e7f6bca593dcb22f81208977fd74630cb6d98d313a61ff052a9`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `1a938719e822b8dcc267e1e407a84e89749b4f361f2e61e9181be9b004e6a2b3`, `_DEPENDENCIES.md` `6c5585213b10ef34a1833679426189c3ec6048cac8a13fde1a65318aa6204b8a`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 23 (`LastSeen=2026-09-27`); restated in place 2; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RESTATED DEP-07-05-015 (ANCHOR UPSTREAM OTHER -> REQ-DEL-07-05-013) (beyond DX); see the row `Notes`.
  - RESTATED DEP-07-05-025 (EXECUTION DOWNSTREAM INTERFACE -> Dependency library and retained Chirality tool contracts) DX-08,DX-09,DX-10; see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-07-05`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `edd9377519617799f78c20433631390096b52b86236ee3710a501d25c1d095b8`; `_CONTEXT.md` `c4b7d418b00b1ff1c895ecc7274cce80bf20f24ca4a0759eea82169626394cd6`; `_REFERENCES.md` `bfc1a7455af88525e29ebefc290e05d2ce9fa7748604e307e4df0e954f32f421`; `_STATUS.md` `71b50f298f742e7f6bca593dcb22f81208977fd74630cb6d98d313a61ff052a9`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `5e0455ca13f2f325cc92471bd3fe19a4e7a282ffdf024fde7a212697aebdbdb6`, `_DEPENDENCIES.md` `20301c6c4731545bfc328e0f4f82c58afbf380543a34d6f56e16f4d37e12b25c`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; no source text changed since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 25 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20 19:54 | UPDATE | CONSERVATIVE | Found v3.2 decomposition authority | OBJECTIVE_TARGET_TYPE_UNAVAILABLE; UNKNOWN_INTERFACE_CONSUMER; SOURCE_HASH_MISMATCH | 26 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=25 (ANCHOR=20; EXECUTION=5) |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=25 (ANCHOR=20; EXECUTION=5) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 25 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 1 |
| SatisfactionStatus | TBD | 25 |
| RequiredMaturity | SEMANTIC_READY | 26 |
| DependencyClass | ANCHOR | 20 |
| DependencyClass | EXECUTION | 6 |
| DependencyType | CONSTRAINT | 2 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 20 |
| DependencyType | PREREQUISITE | 3 |

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

## Current residual-specific interpretation — 2026-09-22

DEP-001..025 four-document EvidenceFile/SourceRef values preserve historical source quotations; ScopeOfWork.md is the current claim carrier. OBJECTIVE_TARGET_TYPE_UNAVAILABLE is a dated extraction warning, not a new current discovery: DEP-002 remains UNKNOWN in the unchanged formal register. Any decision to reclassify that formal target remains with its owning dependency pass.

## Current evidence-locator refresh — 2026-09-22

24 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
