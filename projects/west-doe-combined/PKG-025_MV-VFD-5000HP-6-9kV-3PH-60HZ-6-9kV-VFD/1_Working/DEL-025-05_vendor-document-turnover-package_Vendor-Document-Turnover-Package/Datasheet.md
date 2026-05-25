# Datasheet: DEL-025-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-025-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-025` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 25 / row 27 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-025` |
| CoA tracking number | 26020-01-30-016 | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Discipline | Electrical | Workbook Packages row 27; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Covers scope items | `SOW-0026` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable class | Single Package Vendor turnover deliverable for vendor documentation, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-025-05`; `PACKAGE_REGISTER.csv` row `PKG-025` |
| Function | Aggregate and submit the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for `PKG-025`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-025-05` |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-025-05` |
| Package context | `PKG-025` is the workbook-defined vendor-owned Electrical package for the 5000 HP, 6.9 kV, 3-phase, 60 Hz MV VFD under WBS 01, CoA 26020-01-30-016. | Workbook Packages row 27; `PACKAGE_REGISTER.csv` row `PKG-025` |
| DBM-stated vendor-document requirement | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph |
| Detailed vendor-document register content | TBD. No accessible source slice enumerates the per-document list, revision plan, hold/code, transmittal IDs, or turnover schedule for `PKG-025`. | `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB` records this as a vendor documentation gap. |
| Turnover record content | TBD. Source materials do not define which turnover records (test certificates, factory acceptance reports, calibration records, spare-parts lists, training records, as-built marks) the vendor must include for `PKG-025`. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-025 package match in the deliverable folder. |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Vendor documentation for `PKG-025` shall preserve the Electrical Power interface fact carried by the package. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-812CB082EA` |
| Grounding / Bonding | Vendor documentation shall preserve the Grounding / Bonding interface fact. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3BE8D26B6B` |
| I&C / Control Cabling | Vendor documentation shall preserve the I&C / Control Cabling interface fact. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-949E34ECEA` |
| Communications / Network | Vendor documentation shall preserve the Communications / Network interface fact. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-EF46C006CC` |
| Maintenance Access | Vendor documentation shall preserve the Maintenance Access interface fact. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3A60522074` |
| Structural / Foundations / Supports | Vendor documentation shall preserve the Structural / Foundations / Supports interface fact. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-FB81FE736B` |
| EPC review interface | EPC Integrator review of vendor documentation is required for interface/integration acceptance against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `DELIVERABLE_REGISTER.csv` rows `DEL-025-01`, `DEL-025-02`, `DEL-025-03`, `DEL-025-06` |
| Source-required vendor documentation | The DBM mechanical packages paragraph defines the minimum content category set that vendor documentation should support (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating/design envelopes, sparing philosophy, materials/coating basis, maintenance access, shipped-loose item lists, vendor document registers). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register | Package Vendor responsibility. Register shall list each vendor document with identifier, title, revision, status, and submittal/turnover state. | `PACKAGE_REGISTER.csv` row `PKG-025`; `_CONTEXT.md` |
| Vendor document submittals | Package Vendor responsibility. Submittals shall conform to EPC transmittal handling and be reviewable against the EPC Scope of Work and Package Datasheet. | `DELIVERABLE_REGISTER.csv` row `DEL-025-05`; `DELIVERABLE_REGISTER.csv` rows `DEL-025-01`, `DEL-025-02` |
| Source-required vendor documentation | Where the DBM mechanical packages content categories apply to a 6.9 kV MV VFD package, the vendor shall include the applicable items in the register and submittals. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph |
| Turnover records | Package Vendor responsibility. Detailed turnover record content (FAT/SAT, certifications, calibrations, spare parts, training, as-builts) is TBD pending source-supported turnover requirement set. | Source gap |
| EPC integration review | EPC Integrator responsibility. Review against EPC anchors and tie-in completeness; review evidence is consumed by `DEL-025-06_epc-vendor-package-review-and-acceptance`. | `DELIVERABLE_REGISTER.csv` row `DEL-025-06`; `PACKAGE_REGISTER.csv` row `PKG-025` |
| Per-document detail (titles, revisions, hold codes) | TBD. No accessible package-specific source slice. | `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB`; source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream/downstream dependencies (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-025-05_vendor-document-turnover-package` and sibling rows `DEL-025-01` through `DEL-025-06`.
- `PACKAGE_REGISTER.csv`, row `PKG-025`.
- `ARTIFACT_REGISTER.csv`, row `ART-5D23A5F2CB` (TBD vendor document register; vendor documentation gap evidence).
- `INTERFACE_REGISTER.csv`, six `PKG-025` interface rows (`IFC-812CB082EA`, `IFC-3BE8D26B6B`, `IFC-949E34ECEA`, `IFC-EF46C006CC`, `IFC-3A60522074`, `IFC-FB81FE736B`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, seven `DEL-025-05` objective rows (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph (vendor document register requirement).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (Deepcut decomposition basis source).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-025 vendor-document content; no accessible package-specific slice surfaced for this deliverable.
