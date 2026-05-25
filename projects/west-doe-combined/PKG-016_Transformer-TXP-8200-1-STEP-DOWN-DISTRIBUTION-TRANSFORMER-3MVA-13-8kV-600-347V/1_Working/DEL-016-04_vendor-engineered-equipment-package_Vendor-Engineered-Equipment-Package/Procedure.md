# Procedure: DEL-016-04_vendor-engineered-equipment-package

## Purpose

Define the bounded procedure for producing and checking the Vendor Engineered Equipment Package for DEL-016-04, using accepted Gate 7 decomposition truth and locally accessible source slices, for the PKG-016 Transformer TXP-8200-1 (3 MVA, 13.8 kV / 600 / 347 V).

## Prerequisites

- Accepted upstream decomposition snapshot: Gate 7 Final Published 2026-05-24.
- Deliverable context files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Accessible source basis:
  - Gate 7 `PACKAGE_REGISTER.csv`
  - Gate 7 `DELIVERABLE_REGISTER.csv`
  - Gate 7 `ARTIFACT_REGISTER.csv`
  - Gate 7 `INTERFACE_REGISTER.csv`
  - Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical basis (System Voltages; Incoming Power and Transformers; 600V MCC and Standby Power; Electrical Buildings, Raceways, Lighting, and Heat Tracing; Area Classification; grounding/bonding; cable tray/conduit)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 18
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity.
   - Verify `DEL-016-04_vendor-engineered-equipment-package`, parent `PKG-016`, package name `Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V`, discipline Electrical, and responsible party from `_CONTEXT.md` and Gate 7 registers.

2. Confirm source basis.
   - Use the Gate 7 registers and DBM electrical basis as the accepted source set for Phase 2.2.
   - Do not reinterpret raw source corpus or sibling deliverables.
   - Mark missing vendor-specific information as `TBD`.

3. Establish vendor package scope.
   - Include vendor engineering, design, fabrication/supply, physical equipment package, vendor package design basis, and vendor datasheet set.
   - Preserve EPC Integrator integration review for facility-level interfaces and acceptance.

4. Establish electrical basis for vendor design.
   - Carry forward 13.8 kV, 3 phase, 3 wire, 60 Hz LRG primary supply sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building.
   - Carry forward the DBM "13.8 kV to 600 V, 3 MVA transformer" basis that feeds the 600 V MCC for LV loads.
   - Carry forward 600 V, 3 phase, 3 wire, 60 Hz HRG with a 5 A continuous resistor as the LV secondary service basis.
   - Treat the 347 V service portion of the package name as not source-established; carry it as `ASSUMPTION` (line-to-neutral of a 600 V wye) and mark `TBD` until confirmed.

5. Establish interface requirements.
   - Include all seven Gate 7 PKG-016 interface facts: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
   - Coordinate ground-grid two-point connection, separate copper ground conductors for the distribution transformer per CEC sizing, raceway separation between 13.8 kV / 600 V power and control/instrument circuits, and cable/conduit routing that preserves maintenance access.
   - Require vendor transformer loading data sufficient for EPC foundation/support design (including oil-containment data if the vendor selects a liquid-filled design).

6. Identify unresolved items.
   - Keep cooling class, insulating medium (liquid-filled vs. dry-type), winding configuration / vector group, impedance, BIL, tap-changer configuration, bushing class, protective accessories, factory test scope, site environmental basis, and hazardous-area classification applicability open as `TBD` where no accepted source establishes them.
   - Keep the 347 V service definition open as `TBD` per HRR-016-04-001.
   - Keep vendor document register, inspection/test plan, and turnover detail open in DEL-016-04 and defer to DEL-016-05 / DEL-016-06 unless human rules otherwise.

7. Package the vendor engineering output for EPC review.
   - Provide the vendor engineered physical equipment package (`ART-AC4469EC25`).
   - Provide the vendor package design basis and datasheet set (`ART-13F6F3D6B6`).
   - Provide interface data required for EPC Integrator review.
   - Preserve traceability to accepted Gate 7 and DBM source slices.

8. Cross-document consistency and human-ruling sweep.
   - Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, ratings, interface set, and `TBD` items.
   - Surface 347 V service definition, insulating medium / cooling class, and vendor test/turnover detail as `NEEDS_HUMAN_RULING` items.

9. Status update.
   - After successful Pass 1 / Pass 2, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

- Check that all four documents use the same deliverable ID, package ID, package name, discipline, and responsible party.
- Check that values match source: 13.8 kV; 600 V; 3 MVA; 3 phase, 3 wire, 60 Hz; LRG primary; HRG 600 V with 5 A continuous resistor; "13.8 kV to 600 V, 3 MVA transformer" feeding the 600 V MCC.
- Check that requirements in `Specification.md` have corresponding verification hooks in this procedure.
- Check that `Guidance.md` contains human-ruling items for unresolved conflicts rather than silently resolving unsupported details (347 V, insulating medium / cooling class, vendor test/turnover detail).
- Check that no declared dependency blockers exist in `_DEPENDENCIES.md`.

## Records

- Vendor engineered physical equipment package (`ART-AC4469EC25`).
- Vendor package design basis and datasheet set (`ART-13F6F3D6B6`).
- Interface review data for the seven Gate 7 PKG-016 interface types.
- EPC Integrator review comments and dispositions: TBD, expected in DEL-016-06 (EPC Vendor Package Review and Acceptance).
- Detailed electrical studies (short-circuit, coordination, harmonic, grounding) affecting the 13.8 kV / 600 V interface: TBD.
- Human rulings for HRR-016-04-001, HRR-016-04-002, and HRR-016-04-003.
