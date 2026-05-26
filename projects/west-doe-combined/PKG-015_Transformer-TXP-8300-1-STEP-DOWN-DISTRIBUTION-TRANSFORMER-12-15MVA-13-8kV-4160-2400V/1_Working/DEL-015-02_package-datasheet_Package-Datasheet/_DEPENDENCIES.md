# Dependencies: DEL-015-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

18 rows extracted; all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-015-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0016 | Scope decision SOW-0016 — Transformer TXP-8300-1 (WBS 02) | HIGH | ACTIVE |
| DEP-015-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-015-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-015-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-015-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-015-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-015-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-015-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-015-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-015-01_scope-of-work | Scope of Work — PKG-015 | HIGH | ACTIVE |
| DEP-015-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-015-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-015 | HIGH | ACTIVE |
| DEP-015-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-015-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-015 | HIGH | ACTIVE |
| DEP-015-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-E8F09F1065 | Interface IFC-E8F09F1065 — Electrical Power | HIGH | ACTIVE |
| DEP-015-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-073273FE3A | Interface IFC-073273FE3A — Grounding / Bonding | HIGH | ACTIVE |
| DEP-015-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-677CA55221 | Interface IFC-677CA55221 — Area / Exterior Lighting | HIGH | ACTIVE |
| DEP-015-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-99831AAF77 | Interface IFC-99831AAF77 — I&C / Control Cabling | HIGH | ACTIVE |
| DEP-015-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-6582D48513 | Interface IFC-6582D48513 — Communications / Network | HIGH | ACTIVE |
| DEP-015-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-B9C22F51DB | Interface IFC-B9C22F51DB — Maintenance Access | HIGH | ACTIVE |
| DEP-015-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-2646D74297 | Interface IFC-2646D74297 — Structural / Foundations / Supports | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs:** AUTO — scanned deliverable folder; primary source documents found: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
- **Anchor doc:** `Datasheet.md` (matched heuristic: filename contains `datasheet`)
- **Execution docs:** `Datasheet.md`, `Procedure.md`, `Guidance.md`, `Specification.md`
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — RESOLVED; used for anchor validation and label resolution.
- **Decomposition brief path referenced in brief:** `GATE-07_Final_Published_2026-05-24/` (resolved to full path above).
- **Pass 1 (ANCHOR):** SOW-0016 confirmed in SCOPE_LEDGER.csv as parent scope decision; seven objective traces (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed in OBJECTIVE_DELIVERABLE_MAP.csv. One IMPLEMENTS_NODE row emitted; seven TRACES_TO_REQUIREMENT rows emitted.
- **Pass 2 (EXECUTION):** Three deliverable-to-deliverable edges extracted from Datasheet.md and DELIVERABLE_REGISTER.csv: upstream PREREQUISITE from DEL-015-01 (Scope of Work as responsibility/boundary basis); downstream HANDOVER to DEL-015-04 (vendor engineering handoff); downstream HANDOVER to DEL-015-06 (acceptance review against this datasheet). Seven interface edges extracted from Datasheet.md Conditions table (IFC-E8F09F1065, IFC-073273FE3A, IFC-677CA55221, IFC-99831AAF77, IFC-6582D48513, IFC-B9C22F51DB, IFC-2646D74297) — all explicitly cited as must-be-represented in the package interface requirements matrix.
- **Tree x DAG check:** One IMPLEMENTS_NODE row present — no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- **_REFERENCES.md:** Read; confirmed Gate 7 decomposition path and shared source root. No document-to-document dependency rows emitted from references alone (per skill contract: references alone are not sufficient evidence).

## Lifecycle Summary

- **ACTIVE rows:** 18
- **RETIRED rows:** 0
- **ANCHOR rows (ACTIVE):** 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
- **EXECUTION rows (ACTIVE):** 10 (3 deliverable-to-deliverable + 7 interface)
- **SatisfactionStatus breakdown:** 18 TBD

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (RESOLVED). 18 ACTIVE rows extracted. No warnings.
