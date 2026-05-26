# Procedure — DEL-051-04 Vendor Engineered Equipment Package (PKG-051 Process Heat Medium Unit)

## Purpose

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package deliverable for PKG-051 — i.e., the work the Package Vendor (with EPC Integrator integration review) performs to engineer, design, and supply the physical Process Heat Medium Unit equipment package and supporting vendor documentation.

## Prerequisites

- DEL-051-01 (EPC Scope of Work) issued and accepted as the dispatching scope basis. (Declared upstream not yet captured in `_DEPENDENCIES.md`; record `TBD` for the formal `Upstream` edge until written there.)
- DEL-051-02 (Package Datasheet) issued and accepted as the EPC-side datasheet input to the vendor.
- Access to source slices used by this deliverable:
  - 26020-Package_Requirements.docx, heading 6 (`_Sources/26020-Package_Requirements.docx`).
  - 26020-Packages_Interfaces_4_export.xlsx, Packages row 79.
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, §"Heat Medium Basis" (lines 1945-2002), for context on facility-level integration.
- `_REFERENCES.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` available in this deliverable folder.
- Human rulings on `Guidance.md` Conflict Table entries CONF-051-04-01..06 OR a documented decision to bid against the workbook source basis with conflicts flagged. ASSUMPTION: workbook source governs vendor scope baseline pending rulings (per Guidance Conflict Table PROPOSAL rows).

## Steps

### Step 1 — Confirm scope basis
1.1 Read DEL-051-01 (EPC Scope of Work) and DEL-051-02 (Package Datasheet).
1.2 Resolve each open Conflict Table item in `Guidance.md` to either: (a) workbook source baseline (default PROPOSAL), or (b) EPC-issued scope change to the unified-loop basis. Record the rulings.

### Step 2 — Establish vendor design basis
2.1 Adopt fluid, temperature, pressure, pump arrangement, expansion-tank constraints, and total throughput from Specification §Requirements (R-2..R-7) and Datasheet §Conditions, modified per Step 1 rulings.
2.2 Establish heater duty, type, and sparing per Specification R-6 — using DBM-Deepcut candidate values only if Step 1 ruling adopts the unified-loop basis.

### Step 3 — Modular engineering and design
3.1 Engineer the Supply Pump Module: expansion tank, three (3) single-stage vertical inline heat medium pumps (workbook basis), associated piping, instrumentation, and skid structure.
3.2 Engineer the Medium Heater Module: medium heater, heater blower, air intake pre-heater, associated piping, instrumentation, combustion-air system, and skid structure.
3.3 Define vendor skid battery limits consistent with the by-others exclusions (Specification §Scope) so that interconnecting piping, DCS integration, foundations, site mounting buildings, electrical MCC supply, and platforms/stairs are presented as EPC scope at clean skid-edge interfaces.
3.4 Map skid-edge interfaces against the PKG-051 applicable interface types (Specification R-10).

### Step 4 — Produce vendor documentation
4.1 Produce the vendor package design basis document covering loop arrangement, fluid selection rationale, design conditions, sparing philosophy, and skid-edge interfaces.
4.2 Produce the vendor datasheet set for each major equipment item (expansion tank, heat medium pumps, medium heater, heater blower, air intake pre-heater).
4.3 Detailed deliverables list, format, and turnover schedule per DEL-051-05 (Vendor Document Turnover Package). TBD here.

### Step 5 — Fabricate / supply the physical equipment package
5.1 Fabricate, assemble, and shop-test modules per the vendor design.
5.2 Prepare the physical package for site delivery with the supporting documentation produced in Step 4.

### Step 6 — EPC Integrator integration review
6.1 Submit vendor general-arrangement drawings, P&IDs, equipment datasheets, and skid-edge interface schedules for EPC Integrator review per DEL-051-06 (EPC Vendor Package Review and Acceptance).
6.2 Address EPC integration-review comments through vendor-issued revisions until acceptance.

## Verification

| Step | Verification Check |
|---|---|
| 1 | Conflict Table rulings recorded and applied; design basis traceable to rulings or to PROPOSAL defaults. |
| 2 | Design basis traceable to source slices cited in Datasheet/Specification with no unsourced numeric values introduced. |
| 3.1 | Pump and expansion-tank capacities meet R-2, R-3, R-7. |
| 3.2 | Heater module configured to consume Specification R-6 inputs (or Step 1 ruling outputs). |
| 3.3 | Vendor scope-of-supply matrix shows zero overlap with by-others exclusions. |
| 3.4 | Each applicable PKG-051 interface type has at least one identified skid-edge tie-in or an explicit "not applicable to this package" statement. |
| 4 | Vendor design basis and datasheet set cross-reference to Specification requirement IDs. |
| 5 | Shop-test records (hydrostatic, FAT, etc.) on file. (Specific tests: TBD — to be defined by vendor QA plan, not in this skill's scope.) |
| 6 | EPC Integrator acceptance record obtained per DEL-051-06. |

## Records

- Conflict Table rulings (filed in deliverable `MEMORY.md` when written, or in the EPC project record).
- Vendor package design basis document.
- Vendor datasheet set for all major equipment items.
- Vendor general-arrangement drawings and P&IDs.
- Skid-edge interface schedule against PKG-051 applicable interface types.
- Shop-test and FAT records.
- EPC integration-review comments and disposition record.
- EPC acceptance record (cross-references DEL-051-06).
