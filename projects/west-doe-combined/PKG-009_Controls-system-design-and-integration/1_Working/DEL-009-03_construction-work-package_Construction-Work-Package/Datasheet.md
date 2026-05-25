# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-009-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-009 - Controls system design and integration |
| Workbook / WBS basis | Workbook Packages row 10; WBS 02 |
| Discipline | Controls |
| Deliverable type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0009 |
| Current drafting phase | Phase 2.2, Passes 1-2 |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row for `DEL-009-03_construction-work-package`; `PACKAGE_REGISTER.csv` row for `PKG-009`; `SCOPE_LEDGER.csv` row for `SOW-0009`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Mandatory EPC anchor deliverable | Yes. Every approved package includes Scope of Work, Package Datasheet, and Construction Work Package deliverables. | `PROJECT_DECOMP.md` lines 118-127 and 205 |
| Package description | Workbook-defined Controls package for controls system design and integration under WBS 02 with recorded physical interfaces. | `PACKAGE_REGISTER.csv` row `PKG-009` |
| CWP purpose | Describe how the package will be physically installed, built, inspected, turned over, and tied into larger facility systems. | `DELIVERABLE_REGISTER.csv` row `DEL-009-03_construction-work-package` |
| Required artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` rows for `DEL-009-03_construction-work-package` |
| Declared upstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared. | `_DEPENDENCIES.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Applicable package interfaces | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. | Workbook export `26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row for WBS 02 controls package; `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` rows for `PKG-009` |
| Control-system field wiring basis | BPCS process and safety devices are wired to the nearest Remote I/O control panel where practical. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` sections around lines 806, 840, and table at line 853 |
| Safety interface basis | Unit control panel push buttons shall trip local unit emergency shutdown mode where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 3232, 3272, and 3304 |
| Electrical building/control panel installation context | Electrical buildings may house plant PLC control panels and network racks; EMT conduit is used for adjacent equipment such as control panels to contactor panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2973 and 2979 |
| Ambient design condition impacting controls equipment | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 |

## Construction

| Item | Construction data |
|---|---|
| Work package boundaries | Covers physical installation, construction, tie-in, inspection, turnover, and connection to larger facility systems for the PKG-009 controls system design and integration package. |
| Workface planning content | Must include installation and tie-in planning evidence for adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. Source: `ARTIFACT_REGISTER.csv` row `ART-80DA88C819`. |
| Interface/turnover checklist content | Must include construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. Source: `ARTIFACT_REGISTER.csv` row `ART-1D954E6A4A`. |
| Package-specific installation locations | TBD. No deliverable-specific location plan or drawing slice was copied during PREPARATION. |
| Package-specific installation quantities | TBD. No bill of materials, I/O count, panel schedule, cable schedule, or construction quantity takeoff was provided in the accessible references for this deliverable. |
| Controls power-panel treatment | NEEDS_HUMAN_RULING: workbook/source register asks whether controls power-panel interfaces should be tracked separately; Gate 6 disposition keeps them as interface facts/artifacts under the package datasheet, with no separate package or deliverable created. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 snapshot: `PROJECT_DECOMP.md`, `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row for WBS 02 controls package
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
