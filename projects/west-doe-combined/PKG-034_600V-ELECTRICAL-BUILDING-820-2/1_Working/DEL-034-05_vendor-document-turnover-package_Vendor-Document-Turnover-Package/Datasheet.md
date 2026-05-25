# Datasheet: DEL-034-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-034-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-034` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-2) | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 34 / row 36 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-025 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 36; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-034` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Package function | 600V Electrical Building (820-2) housing 600V MCCs/switchgear/distribution and associated HVAC/ventilation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, §"Electrical Buildings, Raceways, Lighting, and Heat Tracing" and §"600V MCC and Standby Power" |
| Turnover content basis | Mechanical package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (mechanical package deliverables paragraph) |
| Covered Scope of Work item | `SOW-0035` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION: package-grouping heuristic; PACKAGE_HEURISTIC mode) |
| Detailed vendor document list | `TBD`. Detailed vendor-document requirements are not present in the accessible source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-D602A4F8C4` (vendor documentation gap evidence) |
| Turnover record format | `TBD`. No package-specific turnover record format is defined in accessible source slices. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-034 match |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-034; vendor documents shall include applicable utility tie-in records. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-FC0F34096E` |
| Drain / Containment | Interface fact applies to PKG-034; vendor documents shall include drain/containment design and tie-in records. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-E270A479B8` |
| Electrical Power | Interface fact applies to PKG-034; vendor documents shall include feeder, distribution, and protective device data. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-0E87B7BCE6` |
| Grounding / Bonding | Interface fact applies to PKG-034; vendor documents shall include grounding/bonding details supporting building tie-in to plant ground grid. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-46D2497CB7` |
| Area / Exterior Lighting | Interface fact applies to PKG-034. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-63A70A25C3` |
| I&C / Control Cabling | Interface fact applies to PKG-034; vendor documents shall include control cable schedules and termination details. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-5EA9F4B39F` |
| Communications / Network | Interface fact applies to PKG-034. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-1333B6962E` |
| Building HVAC / Services | Interface fact applies to PKG-034; vendor documents shall include HVAC/ventilation design coordinated with electrical heat load. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-DA391B1AF1` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-034. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-94BF4E7C7C` |
| Maintenance Access | Interface fact applies to PKG-034; vendor documents shall preserve maintenance access requirements. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-CAE509DDFA` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-034. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-7BD20E62E6` |
| Structural / Foundations / Supports | Interface fact applies to PKG-034; vendor documents shall include building structural and foundation design coordination. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-EC6DF8B5D4` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document authorship | Package Vendor authors and submits vendor documents and the turnover package. | `PACKAGE_REGISTER.csv` row `PKG-034`; `_CONTEXT.md` |
| EPC interface/integration review | EPC Integrator reviews vendor documents for facility integration, interfaces, tie-ins, and constructability. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-034` |
| Anticipated artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-034-05` |
| Source documentation gap | Detailed vendor-document requirements are not present in current source material for this package; an artifact gap is recorded. | `ARTIFACT_REGISTER.csv` row `ART-D602A4F8C4` |
| Source documents searched for package-specific requirements | `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx`; no PKG-034 vendor-document-detail slice was accessible to this run. | `_REFERENCES.md`; source file listing |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-034-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-034`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-034-05_vendor-document-turnover-package` (including `ART-D602A4F8C4`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-034`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-034-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical-package deliverable paragraph (line 617), 600V MCC/standby power section, electrical buildings section.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document content; no PKG-034 match accessible.
