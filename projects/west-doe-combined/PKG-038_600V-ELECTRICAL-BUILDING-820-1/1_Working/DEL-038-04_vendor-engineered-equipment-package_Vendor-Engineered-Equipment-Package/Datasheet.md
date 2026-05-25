# Datasheet: DEL-038-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-038-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-038` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-1) | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 38 / row 40 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-029 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 40; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-038` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-038-04_vendor-engineered-equipment-package` |
| Package function | Prefabricated, modular electrical building (tag 820-1) housing low-voltage (600 V class) electrical distribution and supporting equipment as required by detailed design. | Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Building tag identity (CONFLICT) | Package name carries tag `820-1`. The DBM electrical-buildings table assigns `820-1` to "6.9 kV Inlet / Sales Compressor Electrical Building", while the workbook package name labels the same tag a "600V ELECTRICAL BUILDING". Detailed configuration cannot be set until this conflict is resolved (see Guidance Conflict Table CFL-038-04-001). | Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table |
| Building construction class | Prefabricated, modular building located in a general purpose area, climate controlled, with bottom-entry cable provisions, elevated on piles to provide space for incoming/outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Equipment housed (as required by detailed design) | 600 V MCCs; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; plant PLC control panels; network racks; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels. Package-specific equipment list is `TBD` until vendor data resolves it. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| HVAC basis | Climate-controlled with HVAC sized as an n + 1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Wiring basis | TECK and ACIC cables. EMT conduit shall be used between equipment located adjacent to each other (e.g., control panels to contactor panels). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Receptacle provision | One outdoor GFI receptacle for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Door provisions | Equipment doors sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Power feed basis | Distribution from the 13.8 kV main switchgear, radially through step-down transformers to facility electrical buildings; package-specific feed configuration is `TBD` and subject to the building-tag conflict (CFL-038-04-001). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, power distribution section |
| Vendor engineering inputs | EPC Scope of Work (`DEL-038-01`) and Package Datasheet (`DEL-038-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-038-01_scope-of-work`, `DEL-038-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-038-04`; `ARTIFACT_REGISTER.csv` rows `ART-4F595A7D97`, `ART-CF8553E9A3` |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Utility Piping | Vendor building/skid layout shall accommodate the EPC-defined Utility Piping interface at the building boundary. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-592E5CCFE2` |
| Drain / Containment | Vendor building shall accommodate the EPC-defined Drain / Containment interface (floor drains, oil-containment provisions per detailed design). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-EA9C0A8BD1` |
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface (incoming feed, outgoing distribution). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C7243E4F80` |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface, with two-point ground-grid connection for major equipment and CEC-sized separate copper ground conductors at distribution transformers, panelboards, and three-phase motors larger than 100 hp where applicable. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-065DD9678E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Vendor building shall accommodate the EPC-defined Area / Exterior Lighting interface. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-8D5F57505E` |
| I&C / Control Cabling | Vendor building shall accommodate the EPC-defined I&C / Control Cabling interface (cable entries, tray, segregation). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-33A55B6DBB` |
| Communications / Network | Vendor building shall accommodate the EPC-defined Communications / Network interface (network racks, building entry). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-6F5BF129A3` |
| Building HVAC / Services | Vendor building HVAC shall be sized n + 1 per DBM and shall accommodate the EPC-defined Building HVAC / Services interface. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-F3F5DA500E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Fire & Gas / Safety Systems | Vendor building shall accommodate the EPC-defined Fire & Gas / Safety Systems interface (detection devices, ESD provisions). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C4BE8B720F` |
| Maintenance Access | Vendor building layout shall preserve the EPC-defined Maintenance Access interface; equipment doors sized for removal of largest equipment. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-B981842FD5`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Grading / Site Drainage / Spill Containment | Vendor building elevation and skirt provisions shall accommodate the EPC-defined Grading / Site Drainage / Spill Containment interface. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` (PKG-038 row) |
| Structural / Foundations / Supports | Vendor building shall be elevated on piles for bottom-entry cable provisions; foundation/anchorage coordinated with the EPC-defined Structural / Foundations / Supports interface. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` (PKG-038 row); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-038`; `DELIVERABLE_REGISTER.csv` row `DEL-038-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Shop fabrication | DBM identifies the building tag `820-1` as a Shop-fabricated electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table |
| Installation location | Electrical buildings shall be located in general purpose areas for convenient power distribution. Site-specific location for the 820-1 building is `TBD` pending EPC site decisions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Elevated, pile-supported foundation per DBM; package-specific support basis is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; `INTERFACE_REGISTER.csv` |
| Cable entry | Bottom entry for incoming and outgoing power cables; outgoing cables from 600 V MCCs to facility 600 V loads also bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Vendor documentation set | Captured separately by `DEL-038-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-038-04`, `DEL-038-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-038-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-038`.
- `ARTIFACT_REGISTER.csv`, rows `ART-4F595A7D97`, `ART-CF8553E9A3` for `DEL-038-04`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-038`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-038-04_vendor-engineered-equipment-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 40.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for electrical buildings, power distribution, grounding, cable systems, HVAC; electrical buildings table for 820-1.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical building / cross-facility interface source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for `820`-tag content; no package-specific match found.
- Sibling EPC deliverables: `DEL-038-01_scope-of-work`, `DEL-038-02_package-datasheet` (vendor engineering inputs); `DEL-038-03_construction-work-package` (installation/tie-in); `DEL-038-05_vendor-document-turnover-package`, `DEL-038-06_epc-vendor-package-review-and-acceptance` (downstream integration).
