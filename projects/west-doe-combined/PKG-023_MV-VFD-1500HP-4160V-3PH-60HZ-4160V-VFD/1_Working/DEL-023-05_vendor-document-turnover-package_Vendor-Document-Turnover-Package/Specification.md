# Specification: DEL-023-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-023`, the MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package, with EPC Integrator interface/integration review. The deliverable is a Gate 5 Package Vendor deliverable that consolidates the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for the package.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration and reviews vendor documentation for integration sufficiency.

Exclusions:

- Vendor detailed equipment design content itself (drive engineering, control logic, drawings) is the subject of `DEL-023-04_vendor-engineered-equipment-package`; this turnover deliverable carries the register, transmittals, and turnover records that point to that content.
- EPC vendor package review/acceptance evidence is the subject of `DEL-023-06_epc-vendor-package-review-and-acceptance` and is not duplicated here.
- Package-specific vendor document register content, submittal numbering plan, document control conventions, and turnover record list are `TBD` because the accessible source set does not provide a package-specific vendor-document basis (`ARTIFACT_REGISTER.csv` row `ART-950E899C01`).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-023-05-001 | The Vendor Document Turnover Package shall identify `PKG-023`, workbook row 25, WBS 01, CoA tracking number 26020-01-30-014, discipline Electrical, and package name "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 25; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-023-05-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns vendor documentation; EPC Integrator performs interface/integration review of vendor documentation. Source: `PACKAGE_REGISTER.csv` row `PKG-023`; `_CONTEXT.md`. | Responsibility statement review against Gate 7 package register. |
| REQ-023-05-003 | The deliverable shall contain a vendor document register (index) covering, at minimum: vendor document submittals, source-required vendor documentation, and turnover records. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-023-05_vendor-document-turnover-package`. The detailed content of the register is `TBD` per `ARTIFACT_REGISTER.csv` row `ART-950E899C01`. | Register existence and structure review. |
| REQ-023-05-004 | The vendor document register shall cover evidence for each applicable interface fact: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 25; `INTERFACE_REGISTER.csv` rows for `PKG-023`. | Interface coverage check against `INTERFACE_REGISTER.csv` rows for `PKG-023`. |
| REQ-023-05-005 | The deliverable shall preserve unsupported package-specific vendor-document requirements as `TBD` rather than inventing register contents, submittal numbering, or turnover record types. Source: `ARTIFACT_REGISTER.csv` row `ART-950E899C01`; `_REFERENCES.md`. | Gap review against `TBD` register. |
| REQ-023-05-006 | The deliverable shall provide a submittal transmittal mechanism (transmittal log) that records vendor submittals with revision identifiers, dates, and EPC review disposition pointers. Source-supported convention; detailed numbering scheme and document-control convention are `TBD`. | Transmittal log review. |
| REQ-023-05-007 | The deliverable shall provide a turnover record set listing the turnover artifacts required to close out the package. The detailed list of turnover artifacts (e.g., FAT/SAT, mill certs, calibration, drive tuning, IOM, spares list, as-builts) is `TBD` pending source confirmation. | Turnover record review. |
| REQ-023-05-008 | Where vendor documentation reflects MV VFD voltage-service or plant-PLC communication conventions, it shall align with the DBM-supported 4.16 kV medium-voltage service basis and the DBM plant-PLC Ethernet integration convention to the extent applicable to MV VFDs (ASSUMPTION: MV VFD Ethernet integration convention is to be confirmed). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table; 6.9 kV / 4.16 kV MCC paragraphs. | DBM-alignment check on vendor documentation for voltage and PLC integration. |
| REQ-023-05-009 | Where the package or VFD-fed motors fall in a Zone 2 (or other classified) area, the vendor documentation shall include area-classification and temperature-code marking evidence consistent with DBM. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD/area-classification paragraph. Area classification of PKG-023 is `TBD`. | Area-classification marking review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation, grounding/bonding, and conductor sizing basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to VFD-fed motors and equipment marking where hazardous-area boundaries are defined. | Applicable; package-area classification TBD. |
| Project document control / submittal convention | Governs vendor submittal numbering, transmittal handling, and revision control. | Applicable; specific procedure TBD (no accessible project document-control procedure in source set). |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity to workbook row 25 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Register completeness | Compare the vendor document register to the artifact register row for this deliverable. | Register exists and covers register/submittals/turnover scope; gaps are explicit `TBD`. |
| Interface coverage | Compare register entries to `INTERFACE_REGISTER.csv` rows for `PKG-023`. | All six interface facts have evidence pointers (or explicit `TBD`). |
| Source fidelity | Check non-trivial vendor-document content claims against cited source slices. | Unsupported items are marked `TBD` or `ASSUMPTION`, not invented. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `_CONTEXT.md`. | Vendor documentation ownership and EPC review role are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (per `ARTIFACT_REGISTER.csv` row `ART-950E899C01`; content currently `TBD`).
- Vendor document submittals (transmittal log and submitted documents).
- Source-required vendor documentation (as identified by the vendor document register).
- Turnover records.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 25, applicable Gate 7 registers, and the DBM electrical source slices used for MV VFD service basis and area-classification context.
