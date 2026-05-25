# Specification: DEL-014-04_vendor-engineered-equipment-package

## Scope

This deliverable is the Package Vendor production unit for `PKG-014` (CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE). It covers vendor engineering, design, fabrication/supply, and the physical equipment package for low-voltage contactor panels serving lighting and exhaust fan loads, anchored by the EPC Scope of Work (`DEL-014-01`) and Package Datasheet (`DEL-014-02`). It does not cover the EPC-authored scope-of-work, EPC-authored package datasheet, construction work package, vendor document turnover register, or EPC vendor package review/acceptance — those are sibling deliverables (`DEL-014-01`, `DEL-014-02`, `DEL-014-03`, `DEL-014-05`, `DEL-014-06`).

Inclusions:
- Vendor package engineering and design for low-voltage lighting and exhaust fan contactor panels.
- Vendor-supplied physical equipment package (contactor panels and associated enclosures, internal wiring, terminations, and nameplates).
- Vendor design basis and datasheet set supporting the EPC handoff and integration review.

Exclusions:
- Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration design (EPC Integrator scope per `PACKAGE_REGISTER.csv` row `PKG-014`).
- Vendor document register, submittals, and turnover records (captured by `DEL-014-05`).
- EPC vendor package review and acceptance evidence (captured by `DEL-014-06`).

## Requirements

| ID | Requirement | Source / status |
|---|---|---|
| REQ-014-04-01 | The vendor engineered equipment package shall implement the package function: low-voltage contactor panels for lighting and exhaust fan control. | Workbook Packages row 16; `PACKAGE_REGISTER.csv` row `PKG-014` |
| REQ-014-04-02 | The vendor engineering shall be developed from the EPC Scope of Work (`DEL-014-01`) and the EPC Package Datasheet (`DEL-014-02`). | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` |
| REQ-014-04-03 | The vendor scope shall comprise package engineering, package design, vendor documentation contribution, and the physical equipment package. EPC Integrator retains facility integration, interfaces, tie-ins, constructability, and facility-level coordination. | `PACKAGE_REGISTER.csv` row `PKG-014` |
| REQ-014-04-04 | Low-voltage power feeders to the contactor panel package shall align with the DBM low-voltage service: 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor; where the package serves 120/208 V lighting/utility branches, those branches shall align with the DBM lighting and utility service basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage and service table |
| REQ-014-04-05 | The vendor package shall be engineered to satisfy the EPC-defined interfaces for PKG-014: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` rows for `PKG-014` |
| REQ-014-04-06 | Panel ratings, contactor counts, control logic, control voltage, lighting branch counts, exhaust fan circuit counts, and short-circuit/withstand ratings shall be confirmed by detailed vendor engineering. ASSUMPTION: detailed values are not provided by accessible source slices and shall be established from the EPC Package Datasheet load lists. | Source gap; `DELIVERABLE_REGISTER.csv` row `DEL-014-02` |
| REQ-014-04-07 | Where the contactor panels actuate motor branches (e.g., exhaust fans) supplied from a 600 V MCC, the panel control architecture shall be coordinated with the DBM local-control-station basis (H-O-A or On-Off station adjacent to each motor, hard-wired to the MCC starter circuit). Applicability per branch shall be confirmed by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power paragraph |
| REQ-014-04-08 | Vendor outputs shall include the vendor engineered physical equipment package and the vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-014-04` |
| REQ-014-04-09 | The vendor package shall be subject to EPC Integrator integration review prior to acceptance. | `DELIVERABLE_REGISTER.csv` rows `DEL-014-04`, `DEL-014-06` |
| REQ-014-04-10 | Area classification for the installed location of each contactor panel shall be determined by the EPC area classification deliverables and confirmed in vendor enclosure selection. ASSUMPTION: detailed area class per panel is `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, area classification paragraph |

## Standards

| Standard / code | Applicability | Location |
|---|---|---|
| Project electrical code (e.g., CEC where applicable to Canadian site basis) | Grounding, conductor sizing, panelboard installation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, grounding paragraphs; specific clauses TBD |
| Panelboard / motor control / contactor product standards (e.g., CSA/UL) | Vendor product certification. | location TBD; not enumerated in accessible source slices |
| Hazardous-area enclosure standards | Where contactor panel location is classified hazardous. | location TBD; depends on area classification |
| EPC Package Datasheet (`DEL-014-02`) | Functional and interface requirements normative to the vendor package. | `DELIVERABLE_REGISTER.csv` row `DEL-014-02` |
| EPC Scope of Work (`DEL-014-01`) | Scope and integration boundary normative to the vendor package. | `DELIVERABLE_REGISTER.csv` row `DEL-014-01` |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-014-04-01 | Vendor design review against package function statement. |
| REQ-014-04-02 | Traceability check from vendor design to `DEL-014-01` and `DEL-014-02` content. |
| REQ-014-04-03 | Responsibility-matrix review against `PACKAGE_REGISTER.csv` row `PKG-014`. |
| REQ-014-04-04 | Single-line and feeder review against DBM voltage and service table. |
| REQ-014-04-05 | Interface compliance review against `INTERFACE_REGISTER.csv` rows for `PKG-014`. |
| REQ-014-04-06 | Vendor data sheet and load list review against EPC Package Datasheet; factory and site acceptance tests. |
| REQ-014-04-07 | Control schematic review against DBM local-control-station basis; loop checks. |
| REQ-014-04-08 | Document deliverable list verified during vendor turnover (`DEL-014-05`). |
| REQ-014-04-09 | EPC vendor package review and acceptance (`DEL-014-06`). |
| REQ-014-04-10 | Enclosure rating review against area classification documents. |

## Documentation

- Vendor engineered physical equipment package (production hardware).
- Vendor package design basis.
- Vendor package datasheet set.
- Single-line diagram, schematic diagrams, panel layouts, bill of materials (ASSUMPTION: standard vendor engineering submittal set; exact list determined by `DEL-014-02` and `DEL-014-05`).
- Test reports (factory acceptance test, site acceptance test) — captured under `DEL-014-05`/`DEL-014-06`.
