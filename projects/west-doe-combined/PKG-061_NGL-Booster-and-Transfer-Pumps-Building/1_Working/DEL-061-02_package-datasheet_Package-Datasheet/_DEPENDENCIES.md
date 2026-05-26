# Dependencies: DEL-061-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema, 29 columns). This file is the human-readable view and declared-dependency index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `dependency-extract` skill (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**Summary:** 24 rows total — 24 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName / TargetRefID | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-061-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-061 | HIGH | ACTIVE |
| DEP-061-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0149 | HIGH | ACTIVE |
| DEP-061-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0150 | HIGH | ACTIVE |
| DEP-061-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0151 | HIGH | ACTIVE |
| DEP-061-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0152 | HIGH | ACTIVE |
| DEP-061-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | HIGH | ACTIVE |
| DEP-061-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | HIGH | ACTIVE |
| DEP-061-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH | ACTIVE |
| DEP-061-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | HIGH | ACTIVE |
| DEP-061-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | HIGH | ACTIVE |
| DEP-061-02-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | HIGH | ACTIVE |
| DEP-061-02-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | HIGH | ACTIVE |
| DEP-061-02-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | HIGH | ACTIVE |
| DEP-061-02-014 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | HIGH | ACTIVE |
| DEP-061-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-061-01_scope-of-work | HIGH | ACTIVE |
| DEP-061-02-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-061-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-061-02-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-061-06_epc-vendor-package-review-and-acceptance | MEDIUM | ACTIVE |
| DEP-061-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | PRO-013 | HIGH | ACTIVE |
| DEP-061-02-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | 26020-Package_Requirements.docx heading 17 | HIGH | ACTIVE |
| DEP-061-02-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | DBM-Deepcut/4-25_Deepcut_DBM.md row 58 | HIGH | ACTIVE |
| DEP-061-02-021 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | EPC Integrator — DCS Integration (by others) | HIGH | ACTIVE |
| DEP-061-02-022 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | EPC Integrator / Civil — Foundations (by others) | HIGH | ACTIVE |
| DEP-061-02-023 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | EPC Integrator / Electrical — MCC power supply (by others) | HIGH | ACTIVE |
| DEP-061-02-024 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-061-03_construction-work-package | MEDIUM | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (gate snapshot confirmed present; DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv rows PKG-061 / DEL-061-02 verified).
- **SOURCE_DOCS:** AUTO — scanned: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`. ANCHOR_DOC = `Datasheet.md` (contains "datasheet" in name and Identification table). EXECUTION_DOC_ORDER = `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- **_REFERENCES.md:** Present; used to confirm decomposition snapshot path and source document paths. No TargetType=DOCUMENT rows emitted solely from references listing; evidence-first rule applied.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE parent anchor (DEP-061-02-001, target PKG-061). Thirteen TRACES_TO_REQUIREMENT rows for SOW-0149/0150/0151/0152 and OBJ-001/003–010 per Specification.md Scope and DELIVERABLE_REGISTER.csv. All identifiers confirmed in decomposition.
- **Pass 2 (EXECUTION):** Ten EXECUTION rows covering prerequisite (DEL-061-01), handovers (DEL-061-04, DEL-061-06), source-document constraints (26020-Package_Requirements.docx, DBM row 58, PRO-013), by-others interface constraints (DCS integration, foundations, MCC electrical), and downstream enable (DEL-061-03).
- **Tree x DAG integrity:** Parent anchor count = 1 (DEP-061-02-001). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.
- **CONFLICT-03 note:** PRO-013 (Pump Hydraulic / NPSH Calculations) is registered as an upstream CONSTRAINT on the TDH field. Until PRO-013 closes, the SatisfactionStatus for DEP-061-02-018 remains TBD.
- **DEL-061-06 and DEL-061-03 confidence:** MEDIUM because Procedure.md names the use cases (interface coordination; vendor RFQ) but does not name those deliverable IDs directly. Marked ASSUMPTION in Notes column of CSV.

## Lifecycle Summary

| Metric | Count |
|---|---|
| Total rows | 24 |
| ACTIVE | 24 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 14 |
| EXECUTION rows (ACTIVE) | 10 |
| IMPLEMENTS_NODE | 1 |
| TRACES_TO_REQUIREMENT | 13 |
| SatisfactionStatus = TBD | 24 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed present). Sources: Datasheet.md, Guidance.md, Procedure.md, Specification.md. Result: 24 ACTIVE rows written (14 ANCHOR, 10 EXECUTION). Schema: VALID (29 columns). No FLOATING_NODE. No MISSING_DECOMPOSITION.
