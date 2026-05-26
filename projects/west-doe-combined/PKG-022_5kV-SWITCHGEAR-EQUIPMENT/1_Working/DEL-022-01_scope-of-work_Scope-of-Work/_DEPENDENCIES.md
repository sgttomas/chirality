# Dependencies: DEL-022-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (updated by dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-022-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0023 | Scope decision SOW-0023 — 5kV SWITCHGEAR EQUIPMENT | ACTIVE | HIGH |
| DEP-022-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | ACTIVE | HIGH |
| DEP-022-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned electrical/mechanical package execution | ACTIVE | HIGH |
| DEP-022-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical power and electrical package integration | ACTIVE | HIGH |
| DEP-022-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications integration | ACTIVE | HIGH |
| DEP-022-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site foundations and support | ACTIVE | HIGH |
| DEP-022-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety regulatory codes and standards requirements | ACTIVE | HIGH |
| DEP-022-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability vendor documentation and turnover | ACTIVE | HIGH |
| DEP-022-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | ACTIVE | HIGH |
| DEP-022-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Workbook Packages row 24 | ACTIVE | HIGH |
| DEP-022-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM Deepcut electrical and MV services sections | ACTIVE | HIGH |
| DEP-022-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | — | Package-specific vendor data (bus rating; short-circuit; breaker; BIL; enclosure; footprint) | ACTIVE | HIGH |
| DEP-022-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-022-02_package-datasheet | Package Datasheet | ACTIVE | HIGH |
| DEP-022-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-022-03_construction-work-package | Construction Work Package | ACTIVE | HIGH |
| DEP-022-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-022-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | ACTIVE | HIGH |

**Counts:** 15 rows total — 8 ANCHOR, 7 EXECUTION; all 15 ACTIVE, 0 RETIRED.

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: Specification.md (ANCHOR_DOC), Procedure.md (EXECUTION_DOC), Guidance.md (EXECUTION_DOC), Datasheet.md (informational).
- **ANCHOR_DOC:** Specification.md (contains SOW requirements, identity fields, and scope objectives).
- **EXECUTION_DOC_ORDER:** Procedure.md (explicit prerequisites and steps), Guidance.md (conflict table and principles).
- **DECOMPOSITION_PATH:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor validation. SOW-0023, OBJ-001/004/005/006/008/009/010, and deliverable IDs DEL-022-01 through DEL-022-06 confirmed in SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv, and DELIVERABLE_REGISTER.csv.
- **Tree x DAG check:** 1 IMPLEMENTS_NODE anchor (DEP-022-01-001) — no FLOATING_NODE warning; no AMBIGUOUS_ANCHOR warning.
- **Pass 1 (ANCHOR):** SOW-0023 confirmed as parent scope node. All 7 objectives confirmed in DELIVERABLE_REGISTER.csv OBJ column for DEL-022-01.
- **Pass 2 (EXECUTION):** Three explicit upstream prerequisites from Procedure.md (Gate 7 snapshot, workbook row 24, DBM Deepcut electrical sections). One PENDING upstream (package-specific vendor data explicitly absent per Procedure.md). Two downstream ENABLES rows for Package Datasheet and Construction Work Package confirmed from Specification.md scope statement. One downstream ENABLES for Vendor Engineered Equipment Package confirmed from Specification.md.
- **DEP-022-01-012 (vendor data):** SatisfactionStatus=PENDING; this is the primary open information gap. Package-specific switchgear design data (bus voltage, short-circuit rating, breaker type, BIL, enclosure, footprint, weights) not present in accessible source slices. Affects downstream datasheet readiness.
- **TargetLocation for DOCUMENT rows:** Resolved from Procedure.md prerequisite statements and _REFERENCES.md shared source root. Gate 7 snapshot path confirmed accessible; workbook and DBM path confirmed via _REFERENCES.md shared source root.
- **No downstream handoff notes:** CONSUMER_CONTEXT=NONE.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
| SATISFIED | 3 |
| PENDING | 1 |
| NOT_APPLICABLE | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full extraction run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; decomposition path GATE-07_Final_Published_2026-05-24; 15 rows extracted (8 ANCHOR, 7 EXECUTION); all ACTIVE; 1 PENDING (vendor data gap DEP-022-01-012); schema validation VALID.
