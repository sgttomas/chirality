# Specification: DEL-018-04 — Vendor Engineered Equipment Package (PKG-018 MV VFD)

Normative requirements that the Package Vendor production unit must satisfy for the PKG-018 MV VFD package, framed against accessible source basis (DBM narratives and GATE-07 snapshot). Clause-level requirements that depend on EPC Package Datasheet detail are marked `TBD`.

## Scope

### In scope
- Vendor engineering, design, fabrication/supply, and delivery of the physical MV VFD equipment package described by PKG-018 (4160 V class, 3-phase, 60 Hz, 5000 HP class motor service) [GATE-07 `PACKAGE_REGISTER.csv` row 20].
- Vendor package design basis, vendor datasheets, internal package interface definitions, and the equipment package itself [GATE-07 `DELIVERABLE_REGISTER.csv` row 93, Anticipated Artifacts].
- Package boundary terminations for the interface types declared on PKG-018: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports [GATE-07 `PACKAGE_REGISTER.csv` row 20].
- Vendor input to EPC Integrator integration review.

### Out of scope
- Facility-level integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration are owned by the EPC Integrator [GATE-07 `PACKAGE_REGISTER.csv` row 20].
- Vendor document turnover register and turnover record assembly are produced under `DEL-018-05` (Vendor Document Turnover Package) [GATE-07 `DELIVERABLE_REGISTER.csv` row 94].
- EPC review and acceptance evidence is produced under `DEL-018-06` [GATE-07 `DELIVERABLE_REGISTER.csv` row 95].
- Construction installation/workface plan is produced under `DEL-018-03` (Construction Work Package).

## Requirements

| ID | Requirement | Basis / Source |
|---|---|---|
| R-018-04-001 | The vendor shall engineer, design, fabricate or supply, and deliver the MV VFD equipment package consistent with the EPC Scope of Work (`DEL-018-01`) and EPC Package Datasheet (`DEL-018-02`). | GATE-07 `DELIVERABLE_REGISTER.csv` row 93 (Description) |
| R-018-04-002 | The vendor-engineered package shall serve a 4160 V class, 3-phase, 60 Hz, nominally 5000 HP motor as identified by PKG-018; specific motor data point (rated hp, kW, rpm, frame, enclosure) shall be taken from the EPC Package Datasheet. | GATE-07 `PACKAGE_REGISTER.csv` row 20 (package title) |
| R-018-04-003 | The vendor shall define and document the package boundary, including terminal points for: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; and Structural / Foundations / Supports. | GATE-07 `PACKAGE_REGISTER.csv` row 20 (Interfaces) |
| R-018-04-004 | Where the vendor's package output feeds a Zone 2 motor location, the motor temperature code (T-code) drive-output limit shall be coordinated such that the motor T-code remains lower than the value specified on the area-classification drawing or fugitive-emissions study. (Vendor side: do not produce conditions that prevent the motor from meeting this requirement.) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961 |
| R-018-04-005 | The vendor shall determine harmonic and reactive-power mitigation provisions for the package as determined by detailed electrical studies; capacitor banks shall not be relied upon at the synchronous-transfer bus per SCA-001 VE #37. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| R-018-04-006 | If the package supports an inlet/sales gas compressor motor under the SCA-001 VE #34 starting-VFD basis, the package shall meet starting-VFD duty as defined in the EPC Package Datasheet. The Comp_and_Liquids DBM treats this as a starting VFD; the Deepcut DBM marks 4.16 kV starting basis as `TBD`. **CONFLICT — see Guidance.** | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088 |
| R-018-04-007 | The vendor shall provide an EtherNet communication port (or equivalent as specified by the EPC Package Datasheet) for connection to the plant PLC central control panel for data acquisition. (**ASSUMPTION** by analogy to the 4160V MCC; confirm in EPC Package Datasheet.) | **ASSUMPTION** from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2957 |
| R-018-04-008 | Where the package's load-side power cabling is low-voltage, copper TECK cable shall be used. (Applies to LV cabling fed from VFDs; MV-side cable type is not constrained by DBM and shall follow the EPC Package Datasheet.) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3013 |
| R-018-04-009 | The vendor shall produce a vendor package design basis and datasheet set sufficient for EPC Integrator integration review (separate from the vendor document turnover register produced under `DEL-018-05`). | GATE-07 `DELIVERABLE_REGISTER.csv` row 93 (Anticipated Artifacts) |
| R-018-04-010 | The vendor shall support EPC Integrator integration review and resolve integration items raised during that review prior to package acceptance under `DEL-018-06`. | GATE-07 `DELIVERABLE_REGISTER.csv` rows 93, 95 |
| R-018-04-011 | Drive cubicle / lineup environmental rating shall match the installation environment per the EPC Package Datasheet. Electrical-building installation is the default facility basis for medium-voltage VFDs. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| R-018-04-012 | Motor data (rated hp, kW, voltage, current, rpm, frame, enclosure, insulation class, temperature rise, duty, starting torque/current profile) used by the vendor for VFD sizing shall be sourced from the EPC Package Datasheet (`DEL-018-02`) and not invented from the package title. | GATE-07 `DELIVERABLE_REGISTER.csv` row 91 (Description) |

