# Datasheet: DEL-096-05 — Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-096-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-096` |
| Package | Tanks, Sour Condensate (API 650) |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (producer) with EPC Integrator (interface/integration review) |
| Authoritative Basis | GATE-07 PROJECT_DECOMP snapshot 2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject equipment package | API 650 sour condensate storage tanks (PKG-096 scope, 03-25 Liquids Hub sour condensate service) | `_CONTEXT.md`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 40, lines 404-411 |
| Equipment count and size (context) | Sour condensate storage tanks within the eleven 3,800 bbl condensate tank set; functional allocation per DBM includes two sour inlet condensate tanks and four sour condensate tanks (basis subject to final tank register) | `3-25_Comp_and_Liquids_DBM.md` lines 406, 410-411 |
| Governing design standard (context) | API 650 (per package title); applicable clauses TBD — source clause text not locally accessible | `_CONTEXT.md`; PKG-096 title — location TBD |
| Vendor document register | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts; `3-25_Comp_and_Liquids_DBM.md` line 617 ("Package deliverables shall include … vendor document registers") |
| Vendor document submittals | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Source vendor document rows (as artifacts) | Required where available | `_CONTEXT.md` Anticipated Artifacts; Notes |
| Turnover records | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Scope items covered | `SOW-0217`, `SOW-0218`, `SOW-0219`, `SOW-0220` | `_CONTEXT.md` |
| Objectives supported | `OBJ-002` through `OBJ-010` | `_CONTEXT.md` (ASSUMPTION — package-grouping heuristic; not human-confirmed) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient design envelope | -40 deg C to +35 deg C; -40 deg C minimum governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies | `3-25_Comp_and_Liquids_DBM.md` lines 94-101, 145 |
| Service | Sour condensate (sour service); tanks externally insulated/heated per API-650 Modified analog basis applied to liquids hub tanks | `3-25_Comp_and_Liquids_DBM.md` lines 406, 421 (produced-water tank analogue); sour-condensate-specific construction details TBD |
| Submission lifecycle | Documents progress from vendor submittal through review/comment cycles to accepted turnover records | ASSUMPTION (industry convention); source location TBD in `26020-Package_Requirements.docx` package heading 48 |
| EPC interface | EPC Integrator performs interface/integration review of vendor documents | `_CONTEXT.md` ResponsibleParty |

## Construction

| Element | Description | Source |
|---|---|---|
| Vendor Document Register | Tabular index of all required vendor documents for PKG-096: document number, title, type, revision, submittal status, review status, turnover status, applicable SOW item(s) | ASSUMPTION (industry convention for vendor document registers); register requirement: `3-25_Comp_and_Liquids_DBM.md` line 617 |
| Vendor Document Submittals | The vendor-produced document set (datasheets, drawings, calculations, certifications, manuals, test records) submitted against the register | `_CONTEXT.md`; specific list TBD pending `26020-Package_Requirements.docx` heading 48 |
| Source-Required Vendor Documentation | Documents the source (`26020-Package_Requirements.docx` heading 48) explicitly requires for this package class | location TBD (docx not converted to accessible markdown in workspace) |
| Turnover Records | Final accepted/closed document set, transmittal manifests, and acceptance evidence transferred at package turnover | `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible; mechanical-package deliverable convention at line 617; site/equipment context lines 40, 94-101, 145, 404-411, 421)
- `_Sources/26020-Package_Requirements.docx`, package heading 48 — referenced by `_CONTEXT.md`; NOT locally accessible as markdown; clause-level content **TBD**
- GATE-07 PROJECT_DECOMP snapshot 2026-05-24 (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv)
- `26020-Packages_Interfaces_4_export.xlsx` — referenced by source set; not directly accessible as markdown; interface-level details **TBD**
