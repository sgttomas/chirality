# Datasheet: DEL-022-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-022-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-022 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 |
| Package name | 5kV SWITCHGEAR EQUIPMENT | Gate 7 `PACKAGE_REGISTER.csv` row PKG-022; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 24 |
| Workbook ID / row | ID 22 / row 24 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 24 |
| WBS | 01 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 24 |
| Tracking number | 26020-01-30-013 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 24 |
| Discipline | Electrical | `_CONTEXT.md` Identity; workbook Packages row 24 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis; `_CONTEXT.md` Notes |
| Scope item | SOW-0023 | `_CONTEXT.md` Covers Scope Items; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-022-01 |
| Supported objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-022-01 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-022-01 |
| Tagged equipment | TBD; no equipment tag is exposed in the accessible workbook row or Gate 7 package row for PKG-022. The Deepcut DBM does not enumerate a 5 kV-class switchgear bus or tag list for this package. See Conflict Table HR-022-01-02. | Workbook Packages row 24; Gate 7 `PACKAGE_REGISTER.csv` row PKG-022; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical sections (lines 2917-2973, 2935-2936, 3007-3009) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility MV electrical context | Deepcut DBM defines facility MV services as 6.9 kV (large motors rated 5,500 hp and above), 4.160 kV (motors 250 hp up to 5,500 hp), and a 13.8 kV main distribution bus stepping down to local electrical buildings. A discrete 5 kV facility bus is not described. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2925, 2935-2936 |
| 5 kV insulation class basis | DBM specifies 4.160 kV medium-voltage cables as three-conductor copper TECK cable rated 5 kV with 100 percent insulation. The "5 kV" designation in the package name may refer to a 4.16 kV system using 5 kV-class equipment/insulation, not a discrete 5 kV bus. See Conflict Table HR-022-01-01. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3009; Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 |
| Package interfaces | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 24; Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials (Gate 7 record). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 |
| Design values for switchgear bus rating, short-circuit rating, breaker type, lineup configuration, BIL, enclosure, environmental rating, footprint, weights, and support loads | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 24; Gate 7 PKG-022 rows; DBM electrical sections |
| Companion electrical-building package | A separate package, PKG-037 "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)", appears in the Gate 7 register; the relationship between PKG-022 (equipment) and PKG-037 (building) is not explicitly stated in the accessible source slices and is carried as a dependency context, not a constraint. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-037; `_DEPENDENCIES.md` |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering, package design, vendor documentation, or physical equipment package supply to the EPC Integrator. |
| Electrical Power | Identify the package as a medium-voltage switchgear interface within the Deepcut facility electrical distribution; coordinate with the 13.8 kV main distribution, the 4.16 kV / 5 kV-class system context, and any downstream MCC/transformer feeders identified by detailed design. Specific bus assignment and feeder list are TBD pending source clarification. |
| Grounding / Bonding | Carry grounding and bonding as an interface requiring EPC review and construction coordination at the switchgear lineup, neutral grounding (low-resistance grounded per DBM medium-voltage basis), and downstream circuits. |
| I&C / Control Cabling | Carry control, protection, and monitoring cabling between the switchgear, plant control system, and downstream loads as an interface; specific protection schemes, relay basis, I/O list, and control philosophy are TBD pending vendor data. |
| Communications / Network | Carry communications/network as an interface (e.g., Ethernet connection to the plant PLC consistent with the DBM EtherNet basis for MV motor control); specific protocols, ports, and addressing are TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, clearance, rear/front access, and handoff coordination. |
| Structural / Foundations / Supports | Carry structural and support requirements (housekeeping pad, anchorage, building penetrations) as interface scope; package-specific loads, footprint, and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-022-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, package anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-022 (and contextual row PKG-037).
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-022-01_scope-of-work.
- Gate 7 `ARTIFACT_REGISTER.csv`, rows for DEL-022-01.
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-022-01.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-022 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 24.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and MV services sections (lines 2917-2973, 2935-2936, 3007-3009).
