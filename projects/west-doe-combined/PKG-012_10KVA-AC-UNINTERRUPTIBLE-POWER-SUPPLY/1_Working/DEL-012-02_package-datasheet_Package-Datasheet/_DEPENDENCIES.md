# Dependencies: DEL-012-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-012-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0013 | Scope decision SOW-0013 — 10KVA AC UPS (WBS 02) | HIGH | ACTIVE |
| DEP-012-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-012-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — vendor-owned electrical/mechanical package execution | HIGH | ACTIVE |
| DEP-012-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — facility electrical power basis and integration | HIGH | ACTIVE |
| DEP-012-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — civil/structural/site scope | HIGH | ACTIVE |
| DEP-012-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — sour-service safety and regulatory requirements | HIGH | ACTIVE |
| DEP-012-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — operability/maintainability/vendor-documentation/turnover | HIGH | ACTIVE |
| DEP-012-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-012-01_scope-of-work | Scope of Work (PKG-012) | HIGH | ACTIVE |
| DEP-012-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-012-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (PKG-012) | HIGH | ACTIVE |
| DEP-012-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-012-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (PKG-012) | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

ANCHOR rows: 7 (1 IMPLEMENTS_NODE + 6 TRACES_TO_REQUIREMENT)
EXECUTION rows: 3 (1 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER)

Parent anchor (IMPLEMENTS_NODE): 1 — SOW-0013. No FLOATING_NODE warning.

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: Datasheet.md, Guidance.md, Procedure.md, Specification.md, _REFERENCES.md, _DEPENDENCIES.md
- **ANCHOR_DOC:** Datasheet.md (matches `datasheet` heuristic; also Specification.md as secondary anchor source)
- **EXECUTION_DOC_ORDER:** Procedure.md (primary execution signal), Specification.md, Guidance.md, Datasheet.md
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP` (live surface used; Gate 7 snapshot path per _REFERENCES.md: `_GateSnapshots/GATE-07_Final_Published_2026-05-24`)
- **DECOMPOSITION_PATH from brief:** `GATE-07_Final_Published_2026-05-24/` — directory does not exist as a standalone path; used live `_Decomposition/PROJECT_DECOMP` surface which contains equivalent data (SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, OBJECTIVE_REGISTER.csv confirmed present and current). [WARNING] DECOMP_PATH_REDIRECT: Brief path `GATE-07_Final_Published_2026-05-24/` not found as standalone directory; redirected to live `_Decomposition/PROJECT_DECOMP` surface. Anchor IDs and labels resolved successfully.
- **Anchor resolution:** SOW-0013 confirmed in SCOPE_LEDGER.csv; OBJ-002/004/005/008/009/010 confirmed in OBJECTIVE_REGISTER.csv and DELIVERABLE_REGISTER.csv OBJ column for DEL-012-02.
- **EXECUTION pass:** DEL-012-01 (Scope of Work) identified as upstream PREREQUISITE — DELIVERABLE_REGISTER.csv confirms DEL-012-01 is the mandatory EPC anchor deliverable; Specification.md REQ-012-02-001/002 require package identity and responsibility boundary content that originates in DEL-012-01. DEL-012-04 (Vendor Engineered Equipment Package) identified as downstream HANDOVER consumer — DELIVERABLE_REGISTER.csv row for DEL-012-04 states it is developed from the EPC Scope of Work and Package Datasheet. DEL-012-06 (EPC Vendor Package Review and Acceptance) identified as downstream HANDOVER consumer — DELIVERABLE_REGISTER.csv row explicitly names the Package Datasheet as a reference basis for acceptance review.
- **Coordination statements excluded:** Procedure.md cross-document consistency checks are coordination steps, not information-transfer dependencies; excluded per skill method.
- **Interface register rows (IFC-AA089340E0, IFC-2F50872E45, IFC-52E7E27E87, IFC-1D40B1F072):** These are interface facts carried inside DEL-012-02 per DELIVERABLE_REGISTER.csv design intent; they are not emitted as separate EXECUTION dependency rows because no specific information transfer to a named deliverable is stated beyond what is already captured in the DEL-012-04/DEL-012-06 handover edges.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. SOURCE_DOCS=AUTO. Decomposition redirected to live surface. 10 rows extracted (ACTIVE): 7 ANCHOR + 3 EXECUTION. Schema v3.1. Validation: VALID.
