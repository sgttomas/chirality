# Specification: DEL-024-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator-led review and acceptance deliverable for `PKG-024`, the MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. The deliverable produces the EPC review, integration acceptance, and handoff-readiness evidence for the Package Vendor's vendor-engineered equipment package (`DEL-024-04`) and vendor document turnover package (`DEL-024-05`), measured against the EPC Scope of Work (`DEL-024-01`), EPC Package Datasheet (`DEL-024-02`), and EPC Construction Work Package (`DEL-024-03`).

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor engineering/design content production, vendor documentation production, and equipment fabrication are excluded; those are scope under `DEL-024-04` and `DEL-024-05`.
- Detailed numerical acceptance thresholds for VFD performance, harmonic limits, efficiency, output filter sizing, cooling, and protection coordination are `TBD` because the EPC Package Datasheet (`DEL-024-02`) and `26020-Package_Requirements.docx` PKG-024 slice were not consumed in this run.
- Modifications to vendor-owned design.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-024-06-001 | The deliverable shall identify `PKG-024`, workbook row 26, WBS 01, CoA tracking number 26020-01-30-015, discipline Electrical, and package name "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 26; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-024-06-002 | The deliverable shall preserve the accepted responsibility split: EPC Integrator authors the review log, acceptance checklist, and acceptance decision; Package Vendor supplies vendor documentation and test/inspection evidence. Source: `PACKAGE_REGISTER.csv` row `PKG-024`; `_CONTEXT.md` ResponsibleParty. | Responsibility statement review against Gate 7 package register. |
| REQ-024-06-003 | The deliverable shall produce a vendor document review and comment log covering every submittal in `DEL-024-05`, with disposition (accept / accept-with-comments / reject / TBD) and citation to the EPC SOW, EPC Package Datasheet, EPC CWP, or accepted Gate 7 register that supports the disposition. Source: `ARTIFACT_REGISTER.csv` row `ART-803E267B52`. | Sample log entries against vendor submittals and cited basis. |
| REQ-024-06-004 | The deliverable shall produce a package acceptance and turnover checklist that asserts acceptance against the EPC SOW, EPC Package Datasheet, EPC CWP, and each interface fact listed for `PKG-024` in `INTERFACE_REGISTER.csv`. Source: `ARTIFACT_REGISTER.csv` row `ART-6136727237`; `INTERFACE_REGISTER.csv` rows for `PKG-024`. | Checklist coverage against interface register and EPC anchor deliverables. |
| REQ-024-06-005 | The deliverable shall capture factory/shop test and inspection evidence supplied by the Package Vendor and shall record EPC review status and disposition for each item. Source: `ARTIFACT_REGISTER.csv` row `ART-A9C4AF8FF5`. | Test/inspection evidence review against vendor submittals. |
| REQ-024-06-006 | The deliverable shall confirm that the MV VFD package integrates with the 4.16 kV electrical system in a manner consistent with the DBM electrical basis. Where DBM marks VFD/soft-starter requirements for 4.16 kV motors as `TBD`, the EPC review shall require the issued EPC Package Datasheet to resolve the requirement before acceptance is closed. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph and electrical TBD list. | Review item tied to issued EPC Package Datasheet. |
| REQ-024-06-007 | Where the VFD feeds a motor located in a Zone 2 area, the EPC review shall verify that the motor is marked accordingly and is supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD-fed motor paragraph. | Review item against area-classification drawing and motor nameplate evidence. |
| REQ-024-06-008 | Where low-voltage power cable in the EPC integration scope is fed from VFDs in this package, the EPC review shall verify it is specified as copper TECK cable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical cable type table. | Review item against cable specification and CWP cable schedule. |
| REQ-024-06-009 | The deliverable shall confirm the housing/installation basis for the MV VFD package (electrical building or otherwise) against the EPC Package Datasheet and EPC Construction Work Package before acceptance closure. The DBM allows electrical buildings to house medium-voltage VFDs but does not assign a specific location. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph. | Review item against EPC CWP installation location and EPC Package Datasheet. |
| REQ-024-06-010 | The deliverable shall surface every unresolved acceptance item as `TBD` or as a `NEEDS_HUMAN_RULING` item rather than asserting acceptance without source-supported basis. Source: skill source-grounding contract; `_REFERENCES.md` Missing/Deferred References. | Open-item review before acceptance closure. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation, grounding, conduit, and cable basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Area classification standards | Applicable to motor and equipment marking and temperature-code selection where the VFD feeds motors in Zone 2 areas. | Applicable; package-specific area assignment TBD. |
| Project electrical specifications | Referenced by DBM for voltage, MCC, grounding, cable, and raceway basis. | Applicable; document location TBD. |
| EPC Scope of Work for `PKG-024` (`DEL-024-01`) | Acceptance basis: package scope, tagged equipment, package function, source basis, boundaries, and integration narrative. | Authoritative for EPC review against SOW; content not consumed in this run. |
| EPC Package Datasheet for `PKG-024` (`DEL-024-02`) | Acceptance basis: package technical data, interface requirements matrix, equipment and design criteria. | Authoritative for EPC review against datasheet; content not consumed in this run. |
| EPC Construction Work Package for `PKG-024` (`DEL-024-03`) | Acceptance basis: installation, tie-in, workface plan, construction interface, and turnover checklist. | Authoritative for EPC review against CWP; content not consumed in this run. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare identity fields to workbook row 26 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface acceptance coverage | Compare acceptance checklist to `INTERFACE_REGISTER.csv` rows for `PKG-024`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports each have a checklist entry. |
| Anchor-deliverable coverage | Confirm the checklist references the EPC SOW (`DEL-024-01`), EPC Package Datasheet (`DEL-024-02`), and EPC CWP (`DEL-024-03`) as acceptance bases. | Each anchor is cited; missing anchors are recorded as `TBD`. |
| Vendor document review coverage | Confirm review log includes every submittal in `DEL-024-05`. | Coverage gap recorded as `TBD` until closed. |
| Test/inspection evidence | Confirm vendor-supplied factory/shop test and inspection evidence is captured and dispositioned. | Each evidence item has a disposition; missing items recorded as `TBD`. |
| Source fidelity | Check non-trivial acceptance items against cited source slices or anchor deliverables. | Unsupported items remain `TBD` or `NEEDS_HUMAN_RULING`. |
| Responsibility split | Compare review language to `PACKAGE_REGISTER.csv` row `PKG-024`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interface list, anchor deliverables, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts (per `ARTIFACT_REGISTER.csv` rows for `DEL-024-06` and `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review and comment log (`ART-803E267B52`).
- Vendor package acceptance and turnover checklist (`ART-6136727237`).
- Factory/shop test and inspection evidence (`ART-A9C4AF8FF5`).
- Turnover evidence collated from the above.

The deliverable shall cite the Gate 7 snapshot, workbook row 26, applicable Gate 7 registers (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `SCOPE_LEDGER.csv`), and the DBM electrical source slices used for VFD/MV electrical context.
