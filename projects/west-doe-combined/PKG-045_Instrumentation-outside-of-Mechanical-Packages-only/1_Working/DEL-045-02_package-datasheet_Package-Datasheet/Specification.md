# Specification — DEL-045-02 Package Datasheet (PKG-045 Instrumentation, WBS 03)

## Scope

This specification governs the EPC Integrator's technical handoff datasheet for PKG-045, the WBS 03 Instrumentation package at the 03-25 Compressor Station and Liquids Hub. It defines what the Package Datasheet must contain so that a third-party vendor or discipline package engineer can engineer and design the in-scope instrumentation outside of mechanical packages.

In scope:
- Package identity, parent workbook anchor, discipline, responsibility.
- Source-supported equipment and design criteria for instrumentation, fire and gas detection, ESD, and BPCS/RIO interfaces at 03-25 as established by the DBM.
- Physical interface evidence for the five interface types confirmed by `INTERFACE_REGISTER.csv` PKG-045.
- Datasheet vehicle for the workbook interface facts (per Gate 6 disposition; interface facts carried here as evidence rather than as standalone deliverables — see `_CONTEXT.md` Notes).

Out of scope:
- Instrumentation that is integral to and delivered with mechanical/vendor packages (PKG-045 explicitly covers instrumentation outside of mechanical packages only).
- Construction work packaging (DEL-045-03), Scope of Work narrative (DEL-045-01), and discipline production package (DEL-045-04).

## Requirements

| # | Requirement | Source | Verification Hook |
|---|---|---|---|
| R-01 | The datasheet SHALL identify PKG-045 by its Workbook Packages row 47 anchor, WBS 03, and Workbook UID 26020-01-32-002. | `PACKAGE_REGISTER.csv` PKG-045 | Procedure step P-02 |
| R-02 | The datasheet SHALL identify the EPC Integrator as the responsible party for this handoff. | `DELIVERABLE_REGISTER.csv` DEL-045-02 | Procedure step P-02 |
| R-03 | The datasheet SHALL record that instrument air for 03-25 is supplied from 04-25 (no local 03-25 instrument-air compressor) under SCA-006. | DBM SEC-13 "Instrument Air"; SEC-13 "Instrument Air and Electrical Interface" | Procedure step P-04 |
| R-04 | The datasheet SHALL record 03-25 instrument air demand as 393 SCFM TBC and combined 03-25/04-25 demand as 1,113 SCFM TBC. | DBM SEC-13 "Instrument Air Interface" | Procedure step P-04 |
| R-05 | The datasheet SHALL state that fire, gas, and H2S detection use the MSA / General Monitors manufacturer basis; model, ratings, certifications, range, mounting, accessories: TBD detailed design. | DBM SEC-14 "Detector Manufacturer" | Procedure step P-05 |
| R-06 | The datasheet SHALL specify that detector signals associated with the BPCS are wired to the nearest Remote I/O control panel where practical. | DBM SEC-14 "LEL, H2S, Methyl Mercaptan, and Fire Detection" | Procedure step P-05 |
| R-07 | The datasheet SHALL specify that ESD pushbuttons are located outside all building exterior doors and wired to the nearest Remote I/O panel where practical. | DBM SEC-14 "Emergency Shutdown Pushbuttons" | Procedure step P-05 |
| R-08 | The datasheet SHALL state the BPCS/RIO platform as Allen-Bradley ControlLogix BPCS with Flex5000 RIO over PRP. | DBM SEC-14 ESD table | Procedure step P-05 |
| R-09 | The datasheet SHALL document visual-alarm association (red beacon for Fire/LEL/ESD) and audible-alarm tone differentiation among fire/LEL/H2S/ESD trip conditions. | DBM SEC-14 "Audible and Visual Alarms" | Procedure step P-05 |
| R-10 | The datasheet SHALL state that detector quantity, tag list, set points, voting logic, placement, and calibration are TBD pending detailed design and HAZOP/SIL. | DBM SEC-14 "LEL, H2S, Methyl Mercaptan, and Fire Detection" | Procedure step P-06 |
| R-11 | The datasheet SHALL carry the package interface facts for PKG-045: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network — each marked YES per `INTERFACE_REGISTER.csv` PKG-045. | `INTERFACE_REGISTER.csv` PKG-045; `ARTIFACT_REGISTER.csv` DEL-045-02 | Procedure step P-07 |
| R-12 | The datasheet SHALL record the -40 deg C minimum ambient as governing exposed instrumentation, panels, and field devices unless a more severe process/vendor condition applies. | DBM SEC-04 "Site Basis" | Procedure step P-04 |
| R-13 | The datasheet SHALL coordinate package-building, MCC, RIO, heat-tracing, HVAC, fire/gas-detection, and drain/vent tie-ins with civil, electrical, controls, and instrumentation sections. | DBM SEC-08 | Procedure step P-04 |
| R-14 | The datasheet SHALL state the cable-separation basis: 13.8 kV / 4,160 V / 600 V power separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. | DBM SEC-13 | Procedure step P-04 |
| R-15 | The datasheet SHALL flag service split for shared HP/Cryo and LP dual flare stack and incinerator as an open interface item until 03-25/04-25 allocation is resolved. | DBM SEC-04 (line 56) | Procedure step P-08 |
| R-16 | Vendor handoff content (battery limits, design expectations, source-supported requirements) SHALL be expressed in the datasheet and cite the source slice that supports each entry; missing values SHALL be marked TBD. | Skill four-documents source-grounding rule; `ARTIFACT_REGISTER.csv` DEL-045-02 row ART-63FDE29B88 | Procedure step P-09 |

