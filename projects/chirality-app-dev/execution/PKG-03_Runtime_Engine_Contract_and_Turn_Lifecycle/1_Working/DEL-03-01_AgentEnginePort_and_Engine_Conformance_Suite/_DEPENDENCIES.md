# Dependencies: DEL-03-01 AgentEnginePort and Engine Conformance Suite

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

Total rows: 9. ACTIVE: 8, RETIRED: 1.

| DependencyID | Class | Type | Direction | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-03-01-001 | ANCHOR | OTHER | UPSTREAM | SOW-037 | ACTIVE | SATISFIED |
| DEP-03-01-002 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE | SATISFIED |
| DEP-03-01-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | RETIRED | NOT_APPLICABLE |
| DEP-03-01-004 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | SATISFIED |
| DEP-03-01-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-03-SPEC-SCOPE | ACTIVE | PENDING |
| DEP-03-01-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 | RETIRED | NOT_APPLICABLE |
| DEP-03-01-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-01-02 | ACTIVE | PENDING |
| DEP-03-01-008 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 | ACTIVE | PENDING |
| DEP-03-01-009 | EXECUTION | INTERFACE | UPSTREAM | Runtime-owned Codex contracts and App-client conformance | ACTIVE | PENDING |

This is a read-only summary of formal rows. D-GOV-43/D-APP-127 adapt current Runtime ownership and retire daemon proof subjects; formal row amendments, satisfaction changes and basis pins retain their owning process. Earlier notes below remain historical and do not override this current summary.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used to validate target IDs and labels.
- Source selection: `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Specification.md, Procedure.md, Guidance.md`; `_CONTEXT.md`, `_REFERENCES.md`, and this file were used as local metadata inputs.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and was not used as evidence.
- Existing `Dependencies.csv` was absent before this run; a new v3.1 register was created.
- [RESOLVED] SOURCE_STATE: D-APP-38 current authority-corpus reconciliation supersedes the prior REF-006 source-state warning; PRD-derived runtime details are accepted for this tranche.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-03-01-005` from a coarse deliverable edge into document-scoped conformance/interface evidence; the row remains active and in objective.

## Extracted Dependency Register

`Dependencies.csv` v3.1 contains 8 ACTIVE rows.

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---:|---:|---:|---|---:|---:|
| DEP-03-01-001 | ANCHOR | OTHER | UPSTREAM | SOW-037 Product-owned engine contract | ACTIVE | SATISFIED |
| DEP-03-01-002 | ANCHOR | OTHER | UPSTREAM | OBJ-002 Runtime architecture objective | ACTIVE | SATISFIED |
| DEP-03-01-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | ACTIVE | PENDING |
| DEP-03-01-004 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | SATISFIED |
| DEP-03-01-005 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT DEL-03-03-SPEC-SCOPE Harness API/SSE compatibility adapter scope | ACTIVE | PENDING |
| DEP-03-01-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE | PENDING |
| DEP-03-01-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-01-02 Reliance Boundary Register | ACTIVE | PENDING |
| DEP-03-01-008 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE | PENDING |
| DEP-03-01-009 | EXECUTION | INTERFACE | UPSTREAM | Root-owned runtime contracts: API v2 and event schema v2 | ACTIVE | PENDING |

## Lifecycle Summary

| Measure | Count |
|---|---:|
| ACTIVE rows | 8 |
| RETIRED rows | 1 |
| ANCHOR rows | 2 |
| EXECUTION rows | 7 |
| SATISFIED rows | 3 |
| PENDING rows | 5 |
| TBD satisfaction rows | 0 |
| NOT_APPLICABLE rows (retired) | 1 |

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-03-01-009`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L303`; quote: "Verify the App client against Root-owned runtime contracts".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Count | Warnings |
|---|---|---|---|---:|---|
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | 8 | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh |
| 2026-06-21T03:00:20-0600 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 runtime taxonomy applied | 8 | none |
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | FOUND: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | 8 | superseded source-state warning |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-114
- **Current counts:** ACTIVE 7; RETIRED 1; NOT_APPLICABLE=1; PENDING=4; SATISFIED=3.
- **Correction:** DEP-03-01-006 is RETIRED; the older active-row table is superseded.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=8; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_0301_FALLBACK.csv`; current rows: ACTIVE=8, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_SCOPE_SEMANTIC_APPROVED.csv`; current rows: ACTIVE=7, RETIRED=2. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
