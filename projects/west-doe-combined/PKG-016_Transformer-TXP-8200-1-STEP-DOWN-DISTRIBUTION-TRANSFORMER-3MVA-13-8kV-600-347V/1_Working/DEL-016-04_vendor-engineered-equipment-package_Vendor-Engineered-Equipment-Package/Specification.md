# Specification: DEL-016-04_vendor-engineered-equipment-package

## Scope

This document specifies the source-grounded requirements for the Vendor Engineered Equipment Package for PKG-016, Transformer TXP-8200-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3 MVA, 13.8 kV / 600 / 347 V.

Included scope:

- Vendor engineering, design, fabrication/supply, and physical equipment package for the step-down distribution transformer package.
- Vendor package design basis and datasheet set.
- Coordination of applicable package interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
- EPC Integrator integration review of the vendor engineered package against the EPC Scope of Work, Package Datasheet, and accepted Gate 7 package basis.

Excluded or not established by available sources:

- Detailed vendor document register requirements: TBD.
- Cooling class, insulating medium (liquid-filled vs. dry-type), winding configuration/vector group, impedance, BIL, tap-changer configuration, bushings, accessories, and protective devices: TBD pending vendor design and EPC review.
- 347 V service configuration (e.g., 600/347 V wye derivation): TBD; not stated in accessible sources.
- Package-specific exclusions: TBD; Gate 7 states no package-specific exclusions in source materials.

Sources: `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `INTERFACE_REGISTER.csv`.

## Requirements

| ID | Requirement | Verification | Source |
|---|---|---|---|
| REQ-016-04-001 | The Package Vendor shall produce the vendor engineered physical equipment package and vendor package design basis/datasheet set for PKG-016. | Confirm delivered artifacts against Gate 7 `ART-AC4469EC25` and `ART-13F6F3D6B6`. | Gate 7 `ARTIFACT_REGISTER.csv`, DEL-016-04 |
| REQ-016-04-002 | The package shall be developed as a vendor-owned electrical package for a 3 MVA step-down distribution transformer (TXP-8200-1), with EPC Integrator review for facility integration and interfaces. | Review vendor package submittal against responsibility model and interface register. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-016 |
| REQ-016-04-003 | The vendor design shall accept a 13.8 kV, 3 phase, 3 wire, 60 Hz LRG primary supply sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | Check vendor electrical ratings and incoming-service data against the DBM electrical basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages and Incoming Power and Transformers |
| REQ-016-04-004 | The vendor design shall deliver a 600 V, 3 phase, 3 wire, 60 Hz HRG (5 A continuous resistor) low-voltage service consistent with the facility 600 V MCC basis for LV loads. | Check secondary service ratings, neutral grounding resistor coordination, and MCC interface data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages; Incoming Power and Transformers (13.8 kV to 600 V, 3 MVA transformer); 600V MCC and Standby Power |
| REQ-016-04-005 | Where the vendor design provides a 347 V service, the configuration shall be documented and confirmed with the EPC Integrator. The accessible source set does not define the 347 V service; assumptions (e.g., line-to-neutral of a 600 V wye) shall not be treated as established design until confirmed. | Review vendor service basis and EPC integration ruling. | Workbook Packages row 18; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages (gap) |
| REQ-016-04-006 | The vendor package shall coordinate Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports interfaces. | Check interface matrix and EPC review comments against `INTERFACE_REGISTER.csv` rows for PKG-016. | Gate 7 `INTERFACE_REGISTER.csv`, PKG-016 |
| REQ-016-04-007 | The vendor package, treated as major electrical equipment, shall be directly connected to the ground grid at two points; distribution transformer grounding shall use separate copper ground conductors per CEC sizing. | Review vendor grounding/bonding details and EPC grounding interface review. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, grounding/bonding paragraphs |
| REQ-016-04-008 | Power circuits at 13.8 kV and 600 V associated with this package shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | Review vendor layout/raceway/interface requirements where vendor scope affects routing. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| REQ-016-04-009 | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design; vendor cable-routing requirements shall not interfere with maintenance access. | Confirm vendor interface requirements and EPC integration review. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| REQ-016-04-010 | The vendor shall provide transformer loading data (weights, footprint, anchorage, and — if liquid-filled — oil-containment requirements) sufficient for EPC foundation/support design. | Confirm vendor structural data against EPC civil/structural review. | Gate 7 `INTERFACE_REGISTER.csv`, `IFC-E3BE98E89B` |
| REQ-016-04-011 | Vendor-specific values not established by an accessible source slice (cooling class, insulating medium, winding configuration, vector group, impedance, BIL, tap-changer, bushing class, protective accessories, factory test scope, site environmental basis, hazardous-area applicability) shall be carried as `TBD` until vendor design or accepted EPC source establishes them. | Gap review before vendor handoff. | `_REFERENCES.md`; `26020-Package_Requirements.docx` package search (no PKG-016 match) |

## Standards

| Standard / basis | Status |
|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section; specific clauses TBD. |
| Project electrical specifications | Referenced by DBM for cable tray, conduit, grounding, and bonding compliance; specific specification numbers and clauses TBD. |
| API RP 505 | Mentioned by DBM as the basis for fugitive-emission studies supporting Zone 2 classification for process modules/buildings; applicability at the transformer location TBD; direct clause text not available in deliverable-local source slice. |
| Detailed electrical studies | Required for harmonic, short-circuit, coordination, and grounding studies affecting the 13.8 kV / 600 V interface; study identity and acceptance criteria TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. |

## Verification

Verification shall include:

- EPC Integrator review of vendor datasheets, design basis, drawings, interface data, and physical package documentation against Gate 7 package basis and DBM electrical basis for the 13.8 kV / 600 V step-down distribution transformer.
- Interface review against Gate 7 `INTERFACE_REGISTER.csv` for PKG-016 (seven interface facts).
- Confirmation that unsupported details remain marked `TBD` until vendor design or EPC-approved source material establishes them.
- Confirmation that any change from the current DBM basis (e.g., 347 V service definition, cooling class, insulating medium) is captured as a formal accepted design ruling before being treated as authoritative.
- Cross-document consistency check that Datasheet, Specification, Guidance, and Procedure use the same package identity, ratings (3 MVA, 13.8 kV, 600 V), interface set, and `TBD` items.

## Documentation

Required or expected documentation for this production unit:

- Vendor engineered physical equipment package.
- Vendor package design basis.
- Vendor datasheet set (transformer nameplate data, cooling, impedance, BIL, vector group, tap changer, accessories, weights/dimensions).
- Vendor interface data for electrical power, grounding/bonding, area/exterior lighting coordination, controls cabling separation, communications/network monitoring, maintenance access, and structural/foundation/support coordination.
- TBD: vendor document register, inspection/test plan, factory routine/type/special test records, and final turnover package requirements (carried by DEL-016-05 and DEL-016-06).
