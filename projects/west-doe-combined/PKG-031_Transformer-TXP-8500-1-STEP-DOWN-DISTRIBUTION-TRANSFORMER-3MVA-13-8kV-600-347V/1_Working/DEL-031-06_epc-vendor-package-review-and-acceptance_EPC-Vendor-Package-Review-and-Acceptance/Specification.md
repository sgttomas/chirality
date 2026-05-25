# Specification: DEL-031-06_epc-vendor-package-review-and-acceptance

## Scope

This specification governs the EPC Integrator-authored vendor package review and acceptance deliverable for `PKG-031`, the Transformer TXP-8500-1 step-down distribution transformer (3 MVA, 13.8 kV / 600 V / 347 V). The deliverable provides the review log, package acceptance checklist, test/inspection evidence, and turnover evidence required to accept the Package Vendor's engineered equipment package into the facility scope, against the EPC Scope of Work (`DEL-031-01`), Package Datasheet (`DEL-031-02`), and Construction Work Package (`DEL-031-03`).

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (carried under `DEL-031-04` and `DEL-031-05`). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and the certified equipment dossier are not authored under this deliverable; they are received from the vendor and reviewed/accepted here.
- Vendor document register content itself is authored under `DEL-031-05`; this deliverable captures the EPC review/comment evidence and acceptance disposition.
- Transformer-specific ratings, impedance, BIL, cooling class, tap-changer arrangement, oil/dry construction, and certified test parameters are `TBD` at acceptance-criteria authoring time and shall be locked through the Package Datasheet and vendor data prior to acceptance.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-031-06-001 | The deliverable shall identify `DEL-031-06`, `PKG-031`, workbook row 33, WBS 01, CoA tracking number 26020-01-30-022, discipline Electrical, equipment tag TXP-8500-1, and package name "Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V." Source: Workbook Packages row 33; `PACKAGE_REGISTER.csv`. | Identity review against Gate 7 registers and workbook row. |
| REQ-031-06-002 | The acceptance record shall preserve the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-031`. | Responsibility statement review against Gate 7 package register. |
| REQ-031-06-003 | The acceptance checklist shall require review and disposition for each of the seven `PKG-031` interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv` rows for `PKG-031`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-031-06-004 | The acceptance evidence shall confirm vendor package alignment with the facility electrical design basis: 13.8 kV medium-voltage backbone primary, 600 V three-phase three-wire low-voltage secondary, and 5 A continuous high-resistance grounding for the 600 V secondary system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table and grounding paragraphs. | Source citation review; deviations recorded as acceptance comments and conditions. |
| REQ-031-06-005 | The acceptance evidence shall confirm transformer foundation/support and spacing arrangements against facility design basis (precast concrete bearing foundations and/or steel transformer bases; CEC spacing for oil-filled transformers if applicable). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs. | Foundation/spacing review against vendor general arrangement and EPC civil/structural package. |
| REQ-031-06-006 | The acceptance evidence shall include a vendor document review log (`ART-8D69884269`) listing each vendor submittal, review status, EPC comments, and comment resolution. Source: `ARTIFACT_REGISTER.csv`. | Log completeness review prior to acceptance. |
| REQ-031-06-007 | The acceptance evidence shall include a single-record package acceptance and turnover checklist (`ART-E97EECD60B`) with pass/conditional/fail markings for each interface and for the vendor document register. Source: `ARTIFACT_REGISTER.csv`. | Checklist completeness review against interface and document scope. |
| REQ-031-06-008 | The acceptance evidence shall include factory/shop test and inspection evidence (`ART-0D8191743E`), including (at minimum) factory acceptance and routine test records appropriate to the certified transformer construction. Source: `ARTIFACT_REGISTER.csv`. ASSUMPTION: detailed FAT scope is vendor-specification driven and is `TBD` pending Package Datasheet/ITP. | Cross-check FAT/routine test record list against Package Datasheet and vendor ITP. |
| REQ-031-06-009 | Acceptance shall not be granted while open interface non-conformances, missing vendor documents, or outstanding test records remain. Conditional acceptance shall be explicit, time-bounded, and tied to remediation actions. | Acceptance disposition review; conditional acceptances tracked to closure. |
| REQ-031-06-010 | Acceptance evidence shall cite the Gate 7 snapshot used as the decomposition authority and the workbook row used as the source authority. | Provenance review on the acceptance record. |
| REQ-031-06-011 | Source gaps for transformer-specific data (rating margins, impedance, BIL, cooling class, tap-changer, oil/dry, sound level, installation location) shall be carried as `TBD` and resolved through the Package Datasheet and accepted vendor data before acceptance is granted. | Open-item review at acceptance. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding, conduit, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Facility electrical design basis (DBM-Deepcut) | Voltage architecture, grounding system, transformer support, electrical buildings, cable tray/conduit. | Authoritative source for facility-level acceptance criteria. |
| Project electrical specifications | Vendor specifications and master engineering specs governing transformer construction and FAT scope. | Applicable; document location `TBD`. |
| Vendor equipment standards (e.g., CAN/CSA C88, CSA C802, IEEE C57 series) | Standards typically governing distribution transformer ratings, losses, and test methods. ASSUMPTION: applicable standard set is to be confirmed by the vendor specification and Package Datasheet. | Applicability `TBD` pending Package Datasheet. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity to workbook row 33 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface coverage | Compare acceptance checklist to `INTERFACE_REGISTER.csv` rows for `PKG-031`. | All seven interface facts addressed with dispositions. |
| Document register completeness | Compare vendor document review log against the `DEL-031-05` vendor document register. | All listed vendor documents have a review status and comment resolution. |
| Test/inspection evidence | Compare received test records against Package Datasheet test requirements / vendor ITP. | All required tests present; deviations either accepted or corrected. |
| Source fidelity | Each acceptance criterion citing source content traces to the cited slice. | No invented criteria; `TBD` preserved where source is silent. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interface set, and `TBD` set. | No unresolved internal inconsistency. |
| Acceptance disposition | Single acceptance/turnover checklist signed by authorized EPC Integrator reviewer; conditional acceptances time-bounded. | K-AUTH-1: only humans author binding approval records. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document review log (`ART-8D69884269`).
- Vendor package acceptance and turnover checklist (`ART-E97EECD60B`).
- Factory/shop test and inspection evidence (`ART-0D8191743E`).
- Turnover evidence package (received from `DEL-031-05` and incorporated here).
- Open-item / conditional-acceptance tracker (where conditional acceptance is granted).

The deliverable shall cite the Gate 7 snapshot, workbook row 33, applicable Gate 7 registers, and the DBM electrical source slices used for facility-level acceptance criteria.
