# Dependencies: DEL-08-05 Subagent Child Run Records and Artifacts

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-08-05-001`, `DEP-08-05-002`, `DEP-08-05-003`, `DEP-08-05-004`, `DEP-08-05-005`, `DEP-08-05-006`, `DEP-08-05-007`, `DEP-08-05-008`, `DEP-08-05-009`, `DEP-08-05-010`, `DEP-08-05-011`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

Extraction timestamp: 2026-08-24T00:54:53-0600

| Count Type | Value |
|---|---:|
| Total rows | 11 |
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ANCHOR rows | 3 |
| EXECUTION rows | 8 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 2 |

| DependencyID | Class | Type / Anchor | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-05-001 | ANCHOR | OTHER | UPSTREAM | SOW-063 | ACTIVE | SATISFIED |
| DEP-08-05-002 | ANCHOR | OTHER | UPSTREAM | OBJ-003 | ACTIVE | SATISFIED |
| DEP-08-05-003 | ANCHOR | OTHER | UPSTREAM | OBJ-007 | ACTIVE | SATISFIED |
| DEP-08-05-004 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-08-04 | ACTIVE | TBD |
| DEP-08-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | Runtime event schema and HarnessEvent | ACTIVE | TBD |
| DEP-08-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | Artifact storage policy | ACTIVE | SATISFIED |
| DEP-08-05-007 | EXECUTION | CONSTRAINT | UPSTREAM | Runtime redaction policy | ACTIVE | TBD |
| DEP-08-05-008 | EXECUTION | CONSTRAINT | UPSTREAM | SDK transcript metadata boundary | ACTIVE | TBD |
| DEP-08-05-009 | EXECUTION | CONSTRAINT | UPSTREAM | Retired unified pipeline run record boundary | ACTIVE | TBD |
| DEP-08-05-010 | EXECUTION | CONSTRAINT | UPSTREAM | D-APP-40 denied child-run allocation boundary | ACTIVE | SATISFIED |
| DEP-08-05-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-04 | ACTIVE | TBD |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run on 2026-05-20T20:55:00-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment were skipped.
- `ANCHOR_DOC=AUTO` selected `_CONTEXT.md` and `Datasheet.md` traceability fields for explicit identifiers.
- `EXECUTION_DOC_ORDER=AUTO` used `Procedure.md`, `Specification.md`, `Guidance.md`, and `Datasheet.md` for execution prerequisites and constraints.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor was found.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 current authority-corpus reconciliation supersedes the prior PRD source-state warning for this tranche.
- `[RESOLVED] HUMAN_RULING_APPLIED`: D-APP-40 resolves denied child-run allocation semantics; denied `ChildRunRecord` evidence is required only after the runtime reaches the child-run record layer.
- `[RESOLVED] CHILD_OUTPUT_ARTIFACT_EVIDENCE`: ADQ-12 persists over-inline child summaries under session child-output artifacts with parent-turn, task, child-run, tool-use, source-file, checksum, byte-count, truncation, and redaction evidence.
- Schema validation passed: 29 required columns and 10 data rows.
- TASK + dependency-extract semantic refresh on 2026-08-24T00:54:53-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`.
- Runtime declaration: `CHIRALITY_INSTRUCTION_ROOT=/Users/ryan/.codex/worktrees/ef5e/chirality`; the additive V2 declaration cured the earlier fail-closed normalization attempt without changing the sealed brief.
- Decomposition authority used: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SHA-256 `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md` v19, `ScopeOfWork.md`, existing dependency artifacts, and the exact applied decomposition. `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` were not dependency evidence.
- `ANCHOR_DOC=AUTO` selected `_CONTEXT.md` and the applied decomposition's explicit DEL-08-05/SOW-063/OBJ-003/OBJ-007 mappings. Pass 1 retained one parent anchor and two trace anchors with stable DependencyIDs.
- `EXECUTION_DOC_ORDER=AUTO` used `ScopeOfWork.md` followed by the applied decomposition's DEL-08-04 and DEL-08-05 carrier rows. Pass 2 retained seven supported execution edges and added one distinct class-aware interface edge.
- Descendant-class evidence is deliberately non-conflated: DEP-08-05-004 covers the Chirality-managed class exactly once; DEP-08-05-011 covers the delegated-harness-native class exactly once. Native descent assigns no Agent 0/1/2 role; managed sealed-brief evidence remains distinct.
- E-020 (`DEL-08-05` feedback to `DEL-08-04`) was not present in the allowed source documents or applied decomposition, so this conservative extraction did not surface or invent it. No schedule gate was created and no SCC was silently linearized.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor was found.
- `[WARNING] ID_FORMAT_VALIDATOR_PROJECT_CONVENTION`: `validate_id_format.sh` requires `DEL-[0-9]{3}-[0-9]{2}` and `PKG-[0-9]{3}`, so it rejects the accepted live project identifiers `DEL-08-05`, `DEL-08-04`, and `PKG-08`. The extraction preserves those decomposition-authoritative identifiers; no alternative IDs were invented.
- Schema validation passed: 29 required columns and 11 data rows.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-08-24T00:54:53-0600 | UPDATE | CONSERVATIVE | Exact post-application SHA-256 `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` | 11 | ID validator/project convention mismatch |
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, D-APP-40 child-run taxonomy, and child-output artifact evidence applied | 10 | none |
| 2026-06-21T03:00:20-0600 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 child-run taxonomy applied | 10 | none |
| 2026-05-20T20:55:00-0600 | UPDATE | CONSERVATIVE | Found and used explicit path | 10 | superseded source-state warning; superseded denied-allocation ruling request |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 11 |
| RequiredMaturity=SEMANTIC_READY | 11 |
| ProposedMaturity=SATISFIED | 1 |
| ProposedMaturity=SEMANTIC_READY | 4 |
| ProposedMaturity=TBD | 6 |
| SatisfactionStatus=SATISFIED | 5 |
| SatisfactionStatus=TBD | 6 |

## Downstream Handoff Notes

- Consumer context: `RECONCILIATION`.
- Consume DEP-08-05-004 and DEP-08-05-011 as distinct class-aware evidence flows; do not merge managed sealed-brief evidence with native-origin lineage evidence.
- The absent E-020 source signal remains non-gating and is not represented in this local register. A downstream graph consumer may preserve an independently governed E-020 edge only from its accepted source, without turning it into schedule authority.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-139
- **Current counts:** ACTIVE 10; RETIRED 0; SATISFIED=5; TBD=5.
- **Correction:** DEP-08-05-006 alone is newly SATISFIED; other documentary rows remain unchanged.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
