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

Total rows: 9. ACTIVE: 9. RETIRED: 0.

| DependencyID | Class | Type | Direction | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-02-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-02 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-002 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-003 | ACTIVE | NOT_APPLICABLE |
| DEP-02-03-004 | EXECUTION | INTERFACE | UPSTREAM | REF-003 | ACTIVE | TBD |
| DEP-02-03-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-01 | ACTIVE | TBD |
| DEP-02-03-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-03 | ACTIVE | TBD |
| DEP-02-03-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-04 | ACTIVE | TBD |
| DEP-02-03-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-05 | ACTIVE | TBD |
| DEP-02-03-009 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-08-03 | ACTIVE | TBD |

This is a read-only summary of formal rows. D-GOV-43/D-APP-127 adapt current Runtime ownership and retire daemon proof subjects; formal row amendments, satisfaction changes and basis pins retain their owning process. Earlier notes below remain historical and do not override this current summary.

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

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:30:42-0600 | UPDATE | CONSERVATIVE | available: `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PRD_HASH_MISMATCH; PACKAGE_FOLDER_LABEL_MISMATCH; TARGET_RESOLUTION_MEDIUM | 9 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 3 |
| TBD | 6 |

## Current evidence-locator refresh — 2026-09-22

6 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
