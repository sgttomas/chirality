# Specification: DEL-028-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor production unit for `PKG-028`, the Transformer TXP-8801-1 step-down distribution transformer package rated 7.5 MVA, 13.8 kV / 4160 / 2400 V. The deliverable covers vendor engineering, design, fabrication/supply, and the physical equipment package, developed from the EPC Scope of Work (`DEL-028-01`) and EPC Package Datasheet (`DEL-028-02`), with EPC Integrator integration review.

The package is a vendor-owned Electrical package under WBS 01 in the Deepcut (4-25) facility scope. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-owned facility integration design, tie-ins, foundations/supports detailed engineering, and constructability planning are excluded from the vendor production unit except as required vendor inputs (e.g., loading data, terminations).
- Detailed transformer electrical parameters not present in the accessible source set — cooling class, vector group, impedance, BIL, tap-changer configuration, insulating medium, 4160 V and 2400 V service definitions, site environmental design conditions, hazardous-area classification, factory test list, and installation location — are carried as `TBD` and shall be resolved through the EPC Scope of Work, EPC Package Datasheet, and vendor design basis before fabrication release.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-028-04-001 | The vendor production unit shall identify `PKG-028`, workbook row 30, WBS 01, CoA tracking number 26020-01-30-019, discipline Electrical, package tag TXP-8801-1, and package name "Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V." Source: Workbook Packages row 30; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-028-04-002 | The vendor production unit shall observe the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-028`. | Responsibility review against Gate 7 package register. |
| REQ-028-04-003 | The vendor package shall be engineered for a 13.8 kV, 3-phase, 3-wire, 60 Hz LRG primary supply consistent with the Deepcut facility 13.8 kV distribution and shall deliver 4160 V and 2400 V secondary services as carried by the package name. Source: Workbook Packages row 30; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` facility electrical system narrative and voltage/service table. | Vendor design basis review against source feed basis; 4160 V and 2400 V secondary service definitions flagged for EPC clarification (HRR-028-04-001). |
| REQ-028-04-004 | The vendor production unit shall address all seven `PKG-028` interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 30; `INTERFACE_REGISTER.csv` rows for `PKG-028`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-028`. |
| REQ-028-04-005 | Major electrical equipment in the package shall be connectable to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall be served by separate copper ground conductors sized per CEC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` grounding/bonding paragraphs. | Grounding/bonding design review. |
| REQ-028-04-006 | Power circuits at medium voltage (13.8 kV) and low voltage (600 V and below) shall be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical system narrative. | Cable routing and segregation review against the package interface matrix. |
| REQ-028-04-007 | Cable tray and conduit routing related to or interfacing with the package shall not interfere with maintenance access. Source: `INTERFACE_REGISTER.csv` `IFC-5C19FEBFC8`. | Layout/maintenance access review. |
| REQ-028-04-008 | The vendor shall provide transformer loading, anchor, and clearance data sufficient for EPC foundation/support design and constructability review; general DBM practice is precast concrete bearing foundations or structural steel transformer bases. Source: `INTERFACE_REGISTER.csv` `IFC-B1AD88E9C0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers and foundations sections; `PACKAGE_REGISTER.csv` row `PKG-028`. | Foundation/support interface review. |
| REQ-028-04-009 | If the vendor selects an oil-filled transformer, spacing per CEC requirements and review of secondary containment requirements shall be addressed per the DBM Transformers section, with selection biased toward avoiding or limiting containment requirements where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers section. | Insulating-medium selection and containment review. |
| REQ-028-04-010 | The vendor production unit shall produce the artifacts identified in `ARTIFACT_REGISTER.csv` for `DEL-028-04`: the vendor engineered physical equipment package (`ART-BC53713A9F`) and the vendor package design basis and datasheet set (`ART-6814431C11`). Source: `ARTIFACT_REGISTER.csv`. | Artifact completeness review. |
| REQ-028-04-011 | Detailed transformer parameters not supported by accessible source slices — cooling class, vector group, impedance, BIL, tap-changer configuration, insulating medium, 4160 V and 2400 V service definitions, site environmental design conditions, hazardous-area classification, factory test scope, and installation location — shall remain `TBD` and shall be resolved through the EPC Scope of Work, EPC Package Datasheet, and vendor design basis before fabrication release. Source: `_REFERENCES.md`; source gap recorded in this run. | TBD/open-item review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding/bonding of major electrical equipment, conductor sizing, transformer spacing, and electrical installation basis referenced by DBM electrical sections. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical sections. | Applicable; document location TBD. |
| Area classification standards | Applicable to outdoor/indoor electrical equipment installation; specific classification at TXP-8801-1 location not stated in accessible sources. | Applicable; location/classification TBD. |
| Transformer standards (IEEE C57 series, IEC 60076, CSA equivalents) | Likely applicable to step-down distribution transformer design, testing, and acceptance. | ASSUMPTION: likely applicable; clauses not derivable without access to standard text. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 30 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-028`. | All seven interface facts (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are present. |
| Feed and service basis | Confirm primary 13.8 kV feed basis against the Deepcut DBM facility electrical system narrative and voltage/service table; flag the 4160 V and 2400 V secondary service definitions as TBD. | Vendor design accepts the documented primary feed and carries 4160 V / 2400 V secondaries per package name pending EPC clarification. |
| Source fidelity | Check every non-trivial value against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor scope (engineering/design/fabrication/equipment) and EPC integration-review scope are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, ratings, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Artifact completeness | Confirm both `DEL-028-04` artifacts are produced or planned. | `ART-BC53713A9F` and `ART-6814431C11` are accounted for. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (`ART-BC53713A9F`).
- Vendor package design basis and datasheet set (`ART-6814431C11`).
- Vendor-side interface confirmations for the seven `PKG-028` interface facts.
- Source-supported design criteria and source-gap / `TBD` list for EPC and vendor resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 30, applicable Gate 7 registers, the Deepcut DBM electrical source slices used for feed/grounding/transformer/foundation basis, and the EPC anchor deliverables `DEL-028-01` (Scope of Work) and `DEL-028-02` (Package Datasheet) as upstream inputs.
