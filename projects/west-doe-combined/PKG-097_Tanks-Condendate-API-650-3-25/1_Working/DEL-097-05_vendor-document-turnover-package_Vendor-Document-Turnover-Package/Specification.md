# Specification — DEL-097-05 Vendor Document Turnover Package

> Pass 1/2 generation by `TASK + four-documents`. Requirements derived only from accessible source slices; inferred requirements labeled `ASSUMPTION`.

## Scope

This deliverable specifies the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for `PKG-097` Tanks, Condendate (API 650) 3-25, produced by the Package Vendor with EPC Integrator interface/integration review (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-097-05).

Scope includes:
- Definition and maintenance of a controlled vendor document register for `PKG-097`.
- Issue and revision control of vendor submittals (drawings, calculations, datasheets, certifications, test reports) covering the tank field and ancillary package equipment.
- Compilation and submission of source-required vendor documentation referenced by Workbook Packages row 88 and `26020-Package_Requirements.docx` package heading 49.
- Final turnover records (transmittal log, hand-off package, completion evidence) supporting `DEL-097-06` EPC Vendor Package Review and Acceptance.

Scope excludes:
- Physical equipment design and fabrication (covered by `DEL-097-04` Vendor Engineered Equipment Package).
- EPC-side scope-of-work and package datasheet authorship (covered by `DEL-097-01` and `DEL-097-02`).
- Construction and installation planning (covered by `DEL-097-03` Construction Work Package).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R-01 | A vendor document register shall be provided for `PKG-097`. | DBM SEC-09 Mechanical Package Structure (line 617): "Package deliverables shall include … vendor document registers." |
| R-02 | The vendor document register shall enumerate every controlled document the Package Vendor issues for the package, including drawings, calculations, datasheets, test reports, and certifications. | `ASSUMPTION` from common vendor document register practice and `_CONTEXT.md` anticipated artifacts |
| R-03 | Source-required vendor documentation rows from Workbook Packages row 88 and `26020-Package_Requirements.docx` package heading 49 shall be carried as register rows and individually submitted. | `_CONTEXT.md` "source vendor document table rows as artifacts where available"; specific row list `TBD` (sources not text-accessible) |
| R-04 | Submittals shall use a controlled revision scheme with explicit hold/issued-for codes; specific code scheme is `TBD`. | `ASSUMPTION`; concrete scheme `location TBD` |
| R-05 | Vendor documentation for produced-water tanks shall reflect API-650 Modified atmospheric tank construction with Devchem 253 internal coating, external insulation, and heating provisions. | DBM SEC-06 (line 421) |
| R-06 | Vendor documentation for condensate tanks shall reflect API 650 construction (per package name "Tanks, Condendate (API 650) 3-25"); the specific API 650 clause set governing condensate tanks is `TBD` (not located in accessible source). | Package name; clause `TBD` |
| R-07 | Vendor documentation shall reflect the -40 deg C minimum ambient basis where equipment is exposed. | DBM SEC-02 (line 145) |
| R-08 | Turnover records shall include a transmittal log, acceptance evidence, and final as-built revision status sufficient to support EPC review and acceptance under `DEL-097-06`. | `ASSUMPTION` based on declared interface between DEL-097-05 and DEL-097-06 (decomposition register) |
| R-09 | The vendor document register and submittals shall be released to the EPC Integrator for interface/integration review per the responsibility assignment for this deliverable. | `_CONTEXT.md` ResponsibleParty field |

## Standards

| Standard / Source Document | Applicability | Location |
|---|---|---|
| API 650 (and API 650 Appendix / Modified equivalents) | Atmospheric tank code basis (produced-water tanks explicitly API-650 Modified; condensate tanks API 650 per package name) | DBM SEC-06 line 421 (PW); package name (condensate); specific edition/appendix `TBD` |
| 26020-Package_Requirements.docx (package heading 49) | Source-required vendor document list and submittal expectations | `location TBD` — source is binary, not text-accessible this pass |
| Workbook Packages row 88 | Source-required vendor document list | `location TBD` — source is spreadsheet, not text-accessible this pass |
| Project DBM SEC-09 (Mechanical Package Structure) | Requires vendor document register as a package deliverable | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |

## Verification

| Requirement | Verification Method |
|---|---|
| R-01, R-02 | Inspection of the vendor document register against the controlled register template and the source-document list |
| R-03 | Row-by-row cross-check between source vendor document table rows and register entries |
| R-04 | Inspection of submittal revision blocks and transmittal log entries |
| R-05, R-06 | Vendor document review against API 650 / API-650 Modified clauses (specific edition `TBD`) and DBM SEC-06 |
| R-07 | Vendor data sheet review for stated minimum design ambient -40 deg C |
| R-08 | Inspection of completed transmittal log, acceptance signatures, and final-rev document set at turnover |
| R-09 | EPC Integrator confirms receipt and integration review per `DEL-097-06` |

## Documentation

Required artifacts to be produced by this deliverable (per `_CONTEXT.md` and Specification scope):

- Vendor document register (controlled, revision-tracked)
- Vendor document submittals package (drawings, calculations, datasheets, certifications, test reports)
- Source-document table row submittals (where rows exist; specific list `TBD`)
- Turnover records (transmittal log; final acceptance evidence; as-built document set)
