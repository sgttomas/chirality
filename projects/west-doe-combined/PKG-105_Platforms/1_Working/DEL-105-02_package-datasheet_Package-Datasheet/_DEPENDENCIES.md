# Dependencies: DEL-105-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

15 rows extracted (15 ACTIVE, 0 RETIRED).

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-105-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0261 | Scope decision SOW-0261 — Platforms (WBS 01) | HIGH | ACTIVE |
| DEP-105-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-105-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical / area lighting | MEDIUM | ACTIVE |
| DEP-105-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil/structural/site scope | HIGH | ACTIVE |
| DEP-105-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Handoff readiness | MEDIUM | ACTIVE |
| DEP-105-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-105-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-105-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 registers (PACKAGE / DELIVERABLE / ARTIFACT / INTERFACE / OBJECTIVE_DELIVERABLE) | HIGH | ACTIVE |
| DEP-105-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Workbook Packages row 106 — 26020-Packages_Interfaces_4_export | HIGH | ACTIVE |
| DEP-105-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut structural/civil source sections (SEC-11) | HIGH | ACTIVE |
| DEP-105-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Geotechnical assessment report (bearing capacity; LPILE curves; dynamic design criteria) | HIGH | ACTIVE |
| DEP-105-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-105-03_construction-work-package | Construction Work Package | MEDIUM | ACTIVE |
| DEP-105-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-105-04_epc-structural-discipline-production-package | EPC / Structural Discipline Production Package | MEDIUM | ACTIVE |
| DEP-105-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-26E3DCAD56 | Interface Fact IFC-26E3DCAD56 — Area / Exterior Lighting | HIGH | ACTIVE |
| DEP-105-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-07C472C58B | Interface Fact IFC-07C472C58B — Grading / Site Drainage / Spill Containment | HIGH | ACTIVE |
| DEP-105-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-B7C0A01E38 | Interface Fact IFC-B7C0A01E38 — Structural / Foundations / Supports | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
| PENDING | 1 |
| SATISFIED | 4 |
| IN_PROGRESS | 0 |
| WAIVED | 0 |
| NOT_APPLICABLE | 0 |

**PENDING items (action required):**
- DEP-105-02-010 — Geotechnical assessment report not yet in `_Sources`; platform foundation sizing cannot close without bearing capacity, LPILE curves, and dynamic design criteria.

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE (first extraction; no prior Dependencies.csv)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned:** `Datasheet.md` (ANCHOR_DOC), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOCS)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed present; all anchor IDs validated against PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- **`_REFERENCES.md` consulted:** Yes — used to resolve Gate 7 snapshot path and confirm no additional source slices were copied during PREPARATION.
- **DependencyID format:** `DEP-{PKG_NUM}-{DEL_NUM}-{SEQ}` following project pattern from PKG-001 reference register.
- **Objective associations OBJ-005 and OBJ-010:** Confidence=MEDIUM; these derive from PACKAGE_HEURISTIC mode in OBJECTIVE_DELIVERABLE_MAP.csv per Guidance.md Considerations. Labeled ASSUMPTION in Notes column.
- **No geotechnical report located in `_Sources`:** DEP-105-02-010 SatisfactionStatus=PENDING; TargetLocation left blank.
- **Interface facts (DEP-105-02-013/014/015):** Carried as UPSTREAM INTERFACE edges to EXTERNAL targets per Specification.md R-6/R-7 and Datasheet.md Package Interface Facts table. TargetType=EXTERNAL reflects that IFC records live in INTERFACE_REGISTER, not as deliverables.
- **No `[WARNING] FLOATING_NODE`:** One IMPLEMENTS_NODE parent anchor (DEP-105-02-001) found — Tree integrity satisfied.
- **No `[WARNING] AMBIGUOUS_ANCHOR`:** Exactly one IMPLEMENTS_NODE row.
- **No `[WARNING] MISSING_DECOMPOSITION`:** Gate 7 snapshot confirmed present.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run; UPDATE mode; CONSERVATIVE strictness; 15 rows written (15 ACTIVE, 0 RETIRED); decomposition path GATE-07_Final_Published_2026-05-24 confirmed; no integrity warnings.
