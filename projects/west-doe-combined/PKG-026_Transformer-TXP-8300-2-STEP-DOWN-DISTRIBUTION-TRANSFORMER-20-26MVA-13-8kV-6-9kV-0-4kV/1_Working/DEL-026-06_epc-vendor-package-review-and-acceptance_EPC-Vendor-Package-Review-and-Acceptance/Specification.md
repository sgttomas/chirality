# Specification: DEL-026-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator-led review and acceptance deliverable for `PKG-026`, the Transformer TXP-8300-2 step-down distribution transformer package (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV). The deliverable evidences that the vendor-engineered equipment package (`DEL-026-04`) and the vendor document/turnover package (`DEL-026-05`) have been reviewed and accepted against the EPC Scope of Work (`DEL-026-01`), Package Datasheet (`DEL-026-02`), and Construction Work Package (`DEL-026-03`).

The EPC Integrator owns review, integration acceptance, and handoff readiness; the Package Vendor provides supporting input (vendor documentation, test/inspection records, certifications). This deliverable does not author vendor design content; it authors the review and acceptance evidence.

Exclusions:

- Vendor detailed engineering, design calculations, drawings, fabrication records, and certifications themselves (owned by `DEL-026-04` / `DEL-026-05`).
- Construction installation and tie-in execution (owned by `DEL-026-03`).
- Authoring of the EPC Scope of Work or Package Datasheet (owned by `DEL-026-01` / `DEL-026-02`).
- Detailed transformer technical parameters (rating, impedance, vector group, BIL, cooling, grounding scheme) — these remain `TBD` because the accessible source set does not provide package-specific values for `PKG-026`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-026-06-001 | The acceptance package shall identify `PKG-026`, workbook row 28, WBS 02, CoA tracking number 26020-02-30-017, discipline Electrical, and package name "Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV." Source: `PACKAGE_REGISTER.csv`. | Identity review against Gate 7 registers. |
| REQ-026-06-002 | The acceptance package shall preserve the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and acceptance. Source: `PACKAGE_REGISTER.csv` row `PKG-026`; `DELIVERABLE_REGISTER.csv` row `DEL-026-06`. | Responsibility statement review against Gate 7 registers. |
| REQ-026-06-003 | The vendor document review log shall record each vendor submittal received under `DEL-026-05`, its review status (e.g., reviewed, comment, hold), comment disposition, and final acceptance status. Source: `ARTIFACT_REGISTER.csv` row `ART-AF00FF6B63` (Vendor document review and comment log). | Review log completeness check against `DEL-026-05` vendor document register. |
| REQ-026-06-004 | The acceptance and turnover checklist shall record acceptance of the vendor-engineered equipment package against the EPC Scope of Work (`DEL-026-01`), Package Datasheet (`DEL-026-02`), and Construction Work Package (`DEL-026-03`), and shall record turnover evidence for facility integration. Source: `ARTIFACT_REGISTER.csv` row `ART-28805E8681` (Vendor package acceptance and turnover checklist). | Checklist review against EPC anchor deliverables. |
| REQ-026-06-005 | The acceptance package shall include factory/shop test and inspection evidence for the transformer package. Detailed test list and acceptance criteria shall be drawn from the EPC Package Datasheet (`DEL-026-02`) and vendor design basis (`DEL-026-04`); package-specific test thresholds are `TBD` until those documents resolve them. Source: `ARTIFACT_REGISTER.csv` row `ART-063BACA4E7` (Factory/shop test and inspection evidence). | Test/inspection evidence review against `DEL-026-02` and `DEL-026-04`. |
| REQ-026-06-006 | The acceptance package shall confirm that all applicable interface facts for `PKG-026` are addressed by vendor design and EPC integration: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv` rows for `PKG-026`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-026-06-007 | The acceptance package shall mark unsupported package-specific transformer parameters (rating allocation, impedance, vector group, taps, cooling, BIL, grounding scheme, ambient/environmental envelope, hazardous area classification) as `TBD` rather than asserting values not supported by accepted sources. Source: `_REFERENCES.md`; source-fidelity rule. | Source-fidelity review of acceptance evidence. |
| REQ-026-06-008 | The acceptance package shall record human rulings (HRR items) for unresolved conflicts, ambiguous mappings, or unsupported claims, and shall not silently reconcile them. Source: this skill's epistemic controls; `four-documents` SKILL. | HRR list review at acceptance gate. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Gate 7 PROJECT_DECOMP snapshot (`GATE-07_Final_Published_2026-05-24`) | Accepted decomposition truth for package identity, deliverable basis, artifacts, interfaces, and responsibility split. | Authoritative upstream snapshot. |
| Canadian Electrical Code (CEC) | Electrical grounding, conduit/raceway, and installation basis referenced by DBM electrical sections. | Applicable; clause locations TBD. |
| Project electrical specifications | Voltage classes, grounding, cabling, raceway, and protection basis referenced by DBM electrical sections. | Applicable; document location TBD. |
| Applicable transformer standards (e.g., IEEE C57 / IEC 60076 series, CSA equivalents) | Governing transformer design, factory testing, and acceptance basis. | ASSUMPTION — likely applicable; specific clauses and acceptance values TBD until vendor design basis or Package Datasheet resolves them. |
| Area classification standards | Applicable to electrical equipment installation classification where hazardous/non-hazardous areas are defined. | Applicable; package-specific classification TBD. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare acceptance package identity to `PACKAGE_REGISTER.csv` row `PKG-026` and `DELIVERABLE_REGISTER.csv` row `DEL-026-06`. | All fields match accepted source spelling and IDs. |
| Responsibility split | Compare responsibility language in acceptance package to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Vendor document review completeness | Cross-check review log entries to `DEL-026-05` vendor document register. | Every register entry has a corresponding review-log row with disposition. |
| Acceptance against EPC anchors | Cross-check acceptance checklist line items to requirements in `DEL-026-01`, `DEL-026-02`, and `DEL-026-03`. | Every applicable EPC requirement has an acceptance entry (or an explicit deferral with rationale). |
| Test/inspection evidence sufficiency | Compare collected FAT/inspection evidence to test list defined by `DEL-026-02` and `DEL-026-04`. | Each required test has a result and an acceptance disposition; gaps are `TBD` with traceable cause. |
| Interface coverage | Confirm acceptance evidence addresses each `PKG-026` interface row in `INTERFACE_REGISTER.csv`. | All seven applicable interface types are addressed or explicitly marked `TBD` with traceable cause. |
| Source fidelity | Confirm no acceptance claim asserts package-specific values absent from accessible sources or upstream deliverables. | Unsupported values are marked `TBD`; inferences labeled `ASSUMPTION`. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, scope split, interface set, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts (per `ARTIFACT_REGISTER.csv` for `DEL-026-06`):

- Vendor document review and comment log (`ART-AF00FF6B63`).
- Vendor package acceptance and turnover checklist (`ART-28805E8681`).
- Factory/shop test and inspection evidence (`ART-063BACA4E7`).
- HRR / open-item list for unresolved acceptance conditions.

The deliverable shall cite the Gate 7 snapshot, workbook row 28, the applicable Gate 7 registers, and the upstream EPC anchor deliverables (`DEL-026-01`, `DEL-026-02`, `DEL-026-03`) plus the vendor packages (`DEL-026-04`, `DEL-026-05`).
