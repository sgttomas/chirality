# Datasheet: DEL-027-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-027-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 27 / row 29 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-018 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 29; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package for a step-down distribution transformer. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-027-04_vendor-engineered-equipment-package` |
| Equipment tag | TXP-8301-1 | Workbook Packages row 29 (package name) |
| Package function | Step-down distribution transformer for facility electrical distribution. | Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution paragraphs (13.8 kV distribution to step-down transformers) |
| Nameplate rating | 20/26 MVA (per package title; ASSUMPTION: 20 MVA ONAN / 26 MVA ONAF or equivalent dual rating per typical oil-filled distribution transformer practice). Vendor data to confirm cooling-class basis. | Workbook Packages row 29 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer paragraphs |
| Voltage basis (per package title) | 13.8 kV primary; 6.9 kV and/or 0.4 kV secondary(ies). The accessible source describes 13.8 kV facility backbone distribution and 6.9 kV process AC inverter-drive motor service. A 0.4 kV (400 V) winding is not described in the accessible DBM source slices; treat secondary configuration (single 6.9 kV with separate 0.4 kV winding vs. dual-secondary vs. labelling artifact) as `TBD` for vendor data. | Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table and 6.9 kV inlet/sales compressor electrical building |
| Service basis (primary 13.8 kV) | Facility backbone distribution: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table |
| Service basis (6.9 kV secondary) | Facility process AC inverter-drive motors rated 5,500 hp and above; 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table |
| Service basis (0.4 kV secondary) | TBD. No DBM source slice describes a 0.4 kV (400 V) facility service; package title is the only basis for this voltage. | Workbook Packages row 29 (package name); source gap |
| Neutral grounding | Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. The BC Hydro utility transformer uses a 200 A, 10 s NGR; each 600 V transformer uses a 5 A continuous high-resistance NGR. Application to the 13.8 kV primary winding of TXP-8301-1 is not directly stated; vendor data to confirm. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| Construction (insulation/cooling medium) | ASSUMPTION: oil-filled (large oil-filled transformers are described in the DBM and shown on the equipment list). Vendor data to confirm. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer paragraph; equipment list "Oil-Filled Transformers (2)" |
| Foundations | Generally supported on precast concrete bearing foundations (and structural steel transformer bases for large oil-filled units). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations paragraph; transformer paragraph |
| Spacing / secondary containment | CEC spacing requirements apply; secondary containment requirements shall be reviewed, and transformer selection shall avoid or limit containment requirements where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer paragraph |
| Medium-voltage cable interface (13.8 kV side) | Three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |
| Medium-voltage cable interface (6.9 kV side) | Three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |
| Vendor engineering inputs | EPC Scope of Work (`DEL-027-01`) and Package Datasheet (`DEL-027-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-027-01`, `DEL-027-02` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-027-04`; `ARTIFACT_REGISTER.csv` rows `ART-6FA1DBA3D1`, `ART-0723EEECE8` |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface for the 13.8 kV primary feed and the 6.9 kV (and any 0.4 kV) secondary distribution. | `INTERFACE_REGISTER.csv` `IFC-7FDEAE3A5F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, distribution paragraphs |
| Grounding / Bonding | Vendor package grounding shall be compatible with the EPC-defined ground grid and with the applicable neutral-grounding resistor scheme (100 A, 10 s NGR on each 6.9 kV transformer; major equipment connected to the ground grid at two points; ground wells at power transformers with bolted ground connections at test points). | `INTERFACE_REGISTER.csv` `IFC-868150D715`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Vendor package layout shall not interfere with the EPC-defined Area / Exterior Lighting interface; vendor coordinates clearance for lighting standards and access lighting around the transformer pad. | `INTERFACE_REGISTER.csv` `IFC-A7AA374E9F`; source gap on package-specific lighting layout (TBD). |
| I&C / Control Cabling | Vendor package shall provide control, protection, monitoring, and metering signal landing points compatible with the EPC-defined I&C / Control Cabling interface. | `INTERFACE_REGISTER.csv` `IFC-A771D8D087` |
| Communications / Network | Vendor package shall provide network/communications landing points (e.g., Ethernet for protection relays, monitoring) compatible with the EPC-defined Communications / Network interface. | `INTERFACE_REGISTER.csv` `IFC-41603B3260`; ASSUMPTION (consistent with DBM 6.9 kV MCC Ethernet practice). |
| Maintenance Access | Vendor package layout and supply shall preserve the EPC-defined Maintenance Access interface (CEC spacing; access for radiators, bushings, tap changer, NGR cubicle if applicable, oil sampling, and oil containment). | `INTERFACE_REGISTER.csv` `IFC-6D508F385A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer paragraph |
| Structural / Foundations / Supports | Vendor package skid/frame/foundation/support provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface (precast concrete bearing foundations; structural-steel transformer bases for large oil-filled units). | `INTERFACE_REGISTER.csv` `IFC-1B8FDDED83`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformer paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-027`; `DELIVERABLE_REGISTER.csv` row `DEL-027-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Installation location | TBD. Source material confirms a 13.8 kV switchgear electrical building (810-1) and a 6.9 kV inlet/sales compressor electrical building (820-1), and describes step-down transformers distributing from the 13.8 kV bus, but PKG-027 (TXP-8301-1) is not explicitly assigned to a specific building/pad in the accessible source slices. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list and distribution paragraph |
| Foundations / supports | Precast concrete bearing foundations and/or structural-steel transformer bases per DBM transformer practice; coordinated with the Structural / Foundations / Supports interface. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformer paragraphs; `INTERFACE_REGISTER.csv` `IFC-1B8FDDED83` |
| Secondary containment | Reviewed and minimized where practical per DBM transformer practice; vendor selection should support this preference. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer paragraph |
| Vendor documentation set | Captured separately by `DEL-027-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-027-04`, `DEL-027-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-027-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-027`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-027` and specifically `ART-6FA1DBA3D1`, `ART-0723EEECE8`.
- `INTERFACE_REGISTER.csv`, rows `IFC-7FDEAE3A5F`, `IFC-868150D715`, `IFC-A7AA374E9F`, `IFC-A771D8D087`, `IFC-41603B3260`, `IFC-6D508F385A`, `IFC-1B8FDDED83`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-027-04_vendor-engineered-equipment-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for facility distribution (13.8 kV/6.9 kV/600 V voltage table), step-down transformer distribution paragraph, transformers paragraph, grounding paragraphs (100 A 10 s NGR on each 6.9 kV transformer; major-equipment two-point ground grid), foundations paragraph, electrical buildings paragraph, medium-voltage cable table.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-027 (TXP-8301-1) match was identified in source slices accessible to this run.
- Sibling EPC deliverables: `DEL-027-01_scope-of-work`, `DEL-027-02_package-datasheet` (vendor engineering inputs); `DEL-027-05_vendor-document-turnover-package`, `DEL-027-06_epc-vendor-package-review-and-acceptance` (downstream integration).
