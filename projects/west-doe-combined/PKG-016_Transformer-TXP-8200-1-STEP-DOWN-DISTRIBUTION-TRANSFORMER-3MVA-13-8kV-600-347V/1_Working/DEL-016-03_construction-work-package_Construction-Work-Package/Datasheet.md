# Datasheet: DEL-016-03 — Construction Work Package (Transformer TXP-8200-1)

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-016-03_construction-work-package` |
| Deliverable Name | Construction Work Package |
| Parent Package | `PKG-016` — Transformer TXP-8200-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3 MVA, 13.8 kV / 600/347 V |
| Workbook Row | 18 |
| Discipline | Electrical |
| Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Covers Scope Item | `SOW-0017` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Source Basis | Workbook Packages row 18; `3-25_Comp_and_Liquids_DBM.md` SEC-12 Electrical |

## Attributes — Subject Equipment as Defined in Source

| Attribute | Value | Source |
|---|---|---|
| Equipment tag | TXP-8200-1 | `PACKAGE_REGISTER.csv` row 18 (package title) |
| Equipment description | Step-down distribution transformer | Package title |
| Primary voltage | 13.8 kV, 3-phase, 3-wire, 60 Hz | DBM SEC-12 "Incoming Power and Transformers" (`13.8 kV to 600V, 3 MVA transformer`) |
| Secondary voltage | 600 V, 3-phase (line-to-line); 347 V line-to-neutral implied by Wye secondary in package title | Package title; DBM SEC-12 System Voltages (600 V, 3-phase, 3-wire HRG); secondary 347 V line-to-neutral is ASSUMPTION pending vendor confirmation |
| Rated capacity | 3 MVA | DBM SEC-12 "Incoming Power and Transformers" |
| Secondary grounding | High-Resistance Grounded (HRG) with 5 A continuous resistor at facility 600 V level | DBM SEC-12 "System Voltages" — 600 V service |
| Primary system grounding | 13.8 kV LRG (Low-Resistance Grounded) from 04-25 main switchgear | DBM SEC-12 "System Voltages" |
| Source feeder | Sub-fed from 04-25 13.8 kV Main Switchgear Electrical Building | DBM SEC-12 "Incoming Power and Transformers" |
| Secondary load served | 600 V MCC for LV loads (MCC-8200 lineup) | DBM SEC-12 "Incoming Power and Transformers"; "600V MCC and Standby Power" |
| Frequency | 60 Hz | DBM SEC-12 "System Voltages" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 "Site Location" |
| Elevation | 673 m AMSL | DBM SEC-02 |
| Barometric pressure | 93.3 kPa(a) | DBM SEC-02 |
| Design minimum ambient | -40 deg C | DBM SEC-02 "Ambient Design Conditions" |
| Design maximum ambient | +35 deg C | DBM SEC-02 "Ambient Design Conditions" |
| Hazardous-area classification | General classification basis Class I Zone 2, Gas Groups IIA/IIB; final classification per drawings | DBM SEC-11 "Area Classification" |
| Indoor/outdoor location | TBD (likely indoors in MCC/electrical building — sourced statement that electrical buildings house MCCs/switchgear/distribution equipment) | DBM SEC-12 "Electrical Buildings…" |

## Construction (Physical Installation Description)

| Item | Value | Source |
|---|---|---|
| Foundation type | TBD — to be designed against final geotechnical report; equipment-specific anchorage required | DBM SEC-11 "Foundations and Structural Supports" |
| Setting/anchoring | Equipment-specific foundation/anchorage check required | DBM SEC-11 |
| Primary cable origination | 04-25 13.8 kV Main Switchgear (cross-facility feed) | DBM SEC-12 |
| Primary feeder cable | TBD (cable size, type, raceway) — to be defined in detailed electrical design | DBM SEC-12 |
| Secondary connection to MCC-8200 | Bus duct or cable to 600 V MCC lineup — TBD method | DBM SEC-12 |
| Grounding/bonding | Per project electrical specifications and detailed design | DBM SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" |
| Cable separation rule | Power circuits at 13.8 kV, 4,160 V, and 600 V separated from control/instrument circuits by distance, shielding, or routing | DBM SEC-12 |
| Heat tracing / winterization for outdoor terminations | Per facility heat-trace and winterization basis | DBM SEC-12 |
| Construction interfaces | Pile/foundation civil, structural supports, raceway/cable tray, grounding grid, building HVAC where indoor | DBM SEC-11; SEC-12 |
| Tie-ins | Primary feeder from 04-25; secondary feeder to 600 V MCC; ground grid; building services if indoor | DBM SEC-12 |

## References

- Workbook Packages row 18 (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv` rows 80 for DEL-016-03)
- DBM: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - SEC-02 Site-Specific Design Data
  - SEC-11 Civil / Foundations
  - SEC-12 Electrical
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
