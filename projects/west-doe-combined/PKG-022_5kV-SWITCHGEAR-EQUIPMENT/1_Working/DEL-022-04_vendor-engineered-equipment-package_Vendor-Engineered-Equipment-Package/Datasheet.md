# Datasheet: DEL-022-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-022-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-022` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR EQUIPMENT | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 22 / row 24 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-013 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-022` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-022` |
| Package function | Vendor engineering, design, fabrication/supply, and physical equipment package for the package's medium-voltage switchgear scope, developed from the EPC Scope of Work (`DEL-022-01`) and Package Datasheet (`DEL-022-02`). | `DELIVERABLE_REGISTER.csv` row `DEL-022-04_vendor-engineered-equipment-package`; `PACKAGE_REGISTER.csv` row `PKG-022` |
| Package title interpretation | Package title "5kV SWITCHGEAR EQUIPMENT" identifies a medium-voltage switchgear package in the Electrical workbook scope. ASSUMPTION: "5kV" denotes a 5 kV insulation class consistent with the facility's 4.16 kV medium-voltage services; the source DBM does not call out a 5 kV nominal switchgear bus separately from the 13.8 kV main switchgear and 6.9/4.16 kV motor control centers. HRR-022-04-001. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System and System Voltages tables; `PACKAGE_REGISTER.csv` row `PKG-022` |
| Equipment list anchor | Source equipment list references Medium Voltage Switchgear (qty 1) and Medium Voltage Motor Control Centers (qty 1) under Electrical specifications. Allocation of these counts specifically to PKG-022 is not confirmed by an accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table (rows ELC-QAS-000007-001 and ELC-QAS-000008-001) |
| Governing equipment specification | Medium Voltage Switchgear procurement and engineering basis is governed by specification `ELC-QAS-000007-001` (Medium Voltage Switchgear, Rev 1); Electrical Requirements for Packaged Equipment is governed by `ELC-QAS-000003-001` (Rev 2). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical specifications table |
| System voltage basis | Facility medium-voltage services include 13.8 kV (backbone), 6.9 kV (5,500 hp and above process motors), and 4.16 kV (250 hp to 5,500 hp process motors), all 3-phase, 3-wire, 60 Hz, low-resistance grounded. Exact nominal voltage and bus configuration for PKG-022 is TBD pending Package Datasheet (`DEL-022-02`) and accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Cabling insulation class basis | 13.8 kV medium-voltage cables shall be three-conductor copper TECK rated 15 kV with 133% insulation, shielded. 4.160 kV medium-voltage cables shall be three-conductor copper TECK rated 5 kV with 100% insulation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable rows |
| Grounding basis | BC Hydro utility transformer grounded by 200 A, 10 s neutral grounding resistor (tripping). Each 6.9 kV transformer grounded by 100 A, 10 s neutral grounding resistor (tripping). Each 600 V transformer grounded by 5 A continuous high-resistance grounding resistor. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding paragraphs |
| Control / protection supply | Medium-voltage breaker control circuits and medium-voltage protective relays are served by 120 VAC / 125 VDC UPS services. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row in System Voltages table |
| Equipment rating studies | Short-circuit, relay coordination and arc-flash energy, load-flow, and load analysis studies shall be completed before finalizing equipment ratings and suitability. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical studies table |
| Area classification | Facility general design: Class I Zone 2, Gas Groups IIA and IIB; electrical buildings located in general purpose areas. Package-specific classification is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification paragraphs |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | `INTERFACE_REGISTER.csv` `IFC-FAD0C5C924` |
| Grounding / Bonding | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | `INTERFACE_REGISTER.csv` `IFC-291807A33B` |
| I&C / Control Cabling | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | `INTERFACE_REGISTER.csv` `IFC-FFD6E87354` |
| Communications / Network | Interface fact applies to PKG-022; medium-voltage MCCs require Ethernet communication port to plant PLC central control panel for data acquisition (DBM basis for the 6.9 kV and 4.16 kV MCCs). | `INTERFACE_REGISTER.csv` `IFC-652BE03197`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control paragraphs |
| Maintenance Access | Interface fact applies to PKG-022; cable tray and conduit routing shall not interfere with maintenance access; equipment doors shall allow removal of the largest equipment. | `INTERFACE_REGISTER.csv` `IFC-53BEFBC3CA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-022; package-specific foundation/support basis is TBD. | `INTERFACE_REGISTER.csv` `IFC-ED54C3FD1A` |
| Hazardous-area marking | VFD-fed motors and equipment placed in Zone 2 areas shall be marked accordingly. Applicability to PKG-022 medium-voltage switchgear (typically located in general-purpose electrical buildings) is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control / area classification paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-022`; `DELIVERABLE_REGISTER.csv` row `DEL-022-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility, with integration review of the vendor package. | `PACKAGE_REGISTER.csv` row `PKG-022`; `DELIVERABLE_REGISTER.csv` row `DEL-022-04` |
| Installation location | TBD. DBM identifies prefabricated, modular electrical buildings in general-purpose areas that may house 13.8 kV main switchgear, medium-voltage MCCs, soft-starters, VFDs, and 600 V MCCs; the package-specific building, room, or skid assignment for PKG-022 is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| Cable entry / building integration | Electrical buildings designed for bottom entry of incoming and outgoing power cables; buildings elevated on piles. Applicability to PKG-022 confirmed at the facility level; package-specific cable entry plan is TBD pending Package Datasheet. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| HVAC environment | Electrical buildings climate controlled with n+1 HVAC; package vendor equipment shall be specified to operate within the resulting indoor environment. Specific temperature/humidity envelope for PKG-022 is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Vendor documentation | Vendor package design basis and datasheet set are anticipated artifacts and must be delivered through the Vendor Document Turnover deliverable (`DEL-022-05`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-022-05` |
| Acceptance | EPC vendor package review and acceptance evidence is captured in `DEL-022-06`. | `DELIVERABLE_REGISTER.csv` row `DEL-022-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, dependency view.
- `DELIVERABLE_REGISTER.csv`, row `DEL-022-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-022`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-022` (`IFC-FAD0C5C924`, `IFC-291807A33B`, `IFC-FFD6E87354`, `IFC-652BE03197`, `IFC-53BEFBC3CA`, `IFC-ED54C3FD1A`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows associated with `PKG-022` (objective association recorded as ASSUMPTION under PACKAGE_HEURISTIC mode).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 24.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices (Power System, System Voltages, Standby Power, Motor Control, Electrical Buildings, Grounding and Bonding, Cabling, Area Classification, Electrical Specifications table).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific switchgear content; no PKG-022 package-specific source slice located during this run.
