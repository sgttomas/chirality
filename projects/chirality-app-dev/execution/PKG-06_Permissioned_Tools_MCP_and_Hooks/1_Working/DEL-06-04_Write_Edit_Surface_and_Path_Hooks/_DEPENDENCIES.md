# Dependencies: DEL-06-04 Write/Edit Surface and Path Hooks

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-04-001, DEP-06-04-002, DEP-06-04-003, DEP-06-04-004, DEP-06-04-005, DEP-06-04-006, DEP-06-04-007, DEP-06-04-008, DEP-06-04-009, DEP-06-04-010

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-04-010` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture. External upstream edges
remain pending unless separately closed by their owning deliverables.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Anchor document selection: `Datasheet.md` and `Specification.md` traceability sections.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: available and used for package, deliverable, SOW, and objective target resolution.
- `[HISTORICAL WARNING] PRD_HASH_MISMATCH`: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-04-010` is now `SATISFIED`.
- `[WARNING] HUMAN_RULING_SEMANTIC_SKIPPED`: inherited `SatisfactionThreshold=SEMANTIC_READY` is not used as evidence in this extraction because semantic lensing was explicitly skipped.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-06-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `a677b46b8a6a2ebe6524ad7b0caaa0f28dd709a98e5c26f4f2e92ec19d02ae39`; `_CONTEXT.md` `db51716d0c118ca021d7101eb9acd09edf8cacfafb5f5585ec78c8bb217ad45f`; `_REFERENCES.md` `d19010786b798a334f71157f70888ca3538ffa74cad2f3b4b32b34eefda79d21`; `_STATUS.md` `67cd2f40d40aec52601c8a6f7453635979bf64ed4aacb18158693ab3469a098d`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `17077465dd485acc91e248afaf82254a4b842abcb0546f650a0565119e9905d1`, `_DEPENDENCIES.md` `6201e8f68c18e37f3e6bb862dbd9d0d02bbae9b0f0a5ae780ff9a1234b372975`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 9 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 9 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 6 |
| ACTIVE EXECUTION rows | 3 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-06-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-06 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-027 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-057 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-004 | ANCHOR | UPSTREAM | OTHER | SOW-060 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-005 | ANCHOR | UPSTREAM | OTHER | OBJ-005 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-006 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-007 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-06-01 | ACTIVE | PENDING |
| DEP-06-04-008 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-01 | ACTIVE | PENDING |
| DEP-06-04-009 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-06 | RETIRED | NOT_APPLICABLE |
| DEP-06-04-010 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | ACTIVE | SATISFIED |

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:47:30-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | Historical PRD_HASH_MISMATCH, later reconciled by D-APP-38 corpus v2; HUMAN_RULING_SEMANTIC_SKIPPED | ANCHOR=6; EXECUTION=4; TOTAL=10 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | none | ACTIVE=9 (ANCHOR=6; EXECUTION=3) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 9 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 7 |
| SatisfactionStatus | PENDING | 2 |
| SatisfactionStatus | SATISFIED | 1 |
| RequiredMaturity | ACCEPTED_DECOMPOSITION | 6 |
| RequiredMaturity | RECONCILED_REFERENCE_HASH | 1 |
| RequiredMaturity | TBD | 3 |
| DependencyClass | ANCHOR | 6 |
| DependencyClass | EXECUTION | 4 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | INTERFACE | 2 |
| DependencyType | OTHER | 6 |
| DependencyType | PREREQUISITE | 1 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App governed mutation routes and retained `frontend/src/lib/harness/tool-path-policy.ts`, write/edit hooks and tests. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=9, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
