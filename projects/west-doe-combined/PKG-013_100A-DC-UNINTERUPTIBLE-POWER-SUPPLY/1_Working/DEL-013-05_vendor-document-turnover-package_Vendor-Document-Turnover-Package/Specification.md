# Specification: DEL-013-05_vendor-document-turnover-package

## Scope

This deliverable is the single Package Vendor Vendor Document Turnover Package for `PKG-013` (100A DC UNINTERUPTIBLE POWER SUPPLY). It covers the vendor document register, vendor document submittals, source-required vendor documentation (carried as artifact rows where available), and turnover records for the package, subject to EPC Integrator interface/integration review. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-013-05`.)

In scope:
- Vendor document register listing all documents the Package Vendor will submit for the package.
- Vendor document submittals (drawings, datasheets, calculations, certificates, test/inspection records, operating and maintenance manuals, shipped-loose item lists) supporting the package.
- Source vendor document table rows where exposed by source material, carried as artifacts/evidence rather than as separate deliverables.
- Turnover records associated with the package (final certified data, completed tests, marked-up/as-built content, spares/manuals) for handoff into EPC turnover.

Out of scope:
- EPC Integrator review and acceptance of submitted vendor documents (belongs to `DEL-013-06_epc-vendor-package-review-and-acceptance`; sources: `DELIVERABLE_REGISTER.csv` row `DEL-013-06`; `ARTIFACT_REGISTER.csv` `ART-BF80E6E249`, `ART-E565B29B24`).
- Vendor-engineered physical equipment package itself (`DEL-013-04_vendor-engineered-equipment-package`).
- EPC Package Datasheet handoff content (`DEL-013-02_package-datasheet`).
- Construction work package planning (`DEL-013-03_construction-work-package`).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| R-013-05-01 | The Package Vendor shall be responsible for vendor documentation for this package; the EPC Integrator shall perform interface/integration review. | `DELIVERABLE_REGISTER.csv` row `DEL-013-05` (Responsible Party); `PACKAGE_REGISTER.csv` row `PKG-013` (responsibility model) | FACT |
| R-013-05-02 | The deliverable shall produce a vendor document register identifying all vendor documents to be submitted for the package. | `_CONTEXT.md` (anticipated artifacts: "Vendor document register"); `DELIVERABLE_REGISTER.csv` row `DEL-013-05` (Anticipated Artifacts) | FACT |
| R-013-05-03 | The deliverable shall produce vendor document submittals as identified by the register. | `_CONTEXT.md` (anticipated artifacts: "vendor document submittals"); `DELIVERABLE_REGISTER.csv` row `DEL-013-05` | FACT |
| R-013-05-04 | Where source material exposes specific vendor document table rows applicable to the package, those rows shall be carried as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (anticipated artifacts: "source vendor document table rows as artifacts where available"); `DELIVERABLE_REGISTER.csv` row `DEL-013-05` notes | FACT |
| R-013-05-05 | The deliverable shall produce turnover records for the package, supporting handoff into EPC turnover. | `_CONTEXT.md` (anticipated artifacts: "turnover records"); `DELIVERABLE_REGISTER.csv` row `DEL-013-05` | FACT |
| R-013-05-06 | The vendor document set shall provide the package-side data required to satisfy PKG-013 interface obligations: Electrical Power, Grounding / Bonding, Maintenance Access, Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row `PKG-013` (applicable interface types); `INTERFACE_REGISTER.csv` rows `IFC-3B1ED82A25`, `IFC-8093ECDA51`, `IFC-DA9E0BAB70`, `IFC-CAE19AED68` | FACT (set); content TBD |
| R-013-05-07 | The vendor document register and submittals should align with the general package-deliverables expectation that packages provide datasheets, utility load summaries, field tie-in lists, operating and design envelopes, materials/coating basis, maintenance access, shipped-loose item lists, and vendor document registers. The source paragraph applies to mechanical packages; applicability to this electrical UPS package is directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph) | ASSUMPTION (cross-discipline application) |
| R-013-05-08 | Package-specific vendor document requirements (mandatory documents, formats, revision codes, native-file requirements, transmittal mechanics) | `ARTIFACT_REGISTER.csv` `ART-23F404EC4B` ("Detailed vendor-document requirements are not present in current source material for this package.") | TBD (source gap) |
| R-013-05-09 | Document control numbering, revision states, transmittal numbering, and review-cycle codes | Source gap | TBD |
| R-013-05-10 | Turnover record fields, completeness checklist, and handoff acceptance criteria | Source gap; coordination point with `DEL-013-06_epc-vendor-package-review-and-acceptance` | TBD |

## Standards

| Standard / governing source | Use | Location |
|---|---|---|
| Project-wide vendor document control standard | Document numbering, revision conventions, transmittal format | location TBD; no project-wide vendor document control source is locally accessible. |
| `26020-Package_Requirements.docx` (if it contains PKG-013 vendor document requirements) | Package-specific vendor document scope | location TBD; no PKG-013 match found in current search. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` package-deliverables paragraph | General expectation of vendor document register as a package deliverable | accessible; applies directly to mechanical packages, directional for this electrical package. |
| EPC vendor package review and acceptance standard | EPC review of submitted vendor documents | location TBD; method described in `DEL-013-06`. |

## Verification

| Requirement | Verification approach |
|---|---|
| R-013-05-01 | Confirm responsibility assignment in `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv`. |
| R-013-05-02 | Inspect deliverable folder for a vendor document register artifact; confirm it lists vendor documents to be submitted. |
| R-013-05-03 | Inspect submittals against register entries; confirm each register entry has a corresponding submittal status. |
| R-013-05-04 | Confirm source-derived vendor document rows are carried as artifacts under `ARTIFACT_REGISTER.csv` rather than minted as deliverables. |
| R-013-05-05 | Inspect turnover record set for the package; confirm coverage of certified data, tests, and handoff documentation. |
| R-013-05-06 | Confirm each applicable interface (Electrical Power, Grounding / Bonding, Maintenance Access, Structural / Foundations / Supports) has package-side vendor documentation referenced from the register. |
| R-013-05-07 | EPC Integrator review judgment on alignment with the general package-deliverables expectation. |
| R-013-05-08, R-013-05-09, R-013-05-10 | Cannot be verified until governing source is identified and resolved. |

## Documentation

Required artifacts for this deliverable, per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`:

- Vendor document register (artifact within this deliverable folder).
- Vendor document submittals (artifacts within this deliverable folder).
- Source vendor document table rows carried as artifacts where available.
- Turnover records for the package.

Cross-deliverable artifact pointers (from `ARTIFACT_REGISTER.csv`):

- `ART-23F404EC4B` — TBD vendor document register evidence (this deliverable).
- `ART-BF80E6E249` — Vendor document review and comment log (`DEL-013-06`).
- `ART-E565B29B24` — Vendor package acceptance and turnover checklist (`DEL-013-06`).
- `ART-6CC0DC45E9` — Factory/shop test and inspection evidence (`DEL-013-06`).
