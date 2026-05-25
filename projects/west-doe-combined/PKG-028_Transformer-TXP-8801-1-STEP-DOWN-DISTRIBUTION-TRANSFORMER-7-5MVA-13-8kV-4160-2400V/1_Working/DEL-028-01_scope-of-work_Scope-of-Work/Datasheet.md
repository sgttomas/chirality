# Datasheet: DEL-028-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-028-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-028 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| Package name | Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 30 |
| Workbook ID / row | ID 28 / row 30 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 30; Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| WBS | 01 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| Tracking number | 26020-01-30-019 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-028-01 |
| Scope item covered | SOW-0029 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0029 |
| Objectives supported | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-028-01 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged equipment | Equipment tag `TXP-8801-1` is exposed in the package name; no additional tagged equipment is exposed in the accessible workbook row or Gate 7 package row. | Workbook Packages row 30; Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Nameplate rating (identity-level, source-derived label) | 7.5 MVA, 13.8 kV primary / 4160 V and 2400 V secondaries (carried as the source-derived package name string, not as a verified vendor nameplate). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028; workbook Packages row 30 |
| Facility electrical context | Facility primary distribution is 13.8 kV from a 25 kV / 13.8 kV, 50 MVA utility transformer; 13.8 kV switchgear is the plant main power distribution center and feeds step-down transformers radially to electrical buildings/loads across the facility. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2937 |
| Package interfaces | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 30; Gate 7 `INTERFACE_REGISTER.csv` rows IFC-5A6FBABCBA, IFC-22E75E0E48, IFC-487236B7E5, IFC-FD9BCC3585, IFC-2C9EC16D97, IFC-5C19FEBFC8, IFC-B1AD88E9C0 |
| Foundation / support context | Oil-filled transformers are generally installed on structural steel transformer bases; large oil-filled transformers shall be spaced per CEC requirements; secondary containment requirements shall be reviewed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2745, 2947-2949 |
| Grounding context | Each 600 V transformer has 5 A continuous high-resistance grounding; major electrical equipment is connected to the ground grid at two points; distribution transformers have a separate copper ground conductor sized per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2985-2991 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 (Exclusions = TBD) |
| Package-specific design values | TBD for vendor-specific nameplate confirmation, impedance, vector group, taps, cooling class (e.g., ONAN/ONAF), insulation class, BIL, fluid type, conservator/free-breathing configuration, accessories (Buchholz, sudden-pressure, RTDs), weights, dimensions, and support loads. | Workbook Packages row 30; Gate 7 PKG-028 rows; DBM Deepcut electrical section |
| Secondary voltage configuration (4160 V and 2400 V) | TBD whether the package is a dual-secondary unit, a tertiary-winding unit, or a sectionalized arrangement; not described in accessible source slices. | Workbook Packages row 30; DBM Deepcut electrical section |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering/design to the EPC Integrator. |
| Electrical Power | Carry as primary interface: 13.8 kV primary feed from facility 13.8 kV switchgear and 4160 V / 2400 V secondary distribution boundaries; package-specific feeder routing, breaker assignments, and load allocations are `TBD` pending detailed electrical design. |
| Grounding / Bonding | Carry as interface requiring EPC review and construction coordination per DBM grounding basis; transformer-specific grounding (e.g., neutral grounding resistor sizing) is `TBD` pending detailed design. |
| Area / Exterior Lighting | Carry as interface; coordinate area lighting at the transformer pad/enclosure with facility lighting design. |
| I&C / Control Cabling | Carry as interface for transformer monitoring/protection cabling routing to associated control/protection panels. |
| Communications / Network | Carry as interface where transformer monitoring is networked to facility systems; specific protocol/path is `TBD`. |
| Maintenance Access | Carry as interface requiring layout and handoff coordination, including spacing per CEC. |
| Structural / Foundations / Supports | Carry as interface; structural steel transformer base, spacing, and secondary containment review per DBM; package-specific loads and support details `TBD` pending vendor data. |

## References

- `_CONTEXT.md`, DEL-028-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-028.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-028-01_scope-of-work.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0029.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-028 rows (seven interface types).
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-028-01 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 30.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical sections (lines 2660, 2745, 2917-2991).
