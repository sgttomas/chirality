# Specification — DEL-055-02 Package Datasheet (PKG-055 LP Flare KO Drum 4-25)

## Scope

### Covers

This specification governs the EPC Integrator Package Datasheet for PKG-055, the Flare KO Drum (Low Pressure) 4-25 package (vendor package number 26020-01-17-003). It establishes the technical handoff content required by a third-party Package Vendor for engineering, design, fabrication, and supply of:

- one low-pressure flare knock-out drum (V-3900-1), and
- one LP flare KO drum transfer pump (P-3900-1),

assembled as the shop-built `390-1 LP Flare KO Drum Module`, integrated to the 04-25 Deepcut LP flare system.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-055-02; `DBM-Deepcut/4-25_Deepcut_DBM.md` LP flare and equipment-list rows.

### Excludes

- Vendor-internal engineering processes (covered by DEL-055-04).
- Construction work package content (covered by DEL-055-03).
- Vendor document turnover content (covered by DEL-055-05).
- EPC vendor package review/acceptance evidence (covered by DEL-055-06).
- PKG-082 LP Flare KO Drum 3-25 package scope.
- HP flare KO drum and cryogenic flare KO drum scope (separate facility equipment, not in this package).

Source: `DELIVERABLE_REGISTER.csv` rows DEL-055-03 through DEL-055-06; `PACKAGE_REGISTER.csv` rows PKG-082 and DBM "High-pressure flare"/"Cryogenic flare" rows.

## Requirements

### R1 — Equipment Identity (FACT)

The package datasheet shall identify the package equipment as:

- V-3900-1 — L.P Flare KO Drum (quantity 1),
- P-3900-1 — L.P Flare KO Drum Transfer Pump (quantity 1).

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` equipment-list and Word-source equipment-detail tables.

### R2 — Process Service Definition (FACT)

The datasheet shall define service as LP flare relief liquid knock-out, downstream of the 508 mm (20 in) LP relief header, upstream of the LP flare element which piggy-backs on the common HP/cryo stack.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "Low-pressure flare" and "LP stack" rows.

### R3 — Header / Material Data (FACT)

The datasheet shall record LP flare header data:

- Material: SA-106.
- Listed nominal size: 324 mm.
- Above-ground length: 270 m; below-ground length: 50 m.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "Flare Header Materials" table.

### R4 — Connected LP Flare Sources (FACT)

The datasheet shall list connected LP flare sources, including at minimum:

- amine regeneration LP flare pressure control,
- TEG flash drum LP flare blowdown,
- VRU package blowdown, VRU suction header bypass to LP flare, VRU primary seal vent,
- reciprocating compressor seal-pot vents,
- mole-sieve regeneration gas blowdown (when contaminated),
- pressurized caustic drain tank vapour (when overheads compressor is down),
- LP flare header purge gas.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` LP flare narrative paragraphs.

### R5 — Design Cases and Relief Volumes (TBD)

The datasheet shall present LP flare relief case load summary and backpressure analysis basis once Aspen Flare System Analyzer modelling is completed during detailed engineering. TBD at DBM stage.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` flare system summary row (relief volumes open).

### R6 — Pilot and Purge Gas (FACT, partial)

The datasheet shall record published source-level estimates for LP flare pilot and LP flare header purge as documented in the DBM, and shall mark pilot/purge specification values TBC for vendor confirmation.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` LP Flare Pilot and LP Flare Header Purge tables; "LP flare stack pilot and purge gas | TBC" row.

### R7 — Supplemental Fuel Gas (FACT)

The datasheet shall require supplemental fuel gas at the LP flare stack such that any blended gas mixture directed to flare has LHV ≥ 20 MJ/Sm³.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` flare narrative.

### R8 — Smokeless Operation (FACT)

The LP element shall be air-assisted (blower) for smokeless operation, with a Ringelmann 1 criterion at approximately 5% (TBC) of the emergency design case flare load.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "LP stack" row.

### R9 — Spacing and Radiation (FACT, with regulatory verification TBD)

The package shall be located consistent with site spacing criteria:

- ≥ 10 m (32 ft) between flare tanks (including KO drums) and vegetation/fire hazards (OGAOM 9.6.15).
- Stack thermal-radiation flux limits ≤ 9 kW/m² inside the blackened-area boundary and ≤ 5 kW/m² outside, per OGPFR Appendix 1, Schedule 1, Sec. 2 — values retained as DBM basis and to be verified against the governing regulation during detailed design.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` spacing table and OGPFR caveat note.

