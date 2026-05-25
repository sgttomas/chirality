# Specification: DEL-039-05_vendor-document-turnover-package

## Scope

This deliverable is the single Package Vendor Vendor Document Turnover Package for `PKG-039` (600V ELECTRICAL BUILDING (850-1) — the 600 V Inlet / Sales Compressor Electrical Building per the DBM Shop electrical-buildings table). It covers the vendor document register, vendor document submittals, source-required vendor documentation (carried as artifact rows where available), and turnover records for the package, subject to EPC Integrator interface/integration review. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Shop table.)

In scope:
- Vendor document register listing all documents the Package Vendor will submit for the package.
- Vendor document submittals (drawings, datasheets, calculations, certificates, test/inspection records, operating and maintenance manuals, shipped-loose item lists) supporting the building and its installed electrical equipment subset.
- Source vendor document table rows where exposed by source material, carried as artifacts/evidence rather than as separate deliverables.
- Turnover records associated with the package (final certified data, completed tests, marked-up/as-built content, spares/manuals) for handoff into EPC turnover.

Out of scope:
- EPC Integrator review and acceptance of submitted vendor documents (belongs to `DEL-039-06_epc-vendor-package-review-and-acceptance`; sources: `DELIVERABLE_REGISTER.csv` row `DEL-039-06`; `ARTIFACT_REGISTER.csv` `ART-3910447327`, `ART-AA4BFB86C9`).
- Vendor-engineered physical equipment package itself (`DEL-039-04_vendor-engineered-equipment-package`).
- EPC Package Datasheet handoff content (`DEL-039-02_package-datasheet`).
- Construction work package planning (`DEL-039-03_construction-work-package`).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| R-039-05-01 | The Package Vendor shall be responsible for vendor documentation for this package; the EPC Integrator shall perform interface/integration review. | `DELIVERABLE_REGISTER.csv` row `DEL-039-05` (Responsible Party); `PACKAGE_REGISTER.csv` row `PKG-039` (responsibility model) | FACT |
| R-039-05-02 | The deliverable shall produce a vendor document register identifying all vendor documents to be submitted for the package. | `_CONTEXT.md` (anticipated artifacts: "Vendor document register"); `DELIVERABLE_REGISTER.csv` row `DEL-039-05` (Anticipated Artifacts) | FACT |
| R-039-05-03 | The deliverable shall produce vendor document submittals as identified by the register. | `_CONTEXT.md` (anticipated artifacts: "vendor document submittals"); `DELIVERABLE_REGISTER.csv` row `DEL-039-05` | FACT |
| R-039-05-04 | Where source material exposes specific vendor document table rows applicable to the package, those rows shall be carried as artifacts/evidence rather than as separate deliverables. | `_CONTEXT.md` (anticipated artifacts: "source vendor document table rows as artifacts where available"); `DELIVERABLE_REGISTER.csv` row `DEL-039-05` notes | FACT |
| R-039-05-05 | The deliverable shall produce turnover records for the package, supporting handoff into EPC turnover. | `_CONTEXT.md` (anticipated artifacts: "turnover records"); `DELIVERABLE_REGISTER.csv` row `DEL-039-05` | FACT |
| R-039-05-06 | The vendor document set shall provide the package-side data required to satisfy the twelve PKG-039 interface obligations: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row `PKG-039` (applicable interface types); `INTERFACE_REGISTER.csv` rows `IFC-A257E2C89C`, `IFC-5C80D8C3EC`, `IFC-C1DF6B8DD9`, `IFC-9653B84E14`, `IFC-4BC9BD20C1`, `IFC-3F18DB0D3A`, `IFC-B95212AB85`, `IFC-D8A8F7FEBC`, `IFC-9C0AFE36A2`, `IFC-D971A17948`, `IFC-50A5B3F280`, `IFC-E3D0A5A836` | FACT (set); content TBD |
| R-039-05-07 | The vendor document register and submittals should align with the general package-deliverables expectation that packages provide datasheets, utility load summaries, field tie-in lists, operating and design envelopes, materials/coating basis, maintenance access, shipped-loose item lists, and vendor document registers. The source paragraph applies to mechanical packages; applicability to this electrical building package is directional. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (package deliverables paragraph) | ASSUMPTION (cross-discipline application) |
| R-039-05-08 | The vendor document set shall describe the building features called out in the DBM Electrical Buildings paragraphs that are within the actually-installed subset for 850-1: prefabricated/modular construction, climate-control HVAC sized n + 1, bottom-entry cable arrangement, building elevated/installed on piles, TECK/ACIC wiring with EMT for adjacent panels, exterior GFI receptacle, and door sizing (or removable transom sections) for removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs | FACT (basis); installed subset TBD |
| R-039-05-09 | Package-specific vendor document requirements (mandatory documents, formats, revision codes, native-file requirements, transmittal mechanics) | `ARTIFACT_REGISTER.csv` `ART-A64A8A25DC` ("Detailed vendor-document requirements are not present in current source material for this package.") | TBD (source gap) |
| R-039-05-10 | Document control numbering, revision states, transmittal numbering, and review-cycle codes | Source gap | TBD |
| R-039-05-11 | Turnover record fields, completeness checklist, and handoff acceptance criteria | Source gap; coordination point with `DEL-039-06_epc-vendor-package-review-and-acceptance` | TBD |

