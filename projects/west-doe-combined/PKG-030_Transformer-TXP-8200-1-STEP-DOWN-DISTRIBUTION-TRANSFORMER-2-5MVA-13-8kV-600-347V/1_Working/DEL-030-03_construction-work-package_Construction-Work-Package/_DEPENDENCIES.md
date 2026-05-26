# Dependencies: DEL-030-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv generated)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-030-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-030 | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | TBD | ACTIVE |
| DEP-030-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0031 | Scope Item SOW-0031 | TBD | ACTIVE |
| DEP-030-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide the 04-25 Deepcut facility scope | TBD | ACTIVE |
| DEP-030-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Execute each electrical and mechanical equipment package as vendor-owned | TBD | ACTIVE |
| DEP-030-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Provide and integrate the facility electrical power basis | TBD | ACTIVE |
| DEP-030-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Provide and integrate controls instrumentation and communications | TBD | ACTIVE |
| DEP-030-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Provide civil structural site and construction-support scope | TBD | ACTIVE |
| DEP-030-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Carry sour-service safety and regulatory requirements | TBD | ACTIVE |
| DEP-030-03-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Maintain operability maintainability commissioning and turnover evidence | TBD | ACTIVE |
| DEP-030-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-030-02_package-datasheet | Package Datasheet | TBD | ACTIVE |
| DEP-030-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-030-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | TBD | ACTIVE |
| DEP-030-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-030-05_vendor-document-turnover-package | Vendor Document Turnover Package | TBD | ACTIVE |
| DEP-030-03-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-030-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | TBD | ACTIVE |

**Totals:** 13 rows — 9 ANCHOR, 4 EXECUTION; all ACTIVE.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 8 |
| EXECUTION / UPSTREAM / PREREQUISITE | 3 |
| EXECUTION / DOWNSTREAM / HANDOVER | 1 |
| SatisfactionStatus = TBD | 13 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md`, `Specification.md`, `Procedure.md`, `_CONTEXT.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic: contains identification/attributes tables)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; contains explicit prerequisite and handover statements), `Specification.md` (secondary; corroborates)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate PKG-030 anchor, SOW-0031, and OBJ-* identifiers
- **Parent anchor:** PKG-030 confirmed as WBS_NODE in PACKAGE_REGISTER.csv row 32; parent anchor emitted as DEP-030-03-001 (IMPLEMENTS_NODE).
- **Field-execution prerequisites:** Procedure.md explicitly names DEL-030-02, DEL-030-04, and DEL-030-05 as prerequisites for executing construction steps (not for authoring this deliverable). Captured as UPSTREAM/PREREQUISITE EXECUTION rows.
- **Downstream handover:** Procedure.md step 30 explicitly states the construction interface and turnover checklist (ART-E6DA4BF5C2) is handed to DEL-030-06 with all turnover evidence. Captured as DOWNSTREAM/HANDOVER EXECUTION row.
- **Gate 7 snapshot path note:** Brief specified `DECOMPOSITION_PATH` as `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` (directory not found at that path). Resolved to canonical location under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` consistent with `_CONTEXT.md` decomposition reference.
- **`_REFERENCES.md`:** Present; reviewed for document pointers. No additional DOCUMENT-type dependency rows warranted under CONSERVATIVE strictness beyond what is explicitly stated in source text.
- **No FLOATING_NODE warning:** One IMPLEMENTS_NODE anchor (DEP-030-03-001) present.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. SOURCE_DOCS=AUTO. Decomposition: GATE-07_Final_Published_2026-05-24. Produced Dependencies.csv v3.1 with 13 ACTIVE rows (9 ANCHOR, 4 EXECUTION). Schema: VALID.
