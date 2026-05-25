# Datasheet: DEL-028-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-028-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-028` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 28 / row 30 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-019 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 30; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Facility context | Deepcut expansion (4-25); package serves as a step-down distribution transformer within the 4-25 / 880-1 area electrical distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system narrative |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package tag | TXP-8801-1 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Equipment class | Step-down distribution transformer (vendor-owned Electrical package) | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Rated capacity | 7.5 MVA (as carried in the package name) | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Primary voltage | 13.8 kV (as carried in the package name) | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Secondary voltage(s) | 4160 V and 2400 V (as carried in the package name) | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Source feed basis | Facility electrical system is fed from a BC Hydro utility supply through a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer to local 13.8 kV switchgear; the 13.8 kV switchgear distributes radially through step-down transformers to facility electrical buildings. The TXP-8801-1 vendor package shall accept a 13.8 kV, 3-phase, 3-wire, 60 Hz LRG primary feed consistent with the medium-voltage service basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system narrative and voltage/service table |
| Medium-voltage service basis | Facility medium-voltage service basis is 13.8 kV, 3-phase, 3-wire, 60 Hz LRG. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table |
| 4160 V service basis | TBD. The Deepcut DBM voltage/service table does not list a 4,160 V service tier directly comparable to the Comp/Liquids 4160V MCC. The 4160 V secondary in the package name is not corroborated by an explicit 4,160 V service entry in the accessible Deepcut source slices. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table; source gap |
| 2400 V service basis | TBD. No 2400 V service is listed in the Deepcut DBM voltage/service table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table; source gap |
| Cooling class | TBD. Accessible sources do not state the transformer cooling class (e.g., ONAN/ONAF) for TXP-8801-1. | Source gap |
| Winding configuration / vector group | TBD. No vector group or winding configuration stated in accessible sources. | Source gap |
| Impedance, BIL, tap changer | TBD. No impedance, basic insulation level, or tap-changer configuration stated in accessible sources. | Source gap |
| Insulating medium | The DBM notes that "Large oil-filled transformers shall be spaced in accordance with CEC requirements"; specific TXP-8801-1 insulating medium (oil-filled or dry-type) is not stated in accessible sources and is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers section; source gap |
| Quantity per package | 1 (as carried by the single package tag TXP-8801-1) | Workbook Packages row 30; ASSUMPTION based on single tag |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-028; vendor package shall accept 13.8 kV primary feed from facility 13.8 kV distribution and deliver 4160 V and 2400 V secondary services per facility integration design. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-5A6FBABCBA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` facility electrical system narrative |
| Grounding / Bonding | Interface fact applies to PKG-028. All major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors sized per CEC. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-22E75E0E48`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` grounding/bonding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-028. Package shall coordinate exterior lighting tie-ins per facility lighting design. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-487236B7E5` |
| I&C / Control Cabling | Interface fact applies to PKG-028. Power circuits at medium and low voltage shall be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-FD9BCC3585` |
| Communications / Network | Interface fact applies to PKG-028. Communications/network tie-ins shall be coordinated through facility network design. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-2C9EC16D97` |
| Maintenance Access | Interface fact applies to PKG-028. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-5C19FEBFC8` |
| Structural / Foundations / Supports | Interface fact applies to PKG-028. Vendor shall provide transformer loading data sufficient for EPC foundation/support design. The DBM notes transformers are generally installed on structural steel or precast concrete bearing foundations. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-B1AD88E9C0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` foundations and Transformers sections |
| Site environmental conditions | TBD. Site ambient temperature range, altitude, seismic, and wind/snow loading were not located in the accessible source slices for this deliverable. | Source gap |
| Hazardous-area classification | TBD. Area classification at the TXP-8801-1 location is not stated in the accessible source slices. | Source gap |
| Secondary containment | The DBM states "Secondary containment requirements shall be reviewed, and transformer selection shall avoid or limit containment requirements where practical." Applicability to TXP-8801-1 is TBD pending vendor selection of insulating medium. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers section |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, and the physical equipment package | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-028`; `DELIVERABLE_REGISTER.csv` row `DEL-028-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (integration review on this deliverable). | `PACKAGE_REGISTER.csv` row `PKG-028`; `DELIVERABLE_REGISTER.csv` row `DEL-028-04` |
| Installation location | TBD. Accessible Deepcut DBM slices describe the broader 4-25 facility electrical buildings and the 880-1 area in general terms but do not assign TXP-8801-1 to a specific pad, building, or yard location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` facility electrical system; source gap |
| Foundations / supports | Structural / foundations / supports interface applies; DBM general practice is precast concrete bearing foundations or structural steel transformer bases. Transformer-specific foundation loads, anchor bolting, and oil-containment requirements are TBD pending vendor loading data and EPC civil/structural design. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-B1AD88E9C0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers and foundations sections |
| Bushings, accessories, protective devices | TBD unless defined by vendor package data sheets and detailed design. | Source gap; no PKG-028-specific entry located in `_Sources/26020-Package_Requirements.docx` during this run. |
| Testing and factory acceptance | TBD. Factory routine, type, and special tests are not enumerated in accessible source slices and will be carried by the vendor design basis and datasheet set artifact. | Source gap; expected `ART-6814431C11` content |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-028-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-028`.
- `ARTIFACT_REGISTER.csv`, rows `ART-BC53713A9F` (Vendor engineered physical equipment package) and `ART-6814431C11` (Vendor package design basis and datasheet set).
- `INTERFACE_REGISTER.csv`, rows for `PKG-028` (`IFC-5A6FBABCBA`, `IFC-22E75E0E48`, `IFC-487236B7E5`, `IFC-FD9BCC3585`, `IFC-2C9EC16D97`, `IFC-5C19FEBFC8`, `IFC-B1AD88E9C0`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, objectives for `DEL-028-04_vendor-engineered-equipment-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 — ASSUMPTION via PACKAGE_HEURISTIC).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 30.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system narrative, voltage/service table, Transformers section, grounding/bonding paragraphs, foundations general practice.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific TXP-8801-1 content; no PKG-028-specific match located during this run.
- Sibling deliverables `DEL-028-01_scope-of-work` (EPC Scope of Work) and `DEL-028-02_package-datasheet` (EPC Package Datasheet) are the cited upstream EPC anchors for this vendor production unit.
