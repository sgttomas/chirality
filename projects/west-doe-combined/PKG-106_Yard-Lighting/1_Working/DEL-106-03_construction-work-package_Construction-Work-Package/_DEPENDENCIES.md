# Dependencies: DEL-106-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Produced by `TASK + dependency-extract` run on 2026-05-26.

**Total rows:** 6 | **ACTIVE:** 6 | **RETIRED:** 0

| DependencyID | Class | AnchorType | Direction | Type | TargetType | Target | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-106-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-106 Yard Lighting | HIGH | ACTIVE |
| DEP-106-03-002 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-01_scope-of-work | HIGH | ACTIVE |
| DEP-106-03-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-02_package-datasheet | HIGH | ACTIVE |
| DEP-106-03-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-106-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-106-03-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-106-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-106-03-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-106-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

---

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned (AUTO):** Procedure.md (primary execution doc), Guidance.md, Specification.md, Datasheet.md
- **ANCHOR_DOC:** Datasheet.md (contains Identification section with ParentPackageID — highest-confidence anchor signal)
- **EXECUTION_DOC_ORDER:** Procedure.md (first — explicit prerequisites listed), Specification.md (R-5 handover), Guidance.md (supporting)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - Validated PKG-106, DEL-106-01..06 against DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv.
- **DECOMPOSITION_PATH parameter provided:** `GATE-07_Final_Published_2026-05-24/` was provided but pointed to a non-existent direct path. Resolved to the correct path under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. Recorded.
- **Missing source slices:** Deliverable-local source slices for DBM-Deepcut SEC-11/12/14/15 and Workbook Packages row 12 detail are not deliverable-local per `_REFERENCES.md`. No additional execution edges could be extracted from these sources.
- **Pass 1 (ANCHOR):** One parent anchor emitted (DEP-106-03-001, IMPLEMENTS_NODE to PKG-106). No requirement trace anchors emitted — no explicit requirement IDs mapped in source documents with `CONSERVATIVE` strictness.
- **Pass 2 (EXECUTION):** Four upstream edges and one downstream edge emitted. All grounded in explicit statements in Procedure.md and Specification.md.
- **Tree x DAG integrity:** Parent anchor count = 1 (DEP-106-03-001). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 6 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — UPDATE run via `TASK + dependency-extract`. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. 6 rows extracted (1 ANCHOR, 5 EXECUTION). All ACTIVE. Schema VALID (29 columns). All enums validated.
