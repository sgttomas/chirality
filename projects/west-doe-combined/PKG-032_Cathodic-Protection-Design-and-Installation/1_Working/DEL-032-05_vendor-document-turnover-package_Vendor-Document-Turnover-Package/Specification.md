# Specification: DEL-032-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-032` Cathodic Protection Design and Installation. It defines the documentation set the Package Vendor must produce, the EPC Integrator review/acceptance interface, and the records that close out the vendor documentation deliverable. It does NOT specify the technical design of the cathodic protection system itself (that belongs to `DEL-032-04` Vendor Engineered Equipment Package) or the EPC scope/datasheet/CWP (`DEL-032-01`/`-02`/`-03`).

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-032-05_vendor-document-turnover-package`; Workbook Packages row 34.

## Requirements

| ID | Requirement | Basis |
|---|---|---|
| R-1 | The vendor shall produce a Vendor Document Index (PRQ-009) listing every document in the turnover package by document number, title, revision, and status. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (PRQ-009) |
| R-2 | The vendor shall produce a Vendor Document Control Procedure (DOC-008) describing document numbering, revision control, transmittal handling, and review/disposition. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (DOC-008) |
| R-3 | The vendor shall produce a Supplier Quality Plan (QLT-006) covering the cathodic protection equipment supplied. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (QLT-006) |
| R-4 | The vendor shall produce an Inspection and Test Plan / ITP (QLT-003) defining hold/witness/review points for CP equipment and installation. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (QLT-003) |
| R-5 | The vendor shall provide Material Test Reports / Certificates (QLT-013) for traceable CP materials (e.g., anodes, cable, conductive backfill). ASSUMPTION: CP-specific traceable materials list is TBD pending CP design. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (QLT-013) |
| R-6 | The vendor shall provide Inspection Release Certificates (QLT-020) prior to shipment of cathodic protection equipment. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (QLT-020) |
| R-7 | The vendor shall compile a Manufacturing Record Book / Vendor Data Book (QLT-021) as a per-item dossier. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (QLT-021) |
| R-8 | The vendor shall provide a Logistics / Shipping Plan (PRQ-013) for CP equipment delivery to site. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (PRQ-013) |
| R-9 | The vendor shall provide a Spare Parts Interchangeability Record (SPIR, PRQ-015) for CP equipment spares. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (PRQ-015) |
| R-10 | The vendor shall deliver the Final Vendor Data Book (PRQ-016) as the consolidated turnover artifact, incorporating all accepted vendor documents, certificates, test records, and as-built data. | `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables (PRQ-016) |
| R-11 | Turnover records shall include installation, pre-commissioning, and commissioning records for the cathodic protection system. **TBD**: specific record types and acceptance certificate formats are not defined in accessible sources. | `_CONTEXT.md` (anticipated artifacts: turnover records); source gap |
| R-12 | Vendor documents shall be reviewed and accepted by the EPC Integrator before inclusion in the final turnover package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-032-05_vendor-document-turnover-package` |
| R-13 | Vendor documentation shall capture the electrical power supply, grounding/bonding, I&C/control cabling, and communications/network interfaces declared for PKG-032. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 34 |
| R-14 | Source vendor document table rows referenced by upstream sources shall be carried as artifacts/evidence within this turnover package, not as separate deliverables. | `_CONTEXT.md`, Notes |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` — Vendor Engineering Deliverables | Generic vendor document deliverable set for all vendor production units. | `_Sources/26020-Package_Requirements.docx` |
| `26020-Packages_Interfaces_4_export.xlsx` — Packages sheet, row 34 | Interface scope basis for PKG-032 Cathodic Protection Design and Installation. | `_Sources/26020-Packages_Interfaces_4_export.xlsx` |
| Cathodic protection technical standards (e.g., NACE/AMPP SP0169, SP0285; ISO 15589) | ASSUMPTION: likely applicable to underlying CP technical design referenced by vendor data; not consumed here. | location TBD — no accessible source slice |
| EPC document control procedure | TBD — no accessible source slice describes the EPC's document control conventions for vendor submittals. | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Index review: confirm every document in the turnover package appears in PRQ-009 with current revision. |
| R-2 | Procedure review against EPC document control conventions (procedure TBD). |
| R-3 — R-9 | Document-by-document review against the EPC ITP, ITR, and acceptance criteria. |
| R-10 | Final Vendor Data Book completeness audit before turnover acceptance. |
| R-11 | Witness/sign-off review of installation, pre-commissioning, and commissioning records (specific acceptance criteria TBD). |
| R-12 | EPC review log records acceptance disposition for each vendor document. |
| R-13 | Interface trace: confirm electrical power, grounding/bonding, I&C, and communications interfaces are represented in vendor documents. |
| R-14 | Cross-check that no source vendor document row was promoted to a standalone deliverable; all such rows are carried as artifacts. |

## Documentation

The turnover deliverable produces the following artifacts (anticipated, per `_CONTEXT.md`):

- Vendor document register (PRQ-009).
- Vendor document submittals (DOC-008, QLT-003, QLT-006, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015).
- Source vendor document table rows carried as artifacts/evidence.
- Turnover records (mechanical completion, pre-commissioning, commissioning, final acceptance — formats TBD).
- Final Vendor Data Book (PRQ-016) as the closure artifact.
