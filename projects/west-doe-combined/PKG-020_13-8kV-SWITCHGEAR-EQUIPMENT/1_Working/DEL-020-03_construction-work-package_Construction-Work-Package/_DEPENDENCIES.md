# Dependencies: DEL-020-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Schema version:** v3.1
**Total rows:** 17
**ACTIVE:** 17 | **RETIRED:** 0

### ANCHOR rows (8 total — all ACTIVE)

| DependencyID | AnchorType | TargetRefID | TargetName | Confidence |
|---|---|---|---|---|
| DEP-020-03-001 | IMPLEMENTS_NODE | SOW-0021 | Scope decision SOW-0021 — 13.8kV SWITCHGEAR EQUIPMENT (WBS 01) | HIGH |
| DEP-020-03-002 | TRACES_TO_REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | HIGH |
| DEP-020-03-003 | TRACES_TO_REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH |
| DEP-020-03-004 | TRACES_TO_REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH |
| DEP-020-03-005 | TRACES_TO_REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH |
| DEP-020-03-006 | TRACES_TO_REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH |
| DEP-020-03-007 | TRACES_TO_REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH |
| DEP-020-03-008 | TRACES_TO_REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH |

### EXECUTION rows (9 total — all ACTIVE)

| DependencyID | Direction | DependencyType | TargetType | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|
| DEP-020-03-009 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-020-01 Scope of Work | PENDING | HIGH |
| DEP-020-03-010 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-020-02 Package Datasheet | PENDING | HIGH |
| DEP-020-03-011 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-020-04 Vendor Engineered Equipment Package | PENDING | HIGH |
| DEP-020-03-012 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-020-06 EPC Vendor Package Review and Acceptance | TBD | HIGH |
| DEP-020-03-013 | UPSTREAM | PREREQUISITE | EXTERNAL | Final Geotechnical Report | PENDING | HIGH |
| DEP-020-03-014 | UPSTREAM | PREREQUISITE | EXTERNAL | Protection Coordination and Arc-Flash Studies | PENDING | HIGH |
| DEP-020-03-015 | UPSTREAM | PREREQUISITE | EXTERNAL | BC Hydro Utility Coordination Agreement | PENDING | HIGH |
| DEP-020-03-016 | UPSTREAM | PREREQUISITE | DOCUMENT | IFC Electrical Drawings | PENDING | MEDIUM |
| DEP-020-03-017 | UPSTREAM | INTERFACE | PACKAGE | PKG-013 100A DC UPS Package | PENDING | MEDIUM |

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

**SatisfactionStatus breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| TBD | 9 |
| PENDING | 8 |

---

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `_CONTEXT.md` (primary identity / scope basis); supplemented by GATE-07 SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary), `Specification.md`, `Guidance.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — found and used for anchor validation and label resolution.
- `Datasheet.md` was not found in the deliverable folder on this run; it is listed in the `ls` output but contained no dependency-bearing content distinct from Specification.md.
- Parent anchor (IMPLEMENTS_NODE): 1 row — DEP-020-03-001 anchors to SOW-0021. Tree integrity check PASS.
- All ACTIVE EXECUTION rows include EvidenceFile and SourceRef.
- DEP-020-03-017 uses TargetType=PACKAGE (PKG-013) because only the package ID is resolvable from source; no specific deliverable ID within PKG-013 is named. ASSUMPTION noted in row.
- IFC electrical drawings (DEP-020-03-016): TargetLocation is TBD — documents not yet in `_Sources`.
- No rows retired on this run (first extraction run; no pre-existing rows).

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (used). Source docs: Procedure.md, Specification.md, Guidance.md, _CONTEXT.md. Extracted 17 rows (8 ANCHOR, 9 EXECUTION); 0 retired. Parent anchor: 1 (IMPLEMENTS_NODE → SOW-0021). No pre-existing rows. Warnings: none.
