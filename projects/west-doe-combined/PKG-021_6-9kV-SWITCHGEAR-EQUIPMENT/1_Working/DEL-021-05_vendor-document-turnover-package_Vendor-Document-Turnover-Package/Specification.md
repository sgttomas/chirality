# Specification: DEL-021-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-021`, the 6.9kV SWITCHGEAR EQUIPMENT package. The deliverable provides the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records used as the documentary basis for EPC Integrator review (`DEL-021-06`) and for facility integration of the 6.9 kV switchgear into the 6.9 kV Inlet/Sales Compressor Electrical Building.

The package is a vendor-owned Electrical package under WBS 01, CoA tracking number 26020-01-30-012, workbook row 23. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Detailed vendor design calculations and certified drawings are produced by the Package Vendor; this specification does not redefine vendor internal design content.
- EPC review and acceptance evidence (vendor document review and comment log, vendor package acceptance and turnover checklist, factory/shop test and inspection evidence as EPC accepts it) belongs to `DEL-021-06_epc-vendor-package-review-and-acceptance` and is not duplicated here.
- A project-wide vendor document register format, numbering convention, and transmittal protocol are not defined by the accessible source set and remain `TBD`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-021-05-001 | The deliverable shall identify `PKG-021`, workbook row 23, WBS 01, CoA tracking number 26020-01-30-012, discipline Electrical, and package name "6.9kV SWITCHGEAR EQUIPMENT." Source: Workbook Packages row 23; `PACKAGE_REGISTER.csv`. | Identification review against workbook row 23 and Gate 7 registers. |
| REQ-021-05-002 | The deliverable shall declare responsibility as Package Vendor (vendor documentation) with EPC Integrator interface/integration review, consistent with the accepted package responsibility model. Source: `PACKAGE_REGISTER.csv` row `PKG-021`; `DELIVERABLE_REGISTER.csv`. | Responsibility statement review against Gate 7 registers. |
| REQ-021-05-003 | The Package Vendor shall produce a vendor document register that lists every vendor document associated with `PKG-021`, including document number, title, revision, status, submittal stage, and intended use. Source: `ARTIFACT_REGISTER.csv` `ART-FA39AD509D` (TBD register evidence); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical-packages paragraph (analogous expectation that package deliverables include vendor document registers). | Register completeness review against actual submittals and Gate 7 expectation; gap items recorded as `TBD`. |
| REQ-021-05-004 | The vendor documentation set shall cover each applicable interface fact for `PKG-021`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 23; `INTERFACE_REGISTER.csv` rows for `PKG-021`. | Interface coverage check against `INTERFACE_REGISTER.csv` rows. |
| REQ-021-05-005 | The vendor documentation set shall reflect the medium-voltage service basis of 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded, supporting facility inverter-drive motors rated 5,500 hp and above. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services row. | Documentation review against DBM electrical service basis. |
| REQ-021-05-006 | The vendor documentation set shall reflect the facility neutral grounding scheme as it applies at the switchgear boundary, including the project basis that each 6.9 kV transformer is grounded using a 100 A, 10 s neutral grounding resistor operating as a tripping system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraphs. | Source-fidelity review; package-specific protection coordination data captured by vendor or marked `TBD`. |
| REQ-021-05-007 | The vendor documentation set shall provide information sufficient for installation in the 6.9 kV Inlet/Sales Compressor Electrical Building, including weights, anchor patterns, clearances for racking/withdrawal, cable entry, and grounding terminations required by the EPC Integrator. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and "820-1 6.9kV Inlet / Sales Compressor Electrical Building" entry. | Integration data review by EPC. |
| REQ-021-05-008 | The vendor documentation set shall provide test and inspection records consistent with `ART-E523401B0C` (factory/shop test and inspection evidence). Detailed test requirements are `TBD` where source-specific requirements are not yet available; the vendor shall propose and the EPC Integrator shall accept. Source: `ARTIFACT_REGISTER.csv` `ART-E523401B0C`. | Test record completeness review. |
| REQ-021-05-009 | The turnover package shall preserve traceability to the EPC vendor document review and comment log (`ART-5D5CAC1D6D`) and to the vendor package acceptance and turnover checklist (`ART-4B01C09131`) produced by `DEL-021-06`. Source: `ARTIFACT_REGISTER.csv` rows under `DEL-021-06`. | Cross-deliverable traceability review. |
| REQ-021-05-010 | Where detailed vendor-document requirements are not present in current source material (per `ART-FA39AD509D` gap evidence), the Package Vendor shall propose the document list and the EPC Integrator shall confirm or amend it; unresolved items shall remain `TBD` rather than be silently assumed. Source: `ARTIFACT_REGISTER.csv` `ART-FA39AD509D`. | TBD/open-item review before turnover. |
| REQ-021-05-011 | The deliverable shall record support of objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, and `OBJ-010` per the objective-deliverable map. Source: `OBJECTIVE_DELIVERABLE_MAP.csv`. | Objective mapping check. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation, grounding, and bonding basis referenced by DBM electrical section; vendor documentation shall be consistent with CEC where it applies at the package battery limit. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, switchgear, grounding, cable, and raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment installed in the 6.9 kV electrical building and classified areas. | Applicable; classification confirmation TBD. |
| Project-wide vendor document register / transmittal standard | Format, numbering, and transmittal protocol governing vendor document register and submittals. | `TBD`; no source-confirmed project-wide standard identified in this run. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity fields to workbook row 23 and Gate 7 registers. | Identity matches accepted source spelling and IDs. |
| Interface coverage | Compare vendor documentation set to `INTERFACE_REGISTER.csv` rows for `PKG-021`. | All six applicable interface facts are addressed in the documentation set. |
| Source fidelity | Check each non-trivial requirement statement against cited source slices (workbook, registers, DBM source). | Unsupported items remain `TBD`/`ASSUMPTION`. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor documentation authorship and EPC review/integration are not conflated. |
| Cross-deliverable traceability | Confirm explicit linkage to `DEL-021-06` review/acceptance artifacts. | Traceability map present in turnover record. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interface list, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (`ART-FA39AD509D`; detailed content TBD).
- Vendor document submittals (organized per the register).
- Source-required vendor documentation (drawings, datasheets, test reports, manuals, spare-parts lists, etc.) where required by source or by EPC integration need.
- Turnover records that support `DEL-021-06_epc-vendor-package-review-and-acceptance`.
- A `TBD`/open-item list naming each documentation gap explicitly, with the reason for the gap.

The deliverable shall cite the Gate 7 snapshot, workbook row 23, applicable Gate 7 registers, and DBM electrical source slices used for service basis, grounding, electrical-building installation context, and maintenance access.
