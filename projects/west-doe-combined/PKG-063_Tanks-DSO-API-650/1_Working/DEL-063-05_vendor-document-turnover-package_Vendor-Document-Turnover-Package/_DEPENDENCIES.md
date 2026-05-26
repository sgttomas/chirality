# Dependencies: DEL-063-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv generated; this file is the human-readable view)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract` (UPDATE mode, CONSERVATIVE strictness).

**Total rows:** 9 (all ACTIVE)

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-063-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-063 — Tanks DSO (API 650) | HIGH | ACTIVE |
| DEP-063-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0209 | HIGH | ACTIVE |
| DEP-063-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0210 | HIGH | ACTIVE |
| DEP-063-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0211 | HIGH | ACTIVE |
| DEP-063-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0212 | HIGH | ACTIVE |
| DEP-063-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | Scope of Work (DEL-063-01) | HIGH | ACTIVE |
| DEP-063-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | Package Datasheet (DEL-063-02) | HIGH | ACTIVE |
| DEP-063-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | Vendor Engineered Equipment Package (DEL-063-04) | HIGH | ACTIVE |
| DEP-063-05-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | EPC Vendor Package Review and Acceptance (DEL-063-06) | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 9 |

ANCHOR rows: 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
EXECUTION rows: 4 (3 UPSTREAM PREREQUISITE + 1 DOWNSTREAM HANDOVER)

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Specification.md, Procedure.md, Guidance.md
- **ANCHOR_DOC (AUTO):** Datasheet.md — matched on `datasheet` filename heuristic; contains explicit DeliverableID, ParentPackageID, DecompositionRow, and SOW coverage fields.
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (primary — contains explicit Prerequisites table and Steps), Specification.md (R-03/R-06 cross-confirms), Guidance.md (downstream consumer note)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** PRESENT — DELIVERABLE_REGISTER.csv row 508 confirmed; PKG-063 PACKAGE_REGISTER.csv row 90 confirmed. Parent anchor validated against decomposition.
- **_REFERENCES.md:** Read. No deliverable-specific source slices copied locally; heading-18 source slice (26020-Package_Requirements.docx) not accessible as text. No DOCUMENT-type dependency rows emitted for inaccessible binaries (conservative per STRICTNESS).
- **Existing Dependencies.csv:** None — created fresh.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row (DEP-063-05-001 → PKG-063). No AMBIGUOUS_ANCHOR. No FLOATING_NODE.
- **Objectives not registered as dependency rows:** OBJ-001; OBJ-003..OBJ-010 are listed in DELIVERABLE_REGISTER row 508 as supported objectives. These are not emitted as TRACES_TO_REQUIREMENT rows because the source documents reference only SOW items (SOW-0209..0212) as traceable requirements against this deliverable — objectives are captured at the package/decomposition level and not explicitly framed as requirement trace targets in the deliverable's source documents. CONSERVATIVE posture: no objective trace rows emitted.
- **26020-Package_Requirements.docx heading 18:** Binary; not accessible. No DOCUMENT dependency rows emitted for this source. If a text slice becomes accessible, a refresh run may emit a PREREQUISITE row for heading-18 resolution.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition GATE-07_Final_Published_2026-05-24 present and validated. 9 rows extracted (5 ANCHOR + 4 EXECUTION), all ACTIVE. Schema validation: VALID (29 columns, 9 data rows).
