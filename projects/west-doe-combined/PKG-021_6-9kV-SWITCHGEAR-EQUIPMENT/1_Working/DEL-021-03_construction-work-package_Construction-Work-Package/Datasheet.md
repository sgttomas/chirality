# Datasheet: DEL-021-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-021-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-021` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR EQUIPMENT | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 21 / row 23 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-012 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 23; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope-item coverage | `SOW-0022` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Field construction responsibility | Tourmaline Oil Corporation (field construction scope per DBM Construction Responsibility section). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package under WBS 01 | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Package function | 6.9 kV switchgear equipment serving facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table (medium-voltage 6.9 kV service basis) |
| System voltage / grounding basis | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. Each 6.9 kV transformer grounded via 100 A, 10 s neutral grounding resistor operating as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table; Grounding and Bonding section |
| Cable basis (MV) | 6.9 kV cables: three-conductor copper TECK, rated 8 kV with 100 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Specifications table |
| Housing context | DBM identifies a "820-1 6.9kV Inlet / Sales Compressor Electrical Building" as a shop-fabricated module; electrical buildings are prefabricated modular buildings located in general purpose areas with bottom-entry cabling. Package-specific allocation of PKG-021 equipment to a specific building/skid is not confirmed by an accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings table; Electrical Buildings section |
| Governing equipment specification | Project specification `ELC-QAS-000007-001 Medium Voltage Switchgear` (Revision 1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| Governing construction specification | Project specification `ELC-QAS-000001-001 Electrical Construction` (Revision 1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| Required electrical studies | Hazardous area classification, load analysis, short-circuit study, relay coordination and arc-flash energy study, load-flow study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical studies table |
| Quantity / lineup configuration | TBD. The DBM equipment list (`ELC-QAS-000007-001`) records "Medium Voltage Switchgear, 1" but does not confirm allocation, rating, or lineup configuration for PKG-021 specifically. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| Installation location | TBD. DBM context places 6.9 kV switchgear in the Inlet/Sales Compressor Electrical Building (Building 820-1), but the package-specific assignment of PKG-021 equipment is not confirmed in the accessible source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings table |

## Conditions

| Interface / condition | Construction-work-package basis | Source |
|---|---|---|
| Electrical Power | Construction tie-in to the upstream 13.8 kV switchgear via step-down transformer; radial distribution basis. Tie-in execution and field cabling under EPC Integrator scope. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9D7DF96637`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System section |
| Grounding / Bonding | Connect package equipment to the plant ground grid at two points; comply with neutral grounding resistor basis for 6.9 kV transformers; install separate copper ground conductors per CEC where applicable. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-2ACD080082`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section |
| I&C / Control Cabling | Install instrumentation and control cabling (ACIC and TECK as applicable) between switchgear and PLC/relay panels; observe area-classification cabling rules. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-B44478ADB6`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways section |
| Communications / Network | Install network/communications cabling (Ethernet, fiber, etc.) for relay and PLC connectivity; field-run communications cables shall be armored and rated for cable tray installation. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-FC8113A0CE`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways section |
| Maintenance Access | Cable tray and conduit routing shall not interfere with maintenance access; equipment door clearances and removable transom sections shall be preserved during installation. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9E975838A2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Cable Tray/Conduit paragraphs |
| Structural / Foundations / Supports | Equipment shall be set on prepared foundations or skids; electrical buildings shall be elevated and installed on piles with bottom-entry cabling. Field installation of miscellaneous structural supports is within Tourmaline field construction scope. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-A795E61D99`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Construction Responsibility sections |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment supply | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Facility integration, interfaces, tie-ins, constructability | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Field construction execution | Tourmaline Oil Corporation field construction scope (management, off-loading, setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, electrical terminations, field installation of home-run cables, installation of miscellaneous structural supports). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Installation activities (anticipated) | Off-load and set switchgear lineup on prepared foundation/skid; mechanical hookup; bottom-entry power and control cable termination; ground-grid bonding at two points; commissioning checks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility and Electrical Buildings sections; ASSUMPTION (typical MV switchgear installation sequence) labelled as ASSUMPTION pending project construction specification slice access |
| Inspection and testing | Per `ELC-QAS-000001-001` Electrical Construction and `ELC-QAS-000007-001` Medium Voltage Switchgear specifications. Electrical studies (short-circuit, relay coordination, arc-flash) shall be completed prior to energization. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Codes paragraph and electrical studies table |
| Turnover and tie-in evidence | Construction interface and turnover checklist required per `ARTIFACT_REGISTER.csv` row `ART-AD43276A93`; installation and tie-in workface plan per `ART-7EEEDBBC28`. | `ARTIFACT_REGISTER.csv` rows for `DEL-021-03_construction-work-package` |
| Detailed installation drawings, lift plans, rigging studies | TBD pending vendor-issued installation details, equipment weights/dimensions, and detailed engineering. | Source gap; no PKG-021-specific construction document in accessible source set |
| Detailed sequencing and schedule | TBD pending construction schedule from Tourmaline field construction and vendor delivery dates. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-021-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-021`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-021-03_construction-work-package` (`ART-C2EC8C7D5D`, `ART-7EEEDBBC28`, `ART-AD43276A93`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-021` (`IFC-9D7DF96637`, `IFC-2ACD080082`, `IFC-B44478ADB6`, `IFC-FC8113A0CE`, `IFC-9E975838A2`, `IFC-A795E61D99`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-021-03_construction-work-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `SCOPE_LEDGER.csv`, row `SOW-0022`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Basis (System Voltages, Standby Power, Electrical Buildings, Grounding and Bonding, Cable Tray and Conduit), Construction Responsibility section, Modular Buildings table, Table 12-1 specifications.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-021 / 6.9 kV switchgear package-specific construction content; no PKG-021 match found in the accessible source set (location TBD).
