# Guidance — DEL-061-05 Vendor Document Turnover Package

## Purpose

The vendor document turnover package exists to give the EPC Integrator a complete, controlled, traceable set of vendor documents for PKG-061 — sufficient for design integration, construction, commissioning, operations handover, and long-term plant records. It is the documentation backbone that lets the EPC accept the engineered equipment package (`DEL-061-04`) and close out the EPC review and acceptance deliverable (`DEL-061-06`).

## Principles

- **Single accountable register.** One Vendor Document Index (PRQ-009) is the source of truth for what the vendor owes. Every transmittal updates the index status.
- **Source-grounded inclusion.** The vendor document set is anchored in the Mechanical/rotating-equipment "Vendor Engineering Deliverables" list from `_Sources/26020-Package_Requirements.docx` (Tank Pumps section is the nearest documented comparator). Inclusion is verified against actual package scope, not assumed by template.
- **Interface-aware filtering.** Use Workbook row 75 applicability (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) to confirm interface-specific documents are in scope; explicitly exclude or mark N/A for non-applicable interfaces.
- **Evidence, not duplication.** Source documents (e.g., PRO-008 P&IDs, MEC-007 pump data sheets) are evidence artifacts, not separate deliverables — per decomposition row 418 note.
- **Closeout discipline.** Turnover records must demonstrate that every document on the index is at its final accepted revision before handover.

## Considerations

- **Building-wrapper deliverable.** PKG-061 is a building that aggregates rotating-equipment packages (Tank Pumps and related per decomposition pointer to package heading 17 in `26020-Package_Requirements.docx`). The vendor document set may need to span multiple equipment scopes inside the building. Confirm sub-package scope at PRQ-009 issuance.
- **EPC Integrator interface review.** Because the EPC reviews documents at every flagged interface (13 interfaces are `X` on row 75), the document set must explicitly address each one. Missing an interface document is the most common gap.
- **Document timing vs. construction.** Several documents (PIP-024 hydrotest packages, ELE-029/030 electrical FAT/SAT, INS-006 hookup, MEC-017 setting drawings) are needed before construction can proceed; others (PIP-028 as-builts, INS-029 instrument as-builts) close out after construction.
- **Data Book finality.** The Vendor Data Book (PRQ-016/MEC-023) is final-issue only; superseded revisions should be archived not included in the turnover book.

## Trade-offs

- **Tighter index discipline ↔ vendor flexibility.** A strict early-locked PRQ-009 reduces gap risk but limits the vendor's ability to revise document scope as engineering matures. Recommended: lock index at IFR-stage with a controlled change procedure.
- **Native vendor numbering ↔ project numbering.** Vendors typically have their own document numbering. The project document control procedure (DOC-008) governs reconciliation. Choose one canonical project number per document for the index.
- **Volume vs. usefulness.** Over-inclusion (every vendor internal drawing) bloats the Data Book; under-inclusion creates operations risk. Anchor inclusion to the Datasheet "Construction" set and the EPC review interfaces.

## Examples

- Example index row: `PRQ-009 / VDR-PKG061-MEC-007-001 / Pump Data Sheet (P-9290-1) / IFA / 2026-MM-DD / Submitted / EPC-Reviewed`.
- Example interface-driven inclusion: Workbook row 75 flags "Fire & Gas / Safety Systems" = X, so TSF-002/003/004/009/011/013/028 are in scope and must appear in PRQ-009.
- Example exclusion: Workbook row 75 leaves "Cathodic Protection" blank; no CP-specific vendor document is required for this package's turnover unless EPC explicitly adds it.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Decomposition cites "package heading 17" of `26020-Package_Requirements.docx` as basis for the NGL Booster and Transfer Pumps Building, but no heading with that exact title was found in the accessible source slice (`PT-18-002 Tank Pumps` is the nearest mechanical/pump package; the building wrapper is not present as a standalone heading). | `_Decomposition/.../DELIVERABLE_REGISTER.csv` line 418 (Source Reference column) | `_Sources/26020-Package_Requirements.docx` TOC enumeration (no explicit "NGL Booster and Transfer Pumps Building" heading in accessible text) | Datasheet "Construction" table; Specification R-01 scope | Treat Workbook row 75 as the authoritative package identity and the Tank Pumps "Vendor Engineering Deliverables" table as the nearest documented comparator for the vendor document set; confirm at PRQ-009 issuance. | TBD |
| C-02 | Vendor document workflow stages (IFR/IFA/IFC/AB) and revision matrix are not present in the accessible source slice. | n/a | n/a | Specification R-03 | Adopt project document control procedure default; mark `location TBD` until source confirmed. | TBD |
