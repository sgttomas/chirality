# Datasheet: DEL-042-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-042-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-042` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Control Room Building | Workbook Packages row 44; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 42 / row 44 | Workbook Packages row 44; `PACKAGE_REGISTER.csv` |
| WBS | 03 | Workbook Packages row 44; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-03-39-010 | Workbook Packages row 44; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 44; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-042` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-042` |
| Package function | Control Room Building housing control-room equipment, operator interface, and associated electrical/HVAC services. | `PACKAGE_REGISTER.csv` row `PKG-042`; Workbook Packages row 44. ASSUMPTION: building-function description is consistent with package name and the broader DBM "Electrical Buildings, Raceways, Lighting, and Heat Tracing" scope; specific room-equipment list is `TBD`. |
| Turnover content basis | Mechanical package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (mechanical package deliverables paragraph) |
| Covered Scope of Work item | `SOW-0043` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION: package-grouping heuristic; `PACKAGE_HEURISTIC` mode) |
| Detailed vendor document list | `TBD`. Detailed vendor-document requirements are not present in the accessible source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-F6E4C1C060` (vendor documentation gap evidence) |
| Turnover record format | `TBD`. No package-specific turnover record format is defined in accessible source slices. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-042 match in this run. |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-042; vendor documents shall include applicable utility tie-in records. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-BE3458FDB4` |
| Drain / Containment | Interface fact applies to PKG-042; vendor documents shall include drain/containment design and tie-in records. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-24C34638A3` |
| Electrical Power | Interface fact applies to PKG-042; vendor documents shall include feeder, distribution, and protective device data. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-DC78111478` |
| Grounding / Bonding | Interface fact applies to PKG-042; vendor documents shall include grounding/bonding details supporting building tie-in to plant ground grid. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-DA72344D63` |
| Area / Exterior Lighting | Interface fact applies to PKG-042. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-0DCC239AB3` |
| I&C / Control Cabling | Interface fact applies to PKG-042; vendor documents shall include control cable schedules and termination details. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-F360E6EC35` |
| Communications / Network | Interface fact applies to PKG-042; vendor documents shall include network architecture and termination details relevant to the control room. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-66A84D947D` |
| Building HVAC / Services | Interface fact applies to PKG-042; vendor documents shall include HVAC/ventilation design coordinated with control-room thermal load. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-681FD52C78` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-042. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-E549CF5FDE` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-042. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-732E8E4246` |
| Structural / Foundations / Supports | Interface fact applies to PKG-042; vendor documents shall include building structural and foundation design coordination. | Workbook Packages row 44; `INTERFACE_REGISTER.csv` `IFC-7F7D8698DC` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document authorship | Package Vendor authors and submits vendor documents and the turnover package. | `PACKAGE_REGISTER.csv` row `PKG-042`; `_CONTEXT.md` |
| EPC interface/integration review | EPC Integrator reviews vendor documents for facility integration, interfaces, tie-ins, and constructability. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-042` |
| Anticipated artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-042-05` |
| Source documentation gap | Detailed vendor-document requirements are not present in current source material for this package; an artifact gap is recorded. | `ARTIFACT_REGISTER.csv` row `ART-F6E4C1C060` |
| Source documents searched for package-specific requirements | `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx`; no PKG-042 vendor-document-detail slice was accessible to this run. | `_REFERENCES.md`; source file listing |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-042-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-042`.
- `ARTIFACT_REGISTER.csv`, row `ART-F6E4C1C060` for `DEL-042-05_vendor-document-turnover-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-042` (11 interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-042-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 44.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical-package deliverable paragraph (line 617); "Electrical Buildings, Raceways, Lighting, and Heat Tracing" section (referenced via PACKAGE_REGISTER source list).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document content; no PKG-042 match accessible in this run.
