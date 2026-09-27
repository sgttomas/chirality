# Dependencies: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-09-04-001`, `DEP-09-04-002`, `DEP-09-04-003`, `DEP-09-04-004`, `DEP-09-04-005`, `DEP-09-04-006`, `DEP-09-04-007`, `DEP-09-04-008`, `DEP-09-04-009`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract updated this register on 2026-05-20T21:02:18-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` outputs are invalid evidence and were not read or consumed.
- Anchor document selection: `_CONTEXT.md` and `Datasheet.md`; execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available and used to validate PKG-09, DEL-09-04, SOW-030, SOW-072, SOW-073, OI-003, and OI-004.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- [WARNING] OPEN_ISSUE_TARGET_TYPE: OI-003 and OI-004 were preserved as `TargetType=UNKNOWN` because `OPEN_ISSUE` is not a Dependencies.csv v3.1 target enum.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor (`DEP-09-04-001`) exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor exists.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-09-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `57b567dfcd1e5a4c24ea0da655595789faca599a772b09dc1c5c106b83953c87`; `_CONTEXT.md` `9f89ea862cadc7f6002d0a0cd791c14b16bf38b94a44be834b5319db2a983f9a`; `_REFERENCES.md` `535bb9cdab296d4e0005d11ba6c56fc967da35d4461b7021d57d3eb9acfa18fa`; `_STATUS.md` `937bbacfb4d4cc7a1ad9aa763c825b1dfa52ab83d1f900d040a6fc1e17c58783`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `00bb72a4ca1869eb615e266663987ee499eeaee3f743b8d70cc3779251a1369d`, `_DEPENDENCIES.md` `0f857d8e55e5e76c639922bf430c368bdc7ac08ff0926ca1b283df124023f651`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-22; the 2026-09-23 retired-status clauses are the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 9 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- [INFO] New text scanned: APP-R078 in the 2026-09-23 retired status detail ('Preserve source artwork and the renderer removal direction with DEL-02-01') names DEL-02-01 without a direction. The relationship is already recorded from the supplier side as DEP-02-01-013 (DEL-02-01 -> DEL-09-04, re-evidenced to APP-R016 on 2026-09-27), so under `STRICTNESS=CONSERVATIVE` no row is emitted here; noted for the register owner.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 9 |
| ACTIVE rows | 9 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 4 |
| ACTIVE EXECUTION rows | 5 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-09-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-09 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-030 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-072 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-004 | ANCHOR | UPSTREAM | OTHER | SOW-073 | ACTIVE | TBD |
| DEP-09-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | Node.js and frontend npm dependencies | ACTIVE | TBD |
| DEP-09-04-006 | EXECUTION | UPSTREAM | PREREQUISITE | Pre-packaging local validation commands | ACTIVE | TBD |
| DEP-09-04-007 | EXECUTION | UPSTREAM | CONSTRAINT | OI-004 | ACTIVE | TBD |
| DEP-09-04-008 | EXECUTION | UPSTREAM | CONSTRAINT | OI-003 | ACTIVE | TBD |
| DEP-09-04-009 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-09-04-REQ-009 | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---|
| 2026-05-20T21:02:18-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | REF-006_HASH_MISMATCH; OPEN_ISSUE_TARGET_TYPE | 9 |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=9 (ANCHOR=4; EXECUTION=5) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 9 |
| SatisfactionStatus | NOT_APPLICABLE | 3 |
| SatisfactionStatus | TBD | 6 |
| RequiredMaturity | SEMANTIC_READY | 9 |
| DependencyClass | ANCHOR | 4 |
| DependencyClass | EXECUTION | 5 |
| DependencyType | CONSTRAINT | 3 |
| DependencyType | OTHER | 4 |
| DependencyType | PREREQUISITE | 2 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_09_PREVIEW.csv`; current rows: ACTIVE=9, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
