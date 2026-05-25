# Datasheet: DEL-021-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-021-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-021` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR EQUIPMENT | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 21 / row 23 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-012 | Workbook Packages row 23; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 23; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Covers Scope Item | `SOW-0022` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-021` |
| Package function | 6.9 kV switchgear equipment package supporting facility medium-voltage distribution to inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services row |
| Turnover deliverable nature | Single Package Vendor deliverable for the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-021-05_vendor-document-turnover-package` |
| Documentation responsibility owner | Package Vendor authors and submits vendor documentation; EPC Integrator performs interface/integration review and uses documentation to support facility integration. | `PACKAGE_REGISTER.csv` row `PKG-021`; `_CONTEXT.md` |
| Mechanical/process package documentation precedent | Package deliverables (for the analogous mechanical packages in the same project) include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. Applicability of each item to a 6.9 kV switchgear electrical package is `TBD` and shall be confirmed by vendor document register issuance. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph |
| Detailed vendor-document register content | TBD. Gate 7 artifact register explicitly records this row as a "TBD vendor document register — detailed vendor-document requirements are not present in current source material for this package." | `ARTIFACT_REGISTER.csv` `ART-FA39AD509D` |
| Vendor document review and comment log | A vendor document review and comment log is produced by the EPC review deliverable `DEL-021-06`. This turnover package shall be consistent with that review log, but its detailed content is owned by `DEL-021-06`. | `ARTIFACT_REGISTER.csv` `ART-5D5CAC1D6D` |
| Final turnover records | Vendor package acceptance and turnover checklist evidence is produced by `DEL-021-06`. This turnover package consolidates the Package Vendor documentation set used as input to that acceptance. | `ARTIFACT_REGISTER.csv` `ART-4B01C09131` |
| Factory/shop test and inspection records | Expected as part of vendor documentation; detailed test/inspection requirements are source-specific where available and otherwise `TBD`. | `ARTIFACT_REGISTER.csv` `ART-E523401B0C` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-021`; vendor documentation set shall describe electrical power connections at the package battery limit. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9D7DF96637` |
| Grounding / Bonding | Interface fact applies to `PKG-021`; vendor documentation set shall describe grounding/bonding connections, including coordination with facility ground grid and neutral grounding resistor scheme. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-2ACD080082`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph (6.9 kV transformer neutral grounding) |
| I&C / Control Cabling | Interface fact applies to `PKG-021`; vendor documentation set shall describe I&C and control cabling interfaces. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-B44478ADB6` |
| Communications / Network | Interface fact applies to `PKG-021`; vendor documentation set shall describe communications/network interfaces (e.g., Ethernet to plant PLC where applicable). | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-FC8113A0CE`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC Ethernet communication port paragraph (analogous MV practice) |
| Maintenance Access | Interface fact applies to `PKG-021`; vendor documentation set shall preserve maintenance access (clearances, withdrawal/rack-out, panel access). | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-9E975838A2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/maintenance access paragraph |
| Structural / Foundations / Supports | Interface fact applies to `PKG-021`; vendor documentation set shall include weights, anchor patterns, and support loads required by facility structural design. | Workbook Packages row 23; `INTERFACE_REGISTER.csv` `IFC-A795E61D99` |
| Installation building context | Vendor documentation shall reflect installation in the 6.9 kV Inlet/Sales Compressor Electrical Building (per DBM facility electrical building list and architecture). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and "820-1 6.9kV Inlet / Sales Compressor Electrical Building" entries |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register authorship | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021`; `_CONTEXT.md` |
| EPC review and integration use of vendor documentation | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-021`; `_CONTEXT.md` |
| Document register format and numbering | TBD. The accessible source set does not specify a project-wide vendor document register format, numbering convention, or transmittal protocol. | `ARTIFACT_REGISTER.csv` `ART-FA39AD509D` (gap evidence); `26020-Package_Requirements.docx` not specifically searched for PKG-021 in this run |
| Detailed required vendor document list | TBD. Detailed vendor-document requirements are not present in current source material for `PKG-021`. The Package Vendor shall propose the document list; the EPC Integrator shall confirm completeness against facility integration needs. | `ARTIFACT_REGISTER.csv` `ART-FA39AD509D` |
| Turnover records format | TBD pending project-wide turnover convention. The vendor documentation set shall be aligned with `DEL-021-06_epc-vendor-package-review-and-acceptance` artifacts. | `ARTIFACT_REGISTER.csv` `ART-4B01C09131`, `ART-5D5CAC1D6D` |
| Submittal control gates | TBD. ASSUMPTION: vendor documentation shall be issued in submittal stages consistent with project schedule milestones (e.g., for review, for approval, certified, as-built/turnover). | ASSUMPTION; no source-confirmed gating scheme is available |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream/downstream view.
- `DELIVERABLE_REGISTER.csv`, row `DEL-021-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-021`.
- `ARTIFACT_REGISTER.csv`, rows `ART-FA39AD509D` (this deliverable), `ART-5D5CAC1D6D`, `ART-4B01C09131`, `ART-E523401B0C` (related `DEL-021-06` rows).
- `INTERFACE_REGISTER.csv`, rows `IFC-9D7DF96637`, `IFC-2ACD080082`, `IFC-B44478ADB6`, `IFC-FC8113A0CE`, `IFC-9E975838A2`, `IFC-A795E61D99` for `PKG-021`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-021-05_vendor-document-turnover-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services, 6.9 kV MCC, electrical buildings, grounding/bonding, and cable-tray/maintenance source slices.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical-package deliverable list paragraph (analogous expectations for package vendor documentation).
- `_Sources/26020-Package_Requirements.docx`, not specifically resolved to a `PKG-021` package match in this run; treat as `location TBD`.
