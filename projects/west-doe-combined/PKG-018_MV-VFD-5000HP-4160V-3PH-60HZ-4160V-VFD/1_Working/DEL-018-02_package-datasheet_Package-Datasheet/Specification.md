# Specification: DEL-018-02_package-datasheet

## Scope

This package datasheet specifies the technical handoff basis for `PKG-018` — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD — a vendor-owned Electrical package whose package engineering, package design, vendor documentation, and physical equipment are the responsibility of the Package Vendor, and whose facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination are the responsibility of the EPC Integrator. (Source: `PACKAGE_REGISTER.csv` row `PKG-018`; Workbook Packages row 20.)

Included:
- Medium-voltage VFD package identity and nameplate-class data carried from workbook row 20.
- Source-supported drive, motor, and MCC basis for the inlet/sales compressor application (ASSUMPTION linkage to driven load — see Guidance).
- Package interface requirements matrix evidence for all six interface facts asserted for `PKG-018`.
- Pointers to authoritative source slices for downstream vendor engineering handoff.

Excluded:
- Vendor-internal design selection (semiconductor topology, cell count, harmonic-filter configuration, internal protection coordination) — owned by Package Vendor under `DEL-018-04`.
- Construction work-package and installation/tie-in workface execution — owned by `DEL-018-03`.
- Vendor document register, submittals, and turnover records — owned by `DEL-018-05`.
- Vendor package review and acceptance evidence — owned by `DEL-018-06`.

## Requirements

| ID | Requirement | Basis | Source |
|---|---|---|---|
| REQ-018-02-01 | The package shall be identified as `PKG-018`, CoA tracking number 26020-02-30-009, WBS 02, discipline Electrical. | Identity carry-through from workbook row 20. | `PACKAGE_REGISTER.csv`; Workbook Packages row 20 |
| REQ-018-02-02 | The package shall conform to the workbook nameplate class: MV VFD, 5,000 HP, 4,160 V, 3-phase, 60 Hz, with 4,160 V VFD output. | Workbook identity. (CONFLICT vs. Comp_and_Liquids DBM source motor basis at 4,000 V / 5,200 hp; see Guidance CT-018-02-01.) | Workbook Packages row 20; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 |
| REQ-018-02-03 | If the package serves inlet/sales compressor motors KM-2150 / KM-2250, the drive shall operate as a Starting VFD with synchronous transfer to a normal-service bus after the motor reaches full speed (SCA-001 VE #34). | Source-supported drive mode for the candidate driven load. ASSUMPTION: linkage of PKG-018 to KM-2150/KM-2250 is not confirmed in workbook row 20. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 |
| REQ-018-02-04 | Power-factor-correction capacitor banks shall not be installed on the synchronous-transfer bus where this VFD is present (SCA-001 VE #37). Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | Source-stated facility constraint. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 |
| REQ-018-02-05 | The package shall present the six asserted interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-018`. | `INTERFACE_REGISTER.csv` |
| REQ-018-02-06 | Major electrical equipment shall be directly connected to the ground grid at two points. Detailed conductor sizing per CEC. | DBM grounding basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraphs |
| REQ-018-02-07 | Control and data interface shall include an Ethernet communication port to the plant PLC central control panel for data acquisition, consistent with the 4.16 kV MCC basis. | DBM MCC basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 |
| REQ-018-02-08 | Cable tray and conduit routing serving this package shall not interfere with maintenance access. | DBM routing constraint. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| REQ-018-02-09 | If any VFD-fed motor served by this package is located in a Zone 2 area, the motor shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. | DBM hazardous-area basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961 |
| REQ-018-02-10 | Low-voltage power cable fed from VFDs (where applicable to ancillary LV outputs from the package) shall be Copper TECK cable. Applicability to MV VFD output cabling is TBD. | DBM cable basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3013 |
| REQ-018-02-11 | The package shall be located, where source-supported, within a prefabricated modular electrical building capable of housing medium-voltage VFDs. Specific location assignment for `PKG-018` is TBD. | DBM electrical-buildings basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |

## Standards

| Standard / code | Applicability | Source / status |
|---|---|---|
| NEMA MG1 | Applies to the driven motor basis cited by source; applicability to the VFD package itself is `TBD` (likely applies to a vendor-supplied integrated motor where included). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324; location TBD for VFD-side clauses. |
| Canadian Electrical Code (CEC) | Governs grounding and conductor sizing for major electrical equipment per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs; location TBD. |
| SCA-001 VE #34 | Establishes Starting VFD basis for KM-2150 / KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893. |
| SCA-001 VE #37 | Removes capacitor banks from the synchronous-transfer bus where VFDs are present. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756. |
| IEEE 519 (harmonic limits) | ASSUMPTION: likely applicable to MV VFD harmonic mitigation studies; not cited in accessible source. Location `TBD`. | Inferred from REQ-018-02-04 mitigation language; not source-stated. |
| Area-classification / fugitive-emissions drawings | Govern Zone 2 temperature-code requirements for VFD-fed motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961. |

## Verification

| Requirement | Verification approach | Source / status |
|---|---|---|
| REQ-018-02-01, 02 | Document review of package nameplate, vendor proposal, and CoA tag against workbook row 20 identity. | EPC review (`DEL-018-06`). |
| REQ-018-02-03 | Witnessed factory test or simulation of synchronous-transfer sequence; field commissioning verification with KM-2150 / KM-2250 (subject to load assignment confirmation). | `DEL-018-06`. |
| REQ-018-02-04 | Design review of bus single-line; harmonic study report acceptance. | `DEL-018-06`. |
| REQ-018-02-05 | Interface requirements matrix sign-off using `INTERFACE_REGISTER.csv` rows for `PKG-018`. | This deliverable's interface matrix evidence. |
| REQ-018-02-06 | Construction inspection of two-point ground-grid connections; conductor-sizing check vs. CEC. | `DEL-018-03`, `DEL-018-06`. |
| REQ-018-02-07 | Loop check and PLC data-acquisition validation on Ethernet port. | `DEL-018-06`. |
| REQ-018-02-08 | Cable-tray and conduit routing review against maintenance-access drawings. | `DEL-018-03`. |
| REQ-018-02-09 | Area-classification review and motor nameplate temperature-code check. | `DEL-018-06`. |
| REQ-018-02-10 | Cable specification review; MV output cable spec separately confirmed (TBD). | `DEL-018-06`. |
| REQ-018-02-11 | Layout review against electrical-buildings location plan when issued. | `DEL-018-03`. |

## Documentation

Anticipated artifacts to accompany this datasheet (from `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` rows for `DEL-018-02`):

- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis (technical basis, battery limits, design expectations, source-supported requirements).
- Package interface requirements matrix (carrying the six `PKG-018` interface facts).
- Interface fact evidence: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports.
- Source-supported equipment and design criteria.

Downstream consumers:
- `DEL-018-04_vendor-engineered-equipment-package` (vendor package basis).
- `DEL-018-03_construction-work-package` (installation and tie-in).
- `DEL-018-06_epc-vendor-package-review-and-acceptance` (acceptance evidence).
