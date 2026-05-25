# Procedure: Construction Work Package

## Purpose

Define a source-grounded procedure to produce and use the Construction Work Package for DEL-008-03_construction-work-package. The procedure supports physical installation planning, tie-in planning, inspection, turnover, and open-item control for the PKG-008 controls system design and integration package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- DBM-Deepcut SEC-12 Cable, Wire, and Raceways; SEC-13 Controls System Basis; and SEC-14 Instrumented Protection Basis are available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none currently declared in `_DEPENDENCIES.md`.
- ASSUMPTION: final detailed-design documents, construction drawings, safety study outputs, and client IT/OT records will be attached or referenced before construction release. These are not currently available in this deliverable folder.

## Steps

1. Confirm the deliverable identity.
   - Verify the CWP is for DEL-008-03_construction-work-package, PKG-008 Controls system design and integration, responsible party EPC Integrator.
   - Source: Gate 7 `DELIVERABLE_REGISTER.csv` and deliverable `_CONTEXT.md`.

2. Establish the work package boundary.
   - Include physical installation, construction, tie-in, inspection, and turnover into larger systems.
   - Keep sibling deliverables, package datasheet content, and controls discipline production-package design work out of this CWP except as references.
   - Source: Gate 7 `PROJECT_DECOMP.md`, section 7.

3. Build the construction interface matrix.
   - Include process piping, utility piping, relief / flare / vent, electrical power, I&C / control cabling, communications / network, building HVAC / services, and fire & gas / safety systems.
   - Mark unresolved controls power-panel interface tracking as Human Ruling Required until source or human direction resolves it.
   - Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-008.

4. Prepare the controls equipment placement workface plan.
   - Include control room equipment, MCC-based Level 1 components, secondary servers, distribution switches, and process-area Remote I/O cabinets.
   - Mark Remote I/O cabinet final locations as `TBD`.
   - Source: DBM-Deepcut SEC-13 Physical Layout and Equipment Placement; Interfaces, Assumptions, and Open Design Development.

5. Prepare the network and communications tie-in checklist.
   - Include PCN, I/O Network, Controller Network, IDMZ Network, and Enterprise Network touchpoints.
   - Record client IT/OT coordination hold points for IDMZ layout, enterprise-network requirements, network hardware selection, industrial networking policy, and switch configuration.
   - Source: DBM-Deepcut SEC-13 Network Basis and Interfaces.

6. Prepare the Modbus and package-control handoff checklist.
   - Confirm Modbus is used for monitoring and data collection only.
   - Confirm standalone package/unit control systems are integrated for monitoring/alarming and that final package data maps, permissive logic, trip interfaces, and alarm priorities remain detailed-design/vendor-integration deliverables where not available.
   - Source: DBM-Deepcut SEC-13 Modbus Data Basis and Controls System Hardware; DBM-Comp_and_Liquids SEC-13 may be used as contextual corroboration for standalone unit controls if admitted by the project team.

7. Prepare cable, wire, tray, and conduit installation checks.
   - Check armored tray cable, instrumentation cable, fiber cable, tray supports, tray type, conduit material, conduit sealing at area-classification changes, minimum conduit size, and maintenance-access clearance.
   - Include the requirement that secondary tray runs for instruments and small power runs may be field-contractor scope where not shown on drawings.
   - Source: DBM-Deepcut SEC-12 Cable, Wire, and Raceways.

8. Prepare fire, gas, alarm, ESD, and unit-shutdown installation checks.
   - Include fire, gas, H2S, methyl mercaptan, beacon, horn, ESD pushbutton, and local unit shutdown interfaces.
   - Mark final detector quantity, detector coverage, additional outdoor detection, specific methyl mercaptan locations, and large-module ESD pushbutton locations as `TBD` where detailed engineering is required.
   - Source: DBM-Deepcut SEC-14 Instrumented Protection Basis.

9. Compile the turnover package.
   - Include inspection status, interface completion status, open `TBD` items, owner for each unresolved item, and evidence links for source-supported requirements.
   - Do not close the CWP while unresolved `TBD` or Human Ruling Required items lack owner/disposition.

## Verification

- Confirm all required artifacts exist: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
- Confirm every Gate 7 PKG-008 interface type appears in the construction interface matrix or is explicitly marked not applicable with source support.
- Confirm cable/raceway checks cite DBM-Deepcut SEC-12.
- Confirm controls topology, layout, network, hardware, Modbus, and open detailed-design items cite DBM-Deepcut SEC-13.
- Confirm fire/gas/alarm/ESD/unit-shutdown checks cite DBM-Deepcut SEC-14.
- Confirm no dependency blocker is introduced without a declared dependency edge in `_DEPENDENCIES.md`.
- Confirm unresolved detailed-design items are marked `TBD` and Human Ruling Required items are listed in Guidance.md and the run record.

## Records

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface matrix.
- Construction interface and turnover checklist.
- Inspection checklists for controls equipment placement, network/communications, Modbus/package controls, cable/raceway, and fire/gas/alarm/ESD interfaces.
- `TBD` and open-item register.
- Human ruling log for HRR-001 and any later conflicts.
