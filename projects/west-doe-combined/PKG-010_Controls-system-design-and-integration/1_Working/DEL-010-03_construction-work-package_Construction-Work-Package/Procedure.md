# Procedure: DEL-010-03 Construction Work Package

## Purpose

Define the working procedure to produce and use the `PKG-010 - Controls system design and integration` Construction Work Package for construction planning, installation, tie-in, inspection, and turnover.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Accessible source materials include the Gate 7 registers, workbook packages/interfaces export, and relevant DBM controls/construction sections.
- Declared upstream dependencies: none as of PREPARATION.
- Declared downstream dependencies: none as of PREPARATION.
- Detailed project construction procedures, inspection forms, and turnover dossier templates: TBD.

## Steps

1. Confirm package identity.
   - Verify package `PKG-010`, WBS `03`, CoA tracking number `26020-01-32-001`, package name `Controls system design and integration`, discipline `Controls`, and responsible party `EPC Integrator`.
   - Source: PACKAGE_REGISTER.csv, PKG-010.

2. Confirm CWP artifact set.
   - Include construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Source: DELIVERABLE_REGISTER.csv and ARTIFACT_REGISTER.csv, DEL-010-03.

3. Build the construction interface matrix.
   - Include the PKG-010 applicable interface types: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems.
   - Source: INTERFACE_REGISTER.csv, PKG-010; 26020-Packages_Interfaces_4_export.xlsx, Packages sheet, workbook row 11.

4. Develop the workface plan.
   - Address installation/building of the package and connection to applicable adjacent process, utility, electrical, controls, civil/structural, and safety systems.
   - Mark detailed work sequence, crew packaging, hold points, permits, and construction constraints as TBD until project execution procedures and IFC drawings are available.

5. Incorporate controls-system constraints.
   - Preserve BPCS and standalone Unit Control System boundaries.
   - Preserve Modbus monitoring-only restriction.
   - Include remote I/O, network, communications, and control cabling installation/checkout hooks where in scope.
   - Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13.

6. Incorporate safety-system and shutdown interface constraints.
   - Include fire/gas, H2S, LEL, methyl mercaptan, ESD, and unit shutdown interface coordination with BPCS, Remote I/O, package controls, electrical area classification, and HAZOP/SIL outcomes.
   - Keep final alarm philosophy, horn tone mapping, beacon layout, operator notification logic, trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities open until detailed-design evidence is available.
   - Source: 3-25_Comp_and_Liquids_DBM.md, SEC-14.

7. Prepare inspection and turnover checks.
   - Check each applicable interface for construction completion, inspection status, test/checkout evidence, open items, and turnover owner.
   - Include controls/network/RIO checkout records, safety-system interface verification, and open-item register.
   - Use project inspection and turnover forms when available; otherwise mark template references as TBD.

8. Run cross-document consistency review.
   - Confirm Datasheet attributes appear in Specification requirements where appropriate.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance conflict/human-ruling items are not silently treated as closed.

## Verification

| Check | Pass condition |
|---|---|
| Identity check | CWP identifies DEL-010-03 and PKG-010 consistently with Gate 7 registers. |
| Artifact check | Required CWP, workface plan, and interface/turnover checklist are present or explicitly listed as required outputs. |
| Interface check | All eight applicable interface types are listed or dispositioned. |
| Controls boundary check | BPCS, Unit Control System, Modbus, RIO, fire/gas, and shutdown constraints are preserved. |
| TBD/open-item check | Unsupported construction sequence, inspection, alarm/shutdown, and turnover details remain TBD or open. |
| Human ruling check | HRR-010-03-001 remains visible until resolved by human ruling. |

## Records

- Construction Work Package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Interface matrix for PKG-010.
- Controls/network/RIO installation and checkout records.
- Fire/gas and shutdown interface verification records.
- Open-item and human-ruling register entries.
