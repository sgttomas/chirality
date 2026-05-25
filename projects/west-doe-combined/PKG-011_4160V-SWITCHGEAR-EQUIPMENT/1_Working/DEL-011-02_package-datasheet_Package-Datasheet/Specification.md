# Specification: DEL-011-02_package-datasheet - Package Datasheet

## Scope

This specification governs the EPC Integrator package datasheet for `PKG-011` 4160V SWITCHGEAR EQUIPMENT. The datasheet is a technical handoff deliverable for third-party vendor or discipline package engineering and design, and it must preserve source-supported equipment data, package interface requirements, and EPC/vendor responsibility boundaries.

This document does not specify the final vendor design in place of the vendor engineered equipment package. Package-specific lineup configuration, equipment ratings, interrupting capacity, protection settings, enclosure details, and final cable/interface quantities remain `TBD` until confirmed by detailed electrical studies, project electrical specifications, and vendor design submittals.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-011-02-001 | The datasheet shall identify `PKG-011` as an Electrical package named 4160V SWITCHGEAR EQUIPMENT with CoA tracking number `26020-02-30-002`. | `PACKAGE_REGISTER.csv`, `PKG-011` |
| REQ-011-02-002 | The datasheet shall state the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv`, `PKG-011` |
| REQ-011-02-003 | The datasheet shall include the applicable interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv`, `PKG-011` |
| REQ-011-02-004 | The datasheet shall carry the 03-25 electrical basis that the electrical system is a shared cross-facility utility supplied from 04-25. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Design Basis |
| REQ-011-02-005 | The datasheet shall state the incoming feed basis: 03-25 main power is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| REQ-011-02-006 | The datasheet shall state the transformer/service basis: 13.8 kV to 4.16 kV, 12 MVA transformer serving the 4160V MCC for 4000V motors. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| REQ-011-02-007 | The datasheet shall state the 4,160 V medium-voltage service basis: 3 phase, 3 wire, 60 Hz, low-resistance grounded, for process AC inverter-drive motors from 250 hp to 5,500 hp. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages |
| REQ-011-02-008 | The datasheet shall state that the 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-02-009 | The datasheet shall state that the 4160V MCC serves large 4000V motors, including inlet compressors `KM-2150` and `KM-2250`. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-02-010 | The datasheet shall state that `KM-2150` and `KM-2250` require starting VFDs and that soft starts are not used for those motors under the current basis. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-02-011 | The datasheet shall record that harmonic and reactive-power mitigation are to be determined by detailed electrical studies. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-02-012 | The datasheet shall not assert final package ratings or protection settings until load analysis, short-circuit, relay coordination/arc-flash, and load-flow studies are available. | `4-25_Deepcut_DBM.md`, SEC-12 Governing Codes, Standards, Specifications, and Studies |
| REQ-011-02-013 | The datasheet shall identify unsupported or unavailable package-specific values as `TBD` rather than inferred values. | `four-documents` skill source-grounding rule |

## Standards

| Standard / specification | Applicability | Source / status |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code, applicable BC provincial/local codes, and electrical inspection authority requirements | Electrical design and installation basis. | `4-25_Deepcut_DBM.md`, SEC-12 Governing Codes, Standards, Specifications, and Studies |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | Applicable standards and regulatory bodies for electrical materials/equipment. | `4-25_Deepcut_DBM.md`, SEC-12 Governing Codes, Standards, Specifications, and Studies |
| `ELC-QAS-000003-001` Electrical Requirements for Packaged Equipment, Rev. 2 | Packaged electrical equipment requirements. | `4-25_Deepcut_DBM.md`, SEC-12 Table 12-1 |
| `ELC-QAS-000007-001` Medium Voltage Switchgear, Rev. 1 | Medium-voltage switchgear procurement/design basis. | `4-25_Deepcut_DBM.md`, SEC-12 Table 12-1 |
| `ELC-QAS-000008-001` Medium Voltage Motor Control Centers, Rev. 1 | Medium-voltage MCC procurement/design basis. | `4-25_Deepcut_DBM.md`, SEC-12 Table 12-1 |
| Project electrical specifications not present as local source bodies | Clause-level requirements remain TBD until specification text is available. | Current source gap |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-011-02-001 through REQ-011-02-003 | Check datasheet identity, responsibility, and interface matrix against Gate 7 package, deliverable, artifact, and interface registers. |
| REQ-011-02-004 through REQ-011-02-011 | Check datasheet electrical basis against `3-25_Comp_and_Liquids_DBM.md`, SEC-12 source slices. |
| REQ-011-02-012 | Confirm final datasheet issue references the completed electrical studies or explicitly retains ratings/settings as TBD. |
| REQ-011-02-013 | Review all numeric values and package-specific assertions; values lacking source support shall remain TBD or be backed by accepted vendor/project evidence. |

## Documentation

The deliverable shall include, at minimum:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- TBD register or marked datasheet fields for unavailable package-specific values.

Related downstream evidence expected outside this deliverable includes the vendor engineered physical equipment package, vendor package design basis and datasheet set, vendor document register, vendor submittals, EPC review log, package acceptance checklist, test/inspection evidence, and turnover evidence.
