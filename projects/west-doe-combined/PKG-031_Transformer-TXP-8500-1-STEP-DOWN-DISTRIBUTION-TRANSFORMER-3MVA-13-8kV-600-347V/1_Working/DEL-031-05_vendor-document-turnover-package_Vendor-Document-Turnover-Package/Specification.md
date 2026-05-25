# Specification: DEL-031-05 — Vendor Document Turnover Package

## Scope

### In scope
- Vendor document register for PKG-031 (Transformer TXP-8500-1, 3 MVA 13.8 kV / 600/347 V step-down distribution transformer).
- Vendor document submittals across the package lifecycle (engineering, fabrication, factory test, shipping, field, commissioning, turnover).
- Source-required vendor documentation rows from `26020-Package_Requirements.docx` matched to PKG-031, carried as artifacts/evidence within this deliverable per DEC-004 and DEC-012.
- Turnover records (final transmittal, completeness sign-off, acceptance evidence) for the package vendor scope.

### Out of scope
- Vendor engineering, design, fabrication, and equipment supply (DEL-031-04 Vendor Engineered Equipment Package).
- EPC integrator review and acceptance evidence (DEL-031-06 EPC Vendor Package Review and Acceptance).
- EPC package scope, datasheet, and construction work package (DEL-031-01, DEL-031-02, DEL-031-03).

## Requirements

| ID | Requirement | Source | Notes |
|---|---|---|---|
| REQ-031-05-01 | Maintain a vendor document register identifying every vendor document required for PKG-031, with document number, title, revision, transmittal, status, and turnover state. | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv | ASSUMPTION (deliverable-type convention); detailed register schema location TBD in source. |
| REQ-031-05-02 | Submit each required vendor document through the agreed transmittal process and record receipt, review status, and acceptance. | `_CONTEXT.md` | ASSUMPTION; specific transmittal protocol not extracted from source. |
| REQ-031-05-03 | Include all source-required vendor documents identified in the PKG-031 section of `_Sources/26020-Package_Requirements.docx` vendor-documentation tables as artifacts under this deliverable. | PROJECT_DECOMP DEC-004; DEC-012; `_Sources/26020-Package_Requirements.docx` | Exact PKG-031 section and table contents `location TBD`; no local slice copied. |
| REQ-031-05-04 | Produce turnover records demonstrating completeness of the vendor document set, including final transmittal, register reconciliation, and acceptance sign-off. | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv; OBJ-010 | OBJ-010 establishes turnover/closure evidence as a package-level objective. |
| REQ-031-05-05 | Provide EPC Integrator with access to the register and submittals for interface/integration review. | `_CONTEXT.md` ResponsibleParty (EPC Integrator interface/integration review) | Review interface mechanism not specified in extracted sources. |
| REQ-031-05-06 | Preserve vendor document ownership and responsibility with the Package Vendor; the EPC Integrator does not author vendor documents. | PROJECT_DECOMP DEC-006; OBJ-004 | Hard responsibility boundary. |
| REQ-031-05-07 | Track open items, holds, and unresolved comments against vendor documents until closure or accepted disposition. | OBJ-010 (controlled open-item closure evidence) | ASSUMPTION; specific open-item tracking format TBD. |

## Standards

| Standard / Reference | Relevance | Location |
|---|---|---|
| `26020-Package_Requirements.docx` — PKG-031 section, vendor-documentation tables | Defines the required vendor document list for the package | `_Sources/26020-Package_Requirements.docx` (PKG-031 section — location TBD) |
| `26020-Packages_Interfaces_4_export.xlsx` — Packages row 33 | Package identity and scope basis | `_Sources/26020-Packages_Interfaces_4_export.xlsx` |
| Project DBMs (DBM-Comp_and_Liquids, DBM-Deepcut) | Design basis context for objectives and package boundaries | `_Sources/` (no PKG-031 slice extracted) |
| Industry transformer vendor documentation standards (e.g., IEEE C57 series, vendor QA manuals) | Likely applicable to scope of typical vendor document set | ASSUMPTION: likely applicable; not cited in extracted source slices |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-031-05-01 | Register exists, is complete against the source vendor-documentation table, and is current as of each transmittal. |
| REQ-031-05-02 | Transmittal log evidences every register row; submitted documents are present in the submittal folder with revision match. |
| REQ-031-05-03 | Cross-check register against PKG-031 source section of `26020-Package_Requirements.docx`; flag missing items. |
| REQ-031-05-04 | Turnover record set includes final transmittal, completeness reconciliation, and Package Vendor sign-off; EPC acceptance recorded under DEL-031-06. |
| REQ-031-05-05 | EPC Integrator review log shows access and review disposition for each register row. |
| REQ-031-05-06 | Author attribution on every vendor document is the Package Vendor or its sub-suppliers; no EPC-authored vendor documents. |
| REQ-031-05-07 | Open-item log is current; closed items have accepted disposition recorded. |

## Documentation

- Vendor document register (artifact)
- Vendor document submittals (artifacts)
- Source vendor-document table rows for PKG-031 (artifacts)
- Turnover records (artifacts)
- Open-item / hold log (artifact, when required)
