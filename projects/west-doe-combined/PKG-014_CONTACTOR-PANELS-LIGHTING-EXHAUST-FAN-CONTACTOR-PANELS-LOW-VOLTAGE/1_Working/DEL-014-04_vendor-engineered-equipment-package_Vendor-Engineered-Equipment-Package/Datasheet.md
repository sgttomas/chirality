# Datasheet: DEL-014-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-014-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-014` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 14 / row 16 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-005 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 16; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-014` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-014-04_vendor-engineered-equipment-package` |
| Package function | Low-voltage contactor panels for lighting and for exhaust fan control. | Workbook Packages row 16; `PACKAGE_REGISTER.csv` row `PKG-014` |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor; used for motors 3/4 hp through 250 hp, DOL starting, lighting transformers, building heaters, and UPS larger than 10 kVA. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage and service table |
| Lighting and utility service basis | 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded; used for lighting, receptacles, heat trace, small motors, and UPS 10 kVA or smaller. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage and service table |
| Contactor panel count / rating | TBD. No package-specific source slice defines the number of contactor panels, the panel ratings, the number of contactor circuits per panel, control voltage, or control logic. | Source gap; no PKG-014 match found in `_Sources/26020-Package_Requirements.docx`; no contactor-panel-specific text in DBM |
| Lighting load served | TBD. The DBM identifies lighting (area, building, exterior) as part of electrical scope but does not enumerate panel-by-panel lighting loads, branch circuits, or downstream lighting distribution allocated to PKG-014. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings/lighting paragraphs |
| Exhaust fan loads served | TBD. The DBM references building HVAC and ventilation but does not enumerate exhaust fan tags, motor sizes, count, or control bases allocated to PKG-014. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings and HVAC interface text |
| Vendor engineering inputs | EPC Scope of Work (`DEL-014-01`) and Package Datasheet (`DEL-014-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-014-01_scope-of-work`, `DEL-014-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-014-04` |
| Local control station basis | ASSUMPTION (directional context): the DBM specifies that for 600 V MCC motor circuits, one local control station (H-O-A or On-Off) shall be installed adjacent to each motor and hard-wired to the starter circuit; applicability to exhaust fan contactor panel circuits is to be confirmed by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power paragraph |
| Standards / codes basis | TBD; specific standards governing low-voltage contactor panels (e.g., CSA/UL panelboard, contactor, and lighting control standards) are not enumerated in accessible source slices for PKG-014. | Source gap |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-78CF31138D` |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-31C88BB424` |
| Area / Exterior Lighting | Vendor lighting contactor panel scope shall be coordinated with the EPC-defined Area / Exterior Lighting interface. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-EF784327FA` |
| I&C / Control Cabling | Vendor package shall be engineered to the EPC-defined I&C / Control Cabling interface (control input/permissive cabling to and from contactor panels). | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-C715E9AA3E` |
| Communications / Network | Vendor package shall be engineered to the EPC-defined Communications / Network interface where contactor panels expose status, monitoring, or control over plant network. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-2D60238809` |
| Maintenance Access | Vendor package layout and supply shall preserve the EPC-defined Maintenance Access interface. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-52B07B0D36` |
| Structural / Foundations / Supports | Vendor package skid/frame/wall-mount provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-53646D26A1` |
| Area classification | TBD. Package-specific hazardous area classification for contactor panel locations (electrical building vs. field) is not enumerated in accessible source slices. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, area classification paragraph |
| Electrical building interface | Electrical buildings shall house MCCs, switchgear, and distribution equipment; allocation of PKG-014 contactor panels to electrical buildings vs. other locations is TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package (low-voltage lighting and exhaust fan contactor panels). | `PACKAGE_REGISTER.csv` row `PKG-014`; `DELIVERABLE_REGISTER.csv` row `DEL-014-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Installation location | TBD. DBM allows for distribution equipment in electrical buildings and for lighting/heat trace utility distribution throughout the facility, but does not assign PKG-014 panels to a specific building, MCC room, or field location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings/lighting paragraphs |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific mounting basis (wall, floor stand, skid) is TBD. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` |
| Vendor documentation set | Captured separately by `DEL-014-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-014-04`, `DEL-014-05` |
| EPC review and acceptance | EPC review/acceptance of the vendor package is captured by `DEL-014-06_epc-vendor-package-review-and-acceptance`. | `DELIVERABLE_REGISTER.csv` row `DEL-014-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-014-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-014`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-014`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-014`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-014-04_vendor-engineered-equipment-package` (PACKAGE_HEURISTIC).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design basis source slices for low-voltage service, lighting/utility service, MCC and local control stations, electrical buildings, and area classification.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific contactor panel content; no PKG-014 match found.
- Sibling EPC deliverables: `DEL-014-01_scope-of-work`, `DEL-014-02_package-datasheet` (vendor engineering inputs); `DEL-014-05_vendor-document-turnover-package`, `DEL-014-06_epc-vendor-package-review-and-acceptance` (downstream integration).
