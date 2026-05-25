# Specification: DEL-022-04_vendor-engineered-equipment-package

## Scope

This specification defines the normative requirements applicable to the Vendor Engineered Equipment Package for `PKG-022` 5kV SWITCHGEAR EQUIPMENT. It covers Package Vendor engineering, design, fabrication/supply, and the physical equipment package produced from the EPC package Scope of Work (`DEL-022-01`) and Package Datasheet (`DEL-022-02`), with EPC Integrator integration review.

**In scope**
- Vendor package engineering and design of the medium-voltage switchgear package and associated vendor-supplied auxiliaries within the package boundary.
- Fabrication/supply of the physical equipment package.
- Vendor package design basis and datasheet set (delivered through `DEL-022-05`).
- Source-grounded conformance to the project Electrical specifications (`ELC-QAS-000003-001` and `ELC-QAS-000007-001`) and the electrical design basis sections of the DBM.

**Out of scope**
- Facility integration, tie-ins, constructability, procurement/construction coordination (EPC Integrator scope per `PACKAGE_REGISTER.csv` row `PKG-022`).
- Construction Work Package (`DEL-022-03`).
- Vendor document turnover (`DEL-022-05`) and EPC review and acceptance (`DEL-022-06`).

**Title scope clarification.** The package title is "5kV SWITCHGEAR EQUIPMENT." The exact nominal bus voltage, equipment count, and physical scope of the package are TBD pending the Package Datasheet (`DEL-022-02`) and package-specific source slice. See Conflict Table in `Guidance.md` (HRR-022-04-001).

## Requirements

