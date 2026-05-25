# Datasheet: DEL-015-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-015-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-015` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 15 / row 17 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-006 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-015` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Workbook-defined vendor-owned Electrical package under WBS 02 | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Equipment tag (package) | TXP-8300-1 | Workbook Packages row 17 (package title); `_CONTEXT.md` |
| Equipment function | Step-down distribution transformer (13.8 kV primary, 4160/2400 V secondary, 12/15 MVA) | Workbook Packages row 17 (package title); `PACKAGE_REGISTER.csv` |
| Deliverable basis | Single Package Vendor deliverable comprising the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Core vendor document references (project standard) | PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality (referenced as the "Core vendor documents" block applied per-package in the project package requirements document). | `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block in per-package sections |
| Package-specific requirements text | TBD. The `_Sources/26020-Package_Requirements.docx` table of contents enumerates process (`26020-01-PT-*`) packages; no PKG-015 / TXP-8300-1 step-down distribution transformer section was located in the searched extract. | `_Sources/26020-Package_Requirements.docx`, TOC and recurring section blocks |

## Conditions

| Interface / condition | Datasheet representation basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` (Applicable interface types) |
| Grounding / Bonding | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Area / Exterior Lighting | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| I&C / Control Cabling | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Communications / Network | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Maintenance Access | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Structural / Foundations / Supports | Interface fact applies to PKG-015 and must be carried into the vendor document register and turnover records. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| DBM coupling — Incoming Power and Transformers | The 03-25 Comp and Liquids DBM lists, in the "Incoming Power and Transformers" section, a "13.8 kV to 4.16 kV, 12 MVA transformer" feeder serving the 4160V MCC for 4000V motors. ASSUMPTION (best-effort): this DBM row corresponds to TXP-8300-1 in PKG-015. Confirmation requires source mapping accepted by the human. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 738-745 |
| DBM coupling — Package deliverables list | DBM requires package deliverables to include "vendor document registers" among the standard mechanical-package outputs. Applied here by analogy to this electrical package. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 617 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document register ownership | Package Vendor produces and maintains the vendor document register. | `_CONTEXT.md` (ResponsibleParty); `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" / PRQ-009 |
| Vendor document submittals | Package Vendor submits, EPC Integrator reviews under the integration/interface review scope. | `_CONTEXT.md` (ResponsibleParty); `PACKAGE_REGISTER.csv` row `PKG-015` |
| Source-required vendor documentation | Vendor documents required by source materials (DBM, package requirements, applicable standards) are tracked as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (Notes); `DELIVERABLE_REGISTER.csv` row `DEL-015-05` (Notes) |
| Turnover records | Package Vendor compiles turnover records covering submittals, factory and field test reports, certifications, as-built drawings, and warranty documentation appropriate to a step-down distribution transformer. Specific record list is TBD pending a PKG-015–specific package requirements section or vendor data. | Source gap; `_Sources/26020-Package_Requirements.docx` has no accessible PKG-015 match |
| EPC Integrator review | EPC Integrator reviews vendor documentation for interface and integration impact (Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports). | `PACKAGE_REGISTER.csv` row `PKG-015`; `_CONTEXT.md` (ResponsibleParty) |
| Decomposition framing | Deliverable is an additional Gate 5 deliverable; individual source document rows remain artifacts/evidence rather than separate deliverables. | `_CONTEXT.md` (Notes); `DELIVERABLE_REGISTER.csv` row `DEL-015-05` (Notes) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-015-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-015`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-015-05_vendor-document-turnover-package` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 17.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" section and the mechanical-package deliverables sentence.
- `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block (PRQ-009, DOC-008, QLT-006) applied across per-package sections; no PKG-015–specific section located in the searched extract — `location TBD` for PKG-015 detail.
