# Datasheet: DEL-076-05 — Vendor Document Turnover Package

> Descriptive datasheet for the Lube Oil Supply (PKG-076) Vendor Document Turnover Package. Non-trivial values cite source slices; absent values are marked `TBD`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-076-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-076` |
| PackageName | Lube Oil Supply |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| CoversScope | SOW-0135, SOW-0136, SOW-0137, SOW-0138 |
| SupportsObjectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC) |
| DecompositionBasis | GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP |
| AuthoritativeSourceSlice | `_Sources/26020-Package_Requirements.docx` heading 30 (location TBD — DOCX not converted) |
| Supporting DBM Source A | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Mechanical Package Structure" (line 617) |
| Supporting DBM Source B | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers" (lines 503-507) |
| Supporting DBM Source C | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" (lines 2059-2068) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Document set type | Vendor turnover package (register + submittals + turnover records) | _CONTEXT.md Scope; Workbook Packages row 70 |
| Required content classes | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers | DBM 3-25 line 617 |
| Lube-oil scope items implicating vendor docs | Cylinder lube-oil 400 bbl heated tank; cylinder lube-oil pump P-9240-1; crank-case lube-oil basis | DBM 4-25 lines 2059-2068 |
| EPC Integrator role | Interface/integration review of vendor submittals | _CONTEXT.md ResponsibleParty |
| Document numbering scheme | TBD (project document control basis not in accessible workspace) | location TBD |
| Document classification (IFR/IFA/IFC/Final/As-Built) workflow | TBD | location TBD |
| Approval / acceptance authority | EPC Integrator (vendor doc review log per DEL-076-06 convention) | ASSUMPTION based on DEL-076-06 register row |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating environment of equipment whose vendor docs are turned over | Compressor area / liquids hub at 03-25 facility | DBM 3-25 line 503 et seq. |
| Hazardous-material classification of lube-oil storage | TBD — project hazardous-material list not in workspace | DBM 3-25 line 507 |
| Document delivery medium | TBD (paper, electronic, EDMS) | location TBD |
| Language | TBD | location TBD |

## Construction (Document Set Composition)

| Component | Description | Source |
|---|---|---|
| Vendor Document Register | Index of all vendor documents required to be supplied for the package, with revision and status fields | DBM 3-25 line 617; _CONTEXT.md Anticipated Artifacts |
| Vendor Document Submittals | The actual submitted documents (datasheets, drawings, calculations, manuals, test records) | _CONTEXT.md |
| Source-required Vendor Document Table Rows | Where the project source specifies named vendor documents, those rows are carried as artifacts under this deliverable | _CONTEXT.md Notes |
| Turnover Records | Acceptance, hand-over, custody-transfer and as-built confirmation records | _CONTEXT.md |
| Maintenance & Operating Manuals | Vendor O&M, lubrication schedules, spare-parts lists | ASSUMPTION (standard package turnover content; specific list TBD) |

## References

- `_Sources/26020-Package_Requirements.docx` (heading 30 — not converted; location TBD)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 503-507, line 617)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines 2059-2068, line 1835)
- GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP registers (DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv)
