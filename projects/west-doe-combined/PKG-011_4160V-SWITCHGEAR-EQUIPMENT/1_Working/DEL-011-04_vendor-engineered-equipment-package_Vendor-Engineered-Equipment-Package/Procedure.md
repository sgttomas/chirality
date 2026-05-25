# Procedure: DEL-011-04_vendor-engineered-equipment-package

## Purpose

Define the bounded procedure for producing and checking the Vendor Engineered Equipment Package for DEL-011-04, using accepted Gate 7 decomposition truth and locally accessible source slices.

## Prerequisites

- Accepted upstream decomposition snapshot: Gate 7 Final Published 2026-05-24.
- Deliverable context files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Accessible source basis:
  - Gate 7 `PACKAGE_REGISTER.csv`
  - Gate 7 `DELIVERABLE_REGISTER.csv`
  - Gate 7 `ARTIFACT_REGISTER.csv`
  - Gate 7 `INTERFACE_REGISTER.csv`
  - Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity.
   - Verify `DEL-011-04_vendor-engineered-equipment-package`, parent `PKG-011`, package name `4160V SWITCHGEAR EQUIPMENT`, discipline Electrical, and responsible party from `_CONTEXT.md` and Gate 7 registers.

2. Confirm source basis.
   - Use the Gate 7 registers and DBM SEC-12 electrical basis as the accepted source set for Phase 2.2.
   - Do not reinterpret raw source corpus or sibling deliverables.
   - Mark missing vendor-specific information as `TBD`.

3. Establish vendor package scope.
   - Include vendor engineering, design, fabrication/supply, physical equipment package, vendor package design basis, and vendor datasheet set.
   - Preserve EPC Integrator integration review for facility-level interfaces and acceptance.

4. Establish electrical basis for vendor design.
   - Carry forward 4,160 V, 3 phase, 3 wire, 60 Hz LRG medium-voltage service.
   - Carry forward 13.8 kV to 4.16 kV, 12 MVA transformer service to the 4160V MCC for 4000V motors.
   - Carry forward 4160V MCC functions: field-fused contactors, motor protection relays, and EtherNet communication port to the plant PLC central control panel for data acquisition.

5. Establish motor/starter basis.
   - Include large 4000V motors identified in source, including KM-2150 and KM-2250.
   - Require starting VFDs for KM-2150 and KM-2250 under the current basis.
   - Do not use soft starts for those inlet compressor motors unless a later accepted design ruling supersedes the current basis.

6. Establish interface requirements.
   - Include Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
   - Coordinate raceway separation, grounding, bonding, and controls/network interfaces with project electrical specifications and detailed design.

7. Identify unresolved items.
   - Keep harmonic and reactive-power mitigation open pending detailed electrical studies.
   - Keep vendor-specific ratings, layouts, protection settings, dimensions, inspection/test plans, and turnover details open as `TBD` where no accepted source establishes them.
   - Surface nomenclature uncertainty between "4160V SWITCHGEAR EQUIPMENT" and DBM "4160V MCC" for human ruling.

8. Package the vendor engineering output for EPC review.
   - Provide the vendor engineered physical equipment package.
   - Provide the vendor package design basis and datasheet set.
   - Provide interface data required for EPC Integrator review.
   - Preserve traceability to accepted Gate 7 and DBM source slices.

## Verification

- Check that all four documents use the same deliverable ID, package ID, package name, discipline, and responsible party.
- Check that values match source: 4,160 V; 3 phase; 3 wire; 60 Hz LRG; 13.8 kV to 4.16 kV; 12 MVA; KM-2150; KM-2250.
- Check that requirements in `Specification.md` have corresponding verification hooks in this procedure.
- Check that `Guidance.md` contains human-ruling items for unresolved conflicts rather than silently resolving unsupported details.
- Check that no declared dependency blockers exist in `_DEPENDENCIES.md`.

## Records

- Vendor engineered physical equipment package.
- Vendor package design basis.
- Vendor datasheet set.
- Interface review data for the six Gate 7 interface types.
- EPC Integrator review comments and dispositions: TBD, expected in later review/acceptance workflow.
- Detailed electrical studies for harmonic and reactive-power mitigation: TBD.
- Human rulings for HRR-011-04-001 and HRR-011-04-002.
