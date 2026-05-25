# Datasheet: DEL-035-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-035-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-035 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-035 |
| Package name | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-035; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 37 |
| Workbook ID / row | ID 35 / row 37 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 37 |
| WBS | 01 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 37 |
| Tracking number | 26020-01-30-026 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 37 |
| Discipline | Electrical | `_CONTEXT.md` Identity; workbook Packages row 37 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration and interfaces. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-035 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` package anchor deliverable basis |
| Scope item | SOW-0036 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0036 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged building identifier | 810-1 (13.8kV Switchgear Electrical Building) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings table, row "810-1 13.8kV Switchgear Electrical Building" |
| Building delivery basis | Shop (pre-engineered electrical building) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings table, row "810-1 13.8kV Switchgear Electrical Building" |
| Housed equipment scope | Electrical building shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems; building area classification, HVAC, and remote distribution centres shall be coordinated with hazardous area classification and controls architecture. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` electrical buildings narrative |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility electrical role | 810-1 houses the plant main 13.8 kV switchgear; the 13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center with sufficient capacity to distribute power to facility electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (lines 2917-2927) |
| Incoming source basis | BC Hydro utility supply feeds a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer; the 13.8 kV switchgear bus shall be sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (lines 2917) |
| Downstream distribution targets | Radial step-down distribution from 13.8 kV switchgear to: 6.9 kV Inlet/Sales Compressor Electrical Building; 4.16 kV Acid Gas/Overheads Compressor Electrical Building; 600 V Acid Gas Compressor Electrical Building; 600 V Sales/Overheads Compressor Electrical Building; 4.16 kV / 600 V General Area/Tank Farm/Process Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (lines 2919-2925) |
| Shared-facility scope | Power distribution is shared between the 04-25 and 03-25 facilities; incoming power metering, protection coordination, and emergency / standby power scope split remain to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (line 2927) |
| System voltage basis | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded for BC Hydro utility distribution and facility medium-voltage backbone. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table (lines 2933-2934) |
| Package interfaces | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Workbook Packages row 37; Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-035 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-035 |
| Package-specific design values (switchgear ratings, bus continuous current, short-circuit rating, breaker count, lineup configuration, building dimensions, structural loads, HVAC heat load, fire & gas device list) | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 37; Gate 7 PKG-035 rows; DBM electrical basis |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package design to the EPC Integrator. |
| Electrical Power | Coordinate 25 kV utility feed, 25 kV/13.8 kV transformer connection, and radial 13.8 kV outgoing feeders to downstream electrical buildings. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring low-resistance grounding coordination, EPC review, and construction coordination. |
| Area / Exterior Lighting | Coordinate exterior building lighting tie-in and area classification at the building envelope. |
| I&C / Control Cabling | Coordinate control and protection cabling tie-ins to MV breakers and protective relays. |
| Communications / Network | Coordinate communications/network cabling between 810-1 and facility control architecture. |
| Building HVAC / Services | Carry building HVAC/ventilation coordination required for housed electrical equipment. |
| Fire & Gas / Safety Systems | Carry fire & gas / safety systems integration coordination at the building envelope. |
| Utility Piping | Carry utility piping interface coordination at the building envelope (TBD package-specific utility lines). |
| Drain / Containment | Carry drain/containment interface coordination at the building envelope. |
| Maintenance Access | Carry maintenance access as an interface requiring layout and handoff coordination. |
| Grading / Site Drainage / Spill Containment | Carry site grading, drainage, and containment coordination at the building footprint. |
| Structural / Foundations / Supports | Carry structural/foundation/support requirements as interface scope; package-specific loads and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-035-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, package anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-035.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0036.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-035-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-035 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 37.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings table and 13.8 kV switchgear narrative (System Voltages table).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings narrative.
