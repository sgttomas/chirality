# Dependencies: DEL-024-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv generated)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extraction run: 2026-05-25 | MODE=UPDATE | STRICTNESS=CONSERVATIVE

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-024-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0025 | Scope decision SOW-0025 — MV VFD package (WBS 01) | ACTIVE |
| DEP-024-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | ACTIVE |
| DEP-024-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package execution model | ACTIVE |
| DEP-024-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power and infrastructure | ACTIVE |
| DEP-024-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation communications | ACTIVE |
| DEP-024-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site and foundations | ACTIVE |
| DEP-024-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Sour-service safety and regulatory | ACTIVE |
| DEP-024-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability and turnover | ACTIVE |
| DEP-024-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PACKAGE_REGISTER.csv row PKG-024 | ACTIVE |
| DEP-024-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 INTERFACE_REGISTER.csv PKG-024 rows | ACTIVE |
| DEP-024-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut facility electrical basis (lines 2957–2973) | ACTIVE |
| DEP-024-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-024-02_package-datasheet | Package Datasheet — DEL-024-02 | ACTIVE |
| DEP-024-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-024-03_construction-work-package | Construction Work Package — DEL-024-03 | ACTIVE |
| DEP-024-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-024-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — DEL-024-04 | ACTIVE |

**Total ACTIVE rows:** 14 (8 ANCHOR, 6 EXECUTION)
**Total RETIRED rows:** 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md, Specification.md, Procedure.md, Guidance.md (ANCHOR_DOC heuristic: Datasheet.md / Specification.md; EXECUTION_DOC_ORDER: Procedure.md, Specification.md, Datasheet.md)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — found and used; anchors validated against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv.
- **_REFERENCES.md:** Present; used for source document path confirmation. No additional TargetType=DOCUMENT rows added solely from _REFERENCES.md (no source statement requires them beyond what was captured).
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE anchor to SOW-0025 (WBS_NODE); seven TRACES_TO_REQUIREMENT anchors to OBJ-001/004/005/006/008/009/010. All confirmed in DELIVERABLE_REGISTER.csv.
- **Pass 2 (EXECUTION):** Three UPSTREAM PREREQUISITE rows for Gate 7 registers and DBM-Deepcut electrical basis (Procedure.md Steps 2-3, 5-6; Specification.md SOW-024-05). Three DOWNSTREAM ENABLES rows for DEL-024-02, DEL-024-03, DEL-024-04 (Specification.md Scope paragraph explicit statement; decomposition confirmed IDs).
- **DEP-024-01-014 note:** MEDIUM confidence — enable relationship to DEL-024-04 is stated in Specification.md and supported by decomposition description but is partially indirect; Notes field marks the ASSUMPTION.
- **Tree x DAG integrity:** Exactly one IMPLEMENTS_NODE anchor found — no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- **Vendor data gaps:** Package-specific MV VFD vendor data (driven motor tag, topology, harmonic mitigation, weights, dimensions) is TBD and not present in accessible source slices. No dependency rows created for unavailable vendor documents; this would require a later REFRESH run once vendor data is received.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |
| PENDING | 3 |

PENDING rows: DEP-024-01-009, DEP-024-01-010, DEP-024-01-011 (upstream prerequisite documents; Gate 7 snapshot accepted, DBM accessible — dependencies are satisfied at accepted snapshot level but marked PENDING pending formal SOW completion).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition path used: GATE-07_Final_Published_2026-05-24. SOURCE_DOCS=AUTO (Datasheet.md, Specification.md, Procedure.md). 14 rows extracted (8 ANCHOR, 6 EXECUTION). 0 RETIRED. Schema validation: VALID.
