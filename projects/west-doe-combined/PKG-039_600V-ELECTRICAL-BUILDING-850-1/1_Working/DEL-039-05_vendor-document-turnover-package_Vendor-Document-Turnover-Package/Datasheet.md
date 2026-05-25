# Datasheet: DEL-039-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-039-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-039` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (850-1) | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 39 / row 41 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-039` |
| CoA tracking number | 26020-01-30-030 | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Covers scope items | `SOW-0040` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (PACKAGE_HEURISTIC, ASSUMPTION) |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Package function | 600 V Inlet / Sales Compressor Electrical Building (Site Tag 850-1) — prefabricated, modular electrical building in the West Doe Deepcut electrical building set. | Workbook Packages row 41; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Shop electrical buildings table; Electrical Buildings paragraphs) |
| Documentation ownership | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration; the EPC Integrator reviews vendor documentation. | `PACKAGE_REGISTER.csv` row `PKG-039`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05` |
| General source basis for vendor document register | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." This statement is anchored in mechanical-package text; its applicability to an electrical building vendor document set is treated as directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, package deliverables paragraph |
| Anticipated package-side content scope (from DBM) | Electrical buildings may house, as required by detailed design: 13.8 kV main switchgear, medium-voltage MCCs, medium-voltage RVSS, medium-voltage VFDs, 600 V MCCs, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. Vendor documentation shall cover the actually-installed subset for 850-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Package-specific vendor document requirements | TBD. `ARTIFACT_REGISTER.csv` flags this deliverable as `Vendor Documentation Gap Evidence`: "Detailed vendor-document requirements are not present in current source material for this package." | `ARTIFACT_REGISTER.csv` `ART-A64A8A25DC` |
| Document control numbering and revision basis | TBD. No project-wide vendor document control or revision convention is locally accessible in the source slices reviewed for this deliverable. | Source gap |
| Turnover record set | TBD. Decomposition lists "turnover records" as an anticipated artifact but does not enumerate fields or formats. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-039; vendor documentation shall include any package-side utility piping data (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-A257E2C89C` |
| Drain / Containment | Interface fact applies to PKG-039; vendor documentation shall include package-side drain / containment data (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-5C80D8C3EC` |
| Electrical Power | Interface fact applies to PKG-039; vendor documentation shall include incoming and outgoing power feeder data, single-line, load schedules (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9` |
| Grounding / Bonding | Interface fact applies to PKG-039; vendor documentation shall include grounding/bonding arrangement, ground bus, and ground-grid tie points (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9653B84E14` |
| Area / Exterior Lighting | Interface fact applies to PKG-039; vendor documentation shall include exterior and emergency lighting data for the building envelope (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-4BC9BD20C1` |
| I&C / Control Cabling | Interface fact applies to PKG-039; vendor documentation shall include control cabling, PLC panel, and instrument interface data (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-3F18DB0D3A` |
| Communications / Network | Interface fact applies to PKG-039; vendor documentation shall include network rack and communications interface data (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-B95212AB85` |
| Building HVAC / Services | Interface fact applies to PKG-039; vendor documentation shall include the building HVAC system (n + 1 cooling per DBM) and associated services (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings HVAC paragraph |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-039; vendor documentation shall include fire and gas detection, suppression, and safety-system interface data for the building (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9C0AFE36A2` |
| Maintenance Access | Interface fact applies to PKG-039; vendor documentation shall include equipment removal, door/transom, and clearance data. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D971A17948`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph on door sizing |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-039; vendor documentation shall include site grading and drainage interface at the building footprint (final content TBD). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-50A5B3F280` |
| Structural / Foundations / Supports | Interface fact applies to PKG-039; vendor documentation shall include building support/anchorage, piling interface, and bottom-cable-entry support data sufficient for EPC structural design. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph on piling and bottom entry |
| EPC review condition | Submitted vendor documents are subject to EPC Integrator review under `DEL-039-06_epc-vendor-package-review-and-acceptance`; results are recorded in the vendor document review log artifact. | `ARTIFACT_REGISTER.csv` `ART-3910447327`; `DELIVERABLE_REGISTER.csv` row `DEL-039-06` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Document register construction | Package Vendor establishes the vendor document register listing all documents the vendor will submit for the package; structure and required fields are TBD pending project-wide vendor document control basis. | `_CONTEXT.md`; source gap |
| Submittal package construction | Package Vendor assembles submittals against the register (drawings, datasheets, calculations, certificates, test records, manuals) for EPC review and acceptance; detailed content list is TBD until vendor scope is defined. | `_CONTEXT.md` (anticipated artifacts); source gap |
| Source vendor document table rows | Where source material exposes specific vendor document table rows, those rows are carried as artifacts/evidence rather than as separate deliverables. No PKG-039-specific rows are locally accessible. | `_CONTEXT.md` notes; `ARTIFACT_REGISTER.csv` `ART-A64A8A25DC` |
| Turnover record assembly | Package Vendor compiles turnover records (final certified data, test/inspection results, as-built/marked-up content, spares/loose-item lists, manuals) for handoff into the EPC turnover process; field set TBD. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05` |
| Linkage to EPC acceptance | Turnover package feeds `DEL-039-06_epc-vendor-package-review-and-acceptance`, which produces the review-and-comment log, acceptance/turnover checklist, and factory/shop test evidence artifacts. | `ARTIFACT_REGISTER.csv` `ART-3910447327`, `ART-AA4BFB86C9`, `ART-0156F0196A` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependency posture (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-039-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-039`.
- `ARTIFACT_REGISTER.csv`, row `ART-A64A8A25DC` (vendor documentation gap evidence) and PKG-039 review-and-acceptance artifact rows (`ART-3910447327`, `ART-AA4BFB86C9`, `ART-0156F0196A`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-039` (`IFC-A257E2C89C`, `IFC-5C80D8C3EC`, `IFC-C1DF6B8DD9`, `IFC-9653B84E14`, `IFC-4BC9BD20C1`, `IFC-3F18DB0D3A`, `IFC-B95212AB85`, `IFC-D8A8F7FEBC`, `IFC-9C0AFE36A2`, `IFC-D971A17948`, `IFC-50A5B3F280`, `IFC-E3D0A5A836`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-039-05_vendor-document-turnover-package` (PACKAGE_HEURISTIC association, ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs and Shop electrical-buildings table (identifies the 850-1 building as the 600 V Inlet / Sales Compressor Electrical Building).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, package deliverables paragraph (vendor document register as a general package deliverable expectation).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document requirements; no PKG-039 match found.
