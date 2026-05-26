# Specification — DEL-050-05 Vendor Document Turnover Package

## Scope

This specification governs the Package Vendor's compilation, transmittal, and turnover of vendor documentation for **PKG-050 Stabilizer Overheads Compressors**. It covers:

- the vendor document register,
- vendor document submittals (engineering and quality),
- source-required vendor documentation cited or implied by the package scope,
- and turnover records demonstrating closure.

**Excludes:** EPC-side review and acceptance (covered by sibling deliverable `DEL-050-06_epc-vendor-package-review-and-acceptance`); construction execution (covered by `DEL-050-03_construction-work-package`); engineered equipment design content itself (covered by `DEL-050-04_vendor-engineered-equipment-package`).

Sources: `_CONTEXT.md` (Scope, Anticipated Artifacts); `DELIVERABLE_REGISTER.csv` Gate 7 snapshot.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-050-05-01 | The Package Vendor shall produce a Vendor Document Register enumerating every required vendor document for the package, with document number, title, class, revision, status, transmittal reference, and acceptance state. | DBM-Comp_and_Liquids §617 (vendor document registers required); ASSUMPTION on detail columns. |
| R-050-05-02 | The vendor document register shall remain the single, current index of vendor documentation for PKG-050 throughout submittal and turnover. | ASSUMPTION (industry convention; consistent with §617 register requirement). |
| R-050-05-03 | The Package Vendor shall transmit submittals through controlled transmittals identifying document IDs, revision, submittal type (e.g., for-review, for-approval, certified, as-built), and required response. | TBD — submittal workflow not located in accessible source slices. |
| R-050-05-04 | Source-required vendor documentation referenced by the package scope of work (`SOW-0173`–`SOW-0176`) shall be included and traceable to the SOW row. | `_CONTEXT.md` Covers Scope Items; SOW row text not in accessible slices — content TBD. |
| R-050-05-05 | A turnover record shall be produced demonstrating that each register entry has reached its required acceptance state and that final certified/as-built revisions have been delivered. | DELIVERABLE_REGISTER.csv ("turnover records"); detail TBD. |
| R-050-05-06 | The vendor document turnover package shall be compatible with EPC Integrator review and acceptance workflows (`DEL-050-06`). | Decomposition narrative; interface detail TBD. |
| R-050-05-07 | Document classes (drawings, calculations, manuals, certifications, ITPs, MTRs, weld records, test/inspection reports, spares lists) shall each be enumerated where applicable. | ASSUMPTION (industry convention for compressor packages); explicit class list TBD. |

## Standards

- Package Requirements specification: `26020-Package_Requirements.docx` package heading 5 — **location TBD** (source not text-accessible in this run).
- Comp & Liquids Design Basis Manual: `3-25_Comp_and_Liquids_DBM.md` §617 — vendor document register requirement.
- Project document control standard: TBD.
- Applicable equipment codes (compressor-specific, e.g., API standards): TBD — not derivable from accessible slices.

## Verification

| Req ID | Verification Approach |
|---|---|
| R-050-05-01 | Inspection of vendor document register against required column set and PKG-050 scope coverage. |
| R-050-05-02 | Audit of register revision history against transmittals. |
| R-050-05-03 | Review of transmittal log against register entries; sample transmittal inspection. |
| R-050-05-04 | Traceability check: each `SOW-0173`–`SOW-0176` row mapped to register entries. |
| R-050-05-05 | Turnover record review: every register entry reaches required acceptance state with certified/as-built revision. |
| R-050-05-06 | Cross-deliverable review against `DEL-050-06` acceptance checklist. |
| R-050-05-07 | Document-class completeness check against PKG-050 equipment scope. |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records

Additional anticipated artifacts (ASSUMPTION):

- Transmittal log
- Final certified/as-built document index
- Turnover acceptance sign-off
