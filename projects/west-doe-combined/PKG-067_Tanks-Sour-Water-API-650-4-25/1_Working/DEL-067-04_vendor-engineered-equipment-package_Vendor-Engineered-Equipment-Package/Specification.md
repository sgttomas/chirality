# Specification — DEL-067-04 Vendor Engineered Equipment Package (Tanks, Sour Water — API 650, 4-25)

## Scope

This specification governs the **Package Vendor production unit** for the Sour Water (Produced Water) Storage Tank package PKG-067 in the 4-25 Deepcut Gas Plant area. It covers vendor engineering, design, fabrication/supply, and the physical equipment package developed from the EPC `Scope of Work` (DEL-067-01) and `Package Datasheet` (DEL-067-02). (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 531.)

In scope:
- Two (2) produced-water storage tanks tagged `TK-9010-1` and `TK-9020-1`, each 2,000 bbl nominal, atmospheric, modified API-650 construction. (DBM Package Line-Item row 99; DBM §"Product Storage and Distribution Summary".)
- Tank shell, roof, floor, internal coating, external insulation, heating, internal hydrocarbon skim system, PVRV(s), nozzles, and ladders/platforms required to complete the tank as an engineered package. (DBM §"Produced Water" prose.)
- Vendor package design basis and datasheet set (anticipated artifact per `_CONTEXT.md`).

Out of scope (EPC Integrator):
- Foundations and supports, tie-in piping beyond package battery limits, area lighting, cathodic protection, grading and spill containment, grounding/bonding, I&C cabling and process piping integration. (PACKAGE_REGISTER.csv row 94 — "Applicable interface types".)
- Produced water pipeline to 03-25 Liquids Hub (designed and installed by others). (DBM §"Produced Water" prose.)

## Requirements

### R1 — Tank construction
- R1.1 Each tank SHALL be constructed in accordance with **API 650**, with the modifications stated in the DBM (atmospheric, 16 oz test pressure). (DBM §"Produced Water" table — "Tank design: Modified API-650 atmospheric tank; 16 oz test pressure".)
- R1.2 Maximum operating fill SHALL be limited to **90% of tank volume**, with thermal expansion review documented. (DBM §"Produced Water" table.)
- R1.3 Nominal capacity per tank: **2,000 bbl**, quantity 2. (DBM §"Product Storage and Distribution Summary".)

### R2 — Stored fluid and design conditions
- R2.1 Design specific gravity for tank sizing SHALL be **1.25** (TBC). (DBM §"Produced Water" prose.) *ASSUMPTION until confirmed.*
- R2.2 Design temperature basis: produced water 1008 kg/m³ at 26.7 °C. (DBM §"Produced Water" prose.)
- R2.3 Stored fluid composition includes potential trace H2S, mercaptans, hydrocarbons, TEG, amine, caustic, and lube oils — the list is **not comprehensive (TBC)**. (DBM §"Produced Water" prose.) Material selection SHALL accommodate this trace contaminant set; final composition envelope TBD.

### R3 — Coatings and insulation
- R3.1 Internal coating SHALL be **Devchem 253** (or vendor-proposed equivalent subject to EPC Integrator acceptance) applied to floor, walls, and roof. (DBM §"Produced Water" prose.)
- R3.2 Tanks SHALL be **externally insulated** and **heated**. Heater type, duty, and insulation thickness/material: TBD by vendor sizing.

### R4 — Internals
- R4.1 Each tank SHALL include a **Kennilworth-type hydrocarbon skim float system**. (DBM §"Produced Water" prose.)

