# Procedure: DEL-079-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing and checking the Vendor Document Turnover Package for `DEL-079-05_vendor-document-turnover-package`, covering the `PKG-079` Instrument Air Building package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 69.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Package requirements source slice: `_Sources/26020-Package_Requirements.docx`, heading 32 (Instrument Air Building): Source Basis table, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables table, Interface Coordination Notes (TBD).
- Vendor RFQ source basis (cited only): `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` (not locally accessible at this run).
- DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-079-05_vendor-document-turnover-package`.
3. Read Workbook Packages row 69 and record package ID, WBS, CoA tracking number, package name ("Instrument Air Building"), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-079` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-079-05` and confirm the deliverable carries the vendor document register (`ART-95A888C02E`), one row per source-listed Vendor Engineering Deliverables code, and per-category evidence rows.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-079` and confirm the vendor documentation must address each of the ten applicable interfaces where vendor scope crosses them.
7. Read the DBM mechanical package deliverables paragraph (line 617) for the vendor-document-register-required basis.
8. Read `_Sources/26020-Package_Requirements.docx` heading 32 (Instrument Air Building) and extract:
   - Source Basis (vendor RFQ document reference);
   - Basic Scope (package composition);
   - Major Included Equipment (ratings, set conditions, vendor-discretion items);
   - Scope Notes / Open Items (by-others items);
   - Physical Interface Summary (interface Yes/No matrix; row 69 column M lighting reference);
   - Vendor Engineering Deliverables table (full enumerated list by category and code);
   - Interface Coordination Notes (TBD).
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`; carry every source-listed Vendor Engineering Deliverables code by category in Attributes.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, including the equipment ratings, set conditions, and the source-enumerated turnover document codes.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, by-others scope handling, and human-ruling items (Conflict Table).
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, document codes, equipment ratings/set conditions, by-others scope, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite Workbook row 69, Gate 7 registers, the `_Sources/26020-Package_Requirements.docx` heading 32 slice, or the DBM mechanical package deliverables paragraph; otherwise are marked `TBD` / `ASSUMPTION`. |
| Equipment / conditions fidelity | PSV set 948 kPag (137.5 psig); delivered air dew point -73.3 °C at 1000 kPag; 2 x 1113 SCFM at 861 kPag (125 psig) rotary screw compressors; 2 x 250 HP motors; one wet air receiver; two dryer pre-filters; one 100% regenerative desiccant air dryer (sized for 2 compressors; size/capacity TBD by vendor); one common after-filter; one or two dry air receivers — values match across Datasheet, Specification, Guidance, and Procedure. |
| Interface consistency | All ten applicable interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) are consistent across the four documents and across `INTERFACE_REGISTER.csv`. |
| Vendor document code consistency | Every source-listed Vendor Engineering Deliverables code appears in Datasheet/Specification with identical spelling and matches an `ARTIFACT_REGISTER.csv` row for `DEL-079-05`. |
| Responsibility consistency | Vendor documentation production and EPC interface/integration review are not conflated. |
| By-others handling | Shipping, installation on piles, tie-in piping, electrical connections, and mounting platform/stairs are treated as outside vendor turnover scope. |
| Source-gap handling | Submittal stages, hold/issue codes, transmittal numbering, acceptance criteria, and Interface Coordination Notes remain `TBD` unless source-supported. |
| Human ruling items | Source-supported but operationally ambiguous items (submittal-control schema; by-others scope boundary; vendor-discretion dryer/receiver sizing) appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
