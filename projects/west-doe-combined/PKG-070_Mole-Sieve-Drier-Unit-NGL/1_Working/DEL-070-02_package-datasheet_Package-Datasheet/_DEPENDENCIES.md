# Dependencies: DEL-070-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 generated)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Extraction run: 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-070-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-070 | Mole Sieve Drier Unit (NGL) | HIGH | ACTIVE |
| DEP-070-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0145 | SOW-0145 | HIGH | ACTIVE |
| DEP-070-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0146 | SOW-0146 | HIGH | ACTIVE |
| DEP-070-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0147 | SOW-0147 | HIGH | ACTIVE |
| DEP-070-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0148 | SOW-0148 | HIGH | ACTIVE |
| DEP-070-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-070-01_scope-of-work | Scope of Work (PKG-070) | HIGH | ACTIVE |
| DEP-070-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-DECOMP | GATE-07 PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-070-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-DEEPCUT | DBM-Deepcut 4-25_Deepcut_DBM.md §1574-1623 | HIGH | ACTIVE |
| DEP-070-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-070-03_construction-work-package | Construction Work Package (PKG-070) | HIGH | ACTIVE |
| DEP-070-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-070-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (PKG-070) | HIGH | ACTIVE |
| DEP-070-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-070-05_vendor-document-turnover-package | Vendor Document Turnover Package (PKG-070) | MEDIUM | ACTIVE |
| DEP-070-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-070-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (PKG-070) | HIGH | ACTIVE |

**Total ACTIVE rows:** 12 (5 ANCHOR, 7 EXECUTION) | **RETIRED rows:** 0

---

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`
- **ANCHOR_DOC (AUTO):** `Datasheet.md` (contains explicit identification, ParentPackageID, SOW coverage fields)
- **EXECUTION_DOC_ORDER (AUTO):** `Specification.md`, `Procedure.md`, `Guidance.md`, `Datasheet.md`
- **Decomposition path:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — path verified to exist at runtime
- **DECOMPOSITION_PATH parameter:** The invoking task specified `GATE-07_Final_Published_2026-05-24/` as a relative fragment; the actual path `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` was resolved by discovering the snapshot under `_Decomposition/`. No warning required — snapshot confirmed present.
- **No prior `Dependencies.csv` existed** — new file created (UPDATE mode without prior file is equivalent to initial extraction).
- **Tree x DAG integrity:** Parent anchor count = 1 (DEP-070-02-001, IMPLEMENTS_NODE on PKG-070). No FLOATING_NODE, no AMBIGUOUS_ANCHOR.
- **Notes on inaccessible sources:** `_Sources/26020-Package_Requirements.docx` heading 24 and `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 74 are binary files with no text extraction available. No dependency rows were generated from these sources; their content remains `location TBD`. This is consistent with CONSERVATIVE strictness.
- **Objective anchors not emitted:** DEL-070-02 supports OBJ-001, OBJ-003 through OBJ-010 per `_CONTEXT.md`. Under CONSERVATIVE strictness, objective-level trace anchors were not emitted because the decomposition OBJECTIVE_DELIVERABLE_MAP provides this linkage at the project level; emitting them here would duplicate project-level graph structure without adding deliverable-local evidence. This decision is logged here for transparency; they may be added under AGGRESSIVE strictness on a future refresh run.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: GATE-07 snapshot confirmed. 12 ACTIVE rows written (5 ANCHOR, 7 EXECUTION). No rows RETIRED. Schema validation: VALID. No integrity warnings.
