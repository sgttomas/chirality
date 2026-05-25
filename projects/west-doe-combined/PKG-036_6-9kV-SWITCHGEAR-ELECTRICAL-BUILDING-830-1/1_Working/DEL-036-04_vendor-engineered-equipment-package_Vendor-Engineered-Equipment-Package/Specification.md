# Specification: DEL-036-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor production-unit deliverable for PKG-036 "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)": vendor engineering, vendor design, fabrication/supply, and the physical equipment package, plus the vendor design basis and datasheet set. The vendor production unit is developed against the EPC Scope of Work (`DEL-036-01`) and EPC Package Datasheet (`DEL-036-02`); EPC Integrator scope (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination) is excluded. The package is an Electrical-discipline, WBS 01, CoA 26020-01-30-027 production unit per `PACKAGE_REGISTER.csv`.

Excluded:

- EPC Scope of Work authorship (`DEL-036-01`).
- EPC Package Datasheet authorship (`DEL-036-02`).
- Construction Work Package (`DEL-036-03`).
- Vendor Document Turnover Package (`DEL-036-05`).
- EPC Vendor Package Review and Acceptance (`DEL-036-06`).

## Requirements

| ID | Requirement | Source / status |
|---|---|---|
| REQ-036-04-001 | The vendor production unit shall consist of the vendor engineered physical equipment package and the vendor package design basis and datasheet set. | `ARTIFACT_REGISTER.csv` rows `ART-5464B33F42`, `ART-4CFD465CF3` |
| REQ-036-04-002 | Vendor engineering, design, fabrication/supply, and physical-equipment scope shall be developed against the EPC Scope of Work (`DEL-036-01`) and EPC Package Datasheet (`DEL-036-02`). | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row `DEL-036-04` |
| REQ-036-04-003 | The medium-voltage service basis for facility 6.9 kV equipment is 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; vendor switchgear shall be rated for this service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2935 |
| REQ-036-04-004 | Each 6.9 kV transformer at the upstream interface to this package shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system; vendor protection coordination shall accept this grounding configuration. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2985 |
| REQ-036-04-005 | 6.9 kV medium-voltage cables connecting to the vendor switchgear shall be three-conductor copper TECK rated 8 kV with 100 percent insulation, shielded; vendor cable terminations and cable-entry provisions shall be compatible. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3008 |
| REQ-036-04-006 | The vendor prefabricated electrical building shall be modular, located in a general purpose area, elevated and installed on piles, and designed for bottom entry of incoming and outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2911, 2971-2977 |
| REQ-036-04-007 | Building HVAC shall be sized as n + 1 so that failure or maintenance of one HVAC unit does not affect building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2975 |
| REQ-036-04-008 | Major electrical equipment in the package shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall use separate copper ground conductors per CEC sizing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2987-2991 |
| REQ-036-04-009 | Where the vendor provides medium-voltage protective relays/MCC equipment, an Ethernet communication port shall be provided for connection to the plant PLC central control panel for data acquisition (DBM convention; ASSUMPTION for MV switchgear pending EPC Package Datasheet confirmation). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2955 (ASSUMPTION: extended from MCC paragraph to switchgear) |
| REQ-036-04-010 | The vendor production unit shall represent all 12 interface types listed for PKG-036 in `INTERFACE_REGISTER.csv` (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) in the vendor design basis/datasheet set as the package-side counterparts to the EPC Package Datasheet matrix. | `INTERFACE_REGISTER.csv` rows for `PKG-036`; `ARTIFACT_REGISTER.csv` row `ART-25E7F85421` (interface matrix in DEL-036-02) |
| REQ-036-04-011 | Cable tray and conduit routing within and beneath the building shall not interfere with maintenance access for vendor equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 3023-3025 |
| REQ-036-04-012 | Vendor responsibility shall be limited to package engineering, package design, vendor documentation, and the physical equipment package; facility integration responsibilities belong to the EPC Integrator. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| REQ-036-04-013 | Detailed vendor switchgear ratings (kA short-circuit, BIL, continuous bus rating, breaker frame sizes, protection settings, panel schedules) shall be defined by the EPC Package Datasheet (`DEL-036-02`) and confirmed by the vendor design basis. Where source material is silent, values remain TBD until vendor data or the EPC Package Datasheet provides them. | Source gap; `DELIVERABLE_REGISTER.csv` row `DEL-036-02`; `ARTIFACT_REGISTER.csv` row `ART-4CFD465CF3` |
| REQ-036-04-014 | The building-number-to-voltage identification for "830-1" shall be reconciled prior to vendor design freeze; see Conflict Table CT-036-04-001 in `Guidance.md`. The DBM equipment list assigns 830-1 to a 4.16 kV building and 820-1 to the 6.9 kV building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2811-2816 |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Cited explicitly for grounding-conductor sizing of distribution transformers, panelboards, and three-phase motors larger than 100 hp. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2991 |
| Project Design Basis Memorandum (Deepcut electrical section) | Governing electrical design basis for medium-voltage service, electrical-building construction, HVAC, cable entry, grounding, and cable systems. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical sections |
| Other electrical and switchgear standards (e.g., IEEE C37, ANSI C37, CSA/UL switchgear standards) | Likely applicable to vendor switchgear assemblies; relevant clauses not cited in accessible sources. | ASSUMPTION: likely applicable; location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-036-04-001 | Inspection of vendor deliverable register confirming both physical package and design basis/datasheet set are produced. |
| REQ-036-04-002 | Document review traceability matrix linking vendor outputs to EPC Scope of Work (`DEL-036-01`) and EPC Package Datasheet (`DEL-036-02`) clauses. |
| REQ-036-04-003 | Vendor design basis review and factory test records confirming 6.9 kV / 3-phase / 60 Hz / LRG rating. |
| REQ-036-04-004 | Protection coordination study review confirming compatibility with 100 A, 10 s NGR tripping. |
| REQ-036-04-005 | Cable schedule and termination drawing review against 8 kV TECK cable specification. |
| REQ-036-04-006 | Building fabrication inspection (modular, piled, bottom-entry cable provisions) at the vendor shop. |
| REQ-036-04-007 | HVAC datasheet and shop-test review confirming n + 1 redundancy. |
| REQ-036-04-008 | Grounding drawing and conductor sizing review against CEC. |
| REQ-036-04-009 | Communication architecture review and FAT confirming Ethernet integration (subject to CT-036-04-002 confirmation). |
| REQ-036-04-010 | Interface matrix cross-check between vendor design basis/datasheet set and the EPC Package Datasheet interface matrix (`ART-25E7F85421`). |
| REQ-036-04-011 | Cable-tray/conduit routing review against vendor maintenance-access drawings. |
| REQ-036-04-012 | Responsibility matrix review (vendor vs. EPC Integrator) at design review and acceptance. |
| REQ-036-04-013 | Open until EPC Package Datasheet provides ratings; verification by review when data is available. |
| REQ-036-04-014 | Human ruling on CT-036-04-001 before vendor design freeze; verification by accepted reconciliation record. |

## Documentation

- Vendor engineered physical equipment package evidence (`ART-5464B33F42`).
- Vendor package design basis and datasheet set (`ART-4CFD465CF3`).
- Vendor traceability to EPC Scope of Work (`DEL-036-01`) and EPC Package Datasheet (`DEL-036-02`).
- Vendor interface representation aligned with `INTERFACE_REGISTER.csv` rows for `PKG-036`.
- Source slices cited in this specification (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2811-2816, 2911, 2935, 2955, 2971-2977, 2985, 3008).
