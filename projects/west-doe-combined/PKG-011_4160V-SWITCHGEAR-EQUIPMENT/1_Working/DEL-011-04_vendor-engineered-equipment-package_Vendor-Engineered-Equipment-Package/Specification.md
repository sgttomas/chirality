# Specification: DEL-011-04_vendor-engineered-equipment-package

## Scope

This document specifies the source-grounded requirements for the Vendor Engineered Equipment Package for PKG-011, 4160V SWITCHGEAR EQUIPMENT.

Included scope:

- Vendor engineering, design, fabrication/supply, and physical equipment package for the 4160V switchgear equipment package.
- Vendor package design basis and datasheet set.
- Coordination of applicable package interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
- EPC Integrator integration review of the vendor engineered package against the EPC Scope of Work, Package Datasheet, and accepted Gate 7 package basis.

Excluded or not established by available sources:

- Detailed vendor document register requirements: TBD.
- Detailed switchgear lineup configuration, enclosure rating, bus rating, protection settings, physical dimensions, and testing procedures: TBD pending vendor design and EPC review.
- Package-specific exclusions: TBD; Gate 7 states no package-specific exclusions in source materials.

Sources: `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `INTERFACE_REGISTER.csv`.

## Requirements

| ID | Requirement | Verification | Source |
|---|---|---|---|
| REQ-011-04-001 | The Package Vendor shall produce the vendor engineered physical equipment package and vendor package design basis/datasheet set for PKG-011. | Confirm delivered artifacts against Gate 7 ART-35E12ECF7A and ART-095CD46A13. | Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-04 |
| REQ-011-04-002 | The package shall be developed as a vendor-owned electrical package for 4160V switchgear equipment, with EPC Integrator review for facility integration and interfaces. | Review vendor package submittal against responsibility model and interface register. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011 |
| REQ-011-04-003 | The vendor design shall support the 4,160 V, 3 phase, 3 wire, 60 Hz LRG medium-voltage service basis. | Check vendor electrical ratings and datasheets. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages |
| REQ-011-04-004 | The vendor design shall coordinate with the 13.8 kV to 4.16 kV, 12 MVA transformer service basis for the 4160V MCC serving 4000V motors. | Check one-line/interface data and vendor incoming/service data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| REQ-011-04-005 | The 4160V MCC package basis shall include field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition unless superseded by a later accepted design ruling. | Review vendor MCC datasheets, protection/control drawings, and communication interface data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-04-006 | The package shall support large 4000V motor loads identified in source, including inlet compressors KM-2150 and KM-2250. | Review load list alignment and starter/feed data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-04-007 | Starting VFDs shall be used for KM-2150 and KM-2250; soft starts shall not be used for these inlet compressor motors under the current basis. | Confirm starter technology in vendor design documents. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-04-008 | Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | Confirm study completion or formal TBD carry-forward before final acceptance. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| REQ-011-04-009 | The vendor package shall coordinate Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports interfaces. | Check interface matrix and EPC review comments. | Gate 7 `INTERFACE_REGISTER.csv`, PKG-011 |
| REQ-011-04-010 | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | Review vendor layout/raceway/interface requirements where vendor scope affects routing. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| REQ-011-04-011 | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. | Confirm vendor interface requirements and EPC integration review. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |

## Standards

| Standard / basis | Status |
|---|---|
| API RP 505 | Mentioned as the basis for fugitive-emission studies supporting Zone 2 classification for process modules/buildings; direct clause text not available in deliverable-local source slice. |
| Project electrical specifications | Referenced by DBM for cable tray, conduit, grounding, and bonding compliance; specific specification numbers and clauses are TBD. |
| Detailed electrical studies | Required to determine harmonic and reactive-power mitigation; study identity and acceptance criteria are TBD. |

## Verification

Verification shall include:

- EPC Integrator review of vendor datasheets, design basis, drawings, interface data, and physical package documentation against Gate 7 package basis and DBM SEC-12 electrical basis.
- Interface review against Gate 7 `INTERFACE_REGISTER.csv` for PKG-011.
- Confirmation that unsupported details remain marked `TBD` until vendor design or EPC-approved source material establishes them.
- Confirmation that any change from the current DBM basis is captured as a formal accepted design ruling before being treated as authoritative.

## Documentation

Required or expected documentation for this production unit:

- Vendor engineered physical equipment package.
- Vendor package design basis.
- Vendor datasheet set.
- Vendor interface data for electrical power, grounding/bonding, controls cabling, communications/network, maintenance access, and structural/foundation/support coordination.
- TBD: vendor document register, inspection/test plan, factory/shop test records, and final turnover package requirements.
