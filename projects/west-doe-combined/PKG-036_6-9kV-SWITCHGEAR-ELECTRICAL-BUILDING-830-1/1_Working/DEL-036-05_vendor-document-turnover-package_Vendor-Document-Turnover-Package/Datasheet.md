# Datasheet: DEL-036-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-036-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-036` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 36 / row 38 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-036` |
| CoA tracking number | 26020-01-30-027 | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Covers scope items | `SOW-0037` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package (prefabricated modular electrical building) | `PACKAGE_REGISTER.csv` row `PKG-036`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical buildings paragraph, line 2973) |
| Package function | Medium-voltage 6.9 kV switchgear electrical building (Building 830-1) housing switchgear, MCC, distribution, and UPS gear as required by detailed design | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines 2973, 2935, 2955) |
| Documentation ownership | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration; the EPC Integrator reviews vendor documentation. | `PACKAGE_REGISTER.csv` row `PKG-036`; `DELIVERABLE_REGISTER.csv` row `DEL-036-05` |
| General source basis for vendor document register | "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." This statement is written for mechanical packages in the source; its applicability to an electrical-building vendor document set is treated as directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (package deliverables paragraph) |
| Package-specific vendor document requirements | TBD. Artifact register flags this deliverable as `Vendor Documentation Gap Evidence`: "Detailed vendor-document requirements are not present in current source material for this package." | `ARTIFACT_REGISTER.csv` `ART-462B18445D` |
| Document control numbering and revision basis | TBD. No project-wide vendor document control or revision convention is locally accessible in the source slices reviewed for this deliverable. | Source gap |
| Turnover record set | TBD. Decomposition lists "turnover records" as an anticipated artifact but does not enumerate fields or formats. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Building identity discrepancy | The package name in the workbook is `6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)`, while the DBM building list (line 2813) names building 830-1 as `4.16kV Acid Gas / Overheads Compressor Electrical Building` and lists the 6.9 kV electrical building as 820-1 (line 2812). This naming discrepancy is carried as a Conflict Table item for human ruling; it does not alter responsibility or scope. | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2811-2813 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-036; vendor documentation shall include the package-side data required for the Utility Piping interface (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-9188C9FD26` |
| Drain / Containment | Interface fact applies to PKG-036; vendor documentation shall include drain/containment data for the electrical building (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-628EF275F0` |
| Electrical Power | Interface fact applies to PKG-036; vendor documentation shall include the package-side data required for the Electrical Power interface (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-3B6012818E` |
| Grounding / Bonding | Interface fact applies to PKG-036; vendor documentation shall include grounding/bonding data and arrangement for the building and its equipment (final detailed content TBD). The DBM specifies neutral-grounding-resistor requirements that apply to the 6.9 kV system. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-B6F77BBE8A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 |
| Area / Exterior Lighting | Interface fact applies to PKG-036; vendor documentation shall include exterior/area lighting data for the building (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-D49FB38D6F` |
| I&C / Control Cabling | Interface fact applies to PKG-036; vendor documentation shall include I&C and control cabling data (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-972B08F285` |
| Communications / Network | Interface fact applies to PKG-036; vendor documentation shall include communications/network data for plant PLC integration (final detailed content TBD). The DBM requires an Ethernet communication port for connection to the plant PLC central control panel. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-349D2200D1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 |
| Building HVAC / Services | Interface fact applies to PKG-036; vendor documentation shall include building HVAC and service data (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-C81A342112` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-036; vendor documentation shall include fire-and-gas and life-safety system data (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-2C313DA749` |
| Maintenance Access | Interface fact applies to PKG-036; vendor documentation shall include maintenance access envelopes and clearances (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-21B90D3691` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-036; vendor documentation shall include grading/drainage/containment data relevant to the building footprint (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-DC7DB17C89` |
| Structural / Foundations / Supports | Interface fact applies to PKG-036; vendor documentation shall include support/anchorage data sufficient for EPC structural design (final detailed content TBD). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-BDE626F7DD` |
| EPC review condition | Submitted vendor documents are subject to EPC Integrator review under `DEL-036-06_epc-vendor-package-review-and-acceptance`; results are recorded in the vendor document review log artifact. | `ARTIFACT_REGISTER.csv` `ART-FB61C5F7B1`; `DELIVERABLE_REGISTER.csv` row `DEL-036-06` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Document register construction | Package Vendor establishes the vendor document register listing all documents the vendor will submit for the package; structure and required fields are TBD pending project-wide vendor document control basis. | `_CONTEXT.md`; source gap |
| Submittal package construction | Package Vendor assembles submittals against the register (drawings, datasheets, calculations, certificates, test records, manuals) for EPC review and acceptance; detailed content list is TBD until vendor scope is defined. | `_CONTEXT.md` (anticipated artifacts); source gap |
| Source vendor document table rows | Where the source material exposes specific vendor document table rows for this package, those rows are carried as artifacts/evidence rather than as separate deliverables. No PKG-036-specific vendor document rows are locally accessible. | `_CONTEXT.md` notes; `ARTIFACT_REGISTER.csv` `ART-462B18445D` |
| Turnover record assembly | Package Vendor compiles turnover records (final certified data, test/inspection results, as-built/marked-up content, spares/loose-item lists, manuals) for handoff into the EPC turnover process; field set TBD. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-036-05` |
| Linkage to EPC acceptance | Turnover package feeds `DEL-036-06_epc-vendor-package-review-and-acceptance`, which produces the review-and-comment log, acceptance/turnover checklist, and factory/shop test evidence artifacts. | `ARTIFACT_REGISTER.csv` `ART-FB61C5F7B1`, `ART-8F50EF826E`, `ART-2E1BDD099B` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependency posture (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-036-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-036`.
- `ARTIFACT_REGISTER.csv`, row `ART-462B18445D` (vendor documentation gap evidence) and PKG-036 review-and-acceptance artifact rows (`ART-FB61C5F7B1`, `ART-8F50EF826E`, `ART-2E1BDD099B`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-036` (`IFC-9188C9FD26`, `IFC-628EF275F0`, `IFC-3B6012818E`, `IFC-B6F77BBE8A`, `IFC-D49FB38D6F`, `IFC-972B08F285`, `IFC-349D2200D1`, `IFC-C81A342112`, `IFC-2C313DA749`, `IFC-21B90D3691`, `IFC-DC7DB17C89`, `IFC-BDE626F7DD`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-036-05_vendor-document-turnover-package` (PACKAGE_HEURISTIC association, ASSUMPTION).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph (line 2973), 6.9 kV service basis (lines 2935, 2955), grounding (line 2985), building list (lines 2811-2813).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, package deliverables paragraph (line 617) — general vendor document register expectation.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document requirements; no PKG-036 match found.
