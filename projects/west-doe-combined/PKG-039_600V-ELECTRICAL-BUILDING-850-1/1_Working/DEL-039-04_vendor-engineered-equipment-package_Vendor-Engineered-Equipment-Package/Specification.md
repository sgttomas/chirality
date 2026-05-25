# Specification: DEL-039-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-039`, the 600V ELECTRICAL BUILDING (850-1) — the 600 V Inlet / Sales Compressor Electrical Building. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-039-01`) and Package Datasheet (`DEL-039-02`), and is subject to EPC Integrator integration review through `DEL-039-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (the shop-built modular electrical building and its internal equipment). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-039-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-039-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-039-06_epc-vendor-package-review-and-acceptance`.
- Facility-level standby-power coordination — TOU standby generator sizing, transfer-switch configuration at the 600 V MCC, load shedding, sequencing, and TOU standard confirmation — is EPC integration scope and is not vendor scope.
- Package-specific equipment counts (MCC sections, transformer ratings, UPS ratings, VFD list, PLC and network rack count), plot-plan coordinates, pile and foundation design, and detailed Fire & Gas device lists remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor and EPC shall resolve these during package engineering and integration.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-039-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-039-01`) and Package Datasheet (`DEL-039-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-039-01`, `DEL-039-02`, `DEL-039-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-039-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-039`. | Responsibility statement review against Gate 7 package register. |
| REQ-039-04-003 | The vendor package shall be engineered to all twelve applicable package interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; and Structural / Foundations / Supports. Source: Workbook Packages row 41; `INTERFACE_REGISTER.csv` rows for `PKG-039`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-039`. |
| REQ-039-04-004 | The vendor building shall be a prefabricated, shop-built modular electrical building located in a general-purpose (unclassified) area. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings paragraph and electrical-buildings table row "850-1 ... Shop"; area-classification paragraph. | Compare vendor design to DBM building classification and shop-build basis. |
| REQ-039-04-005 | Building equipment population shall be drawn from the DBM-permitted set "as required by detailed design": 600 V MCCs (traditional with electronic motor overload relays), 600 V VFDs as part of the MCC lineup, 600 V SCR heater-control panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, plant PLC control panels, and network racks. Equipment counts, ratings, and inclusion of medium-voltage gear remain `TBD` until vendor data resolves them. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" and 600 V MCC paragraphs. | Vendor equipment list review against the DBM-permitted population. |
| REQ-039-04-006 | The vendor building shall be designed for bottom entry of incoming and outgoing power cables and shall be elevated on piles to provide space beneath the building for MCC incoming cable trays and outgoing 600 V MCC cabling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph. | Vendor layout/section drawing review against the cable-entry basis. |
| REQ-039-04-007 | Internal wiring shall use TECK and ACIC cables; EMT conduit shall be used for adjacent equipment (e.g., control panels to contactor panels). An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors shall be sized for (or include removable transom sections to allow) removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph. | Vendor wiring and door-sizing review. |
| REQ-039-04-008 | The vendor building HVAC shall be n + 1 sized so the cooling system tolerates failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling; electric heaters (e.g., Ruffneck-type) shall provide heat where heat-medium heating is impractical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, HVAC and building-heaters paragraphs. | Vendor HVAC sizing and heater selection review. |
| REQ-039-04-009 | The vendor building shall be engineered to be compatible with standby-power coordination at the 600 V MCC level via TOU standby generators and transfer switches; generator sizing, transfer-switch configuration, load shedding, sequencing, and TOU standard confirmation remain EPC integration scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby-power paragraph. | TBD/open-item review at integration acceptance. |
| REQ-039-04-010 | The vendor grounding system shall meet major-equipment two-point ground-grid connection and CEC-sized separate copper grounding conductors for distribution transformers, panelboards, and three-phase motors larger than 100 hp where applicable, without overstating package-specific grounding detail not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor grounding design review. |
| REQ-039-04-011 | Motor local control stations (default Hand-Off-Auto or On-Off) shall be supplied as required by detailed design and shall be hard-wired to the motor starter circuits of the 600 V MCC by the field construction contractor; standalone 600 V VFDs are not allowed unless dedicated to large motors. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 600 V MCC paragraphs. | Vendor MCC and VFD lineup review against the DBM motor-control basis. |
| REQ-039-04-012 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package (the shop-built electrical building and internal equipment per the design basis) and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-039-04`. | Artifact register check against vendor delivery. |
| REQ-039-04-013 | Source gaps for equipment counts/ratings, plot-plan location, pile/foundation design, F&G device list, and any package-specific exclusions shall be resolved by vendor data and EPC integration during package engineering; values shall not be invented in advance. Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row `PKG-039` (exclusions: TBD). | Vendor data review at EPC vendor package acceptance (`DEL-039-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Vendor building is sited in a general-purpose (unclassified) area per DBM; equipment classification applies where local hazardous-area exceptions arise. | Applicable; specific clause locations TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-039-01`) and EPC Package Datasheet (`DEL-039-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-039-01` Scope of Work and `DEL-039-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 41 and Gate 7 registers. | Package name, IDs, discipline, and `PACKAGE_REGISTER.csv` identity fields match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-039`. | All twelve applicable interfaces are addressed. |
| Building basis fidelity | Compare vendor building to DBM electrical-buildings basis (prefabricated, modular, shop-built, general-purpose-area, elevated on piles, bottom cable entry, n + 1 HVAC, TECK/ACIC internal wiring). | Each DBM basis item is reflected or explicitly carried as a vendor-data gap. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-039-05` (turnover) and `DEL-039-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (the shop-built modular 600 V electrical building, complete with the internal equipment specified by the design basis).
- Vendor package design basis (including building layout, interface responses, HVAC sizing basis, cable-entry basis, grounding basis, and standby-power compatibility statement).
- Vendor package datasheet set (per-equipment datasheets for MCCs, VFDs, transformers, panelboards, UPS systems, control panels, and HVAC as applicable).
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 41, applicable Gate 7 registers, and the DBM electrical-buildings source slices used for the design basis, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
