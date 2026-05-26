# Dependencies: DEL-030-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (updated from DECLARED)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-030-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0031 | Scope decision SOW-0031 — Transformer TXP-8200-1 (WBS 01) | ACTIVE |
| DEP-030-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | ACTIVE |
| DEP-030-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned electrical/mechanical package responsibility model | ACTIVE |
| DEP-030-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical power basis and electrical equipment integration | ACTIVE |
| DEP-030-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications integration | ACTIVE |
| DEP-030-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil/structural/foundations/support scope | ACTIVE |
| DEP-030-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety/drain/containment/regulatory/codes | ACTIVE |
| DEP-030-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability/maintainability/vendor-documentation/turnover/closure | ACTIVE |
| DEP-030-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | ACTIVE |
| DEP-030-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-030-01_scope-of-work | Scope of Work — PKG-030 Transformer TXP-8200-1 | ACTIVE |
| DEP-030-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-009C48E7FF | Interface IFC-009C48E7FF — Electrical Power | ACTIVE |
| DEP-030-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-6C663BF69D | Interface IFC-6C663BF69D — Grounding/Bonding | ACTIVE |
| DEP-030-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-4B50D76AF1 | Interface IFC-4B50D76AF1 — Structural/Foundations/Supports | ACTIVE |
| DEP-030-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-030-03_construction-work-package | Construction Work Package — PKG-030 | ACTIVE |
| DEP-030-02-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-030-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-030 | ACTIVE |
| DEP-030-02-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-030-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-030 | ACTIVE |

**Total ACTIVE rows:** 16 (8 ANCHOR, 8 EXECUTION)
**RETIRED rows:** 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md, Specification.md, Procedure.md, Guidance.md
- **ANCHOR_DOC:** Datasheet.md (matches `datasheet` heuristic; highest-confidence anchor signal)
- **EXECUTION_DOC_ORDER:** Procedure.md, Specification.md, Guidance.md
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` (from BRIEF) — resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` per `_REFERENCES.md` authoritative path. Decomposition successfully read; SCOPE_LEDGER.csv and OBJECTIVE_DELIVERABLE_MAP.csv used for anchor validation.
- **Pass 1 (ANCHOR):** SOW-0031 confirmed in SCOPE_LEDGER.csv as the parent scope decision node for PKG-030. Seven objectives (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed in OBJECTIVE_DELIVERABLE_MAP.csv for DEL-030-02_package-datasheet. One IMPLEMENTS_NODE parent anchor emitted.
- **Pass 2 (EXECUTION):** Gate 7 snapshot prerequisite (DEP-030-02-009) and Scope of Work prerequisite (DEP-030-02-010) extracted from Procedure.md. Three interface-register inputs (IFC-009C48E7FF, IFC-6C663BF69D, IFC-4B50D76AF1) extracted from Datasheet.md § Conditions. Three downstream handover targets extracted from Specification.md. Remaining four workbook interfaces (IFC-0B28AED229, IFC-D000451C37, IFC-9EF13A0FC1, IFC-345609CB34) are interface facts consumed within this deliverable's own matrix but do not constitute separate information-flow edges under CONSERVATIVE strictness — they are documented in the interface matrix, not as incoming dependency transfers to another deliverable.
- **Dropped (coordination-only):** DBM source slices are source references, not information-flow dependencies. No rows emitted for DBM reads.
- **No MISSING_DECOMPOSITION warning:** Decomposition successfully resolved.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition path resolved. 16 ACTIVE rows written (8 ANCHOR + 8 EXECUTION). Schema validated VALID.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 16 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 8 |
