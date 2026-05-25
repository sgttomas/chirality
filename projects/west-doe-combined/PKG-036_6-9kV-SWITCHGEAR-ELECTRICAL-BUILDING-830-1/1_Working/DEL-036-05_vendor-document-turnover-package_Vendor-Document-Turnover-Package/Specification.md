# Specification: DEL-036-05_vendor-document-turnover-package

## Scope

This deliverable is the single Package Vendor Vendor Document Turnover Package for `PKG-036` (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)). It covers the vendor document register, vendor document submittals, source-required vendor documentation (carried as artifact rows where available), and turnover records for the package, subject to EPC Integrator interface/integration review. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-036-05`.)

In scope:
- Vendor document register listing all documents the Package Vendor will submit for the package.
- Vendor document submittals (drawings, datasheets, calculations, certificates, test/inspection records, operating and maintenance manuals, shipped-loose item lists) supporting the package.
- Source vendor document table rows where exposed by source material, carried as artifacts/evidence rather than as separate deliverables.
- Turnover records associated with the package (final certified data, completed tests, marked-up/as-built content, spares/manuals) for handoff into EPC turnover.

Out of scope:
- EPC Integrator review and acceptance of submitted vendor documents (belongs to `DEL-036-06_epc-vendor-package-review-and-acceptance`; sources: `DELIVERABLE_REGISTER.csv` row `DEL-036-06`; `ARTIFACT_REGISTER.csv` `ART-FB61C5F7B1`, `ART-8F50EF826E`).
- Vendor-engineered physical equipment package itself (`DEL-036-04_vendor-engineered-equipment-package`).
- EPC Package Datasheet handoff content (`DEL-036-02_package-datasheet`).
- Construction work package planning (`DEL-036-03_construction-work-package`).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| R-036-05-01 | The Package Vendor shall be responsible for vendor documentation for this package; the EPC Integrator shall perform interface/integration review. | `DELIVERABLE_REGISTER.csv` row `DEL-036-05` (Responsible Party); `PACKAGE_REGISTER.csv` row `PKG-036` (responsibility model) | FACT |
| R-036-05-02 | The deliverable shall produce a vendor document register identifying all vendor documents to be submitted for the package. | `_CONTEXT.md` (anticipated artifacts: "Vendor document register"); `DELIVERABLE_REGISTER.csv` row `DEL-036-05` (Anticipated Artifacts) | FACT |
| R-036-05-03 | The deliverable shall produce vendor document submittals as identified by the register. | `_CONTEXT.md` (anticipated artifacts: "vendor document submittals"); `DELIVERABLE_REGISTER.csv` row `DEL-036-05` | FACT |
| R-036-05-04 | Where source material exposes specific vendor document table rows applicable to the package, those rows shall be carried as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (anticipated artifacts: "source vendor document table rows as artifacts where available"); `DELIVERABLE_REGISTER.csv` row `DEL-036-05` notes | FACT |
| R-036-05-05 | The deliverable shall produce turnover records for the package, supporting handoff into EPC turnover. | `_CONTEXT.md` (anticipated artifacts: "turnover records"); `DELIVERABLE_REGISTER.csv` row `DEL-036-05` | FACT |
| R-036-05-06 | The vendor document set shall provide the package-side data required to satisfy the twelve declared PKG-036 interface obligations: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row `PKG-036` (applicable interface types); `INTERFACE_REGISTER.csv` PKG-036 rows | FACT (set); content TBD |
| R-036-05-07 | The vendor document register and submittals should align with the general package-deliverables expectation that packages provide datasheets, utility load summaries, field tie-in lists, operating and design envelopes, materials/coating basis, maintenance access, shipped-loose item lists, and vendor document registers. The source paragraph applies to mechanical packages; applicability to this electrical-building package is directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (package deliverables paragraph) | ASSUMPTION (cross-discipline application) |
| R-036-05-08 | The vendor document set shall convey the medium-voltage 6.9 kV service basis (3 phase, 3 wire, 60 Hz, low-resistance grounded) and the 100 A / 10 s neutral grounding resistor requirement for each 6.9 kV transformer; data shall be reflected in submitted single-line, grounding, and protection documents. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2935 (medium-voltage services); line 2985 (grounding) | FACT (general); package allocation ASSUMPTION |
| R-036-05-09 | The vendor document set shall include the Ethernet communication port and plant PLC central control panel data acquisition interface description for any motor control center within the package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 | FACT (general); applicability ASSUMPTION |
| R-036-05-10 | Package-specific vendor document requirements (mandatory documents, formats, revision codes, native-file requirements, transmittal mechanics) | `ARTIFACT_REGISTER.csv` `ART-462B18445D` ("Detailed vendor-document requirements are not present in current source material for this package.") | TBD (source gap) |
| R-036-05-11 | Document control numbering, revision states, transmittal numbering, and review-cycle codes | Source gap | TBD |
| R-036-05-12 | Turnover record fields, completeness checklist, and handoff acceptance criteria | Source gap; coordination point with `DEL-036-06_epc-vendor-package-review-and-acceptance` | TBD |

## Standards

| Standard / governing source | Use | Location |
|---|---|---|
| Project-wide vendor document control standard | Document numbering, revision conventions, transmittal format | location TBD; no project-wide vendor document control source is locally accessible. |
| `26020-Package_Requirements.docx` (if it contains PKG-036 vendor document requirements) | Package-specific vendor document scope | location TBD; no PKG-036 match found in current search. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical systems and Electrical buildings sections) | 6.9 kV service basis, grounding, MCC communication, prefabricated electrical-building basis | accessible; lines 2935, 2955, 2973, 2985. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` package-deliverables paragraph | General expectation of vendor document register as a package deliverable | accessible; line 617 applies directly to mechanical packages, directional for this electrical-building package. |
| EPC vendor package review and acceptance standard | EPC review of submitted vendor documents | location TBD; method described in `DEL-036-06`. |

