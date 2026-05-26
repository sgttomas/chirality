# Datasheet — DEL-073-02 Package Datasheet (PKG-073 Amine Treating Unit)

> Source-grounded values are cited inline using `SourcePath` + `SectionRef`.
> Inferred values are labeled `ASSUMPTION`; unresolved values are `TBD`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-073-02_package-datasheet` |
| DeliverableName | Package Datasheet |
| ParentPackageID | `PKG-073` |
| ParentWorkbookRow | 49 |
| PackageName | Amine Treating Unit (ATU) |
| EquipmentTag | `26020-01-27-001` (SourcePath: PROJECT_DECOMP `_GateSnapshots/GATE-07.../PACKAGE_REGISTER.csv` row 49) |
| Discipline | Mechanical |
| Type | EPC Package Datasheet |
| WBS | 01 |
| ResponsibleParty | EPC Integrator (datasheet owner); Package Vendor consumes for engineering |
| DecompositionRef | `_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-073-02 |

## Package Function (Attributes)

| Attribute | Value | Source |
|---|---|---|
| Process function | Removes H₂S and CO₂ from sour natural gas using a continuous MDEA absorption-regeneration cycle, operating across two modules | `PACKAGE_REGISTER.csv` row 49 |
| Module 1 | Amine Gas Sweetening — conditions sour inlet gas and contacts it with lean MDEA solvent to produce pipeline-quality sweet gas | `PACKAGE_REGISTER.csv` row 49 |
| Module 2 | Amine Regeneration — thermally regenerates rich amine, returning lean solvent | `PACKAGE_REGISTER.csv` row 49 |
| Solvent | MDEA-based, selected to permit CO₂ slip while prioritizing H₂S removal | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Amine Treating Basis" / "Amine Design Values" |
| Configuration (Module 520 — sweetening) | Inlet/TEG cross-exchanger; 2 amine inlet filter coalescers; 2 amine absorbers; 1 sweet gas scrubber (not included as separate item per design basis — see Specification); 1 TEG inlet air cooler; 1 TEG inlet filter coalescer | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Module 520 row |
| Configuration (Module 530 — regeneration) | 1 amine flash drum; rich + lean amine solids filters; 1 carbon filter; 1 lean amine cooler; 2 amine reflux pumps; 1 amine reflux accumulator; 1 amine reflux condenser; 2 lean/rich amine exchangers; 2 amine booster pumps; 1 amine reboiler; 1 amine regenerator; 1 amine surge tank; anti-foam tank + injection pump; 3 amine charge pumps; amine make-up storage; amine transfer pump; process-water storage and transfer; amine slop tank | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Module 530 row |

## Process Conditions

| Parameter | Value | Source |
|---|---|---|
| Inlet temperature (winter) | 36.8 °C (98.3 °F) | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Inlet temperature (summer) | 44.1 °C (111.3 °F) | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Hydrate margin (above hydrate temperature) | ~6 °C above expected hydrate; no methanol injection in this area | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| HC dewpoint margin | ~6 °C above expected hydrocarbon dewpoint | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Inlet H₂S basis | ~1.0 mol% H₂S at plant inlet (subject to marginal change at contactor due to blending with stabilizer overheads compressor discharge) | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Sweet gas H₂S spec | ≤4 ppmv H₂S at amine absorber outlet | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| CO₂ basis | MDEA allows CO₂ slip; sales gas CO₂ ≤2 mol%; H₂S removal prioritized | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Mercaptan recovery | 0% by design; only incidental adsorption at low H₂S loading | `4-25_Deepcut_DBM.md` "Amine Design Values" |
| Amine pressure basis | 7722 kPag (unless amended) | `4-25_Deepcut_DBM.md` "Amine Open Items and Assumptions" |
| Amine flash drum pressure | ~60 psig (~414 kPag) | `4-25_Deepcut_DBM.md` "Amine Equipment and Design Requirements" |
| Lean amine cooler outlet | 15 °F above absorber inlet temperature or 110 °F, whichever is lower | `4-25_Deepcut_DBM.md` "Amine Equipment and Design Requirements" |
| Amine reboiler heat-medium supply | 350 °F supply (hot oil); skin temperature limited <350 °F to prevent degradation | `4-25_Deepcut_DBM.md` "Amine Equipment and Design Requirements" |
| Reflux condenser overhead temperature | 110 °F (partial condenser) | `4-25_Deepcut_DBM.md` "Amine Equipment and Design Requirements" |
| Plant inlet capacity context | Combined-feed inlet basis (1 mol% H₂S, scaled trace S species) | `4-25_Deepcut_DBM.md` §"Combined feed design composition" |
| Amine flash gas flow / properties | V-5355-1 reference stream (numeric values per source); detailed flow `TBC` | `4-25_Deepcut_DBM.md` amine flash gas row |
| Acid gas water saturation | Acid gas from amine regenerator is water-saturated | `4-25_Deepcut_DBM.md` "Acid Gas" section |
| Low-pressure case CO₂/H₂S ratios (100 MMSCFD) | `TBD` | `4-25_Deepcut_DBM.md` "Amine Open Items and Assumptions" |
| Process-water user rates | `TBD` | `4-25_Deepcut_DBM.md` "Amine Open Items and Assumptions" |

