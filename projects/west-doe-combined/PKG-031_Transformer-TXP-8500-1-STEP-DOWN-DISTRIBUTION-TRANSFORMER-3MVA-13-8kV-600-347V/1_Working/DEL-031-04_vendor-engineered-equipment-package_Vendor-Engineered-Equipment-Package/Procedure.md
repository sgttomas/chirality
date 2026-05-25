# Procedure: DEL-031-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-031` (Transformer TXP-8500-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3 MVA, 13.8 kV / 600/347 V) from the accepted EPC inputs (`DEL-031-01` Scope of Work; `DEL-031-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-031-05`) and EPC vendor package acceptance (`DEL-031-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-031` (`DEL-031-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-031` (`DEL-031-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) are available for the 13.8 kV / 600 V step-down transformer design basis.
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-031-01` and `DEL-031-02` for `PKG-031`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS 01, CoA tracking number 26020-01-30-022, discipline Electrical, equipment tag TXP-8500-1) from workbook row 33 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-031`.
   - Adopt the DBM medium-voltage service basis (13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded) for the primary side.
   - Adopt the DBM low-voltage service basis (600/347 V wye, high-resistance grounded with 5 A continuous resistor; ground-fault alarm-only) for the secondary side.
   - Carry the 03-25 "13.8 kV to 600V, 3 MVA transformer" entry as the working facility allocation (ASSUMPTION); confirm in `DEL-031-02` or flag at `DEL-031-06`.
3. **Engineer the package to the seven applicable interfaces.**
   - Electrical Power: define vendor-side primary connection to the upstream 13.8 kV switchgear feeder and vendor-side secondary connection to the 600 V MCC.
   - Grounding / Bonding: define vendor-side ground bus, transformer ground well/test point, two-point grid connection, and CEC-sized separate copper grounding conductors; provide neutral grounding-resistor connection for the 600 V secondary.
   - Area / Exterior Lighting: confirm 347 V neutral takeoff arrangement consistent with the project lighting service derivation; specific lighting tie-in remains outside the package.
   - I&C / Control Cabling: define vendor-side monitoring (winding/oil temperature, pressure, gas, level), alarm/trip contacts, and metering/CT wiring boundary (vendor-internal vs. EPC-routed).
   - Communications / Network: define vendor-side monitoring/IED communications and any HMI/SCADA tie-ins to the host electrical-building network rack.
   - Maintenance Access: lay out clearances, bushing access, tap-changer access, radiator/cooling-system access, and lifting/handling provisions to preserve maintenance access.
   - Structural / Foundations / Supports: define skid/frame/foundation/support provisions and coordinate with the EPC Structural / Foundations / Supports interface and the host installation location (indoor electrical building vs. outdoor pad).
4. **Develop the vendor package datasheet set.**
   - Capture transformer configuration (winding configuration, impedance, cooling class, insulation type, tap arrangement, primary/secondary terminations, neutral arrangement, accessories, protection package, monitoring, dimensions/weights, sound level, environmental ratings) with vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-031-02`) so each EPC-stated requirement has a vendor response.
   - Confirm no 13.8 kV-level emergency-generator interface is engineered, per the DBM standby-power basis, unless `DEL-031-02` explicitly requires one (flag as integration issue if so).
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including transformer core/coil assembly, accessories, factory protective devices, factory acceptance testing (winding resistance, ratio, polarity, no-load and load loss, impedance, insulation resistance, applied/induced voltage withstand, partial discharge as applicable), and shipping preparation per vendor practice and applicable industry standards (e.g., IEEE/CSA distribution-transformer standards; ASSUMPTION until EPC Package Datasheet confirms).
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (installation location assignment, foundation/anchor design, transformer-pad civil work, secondary containment, ground-grid tie-in design, external cable tray and conduit routing, facility-wide protection coordination study, arc-flash study, site testing and commissioning) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-031-05_vendor-document-turnover-package` and `DEL-031-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all seven applicable interfaces are addressed in vendor design. | Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports each have a vendor response. |
| Nameplate fidelity | Confirm 3 MVA, 13.8 kV / 600/347 V, 60 Hz nameplate matches workbook row 33 and `DEL-031-02`. | Nameplate matches workbook row 33 and EPC Package Datasheet. |
| Service basis | Confirm 13.8 kV LRG primary and 600 V HRG (5 A) secondary bases are preserved in vendor design. | Vendor single-line and design basis reflect DBM electrical services. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no site civil/foundation design, no external cable routing, no facility-wide protection coordination, no site arc-flash study) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-031-05` turnover and `DEL-031-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation, including FAT records).
- Vendor package design basis document.
- Vendor package datasheet set (winding configuration, impedance, cooling class, insulation type, tap arrangement, terminations, neutral arrangement, accessories, protection package, monitoring, dimensions/weights, sound level, environmental ratings).
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-031-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
