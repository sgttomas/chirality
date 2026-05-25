# Specification: DEL-024-04_vendor-engineered-equipment-package

## Scope

This specification governs the **Vendor Engineered Equipment Package** for `PKG-024` (MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD). It covers:

- Package Vendor engineering, design, fabrication / supply, and the physical equipment package itself.
- Vendor package design basis and datasheet set developed from the EPC Scope of Work (`DEL-024-01_scope-of-work`) and EPC Package Datasheet (`DEL-024-02_package-datasheet`).
- Interface obligations against the six declared `PKG-024` interface facts (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).

This specification does **not** cover:

- Facility-level integration, tie-ins, constructability, and procurement / construction coordination, which remain with the EPC Integrator under the package responsibility model and are addressed in `DEL-024-03_construction-work-package` and `DEL-024-06_epc-vendor-package-review-and-acceptance`.
- The vendor document register and submittals, which are scoped to `DEL-024-05_vendor-document-turnover-package`.
- Selection or requirements for the driven 2,000 HP motor itself (TBD; not asserted by source materials for `PKG-024`).

## Requirements

### REQ-1 — Vendor scope ownership (DECLARED)

The Package Vendor shall be responsible for package engineering, package design, vendor documentation, and the physical equipment package. Source: `PACKAGE_REGISTER.csv` row `PKG-024`; `DELIVERABLE_REGISTER.csv` row `DEL-024-04`.

### REQ-2 — EPC integration boundary (DECLARED)

The EPC Integrator shall own facility-level integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration; on this deliverable the EPC Integrator role is limited to integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-024`.

### REQ-3 — Drive rating (DECLARED IDENTITY)

The package shall deliver a medium-voltage VFD function at 2,000 HP, 4,160 V, 3-phase, 60 Hz, with 4,160 V output, as identified in the package name. Source: Workbook Packages row 26.

### REQ-4 — Drive topology, harmonic mitigation, filter, bypass (TBD)

Drive topology, harmonic mitigation requirements, output filter requirements, and bypass arrangement are TBD. The accessible design basis states "VFD and soft-starter requirements for 4.16 kV motors are TBD" and does not assert package-specific values. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957 and 3088.

### REQ-5 — Communications interface (ASSUMPTION)

The package should provide an Ethernet communications port suitable for connection to the plant PLC central control panel, consistent with the facility convention for medium-voltage motor control. ASSUMPTION: convention extended from MV MCC requirement to the MV VFD package; confirmation required against the EPC Package Datasheet (`DEL-024-02`). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Motor Control and Motor Specifications; `INTERFACE_REGISTER.csv` `IFC-22E88310C9`.

### REQ-6 — Grounding (DECLARED, applicability TBD)

Major electrical equipment shall be directly connected to the ground grid at two points. Application of grounding sizing rules and separate copper ground conductors to this VFD package shall be confirmed by detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs; `INTERFACE_REGISTER.csv` `IFC-F8A6E25E1C`.

### REQ-7 — Cabling (DECLARED, applicability TBD)

Low-voltage power cable fed from VFDs shall be Copper TECK cable. Applicability to the 4,160 V output side of `PKG-024` is TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table line 3013.

### REQ-8 — Area classification compliance (DECLARED, applicability TBD)

If any package-supplied motor or VFD-fed equipment is located in a Zone 2 area, that equipment shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor specifications.

### REQ-9 — Maintenance access (DECLARED)

Cable tray and conduit routing into and within the package shall not interfere with maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs; `INTERFACE_REGISTER.csv` `IFC-DD889EF8E3`.

### REQ-10 — Housing and structural supports (TBD)

Whether the package is housed inside a prefabricated electrical building or supplied as an outdoor / skid-mounted assembly is TBD; the design basis confirms only that electrical buildings may house MV VFDs as required by detailed design. Structural / foundation interface obligations apply but package-specific support basis is TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; `INTERFACE_REGISTER.csv` `IFC-850A8082BB`.

### REQ-11 — Vendor design basis and datasheet set (DECLARED ARTIFACT)

The Package Vendor shall produce a vendor package design basis and datasheet set as anticipated artifacts of this deliverable, traceable to the EPC Scope of Work and Package Datasheet inputs. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-024-04`.

## Standards

| Standard / Source | Use | Status |
|---|---|---|
| Project Electrical Design Basis Memorandum (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Authoritative facility-level basis for motor control, MV VFDs, grounding, cabling, and electrical buildings. | Accessible. |
| `_Sources/26020-Package_Requirements.docx` | Project-level package requirements. | Accessible as DOCX; no package-specific PKG-024 slice has been extracted to markdown source. Detailed clauses location TBD. |
| Canadian Electrical Code (CEC) | Cited in design basis for grounding sizing and dry-type transformer spacing context. | Referenced indirectly; clause-level applicability to this package TBD. |
| Workbook Packages row 26 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) | Package identity, WBS, CoA tracking, discipline, interfaces. | Accessible via PACKAGE_REGISTER / INTERFACE_REGISTER. |

Additional MV VFD / motor standards (e.g., IEEE 519, NEMA MG-1, IEC 61800-series) are commonly applicable to a 2,000 HP, 4,160 V VFD but are **not** asserted by accessible source materials for `PKG-024`. ASSUMPTION: likely applicable; location TBD; do not derive clause-level requirements without confirmed source.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-1, REQ-2 | Document review against the EPC Scope of Work (`DEL-024-01`) and the responsibility assignment record. |
| REQ-3 | Vendor datasheet review confirming rated horsepower, input / output voltage, phase, and frequency. |
| REQ-4 | Detailed engineering review and human ruling; verification deferred until source-supported topology / filter / bypass requirements are established. |
| REQ-5 | Factory acceptance test (FAT) and integration test against the plant PLC communication architecture, once confirmed by `DEL-024-02`. |
| REQ-6 | Drawing review and field inspection against the two-point grounding rule and CEC sizing during construction; turnover record per `DEL-024-03` and `DEL-024-06`. |
| REQ-7 | Cable schedule and bill-of-materials review; applicability of TECK cable to MV output side requires human ruling. |
| REQ-8 | Area-classification drawing review against equipment T-code marking. |
| REQ-9 | Maintenance access review during package general arrangement review and constructability review. |
| REQ-10 | Confirmation against the EPC Package Datasheet (`DEL-024-02`) of housing decision and structural / foundation basis. |
| REQ-11 | Vendor document register review against the anticipated artifact list; turnover via `DEL-024-05`. |

## Documentation

The Package Vendor shall produce, at minimum, the following anticipated artifacts (from `_CONTEXT.md`):

- Vendor engineered physical equipment package.
- Vendor package design basis and datasheet set.

These shall be submitted, reviewed, and accepted through the package's vendor document turnover process (`DEL-024-05`) and EPC vendor package review and acceptance process (`DEL-024-06`). Additional document types (e.g., general arrangement drawings, schematics, harmonic studies, FAT records) are conventional for a 2,000 HP MV VFD but are not enumerated in the accessible source set; ASSUMPTION pending the EPC Package Datasheet handoff.
