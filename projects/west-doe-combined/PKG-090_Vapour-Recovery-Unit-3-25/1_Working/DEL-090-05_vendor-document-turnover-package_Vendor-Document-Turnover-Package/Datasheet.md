# Datasheet — Vendor Document Turnover Package (DEL-090-05)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-090-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-090` |
| PackageName | Vapour Recovery Unit 3-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0249`, `SOW-0250`, `SOW-0251`, `SOW-0252` |
| Supports Objectives | `OBJ-002` .. `OBJ-010` (ASSUMPTION — package-heuristic association from decomposition mapping) |
| Source Reference | Workbook Packages row 100; `26020-Package_Requirements.docx` package heading 43 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject equipment | Vapour Recovery Unit 3-25 — two 200 hp electric-drive VRU compressor packages, 2 x 100 percent | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" (line 434-438); equipment list (line 40, 524) |
| Vendor scope | Vendor documentation set covering the vendor-engineered equipment package (DEL-090-04) | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv DEL-090-04 |
| Document register | Vendor document register listing all submittals and their status | `_CONTEXT.md` Anticipated Artifacts |
| Submittal classes | Drawings, datasheets, calculations, manuals, ITPs, certificates, test/inspection reports, spare-parts lists | ASSUMPTION — standard vendor turnover document classes; specific list `location TBD` pending extraction of `26020-Package_Requirements.docx` heading 43 |
| Turnover records | Final turnover record set evidencing acceptance | `_CONTEXT.md` Anticipated Artifacts |
| Document numbering convention | TBD | Source slice not locally accessible |
| Required submittal stages (IFR/IFA/IFC/As-Built) | TBD | Source slice not locally accessible |
| Review/return cycle durations | TBD | Source slice not locally accessible |
| Transmittal mechanism | TBD | Source slice not locally accessible |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Project facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15W6, BC | DBM SEC-01/SEC-02 (line 7, 85) |
| Package service | Tank-vapour and selected process-vent collection; discharge routed to 04-25 SOC suction under SCA-002 | DBM SEC-06 "Vapour Recovery" (line 436) |
| Interface partners | EPC Integrator (review/acceptance); DEL-090-06 consumes turnover evidence | DELIVERABLE_REGISTER.csv |

## Construction

This deliverable is a documentation package, not a physical construction. "Construction" in this datasheet refers to how the package is assembled:

| Element | Description |
|---|---|
| Document register | Authoritative index of all vendor documents tied to PKG-090 |
| Submittal set | The actual vendor-issued documents (drawings, datasheets, manuals, certificates, reports) |
| Turnover records | Final acceptance package: review log closeout, completed ITP records, certification statements, as-built revisions |
| Compilation owner | Package Vendor |
| Reviewer | EPC Integrator |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-01, SEC-06 Vapour Recovery, equipment list)
- DELIVERABLE_REGISTER.csv (Gate 7 snapshot) — sibling deliverables DEL-090-04 and DEL-090-06
- `26020-Package_Requirements.docx` package heading 43 — location TBD (binary source not locally extracted)
- `26020-Packages_Interfaces_4_export.xlsx` Packages row 100 — location TBD (binary source not locally extracted)
