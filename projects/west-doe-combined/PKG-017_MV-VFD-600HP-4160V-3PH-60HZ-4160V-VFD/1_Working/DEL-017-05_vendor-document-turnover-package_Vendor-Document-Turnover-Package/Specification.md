# Specification — DEL-017-05 Vendor Document Turnover Package (PKG-017)

## Scope

### In scope
- The Package Vendor's controlled document register for the PKG-017 MV VFD (600 HP, 4160 V, 3-phase, 60 Hz) equipment package.
- The full set of source-required vendor document submittals associated with the register.
- Turnover records (transmittals, acceptance evidence, MDR/Vendor Data Book compilation) sufficient to support EPC Integrator review and acceptance under `DEL-017-06`.
- EPC Integrator review of vendor documentation as an interface/integration activity.

Source: Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-017-05` (Scope and Responsible Party fields); `_CONTEXT.md`.

### Out of scope
- Authoring of the vendor engineered equipment package itself (covered by `DEL-017-04`).
- Final EPC integration acceptance decisions and acceptance evidence aggregation (covered by `DEL-017-06`).
- Treating individual source document rows as separate deliverables — they remain artifacts/evidence within this package (Gate 7 `DELIVERABLE_REGISTER.csv` Notes).
- Documentation for other facility scopes outside PKG-017.

## Requirements

| ID | Requirement | Source | Verification (see § Verification) |
|---|---|---|---|
| REQ-VDT-01 | A controlled Vendor Document Register shall be issued for PKG-017, listing every vendor document by ID, title, revision, submittal status, submittal date, and EPC review status. | DBM `3-25_Comp_and_Liquids_DBM.md` line 617 ("Package deliverables shall include … vendor document registers"); Gate 7 anticipated artifact | V-1 |
| REQ-VDT-02 | The register shall include all source-required vendor documents for the MV VFD package (data sheets, GA/outline drawings, schematics, BOM, test reports, IOM/O&M manuals, spares, MDR), with the specific list aligned to the active package requirements source. | ASSUMPTION (no PKG-017-specific document-list section located in `26020-Package_Requirements.docx`; location TBD) | V-2 |
| REQ-VDT-03 | Each register entry shall identify the deliverable interface(s) it informs, drawn from the PKG-017 interface set: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Gate 7 `INTERFACE_REGISTER.csv` for PKG-017; `PACKAGE_REGISTER.csv` | V-3 |
| REQ-VDT-04 | Vendor document submittals shall be delivered against the register on a scheduled basis (e.g., for-information, for-approval, approved-for-construction, as-built, final MDR), with status tracked in the register. | ASSUMPTION (typical industry phasing; not enumerated in source for PKG-017) | V-1 |
| REQ-VDT-05 | Turnover records shall include the final transmittal package, document acceptance log, completed Manufacturing Data Record (MDR) / Vendor Data Book, and handover sign-off. | Gate 7 anticipated artifacts ("turnover records"); ASSUMPTION on MDR/VDB naming | V-4 |
| REQ-VDT-06 | The EPC Integrator shall perform interface/integration review of vendor documentation; vendor shall respond to EPC review comments and re-issue affected documents. | Gate 7 `DELIVERABLE_REGISTER.csv` Responsible Party ("Package Vendor … with EPC Integrator interface/integration review") | V-5 |
| REQ-VDT-07 | Individual source document rows shall be carried as artifacts/evidence inside this package, not as separate decomposition deliverables. | Gate 7 `DELIVERABLE_REGISTER.csv` Notes | V-1 |
| REQ-VDT-08 | Documentation of cold-service ratings shall reflect the site basis of -40 °C minimum ambient where applicable to the VFD package. | DBM `3-25_Comp_and_Liquids_DBM.md` line 145 | V-2 |
| REQ-VDT-09 | The register and turnover package shall be in a form acceptable to `DEL-017-06` (EPC Vendor Package Review and Acceptance) and traceable to `DEL-017-01` (Scope of Work) and `DEL-017-02` (Package Datasheet). | Gate 7 `DELIVERABLE_REGISTER.csv` (ASSUMPTION on dependency edges — declared dependencies are empty in `_DEPENDENCIES.md`) | V-5 |

## Standards

| Standard / Document | Application | Location |
|---|---|---|
| Workbook Packages row 19 | Package identity and ownership basis for PKG-017 | Gate 7 `PACKAGE_REGISTER.csv` |
| DBM `3-25_Comp_and_Liquids_DBM.md` | Site basis (-40 °C); vendor document register requirement | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 145, 617) |
| `26020-Package_Requirements.docx` | Package requirements source intended to enumerate per-package vendor deliverable lists | `_Sources/26020-Package_Requirements.docx`; PKG-017 section location TBD |
| Vendor's own document control procedure | Governs revision, transmittal, and acceptance mechanics | location TBD (vendor-supplied at execution) |
| Project document control / numbering standard | Governs document IDs, transmittal forms, MDR structure | location TBD (project DCC standard not in accessible sources) |

## Verification

| ID | Verification approach | Covers |
|---|---|---|
| V-1 | Register completeness audit: every required document class is listed; every listed entry has status, revision, dates, and reviewer. | REQ-VDT-01, REQ-VDT-04, REQ-VDT-07 |
| V-2 | Source-required document presence check: cross-check the register against the active package requirements source list (when located) and against actual vendor data needed to document the 600 HP / 4160 V VFD. | REQ-VDT-02, REQ-VDT-08 |
| V-3 | Interface coverage check: each PKG-017 interface line from the Gate 7 `INTERFACE_REGISTER.csv` is informed by at least one register entry. | REQ-VDT-03 |
| V-4 | Turnover content check: MDR/VDB present and complete; acceptance log closed; handover sign-off captured. | REQ-VDT-05 |
| V-5 | EPC review/acceptance handshake: comment responses closed; package accepted by `DEL-017-06`. | REQ-VDT-06, REQ-VDT-09 |

## Documentation

Required artifacts produced by this deliverable (Gate 7 anticipated artifacts):

- Vendor Document Register (controlled index)
- Vendor document submittals (the indexed documents themselves)
- Source vendor document table rows carried as evidence/artifacts
- Turnover records (transmittals, acceptance log, MDR/VDB, handover sign-off)
