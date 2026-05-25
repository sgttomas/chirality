# Specification: EPC / Controls Discipline Production Package

## Scope

This specification covers the source-limited EPC/discipline production basis for `DEL-010-04_epc-controls-discipline-production-package`, supporting `PKG-010 - Controls system design and integration` for WBS 03 and scope item `SOW-0010`.

The package includes the controls production basis for the non-vendor package scope and the required closure record for source-limited discipline requirements. It does not create a separate vendor-package ownership model or separate controls power-panel package; Gate 7 carries controls power-panel items as interface facts/artifacts under the package datasheet. Source: PACKAGE_REGISTER.csv, ARTIFACT_REGISTER.csv, and INTERFACE_REGISTER.csv for PKG-010.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-010-04-001 | The production package shall identify PKG-010 as the Controls system design and integration package under WBS 03 and retain the source basis as Workbook Packages row 11. | PACKAGE_REGISTER.csv, PKG-010; SCOPE_LEDGER.csv, SOW-0010. |
| REQ-010-04-002 | The production package shall carry the responsibility model as source-dependent EPC Integrator or discipline subcontractor responsibility; it shall not infer a separate vendor-package ownership model from the current sources. | PACKAGE_REGISTER.csv, PKG-010; DELIVERABLE_REGISTER.csv, DEL-010-04. |
| REQ-010-04-003 | The production package shall include a source-limited requirements closure record because detailed discipline requirements are not present in the current source set and remain open. | ARTIFACT_REGISTER.csv, DEL-010-04. |
| REQ-010-04-004 | The controls production basis shall use the BPCS architecture identified in the DBM: Allen-Bradley ControlLogix 1756-L8x BPCS, Flex5000 Remote I/O, PRP redundant Ethernet for RIO, and segregated I/O Network. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 Control System Basis. |
| REQ-010-04-005 | The production package shall preserve the package-control boundary: compression Unit Control Systems remain standalone and replicate required values/general alarms to BPCS; final package maps, permissives, trips, and alarm priorities are vendor integration/detailed-design items. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 Unit Control Systems and Package Interfaces. |
| REQ-010-04-006 | The production package shall state that Modbus is used for monitoring and data collection only and not for process control. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 Unit Control Systems and Package Interfaces. |
| REQ-010-04-007 | The production package shall identify applicable PKG-010 interfaces: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | INTERFACE_REGISTER.csv, PKG-010. |
| REQ-010-04-008 | The production package shall coordinate BPCS-associated safety devices to nearest practical Remote I/O panels, including ESD buttons, fire detection, LEL detection, H2S detection, and other process-related safety items. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 Control System Basis. |
| REQ-010-04-009 | The production package shall preserve the 04-25 instrument-air supply basis and shall not add local 03-25 instrument-air compressor controls. | 3-25_Comp_and_Liquids_DBM.md, SEC-13; SEC-12. |
| REQ-010-04-010 | The production package shall mark detailed discipline deliverable register contents, final controller sizing, final IDMZ/firewall/VLAN/IP details, trip lists, cause-and-effect actions, and reset responsibilities as TBD until detailed-design or source-document evidence is accepted. | 3-25_Comp_and_Liquids_DBM.md, SEC-13; DELIVERABLE_REGISTER.csv notes for DEL-010-04. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP final published snapshot | Governing decomposition basis for package/deliverable/interface/objective records. |
| 3-25 Compressor Station and Liquids Hub DBM, SEC-13 Control System Basis | Locally accessible controls source slice used for BPCS, network, RIO, package interface, and safety-device wiring requirements. |
| Project control-system standards and instrumentation specifications | Identified by DBM as applicable, but the final standards register/specification index is not in this deliverable-local source set; location TBD. |
| HAZOP/SIL outcomes and cause-and-effect logic | Required coordination basis for final shutdown/fire/gas actions, but final values/actions are TBD. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-010-04-001 through REQ-010-04-003 | Check package, deliverable, scope, and artifact registers against the production package cover/basis and closure record. |
| REQ-010-04-004 through REQ-010-04-006 | Review controls architecture deliverables for BPCS/RIO/network platform alignment and for monitoring-only Modbus use. |
| REQ-010-04-007 | Compare interface matrix against INTERFACE_REGISTER.csv rows for PKG-010. |
| REQ-010-04-008 | Check I/O assignment, location, and wiring deliverables for nearest-practical RIO treatment of BPCS-associated safety devices. |
| REQ-010-04-009 | Confirm no local 03-25 instrument-air compressor control scope has been added and that monitoring/alarm/trip interfaces are coordinated to final cause-and-effect logic. |
| REQ-010-04-010 | Confirm TBD items remain in the closure record until accepted source evidence or human ruling resolves them. |

## Documentation

The production package shall include or point to these records:

- Discipline production package basis.
- Source-limited requirements closure record.
- TBD discipline deliverable register.
- Controls architecture basis and package-interface notes.
- Interface matrix for the PKG-010 applicable interface types.
- Verification/closure checklist tying requirements to source evidence.
