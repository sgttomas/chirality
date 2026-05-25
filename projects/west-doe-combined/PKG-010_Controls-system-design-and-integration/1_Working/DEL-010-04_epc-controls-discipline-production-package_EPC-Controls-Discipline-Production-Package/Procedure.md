# Procedure: EPC / Controls Discipline Production Package

## Purpose

Define the steps to produce and verify the controls discipline production package for `DEL-010-04_epc-controls-discipline-production-package` using the accepted Gate 7 decomposition snapshot and accessible controls source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Accessible source/register set:
  - DELIVERABLE_REGISTER.csv
  - PACKAGE_REGISTER.csv
  - SCOPE_LEDGER.csv
  - ARTIFACT_REGISTER.csv
  - INTERFACE_REGISTER.csv
  - OBJECTIVE_DELIVERABLE_MAP.csv
  - 3-25_Comp_and_Liquids_DBM.md, especially SEC-13 Control System Basis.
- Declared upstream dependencies: none declared during PREPARATION.
- Human ruling required for responsible-party assignment and detailed discipline deliverable register content.

## Steps

1. Confirm package identity.
   - Verify `PKG-010`, Workbook row 11, WBS 03, discipline Controls, and package name against PACKAGE_REGISTER.csv.
   - Verify `SOW-0010` against SCOPE_LEDGER.csv.

2. Confirm deliverable identity.
   - Verify `DEL-010-04_epc-controls-discipline-production-package`, type, responsible party, anticipated artifacts, and supported objectives against DELIVERABLE_REGISTER.csv.
   - Preserve responsible party as `TBD; EPC Integrator or discipline subcontractor as assigned` until human assignment is accepted.

3. Establish the controls production basis.
   - Use DBM SEC-13 to identify BPCS, RIO, network, package-interface, Modbus, instrument-air, and safety-device wiring requirements.
   - Mark final topology, sizing, data maps, alarm priorities, permissives, trip interfaces, firewall rules, VLANs, IP addressing, cause-and-effect actions, and reset responsibilities as TBD where final design evidence is not present.

4. Build the package interface matrix.
   - Include Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems from INTERFACE_REGISTER.csv.
   - Preserve the Gate 6 disposition that controls power-panel issues remain package datasheet interface facts/artifacts unless a later approved decomposition change says otherwise.

5. Prepare the source-limited requirements closure record.
   - List each requirement that can be grounded in the Gate 7 registers or DBM SEC-13.
   - List each unresolved detailed requirement as TBD with source/location and needed disposition.
   - Include HRR-010-04-001 through HRR-010-04-003 from Guidance.md until ruled.

6. Assemble the discipline production package.
   - Include the discipline production package basis.
   - Include or reference the source-limited requirements closure record.
   - Include the TBD discipline deliverable register placeholder.
   - Include source references and verification traceability.

7. Perform cross-document consistency checks.
   - Confirm Datasheet attributes align with Specification requirements.
   - Confirm Specification requirements have verification hooks in this Procedure.
   - Confirm Guidance does not overstate source authority and keeps unresolved items in the Conflict Table.
   - Confirm terms match across package identity, BPCS, Remote I/O, Unit Control Systems, Modbus, and interface types.

## Verification

| Check | Acceptance criterion |
|---|---|
| Package identity | PKG-010, WBS 03, Workbook row 11, and package name match Gate 7 registers. |
| Deliverable identity | DEL-010-04 metadata matches deliverable-local context and DELIVERABLE_REGISTER.csv. |
| Source grounding | Non-trivial controls claims cite Gate 7 registers or 3-25_Comp_and_Liquids_DBM.md source sections. |
| Requirements trace | Each Specification requirement has a verification approach or is marked TBD/needs human ruling. |
| Interface trace | Interface matrix matches INTERFACE_REGISTER.csv rows for PKG-010. |
| Closure record | Responsible-party assignment, detailed discipline deliverable register, and detailed requirements remain open until human/source disposition. |

## Records

- Discipline production package basis.
- Source-limited requirements closure record.
- TBD discipline deliverable register.
- PKG-010 interface matrix.
- Cross-document consistency check record.
- Human ruling log for HRR-010-04-001 through HRR-010-04-003.
