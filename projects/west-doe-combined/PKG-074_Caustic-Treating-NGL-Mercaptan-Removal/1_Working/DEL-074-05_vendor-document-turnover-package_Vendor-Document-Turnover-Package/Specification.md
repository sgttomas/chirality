# Specification: DEL-074-05 — Vendor Document Turnover Package

## Scope

### In scope
- Single Package Vendor deliverable for the Caustic Treating (NGL Mercaptan Removal) package (`PKG-074`).
- Compilation, maintenance, and submission of the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for the package.
- Carrying individual source vendor document table rows as artifacts/evidence within this deliverable rather than as separate deliverables.
- Provision of vendor documentation for EPC Integrator interface/integration review.

### Out of scope
- Engineering, design, fabrication, supply, and physical equipment scope, which belong to `DEL-074-04_vendor-engineered-equipment-package`.
- EPC integration acceptance evidence and review log, which belong to `DEL-074-06_epc-vendor-package-review-and-acceptance`.
- Package scope definition (`DEL-074-01`) and package technical datasheet (`DEL-074-02`).

## Requirements

| ID | Requirement | Authority | Notes |
|---|---|---|---|
| REQ-074-05-01 | The Package Vendor shall produce and maintain a vendor document register covering all required documents for `PKG-074`. | `_CONTEXT.md` Anticipated Artifacts | Document list TBD pending source slice. |
| REQ-074-05-02 | The Package Vendor shall submit vendor document submittals against the register through revisions until acceptance. | `_CONTEXT.md` Anticipated Artifacts | Submittal cycle, classes, and acceptance criteria TBD (location TBD). |
| REQ-074-05-03 | Source-required vendor documentation called out by the package requirements source shall be included in the register and submitted. | Decomposition row 274; `26020-Package_Requirements.docx` heading 28 (location TBD) | Exact source-required list TBD. |
| REQ-074-05-04 | Individual source vendor document table rows shall be carried as artifacts/evidence within this deliverable. | Decomposition row 274 notes | ASSUMPTION: register-row-as-artifact convention applies as written in decomposition narrative. |
| REQ-074-05-05 | Turnover records shall be assembled and submitted for the vendor documentation set. | `_CONTEXT.md` Anticipated Artifacts | Turnover record composition TBD. |
| REQ-074-05-06 | Vendor documentation shall be made available to the EPC Integrator for interface/integration review. | Decomposition row 274 responsible-party field | Review path details TBD; ASSUMPTION: follows package-level review convention. |
| REQ-074-05-07 | Document numbering, revision control, and status conventions shall conform to project document control rules. | TBD | Project-level rules location TBD. |

## Standards

- `26020-Package_Requirements.docx` package heading 28 — governing package requirements source for vendor documentation scope (location TBD; binary, not locally accessible as text).
- Project document control standards (TBD).
- ASSUMPTION: industry-standard EPC vendor document and turnover practices apply where the source is silent; specific standard identifiers TBD.

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-074-05-01 | Inspection of issued vendor document register against `26020-Package_Requirements.docx` heading 28 once the source slice is accessible. |
| REQ-074-05-02 | Audit of submittal log against the register; check that each register entry has at least one submittal record. |
| REQ-074-05-03 | Cross-reference of source-required document list (from package requirements source) against the register. |
| REQ-074-05-04 | Inspection of register: each source-row artifact is present as evidence rather than as a standalone deliverable. |
| REQ-074-05-05 | Review of turnover record set for completeness against the register. |
| REQ-074-05-06 | EPC Integrator review log (carried by `DEL-074-06`) confirms vendor documentation was made available and reviewed. |
| REQ-074-05-07 | Document-control audit against project numbering and revision-control rules. |

## Documentation

Required artifacts to be produced and assembled in this deliverable:

- Vendor document register
- Vendor document submittals
- Source vendor document table rows (carried as evidence/artifacts)
- Turnover records
- (Anticipated) submittal log / transmittal records — TBD
- (Anticipated) document-control conformance evidence — TBD
