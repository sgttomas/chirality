# Specification: DEL-030-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-030`, the Transformer TXP-8200-1 STEP DOWN DISTRIBUTION TRANSFORMER (2.5 MVA, 13.8 kV / 600/347 V). The deliverable comprises the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-021). Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Individual source-vendor document rows are carried as artifacts/evidence, not as separate deliverables (per `_CONTEXT.md` Notes).
- Detailed vendor-document content (drawings, IOM manuals, factory test reports, name-plate data, certified test data, etc.) is `TBD` because the accessible source set does not enumerate package-specific vendor-document requirements for `PKG-030`.
- Vendor detailed design calculations and certified vendor drawings are produced under `DEL-030-04` (Vendor Engineered Equipment Package); this turnover deliverable consumes and packages them, it does not author them.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-030-05-001 | The Vendor Document Turnover Package shall identify `PKG-030`, workbook row 32, WBS 01, CoA tracking number 26020-01-30-021, discipline Electrical, and package name "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 32; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-030-05-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns vendor documentation, package engineering/design, and the physical equipment package; EPC Integrator owns facility integration, interfaces, and integration review of the vendor turnover. Source: `PACKAGE_REGISTER.csv` row `PKG-030`; `_CONTEXT.md`. | Responsibility statement review against Gate 7 package register. |
| REQ-030-05-003 | The deliverable shall include a Vendor Document Register that enumerates each vendor document expected for the package (document number, title, type, revision, submittal status, EPC review status). Source: `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` `ART-8B1CB2D887` (gap evidence). | Document register completeness check against vendor scope of supply once available. |
| REQ-030-05-004 | The deliverable shall capture vendor document submittals through completion, retaining each transmittal, revision, and EPC Integrator review disposition. Source: `_CONTEXT.md` Anticipated Artifacts. | Submittal log audit against transmittal evidence. |
| REQ-030-05-005 | The deliverable shall include the seven applicable interface evidences (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) within the vendor documentation set. Source: Workbook Packages row 32; `INTERFACE_REGISTER.csv` rows for `PKG-030`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-030`. |
| REQ-030-05-006 | The deliverable shall, where applicable to a mechanical/electrical package, include datasheets, utility load summaries, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access information, shipped-loose item lists, and the vendor document register. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 617. | Cross-check vendor turnover index against the DBM package-deliverable list. |
| REQ-030-05-007 | The deliverable shall include turnover records sufficient to demonstrate package acceptance, including factory and field test evidence, name-plate documentation, and as-built/red-line records, with content set `TBD` pending vendor scope confirmation. Source: `_CONTEXT.md` Anticipated Artifacts; source gap. | Turnover record audit prior to acceptance. |
| REQ-030-05-008 | The deliverable shall mark items as `TBD` where source material does not establish package-specific vendor-documentation requirements, rather than asserting invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search returned no `PKG-030` match. | Source-gap review before vendor handoff. |
| REQ-030-05-009 | The deliverable shall be reviewed by the EPC Integrator for interface/integration acceptance and shall feed `DEL-030-06_epc-vendor-package-review-and-acceptance` as upstream evidence. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-030-05` and `DEL-030-06`. | Review-handoff confirmation in `DEL-030-06` evidence set. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, bonding, and installation basis for the transformer package, referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Transformer industry standards (e.g., CSA / IEEE / IEC transformer standards governing distribution transformers) | Likely applicable to a 2.5 MVA 13.8 kV / 600/347 V step-down distribution transformer. | ASSUMPTION: likely applicable; no accessible source slice cites a specific standard for `PKG-030`; location TBD. |
| Area classification standards | Applicable to transformer enclosure and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Project document control / submittal standard | Governs vendor document register, transmittal numbering, revision control, and EPC review workflow. | ASSUMPTION: likely applicable; document location TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare turnover package identity fields to workbook row 32 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare turnover documentation matrix to `INTERFACE_REGISTER.csv` rows for `PKG-030`. | All seven applicable interfaces have vendor documentation evidence (or are `TBD` with reason). |
| Document register completeness | Confirm Vendor Document Register lists every vendor document the package scope of supply produces. | No required vendor document is missing from the register. |
| Submittal traceability | Confirm each register row has transmittal, revision, and EPC review status. | No submittal gap; review dispositions captured. |
| Turnover record completeness | Confirm turnover records evidence factory test, field acceptance, name-plate, and as-built information per applicable standard. | No turnover gap at acceptance; remaining gaps explicitly carried as `TBD` items. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `_CONTEXT.md`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor Document Register (per package scope of supply).
- Vendor document submittals (transmittals, revisions, EPC review dispositions).
- Source-required vendor documentation (drawings, datasheets, IOM, factory test data, name-plate documentation, as-applicable; content `TBD` until vendor scope confirmed).
- Turnover records (acceptance evidence, field test results, as-built/red-line documentation).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 32, applicable Gate 7 registers, and the DBM electrical/mechanical-package source slices used as basis.
