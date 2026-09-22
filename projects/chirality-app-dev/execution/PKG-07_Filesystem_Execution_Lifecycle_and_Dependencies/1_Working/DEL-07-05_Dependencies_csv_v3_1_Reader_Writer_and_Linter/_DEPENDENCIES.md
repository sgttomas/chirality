# Dependencies: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-05-001`, `DEP-07-05-002`, `DEP-07-05-003`, `DEP-07-05-004`, `DEP-07-05-005`, `DEP-07-05-006`, `DEP-07-05-007`, `DEP-07-05-008`, `DEP-07-05-009`, `DEP-07-05-010`, `DEP-07-05-011`, `DEP-07-05-012`, `DEP-07-05-013`, `DEP-07-05-014`, `DEP-07-05-015`, `DEP-07-05-016`, `DEP-07-05-017`, `DEP-07-05-018`, `DEP-07-05-019`, `DEP-07-05-020`, `DEP-07-05-021`, `DEP-07-05-022`, `DEP-07-05-023`, `DEP-07-05-024`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-07-05-025`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

`Dependencies.csv` was created with 26 ACTIVE extracted rows.

| Count Type | Count |
|---|---:|
| Total rows | 26 |
| ACTIVE rows | 25 |
| RETIRED rows | 1 |
| ANCHOR rows | 20 |
| EXECUTION rows | 6 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Requirement/objective trace anchors | 19 |

### Counts by Dependency Type

| DependencyType | Count |
|---|---:|
| OTHER | 20 |
| PREREQUISITE | 3 |
| CONSTRAINT | 2 |
| INTERFACE | 1 |

### Counts by Status

| Status | Count |
|---|---:|
| ACTIVE | 25 |
| RETIRED | 1 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEP-07-05-001 | ANCHOR | UPSTREAM | OTHER | SOW-029 Dependencies CSV v3.1 | ACTIVE |
| DEP-07-05-002 | ANCHOR | UPSTREAM | OTHER | OBJ-006 Filesystem governance objective | ACTIVE |
| DEP-07-05-003 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-001 | ACTIVE |
| DEP-07-05-004 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-002 | ACTIVE |
| DEP-07-05-005 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-003 | ACTIVE |
| DEP-07-05-006 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-004 | ACTIVE |
| DEP-07-05-007 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-005 | ACTIVE |
| DEP-07-05-008 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-006 | ACTIVE |
| DEP-07-05-009 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-007 | ACTIVE |
| DEP-07-05-010 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-008 | ACTIVE |
| DEP-07-05-011 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-009 | ACTIVE |
| DEP-07-05-012 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-010 | ACTIVE |
| DEP-07-05-013 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-011 | ACTIVE |
| DEP-07-05-014 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-012 | ACTIVE |
| DEP-07-05-015 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-013 | ACTIVE |
| DEP-07-05-016 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-014 | ACTIVE |
| DEP-07-05-017 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-015 | ACTIVE |
| DEP-07-05-018 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-016 | ACTIVE |
| DEP-07-05-019 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-017 | ACTIVE |
| DEP-07-05-020 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-018 | ACTIVE |
| DEP-07-05-021 | EXECUTION | UPSTREAM | PREREQUISITE | Accepted source references | ACTIVE |
| DEP-07-05-022 | EXECUTION | UPSTREAM | PREREQUISITE | v3.1 schema and enum vocabulary | ACTIVE |
| DEP-07-05-023 | EXECUTION | UPSTREAM | PREREQUISITE | Dependency authority model | ACTIVE |
| DEP-07-05-024 | EXECUTION | UPSTREAM | CONSTRAINT | Working-root write policy | ACTIVE |
| DEP-07-05-025 | EXECUTION | DOWNSTREAM | INTERFACE | Dependency API and MCP contract surfaces | ACTIVE |
| DEP-07-05-026 | EXECUTION | UPSTREAM | CONSTRAINT | docs/PRD.md reference state MATCH | RETIRED |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK run `TASK_RUN_2026-05-20_1954.md` used `TaskSkill=dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source document selection: `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Specification.md, Guidance.md, Procedure.md`; `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md` were used for identity, reference, and declared-edge context.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was invalid evidence and was not read or consumed.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row was found for `SOW-029`.
- No declared rows were present to preserve or merge. All rows in this run are extracted rows.
- [WARNING] OBJECTIVE_TARGET_TYPE_UNAVAILABLE: `OBJ-006` is explicit evidence, but the v3.1 `TargetType` enum has no `OBJECTIVE`; the row preserves `TargetType=UNKNOWN`.
- [WARNING] UNKNOWN_INTERFACE_CONSUMER: the API/MCP dependency surface is explicit, but no consumer deliverable ID is explicitly named in the evidence; the row preserves `TargetType=UNKNOWN`.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20 19:54 | UPDATE | CONSERVATIVE | Found v3.2 decomposition authority | OBJECTIVE_TARGET_TYPE_UNAVAILABLE; UNKNOWN_INTERFACE_CONSUMER; SOURCE_HASH_MISMATCH | 26 |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 25 |
| RETIRED | 1 |
| RequiredMaturity=SEMANTIC_READY | 26 |
| ProposedMaturity=TBD | 26 |
| SatisfactionStatus=NOT_APPLICABLE | 1 |
| SatisfactionStatus=TBD | 25 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

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

## Current residual-specific interpretation — 2026-09-22

DEP-001..025 four-document EvidenceFile/SourceRef values preserve historical source quotations; ScopeOfWork.md is the current claim carrier. OBJECTIVE_TARGET_TYPE_UNAVAILABLE is a dated extraction warning, not a new current discovery: DEP-002 remains UNKNOWN in the unchanged formal register. Any decision to reclassify that formal target remains with its owning dependency pass.

## Current evidence-locator refresh — 2026-09-22

24 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
