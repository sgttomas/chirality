# Procedure: DEL-013-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-013` (100A DC UNINTERUPTIBLE POWER SUPPLY) from the accepted EPC inputs (`DEL-013-01` Scope of Work; `DEL-013-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-013-05`) and EPC vendor package acceptance (`DEL-013-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-013` (`DEL-013-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-013` (`DEL-013-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) are available for the electrical design basis.
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-013-01` and `DEL-013-02` for `PKG-013`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS, CoA tracking number, discipline) from workbook row 15 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-013`.
   - Adopt the DBM electrical service basis (120 VAC / 125 VDC UPS services) as the design basis voltage/service starting point.
3. **Engineer the package to the four applicable interfaces.**
   - Electrical Power: define vendor-side connection points, voltages, currents, and feeder requirements.
   - Grounding / Bonding: define vendor-side ground connections compatible with major-equipment two-point grounding and CEC-sized separate copper grounding conductors where applicable.
   - Maintenance Access: lay out internal cable tray, conduit, and equipment access to preserve maintenance access.
   - Structural / Foundations / Supports: define skid/frame/foundation/support provisions and coordinate with the EPC Structural / Foundations / Supports interface.
4. **Develop the vendor package datasheet set.**
   - Capture UPS configuration (count, rating, battery technology, autonomy, charger/rectifier, distribution panel(s), enclosure, environmental ratings) with vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-013-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including assembly, factory testing, and shipping preparation per vendor practice.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (standby power coordination, transfer-switch configuration, generator sizing, load shedding, sequencing, TOU standard, installation location, area classification) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-013-05_vendor-document-turnover-package` and `DEL-013-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all four applicable interfaces are addressed in vendor design. | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports each have a vendor response. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no transfer-switch logic, no facility load-shedding, no facility ground-grid scope, etc.) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-013-05` turnover and `DEL-013-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-013-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
