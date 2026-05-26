# Specification — DEL-088-05 Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for PKG-088 Caustic Treating (Condensate Mercaptan Removal). It applies to the Package Vendor's compilation and submittal — and the EPC Integrator's review — of all vendor-authored documentation, registers, submittals, and turnover records associated with the non-regenerative caustic mercaptan treating unit for C5+ condensate.

**In scope:**
- Vendor document register (index of all vendor documents)
- Vendor document submittals (the documents themselves)
- Source-required vendor documentation per 26020-Package_Requirements.docx package heading 41
- Turnover records (acceptance, sign-off, transmittal)

**Out of scope:**
- Process design of the caustic treating unit (covered by other DEL-088-0X deliverables: scope, package datasheet, vendor-engineered-equipment package).
- EPC Integrator's acceptance decision itself (DEL-088-06).
- Individual source vendor document rows as separate deliverables (these remain artifacts/evidence per _CONTEXT.md Notes).

## Requirements

| ID | Requirement | Authority | Status |
|---|---|---|---|
| REQ-088-05-01 | The Package Vendor shall produce a Vendor Document Register indexing every vendor document associated with the package. | DBM-Comp_and_Liquids §"Mechanical Package Structure" (line 617): "Package deliverables shall include … vendor document registers." | FACT |
| REQ-088-05-02 | The Vendor Document Register shall include, per row, at minimum: document number, title, current revision, status, transmittal reference, and intended use. | ASSUMPTION (standard EPC turnover register convention); exact column set in 26020-Package_Requirements.docx heading 41 — location TBD | ASSUMPTION |
| REQ-088-05-03 | The Package Vendor shall submit each registered document via controlled transmittals to the EPC Integrator. | ASSUMPTION (standard EPC vendor-document control practice); exact transmittal protocol — location TBD | ASSUMPTION |
| REQ-088-05-04 | The submittal set shall include all source-required vendor documentation enumerated in 26020-Package_Requirements.docx package heading 41. | _REFERENCES.md; specific document list — location TBD | FACT (existence) / TBD (enumeration) |
| REQ-088-05-05 | The EPC Integrator shall perform an interface/integration review of submitted vendor documents. | _CONTEXT.md ResponsibleParty | FACT |
| REQ-088-05-06 | Turnover records evidencing receipt and acceptance shall be retained as part of the package. | _CONTEXT.md Anticipated Artifacts | FACT |
| REQ-088-05-07 | Document revisions superseded during package execution shall remain traceable in the register (revision history). | ASSUMPTION (standard practice) | ASSUMPTION |
| REQ-088-05-08 | Language and units of submitted documents shall conform to project requirements. | TBD — language/units rule not present in accessible sources | TBD |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx (package heading 41) | Governing source-required vendor documentation list | location TBD — file present in `_Sources/` but content not locally accessible to this run |
| Workbook Packages row 50 | Decomposition row for this package | location TBD — workbook inaccessible to this run |
| DBM-Comp_and_Liquids (3-25 DBM) — §"Mechanical Package Structure" | States that vendor document registers are a required package deliverable | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Project document-control standard | Governs transmittal numbering, revision codes, status codes | TBD — not located in accessible sources |

## Verification

| Requirement | Verification Method |
|---|---|
| REQ-088-05-01 | Documentary inspection: confirm a Vendor Document Register exists and lists each submitted document. |
| REQ-088-05-02 | Documentary inspection: confirm register row schema against project document-control standard (TBD). |
| REQ-088-05-03 | Documentary inspection: confirm each register row has a corresponding transmittal reference. |
| REQ-088-05-04 | Cross-check register against 26020-Package_Requirements.docx heading 41 enumeration (when accessible). |
| REQ-088-05-05 | Documentary inspection: EPC Integrator review records exist and reference register entries. |
| REQ-088-05-06 | Documentary inspection: turnover records signed and dated by Package Vendor and EPC Integrator. |
| REQ-088-05-07 | Documentary inspection: superseded revisions retained in register history. |
| REQ-088-05-08 | TBD pending REQ-088-05-08 closure. |

## Documentation

Required artifacts (per _CONTEXT.md Anticipated Artifacts):

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records (transmittals, acceptance/sign-off)
