# Procedure: DEL-033-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-033` (4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)) from the accepted EPC inputs (`DEL-033-01` Scope of Work; `DEL-033-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-033-05`) and EPC vendor package acceptance (`DEL-033-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-033` (`DEL-033-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-033` (`DEL-033-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM source slices are available for the electrical design basis: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-12 Electrical Basis; Foundations; Buildings) and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings, Grounding and Bonding, Cable/Raceway; Buildings schedule).
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-033-01` and `DEL-033-02` for `PKG-033`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)", IDs, WBS 02, CoA tracking 26020-02-30-024, discipline Electrical) from workbook row 35 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-033`.
   - Adopt the 03-25 DBM medium-voltage service basis (4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded) as the design basis service.
   - Adopt the 03-25 DBM incoming-power basis (sub-fed from 04-25 13.8 kV Main Switchgear via 13.8 kV-to-4.16 kV / 12 MVA step-down transformer feeding the 4160 V MCC for 4000 V motors) as the upstream condition.
3. **Engineer the package to the twelve applicable interfaces.**
   - Electrical Power: define vendor-side incoming connection, switchgear bus, feeders, and breakers; reflect facility incoming-power basis.
   - Grounding / Bonding: define vendor-side ground connections compatible with major-equipment two-point grounding and CEC-sized separate copper grounding conductors where applicable.
   - I&C / Control Cabling and Communications / Network: provide segregated control/instrument routing and the EtherNet link from the 4160 V MCC to the plant PLC central control panel.
   - Building HVAC / Services, Fire & Gas / Safety Systems, Area / Exterior Lighting: coordinate vendor-supplied vs. EPC-supplied service split, area classification, fire & gas detection, ESD pushbutton placement, and exterior lighting at the building boundary.
   - Utility Piping, Drain / Containment, Grading / Site Drainage / Spill Containment: coordinate building boundary conditions for any incoming utility piping, drains, and site grading/spill containment requirements.
   - Maintenance Access: lay out internal cable tray, conduit, and equipment access to preserve maintenance access; size doors / removable transoms for largest equipment removal where 04-25 practice is adopted.
   - Structural / Foundations / Supports: define skid/frame/foundation/support provisions; coordinate with foundation design driven by geotechnical, equipment-load, snow/wind/seismic, frost, vibration, settlement, and maintenance-access criteria.
4. **Develop the vendor package datasheet set.**
   - Capture switchgear lineup, bus rating, short-circuit rating, breaker schedule, frame sizes, arc-flash class, MCC functional features (fused contactors, motor protection relays, EtherNet to plant PLC), HVAC sizing, building dimensions, raceway and grounding response, and foundation/anchorage response.
   - Use vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-033-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including building shell, switchgear/MCC equipment, internal raceway and grounding, HVAC/ventilation, assembly, factory testing, and shipping preparation per vendor practice.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that facility-scope items (13.8 kV utility supply, 13.8 kV main switchgear, 13.8 kV-to-4.16 kV / 12 MVA step-down transformer, plot location, area classification finalization, harmonic and reactive-power studies, SCA-001 VE #34 / VE #37 effects, building tag relationship to 04-25 "830-1") remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-033-05_vendor-document-turnover-package` and `DEL-033-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all twelve applicable interfaces are addressed in vendor design. | Each `INTERFACE_REGISTER.csv` row for `PKG-033` has a vendor response. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented facility incoming-power scope, no facility-level harmonic/reactive-power study commitments, no EPC plot-location decisions in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, switchgear/MCC ratings, HVAC, raceway/grounding, foundation/anchorage, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-033-05` turnover and `DEL-033-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation for the 4160 V switchgear electrical building).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-033-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
