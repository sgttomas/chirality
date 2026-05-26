# Specification — Vendor Document Turnover Package (DEL-072-05)

## Scope

### In scope

The Vendor Document Turnover Package for PKG-072 (Truck Product Loading Unit 4-25) comprises:

- A vendor document register indexing all vendor-produced documents for the package.
- The vendor document submittals themselves (per-document files at each required revision/stage).
- Source vendor document table rows captured as artifacts/evidence where available.
- Turnover records: transmittals, review dispositions, and final acceptance/sign-off evidence.

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row 562.

### Out of scope / exclusions

- Engineering of the package itself (covered by other PKG-072 deliverables).
- Facility-level integration documentation produced by the EPC Integrator (subject to EPC Integrator interface/integration review, but not authored under this deliverable).
- Individual vendor document rows are NOT separate deliverables (per `_CONTEXT.md` Notes).
- Package-specific exclusions: TBD — `PACKAGE_REGISTER.csv` row 99 records "TBD; no package-specific exclusions stated in source materials."

## Requirements

| ID | Requirement | Basis | Source |
|---|---|---|---|
| REQ-072-05-01 | The Package Vendor SHALL produce and maintain a vendor document register that lists all vendor documents for PKG-072, with at minimum: document number, title, revision, status, and transmittal reference. | Anticipated artifact in `_CONTEXT.md` | `_CONTEXT.md`; ASSUMPTION on minimum field set; clause-level basis location TBD in `26020-Package_Requirements.docx` heading 26 |
| REQ-072-05-02 | The Package Vendor SHALL submit each vendor document required by `26020-Package_Requirements.docx` heading 26 for the package, at the required revision stages. | Decomposition Source Reference | `DELIVERABLE_REGISTER.csv` row 562; ASSUMPTION — clause-level requirements `location TBD` (binary `.docx` not locally parsed) |
| REQ-072-05-03 | The vendor document turnover package SHALL cover SOW items SOW-0245, SOW-0246, SOW-0247, SOW-0248. | `_CONTEXT.md` Covers Scope Items | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| REQ-072-05-04 | The EPC Integrator SHALL perform interface/integration review of submitted vendor documents and record disposition against each register row. | Responsible Party split | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 99 |
| REQ-072-05-05 | Vendor documents marked as "source-required" SHALL be included as artifacts/evidence in the turnover package where the source row exists. | `_CONTEXT.md` Anticipated Artifacts | `_CONTEXT.md` |
| REQ-072-05-06 | Final turnover records (transmittals, sign-offs, acceptance evidence) SHALL be retained as part of the closed package. | Anticipated artifact | `_CONTEXT.md`; retention period TBD (location TBD) |
| REQ-072-05-07 | The register and submittals SHALL be consistent with the package's applicable interface types (Process Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Product Loading). | Package interfaces | `PACKAGE_REGISTER.csv` row 99 |
| REQ-072-05-08 | Specific document types, content, format, and required revision stages | TBD | `location TBD` in `26020-Package_Requirements.docx` heading 26 |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 26 | Defines the per-package vendor document requirements for PKG-072 | location TBD (binary `.docx`; not locally parsed) |
| `26020-Packages_Interfaces_4_export.xlsx` Packages row 99 | Defines package identification and applicable interfaces | location TBD (binary `.xlsx`; not locally parsed) |
| Project document control standard | Governs document numbering, revision codes, transmittal conventions | TBD — no project-level document-control standard located in `_REFERENCES.md` |
| API 2510 (referenced in DBM at line 257 for "Distance between pressurized bullets and truck loading station") | Indirect facility relevance for truck-loading context only; not a vendor-document standard per se | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §line 257 |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-072-05-01 | Inspection of register completeness against `26020-Package_Requirements.docx` heading 26 expected list (TBD clause-level mapping). |
| REQ-072-05-02 | Document-by-document audit at each required stage; verify revision and stage labels match the register. |
| REQ-072-05-03 | Trace each register row to one or more of SOW-0245…0248; flag uncovered or over-covered items. |
| REQ-072-05-04 | EPC Integrator disposition column populated for every register row before final turnover. |
| REQ-072-05-05 | Cross-check source-row artifacts against the register's "source-required" flag. |
| REQ-072-05-06 | Final transmittal log + signed acceptance evidence on file. |
| REQ-072-05-07 | Interface coverage check against PKG-072's interface type list (PACKAGE_REGISTER.csv row 99). |
| REQ-072-05-08 | TBD pending clause-level mapping from `26020-Package_Requirements.docx`. |

## Documentation

Required artifacts at deliverable closure:

- `VendorDocumentRegister.xlsx` (or equivalent register)
- Submitted vendor documents (one set per required revision stage)
- Source vendor document evidence rows (where available)
- Turnover transmittals
- Final acceptance / sign-off records
- EPC Integrator review dispositions

Specific filenames, formats, and revision codes: TBD (location TBD in `26020-Package_Requirements.docx` heading 26).
