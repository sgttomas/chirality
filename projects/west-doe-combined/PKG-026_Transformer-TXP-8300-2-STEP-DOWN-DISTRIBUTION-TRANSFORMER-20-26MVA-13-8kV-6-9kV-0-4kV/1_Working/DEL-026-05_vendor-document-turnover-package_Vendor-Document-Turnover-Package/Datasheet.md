# Datasheet: DEL-026-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-026-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-026` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 26 / row 28 | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row `PKG-026` |
| CoA tracking number | 26020-02-30-017 | `PACKAGE_REGISTER.csv` row `PKG-026` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Covers scope items | `SOW-0027` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-026` |
| Package function | Step-down distribution transformer TXP-8300-2 package (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV) | Workbook Packages row 28 |
| Documentation ownership | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration; the EPC Integrator reviews vendor documentation. | `PACKAGE_REGISTER.csv` row `PKG-026`; `DELIVERABLE_REGISTER.csv` row `DEL-026-05` |
| General source basis for vendor document register | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." This statement applies to mechanical packages in the source; its applicability to electrical transformer package documentation is treated as directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph) |
| Package-specific vendor document requirements | TBD. Artifact register flags this deliverable as `Vendor Documentation Gap Evidence`: "Detailed vendor-document requirements are not present in current source material for this package." | `ARTIFACT_REGISTER.csv` `ART-C8E49463BD` |
| Document control numbering and revision basis | TBD. No project-wide vendor document control or revision convention is locally accessible in the source slices reviewed for this deliverable. | Source gap |
| Turnover record set | TBD. Decomposition lists "turnover records" as an anticipated artifact but does not enumerate fields or formats. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-026; vendor documentation shall include the package-side data required for the Electrical Power interface (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-E9FC2B952D` |
| Grounding / Bonding | Interface fact applies to PKG-026; vendor documentation shall include grounding/bonding data and arrangement for the package (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-FE5C9BD828` |
| Area / Exterior Lighting | Interface fact applies to PKG-026; vendor documentation shall include lighting requirements/provisions at the package envelope (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-0230019D52` |
| I&C / Control Cabling | Interface fact applies to PKG-026; vendor documentation shall include control/instrumentation termination data, schedules, and interconnect information (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-25E2CF2BD9` |
| Communications / Network | Interface fact applies to PKG-026; vendor documentation shall include communications/network interface data for the transformer monitoring/protection systems (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-E6E0E1FA2B` |
| Maintenance Access | Interface fact applies to PKG-026; vendor documentation shall include maintenance access envelopes and clearances (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-93877B34D5` |
| Structural / Foundations / Supports | Interface fact applies to PKG-026; vendor documentation shall include support/anchorage data sufficient for EPC structural design (final detailed content TBD). | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-7DD82CAE51` |
| EPC review condition | Submitted vendor documents are subject to EPC Integrator review under `DEL-026-06_epc-vendor-package-review-and-acceptance`; results are recorded in the vendor document review log artifact. | `ARTIFACT_REGISTER.csv` `ART-AF00FF6B63`; `DELIVERABLE_REGISTER.csv` row `DEL-026-06` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Document register construction | Package Vendor establishes the vendor document register listing all documents the vendor will submit for the package; structure and required fields are TBD pending project-wide vendor document control basis. | `_CONTEXT.md`; source gap |
| Submittal package construction | Package Vendor assembles submittals against the register (drawings, datasheets, calculations, certificates, test records, manuals) for EPC review and acceptance; detailed content list is TBD until vendor scope is defined. | `_CONTEXT.md` (anticipated artifacts); source gap |
| Source vendor document table rows | Where the source material exposes specific vendor document table rows, those rows are carried as artifacts/evidence rather than as separate deliverables. No PKG-026-specific rows are locally accessible. | `_CONTEXT.md` notes; `ARTIFACT_REGISTER.csv` `ART-C8E49463BD` |
| Turnover record assembly | Package Vendor compiles turnover records (final certified data, test/inspection results, as-built/marked-up content, spares/loose-item lists, manuals) for handoff into the EPC turnover process; field set TBD. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-026-05` |
| Linkage to EPC acceptance | Turnover package feeds `DEL-026-06_epc-vendor-package-review-and-acceptance`, which produces the review-and-comment log, acceptance/turnover checklist, and factory/shop test evidence artifacts. | `ARTIFACT_REGISTER.csv` `ART-AF00FF6B63`, `ART-28805E8681`, `ART-063BACA4E7` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependency posture (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-026-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-026`.
- `ARTIFACT_REGISTER.csv`, row `ART-C8E49463BD` (vendor documentation gap evidence) and PKG-026 review-and-acceptance artifact rows (`ART-AF00FF6B63`, `ART-28805E8681`, `ART-063BACA4E7`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-026` (`IFC-E9FC2B952D`, `IFC-FE5C9BD828`, `IFC-0230019D52`, `IFC-25E2CF2BD9`, `IFC-E6E0E1FA2B`, `IFC-93877B34D5`, `IFC-7DD82CAE51`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-026-05_vendor-document-turnover-package` (PACKAGE_HEURISTIC association, ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 28.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, package deliverables paragraph (vendor document register as a general package deliverable expectation).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document requirements; no PKG-026 match found.
