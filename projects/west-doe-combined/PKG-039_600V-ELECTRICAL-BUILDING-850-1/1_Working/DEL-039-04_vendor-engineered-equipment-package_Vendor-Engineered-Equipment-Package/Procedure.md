# Procedure: DEL-039-04_vendor-engineered-equipment-package

## Purpose

This procedure describes how the Package Vendor produces the Vendor Engineered Equipment Package for `PKG-039` (600V ELECTRICAL BUILDING (850-1) — the 600 V Inlet / Sales Compressor Electrical Building) from the accepted EPC inputs (`DEL-039-01` Scope of Work; `DEL-039-02` Package Datasheet) and how the EPC Integrator confirms readiness for downstream vendor document turnover (`DEL-039-05`) and EPC vendor package acceptance (`DEL-039-06`).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-039` (`DEL-039-01`) is available as the vendor engineering scope basis.
- Accepted EPC Package Datasheet for `PKG-039` (`DEL-039-02`) is available as the vendor engineering technical handoff basis.
- Gate 7 PROJECT_DECOMP snapshot is the accepted decomposition truth (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- DBM electrical source slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) are available for the electrical-buildings design basis, HVAC, cable entry, 600 V MCC, standby power, and grounding paragraphs.
- Declared upstream/downstream dependencies for this deliverable: none declared during PREPARATION; coordination is advisory through the EPC integration workflow.

## Steps

1. **Confirm vendor engineering inputs.**
   - Verify the accepted state of `DEL-039-01` and `DEL-039-02` for `PKG-039`.
   - Resolve any open items in those inputs (or carry them forward as constraints) before starting vendor design.
2. **Establish vendor package design basis.**
   - Restate package identity (name, IDs, discipline, WBS, CoA tracking number) from workbook row 41 and the Gate 7 package register.
   - Restate the package responsibility split (Vendor: engineering/design/equipment/vendor documentation; EPC: facility integration and interfaces) from `PACKAGE_REGISTER.csv` row `PKG-039`.
   - Adopt the DBM electrical-buildings basis: prefabricated, shop-built modular building; general-purpose-area placement; elevated on piles; bottom cable entry; n + 1 HVAC; TECK/ACIC internal wiring; EMT for adjacent equipment; outdoor GFI receptacle; equipment doors sized for largest equipment removal.
3. **Engineer the package to the twelve applicable interfaces.**
   - Utility Piping; Drain / Containment: define building penetrations and drain provisions at the envelope.
   - Electrical Power: define incoming 600 V feeder termination, MCC main incoming section, and outgoing 600 V feeder terminations; preserve bottom cable entry.
   - Grounding / Bonding: define vendor-side ground connections compatible with major-equipment two-point grounding and CEC-sized separate copper grounding conductors where applicable.
   - Area / Exterior Lighting: define exterior building lighting tie-in and the outdoor GFI receptacle.
   - I&C / Control Cabling: define motor local control station wiring to MCC starter circuits and cabling to PLC and contactor panels.
   - Communications / Network: define network rack provisions and cabling envelope.
   - Building HVAC / Services: design the n + 1 HVAC system and electric heater provisions.
   - Fire & Gas / Safety Systems: provide envelope provisions; detailed device lists remain EPC.
   - Maintenance Access: lay out internal equipment and doors to preserve maintenance access.
   - Grading / Site Drainage / Spill Containment: coordinate below-building grade and drainage envelope provisions.
   - Structural / Foundations / Supports: provide the building skid/frame and pile-elevation provisions; pile/foundation design coordinated with EPC.
4. **Develop the vendor package datasheet set.**
   - Capture per-equipment datasheets for the DBM-permitted population actually included (600 V MCCs with in-lineup VFDs; 600 V SCR heater-control panels; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; 120 VAC and 125 VDC UPS systems with battery banks and distribution panels; plant PLC control panels; network racks; HVAC units; lighting and receptacles).
   - Mark `TBD` only where vendor data has not yet been resolved.
   - Cross-reference the EPC Package Datasheet (`DEL-039-02`) so each EPC-stated requirement has a vendor response.
5. **Design and fabricate / supply the physical equipment package.**
   - Produce the shop-built modular electrical building (vendor scope), including assembly, factory testing, and shipping preparation per vendor practice.
6. **Coordinate integration items with EPC Integrator.**
   - Confirm that integration items (standby-power coordination at the 600 V MCC, transfer-switch configuration, generator sizing, load shedding, sequencing, TOU standard confirmation, installation location, pile/foundation design, Fire & Gas device list, area-classification exceptions) remain with the EPC Integrator and are not invented in vendor scope.
   - Record vendor recommendations and constraints that EPC integration must resolve.
7. **Release vendor outputs to downstream deliverables.**
   - Provide the vendor engineered physical equipment package and the vendor package design basis and datasheet set as inputs to `DEL-039-05_vendor-document-turnover-package` and `DEL-039-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Inputs traceability | Trace each vendor design element to a source slice (DBM, Gate 7 register, or accepted EPC input). | Each non-trivial value or constraint cites a source or is explicitly `TBD` / `ASSUMPTION`. |
| Interface coverage | Confirm all twelve applicable interfaces are addressed in vendor design. | Each of the twelve `INTERFACE_REGISTER.csv` rows for `PKG-039` has a vendor response. |
| Building basis fidelity | Compare vendor building to DBM electrical-buildings basis. | Prefabricated/shop-built/modular, general-purpose area, elevated on piles, bottom cable entry, n + 1 HVAC, TECK/ACIC wiring, EMT for adjacent equipment, outdoor GFI, and door-sizing requirements are reflected. |
| Responsibility integrity | Confirm vendor design does not encroach on EPC integration scope. | No invented integration scope (no transfer-switch logic, no facility load-shedding, no facility ground-grid scope, no F&G facility strategy) in vendor design. |
| Datasheet set completeness | Confirm vendor datasheet set covers identity, attributes, interface responses, and supports the EPC Package Datasheet. | Vendor datasheet set ready for `DEL-039-05` turnover and `DEL-039-06` review. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Records

- Vendor engineered physical equipment package (delivered shop-built modular electrical building and factory documentation).
- Vendor package design basis document.
- Vendor package datasheet set.
- Source-gap / `TBD` list closed by vendor data, or carried forward as integration questions to `DEL-039-06`.
- TASK run record at `_run_records/` documenting the four-document drafting pass for this deliverable.
