# Datasheet: DEL-033-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-033-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-033` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 33 / row 35 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row `PKG-033` |
| CoA tracking number | 26020-02-30-024 | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope item covered | `SOW-0034` | `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-033` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance deliverable role | EPC Integrator review and acceptance evidence for the vendor 4160V switchgear / electrical building (830-2) package, against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-033-06_epc-vendor-package-review-and-acceptance` |
| Acceptance basis documents | EPC Scope of Work (`DEL-033-01_scope-of-work`), Package Datasheet (`DEL-033-02_package-datasheet`), Construction Work Package (`DEL-033-03_construction-work-package`), Vendor Engineered Equipment Package (`DEL-033-04_vendor-engineered-equipment-package`), Vendor Document Turnover Package (`DEL-033-05_vendor-document-turnover-package`). | `DELIVERABLE_REGISTER.csv` rows for `PKG-033`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Anticipated acceptance artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` rows `ART-221BEBC7F8`, `ART-396C3EAED7`, `ART-46FF7B44A7` |
| Vendor document review log | EPC review evidence for vendor documentation and integration requirements. | `ARTIFACT_REGISTER.csv` row `ART-221BEBC7F8` |
| Vendor package acceptance and turnover checklist | Acceptance and turnover evidence for integration into the facility. | `ARTIFACT_REGISTER.csv` row `ART-396C3EAED7` |
| Factory/shop test and inspection evidence | Expected package test/inspection evidence; detailed requirements are source-specific where available. | `ARTIFACT_REGISTER.csv` row `ART-46FF7B44A7` |
| Gate position | Gate 5 EPC Integrator deliverable framed as review-and-acceptance evidence (additional to the four core EPC anchors). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Utility Piping | Applicable interface fact for `PKG-033`; vendor package shall be reviewed and accepted against this interface. | `INTERFACE_REGISTER.csv` `IFC-C55D5117E0` |
| Drain / Containment | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-6D41E81E9D` |
| Electrical Power | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-87E42C897B` |
| Grounding / Bonding | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-68149F738F` |
| Area / Exterior Lighting | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-DEF85D9CD6` |
| I&C / Control Cabling | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-34A8619308` |
| Communications / Network | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-F6B851FF9C` |
| Building HVAC / Services | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-F6FC5D19F9` |
| Fire & Gas / Safety Systems | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-BED07EB56D` |
| Maintenance Access | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-73858A4A80` |
| Grading / Site Drainage / Spill Containment | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-9AEF468935` |
| Structural / Foundations / Supports | Applicable interface fact for `PKG-033`. | `INTERFACE_REGISTER.csv` `IFC-D7C1CC054F` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor responsibilities under review | Package engineering, package design, vendor documentation, and physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-033` |
| EPC Integrator responsibilities (reviewer role) | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Review scope coverage | Vendor documentation review, integration acceptance, and handoff readiness against EPC SoW, Package Datasheet, and Construction Work Package. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` Description |
| Test/inspection evidence depth | Factory/shop test and inspection evidence is expected; detailed acceptance criteria are source-specific and remain `TBD` until vendor data and discipline test plans are available. | `ARTIFACT_REGISTER.csv` `ART-46FF7B44A7` Notes |
| Turnover evidence | Package acceptance and turnover checklist captures handoff completeness against integration requirements. | `ARTIFACT_REGISTER.csv` `ART-396C3EAED7` |
| Package-specific 4160V switchgear acceptance criteria | `TBD`. No package-specific source slice (e.g., `26020-Package_Requirements.docx` PKG-033 match) is available in this deliverable folder; `PACKAGE_REGISTER.csv` records `DocxPackageMatched=FALSE` for `PKG-033`. | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` |
| Exclusions | `TBD`; no package-specific exclusions are stated in source materials. | `PACKAGE_REGISTER.csv` row `PKG-033` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, coordination mode and declared edges (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-033-06_epc-vendor-package-review-and-acceptance`.
- `PACKAGE_REGISTER.csv`, row `PKG-033`.
- `INTERFACE_REGISTER.csv`, twelve interface rows for `PKG-033`.
- `ARTIFACT_REGISTER.csv`, rows `ART-221BEBC7F8`, `ART-396C3EAED7`, `ART-46FF7B44A7`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-033-06_epc-vendor-package-review-and-acceptance` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010).
- Sibling deliverables (basis of acceptance): `DEL-033-01_scope-of-work`, `DEL-033-02_package-datasheet`, `DEL-033-03_construction-work-package`, `DEL-033-04_vendor-engineered-equipment-package`, `DEL-033-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-033 match; no match found (`PACKAGE_REGISTER.csv` `DocxPackageMatched=FALSE`).
