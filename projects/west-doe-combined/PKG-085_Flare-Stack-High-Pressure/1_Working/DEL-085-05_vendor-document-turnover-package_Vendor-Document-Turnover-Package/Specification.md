# Specification — Vendor Document Turnover Package (DEL-085-05)

> Normative requirements for the vendor document turnover package supporting PKG-085 Flare Stack (High Pressure).

## Scope

### In scope
- Establishment and maintenance of a **vendor document register** for PKG-085 covering all vendor-produced documentation for the HP flare stack `FL-4120-1` and the shared flare-stack interface content described in the Package Requirements source (`26020-Package_Requirements.docx` heading 38).
- Submittal and transmittal control for **vendor document submittals** (drawings, datasheets, calculations, manuals, certificates) issued by the Package Vendor.
- Preservation of **source vendor document table rows** as artifact-level evidence, where available, per `_CONTEXT.md` Notes.
- Production of **turnover records** evidencing transfer of the assembled documentation set from the Package Vendor (with EPC Integrator review) to the receiving party.

### Out of scope
- Vendor engineering content itself as a standalone deliverable (that is `DEL-085-04` Vendor Engineered Equipment Package). This deliverable controls **documentation handover**, not the engineered content.
- EPC Integrator review/acceptance workflow (covered by `DEL-085-06`).
- Construction execution (covered by `DEL-085-03`).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| SPEC-085-05-R1 | A vendor document register SHALL exist for PKG-085 and SHALL enumerate every vendor-issued document required for turnover. | `_CONTEXT.md` Anticipated Artifacts |
| SPEC-085-05-R2 | The register SHALL identify, per document: Document ID, Title, Revision, Status, Transmittal Reference, and EPC Integrator review disposition. | ASSUMPTION (industry-standard register fields; specific governing list TBD) |
| SPEC-085-05-R3 | Vendor document submittals SHALL be associated with one or more of the SOW items covered: SOW-0087, SOW-0088, SOW-0089, SOW-0090. | `_CONTEXT.md` Covers Scope Items |
| SPEC-085-05-R4 | Vendor document submittals SHALL be reviewed by the EPC Integrator for **interface/integration** consistency before turnover acceptance. | `_CONTEXT.md` ResponsibleParty (`EPC Integrator interface/integration review`) |
| SPEC-085-05-R5 | Documentation covering the package interface domains marked active in the source workbook SHALL be present in the register: Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports. | `26020-Packages_Interfaces_4_export.xlsx` row 58 |
| SPEC-085-05-R6 | Source vendor document table rows SHALL be preserved as artifact-level evidence in the register when available; absent rows SHALL be marked with the gap so they can be resolved or accepted. | `_CONTEXT.md` Anticipated Artifacts + Notes |
| SPEC-085-05-R7 | Turnover records SHALL evidence transfer of custody of the assembled documentation set and SHALL be retained per project document control requirements. | `_CONTEXT.md` Anticipated Artifacts; project document control standard `TBD` (location TBD) |
| SPEC-085-05-R8 | The register SHALL be kept current through the vendor's document issue lifecycle until turnover is accepted. | ASSUMPTION (standard practice) |
| SPEC-085-05-R9 | Items marked `TBD` in the source `Vendor Engineering Deliverables` and `Interface Coordination Notes` sections of `26020-Package_Requirements.docx` heading 38 SHALL be resolved or formally accepted as `TBD` carry-over before turnover acceptance. | `26020-Package_Requirements.docx` heading 38 (both sections shown empty / `TBD`) |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| Project Document Control Procedure (governing vendor document handling and turnover) | Mandatory framework for register fields, status codes, and turnover records | TBD (not present in `_REFERENCES.md`; location TBD) |
| `26020-Package_Requirements.docx` (project Package Requirements specification) | Authoritative source for package scope and vendor engineering deliverables | `_Sources/26020-Package_Requirements.docx`, heading 38 |
| `26020-Packages_Interfaces_4_export.xlsx` (Packages/Interfaces register) | Authoritative source for active interface domains | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 58 |
| Owner / regulatory documentation retention standards | TBD | Location TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| R1 | Inspection of the register file against the package scope of work. |
| R2 | Inspection: register columns match the required field set; spot-check sample documents. |
| R3 | Trace: each submittal in the register maps to at least one SOW row (SOW-0087…SOW-0090). |
| R4 | Review-record inspection: EPC Integrator interface/integration review entries are present for each submittal before turnover acceptance. |
| R5 | Coverage check: register contains documents addressing each of the eight active interface domains identified in workbook row 58. |
| R6 | Sample audit: where source rows are available they are referenced; gaps are explicitly recorded. |
| R7 | Turnover record exists, signed/issued, and is filed in the project document control system. |
| R8 | Revision history within the register demonstrates currency through the lifecycle. |
| R9 | Disposition log resolves or formally accepts each TBD item from the referenced source sections. |

## Documentation (Required Artifacts)

- `VendorDocumentRegister` — index of all vendor-issued documents (format TBD).
- Vendor document submittal files referenced by the register.
- Source vendor document table row exports (where available) as evidence.
- Turnover record(s) (final handover documentation).
- EPC Integrator interface/integration review record (linkage to `DEL-085-06`).
