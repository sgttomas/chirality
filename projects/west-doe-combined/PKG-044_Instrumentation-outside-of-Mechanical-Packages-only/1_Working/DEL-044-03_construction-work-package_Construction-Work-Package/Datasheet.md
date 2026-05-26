# Datasheet — DEL-044-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-044-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-044 |
| ParentWorkbookID | 44 |
| PackageName | Instrumentation (outside of Mechanical Packages only) |
| Discipline | Instrumentation |
| WBS | 02 |
| CoA tracking | 26020-01-32-002 |
| Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Covers Scope Items | SOW-0045 |

Source: DELIVERABLE_REGISTER.csv row 246; PACKAGE_REGISTER.csv row 46; SCOPE_LEDGER.csv row 46 (GATE-07 snapshot).

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Instrumentation scope outside of Mechanical Packages | PACKAGE_REGISTER.csv row 46 |
| Construction outcome | Physical installation, build, inspection, turnover, and tie-in to the larger facility systems | DELIVERABLE_REGISTER.csv row 246 |
| Anticipated artifacts | Construction work package; Installation and tie-in workface plan; Construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row 246; ARTIFACT_REGISTER.csv rows 979-981 |
| Applicable interface types | Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network | PACKAGE_REGISTER.csv row 46; INTERFACE_REGISTER.csv rows 302-306 |
| Scope inclusion note | "Field supports, power, and comms not marked unless confirmed by package scope." Gate 6 disposition: instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | PACKAGE_REGISTER.csv row 46; INTERFACE_REGISTER.csv rows 302-306 |
| Package exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv row 46 |
| Ownership model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | PACKAGE_REGISTER.csv row 46 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Authoritative basis | Workbook Packages row 46 | PACKAGE_REGISTER.csv row 46 |
| Carrier scope decision | DEC-001 carries the workbook-defined Instrumentation package as a distinct flat project package for WBS 02 | SCOPE_LEDGER.csv row 46 |
| Companion sibling deliverables | DEL-044-01 Scope of Work; DEL-044-02 Package Datasheet; DEL-044-04 EPC/Instrumentation Discipline Production Package | SCOPE_LEDGER.csv row 46 |
| Supported objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010 | DELIVERABLE_REGISTER.csv row 246 |
| Source slice provenance | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (referenced by PACKAGE_REGISTER row 46); DBM-Deepcut/4-25_Deepcut_DBM.md (referenced by supported objectives) | PACKAGE_REGISTER.csv row 46; OBJECTIVE_REGISTER.csv rows for OBJ-005/006/007/008 |

## Construction (composition of the deliverable artifact)

The Construction Work Package as a deliverable artifact comprises:

1. **Construction work package narrative** (ART-98EDB38A63) — Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. Source: ARTIFACT_REGISTER.csv row 979.
2. **Installation and tie-in workface plan** (ART-48F9265F2F) — Workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. Source: ARTIFACT_REGISTER.csv row 980.
3. **Construction interface and turnover checklist** (ART-C05FF15A97) — Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. Source: ARTIFACT_REGISTER.csv row 981.

Interface facts that condition construction scope (ASSUMPTION: directionally relevant; carried in DEL-044-02 Package Datasheet but used by construction planning):

| Interface ID | Discipline interface | Source |
|---|---|---|
| IFC-A0182B4C75 | Process Piping | INTERFACE_REGISTER.csv row 302 |
| IFC-9E42D79051 | Utility Piping | INTERFACE_REGISTER.csv row 303 |
| IFC-0DD8B45540 | Electrical Power | INTERFACE_REGISTER.csv row 304 |
| IFC-20C7248CDB | I&C / Control Cabling | INTERFACE_REGISTER.csv row 305 |
| IFC-0664000480 | Communications / Network | INTERFACE_REGISTER.csv row 306 |

Detailed equipment list, tag list, quantities, weights, lift plans, and erection sequences: TBD (no deliverable-specific source slices copied into the deliverable folder; location TBD pending workbook row 46 slice extraction).

## References

- DELIVERABLE_REGISTER.csv row 246 (GATE-07 snapshot)
- PACKAGE_REGISTER.csv row 46 (GATE-07 snapshot)
- SCOPE_LEDGER.csv row 46 (GATE-07 snapshot)
- ARTIFACT_REGISTER.csv rows 979-981 (GATE-07 snapshot)
- INTERFACE_REGISTER.csv rows 302-306 (GATE-07 snapshot)
- OBJECTIVE_REGISTER.csv rows for OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010 (GATE-07 snapshot)
- Workbook Packages row 46 (cited by all of the above; underlying workbook at `_Sources/26020-Packages_Interfaces_4_export.xlsx`; location TBD for clause-level extraction)
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (referenced by PACKAGE_REGISTER row 46)
