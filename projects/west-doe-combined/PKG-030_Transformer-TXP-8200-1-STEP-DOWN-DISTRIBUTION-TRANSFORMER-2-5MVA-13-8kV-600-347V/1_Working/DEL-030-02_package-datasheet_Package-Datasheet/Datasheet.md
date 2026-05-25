# Datasheet: DEL-030-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-030-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-030` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 30 / row 32 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-021 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 32; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-030` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Package function | Step-down distribution transformer package, tag TXP-8200-1, nominal 2.5 MVA, 13.8 kV primary / 600 V / 347 V secondary basis as named in workbook row 32. | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Primary voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (facility MV backbone). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Secondary voltage | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor (facility low-voltage service to 600 V MCCs, lighting/utility distribution transformers, building heaters, UPS > 10 kVA). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| 347 V leg interpretation | 347 V is the line-to-neutral value of a 600 V/347 V grounded-wye secondary used for facility lighting; package-specific wye/delta configuration and neutral treatment are TBD pending vendor data or detailed-design source. | ASSUMPTION (industry-standard 600/347 V wye interpretation); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table does not state 347 V explicitly |
| Rating (nameplate) | 2.5 MVA, as carried in workbook row 32 / package name. Cooling class, impedance, BIL, tap range, winding material, vector group, and temperature rise are TBD pending vendor data. | Workbook Packages row 32; vendor data not available |
| Construction type | TBD. The DBM transformer paragraph addresses "large oil-filled transformers" and a "480 V dry-type transformer" for LACT; it does not assign oil-filled vs. dry-type to TXP-8200-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Distribution role | Step-down from 13.8 kV switchgear to a downstream 600 V MCC / lighting & utility distribution basis per the Deepcut radial distribution scheme. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power distribution paragraph |
| Grounding (secondary) | 600 V transformer secondary grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs include power metering and ground/resistor fault detection; ground-fault protection on 600 V systems is alarm-only. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| 208/120 V derivation | Downstream 208/120 V services are derived from a separate distribution transformer stepping from 600 V with neutral solidly grounded; not within this package unless specified by vendor scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 208/120 V paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-030; primary 13.8 kV feed from the 13.8 kV switchgear bus, secondary 600 V/347 V feed to downstream MCC and lighting/utility distribution. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-009C48E7FF`; DBM power-distribution paragraph |
| Grounding / Bonding | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells shall be provided at power transformers for maintenance and operational testing; distribution transformers shall have a separate copper ground conductor sized per CEC. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-6C663BF69D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-030 (transformer yard / pad area lighting coordination); detailed luminaire and pole assignments are TBD pending detailed design. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-0B28AED229` |
| I&C / Control Cabling | Interface fact applies to PKG-030 for transformer monitoring (winding temperature, oil temperature, sudden-pressure, neutral grounding resistor monitoring as applicable); specific signal list is TBD pending vendor data. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-D000451C37` |
| Communications / Network | Interface fact applies to PKG-030 for any transformer-monitoring relay or RTU network connection to the plant control/network architecture; protocol and tie-in point are TBD. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-9EF13A0FC1` |
| Maintenance Access | CEC spacing for large oil-filled transformers shall be respected; cable tray and conduit routing shall not interfere with maintenance access; ground wells at transformers serve as test points. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-345609CB34`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers and cable-tray paragraphs |
| Structural / Foundations / Supports | Transformers are generally supported on precast concrete bearing foundations / structural-steel transformer bases; secondary containment requirements shall be reviewed and transformer selection shall avoid or limit containment requirements where practical. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-4B50D76AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and Transformers paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Installation location | TBD. DBM describes prefabricated electrical buildings and outdoor transformer installations but does not assign TXP-8200-1 to a specific pad/building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings and Transformers paragraphs |
| Foundations / supports | Precast concrete bearing foundations / structural-steel transformer base. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Foundations table; Transformers paragraph |
| Secondary containment | Containment requirements shall be reviewed; transformer selection shall avoid or limit containment requirements where practical. Package-specific containment design is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Primary cable / termination | TBD pending vendor termination details and Deepcut MV cable schedule. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-030 match |
| Secondary cable / termination | 600 V transformer secondary to plant 600 V MCCs uses ACWU cable; single-conductor cables avoided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule table |
| Protection / metering | Coordination with upstream 13.8 kV switchgear protection; downstream 600 V MCC ground/resistor fault detection and alarm-only ground-fault protection; transformer-specific protection settings are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and MCC paragraphs |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-030-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-030`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-030-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-030` (`IFC-009C48E7FF`, `IFC-6C663BF69D`, `IFC-0B28AED229`, `IFC-D000451C37`, `IFC-9EF13A0FC1`, `IFC-345609CB34`, `IFC-4B50D76AF1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-030-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: System Voltages table, Transformers paragraph, Standby Power paragraph, Electrical Buildings paragraph, Grounding paragraphs, cable schedule, and Foundations table.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-030 match found.
