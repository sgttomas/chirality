# Procedure: DEL-038-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-038` (600V ELECTRICAL BUILDING (820-1)) from the accepted EPC inputs (`DEL-038-01` Scope of Work; `DEL-038-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-038-05`) and EPC vendor package acceptance (`DEL-038-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-038` (`DEL-038-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-038` (`DEL-038-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) are available for the electrical-buildings basis.
- EPC integration ruling on CFL-038-04-001 (building 820-1 voltage class) is either resolved or explicitly carried as an open item.
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-038-01` and `DEL-038-02` for `PKG-038`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS, CoA tracking number, discipline, building tag 820-1) from workbook row 40 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-038`.
   - Adopt the DBM electrical-buildings basis (prefabricated, modular, general-purpose-area location, n + 1 HVAC, pile-supported, bottom-entry cabling, TECK/ACIC wiring, EMT inter-cabinet conduit, outdoor GFI receptacle, equipment-removal door provisions).
   - Carry CFL-038-04-001 (building 820-1 voltage class) as an open item; do not commit voltage class until EPC integration rules.
3. **Engineer the package to the twelve applicable interfaces.**
   - Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
   - For each, define the vendor-side response at the building boundary, citing the relevant DBM slice when applicable.
4. **Develop the vendor package datasheet set.**
   - Capture building configuration (overall dimensions, weight, foundation provisions, HVAC sizing per n + 1, cable entries, door sizes/transoms, GFI receptacle).
   - Capture housed equipment (per resolved EPC equipment list): 600 V MCCs, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, PLC control panels, network racks, and 120 V AC / 125 V DC UPS systems with battery banks and distribution panels.
   - Mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-038-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered building (Shop-fabricated per DBM), housed equipment, internal cable tray and conduit, HVAC, wiring, grounding bus, and door provisions per vendor practice, including assembly, factory testing, and shipping preparation.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (installation location, area classification, facility power feed selection, generator/standby coordination, tie-ins to facility cable tray and grounding grid, building-tag voltage-class ruling) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve, including the building-tag voltage-class conflict.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package (building + housed equipment) and the vendor package design basis and datasheet set as inputs to `DEL-038-05_vendor-document-turnover-package` and `DEL-038-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all twelve applicable interfaces are addressed in vendor design. | Each interface has a vendor response at the building boundary. |
| Voltage-class conflict handling | Confirm CFL-038-04-001 is either ruled or carried as an explicit open item, and vendor design does not silently commit voltage class. | Conflict status traceable in vendor design basis. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no facility-feed selection, no standby logic, no ground-grid scope) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers building configuration, housed equipment, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-038-05` turnover and `DEL-038-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, conflicts, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered building, housed equipment, and factory documentation).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-038-06` (including CFL-038-04-001).
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
