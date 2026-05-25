# Specification: DEL-009-02_package-datasheet — Package Datasheet

## Scope

This specification covers the EPC Integrator package datasheet for PKG-009, Controls system design and integration, WBS 02. The datasheet is the technical handoff basis for controls package engineering and integration, including package identity, controls architecture data, interface requirements, and source-supported design criteria.

The datasheet excludes unsupported package-specific values that are not present in the accepted Gate 7 snapshot or accessible source slices. Those values remain `TBD` until confirmed by detailed design, vendor integration, or a human ruling.

Source: Gate 7 DELIVERABLE_REGISTER.csv row DEL-009-02_package-datasheet; Gate 7 PACKAGE_REGISTER.csv row PKG-009.

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| REQ-009-02-001 | The datasheet shall identify the package as PKG-009, Controls system design and integration, WBS 02, CoA tracking number 26020-01-32-001. | Compare against Gate 7 PACKAGE_REGISTER.csv row PKG-009 and workbook Packages row 10. |
| REQ-009-02-002 | The datasheet shall state that it is a mandatory EPC Integrator technical handoff deliverable for third-party vendor or discipline package engineering and design. | Compare against Gate 7 DELIVERABLE_REGISTER.csv row DEL-009-02_package-datasheet. |
| REQ-009-02-003 | The datasheet shall carry the applicable interface types for PKG-009: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | Compare against Gate 7 INTERFACE_REGISTER.csv rows for PKG-009 and workbook Packages row 10. |
| REQ-009-02-004 | The datasheet shall treat controls power-panel interfaces as datasheet/interface facts, not as a separate package or deliverable. | Compare against Gate 7 INTERFACE_REGISTER.csv notes for PKG-009. |
| REQ-009-02-005 | The datasheet shall identify the current BPCS platform basis as Allen-Bradley ControlLogix 1756-L8x series and Remote I/O basis as Allen-Bradley Flex5000 I/O with PRP network configuration. | Compare against DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| REQ-009-02-006 | The datasheet shall state that Modbus is used for monitoring and data collection only, and that process control is not carried over Modbus. | Compare against DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| REQ-009-02-007 | The datasheet shall identify package and third-party interfaces as using defined communication protocols and hardwired signals according to criticality. | Compare against DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| REQ-009-02-008 | The datasheet shall carry instrument-air monitoring as an interface to 04-25 and shall not add local 03-25 instrument-air compressor controls. | Compare against DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-07 and SEC-13. |
| REQ-009-02-009 | The datasheet shall identify final package data maps, permissive logic, trip interfaces, alarm priorities, and detector design values as `TBD` where not resolved in the available source set. | Confirm no unsupported values were introduced; compare against DBM SEC-13 and SEC-14 TBD statements. |

## Standards

| Standard / basis | Applicability | Source |
|---|---|---|
| Project control-system standards | Applicable to BPCS/RIO architecture and package control interfaces; exact document number/location TBD. | DBM SEC-15, standards basis |
| Project instrumentation specifications | Applicable to instrumentation, detector, ESD, and field wiring requirements; exact document number/location TBD. | DBM SEC-15, standards basis |
| Project electrical specifications | Applicable to power/control separation, grounding, bonding, cable tray, conduit, and electrical interfaces; exact document number/location TBD. | DBM SEC-12 and SEC-15 |
| HAZOP/SIL outcomes | Applicable to final detector, shutdown, voting, setpoint, and cause-and-effect basis; outcomes not available in current source slice. | DBM SEC-14 |

## Verification

1. Confirm the deliverable identity, parent package, WBS, tracking number, discipline, responsibility, and anticipated artifacts against the Gate 7 deliverable and package registers.
2. Confirm every interface type in the datasheet matches the Gate 7 interface register and workbook Packages row 10.
3. Confirm controls architecture statements against DBM SEC-13.
4. Confirm instrumentation, fire and gas, and shutdown interface statements against DBM SEC-14.
5. Confirm electrical/interface constraints against DBM SEC-12.
6. Confirm unresolved values remain `TBD` and are not converted into requirements without source support.

## Documentation

The completed package datasheet should provide or reference:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Package data maps, permissive logic, trip interfaces, and alarm priorities when available from detailed design or vendor integration.
- Cause-and-effect and shutdown logic inputs when available.
- Control-system network and communication protocol basis.
- Fire and gas, ESD, and Remote I/O interface basis.