## Verification

| Requirement | Verification approach |
|---|---|
| R-036-05-01 | Confirm responsibility assignment in `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv`. |
| R-036-05-02 | Inspect deliverable folder for a vendor document register artifact; confirm it lists vendor documents to be submitted. |
| R-036-05-03 | Inspect submittals against register entries; confirm each register entry has a corresponding submittal status. |
| R-036-05-04 | Confirm source-derived vendor document rows are carried as artifacts under `ARTIFACT_REGISTER.csv` rather than minted as deliverables. |
| R-036-05-05 | Inspect turnover record set for the package; confirm coverage of certified data, tests, and handoff documentation. |
| R-036-05-06 | Confirm each of the twelve declared PKG-036 interfaces has package-side vendor documentation referenced from the register. |
| R-036-05-07 | EPC Integrator review judgment on alignment with the general package-deliverables expectation. |
| R-036-05-08 | Confirm submitted single-line, grounding, and protection documents reflect the 6.9 kV/grounding-resistor basis. |
| R-036-05-09 | Confirm MCC vendor documents describe Ethernet/PLC interface where MCC is in package scope. |
| R-036-05-10, R-036-05-11, R-036-05-12 | Cannot be verified until governing source is identified and resolved. |

## Documentation

Required artifacts for this deliverable, per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`:

- Vendor document register (artifact within this deliverable folder).
- Vendor document submittals (artifacts within this deliverable folder).
- Source vendor document table rows carried as artifacts where available.
- Turnover records for the package.

Cross-deliverable artifact pointers (from `ARTIFACT_REGISTER.csv`):

- `ART-462B18445D` — TBD vendor document register evidence (this deliverable).
- `ART-FB61C5F7B1` — Vendor document review and comment log (`DEL-036-06`).
- `ART-8F50EF826E` — Vendor package acceptance and turnover checklist (`DEL-036-06`).
- `ART-2E1BDD099B` — Factory/shop test and inspection evidence (`DEL-036-06`).
