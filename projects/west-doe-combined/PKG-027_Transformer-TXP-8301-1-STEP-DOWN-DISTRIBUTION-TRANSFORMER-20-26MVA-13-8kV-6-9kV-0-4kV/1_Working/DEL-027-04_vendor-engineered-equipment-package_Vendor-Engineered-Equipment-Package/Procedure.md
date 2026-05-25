# Procedure: DEL-027-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-027` (Transformer TXP-8301-1, 20/26 MVA step-down distribution transformer per workbook title) from the accepted EPC inputs (`DEL-027-01` Scope of Work; `DEL-027-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-027-05`) and EPC vendor package acceptance (`DEL-027-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-027` (`DEL-027-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-027` (`DEL-027-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) are available for the electrical design basis (13.8 kV / 6.9 kV / 600 V voltage table, step-down transformer distribution paragraph, transformers paragraph, grounding paragraphs, foundations paragraph, electrical buildings paragraph, medium-voltage cable table).
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-027-01` and `DEL-027-02` for `PKG-027`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design. In particular, resolve the 0.4 kV winding question (CFL-027-04-001) with the EPC before fixing the winding configuration.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS 01, CoA tracking number 26020-01-30-018, discipline Electrical) from workbook row 29 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-027`.
   - Adopt the DBM electrical service basis as the design basis: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded backbone; 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded process motor service; 100 A 10 s NGR on each 6.9 kV transformer; major-equipment two-point ground-grid connection with ground wells at power transformers.
3. **Engineer the package to the seven applicable interfaces.**
   - Electrical Power: define vendor-side primary (13.8 kV) connection points and bushings; define secondary (6.9 kV and any 0.4 kV) connection points, currents, and fault-withstand capability.
   - Grounding / Bonding: define vendor-side neutral bushing and NGR interface (compatible with 100 A 10 s on 6.9 kV), and major-equipment ground pads compatible with two-point ground-grid connection and CEC-sized separate copper grounding conductor.
   - Area / Exterior Lighting: confirm vendor pad-print does not interfere with the EPC lighting layout.
   - I&C / Control Cabling: define vendor protection, monitoring (temperature, oil level, gas, pressure), metering, and control signal landings.
   - Communications / Network: define network interface for protection relays/monitoring (e.g., Ethernet) where applicable.
   - Maintenance Access: lay out radiators, bushings, tap changer, sampling, NGR cubicle if vendor-supplied, and oil-containment provisions with CEC spacing preserved.
   - Structural / Foundations / Supports: provide skid/base design, weights, pad-print, and anchor pattern for the EPC precast concrete bearing foundation or structural-steel transformer base.
4. **Develop the vendor package datasheet set.**
   - Capture transformer configuration (rating 20/26 MVA, cooling class, insulation medium, BIL, impedance, vector group, tap-changer, vector diagram, audible-noise level, losses, accessories) with vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Capture secondary winding configuration explicitly, including resolution of the 0.4 kV winding question (CFL-027-04-001).
   - Cross-reference the EPC Package Datasheet (`DEL-027-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including factory assembly, factory testing (routine tests; type tests as applicable), and shipping preparation per vendor practice and applicable industry standards.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (installation pad assignment, area classification, ground-grid design, NGR supply split, oil-containment design, cable termination logistics, foundation design from vendor weights/pad-print, transformer spacing per CEC) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package (`ART-6FA1DBA3D1`) and the vendor package design basis and datasheet set (`ART-0723EEECE8`) as inputs to `DEL-027-05_vendor-document-turnover-package` and `DEL-027-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all seven applicable interfaces are addressed in vendor design. | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports each have a vendor response. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no facility ground-grid design, no facility pad/foundation design beyond vendor inputs, no facility cable-routing design) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-027-05` turnover and `DEL-027-06` review. |
| Conflict-table closure | Confirm Guidance Conflict Table items (CFL-027-04-001 through CFL-027-04-005) have proposed dispositions and are flagged for human ruling. | All conflicts surfaced with proposals and `TBD` rulings. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-027-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
