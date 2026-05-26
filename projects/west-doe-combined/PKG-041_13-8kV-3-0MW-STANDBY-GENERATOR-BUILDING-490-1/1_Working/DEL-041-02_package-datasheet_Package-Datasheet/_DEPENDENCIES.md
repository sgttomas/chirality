# Dependencies: DEL-041-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 produced)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv contains **14 ACTIVE rows** across two dependency classes:

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-041-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0042 | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) — SOW-0042 | SATISFIED | HIGH |
| DEP-041-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide the 04-25 Deepcut facility scope | TBD | HIGH |
| DEP-041-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Execute each electrical/mechanical package as vendor-owned | TBD | HIGH |
| DEP-041-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Provide and integrate facility electrical power basis | TBD | HIGH |
| DEP-041-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Provide and integrate controls/instrumentation/communications | TBD | HIGH |
| DEP-041-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Provide and integrate shared utilities and ancillary support | TBD | HIGH |
| DEP-041-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Provide civil/structural/site/construction-support scope | TBD | HIGH |
| DEP-041-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Carry sour-service safety and regulatory requirements | TBD | HIGH |
| DEP-041-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Maintain operability/vendor-doc/commissioning/turnover evidence | TBD | HIGH |
| DEP-041-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | GATE-07 PROJECT_DECOMP snapshot | SATISFIED | HIGH |
| DEP-041-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-041-01_scope-of-work | Scope of Work (PKG-041) | TBD | HIGH |
| DEP-041-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-041-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (PKG-041) | TBD | HIGH |
| DEP-041-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-041-05_vendor-document-turnover-package | Vendor Document Turnover Package (PKG-041) | TBD | HIGH |
| DEP-041-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-041-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (PKG-041) | TBD | HIGH |

**Totals:** 14 ACTIVE, 0 RETIRED | 9 ANCHOR (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT), 5 EXECUTION (2 UPSTREAM + 3 DOWNSTREAM)

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: `Datasheet.md` (ANCHOR_DOC), `Guidance.md`, `Procedure.md`, `Specification.md` (EXECUTION_DOCS)
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match: filename contains `datasheet`)
- **EXECUTION_DOC_ORDER:** `Guidance.md`, `Procedure.md`, `Specification.md` (remaining docs by name)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor resolution and label normalization
- **`_REFERENCES.md` consulted:** Yes — used to confirm decomposition path and resolve `TargetLocation` for DOCUMENT row

**Anchor resolution:**
- SOW-0042 confirmed in `SCOPE_LEDGER.csv` row SOW-0042, associated with PKG-041 and DEL-041-02_package-datasheet. FACT.
- OBJ-001, OBJ-004..OBJ-010 confirmed in `DELIVERABLE_REGISTER.csv` row DEL-041-02_package-datasheet `ObjectiveID(s)` column and cross-referenced against `OBJECTIVE_REGISTER.csv`. FACT.

**Execution edge decisions:**
- DEP-041-02-010: GATE-07 snapshot is explicitly listed as a prerequisite in `Procedure.md` Prerequisites and required by `Specification.md` REQ-DS-09.
- DEP-041-02-011: DEL-041-01 is explicitly listed as the scope/boundary source in `Procedure.md` Prerequisites ("scope source for boundary"). Specification REQ-DS-08 prohibits reassertion, implying interface. Classified UPSTREAM INTERFACE.
- DEP-041-02-012..014: `Guidance.md` Purpose explicitly names DEL-041-04, DEL-041-05, DEL-041-06 as dependent on this datasheet ("all depend"). Classified DOWNSTREAM HANDOVER.
- DEL-041-03_construction-work-package: mentioned in Specification out-of-scope section only; no explicit information flow to/from this deliverable stated. Not extracted under CONSERVATIVE strictness.

**No warnings:**
- Parent anchor (IMPLEMENTS_NODE) count: 1 — OK
- Decomposition available and used — OK

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 2 |
| TBD | 12 |
| PENDING | 0 |
| IN_PROGRESS | 0 |
| WAIVED | 0 |
| NOT_APPLICABLE | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07 snapshot (available). SOURCE_DOCS=AUTO (4 docs scanned). Produced Dependencies.csv v3.1 with 14 ACTIVE rows (9 ANCHOR + 5 EXECUTION). No warnings. Schema validated VALID.
