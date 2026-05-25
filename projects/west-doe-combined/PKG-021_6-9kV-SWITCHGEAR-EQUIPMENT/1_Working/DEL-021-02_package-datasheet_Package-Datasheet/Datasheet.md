# Datasheet: DEL-021-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-021-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-021` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR EQUIPMENT | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 21 / row 23 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-012 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 23; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-021` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Package function | 6.9 kV switchgear equipment package supporting facility medium-voltage distribution at the 6.9 kV level. | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| MV service basis (facility) | 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded; per the DBM, 6.9 kV serves facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table |
| Upstream feed basis | The facility 13.8 kV switchgear is the plant main power distribution center; the 6.9 kV system is fed via step-down from 13.8 kV switchgear to the 6.9 kV Inlet/Sales Compressor Electrical Building. Allocation of PKG-021 to specific upstream transformer/feeder remains `TBD` at the package level. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system narrative |
| Neutral grounding | Each 6.9 kV transformer shall be grounded with a 100 A, 10-second neutral grounding resistor operating as a tripping system. Application to switchgear protection coordination is a vendor/EPC interface detail. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| MV cable basis | 6.9 kV medium-voltage cables: three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table |
| Quantity (Medium Voltage Switchgear) | DBM electrical equipment list identifies "Medium Voltage Switchgear" quantity 1. Allocation of this quantity specifically to PKG-021 vs. PKG-036 (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)) is not confirmed by source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list |
| Bus / breaker / cubicle ratings | `TBD`. The accessible source set does not state bus current, short-circuit withstand, breaker continuous/interrupting ratings, cubicle configuration, or arc-resistance class for PKG-021. | Source gap; `26020-Package_Requirements.docx` has no PKG-021-specific match |
| Protective relaying | `TBD`. DBM cites MV protective relays as a UPS-supported load and notes 6.9 kV MCC motor protection relays, but does not define PKG-021 switchgear relay schemes. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services and MCC paragraphs |
| Control power | UPS services at 120 VAC / 125 VDC support MV breaker control circuits and MV protective relays at the facility level. Package-specific control-power interface to PKG-021 is to be coordinated with the UPS packages. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9D7DF96637` |
| Grounding / Bonding | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-2ACD080082` |
| I&C / Control Cabling | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-B44478ADB6` |
| Communications / Network | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-FC8113A0CE` |
| Maintenance Access | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9E975838A2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-021 and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-A795E61D99` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points. Applicability of additional CEC-sized conductors to switchgear, transformers, and ancillary devices shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Plant communications | Ethernet communications to plant PLC central control panels are required at the related 6.9 kV MCC for data acquisition; equivalent communications hooks for PKG-021 switchgear protective relays and metering shall be coordinated by EPC integration. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Installation location | `ASSUMPTION`: the 6.9 kV switchgear is housed in the 820-1 6.9kV Inlet/Sales Compressor Electrical Building or an equivalent electrical building; the source identifies the 820-1 building and lists 13.8 kV main switchgear, MV MCCs, and ancillary equipment as electrical-building tenants without explicitly assigning PKG-021 to a specific building/room. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list and facility electrical system narrative |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is `TBD` (skid vs. floor-mounted lineup, seismic anchorage, deflection). | Workbook Packages row 23; `INTERFACE_REGISTER.csv` |
| MV cable termination | Switchgear shall accommodate 6.9 kV three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. Bottom-entry vs. top-entry, lug type, and stress-cone provisions are `TBD` per vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table |
| Arc-flash, short-circuit, coordination studies | Required as EPC integration scope; specific values, settings, and study report references are `TBD` pending vendor data and detailed design. | Source gap; DBM does not provide package-specific values |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-021-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-021`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-021-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-021`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-021-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for facility electrical system, MV voltage/service table, 6.9 kV MCC paragraph, electrical buildings list, grounding/bonding, neutral grounding, MV cable table, UPS services, and cable tray/conduit paragraphs.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical building and main switchgear cross-facility context.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 6.9 kV switchgear content; no PKG-021 match found.