## Standards

Standards listed by the DBM. Specific clauses are TBD until the project specification index is verified at detailed design (DBM SEC-15 "Codes and Standards"; line 888).

| Standard family | Notes | Source | Location |
|---|---|---|---|
| Project instrumentation specifications | Identified by DBM as part of facility standards; specific spec numbers TBD | DBM SEC-15 (line 894) | location TBD |
| Project electrical specifications (cable tray, conduit, grounding, bonding) | Govern cable separation and grounding | DBM SEC-13 (line 768) | location TBD |
| Control-system standards (BPCS/RIO architecture, detector and ESD requirements) | Per DBM "Codes and Standards" | DBM SEC-15 (line 894) | location TBD |
| HAZOP / SIL assessment outputs | Govern detector voting, ESD logic, cause-and-effect | DBM SEC-14 | location TBD |

## Verification

| Requirement | Verification Method | Artifact |
|---|---|---|
| R-01 to R-02 | Cross-check against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv` | Datasheet Identification table |
| R-03 to R-09, R-12 to R-14 | Source-reread against DBM SEC-04/SEC-08/SEC-13/SEC-14 | Datasheet Attributes/Conditions tables |
| R-10 | Inspect Datasheet for explicit TBD markings on detector quantity/tags/set points | Datasheet Attributes table |
| R-11 | Cross-check against `INTERFACE_REGISTER.csv` rows for PKG-045 | Datasheet Physical Interfaces table |
| R-15 | Inspect Datasheet/Guidance for open-interface flag on shared flare/incinerator | Datasheet Conditions table; Guidance Conflict Table |
| R-16 | Each non-trivial Datasheet value cites a source slice; missing values marked TBD | Datasheet References section |

## Documentation

Anticipated artifacts (per `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` DEL-045-02):

- Package technical datasheet (ART-28707828BB)
- Vendor engineering handoff basis (ART-63FDE29B88)
- Package interface requirements matrix (ART-D4E1D6D31B)
- Interface facts for Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network (ART-8ED52AB0CB, ART-D44857B017, ART-76EDC4125D, ART-69F2289654, ART-0B43FA4ACD)
- Interface note disposition record (ART-C6BB7910F9)
