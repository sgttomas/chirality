# Datasheet: DEL-042-03 — Construction Work Package (Control Room Building)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-042-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-042` |
| PackageName | Control Room Building |
| WBS | 03 |
| WorkbookID / Row | 42 / 44 |
| CoA Tracking Number | `26020-03-39-010` (SourceRef: PACKAGE_REGISTER.csv row PKG-042) |
| Discipline | Electrical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Covers ScopeID | `SOW-0043` (SourceRef: SCOPE_LEDGER.csv) |

## Attributes

| Attribute | Value | SourceRef |
|---|---|---|
| Package function | Control Room Building (Electrical, WBS 03) | PACKAGE_REGISTER.csv (PKG-042) |
| Responsibility split | Package Vendor: engineering, design, vendor documentation, physical equipment package. EPC Integrator: facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | PACKAGE_REGISTER.csv (PKG-042) |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv (DEL-042-03); _CONTEXT.md |
| Construction artifact registered | `ART-6AD15AE851` EPC Construction Work Package | ARTIFACT_REGISTER.csv |
| Tie-in workface artifact registered | `ART-9882790698` Installation and tie-in workface plan | ARTIFACT_REGISTER.csv |

## Conditions

| Condition | Value | SourceRef |
|---|---|---|
| Site / location | TBD (location TBD — not specified in accessible source registers) | location TBD |
| Environmental / area classification | TBD | location TBD |
| Hand-over state | Physically installed, built, inspected, turned over, and tied into the larger facility systems | DELIVERABLE_REGISTER.csv (DEL-042-03 scope) |

## Construction

Applicable interface types requiring construction tie-in coordination (SourceRef: INTERFACE_REGISTER.csv rows for PKG-042):

| InterfaceID | Interface Type |
|---|---|
| IFC-BE3458FDB4 | Utility Piping |
| IFC-24C34638A3 | Drain / Containment |
| IFC-DC78111478 | Electrical Power |
| IFC-DA72344D63 | Grounding / Bonding |
| IFC-0DCC239AB3 | Area / Exterior Lighting |
| IFC-F360E6EC35 | I&C / Control Cabling |
| IFC-66A84D947D | Communications / Network |
| IFC-681FD52C78 | Building HVAC / Services |
| IFC-E549CF5FDE | Fire & Gas / Safety Systems |
| IFC-732E8E4246 | Grading / Site Drainage / Spill Containment |
| IFC-7F7D8698DC | Structural / Foundations / Supports |

Construction sequencing details (lifts, set, terminations, energization windows): TBD — not present in accessible source registers; populated downstream once design and construction planning sources are available.

## References

- DELIVERABLE_REGISTER.csv — DEL-042-03 row (SourceRef: Workbook Packages row 44)
- PACKAGE_REGISTER.csv — PKG-042 row
- ARTIFACT_REGISTER.csv — ART-6AD15AE851, ART-9882790698
- SCOPE_LEDGER.csv — SOW-0043
- INTERFACE_REGISTER.csv — 11 interface rows for PKG-042
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `_Sources/26020-Package_Requirements.docx` (location TBD — not opened in this pass)
