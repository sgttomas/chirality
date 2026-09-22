# Dependencies: DEL-01-02 Reliance Boundary Register

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See `Dependencies.csv` for the derivative dependency-extract register. No dependency row is satisfied
by this documentation reconciliation.

## Declared Downstream

See `Dependencies.csv` for downstream `ENABLES` rows. They remain derivative dependency evidence, not
closure approval.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run `TASK_RUN_DEL-01-02_2026-05-20_1924` executed in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source-document defaults: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md` with `_CONTEXT.md` traceability support, `EXECUTION_DOC_ORDER=Procedure.md, Specification.md, Guidance.md, Datasheet.md`.
- Decomposition authority: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for package, SOW, and deliverable target validation.
- Human ruling applied: semantic lensing and P3 enrichment are skipped. `_SEMANTIC.md` is invalid evidence and was not read or consumed for dependency extraction.
- Human ruling applied: read set limited to `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_STATUS.md` was not read for this extraction run.
- Objective traceability (`OBJ-002`, `OBJ-005`, `OBJ-009`) was preserved in notes but not emitted as dependency rows because the v3.1 schema has no objective target type and the conservative row rules avoid coercing objective IDs into requirement rows.
- `[RECONCILED] REF-006`: D-APP-38 corpus `v1` reconciled `docs/PRD.md`; `_REFERENCES.md` now reports `MATCH`. PRD-derived rows remain active until dependency/evidence disposition, but they are no longer blocked by a PRD hash mismatch.
- `[WARNING] OPEN_BLOCKERS`: exact implementation surfaces, SDK transcript placement, and final Section 9 validation file/test names remain `TBD` in the source documents.
- `[WARNING] ID_FORMAT_VALIDATOR_PATTERN_MISMATCH`: `tools/validation/validate_id_format.sh` rejects accepted v3.2 IDs such as `PKG-01`, `DEL-01-02`, and `SOW-037` because its patterns expect three-digit package/deliverable and four-digit SOW formats. Authoritative IDs were preserved from the decomposition instead of rewritten to match the helper.
- 2026-07-10 (D-APP-53 reconciliation): all 24 open rows re-verified against the live tree and moved `TBD -> SATISFIED` under `PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md` (DRQ-01). Anchor targets confirmed in decomposition v3.2; REF-001..REF-007 MATCH re-verified by live SHA-256 recompute; downstream `ENABLES` targets confirmed via `docs/harness/reliance_boundary_register.md` enforcement matrix plus live enforcement-surface files and implemented Section 9 IDs. `DEP-01-02-018` `TargetLocation` literal corrected (`Append-Only` -> `Append_Only`) to match the real directory. See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. This is derivative evidence only; no lifecycle transition and no issuance.
- 2026-07-10 correction note (D-APP-53 reconciliation): the 2026-05-20 `[WARNING] OPEN_BLOCKERS` is stale for enforcement surfaces and Section 9 IDs — concrete surfaces now exist (e.g. `frontend/src/lib/harness/*`) and implemented Section 9 IDs are listed in `frontend/scripts/validate-harness-section9.mjs`; the original warning text is retained above as history.

## Extracted Dependency Register

Structured register: `Dependencies.csv` (`v3.1`)

| Class | Direction | Type | Status | Count |
|---|---:|---|---|---:|
| ANCHOR | UPSTREAM | OTHER | ACTIVE | 6 |
| EXECUTION | UPSTREAM | PREREQUISITE | ACTIVE | 7 |
| EXECUTION | DOWNSTREAM | ENABLES | ACTIVE | 11 |

### Compact Register View

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEP-01-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 | ACTIVE | SATISFIED |
| DEP-01-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-037 | ACTIVE | SATISFIED |
| DEP-01-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-045 | ACTIVE | SATISFIED |
| DEP-01-02-004 | ANCHOR | OTHER | UPSTREAM | SOW-054 | ACTIVE | SATISFIED |
| DEP-01-02-005 | ANCHOR | OTHER | UPSTREAM | SOW-057 | ACTIVE | SATISFIED |
| DEP-01-02-006 | ANCHOR | OTHER | UPSTREAM | SOW-074 | ACTIVE | SATISFIED |
| DEP-01-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 | ACTIVE | SATISFIED |
| DEP-01-02-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | SATISFIED |
| DEP-01-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | SATISFIED |
| DEP-01-02-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | SATISFIED |
| DEP-01-02-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 | ACTIVE | SATISFIED |
| DEP-01-02-012 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 | ACTIVE | SATISFIED |
| DEP-01-02-013 | EXECUTION | PREREQUISITE | UPSTREAM | REF-007 | ACTIVE | SATISFIED |
| DEP-01-02-014 | EXECUTION | ENABLES | DOWNSTREAM | DEL-03-01 | ACTIVE | SATISFIED |
| DEP-01-02-015 | EXECUTION | ENABLES | DOWNSTREAM | DEL-03-02 | ACTIVE | SATISFIED |
| DEP-01-02-016 | EXECUTION | ENABLES | DOWNSTREAM | DEL-04-02 | ACTIVE | SATISFIED |
| DEP-01-02-017 | EXECUTION | ENABLES | DOWNSTREAM | DEL-05-01 | ACTIVE | SATISFIED |
| DEP-01-02-018 | EXECUTION | ENABLES | DOWNSTREAM | DEL-05-02 | ACTIVE | SATISFIED |
| DEP-01-02-019 | EXECUTION | ENABLES | DOWNSTREAM | DEL-05-04 | ACTIVE | SATISFIED |
| DEP-01-02-020 | EXECUTION | ENABLES | DOWNSTREAM | DEL-06-01 | ACTIVE | SATISFIED |
| DEP-01-02-021 | EXECUTION | ENABLES | DOWNSTREAM | DEL-06-04 | ACTIVE | SATISFIED |
| DEP-01-02-022 | EXECUTION | ENABLES | DOWNSTREAM | DEL-06-06 | ACTIVE | SATISFIED |
| DEP-01-02-023 | EXECUTION | ENABLES | DOWNSTREAM | DEL-08-04 | ACTIVE | SATISFIED |
| DEP-01-02-024 | EXECUTION | ENABLES | DOWNSTREAM | DEL-09-02 | ACTIVE | SATISFIED |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 24 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 24 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | Active Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:24:25-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (found) | SOURCE_HASH_MISMATCH at extraction time; later reconciled by D-APP-38 corpus `v1`; OPEN_BLOCKERS; ID_FORMAT_VALIDATOR_PATTERN_MISMATCH | 24 |
| 2026-07-10 (D-APP-53 reconciliation) | RECONCILE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (re-verified) | none; `validate_dependencies.py` PASS (24 rows, 0 errors, 0 warnings) | 24 |

## Current Source Migration Annotation

2026-07-19 — D-GOV-16/D-APP-68: the four-document source names above describe
the 2026-05-20 extraction and remain historical. Current live evidence pointers
are maintained in `Dependencies.csv` against consolidated `ScopeOfWork.md` CLM
anchors. This migration changed no dependency identity, status, satisfaction,
or lifecycle meaning.

## Current Reliance Annotation (2026-09-22)

D-APP-53 results and earlier MATCH notes above are dated evidence, not a fresh verification of changed source bytes. Formal row identity, status, satisfaction and accepted basis remain unchanged. Current source support is rechecked under D-APP-38; D-GOV-43/D-APP-127 governs current Codex/runtime/settings/policy applicability. REF-007 now names `workflows/software-decomp/WORKFLOW.md`; the descriptive locator now agrees with REF-007; formal edge identity, status and satisfaction remain unchanged.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=24; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
