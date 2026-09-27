# Dependencies: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

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
| Total rows | 10 |
| ACTIVE rows | 9 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 5 |
| ACTIVE EXECUTION rows | 4 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-03-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-03 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-012 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-015 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-004 | ANCHOR | UPSTREAM | OTHER | OBJ-002 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-005 | ANCHOR | UPSTREAM | OTHER | OBJ-003 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-006 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-03-01 | ACTIVE | TBD |
| DEP-03-04-007 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-03-02 | ACTIVE | TBD |
| DEP-03-04-008 | EXECUTION | UPSTREAM | INTERFACE | DEL-03-03 | RETIRED | NOT_APPLICABLE |
| DEP-03-04-009 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-05-02 | ACTIVE | TBD |
| DEP-03-04-010 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-03-04-CONFLICT-001 | ACTIVE | SATISFIED |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- This run used only `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Chosen anchor document: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields.
- Chosen execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for PKG, SOW, objective, and deliverable target labels.
- `[RESOLVED] AUTHORITY_CORPUS_APPLIED`: REF-006 is reconciled under the current D-APP-38 authority corpus.
- `[WARNING] ASSUMPTION_EDGES`: DEP-03-04-006 through DEP-03-04-009 are explicit in `Procedure.md` but assumption-labeled there; they remain `Confidence=LOW` and `SatisfactionStatus=TBD`.
- `[RESOLVED] HUMAN_RULING_APPLIED`: DEP-03-04-010 is satisfied by D-APP-40 Option B; explicit user interruption persists `turn.interrupted`, while `turn.cancelled` is reserved for non-user cancellation.
- Parent anchor check: PASS, exactly one ACTIVE `IMPLEMENTS_NODE` anchor.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-03-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `72eeb1284aea51ccc902fc4e0cb3b0359753b41e93251daa9c4f4686c17956da`; `_CONTEXT.md` `2bfcc0cd8a3e421ca2bb002e5f23db18f12168fe28d6b7727c8eb439e312a51c`; `_REFERENCES.md` `e37136d8916683878353cba85ae860b57769dcb9d8468b2e84160fb2ecd42e5d`; `_STATUS.md` `4f4befbd8dd872071c5444af8f9624f6fd32184b57de5eed4fc586e76d6bcc0c`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `16081bc19c7e6ca63a1980523f1c06a4dd98a2182d8d07e9e58eb7fe7b0119b1`, `_DEPENDENCIES.md` `ef2f5bb2ca8206fe17916d4d259583dc2f6a2815b4d67d0c43120815d2b238f5`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 9 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:35:54-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | superseded source-state warning; ASSUMPTION_EDGES; superseded human-ruling request | 10 |
| 2026-06-21T02:53:33-06:00 | ADQ-05 | CONSERVATIVE | `execution/_Coordination/_DECISIONS/D-APP-40_RULING_2026-06-21.md` | ASSUMPTION_EDGES; HUMAN_RULING_APPLIED | 10 |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | none | ACTIVE=9 (ANCHOR=5; EXECUTION=4) |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 9 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 6 |
| SatisfactionStatus | SATISFIED | 1 |
| SatisfactionStatus | TBD | 3 |
| RequiredMaturity | NOT_APPLICABLE | 5 |
| RequiredMaturity | SEMANTIC_READY | 1 |
| RequiredMaturity | TBD | 4 |
| DependencyClass | ANCHOR | 5 |
| DependencyClass | EXECUTION | 5 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 5 |
| DependencyType | PREREQUISITE | 3 |

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
