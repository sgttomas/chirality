# Datasheet — DEL-053-04 Vendor Engineered Equipment Package (Flare KO Drum, Cryo)

> Descriptive datasheet for the vendor-produced package. Vendor-specific equipment datasheet values (dimensions, MAWP, MDMT, weights, electrical loads, nozzle schedule) are TBD pending vendor engineering output and EPC Package Datasheet (DEL-053-02) handoff.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-053-04_vendor-engineered-equipment-package | _CONTEXT.md |
| Name | Vendor Engineered Equipment Package | _CONTEXT.md |
| Parent Package | PKG-053 — Flare KO Drum (Cryo) | _CONTEXT.md; PACKAGE_REGISTER.csv row 53 |
| Discipline | Mechanical | _CONTEXT.md; PACKAGE_REGISTER.csv row 53 |
| Type | Vendor Package Production Unit | _CONTEXT.md |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | _CONTEXT.md |
| Package Tag | 26020-01-PT-17-001 — Flare KO Drum (Cryo) | PACKAGE_REGISTER.csv row 53 |
| WBS | 01 | PACKAGE_REGISTER.csv row 53 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Supply the cryogenic flare knock-out drum and associated electric immersion heater as a single equipment package. | SCOPE_LEDGER.csv SOW-0068; PACKAGE_REGISTER.csv row 53 |
| Major included equipment | Cryogenic flare KO drum V-4110-1; electric immersion heater H-4112-1 | SCOPE_LEDGER.csv SOW-0069; DBM-Deepcut/4-25_Deepcut_DBM.md package equipment list rows 11-12 |
| Process service | Cryogenic-unit reliefs and molecular-sieve-dehydrated systems with PSVs relieving below -45.5 degC | SCOPE_LEDGER.csv SOW-0070; DBM-Deepcut/4-25_Deepcut_DBM.md "Cryogenic flare" row |
| Service sourness classification (brief) | Non-sour service (per project brief) | SCOPE_LEDGER.csv SOW-0070 |
| Relief header connection | 610 mm (24 in) cryogenic relief header into V-4110-1; header combines with HP flare downstream of both KO drums before HP/cryo stack | DBM-Deepcut/4-25_Deepcut_DBM.md "Cryogenic flare" row (Flare Equipment and Routing table) |
| Cryogenic flare header material | 304SS, 610 mm | DBM-Deepcut/4-25_Deepcut_DBM.md flare header table |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Minimum design metal temperature basis | < -45.5 degC (PSVs in cryogenic service relieve below this threshold) | DBM-Deepcut/4-25_Deepcut_DBM.md "Cryogenic flare" row |
| Drum design pressure | TBD | location TBD (vendor scope; not in accessible sources) |
| Drum operating pressure | TBD | location TBD |
| Drum design temperature (max / min) | TBD | location TBD |
| Drum dimensions (diameter, T/T length) | TBD | location TBD |
| Drum orientation | TBD | location TBD |
| Liquid hold-up / disengagement basis | TBD | location TBD |
| Immersion heater duty (kW) | TBD | location TBD |
| Immersion heater electrical service (V, phase, Hz) | TBD | location TBD |
| Heater control / temperature setpoint | TBD | location TBD |
| Corrosion allowance | TBD | location TBD |
| Insulation system | Cryogenic flare headers outside buildings are NOT heat traced (water not expected); drum insulation specification TBD | DBM-Deepcut/4-25_Deepcut_DBM.md flare section (header heat-trace policy) |

## Construction

| Item | Value | Source |
|---|---|---|
| Materials of construction | TBD (consistent with cryogenic service and connecting 304SS header per DBM); ASSUMPTION: low-temperature-suitable austenitic stainless or LTCS alloy with vendor selection | DBM-Deepcut header MOC; vendor scope |
| Pressure code | TBD; ASSUMPTION: ASME BPVC Section VIII Div. 1 with CRN where required | ASSUMPTION (industry convention; not in accessible sources) |
| Nozzle schedule | TBD | vendor scope |
| Internals (mist eliminator, vortex breaker, baffles) | TBD | vendor scope |
| Heater configuration (sheath, watt density, thermowell) | TBD | vendor scope |
| Skid / structural arrangement | TBD; package boundary terminates at vendor-supplied interface points TBD | vendor scope |
| Surface preparation and coating | TBD | vendor scope |
| Nameplate / tagging | V-4110-1 (drum); H-4112-1 (heater) | DBM-Deepcut equipment list |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- GATE-07 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` (row 53, PKG-053)
  - `DELIVERABLE_REGISTER.csv` (row DEL-053-04)
  - `SCOPE_LEDGER.csv` (SOW-0067, SOW-0068, SOW-0069, SOW-0070)
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Flare Equipment and Routing; Flare Header and Backpressure Basis; package equipment list rows 11-12)
- 26020-Package_Requirements.docx package heading 8 — referenced by SCOPE_LEDGER; **location TBD** (binary .docx not directly accessible to this run)
