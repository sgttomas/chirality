# Dependencies: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-02-001, DEP-06-02-002, DEP-06-02-003, DEP-06-02-004, DEP-06-02-005, DEP-06-02-006, DEP-06-02-007, DEP-06-02-008, DEP-06-02-009, DEP-06-02-010, DEP-06-02-011

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-02-011` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Semantic lensing and P3 enrichment were skipped by human ruling; `_SEMANTIC.md` was not read or consumed.
- Decomposition authority was available and used for anchor validation and canonical target labels.
- Anchor document selected by AUTO/default heuristic: `Datasheet.md` with confirmation from `_CONTEXT.md` and decomposition authority.
- Execution document order selected by AUTO/default heuristic: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- [HISTORICAL WARNING] PRD_HASH_MISMATCH: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-02-011` is now `SATISFIED`.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-06-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `92dc36d418b19074120844e0360ec2940859036c780c3d5a4a361db90c81694e`; `_CONTEXT.md` `5b1b3533fb3cab5e85cfe9cfa11ce37bef3c3692527df1a7c8cce172e1711db7`; `_REFERENCES.md` `899477d7ff7d2a9a504cf6ad32f847c690682f7a1268d73dd700541b2c1657f4`; `_STATUS.md` `444633fbf6b088325910b58286e8822b4b8fd0e9f8406dc3bfb4dde3591c166e`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `8c15849d23d2de9a5440d3e66ff496d2b918773d5051f2f700880c209ffa7f63`, `_DEPENDENCIES.md` `fa4424f57c2f6f0fd4a117c310843111cdb3e6ae922a9c2ff3c806c825653fd5`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-22; the 2026-09-23 retired-status clauses are the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 11 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- New text scanned: the 2026-09-23 edit to procedure step 5 names no other deliverable. The retired `_STATUS.md` `## Remaining` section was cited by no row of this register.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 11 |
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 4 |
| ACTIVE EXECUTION rows | 7 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-06-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-06 | ACTIVE | TBD |
| DEP-06-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-047 | ACTIVE | TBD |
| DEP-06-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-049 | ACTIVE | TBD |
| DEP-06-02-004 | ANCHOR | UPSTREAM | OTHER | SOW-050 | ACTIVE | TBD |
| DEP-06-02-005 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-06-01 | ACTIVE | TBD |
| DEP-06-02-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-03 | ACTIVE | TBD |
| DEP-06-02-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | TBD |
| DEP-06-02-008 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | TBD |
| DEP-06-02-009 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | TBD |
| DEP-06-02-010 | EXECUTION | UPSTREAM | PREREQUISITE | REF-005 | ACTIVE | TBD |
| DEP-06-02-011 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | ACTIVE | SATISFIED |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:47:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | Historical PRD_HASH_MISMATCH, later reconciled by D-APP-38 corpus v2 | 11 |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=11 (ANCHOR=4; EXECUTION=7) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 11 |
| SatisfactionStatus | SATISFIED | 1 |
| SatisfactionStatus | TBD | 10 |
| RequiredMaturity | SEMANTIC_READY | 11 |
| DependencyClass | ANCHOR | 4 |
| DependencyClass | EXECUTION | 7 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 4 |
| DependencyType | PREREQUISITE | 5 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
