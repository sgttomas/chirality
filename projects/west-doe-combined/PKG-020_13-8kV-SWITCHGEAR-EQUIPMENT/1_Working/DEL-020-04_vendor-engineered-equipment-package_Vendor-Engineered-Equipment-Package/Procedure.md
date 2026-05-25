# Procedure: DEL-020-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-020` (13.8kV SWITCHGEAR EQUIPMENT) from the accepted EPC inputs (`DEL-020-01` Scope of Work; `DEL-020-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-020-05`) and EPC vendor package acceptance (`DEL-020-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-020` (`DEL-020-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-020` (`DEL-020-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) are available for the 13.8 kV switchgear design basis.
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-020-01` and `DEL-020-02` for `PKG-020`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, WBS 01, CoA tracking number 26020-01-30-011, discipline Electrical) from workbook row 22 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-020`.
   - Adopt the DBM medium-voltage service basis (13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded) as the design basis.
   - Adopt the DBM "plant main power distribution center" role: bus sized for the full facility scope; radial distribution to step-down transformers; cross-facility sub-feed from 04-25 to 03-25.
3. **Engineer the package to the six applicable interfaces.**
   - Electrical Power: define vendor-side incoming connection to the utility-supplied 25 kV/13.8 kV transformer and outgoing feeder connections to downstream step-down transformers and the 03-25 sub-feed.
   - Grounding / Bonding: define vendor-side ground bus and bonding compatible with major-equipment two-point grounding and CEC-sized separate copper grounding conductors where applicable.
   - I&C / Control Cabling: define vendor-side breaker control, protective-relay wiring, status/alarm contacts, and metering wiring boundary (vendor-internal vs. EPC-routed).
   - Communications / Network: define vendor-side protective-relay communications, IED network drops, and any HMI/SCADA tie-ins to the electrical-building network rack.
   - Maintenance Access: lay out front/rear access, breaker maneuvering space, and arc-flash boundaries to preserve maintenance access.
   - Structural / Foundations / Supports: define skid/frame/foundation/support provisions and coordinate with the EPC Structural / Foundations / Supports interface and the host electrical-building floor plan.
4. **Develop the vendor package datasheet set.**
   - Capture switchgear configuration (bus rating, short-circuit duty, breaker schedule including incoming and outgoing breakers, protective-relay platform/scheme, control voltage source, instrument transformers, enclosure rating, environmental ratings, dimensions/weights) with vendor-data values; mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-020-02`) so each EPC-stated requirement has a vendor response.
   - Confirm no 13.8 kV-level emergency generator interface is engineered, per the DBM standby-power basis, unless `DEL-020-02` explicitly requires one (flag as integration issue if so).
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the engineered physical equipment package (vendor scope), including switchgear lineup assembly, factory protective-relay configuration, factory acceptance testing, and shipping preparation per vendor practice and applicable industry standards (e.g., IEEE/CSA metal-clad switchgear standards; ASSUMPTION until EPC Package Datasheet confirms).
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (installation building assignment, foundation/anchor details, external cable tray and conduit routing, ground-grid tie-in, facility-wide protection coordination study, arc-flash study, site testing and commissioning) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-020-05_vendor-document-turnover-package` and `DEL-020-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all six applicable interfaces are addressed in vendor design. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports each have a vendor response. |
| Service basis | Confirm 13.8 kV, 3 phase, 3 wire, 60 Hz, LRG basis is preserved in vendor design. | Vendor single-line and design basis reflect DBM medium-voltage services. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no site civil/foundation design, no external cable routing, no facility-wide protection coordination, no site arc-flash study) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-020-05` turnover and `DEL-020-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered hardware and factory documentation, including FAT records).
- Vendor package design basis document.
- Vendor package datasheet set (bus rating, short-circuit duty, breaker schedule, protection scheme, control diagrams, enclosure/environmental ratings).
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-020-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
