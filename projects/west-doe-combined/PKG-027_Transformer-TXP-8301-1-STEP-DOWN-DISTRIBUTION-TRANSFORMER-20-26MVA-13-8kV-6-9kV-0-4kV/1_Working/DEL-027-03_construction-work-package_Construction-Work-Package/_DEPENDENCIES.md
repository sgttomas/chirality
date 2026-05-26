# Dependencies: DEL-027-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 produced)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-25. Schema v3.1. 16 data rows.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName (short) | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-027-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0028 | Scope of Work item SOW-0028 | ACTIVE |
| DEP-027-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Objective OBJ-001 | ACTIVE |
| DEP-027-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | ACTIVE |
| DEP-027-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 | ACTIVE |
| DEP-027-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 | ACTIVE |
| DEP-027-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 | ACTIVE |
| DEP-027-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | ACTIVE |
| DEP-027-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 | ACTIVE |
| DEP-027-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | ACTIVE |
| DEP-027-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-027-01_scope-of-work | Scope of Work | ACTIVE |
| DEP-027-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-027-02_package-datasheet | Package Datasheet | ACTIVE |
| DEP-027-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-027-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | ACTIVE |
| DEP-027-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-7FDEAE3A5F | Interface — Electrical Power | ACTIVE |
| DEP-027-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-868150D715 | Interface — Grounding / Bonding | ACTIVE |
| DEP-027-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-1B8FDDED83 | Interface — Structural / Foundations / Supports | ACTIVE |
| DEP-027-03-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO (scanned: `Datasheet.md`, `Specification.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`)
- **ANCHOR_DOC:** `_CONTEXT.md` / `Datasheet.md` (highest-confidence anchor signals)
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Specification.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (used for anchor validation and label resolution)
- **Decomposition status:** AVAILABLE — anchors validated against SCOPE_LEDGER.csv, OBJECTIVE_DELIVERABLE_MAP.csv, and PACKAGE_REGISTER.csv.
- **_REFERENCES.md:** Read; used to confirm decomposition path. No `_REFERENCES.md` local document-pointer table present beyond gate snapshot path.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE anchor to SOW-0028 (confirmed in SCOPE_LEDGER.csv); seven TRACES_TO_REQUIREMENT anchors to OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 (all confirmed in _CONTEXT.md and SCOPE_LEDGER.csv row SOW-0028).
- **Pass 2 (EXECUTION):** Eight EXECUTION rows extracted: Gate 7 snapshot prerequisite (Procedure.md); DEL-027-01 and DEL-027-02 as upstream prerequisites (Specification.md identity/responsibility requirements); DEL-027-04 as upstream interface (vendor data explicitly marked TBD in REQ-027-03-009); three interface register documents (IFC-7FDEAE3A5F Electrical Power, IFC-868150D715 Grounding/Bonding, IFC-1B8FDDED83 Structural/Foundations/Supports from Datasheet.md Conditions); DEL-027-05 downstream handover (turnover checklist ART-6C4FC25B92).
- **Interface coverage note:** Four additional interfaces (IFC-A7AA374E9F Area/Exterior Lighting, IFC-A771D8D087 I&C/Control Cabling, IFC-41603B3260 Communications/Network, IFC-6D508F385A Maintenance Access) are listed in Datasheet.md Conditions table but have less explicit construction-dependency language than the three captured rows; these are not extracted to avoid coordination-only edges under CONSERVATIVE strictness.
- **DEP-027-03-012 SatisfactionStatus=PENDING:** Vendor data explicitly TBD per REQ-027-03-009; dependency is open until DEL-027-04 is accepted.
- **DEP-027-03-016 Confidence=MEDIUM:** ASSUMPTION that turnover checklist produced here is consumed by DEL-027-05; not explicitly stated as a data-handover in source documents.
- **No warnings issued.**

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 16 |
| RETIRED rows | 0 |
| ANCHOR rows (ACTIVE) | 8 |
| EXECUTION rows (ACTIVE) | 8 |
| IMPLEMENTS_NODE anchors | 1 |
| TRACES_TO_REQUIREMENT anchors | 7 |
| SatisfactionStatus=TBD | 15 |
| SatisfactionStatus=PENDING | 1 |

Tree x DAG integrity:
- Parent anchor count (IMPLEMENTS_NODE, ACTIVE): 1 — OK.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition available (GATE-07). 16 ACTIVE rows written (8 ANCHOR + 8 EXECUTION). Schema validation: VALID. No warnings.
