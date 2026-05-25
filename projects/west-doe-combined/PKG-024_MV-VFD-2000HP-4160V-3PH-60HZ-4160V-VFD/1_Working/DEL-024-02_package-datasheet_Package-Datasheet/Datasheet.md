# Datasheet: DEL-024-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-024-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-024` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 24 / row 26 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-015 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 26; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-024` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Package function | Medium-voltage variable frequency drive package for a 2000 hp, 4160 V, three-phase, 60 Hz motor, fed from a 4160 V supply. | Workbook Packages row 26 |
| MV VFD service basis | The facility 4.160 kV three-phase three-wire 60 Hz low-resistance-grounded service supports process AC inverter-drive motors rated 250 hp up to 5,500 hp. A 2000 hp 4160 V VFD-fed motor falls within this service basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table (line ~2936) |
| 4.16 kV MV VFD/soft-starter requirement status | VFD and soft-starter requirements for 4.16 kV motors are stated as `TBD` in the DBM. The package-specific topology (cells, harmonic mitigation, transformer integration) is not established by accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph (line ~2957) |
| Driven load (motor, service) | TBD. The workbook package name identifies the drive rating but not the driven equipment tag, service, or process duty. No accessible source slice assigns this 2000 hp 4160 V drive to a specific motor or process service. | Workbook Packages row 26; DBM Deepcut electrical sections; no assignment found |
| Indoor/outdoor location | Electrical buildings may house medium-voltage VFDs as required by detailed design; package-specific assignment to a building, room, skid, or outdoor location is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph (line ~2973) |
| Harmonic / power-quality mitigation | TBD. Harmonic and reactive-power mitigation for VFD-fed MV buses is to be determined by detailed electrical studies in the supporting design basis; no package-specific value is available. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph (line ~756) |
| Hazardous-area handling | VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Package-area assignment is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor/area-classification paragraph (line ~2961) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-68C5E24846` |
| Grounding / Bonding | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-F8A6E25E1C` |
| I&C / Control Cabling | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-8062D6F881` |
| Communications / Network | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-22E88310C9` |
| Maintenance Access | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-DD889EF8E3` |
| Structural / Foundations / Supports | Applicable interface fact for PKG-024; must be represented in the package interface requirements matrix. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-850A8082BB` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability detail for this MV VFD package is to be confirmed in detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| MV cable basis | 4.160 kV medium-voltage cables on the facility are three-conductor copper TECK cable rated 5 kV with 100 percent insulation; low-voltage power cable fed from VFDs is copper TECK cable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule (lines ~3009, ~3013) |
| Maintenance access constraint | Cable tray and conduit routing shall not interfere with maintenance access for the package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Installation location | TBD. Source confirms electrical buildings may house MV VFDs but does not place PKG-024 in a specific building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis is `TBD`. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` |
| Drive topology, isolation transformer, output filter, cooling | `TBD` unless defined by vendor package data and detailed design. | Source gap; no PKG-024 match found in `_Sources/26020-Package_Requirements.docx`. |
| Communications and I&C tie-in | Communications / Network and I&C / Control Cabling interfaces apply; protocol, ports, and control wiring detail are `TBD` pending vendor data and plant PLC integration design. | Workbook Packages row 26; `INTERFACE_REGISTER.csv`; DBM MCC Ethernet pattern (line ~2957) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-024-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-024`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-024-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-024`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-024-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for MV services, MV VFD/soft-starter status, electrical buildings, motor/area classification, grounding, and MV cable.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC and VFD/harmonic source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD content; no PKG-024 match found.