| # | Requirement | Basis | Source |
|---|---|---|---|
| R-01 | The Vendor Engineered Equipment Package shall be developed from the accepted EPC package Scope of Work (`DEL-022-01`) and Package Datasheet (`DEL-022-02`). | Deliverable contract | `DELIVERABLE_REGISTER.csv` row `DEL-022-04_vendor-engineered-equipment-package` |
| R-02 | The Package Vendor shall own package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator shall own facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Responsibility model | `PACKAGE_REGISTER.csv` row `PKG-022` |
| R-03 | Medium-voltage switchgear engineering, design, and procurement shall conform to specification `ELC-QAS-000007-001` (Medium Voltage Switchgear, Rev 1). | Project Electrical specification | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| R-04 | Vendor-supplied packaged equipment shall conform to specification `ELC-QAS-000003-001` (Electrical Requirements for Packaged Equipment, Rev 2). | Project Electrical specification | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| R-05 | Equipment ratings shall be confirmed by the project's short-circuit, relay coordination and arc-flash energy, load-flow, and load analysis studies before fabrication release. | Project basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical studies table |
| R-06 | Medium-voltage breaker control circuits and medium-voltage protective relays in this package shall be designed to be served by 120 VAC and/or 125 VDC UPS services. | UPS service basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row in System Voltages table |
| R-07 | If the package includes 6.9 kV switchgear or MCC sections, mechanically latched fused contactors with motor protection relays and an Ethernet communication port for connection to the plant PLC central control panel shall be provided. (ASSUMPTION until Package Datasheet (`DEL-022-02`) confirms whether 6.9 kV scope is in PKG-022.) | DBM MV MCC basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control paragraphs |
| R-08 | If the package includes 4.16 kV switchgear or MCC sections, mechanically latched fused contactors with motor protection relays and an Ethernet communication port for connection to the plant PLC central control panel shall be provided. VFD and soft-starter requirements for 4.16 kV motors are TBD. | DBM MV MCC basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control paragraphs |
| R-09 | Grounding of any 6.9 kV transformer associated with this package shall be by a 100 A, 10 s neutral grounding resistor operated as a tripping system. | DBM grounding basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding paragraphs |
| R-10 | Medium-voltage cabling interfacing this package shall conform to the DBM cable basis: 13.8 kV cables shall be three-conductor copper TECK rated 15 kV with 133% insulation, shielded; 4.16 kV cables shall be three-conductor copper TECK rated 5 kV with 100% insulation. | DBM cable basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cabling rows |
| R-11 | The package shall accommodate bottom entry of incoming and outgoing power cables consistent with the electrical building design basis. | DBM electrical buildings basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| R-12 | Equipment shall be specified to operate within the climate-controlled electrical-building indoor environment (HVAC n+1). Specific environmental envelope shall be defined in the Package Datasheet. | DBM electrical buildings basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| R-13 | The Package Vendor shall produce a vendor package design basis and vendor datasheet set covering at minimum: single-line diagram, bus arrangement, breaker schedule, protection and metering schedule, control and DC schematics, layout/general arrangement, and nameplate schedule. Specific document list and granularity shall be confirmed by the Package Datasheet and `DEL-022-05`. ASSUMPTION on document list scope. | Anticipated artifacts | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-022-05_vendor-document-turnover-package` |
| R-14 | All interfaces declared on `PKG-022` in `INTERFACE_REGISTER.csv` (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) shall be addressed in the vendor package datasheet set. | Interface register | `INTERFACE_REGISTER.csv` rows for `PKG-022` |
| R-15 | The package shall not be released for fabrication until the EPC Integrator confirms the package interface requirements matrix in `DEL-022-02` and accepts the vendor package per `DEL-022-06`. | Coordination basis | `DELIVERABLE_REGISTER.csv` rows `DEL-022-02`, `DEL-022-06` |

## Standards

| Standard / spec | Title | Applicability | Source |
|---|---|---|---|
| `ELC-QAS-000003-001` (Rev 2) | Electrical Requirements for Packaged Equipment | Applies to all vendor-engineered electrical packages | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| `ELC-QAS-000007-001` (Rev 1) | Medium Voltage Switchgear | Governs medium-voltage switchgear engineering and procurement | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| `ELC-QAS-000008-001` (Rev 1) | Medium Voltage Motor Control Centers | Applies if package scope includes MV MCC sections — confirmation TBD by Package Datasheet | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| `ELC-QAS-000002-001` (Rev 1) | Electrical Design | Applies as the project Electrical design specification | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| `ELC-QAS-000001-001` (Rev 1) | Electrical Construction | Applies to construction interfaces | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| Canadian Electrical Code (CEC) | National electrical code (Canada) | Governs CEC-driven aspects (e.g., clearances, conduit, grounding sizing) per DBM | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, multiple paragraphs |
| API RP-505 | Hazardous area classification reference | Applies to facility-level area classification framing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification |

Clause-level requirements within each specification are TBD (location TBD); the listed specifications themselves are confirmed by the DBM electrical specifications table.

## Verification

| Requirement | Verification approach | Records |
|---|---|---|
| R-01, R-02 | EPC review against `DEL-022-01` and `DEL-022-02` per acceptance deliverable | `DEL-022-06` package acceptance checklist |
| R-03, R-04, R-08 | Vendor specification-conformance matrix referencing `ELC-QAS-000007-001`, `ELC-QAS-000003-001`, and `ELC-QAS-000008-001` | Vendor specification conformance matrix in `DEL-022-05` |
| R-05 | Confirmation that final equipment ratings reflect short-circuit, relay coordination/arc-flash, load-flow, and load analysis study outputs | Study reports referenced and stamped into the vendor package design basis |
| R-06, R-09 | Inspection / review of control and protection schematics and grounding details against DBM basis | Vendor schematics, grounding drawings |
| R-07, R-08 | Factory inspection / FAT confirming mechanically latched fused contactors, motor-protection relays, and Ethernet communication ports where applicable | FAT report |
| R-10, R-11 | EPC interface review of cable entry, conduit, and tray interfaces | EPC interface checklist (`DEL-022-06`) |
| R-12 | Vendor environmental ratings cross-checked against electrical-building HVAC envelope (TBD by Package Datasheet) | Vendor environmental data sheet |
| R-13, R-14 | Vendor document register completeness check; interface coverage check against `INTERFACE_REGISTER.csv` rows | Vendor document register (`DEL-022-05`) |
| R-15 | Written EPC acceptance to release for fabrication | `DEL-022-06` acceptance record |

## Documentation

Required vendor documentation set (to be confirmed in the Package Datasheet and `DEL-022-05`):

- Vendor package design basis
- Vendor datasheet set (single-line, bus arrangement, breaker schedule, protection and metering schedule, control and DC schematics, layout/general arrangement, nameplate schedule)
- Specification conformance matrix (`ELC-QAS-000003-001`, `ELC-QAS-000007-001`, and others as applicable)
- Interface requirements coverage matrix (per `INTERFACE_REGISTER.csv` rows for `PKG-022`)
- FAT and inspection records
- Vendor document register supporting `DEL-022-05`
