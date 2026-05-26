# Specification: DEL-100-05 — Vendor Document Turnover Package

## Scope

This specification governs the **Vendor Document Turnover Package** for `PKG-100 Hydrogen Peroxide Sweetening Unit`. It defines the required content, structure, submittal/review lifecycle, and turnover artifacts for vendor-produced documentation associated with the package.

**In scope**
- Vendor document register for PKG-100.
- Vendor document submittals against that register.
- Source-required vendor documentation called out by `26020-Package_Requirements.docx` package heading 52 (location TBD; clause-level content not locally accessible).
- Turnover records (transmittals, acceptance evidence, final accepted document set).

**Out of scope**
- Engineered equipment design content itself (covered by `DEL-100-04 Vendor Engineered Equipment Package`).
- EPC review/acceptance workflow execution (covered by `DEL-100-06 EPC Vendor Package Review and Acceptance`).
- Package scope of work (`DEL-100-01`) and package datasheet (`DEL-100-02`).
- Construction work package execution (`DEL-100-03`).

## Requirements

| ID | Requirement | Source | Label |
|---|---|---|---|
| R-1 | The package vendor shall produce and maintain a Vendor Document Register that lists every document required for PKG-100. | DBM SEC-09 line 617 ("Package deliverables shall include … vendor document registers"); `_CONTEXT.md` | derived |
| R-2 | The Vendor Document Register shall, at minimum, identify for each row: document number, title, document type, revision, submittal date, review/comment status, turnover status, and the SOW item(s) it satisfies (`SOW-0107` … `SOW-0110`). | `_CONTEXT.md` SOW mapping | ASSUMPTION (industry-standard register columns; exact column set per `26020-Package_Requirements.docx` heading 52 is location TBD) |
| R-3 | The vendor shall submit each registered document for EPC Integrator review prior to turnover. | `_CONTEXT.md` ResponsibleParty | derived |
| R-4 | The EPC Integrator shall perform interface/integration review on each vendor submittal and return comments through the controlled document-control channel. | `_CONTEXT.md` ResponsibleParty | derived |
| R-5 | Documents required by `26020-Package_Requirements.docx` package heading 52 shall be produced and tracked through the register. | `_CONTEXT.md` Source Reference | location TBD — clause-level content not accessible |
| R-6 | A Turnover Records set shall be produced at package handover comprising: the final accepted document index, transmittal manifests, and acceptance evidence for each register row. | `_CONTEXT.md` Anticipated Artifacts | derived |
| R-7 | Where the source set contains a vendor document table, individual row entries shall be carried as evidence artifacts in the register, not as separate deliverables. | `_CONTEXT.md` Notes ("individual source document rows remain artifacts/evidence, not separate deliverables") | source-grounded |
| R-8 | The deliverable's documentation shall be consistent with the package design envelope (site ambient minimum -40 deg C; sour-water service; H2O2 oxidizer handling) where vendor documents address those attributes. | DBM SEC-02/SEC-09 line 145; DBM SEC-06 lines 214-216 | derived |
| R-9 | Vendor documents shall reflect the package interface scope identified in `PACKAGE_REGISTER.csv` row 63 (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). | `PACKAGE_REGISTER.csv` row 63 Interface_Types_Applicable | source-grounded |
| R-10 | Specific clause-level documentation requirements from `26020-Package_Requirements.docx` heading 52 — **TBD** (source not locally accessible as markdown). | — | TBD |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` heading 52 — Vendor Documentation requirements for the H2O2 sweetening package class | Defines the source-required vendor document set for this package | location TBD (docx not locally parseable) |
| `26020-Packages_Interfaces_4_export.xlsx` row 63 | Defines interface-level documentation for PKG-100 | location TBD (xlsx not locally parseable) |
| DBM "Mechanical Package Structure" (SEC-09) | Establishes the general package deliverable content set, including vendor document registers | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Hydrogen peroxide handling / safety standards (e.g., applicable WHMIS/TDG, manufacturer's safety data, applicable provincial OHS) | Vendor documents shall address safe handling, storage, and incompatibility for H2O2 service | TBD — not identified in accessible sources (ASSUMPTION: applicable) |
| Project Document Control procedures | Govern numbering, revision control, transmittal, and turnover | TBD — not identified in accessible sources |

## Verification

| Requirement | Verification Method | Verification Record |
|---|---|---|
| R-1, R-2 | Inspection of the Vendor Document Register against template/source-required columns | Register file (latest revision) |
| R-3, R-4 | Transmittal log audit showing each register row submitted and reviewed | Transmittal log; comment-resolution records |
| R-5 | Crosscheck register against `26020-Package_Requirements.docx` heading 52 list | Coverage matrix (heading-52 item → register row) — pending source access |
| R-6 | Turnover acceptance — every register row in `Accepted` status with attached evidence | Turnover manifest signed by EPC Integrator |
| R-7 | Inspection of register rows against source vendor document table rows | Source-row trace appendix |
| R-8 | Spot-check of vendor documents for design-envelope and H2O2-service consistency | Review comments / dispositions |
| R-9 | Coverage check: each applicable interface type in `PACKAGE_REGISTER.csv` row 63 is represented by at least one vendor document or explicit not-applicable disposition | Interface coverage matrix |
| R-10 | Re-verify once source slices accessible | TBD |

## Documentation

Required artifacts produced by this deliverable:

- Vendor Document Register (PKG-100) — tabular index, latest revision.
- Vendor Document Submittals — the set of vendor-issued documents tracked through the register.
- Source-row evidence appendix (where the source set contains a vendor document table).
- Turnover Records:
  - Final accepted document index,
  - Transmittal manifests,
  - Acceptance evidence per register row.
- Coverage matrix mapping register rows to `SOW-0107`…`SOW-0110` and (when accessible) `26020-Package_Requirements.docx` heading-52 items.
- Interface coverage matrix mapping register rows to the applicable interface types in `PACKAGE_REGISTER.csv` row 63.
