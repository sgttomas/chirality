# Datasheet: DEL-036-01_scope-of-work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-036-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-036` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name (workbook) | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 36 / row 38 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-027 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 38; `_CONTEXT.md` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope-item ID | `SOW-0037` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-036` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Package function (workbook) | 6.9kV switchgear electrical building, building tag 830-1 | Workbook Packages row 38 |
| Medium-voltage service basis (6.9 kV) | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; intended for facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table |
| Distribution basis | 13.8 kV facility backbone steps down through transformers to local medium-voltage electrical buildings, including a 6.9 kV Inlet/Sales Compressor Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant power distribution paragraph |
| 6.9 kV motor control / starting | 6.9 kV MCC shall provide mechanically latched fused contactors with motor protection relays and an Ethernet communication port for connection to the plant PLC central control panel; starting VFDs shall be provided for the KM-2150/2250 Inlet/Sales Gas Compressor motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV motor control paragraph |
| Building tag vs. function (CONFLICT) | Workbook row 38 labels building 830-1 as "6.9kV Switchgear Electrical Building." The DBM electrical-buildings list assigns 830-1 to "4.16kV Acid Gas / Overheads Compressor Electrical Building" and assigns the 6.9 kV building to tag 820-1 ("6.9kV Inlet / Sales Compressor Electrical Building"). See Conflict Table CT-036-01-001 in `Guidance.md`. | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list (rows for 820-1 and 830-1) |
| Detailed equipment list (this building) | TBD. No source slice itemizes the breakers, MCC line-ups, transformers, and protection devices specifically assigned to the workbook PKG-036 building. | Source gap; `26020-Package_Requirements.docx` not parsed as accessible source slice |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-9188C9FD26` |
| Drain / Containment | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-628EF275F0` |
| Electrical Power | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-3B6012818E` |
| Grounding / Bonding | Interface fact applies to PKG-036; major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-B6F77BBE8A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-D49FB38D6F` |
| I&C / Control Cabling | Interface fact applies to PKG-036; MCC Ethernet to plant PLC central control panel implies a control-cabling tie-in. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-972B08F285`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Communications / Network | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-349D2200D1` |
| Building HVAC / Services | Interface fact applies to PKG-036; building heat/HVAC is addressed by the electrical-building HVAC basis. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-C81A342112`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building HVAC paragraph |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-2C313DA749` |
| Maintenance Access | Interface fact applies to PKG-036; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-21B90D3691`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-036. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-DC7DB17C89` |
| Structural / Foundations / Supports | Interface fact applies to PKG-036; electrical buildings shall be located in general purpose areas for convenient power distribution. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-BDE626F7DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, hazardous area / electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Building delivery model | Electrical buildings in source materials are delivered as shop-built modules. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (Shop) |
| Building location | TBD. No accessible source slice fixes the site coordinates, layout area, or adjacency for the workbook-defined PKG-036 building (CONFLICT pending on building tag 830-1 — see CT-036-01-001). | Source gap |
| Foundations / supports / grading | Structural / foundations / supports and grading interfaces apply; package-specific foundation, grading, and spill-containment basis is TBD. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` |
| Detailed equipment list (breakers, MCC, transformers, protection) | TBD pending vendor package datasheet and accessible package-specific source. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-036-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-036`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-036-01_scope-of-work`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-036`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-036-01_scope-of-work`.
- `SCOPE_LEDGER.csv`, row `SOW-0037`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis: plant power distribution; voltage/service table; 6.9 kV motor control; electrical-buildings list; grounding and bonding; cable tray/conduit; electrical-building HVAC.
- `_Sources/26020-Package_Requirements.docx`, not opened as a parseable source slice in this run; no PKG-036 package match recorded.
