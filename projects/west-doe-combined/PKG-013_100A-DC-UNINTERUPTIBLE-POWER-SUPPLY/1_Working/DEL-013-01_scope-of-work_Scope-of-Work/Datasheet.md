# Datasheet: DEL-013-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-013-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-013 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-013 |
| Package name | 100A DC UNINTERUPTIBLE POWER SUPPLY | Gate 7 `PACKAGE_REGISTER.csv` row PKG-013; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 15 |
| Workbook ID / row | ID 13 / row 15 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 15 |
| WBS | 02 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 15 |
| Tracking number | 26020-02-30-004 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 15 |
| Discipline | Electrical | `_CONTEXT.md` Identity; workbook Packages row 15 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration and interfaces. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-013 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` lines 118-125 and decision DEC-013 |
| Scope item | SOW-0014 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0014 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged equipment | TBD; no tag number is exposed in the accessible workbook row or Gate 7 package row. | Workbook Packages row 15; Gate 7 `PACKAGE_REGISTER.csv` row PKG-013 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility electrical service context | UPS services are listed as 120 VAC / 125 VDC for control system, selected emergency/critical lighting, MV breaker control, and MV protective relay. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Electrical Power Distribution table, lines 734-736 |
| Package interfaces | Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 15; Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-013 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-013 |
| Design values for UPS capacity, autonomy, battery type, enclosure, chargers, DC distribution, and environmental rating | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 15; Gate 7 PKG-013 rows; DBM electrical table |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package design to the EPC Integrator. |
| Electrical Power | Identify the package as an electrical power interface and require coordination with facility UPS/electrical distribution basis. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination. |
| Maintenance Access | Carry maintenance access as an interface requiring layout and handoff coordination. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; package-specific loads and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-013-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, package anchor deliverable basis and DEC-013.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-013.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0014.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-013-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-013 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 15.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical power distribution table.
