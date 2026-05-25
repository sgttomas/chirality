# Datasheet: DEL-010-01_scope-of-work - Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-010-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-010 - Controls system design and integration |
| Workbook ID / row | 10 / row 11 |
| WBS | 03 |
| CoA tracking number | 26020-01-32-001 |
| Discipline | Controls |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Scope item | SOW-0010 |
| Supported objectives | OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-009; OBJ-010 |

Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-010-01_scope-of-work`; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row with ID 10.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Controls system design and integration | Workbook row 11; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010` |
| Package discipline | Controls | Workbook row 11; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010` |
| Package basis | Workbook-defined Controls package for WBS 03 with recorded physical interfaces | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010` |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010` |
| Mandatory scope-of-work content | Package scope, tagged-equipment basis where source-supported, source rows, WBS, discipline, boundaries, package function, whole-facility integration narrative, and responsibility assignment record | Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-010-01_scope-of-work` |
| Tagged equipment list | TBD; no deliverable-specific tagged equipment list was available in the accepted references for this SOW | `_REFERENCES.md`; Gate 7 `ARTIFACT_REGISTER.csv` notes "where source-supported" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility context | 03-25 compressor station and liquids hub scope | Gate 7 `OBJECTIVE_REGISTER.csv` row `OBJ-002`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01 |
| Control-system role | Centralized monitoring and control for the 03-25 Compressor Station and Liquids Hub; BPCS is primary process control except compression unit controls, which are standalone and integrated for monitoring and alarming | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 Control System Basis |
| Network condition | I/O Network is segregated from other networks and uses redundant Ethernet communications with Parallel Redundancy Protocol | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 Control System Basis |
| Package control interface condition | Final package data maps, permissive logic, trip interfaces, and alarm priorities remain vendor-integration/detail-design items | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 Unit Control Systems and Package Interfaces |
| Instrument-air control condition | 03-25 instrument-air supply is from 04-25; local 03-25 instrument-air compressor controls are not to be added | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 Instrument Air Interface Controls |
| Shutdown-interface condition | Final trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities remain detailed-design deliverables | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-14 Unit Shutdown Interfaces |

## Construction

| Interface type | Applicability | Source |
|---|---|---|
| Process Piping | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-D8F0EE6268` |
| Utility Piping | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-B417C160D6` |
| Relief / Flare / Vent | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-0F29FF779E` |
| Electrical Power | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-7692ABF6DF` |
| I&C / Control Cabling | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-0594D83117` |
| Communications / Network | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-BBCAEE6BE3` |
| Building HVAC / Services | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-E721E064DB` |
| Fire & Gas / Safety Systems | YES | Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` row `IFC-84EB36C954` |

Interface review note: confirm whether controls power-panel interfaces should be tracked separately. Gate 6 disposition states controls power-panel interfaces remain interface facts/artifacts under the package datasheet; no separate package or deliverable is created. Source: Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_REGISTER.csv`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row with ID 10
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01, SEC-12, SEC-13, SEC-14, SEC-15
