# Datasheet: DEL-029-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-029-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 29 / row 31 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-020 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 31; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Tagged equipment | TXP-8600-1 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Package function | Step-down distribution transformer (2.5 MVA, 13.8 kV / 600 / 347 V) | Workbook Packages row 31 |
| Vendor documentation responsibility | Package Vendor owns vendor documentation; EPC Integrator performs interface/integration review. | `PACKAGE_REGISTER.csv` row `PKG-029`; `_CONTEXT.md` |
| Required document register basis | Mechanical/equipment packages shall include vendor document registers among other package deliverables (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, mechanical packages paragraph (line 617) |
| Package-specific vendor-document content | TBD. The accessible source set states vendor document registers as a general package deliverable expectation but does not enumerate package-specific document classes, formats, submittal stages, or turnover content for `PKG-029`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `26020-Package_Requirements.docx` has no accessible `PKG-029` match. |
| Vendor document register contents | TBD vendor document register. Detailed vendor-document requirements are not present in current source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-91D8A203E0`; Workbook Packages row 31 |
| Submittal stages (preliminary, approval, certified, as-built) | TBD. ASSUMPTION: typical vendor-package submittal stages apply unless a project-specific submittal procedure is accepted. | Source gap |
| Turnover records | TBD. Source material does not list specific turnover record types for `PKG-029` (e.g., factory test reports, certified drawings, O&M manuals, spares list). ASSUMPTION: typical turnover content applies pending vendor and EPC confirmation. | Source gap |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-029`; vendor documentation must include data sufficient for EPC integration of 13.8 kV primary and 600 / 347 V secondary connections. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-717D0187BA` |
| Grounding / Bonding | Interface fact applies; vendor documentation must include grounding interfaces and connection points consistent with major-equipment two-point ground-grid connection. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-C49653E450`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (lines 2989, 2991) |
| Area / Exterior Lighting | Interface fact applies; vendor documentation must define area/exterior lighting interface where lighting is mounted on or near the transformer/structure. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-DFC1A10C2D` |
| I&C / Control Cabling | Interface fact applies; vendor documentation must define monitoring, alarm, and protective relay interface termination requirements. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-A5C9438164` |
| Communications / Network | Interface fact applies; vendor documentation must define communications interfaces (where supplied) and any network configuration. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-81CFD2A32C` |
| Maintenance Access | Interface fact applies; vendor documentation must include maintenance access requirements (clearances, oil sampling, bushing access, tap-changer access if applicable). | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-2C14FA1228` |
| Structural / Foundations / Supports | Interface fact applies; vendor documentation must include foundation/support loads and anchorage details. Source states transformers are generally installed on structural steel transformer bases on precast concrete bearing foundations. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-380F4773FB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs (lines 2745, 2949) |
| Containment / oil-filled handling | If supplied as oil-filled, vendor documentation shall address CEC spacing and secondary containment review. Containment requirements shall be reviewed; transformer selection shall avoid or limit containment requirements where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (line 2949) |
| Voltage system context | Plant low-voltage 600 V services are 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor; 600 V transformers are grounded by a 5 A continuous high-resistance grounding resistor. Vendor documentation shall be consistent with this system context where the package interacts with the 600 V bus. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage table and grounding paragraphs (lines 2937, 2985) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document ownership | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029`; `_CONTEXT.md` |
| Vendor document review | EPC Integrator performs interface/integration review. | `PACKAGE_REGISTER.csv` row `PKG-029`; `_CONTEXT.md` |
| Vendor document register format | TBD. No project-level vendor document register template was accessible in the source set. | Source gap; `26020-Package_Requirements.docx` not accessible for `PKG-029` match |
| Submittal workflow | TBD. ASSUMPTION: vendor submits per project document control procedure; EPC reviews and dispositions; certified copies issued for fabrication; turnover copies issued at acceptance. No source-confirmed workflow available. | Source gap |
| Turnover record set | TBD. ASSUMPTION: typical set includes certified drawings, factory acceptance test reports, nameplate data, O&M manuals, recommended spare parts, and warranty documentation. No source-confirmed enumeration for `PKG-029`. | Source gap |
| Source vendor document table rows as artifacts | Individual source document rows remain artifacts/evidence; no separate per-document deliverables are created at this gate. | `_CONTEXT.md` notes; `DELIVERABLE_REGISTER.csv` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-029-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-029`.
- `ARTIFACT_REGISTER.csv`, row `ART-91D8A203E0` (TBD vendor document register).
- `INTERFACE_REGISTER.csv`, rows for `PKG-029` (`IFC-717D0187BA`, `IFC-C49653E450`, `IFC-DFC1A10C2D`, `IFC-A5C9438164`, `IFC-81CFD2A32C`, `IFC-2C14FA1228`, `IFC-380F4773FB`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-029-05_vendor-document-turnover-package` (PACKAGE_HEURISTIC: OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 — ASSUMPTION, best-effort mapping).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, mechanical packages paragraph (line 617), transformers and foundations paragraphs (lines 2745, 2949), voltage and grounding paragraphs (lines 2937, 2985, 2989, 2991).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor-document content; no `PKG-029` match found.
