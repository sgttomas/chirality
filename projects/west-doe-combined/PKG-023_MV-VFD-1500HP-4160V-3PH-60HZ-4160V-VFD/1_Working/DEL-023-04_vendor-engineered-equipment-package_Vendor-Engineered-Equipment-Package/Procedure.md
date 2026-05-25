# Procedure: DEL-023-04_vendor-engineered-equipment-package

## Purpose

Produce the Vendor Engineered Equipment Package for `PKG-023` — `MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD`: vendor engineering, design, fabrication/supply, and physical equipment, together with the vendor package design basis and datasheet set. This Procedure covers production of the deliverable artifacts; package commissioning and acceptance are handled separately under `DEL-023-06`.

## Prerequisites

- Accepted upstream EPC Scope of Work for `PKG-023` (`DEL-023-01`) — required for vendor scope authority. Currently `TBD` in this workspace; not declared as a dependency in `_DEPENDENCIES.md`.
- Accepted upstream EPC Package Datasheet for `PKG-023` (`DEL-023-02`) — required for technical handoff. Currently `TBD` in this workspace; not declared as a dependency in `_DEPENDENCIES.md`.
- Access to the Project Design Basis Manual electrical sections (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- Access to `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx` for project package-level requirements.
- Identified Package Vendor with engineering, design, and fabrication capability for a 4.16 kV class MV-VFD package.
- Established interface contract for the six declared `PKG-023` interfaces (`INTERFACE_REGISTER.csv` rows for `PKG-023`).

## Steps

1. **Receive and read the EPC handoff package.** Read `DEL-023-01` (Scope of Work) and `DEL-023-02` (Package Datasheet) for `PKG-023`. Confirm the package boundary, driven-service identity, supply-side bus assignment, environmental conditions, and required interfaces.
2. **Compile the vendor design basis.** Capture all governing inputs in a single vendor design basis: workbook identity (row 25), EPC handoff requirements, applicable DBM clauses (medium-voltage MCC/VFD/MV-soft-starter, Zone 2 marking, electrical buildings, grounding, cable type), and CEC sizing rules. Flag every `TBD` from the Datasheet/Specification as an open vendor item.
3. **Resolve open technical items against source.** For each `TBD` (drive topology, harmonic mitigation, cooling method, enclosure rating, supply-side bus, MV VFD-fed motor cable type), obtain a source-supported answer from the EPC Package Datasheet or from accepted vendor source data; if unavailable, escalate as a human-ruling item.
4. **Engineer the package.** Produce vendor electrical, mechanical, control, and structural engineering: single-line diagram, control philosophy, harmonic study, thermal study, enclosure and area-classification compliance, grounding scheme, lifting/anchorage plan.
5. **Produce the vendor datasheet set.** Build the vendor's own datasheet set for the VFD, transformer (if applicable), control panel, and ancillaries. Cross-check against the EPC Package Datasheet.
6. **Confirm the package interface contract.** For each declared `PKG-023` interface, document the package-side termination, sizing, and EPC-side requirement. Cross-check against `INTERFACE_REGISTER.csv`.
7. **Fabricate and factory-test the package.** Execute factory acceptance per the vendor design basis and EPC requirements. Record factory test results.
8. **Prepare the physical equipment package for delivery.** Apply Zone 2 marking and temperature coding (where applicable per the area-classification drawing), confirm grounding lugs, and confirm communication-port provision aligned with the EPC Package Datasheet.
9. **Hand off the deliverable artifacts.** Submit (a) the vendor engineered physical equipment package (`ART-21EF7BEFD2`) and (b) the vendor package design basis and datasheet set (`ART-B3660C159F`) for EPC Integrator integration review. Submittal documentation control flows through `DEL-023-05`; integration acceptance flows through `DEL-023-06`.

## Verification

| Check | Method |
|---|---|
| Vendor design basis aligns with EPC Scope of Work and EPC Package Datasheet. | Review by EPC Integrator under `DEL-023-06`. |
| Drive ratings consistent with workbook identity (4160 V class, nominal 1500 HP, 3-phase, 60 Hz) and the accepted EPC Package Datasheet. | Datasheet comparison. |
| Every `PKG-023` interface row has a documented package-side termination. | Interface-matrix audit against `INTERFACE_REGISTER.csv` rows for `PKG-023`. |
| Grounding scheme complies with DBM grounding rules (two-point connection; separate copper ground per CEC where applicable). | Grounding design review. |
| Zone 2 marking and temperature code conform to the area-classification drawing where any package component or VFD-fed motor is in a Zone 2 area. | Area-classification compliance review. |
| Cable types coordinated with DBM cable type basis; MV VFD-fed motor cable type resolved. | Cable schedule review. |
| Factory acceptance test passed. | FAT report review. |
| Documentation submitted complete. | Submittal completeness check (handled via `DEL-023-05`). |

## Records

- Vendor package design basis document.
- Vendor datasheet set (drive, transformer if present, control panel, ancillaries).
- Harmonic study, thermal study, grounding study (where applicable).
- Package single-line diagram and control philosophy.
- Interface-matrix record for the six `PKG-023` interfaces.
- Factory acceptance test report.
- Equipment-marking and area-classification compliance record.
- Issued/accepted artifact records:
  - `ART-21EF7BEFD2` — Vendor engineered physical equipment package.
  - `ART-B3660C159F` — Vendor package design basis and datasheet set.
