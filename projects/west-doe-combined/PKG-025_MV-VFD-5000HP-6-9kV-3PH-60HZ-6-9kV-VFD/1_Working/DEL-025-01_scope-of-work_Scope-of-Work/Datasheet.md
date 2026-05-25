# Datasheet: DEL-025-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-025-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-025 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-025 |
| Package name | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD | Gate 7 `PACKAGE_REGISTER.csv` row PKG-025; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 27 |
| Workbook ID / row | ID 25 / row 27 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 27 |
| WBS | 01 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 27 |
| Tracking number | 26020-01-30-016 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 27 |
| Discipline | Electrical | `_CONTEXT.md` Identity; workbook Packages row 27 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-025 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis |
| Scope item | SOW-0026 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0026 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged equipment | TBD; no tag number is exposed in the accessible workbook row or Gate 7 package row for this specific 5000HP/6.9kV VFD package. | Workbook Packages row 27; Gate 7 `PACKAGE_REGISTER.csv` row PKG-025 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility MV service basis (6.9 kV) | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; applies to facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Power Distribution table, line 2935 |
| 6.9 kV neutral grounding | Each 6.9 kV transformer grounded using a 100 A, 10 s neutral grounding resistor; operates as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 |
| 6.9 kV MV cable basis | Three-conductor copper TECK cable rated 8 kV with 100 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3008 |
| MV motor starting context | Facility 6.9 kV MCC provides mechanically latched fused contactors with motor protection relays and an Ethernet port to the plant PLC; Starting VFDs are provided for the KM-2150/2250 Inlet/Sales Gas Compressor motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 |
| Facility electrical building context | Electrical buildings may house MV VFDs alongside 13.8 kV main switchgear, MV MCCs, MV reduced-voltage soft starters, 600 V MCCs, UPS systems, distribution transformers, and plant PLC control panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Applicable package interfaces | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 27; Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-025 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-025 |
| Driven motor identity (specific application) | TBD; the 5000 hp / 6.9 kV motor or compressor served by this VFD is not unambiguously named for PKG-025 in accessible source slices. The DBM names a Starting VFD for the inlet/sales compressor motors (KM-2150/2250) on the 6.9 kV bus, but that compressor driver is documented at 6,700 hp rather than 5,000 hp. ASSUMPTION: this package may serve a different 5,000 hp / 6.9 kV process driver; confirm against detailed engineering / vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 893, 2935, 2955 |
| VFD topology, output filter, harmonic mitigation, isolation/input transformer, bypass, enclosure rating, cooling, dimensions, weights | TBD; not stated in accessible source slices for this package. | Workbook Packages row 27; Gate 7 PKG-025 rows; DBM electrical sections |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering or design to the EPC Integrator. |
| Electrical Power | Identify the package as a 6.9 kV MV power interface and require coordination with facility MV distribution, neutral grounding (100 A, 10 s NGR), and MV cable basis. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review, including equipment grounding and integration with the facility grounding system. |
| I&C / Control Cabling | Carry I&C cabling and control interfaces (VFD start/stop, speed reference, status/alarms, motor protection relay integration) as scope requiring EPC coordination with plant PLC and protective relay schemes. |
| Communications / Network | Carry communications/network as an interface (e.g., Ethernet to plant PLC central control panel for data acquisition) requiring EPC coordination. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, removal-path, and handoff coordination. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; package-specific loads, dimensions, and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-025-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-025.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0026.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-025-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-025 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 27.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical power distribution, MV motor starting, electrical buildings, grounding, and MV cabling sections.