### R10 — Pump and Truck-Out (FACT)

The package shall include the LP flare KO drum transfer pump (P-3900-1) and truck-out provision for accumulated liquid.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` "Low-pressure flare" row.

### R11 — Interface Coverage (FACT)

The datasheet shall provide the package interface requirements matrix covering: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.

Source: `PACKAGE_REGISTER.csv` row 57.

### R12 — Responsibility Split (FACT)

The datasheet shall reflect the Package Vendor / EPC Integrator responsibility split: Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Source: `PACKAGE_REGISTER.csv` row 57.

### R13 — Module Boundary (FACT)

The datasheet shall identify the equipment scope as the shop-assembled `390-1 LP Flare KO Drum Module`.

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` module list.

### R14 — Vessel Mechanical Detail (TBD)

Vessel internal coating, MAWP, MDMT, corrosion allowance, internals (demister/baffle), nozzle schedule, and pump hydraulic data shall be populated on the datasheet. TBD at DBM stage — to be confirmed against `26020-Package_Requirements.docx` package heading 10 once the binary source is extracted, and from the EPC Scope of Work (DEL-055-01).

Source: location TBD inside binary `26020-Package_Requirements.docx`.

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| OGAOM, Sec. 9.6.15 | Flare and flare-tank spacing | Cited in DBM-Deepcut spacing table; regulatory text — location TBD |
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Thermal-radiation flux limits | Cited in DBM-Deepcut; regulatory text — location TBD (DBM notes verification required) |
| API 2510 | Distance between flare and pressurized bullets (site reference) | Cited in DBM spacing table — location TBD |
| 26020-Package_Requirements.docx (heading 10) | Package-specific requirements baseline | Binary; location TBD |
| 26020-Packages_Interfaces_4_export.xlsx (Packages row 57) | Package identity and interface roll-up | Binary; location TBD |
| ASME BPVC Section VIII | Pressure vessel design baseline for the KO drum | ASSUMPTION — typical for jurisdiction; not explicitly cited in DBM |
| ASME B73.1 / API 610 | Centrifugal pump design baseline | ASSUMPTION — to be confirmed by EPC SOW (DEL-055-01) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 Equipment identity | Cross-check against EPC Scope of Work (DEL-055-01) equipment list and DBM equipment table |
| R2–R4 Process service and connections | Trace to DBM LP flare narrative and to facility P&IDs (TBD) |
| R3 Header data | Direct extract from DBM "Flare Header Materials" table |
| R5 Relief volumes | Aspen Flare System Analyzer detailed-design output (TBD) |
| R6 Pilot/purge | Vendor confirmation; site Aspen model (TBD) |
| R7 Fuel gas LHV | Process calculation against blended gas composition |
| R8 Smokeless / Ringelmann | Air-assist stack design study (TBD) |
| R9 Spacing / radiation | Plot-plan compliance review against OGAOM/OGPFR |
| R10 Pump + truck-out | Datasheet review against DBM and EPC SOW |
| R11 Interface coverage | Package interface requirements matrix completeness review |
| R12 Responsibility split | Acceptance review against PACKAGE_REGISTER row 57 and EPC SOW |
| R13 Module boundary | Confirm against DBM module table |
| R14 Vessel/pump mechanical | Datasheet completeness review once `26020-Package_Requirements.docx` heading 10 is extracted |

## Documentation

The completed Package Datasheet shall include, at minimum:

- Equipment identification block (vessel and pump).
- Process conditions table (operating + design pressures/temperatures; relief case summary).
- Header and stack interface data.
- Connected source list with operating cases.
- Materials and construction summary (vessel and pump).
- Internals and nozzle schedule.
- Pump hydraulic data sheet.
- Interface requirements matrix (10 interface types per R11).
- Spacing/radiation compliance summary.
- Reference list with source paths and section refs.

Open items (TBD/ASSUMPTION) shall be enumerated; sources cited per item where known, with `location TBD` for items grounded only in binary sources at the DBM stage.