## Standards

| Standard / governing source | Use | Location |
|---|---|---|
| Project-wide vendor document control standard | Document numbering, revision conventions, transmittal format | location TBD; no project-wide vendor document control source is locally accessible. |
| `26020-Package_Requirements.docx` (if it contains PKG-039 vendor document requirements) | Package-specific vendor document scope | location TBD; no PKG-039 match found in current search. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` package-deliverables paragraph | General expectation of vendor document register as a package deliverable | accessible; applies directly to mechanical packages, directional for this electrical building package. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings paragraphs | Electrical-building feature basis (prefab/modular, HVAC, bottom entry, piles, wiring methods, doors, GFI receptacle) | accessible. |
| Canadian Electrical Code (CEC) | Electrical installation basis for the building's installed electrical equipment | applicable as source-supported basis (referenced by DBM electrical section); clause locations TBD. |
| EPC vendor package review and acceptance standard | EPC review of submitted vendor documents | location TBD; method described in `DEL-039-06`. |

## Verification

| Requirement | Verification approach |
|---|---|
| R-039-05-01 | Confirm responsibility assignment in `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv`. |
| R-039-05-02 | Inspect deliverable folder for a vendor document register artifact; confirm it lists vendor documents to be submitted. |
| R-039-05-03 | Inspect submittals against register entries; confirm each register entry has a corresponding submittal status. |
| R-039-05-04 | Confirm source-derived vendor document rows are carried as artifacts under `ARTIFACT_REGISTER.csv` rather than minted as deliverables. |
| R-039-05-05 | Inspect turnover record set for the package; confirm coverage of certified data, tests, and handoff documentation. |
| R-039-05-06 | Confirm each of the twelve applicable interfaces has package-side vendor documentation referenced from the register, or explicit TBD. |
| R-039-05-07 | EPC Integrator review judgment on alignment with the general package-deliverables expectation. |
| R-039-05-08 | Cross-check against DBM Electrical Buildings paragraphs that vendor documentation covers the prefab/HVAC/bottom-entry/piling/wiring/door/GFI features for the actually-installed subset. |
| R-039-05-09, R-039-05-10, R-039-05-11 | Cannot be verified until governing source is identified and resolved. |

## Documentation

Required artifacts for this deliverable, per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`:

- Vendor document register (artifact within this deliverable folder).
- Vendor document submittals (artifacts within this deliverable folder).
- Source vendor document table rows carried as artifacts where available.
- Turnover records for the package.

Cross-deliverable artifact pointers (from `ARTIFACT_REGISTER.csv`):

- `ART-A64A8A25DC` — TBD vendor document register evidence (this deliverable).
- `ART-3910447327` — Vendor document review and comment log (`DEL-039-06`).
- `ART-AA4BFB86C9` — Vendor package acceptance and turnover checklist (`DEL-039-06`).
- `ART-0156F0196A` — Factory/shop test and inspection evidence (`DEL-039-06`).
