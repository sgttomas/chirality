# Datasheet: DEL-013-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-013-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-013` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 100A DC UNINTERUPTIBLE POWER SUPPLY | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 13 / row 15 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row `PKG-013` |
| CoA tracking number | 26020-02-30-004 | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Covers scope items | `SOW-0014` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Package function | 100A DC uninterruptible power supply package | Workbook Packages row 15 |
| Documentation ownership | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration; the EPC Integrator reviews vendor documentation. | `PACKAGE_REGISTER.csv` row `PKG-013`; `DELIVERABLE_REGISTER.csv` row `DEL-013-05` |
| General source basis for vendor document register | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." This statement applies to mechanical packages in the source; its applicability to electrical UPS package documentation is treated as directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph) |
| Package-specific vendor document requirements | TBD. Artifact register flags this deliverable as `Vendor Documentation Gap Evidence`: "Detailed vendor-document requirements are not present in current source material for this package." | `ARTIFACT_REGISTER.csv` `ART-23F404EC4B` |
| Document control numbering and revision basis | TBD. No project-wide vendor document control or revision convention is locally accessible in the source slices reviewed for this deliverable. | Source gap |
| Turnover record set | TBD. Decomposition lists "turnover records" as an anticipated artifact but does not enumerate fields or formats. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-013; vendor documentation shall include the package-side data required for the Electrical Power interface (final detailed content TBD). | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-3B1ED82A25` |
| Grounding / Bonding | Interface fact applies to PKG-013; vendor documentation shall include grounding/bonding data and arrangement for the package (final detailed content TBD). | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-8093ECDA51` |
| Maintenance Access | Interface fact applies to PKG-013; vendor documentation shall include maintenance access envelopes and clearances (final detailed content TBD). | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-DA9E0BAB70` |
| Structural / Foundations / Supports | Interface fact applies to PKG-013; vendor documentation shall include support/anchorage data sufficient for EPC structural design (final detailed content TBD). | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-CAE19AED68` |
| EPC review condition | Submitted vendor documents are subject to EPC Integrator review under `DEL-013-06_epc-vendor-package-review-and-acceptance`; results are recorded in the vendor document review log artifact. | `ARTIFACT_REGISTER.csv` `ART-BF80E6E249`; `DELIVERABLE_REGISTER.csv` row `DEL-013-06` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Document register construction | Package Vendor establishes the vendor document register listing all documents the vendor will submit for the package; structure and required fields are TBD pending project-wide vendor document control basis. | `_CONTEXT.md`; source gap |
| Submittal package construction | Package Vendor assembles submittals against the register (drawings, datasheets, calculations, certificates, test records, manuals) for EPC review and acceptance; detailed content list is TBD until vendor scope is defined. | `_CONTEXT.md` (anticipated artifacts); source gap |
| Source vendor document table rows | Where the source material exposes specific vendor document table rows, those rows are carried as artifacts/evidence rather than as separate deliverables. No PKG-013-specific rows are locally accessible. | `_CONTEXT.md` notes; `ARTIFACT_REGISTER.csv` `ART-23F404EC4B` |
| Turnover record assembly | Package Vendor compiles turnover records (final certified data, test/inspection results, as-built/marked-up content, spares/loose-item lists, manuals) for handoff into the EPC turnover process; field set TBD. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-013-05` |
| Linkage to EPC acceptance | Turnover package feeds `DEL-013-06_epc-vendor-package-review-and-acceptance`, which produces the review-and-comment log and acceptance/turnover checklist artifacts. | `ARTIFACT_REGISTER.csv` `ART-BF80E6E249`, `ART-E565B29B24`, `ART-6CC0DC45E9` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependency posture (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-013-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-013`.
- `ARTIFACT_REGISTER.csv`, row `ART-23F404EC4B` (vendor documentation gap evidence) and PKG-013 review-and-acceptance artifact rows (`ART-BF80E6E249`, `ART-E565B29B24`, `ART-6CC0DC45E9`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-013` (`IFC-3B1ED82A25`, `IFC-8093ECDA51`, `IFC-DA9E0BAB70`, `IFC-CAE19AED68`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-013-05_vendor-document-turnover-package` (PACKAGE_HEURISTIC association, ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 15.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, package deliverables paragraph (vendor document register as a general package deliverable expectation).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document requirements; no PKG-013 match found.
