# Dependencies: DEL-041-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

6 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | Direction | Type | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-041-04-001 | ANCHOR | UPSTREAM | OTHER | WBS_NODE | PKG-041 — 13.8kV 3.0MW STANDBY GENERATOR BUILDING (490-1) | TBD | HIGH |
| DEP-041-04-002 | ANCHOR | UPSTREAM | OTHER | REQUIREMENT | SOW-0042 — Scope item for PKG-041 | TBD | HIGH |
| DEP-041-04-003 | EXECUTION | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-041-01_scope-of-work | TBD | HIGH |
| DEP-041-04-004 | EXECUTION | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-041-02_package-datasheet | TBD | HIGH |
| DEP-041-04-005 | EXECUTION | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-041-05_vendor-document-turnover-package | TBD | HIGH |
| DEP-041-04-006 | EXECUTION | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-041-06_epc-vendor-package-review-and-acceptance | TBD | HIGH |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents used: `Datasheet.md` (ANCHOR_DOC), `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains Identification table with explicit ParentPackageID and Covers Scope Item fields)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary), `Specification.md`, `Guidance.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor validation and target ID resolution. All target IDs confirmed in DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, and SCOPE_LEDGER.csv (GATE-07).
- **`_REFERENCES.md` status:** Present; no deliverable-specific source slices copied (Missing/Deferred); shared source root noted. Decomposition registers used as primary reference for ID resolution.
- No invented targets. All TargetDeliverableIDs confirmed in DELIVERABLE_REGISTER.csv (GATE-07).
- Parent anchor: 1 IMPLEMENTS_NODE row (DEP-041-04-001, PKG-041). No FLOATING_NODE warning.
- Trace anchor: 1 TRACES_TO_REQUIREMENT row (DEP-041-04-002, SOW-0042).
- EXECUTION edges: 2 UPSTREAM PREREQUISITE (DEL-041-01, DEL-041-02); 2 DOWNSTREAM HANDOVER (DEL-041-05, DEL-041-06).
- Interface register (INTERFACE_REGISTER.csv GATE-07) lists 12 facility-level interface IDs for PKG-041 (IFC-508C53EB72 through IFC-D0146B1F8C). These are design constraints owned by the EPC Integrator, not information-flow dependencies of DEL-041-04 as a deliverable; they are documented in Datasheet.md and Specification.md. Not emitted as dependency rows under CONSERVATIVE strictness (no explicit artifact/approval transfer stated between DEL-041-04 and individual interface deliverables).

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 6 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 2 |
| EXECUTION | 4 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION). No Dependencies.csv generated.
- 2026-05-25 — dependency-extract skill run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. SOURCE_DOCS=AUTO. Decomposition GATE-07 used for anchor validation. 6 ACTIVE rows written to Dependencies.csv (v3.1). Schema validation: VALID. No warnings.
