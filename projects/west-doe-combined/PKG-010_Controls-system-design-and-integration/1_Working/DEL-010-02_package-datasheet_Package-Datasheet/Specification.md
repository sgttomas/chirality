# Specification: DEL-010-02_package-datasheet — Package Datasheet

## Scope

This specification governs the content and acceptance basis for the EPC Integrator's Controls system design and integration package datasheet for `PKG-010`.

The datasheet covers:

- Package identity, discipline, responsibility, and accepted Gate 7 decomposition references.
- Technical handoff data required for third-party vendor or discipline package engineering and design.
- Package interface requirements matrix for the controls package.
- Source-supported controls architecture, network, electrical, instrumentation, fire/gas, safety, HVAC/services, and process/utility/relief interface facts.
- `TBD` fields where detailed design, vendor integration, safety studies, or client IT/OT coordination are required.

The datasheet does not create a separate controls power-panel package or separate power-panel deliverable. Gate 7 disposition keeps those interface facts/artifacts under this package datasheet.

## Requirements

| ID | Requirement | Verification | Source |
|---|---|---|---|
| REQ-010-02-001 | The datasheet shall identify `DEL-010-02_package-datasheet`, `PKG-010`, the package name "Controls system design and integration", discipline "Controls", type "EPC Package Datasheet", and responsible party "EPC Integrator". | Confirm fields against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| REQ-010-02-002 | The datasheet shall include the required artifact set: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and source-supported equipment/design criteria. | Confirm artifact list against Gate 7 rows for `DEL-010-02_package-datasheet`. | Gate 7 `ARTIFACT_REGISTER.csv` rows 146-157 |
| REQ-010-02-003 | The package interface matrix shall include the eight interface categories marked for Workbook row 11: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. | Compare matrix entries to workbook row 11 and Gate 7 interface IDs. | `26020-Packages_Interfaces_4_export.xlsx` sheet1 row 11; Gate 7 `INTERFACE_REGISTER.csv` rows 32-39 |
| REQ-010-02-004 | The datasheet shall carry the controls power-panel question as an interface note/disposition under this package datasheet, not as a separate package or deliverable. | Confirm no separate package/deliverable is asserted in this datasheet. | Gate 7 `ARTIFACT_REGISTER.csv` rows 149-157; Gate 7 `INTERFACE_REGISTER.csv` rows 32-39 |
| REQ-010-02-005 | The datasheet shall state that the BPCS is the primary process control system for facility process inputs/outputs, except compression unit controls, which are standalone Unit Control Systems integrated for monitoring and alarming. | Confirm wording in controls architecture section. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Control System Basis" |
| REQ-010-02-006 | The datasheet shall identify Allen-Bradley ControlLogix 1756-L8x as the BPCS controller platform and Allen-Bradley Flex5000 I/O with PRP network configuration as the Remote I/O basis. | Confirm platform fields are present or explicitly marked superseded by later accepted source. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "BPCS and Remote I/O" |
| REQ-010-02-007 | The datasheet shall distinguish package communication/monitoring from process control: Modbus via Kepware KepserverEX is for monitoring and data collection only, not process control. | Confirm package-interface section contains this constraint. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Unit Control Systems and Package Interfaces" |
| REQ-010-02-008 | The datasheet shall preserve detailed-design/vendor-integration fields as `TBD` where source text does not define data maps, permissive logic, trip interfaces, alarm priorities, VLANs, IP addresses, detector quantities, set points, voting logic, or final model selections. | Confirm unsupported values are not invented. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 and SEC-14 |
| REQ-010-02-009 | The datasheet shall include the design ambient range -40 deg C to +35 deg C where package equipment/facility environmental basis is needed, unless a stricter package-specific basis is later accepted. | Confirm environmental section. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-02 "Design Ambient Temperature" |
| REQ-010-02-010 | The datasheet shall include package-building and interface coordination expectations for MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins. | Confirm coordination fields. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-09 "Mechanical Package Structure" |

## Standards

| Standard or basis | Applicability | Status |
|---|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Governs package/deliverable/artifact/interface identity and objective association. | Authoritative upstream snapshot |
| `26020-Packages_Interfaces_4_export.xlsx` | Workbook row 11 interface categories for the controls package. | Accessible source material |
| DBM SEC-13 Control System Basis | Controls architecture, networks, BPCS, RIO, package interfaces, instrument-air controls interface. | Accessible source material |
| DBM SEC-14 Instrumentation, Fire and Gas Detection, and Shutdown Interfaces | Fire/gas/ESD/shutdown interface expectations and unresolved detailed-design fields. | Accessible source material |
| DBM SEC-12 Electrical Basis | Electrical power, MCC, cable separation, building, heat tracing, and instrument-air electrical interface context. | Accessible source material |
| Project electrical, instrumentation, control-system, IT/OT, HAZOP, SIL, and vendor package specifications | Detailed design criteria needed for final issue. | `TBD`; referenced as needed but not available as deliverable-specific slices in this run |

## Verification

| Verification item | Method | Acceptance criterion |
|---|---|---|
| Identity verification | Register cross-check | Datasheet identity matches `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`. |
| Interface verification | Workbook/register cross-check | All eight row 11 interface categories and Gate 7 interface IDs are represented. |
| Source-grounding verification | Source citation review | Non-trivial values and requirements cite Gate 7, workbook row 11, or DBM source sections. |
| TBD discipline | Source gap review | Unsupported detailed-design and vendor-integration values remain `TBD`. |
| Cross-document consistency | Compare `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` | Terms, interface categories, source references, and TBD items align across the four documents. |

## Documentation

The completed package datasheet package shall retain or produce:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source and snapshot reference list.
- Open/TBD item list for detailed design, vendor integration, IT/OT coordination, HAZOP/SIL outcomes, and human authority rulings.