## Standards

| Reference | Use | Location |
|---|---|---|
| NEMA MG1 (motor compliance referenced for driven motors) | Informational — defines compliance basis of the driven motor that the VFD interfaces with | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533 |
| SCA-001 VE #34 (Starting VFD basis for KM-2150 / KM-2250) | Governs starting basis where applicable | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756 |
| SCA-001 VE #37 (No capacitor banks on MCC-8200 synchronous-transfer bus where VFDs are present) | Constrains reactive-power mitigation strategy | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| Applicable area-classification / fugitive-emissions study | Defines motor T-code envelope for Zone 2 VFD-fed motors | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961 |
| Vendor / industry MV VFD standards (e.g., IEEE 519, NEMA ICS 7.1, IEC 61800 series) | `location TBD` — not enumerated in accessible source slices; vendor to confirm against EPC Package Datasheet | `TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-018-04-001 | EPC Integrator review of vendor design basis and datasheets against `DEL-018-01` and `DEL-018-02` under `DEL-018-06`. |
| R-018-04-002 | Vendor datasheet review confirming motor service alignment with PKG-018 title and `DEL-018-02`. |
| R-018-04-003 | Boundary diagram and terminal-point schedule review against the six declared interface types. |
| R-018-04-004 | T-code compatibility check between vendor drive-output and motor data; cross-reference to area-classification drawing. |
| R-018-04-005 | Review of vendor harmonic/reactive study and confirmation that capacitor banks at synchronous-transfer bus are not relied upon. |
| R-018-04-006 | Conflict resolution outcome (see Guidance Conflict Table); duty-cycle witness against agreed basis. |
| R-018-04-007 | Communications port presence and protocol confirmation against EPC Package Datasheet. |
| R-018-04-008 | Cable schedule review for LV power feeders downstream of VFDs. |
| R-018-04-009 | Vendor design basis and datasheet set delivered and reviewed. |
| R-018-04-010 | Integration review action log closure prior to acceptance under `DEL-018-06`. |
| R-018-04-011 | Enclosure rating cross-check against installation environment specified in the EPC Package Datasheet. |
| R-018-04-012 | Audit of vendor sizing calculations to confirm motor data inputs trace to `DEL-018-02`. |

## Documentation

The vendor shall produce, at minimum:
- Vendor package design basis (single document or controlled set).
- Vendor datasheet set covering the VFD lineup and associated equipment (transformers, reactors, filters, HMI, controls) as designed.
- Package boundary / terminal-point schedules covering the six declared interface types.
- Vendor sizing and electrical study outputs (including harmonic / reactive-power studies per R-018-04-005).
- Integration-review responses and action-log closures supporting `DEL-018-06`.

Vendor document register, submittals, and turnover records are assembled separately under `DEL-018-05` (Vendor Document Turnover Package). [GATE-07 `DELIVERABLE_REGISTER.csv` row 94]
