# Specification: DEL-029-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor production unit for `PKG-029`, the "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" package. The deliverable comprises vendor engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. EPC Integrator integration review and facility-level interfaces are in scope of the EPC Package Datasheet (`DEL-029-02`, if produced) and Construction Work Package, not of this vendor production unit.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-authored Package Datasheet content, EPC Scope of Work, and Construction Work Package are excluded from this vendor production unit; they are separate deliverables.
- Detailed facility-side electrical studies (short-circuit, coordination, arc-flash) are excluded from the vendor package unless explicitly contracted to the vendor.
- Allocation of TXP-8600-1 to a specific facility (04-25 Deepcut vs 03-25 Comp and Liquids) is `TBD` and is not assigned by this specification.
- Vendor winding configuration, impedance, cooling class, insulation type (oil-filled vs dry-type), tap-changer arrangement, and accessory selection are `TBD` and become vendor scope under detailed design.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-029-04-001 | The vendor engineered equipment package shall be delivered as a single transformer asset tagged TXP-8600-1, with nameplate rating 2.5 MVA, 13.8 kV primary, 600/347 V secondary, consistent with the workbook package title and Gate 7 register. Source: Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029`. | Vendor nameplate review against Gate 7 register and workbook row. |
| REQ-029-04-002 | The vendor production unit shall preserve the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-029`. | Responsibility statement review against Gate 7 package register. |
| REQ-029-04-003 | The vendor production unit shall preserve and respond to the seven applicable interface facts for PKG-029: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv` rows for `PKG-029`. | Interface response matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-029`. |
| REQ-029-04-004 | Secondary neutral grounding of the 600 V system at TXP-8600-1 shall use a 5 A continuous high-resistance grounding resistor; downstream 600 V MCC shall include power metering and ground/resistor fault detection; ground-fault protection on the 600 V system shall be alarm-only. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding scheme review against DBM electrical basis. |
| REQ-029-04-005 | The transformer secondary feeder to the served 600 V MCC shall be specified consistent with the facility cable basis (ACWU; single-conductor cables avoided) when interfaced to facility cabling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable type table. | Cable schedule consistency review at the package interface. |
| REQ-029-04-006 | Vendor equipment package shall include vendor documentation supporting the EPC Package Datasheet and the vendor-document turnover deliverable (vendor design basis, certified general-arrangement, electrical schematic, protection scheme, nameplate, factory test certificate, and installation/commissioning data). Source: `_CONTEXT.md` anticipated artifacts; `ARTIFACT_REGISTER.csv` rows `ART-D86EE0EF6E` and `ART-F831FA81A1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis and references to vendor data. | Vendor document register review; turnover readiness check. |
| REQ-029-04-007 | Foundation, spacing, secondary containment (if applicable), grounding well, and maintenance access provisions shall be coordinated with the EPC Integrator and consistent with CEC spacing requirements and the DBM transformers and foundations basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table. | Foundation/spacing/access review at integration. |
| REQ-029-04-008 | Items not supported by accessible source slices (TXP-8600-1 facility allocation, insulation type, cooling class, impedance, vendor selection, EHT or auxiliary loads, control voltage source) shall remain `TBD` in vendor handoff documentation rather than be defaulted to invented values. Source: `_REFERENCES.md` and source gap analysis. | Gap review before vendor design freeze. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding, conduit support, and installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, MCC, grounding, cable, and raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to transformer installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Industry transformer standards (e.g., CSA C88 / IEEE C57 / IEC 60076 series) | Likely applicable to vendor design and factory testing of a 2.5 MVA 13.8 kV/600 V distribution transformer. | ASSUMPTION: likely applicable; specific standard and clause selection TBD pending vendor data and project electrical specification. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare vendor nameplate and identity records to workbook row 31 and Gate 7 registers. | Tag (TXP-8600-1), rating (2.5 MVA), and voltages (13.8 kV / 600 / 347 V) match accepted source. |
| Interface completeness | Compare vendor interface response to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | All seven applicable interface facts have a vendor response. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, tag, ratings, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Grounding compliance | Confirm 600 V high-resistance neutral grounding (5 A continuous) at TXP-8600-1 secondary with downstream alarm-only ground-fault protection. | DBM electrical basis satisfied. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (`ART-D86EE0EF6E`).
- Vendor package design basis and datasheet set (`ART-F831FA81A1`).
- Vendor electrical schematic, protection scheme, nameplate, factory test certificate, and installation/commissioning data.
- Vendor interface response matrix aligned with the seven PKG-029 interface facts.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 31, applicable Gate 7 registers, and the DBM electrical source slices used for distribution transformer, grounding, foundations, and cable basis.
