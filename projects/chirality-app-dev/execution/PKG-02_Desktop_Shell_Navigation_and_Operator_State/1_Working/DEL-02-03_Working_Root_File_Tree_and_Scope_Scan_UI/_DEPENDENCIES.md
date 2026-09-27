# Dependencies: DEL-02-03 Working Root File Tree and Scope Scan UI

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See the current formal `Dependencies.csv` rows whose Direction is UPSTREAM; satisfaction and gates are read from that register, not inferred here.

## Declared Downstream

See the current formal `Dependencies.csv` rows whose Direction is DOWNSTREAM. No new dependency or status is created by this descriptive mirror.

## Current Extracted Dependency Summary — 2026-09-22

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 9 |
| ACTIVE rows | 9 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 3 |
| ACTIVE EXECUTION rows | 6 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-02-03-001 | ANCHOR | UPSTREAM | OTHER | PKG-02 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-002 | ANCHOR | UPSTREAM | OTHER | SOW-002 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-003 | ANCHOR | UPSTREAM | OTHER | SOW-003 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-004 | EXECUTION | UPSTREAM | INTERFACE | REF-003 | ACTIVE | TBD |
| DEP-02-03-005 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-01 | ACTIVE | TBD |
| DEP-02-03-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-03 | ACTIVE | TBD |
| DEP-02-03-007 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-04 | ACTIVE | TBD |
| DEP-02-03-008 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-05 | ACTIVE | TBD |
| DEP-02-03-009 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-08-03 | ACTIVE | TBD |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- Runtime overrides used: `SCOPE=DEL-02-03`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as dependency evidence.
- Human ruling applied: `_STATUS.md` was not read because it was outside the dependency-extraction evidence set authorized for this run.
- Anchor document selected by AUTO heuristic: `Datasheet.md`.
- Execution document order selected by AUTO heuristic: `Procedure.md`, `Guidance.md`, `Specification.md`, then `Datasheet.md`.
- Decomposition authority located and used for anchor and target validation: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Schema validator command required by dispatch: `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_dependencies_schema.py <ScopePath>/Dependencies.csv`.
- `[WARNING] PRD_HASH_MISMATCH`: `_REFERENCES.md` records REF-006 hash mismatch. Existing four-document outputs treat PRD-derived content as warned local source material; this run preserved that warning and did not read `docs/PRD.md`.
- `[WARNING] PACKAGE_FOLDER_LABEL_MISMATCH`: `Guidance.md` records a stale dispatch package-folder label versus the accessible scaffolded folder. Stable IDs `PKG-02` and `DEL-02-03` were used for extraction.
- `[WARNING] TARGET_RESOLUTION_MEDIUM`: DEL-07-03, DEL-07-04, and DEL-07-05 execution targets are resolved from decomposition descriptions and explicit local statements, but exact implementation/widget fields remain `TBD`.
- No `[WARNING] FLOATING_NODE`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] MISSING_DECOMPOSITION`: the explicit decomposition authority was available.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-02-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `e55fa6e2899c061ac68d426a4386a1a583eb2a19b8724056fa15e3198115b3f8`; `_CONTEXT.md` `f21078aff618bc3a986915ff09956dac2ffec5746cce98cee3c4e06d2bd05ffb`; `_REFERENCES.md` `d7c2cf034b749d2f662f7c19df66be31a46f94bd1e6dfe7b6b2b748a762f6463`; `_STATUS.md` `c6132084f55624a28bcb5658b042a22154fb7b80d5bf44b982f7ea384ff8ed53`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `6776d1fcc41ca51daf18265067f7bf07f68f47a5cbc254791e0b7c4579356784`, `_DEPENDENCIES.md` `8376468e3a00a9aed73c32abbad7957c9bc040540774ced903c95199629cfb87`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 8 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 1; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - KEPT DEP-02-03-009 (EXECUTION DOWNSTREAM INTERFACE -> DEL-08-03) DX-15; see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:30:42-0600 | UPDATE | CONSERVATIVE | available: `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PRD_HASH_MISMATCH; PACKAGE_FOLDER_LABEL_MISMATCH; TARGET_RESOLUTION_MEDIUM | 9 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=9 (ANCHOR=3; EXECUTION=6) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 9 |
| SatisfactionStatus | NOT_APPLICABLE | 3 |
| SatisfactionStatus | TBD | 6 |
| RequiredMaturity | TBD | 9 |
| DependencyClass | ANCHOR | 3 |
| DependencyClass | EXECUTION | 6 |
| DependencyType | INTERFACE | 6 |
| DependencyType | OTHER | 3 |

## Current evidence-locator refresh — 2026-09-22

6 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
