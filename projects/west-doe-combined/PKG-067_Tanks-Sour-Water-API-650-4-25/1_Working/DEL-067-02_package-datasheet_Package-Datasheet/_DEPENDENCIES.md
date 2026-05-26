# Dependencies: DEL-067-02_package-datasheet — Package Datasheet

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

11 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-067-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-067 — Tanks Sour Water (API 650) 4-25 | HIGH | ACTIVE |
| DEP-067-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0225 | HIGH | ACTIVE |
| DEP-067-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0226 | HIGH | ACTIVE |
| DEP-067-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0227 | HIGH | ACTIVE |
| DEP-067-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0228 | HIGH | ACTIVE |
| DEP-067-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-067-01_scope-of-work | HIGH | ACTIVE |
| DEP-067-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-067-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-067-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-067-03_construction-work-package | HIGH | ACTIVE |
| DEP-067-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-067-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-067-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx heading 22 | HIGH | ACTIVE |
| DEP-067-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | INTERFACE_REGISTER for PKG-067 | HIGH | ACTIVE |

**ACTIVE count:** 11 (5 ANCHOR, 6 EXECUTION) | **RETIRED count:** 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (provided via DECOMP_PATH parameter; confirmed accessible)
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; found: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`; also read `_REFERENCES.md`. `Procedure.md` contained no additional dependency signals beyond those found in Datasheet/Guidance/Specification.
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match on filename containing "datasheet")
- **EXECUTION_DOC_ORDER:** `Guidance.md`, `Specification.md`, `Procedure.md` (heuristic: Guidance/Spec contain explicit execution flow signals)

**Integrity checks:**
- Parent anchor (IMPLEMENTS_NODE): 1 row — OK
- Tree x DAG: clean; no FLOATING_NODE, no AMBIGUOUS_ANCHOR warnings

**Source gaps recorded:**
- `26020-Package_Requirements.docx` (package heading 22) is referenced in PACKAGE_REGISTER row 94 and DELIVERABLE_REGISTER row 529 as an authoritative source but the binary `.docx` is not locally extracted; values that depend on it are marked TBD in source documents. Captured as DEP-067-02-010 with `SatisfactionStatus=PENDING`. A re-run after source extraction is recommended to integrate any additional requirements.
- `_References.md` confirms no deliverable-specific source slices were copied during PREPARATION beyond what is locally available.

**Naming conflict noted (not a dependency issue):** PACKAGE_REGISTER row 94 names the package "Tanks, Sour Water (API 650)" while equipment tags (TK-9010-1/TK-9020-1) use "Produced Water Storage Tank." Both refer to the same physical assets. Tracked in Guidance.md Conflict Table C-067-02-01 pending human ruling.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

**Closure state breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 3 |
| IN_PROGRESS | 1 |
| PENDING | 2 |
| TBD | 5 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run via dependency-extract skill (UPDATE, CONSERVATIVE). 11 rows written (5 ANCHOR, 6 EXECUTION). Schema v3.1. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). Source gap: 26020-Package_Requirements.docx binary not extracted. No floating node; no ambiguous anchor. Validation: VALID (11 rows).