## Construction (Equipment and Sparing)

| Item | Sparing / Configuration | Source |
|---|---|---|
| Amine inlet gas filter/coalescers | 2 × 100% | `4-25_Deepcut_DBM.md` "Amine Equipment and Design Requirements" |
| Amine absorbers | 2 × 50%; upflow gas contacting; top demister | same |
| Sweet gas scrubber | Not included as separate item in current design | same |
| Amine flash tank | Single drum; HC skim box; manual HC drain | same |
| Amine filtration | Full-flow rich amine particle filtration @ ~5 µm; 25% lean amine slipstream through activated carbon + 5 µm particulate; LP fuel-gas purge before opening sour filter service | same |
| Lean/rich amine exchangers | 2 × 50% plate-and-frame; multiple units required for turndown | same |
| Lean amine cooler | Air-cooled; warm-air recirculation; plenum heat | same |
| Amine surge tank | ~30 min surge at design circulation; HC skim; LP fuel-gas blanket; internal coating; heater; truck-out; secondary containment | same |
| Amine booster pumps | 2 × 115%; single-stage vertical inline; single mechanical seal | same |
| Amine charge pumps | 3 × 57.5%; multi-stage horizontal centrifugal (API-610 axial split casing currently considered; model `TBC`) | same |
| Amine regenerator | 20 actual trays (18 stripping); ≤70% jet/downcomer flood; two water-wash stages (additional stages `TBC`) | same |
| Amine reboiler | BKU kettle-style; hot oil; 350 °F supply | same |
| Amine reflux condenser + accumulator | Partial condenser to 110 °F; demister; HC skim; reflux-water purge to produced-water storage; pressure control to LP flare; dilution-gas review for high-CO₂ acid gas | same |
| Amine reflux pumps | 2 × 115%; single-stage vertical inline; single mechanical seal | same |
| Carbon filter | 1, on 25% lean amine slipstream | Module 530 row |
| Amine make-up storage | Yes (in-package) | Module 530 row |
| Anti-foam tank + injection pump | Yes (in-package) | Module 530 row |
| Process-water storage and transfer | Yes (in-package) | Module 530 row |
| Amine slop tank | Yes; receives manual HC drain and waste amine for off-site disposal/reclamation | Module 530 row; §"Disulphide Oil, Spent Caustic, and Waste Amine" |

## Package Interfaces (Required Tie-Ins to Facility)

Source: `PACKAGE_REGISTER.csv` row 49 "Applicable interface types"

- Process Piping
- Utility Piping
- Relief / Flare / Vent (acid-gas overhead route to acid-gas compressor first-stage suction scrubber; reflux accumulator pressure control to LP flare — `4-25_Deepcut_DBM.md`)
- Drain / Containment (HC drains, waste amine to slop tank, secondary containment)
- Electrical Power
- EHT (electric heat tracing / winterization)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services (Module 530 regen building)
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

## Anticipated Artifacts (delivered by/with this Datasheet)

- Package technical datasheet (this document)
- Vendor engineering handoff basis (consumed by `DEL-073-04`)
- Package interface requirements matrix (interface set above)
- Source-supported equipment and design criteria (Equipment/Conditions tables above)

## Coverage (from `_CONTEXT.md`)

- Covers scope items: `SOW-0051`, `SOW-0052`, `SOW-0053`, `SOW-0054`
- Supports objectives: `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — `PACKAGE_HEURISTIC` association at PKG-073 level)

## References

- `_REFERENCES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Amine Treating Basis"; "Amine Design Values"; "Amine Equipment and Design Requirements"; "Amine Open Items and Assumptions"; module tables; "Disulphide Oil, Spent Caustic, and Waste Amine"
- `_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 49
- `_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-073-02
- `_Sources/26020-Package_Requirements.docx` package heading 27 — location `TBD` (binary docx not locally parsed in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — location `TBD` (binary xlsx not locally parsed in this run)
