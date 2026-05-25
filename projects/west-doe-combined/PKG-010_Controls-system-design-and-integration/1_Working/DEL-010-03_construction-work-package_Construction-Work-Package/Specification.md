# Specification: DEL-010-03 Construction Work Package

## Scope

This specification governs the Construction Work Package for `PKG-010 - Controls system design and integration`, WBS 03, CoA tracking number `26020-01-32-001`.

The deliverable covers the EPC Integrator's construction-facing plan for installing, building, inspecting, turning over, and tying the controls system design and integration package into the larger facility systems. Source: DELIVERABLE_REGISTER.csv, DEL-010-03.

The deliverable must include:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Source: DELIVERABLE_REGISTER.csv and ARTIFACT_REGISTER.csv, DEL-010-03.

Exclusions:

- Third-party LACT equipment is outside 03-25 facility equipment scope except for facility-side power/tie-in interfaces where required. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-01 and SEC-10.
- Local 03-25 instrument-air compressor controls must not be added; instrument air is supplied from 04-25 under SCA-006. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13.
- Package-specific construction sequencing, field redline process, inspection forms, and turnover dossier index are TBD unless supplied by project execution procedures.

## Requirements

| Req ID | Requirement | Source / section | Verification |
|---|---|---|---|
| CWP-010-03-R001 | The CWP shall identify package identity, WBS, CoA tracking number, discipline, responsible party, and workbook/source basis. | PACKAGE_REGISTER.csv, PKG-010; DELIVERABLE_REGISTER.csv, DEL-010-03 | Datasheet and CWP cover/index review. |
| CWP-010-03-R002 | The CWP shall include the three required artifacts: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | DELIVERABLE_REGISTER.csv and ARTIFACT_REGISTER.csv, DEL-010-03 | Artifact completeness check. |
| CWP-010-03-R003 | The installation and tie-in workface plan shall address applicable PKG-010 interface types: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | INTERFACE_REGISTER.csv, PKG-010; workbook packages export, Packages sheet row 11 | Interface matrix and workface checklist review. |
| CWP-010-03-R004 | The CWP shall coordinate package buildings, self-framing enclosures, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins with civil, electrical, controls, and instrumentation sections where applicable. | 3-25_Comp_and_Liquids_DBM.md, SEC-09 | Interdiscipline review signoff or TBD evidence. |
| CWP-010-03-R005 | The CWP shall preserve BPCS / Unit Control System boundaries: BPCS is the primary process control system except compression unit controls, which are standalone Unit Control Systems integrated for monitoring and alarming. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 | Controls interface checkout and cause-and-effect review. |
| CWP-010-03-R006 | The CWP shall preserve Modbus restrictions: Modbus data is for monitoring and data collection only, and process control shall not be performed over Modbus. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 | Network/interface checkout and controls configuration review. |
| CWP-010-03-R007 | The CWP shall include installation/turnover checks for remote I/O architecture where in scope, including Flex5000 I/O and PRP network configuration basis for 03-25 remote distribution centres. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 | RIO cabinet inspection, network continuity, and commissioning checklist. |
| CWP-010-03-R008 | The CWP shall identify that final package data maps, permissive logic, trip interfaces, and alarm priorities remain vendor/detailed-design integration items before construction closeout. | 3-25_Comp_and_Liquids_DBM.md, SEC-13 | Open-item register and turnover checklist. |
| CWP-010-03-R009 | The CWP shall include fire/gas, H2S, LEL, methyl mercaptan, ESD, and unit shutdown interface coordination with BPCS, Remote I/O, package controls, electrical area classification, and HAZOP/SIL outcomes. | 3-25_Comp_and_Liquids_DBM.md, SEC-14 | Safety-system interface review and cause-and-effect verification. |
| CWP-010-03-R010 | The CWP shall not close final alarm philosophy, horn tone mapping, beacon layout, operator notification logic, trip lists, shutdown levels, cause-and-effect actions, or reset responsibilities without detailed-design evidence. | 3-25_Comp_and_Liquids_DBM.md, SEC-14 | Items remain TBD/open until supporting documents are accepted. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative decomposition truth for package/deliverable identity and artifacts. |
| 03-25 Compressor Station and Liquids Hub DBM | Accessible source material for construction, mechanical package coordination, controls, instrumentation, fire/gas, and shutdown interface basis. |
| 4-25 Deepcut DBM SEC-13 | Relevant controls-system architecture context for central control room, MCC, RIO, network, server, workstation, and Modbus bases. |
| Project construction execution procedures | TBD; not available in accessible source set. |
| Project inspection and test plan / turnover procedure | TBD; not available in accessible source set. |

## Verification

| Verification item | Acceptance basis |
|---|---|
| Document completeness | All required CWP artifacts present and traceable to DEL-010-03. |
| Interface completeness | Applicable PKG-010 interface types are listed and assigned to construction/tie-in checks or marked TBD. |
| Controls boundary preservation | BPCS, Unit Control System, Modbus, RIO, fire/gas, and shutdown interface constraints are reflected without unsupported changes. |
| Dependency/blocker status | Declared upstream/downstream dependencies are recorded; none are declared as of PREPARATION. |
| Open-item control | Unsupported construction sequence, inspection form, and turnover details remain TBD or in an open-item register. |

## Documentation

The final CWP package should contain or reference:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Interface matrix for the eight PKG-010 interface types.
- Controls/network/RIO installation and checkout records.
- Safety-system and shutdown interface verification records.
- Open-item register for detailed-design, vendor, HAZOP/SIL, alarm philosophy, and turnover items.
