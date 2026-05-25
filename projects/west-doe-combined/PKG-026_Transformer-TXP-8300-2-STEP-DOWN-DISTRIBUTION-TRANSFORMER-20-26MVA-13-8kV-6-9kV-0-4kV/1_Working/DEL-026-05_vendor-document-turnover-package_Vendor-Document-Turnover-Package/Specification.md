# Specification: DEL-026-05_vendor-document-turnover-package

## Scope

This deliverable is the single Package Vendor Vendor Document Turnover Package for `PKG-026` (Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV). It covers the vendor document register, vendor document submittals, source-required vendor documentation (carried as artifact rows where available), and turnover records for the package, subject to EPC Integrator interface/integration review. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-026-05`.)

In scope:
- Vendor document register listing all documents the Package Vendor will submit for the package.
- Vendor document submittals (drawings, datasheets, calculations, certificates, test/inspection records, operating and maintenance manuals, shipped-loose item lists) supporting the package.
- Source vendor document table rows where exposed by source material, carried as artifacts/evidence rather than as separate deliverables.
- Turnover records associated with the package (final certified data, completed tests, marked-up/as-built content, spares/manuals) for handoff into EPC turnover.

Out of scope:
- EPC Integrator review and acceptance of submitted vendor documents (belongs to `DEL-026-06_epc-vendor-package-review-and-acceptance`; sources: `DELIVERABLE_REGISTER.csv` row `DEL-026-06`; `ARTIFACT_REGISTER.csv` `ART-AF00FF6B63`, `ART-28805E8681`).
- Vendor-engineered physical equipment package itself (`DEL-026-04_vendor-engineered-equipment-package`).
- EPC Package Datasheet handoff content (`DEL-026-02_package-datasheet`).
- Construction work package planning (`DEL-026-03_construction-work-package`).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| R-026-05-01 | The Package Vendor shall be responsible for vendor documentation for this package; the EPC Integrator shall perform interface/integration review. | `DELIVERABLE_REGISTER.csv` row `DEL-026-05` (Responsible Party); `PACKAGE_REGISTER.csv` row `PKG-026` (responsibility model) | FACT |
| R-026-05-02 | The deliverable shall produce a vendor document register identifying all vendor documents to be submitted for the package. | `_CONTEXT.md` (anticipated artifacts: "Vendor document register"); `DELIVERABLE_REGISTER.csv` row `DEL-026-05` (Anticipated Artifacts) | FACT |
| R-026-05-03 | The deliverable shall produce vendor document submittals as identified by the register. | `_CONTEXT.md` (anticipated artifacts: "vendor document submittals"); `DELIVERABLE_REGISTER.csv` row `DEL-026-05` | FACT |
| R-026-05-04 | Where source material exposes specific vendor document table rows applicable to the package, those rows shall be carried as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (anticipated artifacts: "source vendor document table rows as artifacts where available"); `DELIVERABLE_REGISTER.csv` row `DEL-026-05` notes | FACT |
| R-026-05-05 | The deliverable shall produce turnover records for the package, supporting handoff into EPC turnover. | `_CONTEXT.md` (anticipated artifacts: "turnover records"); `DELIVERABLE_REGISTER.csv` row `DEL-026-05` | FACT |
| R-026-05-06 | The vendor document set shall provide the package-side data required to satisfy PKG-026 interface obligations: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row `PKG-026` (applicable interface types); `INTERFACE_REGISTER.csv` rows `IFC-E9FC2B952D`, `IFC-FE5C9BD828`, `IFC-0230019D52`, `IFC-25E2CF2BD9`, `IFC-E6E0E1FA2B`, `IFC-93877B34D5`, `IFC-7DD82CAE51` | FACT (set); content TBD |
| R-026-05-07 | The vendor document register and submittals should align with the general package-deliverables expectation that packages provide datasheets, utility load summaries, field tie-in lists, operating and design envelopes, materials/coating basis, maintenance access, shipped-loose item lists, and vendor document registers. The source paragraph applies to mechanical packages; applicability to this electrical transformer package is directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph) | ASSUMPTION (cross-discipline application) |
| R-026-05-08 | Package-specific vendor document requirements (mandatory documents, formats, revision codes, native-file requirements, transmittal mechanics) | `ARTIFACT_REGISTER.csv` `ART-C8E49463BD` ("Detailed vendor-document requirements are not present in current source material for this package.") | TBD (source gap) |
| R-026-05-09 | Document control numbering, revision states, transmittal numbering, and review-cycle codes | Source gap | TBD |
| R-026-05-10 | Turnover record fields, completeness checklist, and handoff acceptance criteria | Source gap; coordination point with `DEL-026-06_epc-vendor-package-review-and-acceptance` | TBD |

## Standards

| Standard / governing source | Use | Location |
|---|---|---|
| Project-wide vendor document control standard | Document numbering, revision conventions, transmittal format | location TBD; no project-wide vendor document control source is locally accessible. |
| `26020-Package_Requirements.docx` (if it contains PKG-026 vendor document requirements) | Package-specific vendor document scope | location TBD; no PKG-026 match found in current search. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` package-deliverables paragraph | General expectation of vendor document register as a package deliverable | accessible; applies directly to mechanical packages, directional for this electrical transformer package. |
| EPC vendor package review and acceptance standard | EPC review of submitted vendor documents | location TBD; method described in `DEL-026-06`. |

## Verification

| Requirement | Verification approach |
|---|---|
| R-026-05-01 | Confirm responsibility assignment in `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv`. |
| R-026-05-02 | Inspect deliverable folder for a vendor document register artifact; confirm it lists vendor documents to be submitted. |
| R-026-05-03 | Inspect submittals against register entries; confirm each register entry has a corresponding submittal status. |
| R-026-05-04 | Confirm source-derived vendor document rows are carried as artifacts under `ARTIFACT_REGISTER.csv` rather than minted as deliverables. |
| R-026-05-05 | Inspect turnover record set for the package; confirm coverage of certified data, tests, and handoff documentation. |
| R-026-05-06 | Confirm each applicable interface (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) has package-side vendor documentation referenced from the register. |
| R-026-05-07 | EPC Integrator review judgment on alignment with the general package-deliverables expectation. |
| R-026-05-08, R-026-05-09, R-026-05-10 | Cannot be verified until governing source is identified and resolved. |

## Documentation

Required artifacts for this deliverable, per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`:

- Vendor document register (artifact within this deliverable folder).
- Vendor document submittals (artifacts within this deliverable folder).
- Source vendor document table rows carried as artifacts where available.
- Turnover records for the package.

Cross-deliverable artifact pointers (from `ARTIFACT_REGISTER.csv`):

- `ART-C8E49463BD` — TBD vendor document register evidence (this deliverable).
- `ART-AF00FF6B63` — Vendor document review and comment log (`DEL-026-06`).
- `ART-28805E8681` — Vendor package acceptance and turnover checklist (`DEL-026-06`).
- `ART-063BACA4E7` — Factory/shop test and inspection evidence (`DEL-026-06`).
