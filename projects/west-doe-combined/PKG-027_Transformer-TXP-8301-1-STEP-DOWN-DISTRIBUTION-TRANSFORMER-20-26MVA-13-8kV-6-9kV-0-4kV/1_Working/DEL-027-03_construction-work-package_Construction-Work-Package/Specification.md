# Specification: DEL-027-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-027`, the Transformer TXP-8301-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV. The construction work package is a mandatory Gate 5 EPC anchor deliverable that describes how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. This specification addresses only the EPC-owned construction scope.

Exclusions:

- Vendor detailed design calculations, certified drawings, FAT protocols, and final equipment construction-of-the-unit details are excluded except where they constrain field installation.
- Package-specific rigging plan, lift weights, transport route, oil-handling protocol, FAT/SAT/commissioning sequences, foundation footing design, and final tie-in termination drawings are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-027-03-001 | The Construction Work Package shall identify `PKG-027`, workbook row 29, WBS 01, CoA tracking number 26020-01-30-018, discipline Electrical, and package name "Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV." Source: Workbook Packages row 29; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-027-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, construction interfaces, tie-ins, constructability, and construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-027`. | Responsibility statement review against Gate 7 package register. |
| REQ-027-03-003 | The Construction Work Package shall plan and execute construction for all seven applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 29; `INTERFACE_REGISTER.csv` rows for `PKG-027`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-027-03-004 | Foundation construction shall follow source-supported transformer foundation practice (structural steel transformer base or precast concrete bearing foundation), with secondary containment installed where required by the reviewed design. Detailed footing design is `TBD` pending civil/structural detailed engineering. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and foundation concepts paragraphs. | Field inspection against issued-for-construction (IFC) civil/structural drawings; record discrepancies. |
| REQ-027-03-005 | Construction shall install two-point grounding from the transformer to the facility ground grid and shall provide a ground well at the transformer for maintenance and operational testing. The 6.9 kV winding neutral grounding installation shall be coordinated with the project NGR scheme (DBM specifies 100 A, 10 s NGR as a tripping system for 6.9 kV transformers; applicability to TXP-8301-1 shall be confirmed). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Continuity and resistance testing per project electrical commissioning standard. |
| REQ-027-03-006 | Construction shall preserve transformer spacing per CEC requirements during installation and shall coordinate spacing with adjacent equipment, exterior lighting, fencing, and access roads. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. | Field measurement against IFC site plan. |
| REQ-027-03-007 | Construction shall route and install I&C / control cabling and communications/network cabling to the transformer in cable tray and conduit so that maintenance access is preserved. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Walk-down inspection against IFC routing drawings. |
| REQ-027-03-008 | Construction shall produce and maintain the construction interface and turnover checklist (`ART-6C4FC25B92`) and the installation and tie-in workface plan (`ART-16F575F6A0`) as part of the construction work package. Source: `ARTIFACT_REGISTER.csv`. | Document existence and content review at gate closure. |
| REQ-027-03-009 | Construction shall identify and carry forward as `TBD` all items requiring vendor data or detailed engineering inputs (rigging plan, lift weight, transport route, laydown, oil-handling, FAT/SAT/commissioning protocol, termination drawings). The construction work package shall not invent unsupported values. Source: `_REFERENCES.md`; package source gap. | Open-item review before construction release. |
| REQ-027-03-010 | Construction tie-in to 13.8 kV primary, 6.9 kV secondary, and 0.4 kV secondary distribution shall be coordinated with adjacent electrical packages and the facility electrical system architecture. Source: Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical system architecture paragraph (ASSUMPTION: TXP-8301-1 participates in this architecture based on voltage class). | Interface coordination review with adjacent packages. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding conductor sizing, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway/commissioning bases referenced by DBM. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment installation, conduit sealing, and classification of the transformer area. | Applicable; specific area classification for TXP-8301-1 location TBD. |
| Civil/structural design code (foundations) | Applicable to transformer foundation construction. | Applicable; specific code/clauses TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 29 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface coverage | Compare construction scope to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | All seven applicable interfaces are addressed in the construction work package. |
| Source fidelity | Check every non-trivial construction requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as confirmed requirements. |
| Foundation, grounding, spacing | Field inspection and testing against IFC drawings and project electrical standard. | Two-point grounding installed, NGR scheme coordinated, transformer spacing meets CEC. |
| Workface plan and turnover checklist | Verify `ART-16F575F6A0` and `ART-6C4FC25B92` exist and are populated. | Both artifacts produced and accepted. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package narrative (`ART-F3C58917C8`).
- Installation and tie-in workface plan (`ART-16F575F6A0`).
- Construction interface and turnover checklist (`ART-6C4FC25B92`).
- Source-gap / `TBD` list for vendor or human resolution (rigging, oil handling, FAT/SAT/commissioning, termination drawings, foundation footing).

The deliverable shall cite the Gate 7 snapshot, workbook row 29, applicable Gate 7 registers, and the DBM electrical and foundation source slices used.
