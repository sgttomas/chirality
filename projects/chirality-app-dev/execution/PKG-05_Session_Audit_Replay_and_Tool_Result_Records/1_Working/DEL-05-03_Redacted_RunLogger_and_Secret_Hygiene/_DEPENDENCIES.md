# Dependencies: DEL-05-03 Redacted RunLogger and Secret Hygiene

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-03-001, DEP-05-03-002, DEP-05-03-003, DEP-05-03-004, DEP-05-03-005, DEP-05-03-006, DEP-05-03-007, DEP-05-03-008, DEP-05-03-009, DEP-05-03-010, DEP-05-03-011, DEP-05-03-013, DEP-05-03-014

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-03-012

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK dependency-extract run on 2026-05-20 used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for anchor and target resolution.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] UNKNOWN_TBD_RETAINED`: final redaction helper path, run logger path, configured-secret schema, replacement token, and exact policy integration point remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor is present.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-05-03`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `2781a4e54f4bd596e48301ad99b4dca5ff80b95d306191294e38d14520135b7b`; `_CONTEXT.md` `e521c70c84cc1401e390307c9e7723b78c6b94bcbbdb9bdae1df0b91a071d95e`; `_REFERENCES.md` `107e315090988207d830d653e26ebdb153636c3b40c324cab96e177efdff4a43`; `_STATUS.md` `3423e90ee4fd9c34e52dac5b44d3e0eb77e8a116b6b803ab2e65b92a8ae14092`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `e90c3a0cf969efff3cc36d2cf8324bf092407119999cf92c4737bc77b46453a9`, `_DEPENDENCIES.md` `40e9c8e407aae6627d789f9bb2efe6390ca152ffb0641575c1ea3f27a8d748ce`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-22; the 2026-09-23 retired-status clauses are the text added since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 13 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- New text scanned: APP-R045 in the 2026-09-23 retired status detail names no other deliverable. The retired `_STATUS.md` `## Remaining` section was cited by no row of this register.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 13 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 5 |
| ACTIVE EXECUTION rows | 8 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-05-03-001 | ANCHOR | UPSTREAM | OTHER | PKG-05 | ACTIVE | SATISFIED |
| DEP-05-03-002 | ANCHOR | UPSTREAM | OTHER | SOW-021 | ACTIVE | SATISFIED |
| DEP-05-03-003 | ANCHOR | UPSTREAM | OTHER | SOW-041 | ACTIVE | SATISFIED |
| DEP-05-03-004 | ANCHOR | UPSTREAM | OTHER | OBJ-003 | ACTIVE | SATISFIED |
| DEP-05-03-005 | ANCHOR | UPSTREAM | OTHER | OBJ-008 | ACTIVE | SATISFIED |
| DEP-05-03-006 | EXECUTION | UPSTREAM | PREREQUISITE | REF-002 | ACTIVE | SATISFIED |
| DEP-05-03-007 | EXECUTION | UPSTREAM | PREREQUISITE | REF-003 | ACTIVE | SATISFIED |
| DEP-05-03-008 | EXECUTION | UPSTREAM | PREREQUISITE | REF-005 | ACTIVE | SATISFIED |
| DEP-05-03-009 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | ACTIVE | SATISFIED |
| DEP-05-03-010 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-05 | ACTIVE | PENDING |
| DEP-05-03-011 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-02 | RETIRED | NOT_APPLICABLE |
| DEP-05-03-012 | EXECUTION | DOWNSTREAM | CONSTRAINT | DEL-05-05 | ACTIVE | PENDING |
| DEP-05-03-013 | EXECUTION | UPSTREAM | CONSTRAINT | TBD | ACTIVE | PENDING |
| DEP-05-03-014 | EXECUTION | UPSTREAM | INTERFACE | Runtime-owned operational event, diagnostic and artifact sin… | ACTIVE | PENDING |

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-05-03-014`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L324`; quote: "verify that Root-runtime operational records exclude credentials and secrets".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | REF-006_HASH_MISMATCH; UNKNOWN_TBD_RETAINED | 13 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | 13 |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | none | ACTIVE=13 (ANCHOR=5; EXECUTION=8) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 13 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 1 |
| SatisfactionStatus | PENDING | 4 |
| SatisfactionStatus | SATISFIED | 9 |
| RequiredMaturity | SEMANTIC_READY | 14 |
| DependencyClass | ANCHOR | 5 |
| DependencyClass | EXECUTION | 9 |
| DependencyType | CONSTRAINT | 3 |
| DependencyType | INTERFACE | 3 |
| DependencyType | OTHER | 5 |
| DependencyType | PREREQUISITE | 3 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-126
- **Current counts:** ACTIVE 12; RETIRED 1; NOT_APPLICABLE=1; PENDING=3; SATISFIED=9.
- **Correction:** DEP-05-03-011 is RETIRED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=13; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=13, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_04_06_SUPPORTED_APPROVED.csv`; current rows: ACTIVE=13, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SEMANTIC_19_PREVIEW.csv`; current rows: ACTIVE=13, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
