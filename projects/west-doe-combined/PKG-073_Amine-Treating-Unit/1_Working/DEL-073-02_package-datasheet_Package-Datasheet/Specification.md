# Specification — DEL-073-02 Package Datasheet (PKG-073 Amine Treating Unit)

## Scope

This specification defines the normative requirements for the EPC Package Datasheet that the EPC Integrator issues to the Package Vendor for the PKG-073 Amine Treating Unit (ATU). It governs the technical handoff content carried in `Datasheet.md` and the interfaces required for facility integration.

### In scope
- Package identity, function, and configuration of Modules 520 (sweetening) and 530 (regeneration).
- Process design parameters at the package boundary (feed, sweet gas, acid gas, reflux, reboiler).
- Equipment list, sparing philosophy, and key construction requirements at the level needed for vendor engineering.
- Required interface set for facility integration.

### Out of scope
- Detailed vendor design, fabrication drawings, and shop-test procedures (carried by `DEL-073-04 Vendor Engineered Equipment Package`).
- Construction installation/turnover (carried by `DEL-073-03 Construction Work Package`).
- Vendor document register and turnover records (carried by `DEL-073-05`).
- Acceptance and review evidence (carried by `DEL-073-06`).

## Requirements

### R-PKG-073-02-001 — Process function
The ATU shall remove H₂S and CO₂ from sour natural gas using a continuous MDEA absorption-regeneration cycle, organized as Module 1 (Amine Gas Sweetening) and Module 2 (Amine Regeneration).
Source: `PACKAGE_REGISTER.csv` row 49.

### R-PKG-073-02-002 — Sweet gas H₂S
The amine absorber outlet sweet gas shall contain ≤4 ppmv H₂S.
Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Amine Design Values".

### R-PKG-073-02-003 — CO₂ slip / sales gas CO₂
Solvent selection (MDEA) shall permit CO₂ slip while maintaining sales gas CO₂ ≤2 mol%. H₂S removal shall take priority over CO₂ slip.
Source: same.

### R-PKG-073-02-004 — Inlet temperature operating envelope
Package shall be designed to receive sour gas at 36.8 °C (winter) and 44.1 °C (summer) at the inlet boundary.
Source: same.

### R-PKG-073-02-005 — Hydrate and HC dewpoint margins
Inlet temperature operations shall maintain approximately 6 °C margin above expected hydrate temperature and approximately 6 °C margin above expected hydrocarbon dewpoint; no methanol injection provisions are included in this area.
Source: same.

### R-PKG-073-02-006 — Pressure basis
The package design pressure basis shall be 7722 kPag unless amended.
Source: `4-25_Deepcut_DBM.md` §"Amine Open Items and Assumptions".

### R-PKG-073-02-007 — Sparing philosophy
The vendor scope shall comply with the following sparing/configuration:

| Equipment | Required configuration |
|---|---|
| Amine inlet filter/coalescers | 2 × 100% |
| Amine absorbers | 2 × 50% upflow with top demister |
| Lean/rich amine exchangers | 2 × 50% plate-and-frame |
| Amine booster pumps | 2 × 115% single-stage vertical inline, single mech seal |
| Amine charge pumps | 3 × 57.5% multi-stage horizontal centrifugal (model `TBC`) |
| Amine reflux pumps | 2 × 115% single-stage vertical inline, single mech seal |
| Amine regenerator | 20 actual trays (18 stripping); ≤70% jet/downcomer flood; two water-wash stages (additional `TBC`) |
| Amine reboiler | BKU kettle-style, hot oil, 350 °F supply, skin <350 °F |

Source: `4-25_Deepcut_DBM.md` §"Amine Equipment and Design Requirements".

### R-PKG-073-02-008 — Filtration
Rich amine shall be full-flow particle-filtered nominally at 5 µm; a 25% lean amine slipstream shall pass through activated carbon and 5 µm particulate filtration; an LP fuel-gas purge shall be provided before opening sour filter service.
Source: same.

