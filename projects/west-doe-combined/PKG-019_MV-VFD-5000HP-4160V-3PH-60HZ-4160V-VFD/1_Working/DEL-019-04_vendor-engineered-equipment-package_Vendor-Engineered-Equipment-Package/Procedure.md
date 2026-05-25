# Procedure — DEL-019-04 Vendor Engineered Equipment Package

Operational procedure for producing, verifying, and turning over the vendor-engineered MV VFD equipment package under PKG-019.

## Purpose

Define the steps by which the Package Vendor produces the engineered MV VFD equipment package — engineering, design, fabrication/supply, and the physical equipment — from the EPC anchor inputs (`DEL-019-01_scope-of-work`, `DEL-019-02_package-datasheet`), and the verification and record steps required to support downstream EPC review and acceptance (`DEL-019-06`).

## Prerequisites

- Accepted EPC Scope of Work for PKG-019 (`DEL-019-01_scope-of-work`).
- Accepted EPC Package Datasheet for PKG-019 (`DEL-019-02_package-datasheet`).
- Available design-basis source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections cited in `Datasheet.md` References).
- Resolution of Conflict-Table item HRR-019-04-001 (motor basis vs. workbook title) before vendor design freeze.
- Identified application: starting VFD service for inlet compressor motors `KM-2150` and `KM-2250` (DBM §326, §756).
- Declared upstream/downstream dependencies: none declared at deliverable scope (see `_DEPENDENCIES.md`). Effective upstream inputs are the EPC anchor deliverables above and the DBM; downstream consumers are `DEL-019-05` and `DEL-019-06`.

## Steps

1. **Confirm inputs and basis.**
   - Verify the EPC Scope of Work and Package Datasheet are accepted and current.
   - Verify the application and driven-motor basis (`KM-2150`, `KM-2250`; 4,000 V, 60 Hz, 5,200 HP / 3,878 kW, NEMA MG1, Class F / Class B, ~891 rpm, continuous inverter-duty) against the DBM (`§324`, `§523`, `§533`).
   - Confirm resolution of HRR-019-04-001 (workbook title vs. motor basis).
2. **Develop vendor package design basis.**
   - Translate the EPC inputs into the vendor package design basis document.
   - Capture the starting-VFD authority (SCA-001 VE #34) and the no-soft-start constraint.
   - Capture line-side interface to the 4160V MCC and EtherNet path to the plant PLC central control panel (DBM §752, §754).
   - Capture the package-level interface types declared for PKG-019.
3. **Perform VFD sizing and topology selection.**
   - Execute VFD sizing per detailed electrical-design conventions, substantiated against the accepted motor and load data (DBM §326).
   - Select drive topology consistent with the harmonic / reactive-power treatment derived from detailed electrical studies (DBM §756). `TBD` until study outputs are accepted.
4. **Produce vendor datasheet set.**
   - Issue the vendor package datasheet(s) covering the engineered equipment, controls, communications, interfaces, and ancillaries.
   - Cross-reference each datasheet entry to the EPC Package Datasheet line items.
5. **Engineer and design the physical equipment package.**
   - Develop electrical, control, mechanical, and structural design as required for the engineered equipment package.
   - Provide engineering provisions for each PKG-019 InterfaceType (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
6. **Fabricate / supply the physical equipment package.**
   - Procure components and fabricate / assemble the vendor-supplied equipment package per the accepted design.
   - Maintain production records suitable for vendor document turnover (handed off to `DEL-019-05`).
7. **Vendor verification / FAT.**
   - Execute vendor factory verification (FAT) appropriate to a starting MV VFD package, including (where applicable) functional, dielectric, control, and communications checks.
   - Record FAT evidence for inclusion in the turnover package.
8. **Handoff to vendor document turnover and EPC review.**
   - Provide the vendor package design basis, datasheet set, and FAT records to `DEL-019-05_vendor-document-turnover-package`.
   - Provide the engineered equipment package and supporting documentation to `DEL-019-06_epc-vendor-package-review-and-acceptance` for EPC review and integration acceptance.

## Verification

- **Design verification.** Confirm vendor design satisfies REQ-019-04-01 through REQ-019-04-10 (`Specification.md`).
- **Interface verification.** Confirm engineering provisions for each PKG-019 InterfaceType are present in the vendor design (REQ-019-04-07).
- **Communications verification.** Confirm EtherNet communications path to the plant PLC central control panel via the 4160V MCC is supported (REQ-019-04-06).
- **Standards verification.** Confirm NEMA MG1 motor compatibility and applicable adjustable-speed-drive standards (IEEE 519, IEC 61800-series — `location TBD` until reference availability is confirmed).
- **Conflict-Table verification.** Confirm HRR-019-04-001 has a human ruling and that the resolved motor basis is reflected in vendor design (REQ-019-04-11).
- **Soft-start prohibition.** Confirm no soft-start substitution (REQ-019-04-05).

## Records

- Vendor package design basis document.
- Vendor package datasheet set.
- VFD sizing calculations and supporting analysis.
- Harmonic / reactive-power input acceptance record (from detailed electrical studies).
- Factory acceptance test (FAT) records.
- Bill of materials and as-built records for the physical equipment package.
- Interface compliance evidence for the six PKG-019 InterfaceTypes.
- Reference: Conflict Table dispositions captured in `Guidance.md`.
