# Procedure: DEL-017-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-017` (MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD) from the accepted EPC inputs (`DEL-017-01` Scope of Work; `DEL-017-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-017-05`) and EPC vendor package acceptance (`DEL-017-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-017` (`DEL-017-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-017` (`DEL-017-02`) is available as the vendor engineering technical handoff basis (driven motor data, operating duty, signal/protocol list, area classification, location).
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slice (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) is available for the 4160 V system context (transformer, MCC, EtherNet path, VFD starting basis, capacitor-bank removal).
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-017-01` and `DEL-017-02` for `PKG-017`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS 02, CoA tracking number 26020-02-30-008, discipline Electrical) from workbook row 19 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-017`.
   - Adopt the DBM 4160 V system context (13.8 kV / 4.16 kV, 12 MVA transformer; 4160 V MCC; EtherNet to plant PLC) as the system-level design basis context.
3. **Engineer the package to the six applicable interfaces.**
   - Electrical Power (`IFC-5E50E5F700`): define vendor-side input connection, 4160 V class voltage, currents, feeder requirements, and VFD output to the driven motor.
   - Grounding / Bonding (`IFC-1340C6D795`): define vendor-side ground connections compatible with major-equipment two-point grounding and CEC-sized separate copper grounding conductors where applicable.
   - I&C / Control Cabling (`IFC-6ECD9C92A1`): define the vendor-side control termination set (start/stop, run, fault, trip, status) consistent with `DEL-017-02`.
   - Communications / Network (`IFC-FB4034716A`): provide an EtherNet interface compatible with the 4160 V MCC EtherNet path to the plant PLC central control panel; protocol and address per `DEL-017-02`.
   - Maintenance Access (`IFC-A807F5E0B3`): lay out internal cable tray, conduit, and equipment access (drive sections, control compartments, protection) to preserve maintenance access.
   - Structural / Foundations / Supports (`IFC-34EB597147`): define skid/frame/foundation/support provisions and coordinate with the EPC structural interface.
4. **Develop the vendor package datasheet set.**
   - Capture VFD configuration (topology, cooling, harmonic mitigation envelope, input isolation, output contactor / bypass arrangement, enclosure rating, environmental conditions) with vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Capture driven-motor compatibility (inverter-duty rating, insulation class, bearing protection, motor protection settings) taken from `DEL-017-02`.
   - Cross-reference the EPC Package Datasheet (`DEL-017-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including assembly, factory testing (including dielectric and functional testing as applicable to MV equipment), and shipping preparation per vendor practice.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (harmonic and reactive-power studies, capacitor-bank treatment per SCA-001 VE #37, installation location, area classification, structural support coordination, facility EtherNet network attachment) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-017-05_vendor-document-turnover-package` and `DEL-017-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all six applicable interfaces are addressed in vendor design. | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports each have a vendor response. |
| Power-quality basis | Confirm vendor harmonic / reactive-power approach is consistent with EPC-defined electrical studies and does not assume capacitor-bank support removed by SCA-001 VE #37. | Vendor approach references the DBM 4160 V MCC paragraph and EPC study direction. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no facility-level harmonic study, no facility ground-grid scope, no facility EtherNet network design) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-017-05` turnover and `DEL-017-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation, including MV factory test records as applicable).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data and `DEL-017-02`, or carried forward as integration questions to `DEL-017-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
