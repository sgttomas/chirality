# Specification: DEL-034-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator-led review and acceptance deliverable for `PKG-034`, the 600V ELECTRICAL BUILDING (820-2) vendor package. The deliverable establishes EPC review evidence, integration acceptance, and handoff-readiness records evaluated against the EPC Scope of Work (`DEL-034-01`), EPC Package Datasheet (`DEL-034-02`), and EPC Construction Work Package (`DEL-034-03`), with input from the Package Vendor through the Vendor Engineered Equipment Package (`DEL-034-04`) and Vendor Document Turnover Package (`DEL-034-05`).

The parent package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, vendor-internal QA records, and certified vendor drawings are inputs to the review but are not produced by this deliverable.
- Package-specific equipment counts, MCC bucket lists, switchgear lineups, transformer ratings, generator sizing, and building "820-2" physical location are `TBD`; the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-034-06-001 | The deliverable shall identify `PKG-034`, workbook row 36, WBS 02, CoA tracking number 26020-02-30-025, discipline Electrical, and package name "600V ELECTRICAL BUILDING (820-2)." Source: Workbook Packages row 36; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-034-06-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-034`. | Responsibility statement review against Gate 7 package register. |
| REQ-034-06-003 | The deliverable shall produce a vendor document review and comment log covering the vendor documentation set submitted under `DEL-034-05`. Source: `ARTIFACT_REGISTER.csv` `ART-F631454830`; `DELIVERABLE_REGISTER.csv` row `DEL-034-05`. | Review-log artifact check; cross-reference to vendor document register. |
| REQ-034-06-004 | The deliverable shall produce a vendor package acceptance and turnover checklist that confirms integration acceptance against the EPC Scope of Work, Package Datasheet, and Construction Work Package. Source: `ARTIFACT_REGISTER.csv` `ART-8E586DD59F`; `DELIVERABLE_REGISTER.csv` row `DEL-034-06`. | Checklist artifact check; traceability to the three EPC anchor deliverables. |
| REQ-034-06-005 | The deliverable shall capture factory/shop test and inspection evidence for the vendor package; detailed test requirements that are not source-supported shall remain `TBD`. Source: `ARTIFACT_REGISTER.csv` `ART-853E05D6CB`. | Test/inspection evidence completeness review; source-fidelity check. |
| REQ-034-06-006 | The deliverable shall confirm that all twelve applicable interface facts for `PKG-034` are addressed by the vendor package and acceptable to the EPC Integrator: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 36; `INTERFACE_REGISTER.csv` rows for `PKG-034`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-034-06-007 | The deliverable shall confirm that the vendor package's 600V service basis is consistent with the facility low-voltage service: 600 V, 3 phase, 3 wire, 60 Hz HRG. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, low-voltage service row. | Electrical interface review against the DBM service basis. |
| REQ-034-06-008 | The deliverable shall confirm that the vendor package's 600V MCC and standby power interface is consistent with the LV standby natural-gas generator + transfer-switch arrangement at the 600V MCC level. Generator sizing, transfer-switch configuration, emergency bus configuration, and load-shedding/critical-load list shall remain `TBD` unless resolved by the EPC Scope of Work, Package Datasheet, or vendor data. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and standby power paragraphs. | Standby power interface review. |
| REQ-034-06-009 | The deliverable shall confirm that vendor-supplied electrical building HVAC, ventilation, and building heater provisions are consistent with the facility electrical building HVAC basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building heater/HVAC paragraph. | Building HVAC interface review. |
| REQ-034-06-010 | The deliverable shall confirm grounding/bonding, cable tray, conduit, and maintenance-access provisions in the vendor package against the facility electrical basis (CEC sizing where applicable; cable tray and conduit routing shall not interfere with maintenance access). Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray and conduit paragraphs. | Electrical interface and maintenance-access review. |
| REQ-034-06-011 | The deliverable shall identify source gaps as `TBD` rather than invented values, including building "820-2" location reconciliation against the DBM building inventory (840-1/850-1/860-1) and any unsupported package-specific equipment data. Source: Workbook Packages row 36; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings inventory. | Source-gap and naming reconciliation review. |
| REQ-034-06-012 | The deliverable shall verify that handoff to construction is supported by the Construction Work Package (`DEL-034-03`) and that turnover evidence aligns with the construction interface and turnover checklist. Source: `DELIVERABLE_REGISTER.csv` row `DEL-034-03`; `ARTIFACT_REGISTER.csv` `ART-EEB94D0E0D`. | Turnover-readiness review against the Construction Work Package. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs facility grounding sizing and electrical installation basis referenced by the DBM electrical section. | Applicable; clause locations TBD. |
| Project electrical specifications | Voltage, MCC, grounding/bonding, cable, and raceway basis referenced by the DBM electrical section. | Applicable; specification document locations TBD. |
| Area classification standards | Govern electrical-building placement and equipment rating in classified areas. | Applicable; "820-2" specific classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| Gate 5 EPC anchor deliverables (`DEL-034-01`, `DEL-034-02`, `DEL-034-03`) | Acceptance baseline against which vendor package review is evaluated. | Required upstream acceptance basis. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity to workbook row 36 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Anchor traceability | Compare review/acceptance evidence to the EPC Scope of Work, Package Datasheet, and Construction Work Package. | Every acceptance line item traces to one or more upstream anchor requirements. |
| Vendor input completeness | Compare review log entries to the Vendor Document Turnover Package and Vendor Engineered Equipment Package outputs. | No required vendor deliverable category is unreviewed. |
| Interface completeness | Compare acceptance evidence to `INTERFACE_REGISTER.csv` rows for `PKG-034`. | All twelve interface facts are addressed. |
| Source fidelity | Check non-trivial requirements/claims against DBM source slices and Gate 7 registers. | Unsupported values remain `TBD`. |
| Responsibility split | Compare review/acceptance language to `PACKAGE_REGISTER.csv` row `PKG-034`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, anchor list, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Building naming reconciliation | Compare workbook "820-2" naming to DBM Deepcut building inventory. | A naming reconciliation note is recorded; mismatched mapping is treated as `NEEDS_HUMAN_RULING`, not silently asserted. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document review and comment log (`ART-F631454830`).
- Vendor package acceptance and turnover checklist (`ART-8E586DD59F`).
- Factory/shop test and inspection evidence (`ART-853E05D6CB`).
- Source-gap / `TBD` list (including building "820-2" naming reconciliation) for vendor or human resolution.
- Citations to Gate 7 snapshot, workbook row 36, applicable Gate 7 registers, DBM electrical source slices, and the EPC Scope of Work, Package Datasheet, and Construction Work Package upstream deliverables.
