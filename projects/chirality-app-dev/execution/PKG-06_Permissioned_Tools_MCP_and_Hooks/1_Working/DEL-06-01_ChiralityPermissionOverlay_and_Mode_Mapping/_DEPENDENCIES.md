# Dependencies: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-01-001, DEP-06-01-002, DEP-06-01-003, DEP-06-01-004, DEP-06-01-005, DEP-06-01-006, DEP-06-01-007, DEP-06-01-008, DEP-06-01-009, DEP-06-01-010, DEP-06-01-011, DEP-06-01-012, DEP-06-01-013, DEP-06-01-014

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-01-010` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 11 |
| RETIRED rows | 3 |
| ACTIVE ANCHOR rows | 5 |
| ACTIVE EXECUTION rows | 6 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-06-01-001 | ANCHOR | UPSTREAM | OTHER | PKG-06 | ACTIVE | SATISFIED |
| DEP-06-01-002 | ANCHOR | UPSTREAM | OTHER | SOW-054 | ACTIVE | SATISFIED |
| DEP-06-01-003 | ANCHOR | UPSTREAM | OTHER | SOW-055 | ACTIVE | SATISFIED |
| DEP-06-01-004 | ANCHOR | UPSTREAM | OTHER | SOW-056 | ACTIVE | SATISFIED |
| DEP-06-01-005 | ANCHOR | UPSTREAM | OTHER | SOW-058 | ACTIVE | SATISFIED |
| DEP-06-01-006 | EXECUTION | UPSTREAM | PREREQUISITE | REF-004 | ACTIVE | PENDING |
| DEP-06-01-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | PENDING |
| DEP-06-01-008 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | PENDING |
| DEP-06-01-009 | EXECUTION | UPSTREAM | PREREQUISITE | REF-005 | ACTIVE | PENDING |
| DEP-06-01-010 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | ACTIVE | SATISFIED |
| DEP-06-01-011 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-04 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-012 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-02 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-013 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-03 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-014 | EXECUTION | UPSTREAM | INTERFACE | TBD | ACTIVE | PENDING |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used RuntimeOverrides: `SCOPE=DEL-06-01`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` and decomposition traceability fields.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation status: available; parent anchor resolves to `PKG-06`; SOW trace anchors resolve to SOW-054, SOW-055, SOW-056, and SOW-058.
- Parent anchor check: PASS. One ACTIVE `IMPLEMENTS_NODE` anchor exists.
- [HISTORICAL WARNING] SOURCE_STATE: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-01-010` is now `SATISFIED`.
- [WARNING] TARGET_TBD: Event writer/session JSONL append API dependency is explicit in `Procedure.md` as an assumption, but exact target deliverable and call path remain `TBD`; row DEP-06-01-014 preserves `TargetType=UNKNOWN`.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-06-01`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `d25f620aaa9ba04c4119cfda1d9c170d804b5c008541eb1d037112429b6a2ad0`; `_CONTEXT.md` `28429ef4d885a973c0a6431b740e3322fead960889af858a77b67c8bb2fc6e98`; `_REFERENCES.md` `574fb841828f60c054176e81cce51e6fb352a309d61ab49528f7687c48ec0f55`; `_STATUS.md` `900236a0385a8598e5e7bf56c2b5e91b00eda69a1792e73b09b36b3e412ef5e8`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `1227a161c177147a343614442fa64d07ad0a719c16bd3264d2a0972e1dba573d`, `_DEPENDENCIES.md` `d4ade8be402fdd839c68de777e83a3751981fdb92a59b030f1ee16c1721f5556`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-22; the 2026-09-23 retired-status clauses are the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 11 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- New text scanned: the 2026-09-23 edit to procedure step 5 names no other deliverable. The retired `_STATUS.md` `## Remaining` section was cited by no row of this register.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row whose evidence fields this run changed carries the finding (one `LastSeen`-only row, DEP-06-01-001, carries the pre-existing finding); no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | ACTIVE counts | Warnings |
|---|---|---|---|---|---|
| 2026-05-20T19:41:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | 14 total: 5 ANCHOR, 9 EXECUTION | Historical SOURCE_STATE REF-006 HASH_MISMATCH, later reconciled by D-APP-38 corpus v2; TARGET_TBD DEP-06-01-014 |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | ACTIVE=11 (ANCHOR=5; EXECUTION=6) | none |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 11 |
| Status | RETIRED | 3 |
| SatisfactionStatus | NOT_APPLICABLE | 3 |
| SatisfactionStatus | PENDING | 5 |
| SatisfactionStatus | SATISFIED | 6 |
| RequiredMaturity | SEMANTIC_READY | 14 |
| DependencyClass | ANCHOR | 5 |
| DependencyClass | EXECUTION | 9 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | INTERFACE | 4 |
| DependencyType | OTHER | 5 |
| DependencyType | PREREQUISITE | 4 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-127
- **Current counts:** ACTIVE 11; RETIRED 3; NOT_APPLICABLE=3; PENDING=5; SATISFIED=6.
- **Correction:** DEP-06-01-014 now names the appendHarnessEvent call path; upstream deliverable identity remains unassigned.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=3; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=11, RETIRED=3. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_04_06_SUPPORTED_APPROVED.csv`; current rows: ACTIVE=11, RETIRED=3. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
