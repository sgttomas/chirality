# Procedure: DEL-009-04 EPC / Controls Discipline Production Package

## Purpose

Define the working procedure to produce and verify the EPC / Controls Discipline Production Package for `PKG-009 - Controls system design and integration`, WBS 02, using the accepted Gate 7 snapshot and locally accessible controls source material.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Packages workbook is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- DBM controls/electrical/protection source slices are available in:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity.
   Verify DEL-009-04, PKG-009, WBS 02, SOW-0009, discipline Controls, and type EPC/Discipline Production Unit against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.

2. Confirm workbook package row.
   Use `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9, to confirm CoA tracking number 26020-01-32-001, package name, WBS, discipline, interface category flags, and the interface review note.

3. Build the controls interface matrix.
   Include the workbook-flagged categories: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems.

4. Establish controls architecture requirements.
   Extract BPCS, PCN, I/O Network, IDMZ, server, virtualization, BPCS controller, RIO, Unit Control System, package interface, and Modbus requirements from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-13 - Control System Basis`.

5. Establish electrical/control coordination requirements.
   Extract UPS service, area classification controls interfaces, power/control circuit separation, and instrument-air electrical/controls interface requirements from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical basis sections.

6. Establish protection-interface requirements.
   Extract fire detection, LEL, H2S, methyl mercaptan, audible/visual alarm, ESD pushbutton, and local unit shutdown interface requirements from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, instrumented protection sections.

7. Record open detailed-design items.
   Carry unresolved items as `TBD`, including RIO cabinet locations, controller sizing, DLR/PRP selection where not fixed by WBS 02 source material, historian product, IDMZ layout, policies, firewall rules, IP addressing, VLAN segmentation, and controls power-panel interface tracking.

8. Produce the discipline deliverable register.
   Populate source-supported controls deliverables and mark unresolved deliverable membership as `TBD` where Gate 7 and accessible sources do not define it.

9. Produce the source-limited requirements closure record.
   Map each requirement to its cited source section, verification approach, current status, and unresolved human-ruling or detailed-design item.

10. Perform cross-document consistency checks.
    Confirm that terms, values, source citations, TBDs, and human-ruling items match across Datasheet, Specification, Guidance, and Procedure.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | DEL-009-04, PKG-009, WBS 02, SOW-0009, and CoA tracking number 26020-01-32-001 are consistent across documents. |
| Source check | Non-trivial requirements cite accessible source files and section references or are marked `TBD`/`ASSUMPTION`. |
| Interface check | Workbook row `ID #` 9 interface flags are represented in the package documentation. |
| Controls architecture check | BPCS, network, server, RIO, package interface, Modbus, instrument-air, and protection-interface requirements align with cited DBM source slices. |
| Open-items check | Controls power-panel interface tracking and PRP/DLR applicability remain visible as human-ruling/open design-development items. |
| Dependency check | No blockers are asserted because no declared upstream or downstream dependencies exist in `_DEPENDENCIES.md`. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- Discipline deliverable register: TBD production artifact.
- Source-limited requirements closure record: TBD production artifact.
- Interface category matrix for Packages workbook row `ID #` 9.
- Human ruling log containing HRR-001 and HRR-002 until resolved.
