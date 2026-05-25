# Procedure: DEL-037-04_vendor-engineered-equipment-package

## Purpose

This procedure defines the working sequence for producing and checking the **Vendor Engineered Equipment Package** for `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`.

The procedure covers vendor package engineering, package design, fabrication / supply readiness, and preparation of the vendor package design basis and datasheet set. It does not replace EPC Integrator review and acceptance under `DEL-037-06`.

## Prerequisites

1. Accepted upstream decomposition truth:
   - Gate 7 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
2. Required EPC inputs:
   - `DEL-037-01_scope-of-work` — EPC Scope of Work.
   - `DEL-037-02_package-datasheet` — EPC Package Datasheet.
3. Source basis:
   - `_CONTEXT.md` for deliverable identity and scope.
   - `PACKAGE_REGISTER.csv` row `PKG-037` for ownership, scope, interfaces, and package basis.
   - `DELIVERABLE_REGISTER.csv` row `DEL-037-04_vendor-engineered-equipment-package` for deliverable definition.
   - `ARTIFACT_REGISTER.csv` rows `ART-7491C7E69C` and `ART-8870C8E2DE` for expected vendor artifacts.
   - `INTERFACE_REGISTER.csv` rows for `PKG-037` for applicable interface types.
   - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` source slices for electrical buildings, medium-voltage services, UPS services, grounding and bonding, cable tray, conduit, and medium-voltage cables.
4. Declared dependencies:
   - No upstream or downstream dependencies were declared during PREPARATION in `_DEPENDENCIES.md`.
5. Human rulings required before final vendor design closure:
   - Confirm whether the workbook "5kV" package label maps to a specific facility service voltage or only to equipment insulation class / package title.

## Steps

### 1. Confirm Package Identity and Boundary

1. Confirm the deliverable ID is `DEL-037-04_vendor-engineered-equipment-package`.
2. Confirm the parent package is `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`.
3. Confirm the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.
4. Confirm the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration.
5. Record any mismatch between vendor assumptions and the Gate 7 package basis as a review comment for EPC Integrator disposition.

### 2. Establish Electrical Design Basis

1. Use the DBM electrical buildings paragraph as the source basis for prefabricated, modular electrical-building expectations.
2. Identify the equipment subset required for building 880-1 from the EPC Package Datasheet and detailed design inputs.
3. Record all unavailable package-specific values as `TBD`, including bus rating, breaker count, breaker frame, relay scheme, control voltage, HVAC load, building location, module footprint, module weight, and foundation reactions.
4. Use the DBM medium-voltage service table as the general facility voltage basis, but do not treat "5kV" as a confirmed service voltage until ruled by EPC or vendor design authority.
5. Identify any stricter or more specific vendor / unit requirement and route it for precedence review, consistent with the DBM source precedence statement.

### 3. Develop Vendor Package Design Basis

1. Prepare a vendor package design basis document covering:
   - package identity and scope;
   - design inputs from `DEL-037-01` and `DEL-037-02`;
   - applicable electrical-building basis;
   - medium-voltage service and cable assumptions;
   - UPS and control-power assumptions;
   - grounding and bonding basis;
   - interface basis for all twelve `PKG-037` interface types;
   - open `TBD` items and human rulings.
2. Prepare a vendor equipment datasheet set covering:
   - building enclosure;
   - switchgear lineup;
   - auxiliary / ancillary electrical equipment;
   - control power, protective relaying, and communications interfaces;
   - grounding and cable termination interfaces;
   - HVAC, lighting, fire and gas, drainage / containment, and structural / foundation interfaces where applicable.
3. Tie each non-trivial design value to an accessible source or identify it as `TBD` / **ASSUMPTION**.

### 4. Develop Physical Equipment Package

1. Engineer the prefabricated modular electrical building arrangement consistent with the DBM electrical-building basis.
2. Coordinate bottom-entry power cable requirements, building elevation, and pile / under-building cable space with the EPC Integrator.
3. Confirm equipment doors or removable sections support removal of the largest equipment.
4. Confirm cable tray and conduit routing do not interfere with maintenance access.
5. Confirm major electrical equipment grounding and bonding provisions, including two-point ground grid connections where applicable.
6. Confirm UPS-fed breaker control circuits and protective relays where required by detailed design.
7. Confirm medium-voltage cable terminations match the DBM cable basis for the confirmed service voltage.

### 5. Coordinate Interfaces

1. Build an interface requirements matrix for all twelve `PKG-037` interface types:
   - Utility Piping
   - Drain / Containment
   - Electrical Power
   - Grounding / Bonding
   - Area / Exterior Lighting
   - I&C / Control Cabling
   - Communications / Network
   - Building HVAC / Services
   - Fire & Gas / Safety Systems
   - Maintenance Access
   - Grading / Site Drainage / Spill Containment
   - Structural / Foundations / Supports
2. For each interface, identify vendor-side data to be issued to the EPC Integrator.
3. For each interface, identify EPC-side data required by the vendor.
4. Mark missing EPC-side or vendor-side interface data as `TBD`.

### 6. Prepare Review Package

1. Assemble the vendor engineered physical equipment package evidence for `ART-7491C7E69C`.
2. Assemble the vendor package design basis and datasheet set for `ART-8870C8E2DE`.
3. Include a register of `TBD`, **ASSUMPTION**, and conflict items.
4. Submit the package for EPC Integrator review under `DEL-037-06`.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | Deliverable, package ID, workbook row, WBS, discipline, and CoA tracking number match `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row `PKG-037`. |
| Scope check | Vendor package covers engineering, design, fabrication / supply, and the physical package; EPC integration work remains outside this deliverable. |
| Source-grounding check | Non-trivial requirements cite Gate 7 registers or accessible DBM source slices; unsupported values are `TBD` or **ASSUMPTION**. |
| Electrical building check | Building arrangement aligns with the DBM electrical buildings paragraph for prefabricated modular buildings, general-purpose areas, bottom-entry cables, equipment access, and building wiring basis where applicable. |
| Medium-voltage basis check | Voltage mapping is either confirmed by EPC / vendor source or remains explicitly unresolved. |
| Interface check | All twelve `PKG-037` interface types are represented in the interface requirements matrix. |
| Grounding / bonding check | Major equipment grounding and building ground-well requirements are addressed where applicable. |
| Cable / raceway check | Medium-voltage cable basis, tray routing, conduit routing, and maintenance access requirements are addressed. |
| Documentation check | `ART-7491C7E69C` and `ART-8870C8E2DE` evidence is present and ready for EPC Integrator review. |

## Records

Maintain the following records in the vendor package file and turnover path:

- Vendor engineered physical equipment package (`ART-7491C7E69C`).
- Vendor package design basis and datasheet set (`ART-8870C8E2DE`).
- Interface requirements matrix covering all twelve `PKG-037` interface facts.
- Open item register for `TBD`, **ASSUMPTION**, and conflict items.
- EPC Integrator review comments and dispositions under `DEL-037-06`.
- Factory / shop test and inspection evidence where required by detailed vendor scope.
