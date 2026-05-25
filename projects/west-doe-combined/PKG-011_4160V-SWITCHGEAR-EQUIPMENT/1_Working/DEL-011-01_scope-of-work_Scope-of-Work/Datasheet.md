# Datasheet: DEL-011-01 Scope of Work

## Identification

| Attribute | Value |
|---|---|
| Deliverable ID | DEL-011-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-011 - 4160V SWITCHGEAR EQUIPMENT |
| Parent workbook ID / row | Workbook ID 11 / Workbook Packages row 13 |
| WBS | 02 |
| CoA tracking number | 26020-02-30-002 |
| Discipline | Electrical |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Covered scope item | SOW-0012 |
| Supported objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 |

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for DEL-011-01; Gate 7 `PACKAGE_REGISTER.csv` row for PKG-011; Gate 7 `SCOPE_LEDGER.csv` row SOW-0012.

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package identity | Workbook-defined vendor-responsible Electrical package named `4160V SWITCHGEAR EQUIPMENT`. Source: Gate 7 `SCOPE_LEDGER.csv` row SOW-0012. |
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-011. |
| Scope-of-work purpose | Integrator-authored package scope, function, tagged-equipment basis, source rows, WBS, discipline, and boundaries. Source: Gate 7 `ARTIFACT_REGISTER.csv` row ART-4FE41463DD. |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01. |
| Interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Gate 7 `INTERFACE_REGISTER.csv` rows IFC-59155DCD8A through IFC-680C970D3C. |

## Conditions

| Condition | Value |
|---|---|
| Upstream dependencies | None declared during PREPARATION. Source: `_DEPENDENCIES.md`. |
| Downstream dependencies | None declared during PREPARATION. Source: `_DEPENDENCIES.md`. |
| Blocker maturity threshold | INITIALIZED by coordination default; advisory only and limited to declared dependency edges. Source: `_DEPENDENCIES.md`; `_Coordination/_COORDINATION.md`. |
| Source limitations | No deliverable-specific source slices were copied during PREPARATION. Drafting uses the Gate 7 snapshot and locally accessible DBM source slices listed in `_REFERENCES.md`. |
| Package exclusions | TBD; no package-specific exclusions stated in source materials. Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-011. |

## Construction

The scope-of-work document is an EPC Integrator production artifact for the PKG-011 vendor-owned electrical package. It should identify the package, source row, WBS, responsibility split, package boundaries, integration interfaces, and the whole-facility integration narrative without assigning vendor engineering/design work to the EPC Integrator. Source: Gate 7 `PROJECT_DECOMP.md` Section 7 and Decision DEC-006.

Technical content should remain boundary-level unless supported by the DBM or Gate 7 registers. The 03-25 DBM identifies a 4160V MCC serving large 4000V motors, including inlet compressors KM-2150 and KM-2250, with field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12, `4160V MCC`.

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `PROJECT_DECOMP.md`, Sections 5, 7, 10, and 11
- Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-011-01 row
- Gate 7 `PACKAGE_REGISTER.csv`, PKG-011 row
- Gate 7 `SCOPE_LEDGER.csv`, SOW-0012 row
- Gate 7 `ARTIFACT_REGISTER.csv`, ART-4FE41463DD through ART-8698ECE3AB
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-011 rows
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-011-01 rows
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12
