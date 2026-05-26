# Dependencies: DEL-034-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25. Schema version: v3.1. Total rows: 15. ACTIVE: 15. RETIRED: 0.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-034-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0035 | Scope Item SOW-0035 | HIGH | ACTIVE |
| DEP-034-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Objective OBJ-002 | MEDIUM | ACTIVE |
| DEP-034-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | MEDIUM | ACTIVE |
| DEP-034-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 | MEDIUM | ACTIVE |
| DEP-034-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 | MEDIUM | ACTIVE |
| DEP-034-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Objective OBJ-007 | MEDIUM | ACTIVE |
| DEP-034-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 | MEDIUM | ACTIVE |
| DEP-034-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | MEDIUM | ACTIVE |
| DEP-034-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 | MEDIUM | ACTIVE |
| DEP-034-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PACKAGE_REGISTER.csv row PKG-034 | HIGH | ACTIVE |
| DEP-034-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 DELIVERABLE_REGISTER.csv row DEL-034-01 | HIGH | ACTIVE |
| DEP-034-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-034-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-034-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-034-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-034-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-034-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-034-01-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | 04-25 13.8 kV Main Switchgear Electrical Building | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents: `Specification.md` (ANCHOR_DOC, also EXECUTION signal), `Datasheet.md`, `Guidance.md`, `Procedure.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor resolution and label validation.
- **Anchor resolution:** SOW-0035 confirmed in SCOPE_LEDGER.csv as the parent scope node for PKG-034. Objectives OBJ-002, OBJ-004–OBJ-010 confirmed in DELIVERABLE_REGISTER.csv row DEL-034-01.
- **ANCHOR pass notes:** One IMPLEMENTS_NODE anchor emitted (SOW-0035, WBS_NODE). Eight TRACES_TO_REQUIREMENT anchors emitted for OBJ-002 and OBJ-004–OBJ-010. Objective associations are ASSUMPTION (PACKAGE_HEURISTIC) per CFT-034-01-002.
- **EXECUTION pass notes:** Two upstream PREREQUISITE edges to Gate 7 register documents (identity source basis). Two downstream ENABLES edges to DEL-034-03 and DEL-034-04 (explicitly named in Specification.md exclusions). One downstream HANDOVER edge to DEL-034-02 (explicitly pointed to for interface fact detail). One upstream CONSTRAINT edge to 04-25 13.8 kV Main Switchgear Electrical Building (explicit cross-WBS power source per REQ-034-01-005).
- **Excluded from extraction:** DEL-034-05 (Vendor Document Turnover Package) and DEL-034-06 (EPC Vendor Package Review and Acceptance) were referenced in Specification.md exclusions context but without explicit information-flow statements from DEL-034-01; not emitted under CONSERVATIVE strictness.
- **[WARNING] MISSING_DECOMPOSITION does NOT apply** — decomposition path resolved successfully.
- **No `[WARNING] FLOATING_NODE`** — one IMPLEMENTS_NODE anchor present.
- **No `[WARNING] AMBIGUOUS_ANCHOR`** — exactly one IMPLEMENTS_NODE anchor.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 15 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 8 |
| EXECUTION / UPSTREAM | 3 |
| EXECUTION / DOWNSTREAM | 3 |
| SatisfactionStatus = SATISFIED | 2 |
| SatisfactionStatus = TBD | 13 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; dependency-extract skill (CONSERVATIVE); 15 rows extracted (15 ACTIVE, 0 RETIRED); schema VALID v3.1; decomposition resolved at GATE-07_Final_Published_2026-05-24.
