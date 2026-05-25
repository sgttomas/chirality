# Datasheet: DEL-028-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-028-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-028` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 28 / row 30 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-019 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 30; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-028` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Package function | Step-down distribution transformer package, tag TXP-8801-1, with nameplate basis 7.5 MVA, primary 13.8 kV and secondary 4160/2400 V per workbook title. | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Primary distribution context | The 13.8 kV switchgear is the plant main power distribution center and distributes power radially through step-down transformers to facility electrical buildings and process loads. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "facility electrical system" / "13.8 kV switchgear" paragraphs (lines 2917-2919) |
| Primary voltage system basis | Medium-voltage services: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (line 2934) |
| Secondary voltage basis (4160 V) | TBD. The DBM voltage table identifies 13.8 kV and 600 V as the facility distribution voltages; the 4160 V and 2400 V secondaries named in the package title are not separately characterized in the accessible DBM source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| Construction type | TBD. The DBM identifies oil-filled transformers as a facility transformer type and notes general installation practice but does not confirm oil-filled vs dry-type, cooling class, or BIL for this specific 7.5 MVA TXP-8801-1 unit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Transformers" subsection (lines 2947-2951) |
| Neutral grounding | TBD for the 4160/2400 V secondary windings. DBM defines grounding for the BC Hydro utility transformer (200 A NGR), each 6.9 kV transformer (100 A NGR), and each 600 V transformer (5 A high-resistance), but does not specify the grounding scheme for a 7.5 MVA 13.8 kV/4160/2400 V unit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph (line 2985) |
| Standby / utility supply context | Facility power is supplied by BC Hydro at 13.8 kV; standby power is provided by TOU low-voltage MCC standby generators with transfer switches at the 600 V MCC level. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical system overview (line 2917) and standby paragraph (line 2943) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-5A6FBABCBA` |
| Grounding / Bonding | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-22E75E0E48` |
| Area / Exterior Lighting | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-487236B7E5` |
| I&C / Control Cabling | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-FD9BCC3585` |
| Communications / Network | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-2C9EC16D97` |
| Maintenance Access | Interface fact applies to PKG-028 and must be represented in the package interface requirements matrix. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-5C19FEBFC8` |
| Structural / Foundations / Supports | Interface fact applies to PKG-028; transformers are generally supported on precast concrete bearing foundations per DBM. Detailed loading is TBD. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-B1AD88E9C0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table (line 2745) |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers shall be provided for maintenance and operational testing. Distribution transformers require a separate copper ground conductor sized per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (lines 2989-2991) |
| Medium-voltage cabling | 13.8 kV connection on the primary side shall use 3-conductor copper TECK cable rated 15 kV with 133% insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table (line 3007) |
| Oil-filled transformer spacing | If selected as oil-filled, large oil-filled transformers shall be spaced per CEC and secondary containment shall be reviewed; selection shall avoid or limit containment where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers subsection (lines 2947-2949) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Facility integration, interfaces, tie-ins, constructability | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Installation location | TBD. Workbook and DBM source slices do not assign PKG-028 to a specific building, pad, or coordinate. WBS 01 places the package within the WBS-01 facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `PACKAGE_REGISTER.csv` row `PKG-028` |
| Foundations / supports | Transformers are generally supported on precast concrete bearing foundations; package-specific loading, anchor pattern, and oil-containment foundation features are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table (line 2745); `INTERFACE_REGISTER.csv` |
| Cooling, BIL, impedance, tap range, vector group | TBD. Not defined by the accessible DBM source slice for this specific 7.5 MVA TXP-8801-1 unit; expected from vendor data or detailed electrical engineering. | Source gap; `26020-Package_Requirements.docx` not opened — no accessible PKG-028 package-specific slice located during this run. |
| Bushings, surge arresters, neutral grounding equipment | TBD pending vendor data and protection coordination study. | Source gap |
| Monitoring / I&C scope | I&C / Control Cabling interface applies; specific RTD, thermal, oil-level, gas, and Buchholz signals plus their routing to plant PLC/protective relays are TBD. | Workbook Packages row 30; `INTERFACE_REGISTER.csv` `IFC-FD9BCC3585` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-028-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-028`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-028-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-028` (7 applicable interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-028-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 30.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis slices for 13.8 kV facility distribution, transformer installation, grounding, medium-voltage cabling, foundations, and standby power.
- `_Sources/26020-Package_Requirements.docx`, not opened; no PKG-028-specific slice resolved during this run.
