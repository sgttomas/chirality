# Datasheet — DEL-097-05 Vendor Document Turnover Package

> Pass 1/2 generation by `TASK + four-documents`. Non-trivial values cite a source slice or are marked `TBD`. Inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-097-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-097` |
| PackageName | Tanks, Condendate (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Source Reference | Workbook Packages row 88; 26020-Package_Requirements.docx package heading 49 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package physical scope (governing) | Stabilized C5+ condensate storage and produced-water storage tank field within the 03-25 Liquids Hub | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (Condensate Storage and Product Handling; Produced-Water Storage) |
| Condensate tank count and size | 11 x 3,800 bbl condensate tanks | DBM SEC-06, Storage / Pumping Item table (line 410) |
| Produced-water tank count and size | 7 x 3,800 bbl tanks (5 sour, 2 sweet) | DBM SEC-06 (line 421) |
| Produced-water tank code basis | API-650 Modified atmospheric tanks, externally insulated and heated, internal coating Devchem 253 | DBM SEC-06 (line 421) |
| Condensate tank code basis (API 650 per package name) | Package name implies API 650; explicit clause for condensate tanks `TBD` (not located in accessible source slice) | Package name; source location `TBD` |
| Vendor document register scope | Per the Mechanical Package Structure clause, mechanical package deliverables shall include vendor document registers | DBM SEC-09, Mechanical Package Structure (line 617) |
| Vendor documentation control standard / numbering scheme | `TBD` — not located in accessible source slices | location `TBD` (likely in 26020-Package_Requirements.docx — binary, not text-accessible) |
| Turnover record format / dossier index | `TBD` | location `TBD` |

## Conditions (operating / environmental basis affecting documentation requirements)

| Condition | Value | Source |
|---|---|---|
| Minimum design ambient | -40 deg C | DBM SEC-02 (line 145) |
| Service classification | Sour service applicable to a subset of tanks (sour condensate, sour produced water) | DBM SEC-06 (lines 406, 421) |
| Document language and units | `TBD` | `TBD` |

## Construction (documentation set deliverable composition)

Anticipated artifacts to be delivered through this turnover package (from `_CONTEXT.md` and DBM SEC-09):

- Vendor document register (controlled index of all vendor-issued documents)
- Vendor document submittals (drawings, calculations, datasheets, test reports, certifications) — list and detail `TBD`
- Source-required vendor documentation rows from the package source tables — `ASSUMPTION` that the source table referenced is Workbook Packages row 88 plus the package-heading-49 vendor-document list in 26020-Package_Requirements.docx (binary; not text-accessible in this pass)
- Turnover records (transmittal log, acceptance evidence, as-built documentation hand-off)

Detailed sub-document list, revision codes, hold codes, and required signatories: `TBD`.

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-06 (storage), SEC-09 (Mechanical Package Structure)
- `26020-Package_Requirements.docx` (package heading 49) — listed in `_REFERENCES.md` but binary; not text-accessible this pass (`location TBD`)
- Workbook Packages row 88 (`26020-Packages_Interfaces_4_export.xlsx`) — listed; spreadsheet not text-accessible this pass (`location TBD`)
- Decomposition Gate-07 snapshot — `DELIVERABLE_REGISTER.csv` row `DEL-097-05_vendor-document-turnover-package`