### R5 — Pressure / vacuum protection
- R5.1 Each tank SHALL be fitted with **at least one PVRV**. (DBM §"Produced Water" prose.)
- R5.2 PVRV sizing SHALL follow **API 2000** for blanket-gas vacuum prevention. (DBM §"Produced Water" table — "Blanket gas: API-2000 basis for rates".)
- R5.3 **EPRV (emergency pressure relief vent) sizing** SHALL be reviewed and documented during detailed engineering. (DBM §"Produced Water" prose.) Currently TBD.
- R5.4 Tank isolation philosophy in the context of potential sour vapours SHALL be reviewed. (DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements" — "sour-service isolation requirements are TBD".) Currently TBD.

### R6 — Connections and operations interfaces
- R6.1 A **common envirobox truck-out connection** SHALL be provided. (DBM §"Produced Water" table.)
- R6.2 Vacuum-truck connection design SHALL accommodate **2.75 m³/min** pump-out rate assumption (TBC) and a B-train basis of **55 m³ in 20 minutes**. (DBM §"Produced Water" table.)
- R6.3 Suction nozzles for the (2 x 100%) produced water transfer pumps SHALL be provided at tank battery limit. (DBM §"Produced Water" table.) *Pumps are housed in Tank Farm Pump Building 2 (DBM row 81); pumps are not part of this vendor package.*

### R7 — Siting / spacing interface
- R7.1 Tank package design SHALL accommodate atmospheric tank spacing required by the DBM §2.5: 2.35 m between atmospheric tanks (NFPA 30 Table 22.4.2.1), 30.48 m to nearest pressurized bullet (API 2510), 80 m to nearest public road (OGAOM Sec. 9.6.15), etc. (DBM §"Atmospheric Tank and General Plant Spacing".) Final plot enforcement is EPC Integrator scope.

### R8 — Documentation
- R8.1 Vendor SHALL supply the vendor package design basis and the package datasheet set listed as anticipated artifacts. (`_CONTEXT.md` §"Anticipated Artifacts".)
- R8.2 Document submittals and the document register are delivered via the separate **DEL-067-05 Vendor Document Turnover Package**. (DELIVERABLE_REGISTER.csv row 532.) This deliverable produces the engineered equipment; turnover documentation is a sibling deliverable.

## Standards

| Standard | Use | Location |
|---|---|---|
| API 650 (modified) | Tank construction | location TBD (not locally cached) |
| API 2000 | Venting / PVRV sizing basis | location TBD |
| NFPA 30 (Table 22.4.2.1; Table 22.4.1.5) | Atmospheric tank spacing | location TBD (referenced in DBM §2.5) |
| API 2510 | Pressurized bullet spacing reference | location TBD |
| OGAOM Sec. 9.6.15, DPR 48 | BC regulatory spacing | location TBD (referenced in DBM §2.5) |

## Verification

| Req | Verification approach |
|---|---|
| R1 (API 650 construction; 16 oz test; 90% fill) | Design review of vendor calculations; witness/review hydrostatic test; fill-limit shown on datasheet |
| R2 (SG, fluid, density) | Vendor design package shows assumed SG; EPC Integrator confirms SG against the produced-water characterization (TBC item) |
| R3 (coatings, insulation, heating) | Coating MPS/QA report; insulation specification; heater duty calculation |
| R4 (Kennilworth skim) | Vendor GA/internals drawing review |
| R5 (PVRV/EPRV/isolation) | PVRV sizing calc per API 2000; EPRV sizing closed before commissioning (currently TBD); HAZOP confirmation of isolation philosophy |
| R6 (connections) | Nozzle schedule and tie-in point list reconciled to EPC piping ISOs |
| R7 (spacing) | EPC Integrator plot-plan check |
| R8 (documentation) | Cross-reference to DEL-067-05 vendor document register |

## Documentation

Anticipated artifacts produced under this deliverable (from `_CONTEXT.md`):
- Vendor engineered physical equipment package (the tanks themselves)
- Vendor package design basis and datasheet set

Companion deliverables (not produced here):
- DEL-067-01 Scope of Work (EPC Integrator)
- DEL-067-02 Package Datasheet (EPC Integrator) — input to this deliverable
- DEL-067-03 Construction Work Package (EPC Integrator)
- DEL-067-05 Vendor Document Turnover Package (Package Vendor)
- DEL-067-06 EPC Vendor Package Review and Acceptance (EPC Integrator)
