# Datasheet: DEL-033-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-033-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-033 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Package name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033; workbook Packages row 35 |
| Workbook ID / row | ID 33 / row 35 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| WBS | 02 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Tracking number | 26020-02-30-024 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis |
| Scope item | SOW-0034 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0034 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged equipment | TBD; no individual tag numbers are exposed in the accessible Gate 7 package row or workbook row 35 for the package itself; the DBM identifies the 4160V MCC and references inlet compressors KM-2150 and KM-2250 served from the 4160V system, but does not enumerate switchgear lineup tags. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 752-754 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility electrical service context — incoming | 13.8 kV, 3 phase, 3 wire, 60 Hz LRG, sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 732, 740 |
| Facility electrical service context — medium voltage | 4,160 V, 3 phase, 3 wire, 60 Hz LRG; serves process AC inverter-drive motors from 250 hp to 5,500 hp. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 733 |
| Source of 4,160 V supply | 13.8 kV to 4.16 kV, 12 MVA transformer feeding the 4160V MCC for 4000V motors. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 744 |
| Electrical building scope basis | Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems; area classification, building HVAC, and remote distribution centres shall be coordinated with hazardous area classification and controls architecture. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 764-766 |
| Cable/conduit separation basis | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 768 |
| Package interfaces (flagged YES) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Gate 7 `INTERFACE_REGISTER.csv` PKG-033 rows; Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 |
| Design values for switchgear lineup, bus rating, short-circuit/withstand rating, breaker count and ratings, protective relaying, enclosure/NEMA rating, building dimensions, HVAC capacity, foundation loads, ventilation, fire/gas detection scheme | TBD; not present in accessible source slices for this deliverable. | Gate 7 PKG-033 rows; DBM electrical sections |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package design or vendor documentation production to the EPC Integrator. |
| Electrical Power | Coordinate the 13.8 kV incoming feed from 04-25 and the 13.8 kV / 4.16 kV / 12 MVA transformer interface; coordinate facility tie-in to the 4160V distribution and downstream MCC loads. |
| Grounding / Bonding | Carry facility grounding/bonding (LRG basis for MV) and ground grid tie-in as interface scope requiring EPC review and construction coordination. |
| Area / Exterior Lighting | Carry exterior lighting at the electrical building as an interface requiring layout and tie-in coordination. |
| I&C / Control Cabling and Communications / Network | Carry control cabling and network/EtherNet tie-in to the plant PLC central control panel as interfaces; preserve separation from MV power circuits. |
| Building HVAC / Services | Carry building HVAC/ventilation tie-in and coordination with hazardous area classification as interface scope. |
| Fire & Gas / Safety Systems | Carry facility F&G tie-in for the electrical building as interface scope. |
| Maintenance Access | Carry equipment access, breaker racking clearances, and laydown coordination as interface scope. |
| Grading / Site Drainage / Spill Containment, Drain / Containment, Utility Piping | Carry site grading, drainage, containment, and utility piping tie-ins as interface scope; package-specific drainage/containment values TBD. |
| Structural / Foundations / Supports | Carry building/foundation and equipment support requirements as interface scope; package-specific loads and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-033-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-033.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0034.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-033-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-033 rows (twelve YES interfaces).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 35.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification, System Voltages, Incoming Power and Transformers, 4160V MCC, and Electrical Buildings sections.