### R-PKG-073-02-009 — Reflux accumulator pressure control
The reflux accumulator shall provide automated pressure control to the low-pressure flare and include demister, HC skim, and reflux-water purge to produced-water storage.
Source: same.

### R-PKG-073-02-010 — Acid gas overhead routing
Acid gas overheads from the amine regenerator shall be partially condensed at 110 °F, separated in the reflux accumulator, and routed to the acid-gas compressor first-stage suction scrubber.
Source: `4-25_Deepcut_DBM.md` §"Amine Treating Basis".

### R-PKG-073-02-011 — Surge tank
Amine surge tank shall provide approximately 30 minutes of surge at design circulation, with HC skim, LP fuel-gas blanket, internal coating, heater, truck-out connection, and secondary containment.
Source: same.

### R-PKG-073-02-012 — Waste amine handling
Waste/spent amine shall be drained to the amine slop tank and trucked off site for disposal/reclamation.
Source: `4-25_Deepcut_DBM.md` §"Disulphide Oil, Spent Caustic, and Waste Amine".

### R-PKG-073-02-013 — Required interfaces
The vendor package shall provide tie-in provisions for the interface types listed in `Datasheet.md` §"Package Interfaces". Detailed interface schedule values: `TBD` (to be populated from `_Sources/26020-Packages_Interfaces_4_export.xlsx`, which was not locally parsed in this run).
Source: `PACKAGE_REGISTER.csv` row 49; `_REFERENCES.md`.

### R-PKG-073-02-014 — Vendor ownership boundary
Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination.
Source: `PACKAGE_REGISTER.csv` row 49.

## Standards

| Standard | Application | Location |
|---|---|---|
| API 610 | Amine charge pumps (axial split casing currently considered; model `TBC`) | `4-25_Deepcut_DBM.md` §"Amine Equipment and Design Requirements" |
| NEMA MG 1 | Electric motors (general facility basis applies to package motors) | `4-25_Deepcut_DBM.md` (SOC/Sales compressor sections — facility-wide motor basis); ASSUMPTION applies to ATU motors pending vendor confirmation |
| Provincial / federal hazardous-area, F&G, and emissions codes | Package design and integration | `TBD` — not enumerated in accessible sources |
| 26020-Package_Requirements.docx package heading 27 | Authoritative source package requirements | location `TBD` (binary docx not parsed) |

## Verification

| Requirement | Verification approach |
|---|---|
| R-…-001 (process function) | Vendor process design review against source basis |
| R-…-002 (sweet gas H₂S ≤4 ppmv) | Vendor process simulation submittal; performance test during commissioning |
| R-…-003 (CO₂ slip, sales gas CO₂ ≤2 mol%) | Simulation submittal; sales gas composition trend at handover |
| R-…-004 / 005 (temperature, hydrate / HC dewpoint margin) | Operating envelope check sheet at inlet boundary |
| R-…-006 (pressure basis) | Equipment MAWP review per ASME (`TBD` — code citations in source `TBD`) |
| R-…-007 (sparing) | Equipment list audit against datasheet |
| R-…-008 (filtration) | Filter datasheet review; LP fuel-gas purge P&ID review |
| R-…-009 (reflux pressure control) | P&ID review; SIS review where applicable |
| R-…-010 (acid gas routing) | Interface tie-in review with acid-gas compressor PKG-046 |
| R-…-011 (surge tank) | Surge tank datasheet review; containment design review |
| R-…-012 (waste amine) | Drain system P&ID review; slop tank tag/route confirmation |
| R-…-013 (interfaces) | Interface schedule sign-off (carried in `DEL-073-06`) |
| R-…-014 (ownership boundary) | RACI review at vendor kickoff |

## Documentation (artifacts required from / supporting this datasheet)

- `Datasheet.md` (this package datasheet)
- Vendor process datasheets, equipment datasheets, P&IDs, GA drawings (consumed downstream in `DEL-073-04`/`DEL-073-05`)
- Interface requirements matrix (referenced)
- Source-supported design criteria (Conditions / Construction tables in `Datasheet.md`)
