# Datasheet: DEL-020-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-020-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-020` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 20 / row 22 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-020` |
| CoA tracking number | 26020-01-30-011 | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Discipline | Electrical | Workbook Packages row 22; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-020-04_vendor-engineered-equipment-package` |
| Package function | 13.8 kV medium-voltage switchgear equipment package serving as the plant main power distribution center. | Workbook Packages row 22; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (13.8 kV switchgear section) |
| Bus / system voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (LRG) — facility medium-voltage backbone distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table |
| Bus capacity | The 13.8 kV switchgear bus shall be sized for the full facility scope. Numeric bus rating, short-circuit duty, and continuous current ratings are `TBD` pending detailed electrical studies and vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear design basis |
| Source of supply | Upstream supply: utility-supplied 25 kV/13.8 kV transformer (TBC) stepping down BC Hydro utility power to the 13.8 kV switchgear; transformer specifics are owned outside this package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, utility supply paragraph |
| Downstream distribution | Radial distribution through step-down transformers to electrical buildings across the facility (e.g., 13.8 kV → 4.16 kV for medium-voltage motor loads, 13.8 kV → 600 V for low-voltage loads). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear distribution paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 03-25 sub-feeder list |
| Cross-facility feed | Provides 13.8 kV, 3 phase, 3 wire, 60 Hz LRG primary feed from 04-25 main switchgear to 03-25 facility (sub-fed). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, incoming-power and sub-feed paragraphs |
| Standby / emergency power tie-in | Current basis: TOU low-voltage standby generators at 600 V MCC with transfer switches; the prior centralized 13.8 kV emergency-generator concept has been eliminated. No 13.8 kV-level emergency generator interface is required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, emergency power paragraph |
| Vendor engineering inputs | EPC Scope of Work (`DEL-020-01`) and Package Datasheet (`DEL-020-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-020-01_scope-of-work`, `DEL-020-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-020-04` |
| Medium-voltage cable basis | Three-conductor copper TECK cable rated 15 kV with 133 percent insulation; shielded — applies to 13.8 kV feeder/distribution cabling associated with switchgear interfaces. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable paragraph |
| Installation location | DBM identifies a "13.8 kV Switchgear Electrical Building" as a prefabricated, modular building housing 13.8 kV main switchgear among other equipment. Specific PKG-020 building assignment is `TBD` until confirmed by EPC integration. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and equipment-building table |
| Equipment count | DBM equipment list identifies one Medium Voltage Switchgear (`ELC-QAS-000007-001`, qty 1); allocation of that line to PKG-020 is consistent with the package definition but final count for this deliverable is `TBD` pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-611474D99C` |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-F3098CE7CD` |
| I&C / Control Cabling | Vendor package shall be engineered to the EPC-defined I&C / Control Cabling interface (including MV breaker control and MV protective relay wiring boundaries). | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-8BF7209227` |
| Communications / Network | Vendor package shall be engineered to the EPC-defined Communications / Network interface (e.g., relay communications, network drops to electrical building network racks). | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-340091634A` |
| Maintenance Access | Vendor package layout and supply shall preserve the EPC-defined Maintenance Access interface (front/rear access, arc-flash boundaries, withdrawable breaker maneuvering space). | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-2FB786FC10` |
| Structural / Foundations / Supports | Vendor package skid/frame/foundation provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability to this switchgear vendor package shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable / conduit routing | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing. Vendor-supplied internal cable tray and conduit routing shall not interfere with maintenance access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Co-located equipment context | Electrical building may also house medium-voltage MCCs, MV reduced-voltage soft starters, MV VFDs, 600 V MCCs, UPS systems and distribution panels, distribution transformers, contactor panels, PLC panels, and network racks. Vendor package boundary must be preserved among co-located equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-020`; `DELIVERABLE_REGISTER.csv` row `DEL-020-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Installation location | DBM names a "13.8 kV Switchgear Electrical Building" as a prefabricated, modular shop-built building (`810-1 13.8kV Switchgear Electrical Building`); specific PKG-020 assignment to that building is `TBD` pending EPC confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and equipment-building table |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis is `TBD`. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Vendor documentation set | Captured separately by `DEL-020-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-020-04`, `DEL-020-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-020-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-020`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-020`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-020` (`IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-020-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 22.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for 13.8 kV utility supply and main switchgear, electrical buildings, medium-voltage cables, standby power, grounding, cable tray, and conduit.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 03-25 cross-facility incoming-power and sub-feeder source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 13.8 kV switchgear content; no PKG-020 match was extracted into the deliverable-local truth set.
- Sibling EPC deliverables: `DEL-020-01_scope-of-work`, `DEL-020-02_package-datasheet` (vendor engineering inputs); `DEL-020-03_construction-work-package` (installation/turnover); `DEL-020-05_vendor-document-turnover-package`, `DEL-020-06_epc-vendor-package-review-and-acceptance` (downstream integration).
