# Specification: DEL-015-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor production unit for `PKG-015`, the Transformer TXP-8300-1 step-down distribution transformer package rated 12/15 MVA, 13.8 kV / 4160 / 2400 V. The deliverable covers vendor engineering, design, fabrication/supply, and the physical equipment package, developed from the EPC Scope of Work (`DEL-015-01`) and EPC Package Datasheet (`DEL-015-02`), with EPC Integrator integration review.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-owned facility integration design, tie-ins, foundations/supports detailed engineering, and constructability planning are excluded from the vendor production unit except as required vendor inputs (e.g., loading data, terminations).
- Detailed transformer electrical parameters not present in the accessible source set — cooling class, vector group, impedance, BIL, tap-changer configuration, insulating medium, 2400 V service definition, site environmental design conditions, hazardous-area classification, factory test list, and installation location — are carried as `TBD` and shall be resolved through the EPC Scope of Work, EPC Package Datasheet, and vendor design basis before fabrication release.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-015-04-001 | The vendor production unit shall identify `PKG-015`, workbook row 17, WBS 02, CoA tracking number 26020-02-30-006, discipline Electrical, package tag TXP-8300-1, and package name "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V." Source: Workbook Packages row 17; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-015-04-002 | The vendor production unit shall observe the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-015`. | Responsibility review against Gate 7 package register. |
| REQ-015-04-003 | The vendor package shall be engineered for a 13.8 kV, 3-phase, 3-wire, 60 Hz LRG primary supply sub-fed from the 04-25 13.8 kV Main Switchgear and shall deliver 4160 V and 2400 V secondary services as carried by the package name. Source: Workbook Packages row 17; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` voltage/service table and Incoming Power and Transformers section. | Vendor design basis review against source feed/service basis; 2400 V definition flagged for EPC clarification (HRR-015-04-001). |
| REQ-015-04-004 | The vendor package shall be designed for compatibility with the 4160 V process MCC that serves inverter-drive motors from 250 hp to 5,500 hp, including coordination with VFD-driven loads (e.g., KM-2150, KM-2250). Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` 4160V MCC section. | Coordination review with the EPC Package Datasheet and electrical studies. |
| REQ-015-04-005 | The vendor production unit shall address all seven `PKG-015` interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 17; `INTERFACE_REGISTER.csv` rows for `PKG-015`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-015`. |
| REQ-015-04-006 | Major electrical equipment in the package shall be connectable to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall be served by separate copper ground conductors sized per CEC. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` grounding/bonding paragraphs. | Grounding/bonding design review. |
| REQ-015-04-007 | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` power/control separation paragraph. | Cable routing and segregation review against the package interface matrix. |
| REQ-015-04-008 | Cable tray and conduit routing related to or interfacing with the package shall not interfere with maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` cable tray and conduit paragraphs; `INTERFACE_REGISTER.csv` `IFC-B9C22F51DB`. | Layout/maintenance access review. |
| REQ-015-04-009 | The vendor shall provide transformer loading, anchor, and clearance data sufficient for EPC foundation/support design and constructability review. Source: `INTERFACE_REGISTER.csv` `IFC-2646D74297`; `PACKAGE_REGISTER.csv` row `PKG-015`. | Foundation/support interface review. |
| REQ-015-04-010 | The vendor production unit shall produce the artifacts identified in `ARTIFACT_REGISTER.csv` for `DEL-015-04`: the vendor engineered physical equipment package (`ART-365325DAB5`) and the vendor package design basis and datasheet set (`ART-96A2C9D72C`). Source: `ARTIFACT_REGISTER.csv`. | Artifact completeness review. |
| REQ-015-04-011 | Detailed transformer parameters not supported by accessible source slices — cooling class, vector group, impedance, BIL, tap-changer configuration, insulating medium, 2400 V service definition, site environmental design conditions, hazardous-area classification, factory test scope, and installation location — shall remain `TBD` and shall be resolved through the EPC Scope of Work, EPC Package Datasheet, and vendor design basis before fabrication release. Source: `_REFERENCES.md`; source gap recorded in this run. | TBD/open-item review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding/bonding of major electrical equipment, conductor sizing, electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to outdoor/indoor electrical equipment installation; specific classification at TXP-8300-1 location not stated in accessible sources. | Applicable; location/classification TBD. |
| Transformer standards (IEEE C57 series, IEC 60076, CSA equivalents) | Likely applicable to step-down distribution transformer design, testing, and acceptance. | ASSUMPTION: likely applicable; clauses not derivable without access to standard text. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 17 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-015`. | All seven interface facts (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are present. |
| Feed and service basis | Confirm primary 13.8 kV feed basis and secondary service references against the DBM voltage/service table and Incoming Power and Transformers section. | Vendor design accepts the documented primary feed and notes 4160 V / 2400 V secondaries per package name. |
| Source fidelity | Check every non-trivial value against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor scope (engineering/design/fabrication/equipment) and EPC integration-review scope are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, ratings, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Artifact completeness | Confirm both `DEL-015-04` artifacts are produced or planned. | `ART-365325DAB5` and `ART-96A2C9D72C` are accounted for. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (`ART-365325DAB5`).
- Vendor package design basis and datasheet set (`ART-96A2C9D72C`).
- Vendor-side interface confirmations for the seven `PKG-015` interface facts.
- Source-supported design criteria and source-gap / `TBD` list for EPC and vendor resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 17, applicable Gate 7 registers, the DBM electrical source slices used for feed/service/grounding/cable basis, and the EPC anchor deliverables `DEL-015-01` (Scope of Work) and `DEL-015-02` (Package Datasheet) as upstream inputs.
