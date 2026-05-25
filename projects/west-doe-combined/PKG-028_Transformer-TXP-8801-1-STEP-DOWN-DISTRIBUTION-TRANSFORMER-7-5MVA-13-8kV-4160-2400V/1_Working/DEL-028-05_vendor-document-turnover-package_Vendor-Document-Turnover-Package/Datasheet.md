# Datasheet: DEL-028-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-028-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-028` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 28 / row 30 | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-028` |
| CoA tracking number | 26020-01-30-019 | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-028` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Workbook-defined vendor-owned Electrical package under WBS 01 | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Equipment tag (package) | TXP-8801-1 | Workbook Packages row 30 (package title); `_CONTEXT.md` |
| Equipment function | Step-down distribution transformer (13.8 kV primary, 4160/2400 V secondary, 7.5 MVA) | Workbook Packages row 30 (package title); `PACKAGE_REGISTER.csv` |
| Deliverable basis | Single Package Vendor deliverable comprising the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Core vendor document references (project standard) | PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality (referenced as the recurring "Core vendor documents" block applied per-package in the project package requirements document). | `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block in per-package sections |
| Package-specific requirements text | TBD. The `_Sources/26020-Package_Requirements.docx` table of contents enumerates process (`26020-01-PT-*`) packages; no PKG-028 / TXP-8801-1 step-down distribution transformer section was located in the searched extract. | `_Sources/26020-Package_Requirements.docx`, TOC and recurring section blocks |

## Conditions

| Interface / condition | Datasheet representation basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028` (Applicable interface types); `INTERFACE_REGISTER.csv` `IFC-5A6FBABCBA` |
| Grounding / Bonding | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-22E75E0E48` |
| Area / Exterior Lighting | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-487236B7E5` |
| I&C / Control Cabling | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-FD9BCC3585` |
| Communications / Network | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-2C9EC16D97` |
| Maintenance Access | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-5C19FEBFC8` |
| Structural / Foundations / Supports | Interface fact applies to PKG-028 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-028`; `INTERFACE_REGISTER.csv` `IFC-B1AD88E9C0` |
| DBM coupling — Incoming Power and Transformers | The 04-25 Deepcut DBM "Incoming Power and Transformers" section describes the 13.8 kV switchgear bus distributing radially through step-down transformers to facility electrical buildings. ASSUMPTION (best-effort): TXP-8801-1 in PKG-028 is one of these step-down feeders (13.8 kV → 4160/2400 V, 7.5 MVA). Confirmation requires source mapping accepted by the human. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2917-2937 |
| DBM coupling — Grounding for distribution transformers | DBM requires a separate copper ground conductor sized per CEC, connected directly to ground, for all distribution transformers. Applies as an interface/document expectation for grounding-related vendor documentation and turnover. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2991 |
| DBM coupling — Medium-voltage cabling | DBM specifies 13.8 kV medium-voltage cabling as three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded. Relevant to vendor documentation of primary connection arrangement and to interface evidence with the cable/tray installation scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3007 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register ownership | Package Vendor produces and maintains the vendor document register. | `_CONTEXT.md` (ResponsibleParty); `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" / PRQ-009 |
| Vendor document submittals | Package Vendor submits, EPC Integrator reviews under the integration/interface review scope. | `_CONTEXT.md` (ResponsibleParty); `PACKAGE_REGISTER.csv` row `PKG-028` |
| Source-required vendor documentation | Vendor documents required by source materials (DBM, package requirements, applicable standards) are tracked as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (Notes); `DELIVERABLE_REGISTER.csv` row `DEL-028-05` (Notes) |
| Turnover records | Package Vendor compiles turnover records covering submittals, factory and field test reports, certifications, as-built drawings, and warranty documentation appropriate to a 7.5 MVA, 13.8 kV / 4160/2400 V step-down distribution transformer. Specific record list is TBD pending a PKG-028–specific package requirements section or vendor data. | Source gap; `_Sources/26020-Package_Requirements.docx` has no accessible PKG-028 match (companion `ART-CF3AB9D3E0` "Vendor Documentation Gap Evidence" in `ARTIFACT_REGISTER.csv`) |
| EPC Integrator review | EPC Integrator reviews vendor documentation for interface and integration impact across the seven declared interface types. | `PACKAGE_REGISTER.csv` row `PKG-028`; `_CONTEXT.md` (ResponsibleParty) |
| Decomposition framing | Deliverable is an additional Gate 5 deliverable; individual source document rows remain artifacts/evidence rather than separate deliverables. | `_CONTEXT.md` (Notes); `DELIVERABLE_REGISTER.csv` row `DEL-028-05` (Notes) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-028-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-028`.
- `ARTIFACT_REGISTER.csv`, row `ART-CF3AB9D3E0` (TBD vendor document register — gap evidence for `DEL-028-05`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-028` (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-028-05_vendor-document-turnover-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 30.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Incoming Power and Transformers" section (lines 2917-2937), grounding for distribution transformers (line 2991), medium-voltage cabling (line 3007).
- `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block (PRQ-009, DOC-008, QLT-006) applied across per-package sections; no PKG-028–specific section located in the searched extract — `location TBD` for PKG-028 detail.
