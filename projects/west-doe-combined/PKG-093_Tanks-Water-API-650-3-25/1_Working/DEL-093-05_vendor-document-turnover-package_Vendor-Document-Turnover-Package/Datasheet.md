# Datasheet: DEL-093-05 — Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-093-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-093` |
| Package | Tanks, Water (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (producer) with EPC Integrator (interface/integration review) |
| Authoritative Basis | GATE-07 PROJECT_DECOMP snapshot 2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject equipment package | API 650 water storage tanks (PKG-093 scope, 03-25 Liquids Hub produced-water service) | `_CONTEXT.md`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Liquids Hub equipment basis" (line ~40) |
| Equipment count and size (context) | Seven 3,800 bbl produced-water tanks (package scope per current DBM basis) | `3-25_Comp_and_Liquids_DBM.md` line ~40 |
| Governing design standard (context) | API 650 (per package title); applicable clauses TBD | `_CONTEXT.md`; PKG-093 title — location TBD in source |
| Vendor document register | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts; DBM line 617 ("Package deliverables shall include … vendor document registers") |
| Vendor document submittals | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Source vendor document rows (as artifacts) | Required where available | `_CONTEXT.md` Anticipated Artifacts |
| Turnover records | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Scope items covered | `SOW-0229`, `SOW-0230`, `SOW-0231`, `SOW-0232` | `_CONTEXT.md` |
| Objectives supported | `OBJ-002` through `OBJ-010` | `_CONTEXT.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient minimum (design envelope context) | -40 deg C governs exposed equipment, package buildings, control panels, instrumentation unless more severe process/vendor condition applies | `3-25_Comp_and_Liquids_DBM.md` line 145 |
| Submission lifecycle | Documents progress from vendor submittal through review/comment cycles to accepted turnover records | ASSUMPTION (industry convention); source location TBD in `26020-Package_Requirements.docx` package heading 45 |
| EPC interface | EPC Integrator performs interface/integration review of vendor documents | `_CONTEXT.md` ResponsibleParty |

## Construction

| Element | Description | Source |
|---|---|---|
| Vendor Document Register | Tabular index of all required vendor documents for PKG-093: document number, title, type, revision, submittal status, review status, turnover status, applicable SOW item(s) | ASSUMPTION (industry convention for vendor document registers); register requirement: DBM line 617 |
| Vendor Document Submittals | The vendor-produced document set (datasheets, drawings, calculations, certifications, manuals, test records) submitted against the register | `_CONTEXT.md`; specific list TBD pending `26020-Package_Requirements.docx` heading 45 |
| Source-Required Vendor Documentation | Documents the source (26020-Package_Requirements.docx heading 45) explicitly requires for this package class | location TBD (docx not converted to accessible markdown in workspace) |
| Turnover Records | Final accepted/closed document set, transmittal manifests, and acceptance evidence transferred at package turnover | `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible; mechanical-package deliverable convention at line 617; site/equipment context lines 40, 145, 161, 176, 182-194)
- `_Sources/26020-Package_Requirements.docx`, package heading 45 — referenced by `_CONTEXT.md`; NOT locally accessible as markdown; clause-level content **TBD**
- GATE-07 PROJECT_DECOMP snapshot 2026-05-24 (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv)
- `26020-Packages_Interfaces_4_export.xlsx` — referenced by source set; not directly accessible as markdown; interface-level details **TBD**
