# Dependencies: DEL-03-03 Harness API and SSE Compatibility Adapter

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

Total rows: 11. ACTIVE: 10, RETIRED: 1.

| DependencyID | Class | Type | Direction | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-03-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-03 | ACTIVE | NOT_APPLICABLE |
| DEP-03-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-011 | ACTIVE | NOT_APPLICABLE |
| DEP-03-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-040 | ACTIVE | NOT_APPLICABLE |
| DEP-03-03-004 | ANCHOR | OTHER | UPSTREAM | OBJ-001 | ACTIVE | NOT_APPLICABLE |
| DEP-03-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE | NOT_APPLICABLE |
| DEP-03-03-006 | EXECUTION | INTERFACE | UPSTREAM | RUNTIME_ENGINE_CONTRACT_TURN_ENGINE | ACTIVE | TBD |
| DEP-03-03-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 | ACTIVE | TBD |
| DEP-03-03-008 | EXECUTION | INTERFACE | UPSTREAM | Session Audit Replay and Tool Result Records | ACTIVE | TBD |
| DEP-03-03-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-03 | RETIRED | NOT_APPLICABLE |
| DEP-03-03-010 | EXECUTION | PREREQUISITE | UPSTREAM | TBD | ACTIVE | TBD |
| DEP-03-03-011 | EXECUTION | INTERFACE | UPSTREAM | Current Runtime socket/API and extensible Codex event interface | ACTIVE | PENDING |

This is a read-only summary of formal rows. D-GOV-43/D-APP-127 adapt current Runtime ownership and retire daemon proof subjects; formal row amendments, satisfaction changes and basis pins retain their owning process. Earlier notes below remain historical and do not override this current summary.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Defaults used: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`, `EXECUTION_DOC_ORDER=AUTO` resolved to `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 current authority-corpus reconciliation supersedes the prior REF-006 source-state warning; PRD-derived route/SSE details are accepted for this tranche.
- `[WARNING] TBD_FIXTURE_CAPTURE`: current implementation fixture capture is an explicit prerequisite but its target location and baseline SHA remain `TBD`.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row is present.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-03-03-006` from a coarse deliverable edge into document-scoped TurnEngine boundary evidence; the row remains active and in objective.

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-03-03-011`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L305`; quote: "Keep /api/harness/* shapes and browser SSE event names stable while runtime policy moves behind services".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-06-21T03:00:20-06:00 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 runtime taxonomy applied | TBD_FIXTURE_CAPTURE | 10 |
| 2026-05-20T19:30:40-06:00 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used | superseded source-state warning; TBD_FIXTURE_CAPTURE | 10 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| PENDING | 1 |
| NOT_APPLICABLE | 6 |
| TBD | 4 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-116
- **Current counts:** ACTIVE 9; RETIRED 1; NOT_APPLICABLE=6; TBD=4.
- **Correction:** DEP-03-03-009 is RETIRED; the older active-row table is superseded.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=10; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
