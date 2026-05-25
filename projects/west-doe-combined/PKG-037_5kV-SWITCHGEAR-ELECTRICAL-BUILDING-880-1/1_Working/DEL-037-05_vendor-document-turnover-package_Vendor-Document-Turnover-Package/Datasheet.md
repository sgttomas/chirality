# Datasheet: DEL-037-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-037-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-037` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 37 / row 39 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-028 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 39; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; vendor-document turnover scope | `PACKAGE_REGISTER.csv` row `PKG-037`; `_CONTEXT.md` |
| Turnover scope items | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-037-05`; Workbook Packages row 39 |
| Vendor document register requirement | Package deliverables shall include vendor document registers among the required mechanical/equipment package deliverables. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617) |
| Package basis equipment context | 5 kV class switchgear electrical building 880-1. Source set does not contain a building 880-1 fact sheet, single-line diagram, or vendor document index specific to PKG-037; package identity is established by Workbook row 39 and Gate 7 registers. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| 5 kV reference basis | Project medium-voltage cable basis includes three-conductor copper TECK cable rated 5 kV with 100 percent insulation for 4.160 kV MV cables; the "5 kV" naming aligns with project MV insulation class. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table (line 3009) |
| Vendor document register content | Detailed required vendor-document line items, document codes, hold/issue revision rules, and turnover acceptance criteria are not defined in the accessible source set; mark as `TBD` until source-supported. | `ARTIFACT_REGISTER.csv` row `ART-8E3FB7B466` (TBD vendor document register — Vendor Documentation Gap Evidence) |
| Submittal workflow | Submittal review, hold/code assignment, revision control, and acceptance routing are not defined in the accessible source set. | Source gap; `26020-Package_Requirements.docx` lacks accessible package-specific PKG-037 content |
| Turnover record set | Final O&M, as-built drawings, calibration/test reports, spare parts list, warranty, and certification records are conventional vendor-turnover content; the accessible source set does not enumerate package-specific items. Mark detailed list as `TBD`. | Source gap |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-037 and shall be carried in the vendor-document register and turnover record set where vendor scope crosses this interface. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-524BC4670F` |
| Drain / Containment | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-A8DC0D3056` |
| Electrical Power | Interface fact applies to PKG-037; vendor documentation shall represent feeder, protection, and incoming-power interface basis. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-35A170DE7F` |
| Grounding / Bonding | Interface fact applies to PKG-037; vendor documentation shall represent grounding interface basis. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-E26DA604FB` |
| Area / Exterior Lighting | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8F0D1E29F1` |
| I&C / Control Cabling | Interface fact applies to PKG-037; vendor documentation shall represent control/monitoring interface basis. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-F5B78B59CE` |
| Communications / Network | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-1ECBDB6397` |
| Building HVAC / Services | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-D6D4CB07AF` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-4D8A22B2CA` |
| Maintenance Access | Interface fact applies to PKG-037; turnover documentation shall preserve clearances and access provisions. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-CE2AC83D1D` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-037. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-65DF6F2E88` |
| Structural / Foundations / Supports | Interface fact applies to PKG-037; vendor documentation shall include foundation loads and support data. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8012069CE2` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document production | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037`; `_CONTEXT.md` |
| Vendor document review and integration | EPC Integrator interface/integration review. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-037-05` |
| Vendor document register format | TBD. No accessible source defines the register schema (e.g., document number, title, code, revision, status, supplier transmittal) for this package. | Source gap; `ART-8E3FB7B466` (Vendor Documentation Gap Evidence) |
| Submittal stages / hold codes | TBD. Submittal stages (e.g., for review, for construction, as-built), review codes, and revision discipline are not defined in the accessible source set. | Source gap |
| Turnover acceptance | TBD. Acceptance criteria, sign-off authority, and turnover package completeness rules are not defined in the accessible source set. | Source gap; `DEL-037-06_epc-vendor-package-review-and-acceptance` is the EPC acceptance deliverable per `DELIVERABLE_REGISTER.csv` |
| Source vendor document table rows | Where individual vendor document table rows are available in source, they shall be carried as artifacts/evidence, not as separate deliverables. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` notes |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `ARTIFACT_REGISTER.csv`, row `ART-8E3FB7B466` (TBD vendor document register — Vendor Documentation Gap Evidence) for `DEL-037-05`.
- `INTERFACE_REGISTER.csv`, twelve interface rows for `PKG-037`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-037-05` (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617) — vendor document registers as required package deliverable.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; MV cable table (line 3009) — 5 kV insulation class basis.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-037 content; no package-specific match accessible.
