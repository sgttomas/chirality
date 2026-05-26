# Dependencies: DEL-106-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE mode)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-26. Schema version v3.1. **10 rows total; 10 ACTIVE; 0 RETIRED.**

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-106-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0011 | Scope decision SOW-0011 — Yard Lighting | HIGH | ACTIVE |
| DEP-106-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | HIGH | ACTIVE |
| DEP-106-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-106-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-106-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | MEDIUM | ACTIVE |
| DEP-106-05-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-106-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-01_scope-of-work_Scope-of-Work | Scope of Work (DEL-106-01) | HIGH | ACTIVE |
| DEP-106-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-02_package-datasheet_Package-Datasheet | Package Datasheet (DEL-106-02) | HIGH | ACTIVE |
| DEP-106-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-04_vendor-engineered-equipment-package_Vendor-Engineered-Equipment-Package | Vendor Engineered Equipment Package (DEL-106-04) | HIGH | ACTIVE |
| DEP-106-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-106-06_epc-vendor-package-review-and-acceptance_EPC-Vendor-Package-Review-and-Acceptance | EPC Vendor Package Review and Acceptance (DEL-106-06) | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |
| **Total** | **10** |

**By DependencyClass:**

| Class | ACTIVE | RETIRED |
|---|---|---|
| ANCHOR | 6 | 0 |
| EXECUTION | 4 | 0 |

**By SatisfactionStatus:** All 10 rows: TBD (initial extraction; closure not yet assessed).

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents processed: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md`, `Guidance.md` (EXECUTION_DOC_ORDER)
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match: contains identification fields with explicit scope item and objective references)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchor IDs and resolve canonical labels. Decomposition files read: `SCOPE_LEDGER.csv`, `DELIVERABLE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `PACKAGE_REGISTER.csv`.
- **`_REFERENCES.md`:** Read; used to confirm decomposition path and source material pointers. No deliverable-specific source slices present; no `TargetType=DOCUMENT` rows emitted.
- **Parent anchor:** 1 IMPLEMENTS_NODE row (DEP-106-05-001 → SOW-0011). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Objective trace anchors:** 5 TRACES_TO_REQUIREMENT rows (OBJ-001 through OBJ-010 per DELIVERABLE_REGISTER). Objective association in Datasheet.md carries ASSUMPTION flag (package-grouping heuristic); flag preserved in Notes column of each row.
- **EXECUTION edges:** 3 UPSTREAM PREREQUISITE (DEL-106-01, DEL-106-02, DEL-106-04) and 1 DOWNSTREAM HANDOVER (DEL-106-06). All sourced from explicit statements in Procedure.md (Prerequisites section and Step 7) and corroborated by Specification.md.
- **Confidence note:** DEP-106-05-005 (OBJ-009) set to MEDIUM — Yard Lighting is an electrical support package; OBJ-009 safety/sour-service linkage is less direct for this deliverable type. All other rows HIGH.
- **No rows omitted** for coordination-only or structural adjacency — all 4 EXECUTION edges represent explicit information/artifact transfer stated in source documents.
- **Vendor-document source gap:** ART-182773E33C flags the vendor document register for PKG-106 as TBD with Vendor Documentation Gap Evidence. No dependency rows were fabricated from this gap; the gap is noted in source documents only.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run via `dependency-extract` skill (UPDATE / CONSERVATIVE). 10 rows written (6 ANCHOR + 4 EXECUTION). No prior Dependencies.csv existed; created fresh. Decomposition: GATE-07_Final_Published_2026-05-24. No warnings.
