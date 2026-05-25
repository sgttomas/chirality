# Specification: DEL-033-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-033`, the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-033-01`) and Package Datasheet (`DEL-033-02`), and is subject to EPC Integrator integration review through `DEL-033-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (a 4160 V switchgear electrical building housing switchgear, MCC content, distribution equipment, and associated HVAC/ventilation as required by detailed design). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-033-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-033-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-033-06_epc-vendor-package-review-and-acceptance`.
- Facility incoming-power scope upstream of the building boundary (13.8 kV utility supply, 13.8 kV main switchgear, and the 13.8 kV-to-4.16 kV / 12 MVA step-down transformer) is excluded; those are facility scope per the 03-25 DBM and EPC integration.
- Package-specific switchgear lineup, bus rating, short-circuit rating, breaker count and frame size, arc-flash class, building footprint, HVAC sizing, and installation location remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-033-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-033-01`) and Package Datasheet (`DEL-033-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-033-01`, `DEL-033-02`, `DEL-033-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-033-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-033`. | Responsibility statement review against Gate 7 package register. |
| REQ-033-04-003 | The vendor package shall be engineered to the twelve applicable package interfaces enumerated in `INTERFACE_REGISTER.csv` for `PKG-033`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 35; `INTERFACE_REGISTER.csv`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-033`. |
| REQ-033-04-004 | The vendor package medium-voltage design basis shall be consistent with the 03-25 DBM System Voltages table: 4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded, intended for process AC inverter-drive motors from 250 hp to 5,500 hp. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages. | Vendor design basis check against the DBM System Voltages table. |
| REQ-033-04-005 | The vendor package shall be compatible with the incoming-power basis: 4160 V service sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building through a facility-scope 13.8 kV to 4.16 kV, 12 MVA transformer feeding the 4160 V MCC for 4000 V motors. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers. | Vendor design verification against the facility incoming-power one-line and feeder schedule. |
| REQ-033-04-006 | The vendor package shall provide and support the 4160 V MCC functional features required by the DBM: field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC. | Vendor design review confirming presence of fused contactors, motor protection relays, and the EtherNet data link. |
| REQ-033-04-007 | The vendor package shall preserve segregation of 13.8 kV, 4,160 V, and 600 V power circuits from control and instrument circuits by distance, shielding, or routing as required to minimize interference; cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing. | Vendor layout / cable schedule review against the DBM segregation rule. |
| REQ-033-04-008 | The vendor package grounding/bonding design shall accommodate two-point ground-grid connection of major electrical equipment and CEC-sized separate copper grounding conductors for distribution transformers, panelboards, and three-phase motors larger than 100 hp, where applicable to building equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor grounding design review. |
| REQ-033-04-009 | The vendor package building shall be located in a general-purpose (non-hazardous) area and shall coordinate building HVAC, ventilation, and area-classification rating with the controls architecture and hazardous-area classification basis. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification; Electrical Buildings. | Area classification and HVAC basis review at integration acceptance. |
| REQ-033-04-010 | The vendor package layout shall preserve the Maintenance Access interface, including door sizing or removable transom provisions sufficient to remove the largest equipment, where 04-25 practice is adopted. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph. | Vendor layout review against the Maintenance Access interface. |
| REQ-033-04-011 | The vendor package foundation/anchorage design shall be coordinated with the project geotechnical and structural basis: equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access shall be addressed; electrical buildings require equipment-specific foundation and anchorage checks. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations. | Foundation/anchorage check at integration review against the EPC Structural / Foundations / Supports interface. |
| REQ-033-04-012 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-033-04`. | Artifact register check against vendor delivery. |
| REQ-033-04-013 | Source gaps for switchgear lineup, bus rating, short-circuit rating, breaker count/frame size, arc-flash class, building footprint, HVAC sizing, installation location, and the relationship of the "830-2" tag to the 04-25 Buildings-schedule "830-1" tag shall be resolved by vendor data and EPC integration during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search returned no PKG-033 match in accessible sources. | Vendor data review at EPC vendor package acceptance (`DEL-033-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/switchgear/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards (API RP 505; Class I Zone 2 IIA/IIB basis) | Applicable to building location, equipment selection, ventilation, and controls architecture. | Applicable as cited by 03-25 DBM Area Classification; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-033-01`) and EPC Package Datasheet (`DEL-033-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-033-01` Scope of Work and `DEL-033-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 35 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-033`. | All twelve applicable interfaces are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-033-05` (turnover) and `DEL-033-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (4160 V switchgear electrical building).
- Vendor package design basis.
- Vendor package datasheet set (including switchgear lineup, ratings, MCC functional features, HVAC, raceway and grounding response, foundation/anchorage response).
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 35, applicable Gate 7 registers, and the DBM source slices used for the 4160 V service basis, incoming-power basis, MCC functional features, electrical-building and raceway basis, grounding basis, and foundation basis, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
