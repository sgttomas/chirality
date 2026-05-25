# Datasheet: DEL-021-01_scope-of-work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-021-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-021` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR EQUIPMENT | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 21 / row 23 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-021` |
| CoA tracking number | 26020-01-30-012 | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers scope item | `SOW-0022` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-021` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Package function | 6.9 kV switchgear equipment package supporting medium-voltage distribution to inverter-drive process motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table |
| Medium-voltage service basis | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table |
| Associated electrical building | 820-1 6.9kV Inlet/Sales Compressor Electrical Building (Shop-fabricated prefab building). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list (rows 2812, 2921) |
| MCC association | 6.9 kV motor control center (MCC-8200 synchronous-transfer bus) feeds the KM-2150/2250 Inlet/Sales Gas Compressor motors via Starting VFDs with synchronous transfer to a normal-service bus after reaching full speed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Upstream power source | Radial step-down from the 13.8 kV plant main switchgear via 13.8 kV / 6.9 kV step-down transformer feed to the 6.9 kV Inlet/Sales Compressor Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant distribution paragraph |
| Neutral grounding basis | Each 6.9 kV transformer is grounded using a 100 A, 10 s neutral grounding resistor and operates as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| MV cable basis | 6.9 kV medium-voltage cables are three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |
| Motor protection / comms | Mechanically latched fused contactors with motor protection relays and Ethernet communication port to the plant PLC central control panel for data acquisition. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Power-factor correction | Power-factor-correction capacitor banks shall not be installed on the MCC-8200 synchronous-transfer bus. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Governing project specification | ELC-QAS-000007-001 Medium Voltage Switchgear (and ELC-QAS-000008-001 Medium Voltage Motor Control Centers). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical/instrumentation specifications table |
| Equipment quantity / rating detail | TBD. Workbook row 23 and DBM identify the 6.9 kV switchgear/MCC scope but accessible source slices do not provide confirmed switchgear lineup count, bus rating, interrupting capacity, or section detail. Final values await the short-circuit study and vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, short-circuit study row |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-021` and must be represented in the package interface requirements matrix. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9D7DF96637` |
| Grounding / Bonding | Interface fact applies to `PKG-021`; major electrical equipment is directly connected to the ground grid at two points. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-2ACD080082`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| I&C / Control Cabling | Interface fact applies to `PKG-021`; supports Ethernet to plant PLC and protective-relay/control wiring. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-B44478ADB6`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Communications / Network | Interface fact applies to `PKG-021`; Ethernet communication port to plant PLC central control panel. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-FC8113A0CE`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Maintenance Access | Interface fact applies to `PKG-021`; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9E975838A2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable/conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to `PKG-021`; electrical buildings are elevated on piles with bottom entry of incoming/outgoing power cables. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-A795E61D99`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraphs |
| Spacing / area classification | Distance between MCC and process equipment is 7.5 m (25 ft) per CEC requirement; applicability to the 6.9 kV switchgear lineup shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical equipment spacing table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Installation location | 820-1 6.9kV Inlet/Sales Compressor Electrical Building (shop-fabricated prefab). Exact room/lineup location is subject to detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list |
| Building delivery basis | Prefabricated, modular electrical buildings in general purpose areas, designed for bottom entry of incoming and outgoing power cables, elevated on piles to provide cable routing space beneath the building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraphs |
| Tie-in to upstream main | Radial feed from 13.8 kV main switchgear via 13.8 kV / 6.9 kV step-down transformer to the 6.9 kV electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant distribution paragraph |
| Lineup ratings, section count, breaker counts, interrupting capacity | TBD pending the project short-circuit study and vendor engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, short-circuit study row |
| Package exclusions | No package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` row `PKG-021` (exclusions column TBD) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-021-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-021`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-021` (`IFC-9D7DF96637`, `IFC-2ACD080082`, `IFC-B44478ADB6`, `IFC-FC8113A0CE`, `IFC-9E975838A2`, `IFC-A795E61D99`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-021-01_scope-of-work` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 — ASSUMPTION, package-heuristic association).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (voltage/service table, electrical buildings list, 6.9 kV MCC paragraph, grounding paragraph, cable table, plant distribution paragraph, electrical/instrumentation specifications table).
- Workbook Packages row 23.
