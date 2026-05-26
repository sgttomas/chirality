# Specification — DEL-065-02 Package Datasheet (PKG-065 Tanks, Caustic (API 650) 4-25)

## Scope

This specification governs the EPC Integrator's Package Datasheet for the Caustic Tanks package (PKG-065) at the West Doe Deepcut (04-25) facility. The Package Datasheet conveys the technical handoff data required for a third-party vendor or discipline package engineer to design, supply, or assemble the package.

In scope:
- Identification of equipment items in the package (fresh and spent caustic atmospheric tanks supporting the NGL non-regenerative caustic Mercaptan Treating Unit).
- Process service data, design conditions, materials, appurtenances, and interface points required for vendor / discipline engineering.
- Reference to governing codes and project basis documents.

Out of scope (covered by other PKG-065 deliverables):
- EPC Scope of Work narrative (`DEL-065-01`).
- Construction Work Package and tie-in workface plan (`DEL-065-03`).
- Vendor engineering / fabrication package and submittals (`DEL-065-04`, `DEL-065-05`).
- EPC review and acceptance evidence (`DEL-065-06`).

## Requirements

Each numbered requirement is sourced; ASSUMPTION-labelled items require human confirmation.

### R1 — Equipment Roster (FACT)

The package SHALL include, at minimum:
- 1 x 400 bbl fresh caustic storage tank — atmospheric, heated, insulated, truck-in capable, fuel-gas blanketed, NOT tied to the VRU header. (Source: DBM lines 1528, 1562.)
- 1 x 400 bbl spent caustic storage tank — atmospheric, heated, insulated, truck-out capable, fuel-gas blanketed, vented to incinerator header with flame-arrestor backflash protection. (Source: DBM lines 529-530, 1529, 1562.)

### R2 — Governing Code (PROPOSAL / ASSUMPTION)

Tank shell design SHALL conform to API 650 (atmospheric storage tanks) consistent with the package title "Tanks, Caustic (API 650) 4-25". Specific edition, addenda, and any caustic-service supplements: `location TBD` — confirm against `26020-Package_Requirements.docx` heading 20 once a text-readable extract is available.

### R3 — Materials of Construction (FACT, with detailed-engineering TBDs)

- Tank materials SHALL be polymer or other caustic-compatible materials; specific selection is a detailed-engineering TBD. (DBM line 1566.)
- Aluminum SHALL NOT be installed in the caustic building. (DBM line 1566.)
- Insulation cladding or straps in caustic exposure areas SHALL be stainless steel. (DBM line 1566.)
- MTU building floor material is a detailed-engineering TBD. (DBM line 1566.)

### R4 — Vapour-Space Management (FACT)

- Fresh caustic tank SHALL be fuel-gas blanketed and SHALL NOT be connected to the VRU header. (DBM line 1562.)
- Spent caustic tank SHALL be fuel-gas blanketed and vented to the incinerator header. (DBM line 1562.)
- Spent caustic tank SHALL include flame-arrestor backflash protection on the incinerator-header tie. (DBM line 1562.)
- Pressure/vacuum relief: PVRV provision per tank ASSUMED by analogy with DBM produced-water tank basis (DBM line 524); confirm during detailed engineering. EPRV sizing review during DE.

### R5 — Heating, Insulation, Freezing Risk (FACT)

- Tanks SHALL be heated and externally insulated to prevent caustic freezing and crystallization. (DBM lines 1552, 1562.)
- Minimum NaOH solution temperature reference: downstream caustic solution minimum 80 degF (26.7 degC). (DBM line 1338.)

### R6 — Location and Segregation (FACT)

- Caustic-containing equipment SHALL be segregated into the MTU building or an immediately adjacent area; caustic treating equipment is installed indoors due to freeze/crystallization risk. (DBM line 1552.)

### R7 — Loading / Unloading Interfaces (FACT)

- Fresh caustic tank: truck-in capable. (DBM line 1562.)
- Spent caustic tank: truck-out capable; spent caustic is trucked off-site for disposal. (DBM lines 530, 1562.)

### R8 — Plant Spacing (FACT)

Atmospheric tank spacing SHALL meet the project plant spacing basis:
- Between atmospheric tanks: 2.35 m (7.72 ft) — NFPA 30, Table 22.4.2.1. (DBM line 268.)
- Between atmospheric tanks with unstable liquids and property line / building on same property: 30.5 m (100 ft) — NFPA 30, Table 22.4.1.5. (DBM line 269.)
- Between atmospheric tanks and nearest public road: 80 m (262.5 ft) — OGAOM §9.6.15, DPR 48. (DBM line 270.)
- Between pressurized bullets and nearest atmospheric tank: 30.48 m (100 ft) — API 2510. (DBM line 265.)
- Between flare and atmospheric condensate tanks: 50 m (164 ft) — OGAOM §9.6.15. (DBM line 282; ASSUMPTION-eligible whether caustic tank is treated as a "condensate tank" or under a different OGAOM line — confirm during DE.)
- Between fired heater and atmospheric tanks: 25 m (82 ft) — OGAOM §9.6.15. (DBM line 297.)

### R9 — Safety Systems (FACT)

- The MTU building SHALL include water safety showers; quantity and location TBD; shower activation SHALL provide a discrete control-room alert. (DBM line 1552.)

### R10 — Design Specific Gravity (FACT / TBC)

- Fresh caustic tank design specific gravity: 1.75 (TBC). (DBM line 1562.)
- Spent caustic tank design specific gravity: TBD. Not stated in DBM; resolve during DE.

### R11 — Interface Matrix (TBD)

The Package Datasheet SHALL include the package interface requirements matrix (mechanical, piping, electrical, instrumentation, controls, civil/structural, safety, and process tie-ins). Authoritative source: `26020-Packages_Interfaces_4_export.xlsx`; `location TBD` — binary not locally readable. Interface rows are deferred to a downstream pass that consumes a text-readable extract.

## Standards

| Standard | Use | Locally accessible? |
|---|---|---|
| API 650 | Atmospheric tank shell design (governing per package title) | No — `location TBD` |
| NFPA 30 (Table 22.4.2.1, 22.4.1.5) | Atmospheric tank spacing | Cited via DBM only |
| API 2510 | Pressurized-bullet-to-atmospheric-tank separation | Cited via DBM only |
| OGAOM §9.6.15 (and DPR 48) | Site/spacing separation | Cited via DBM only |
| 26020-Package_Requirements.docx (heading 20) | Project package requirements — primary EPC source | No — binary, `location TBD` |
| 26020-Packages_Interfaces_4_export.xlsx | Project package interface matrix | No — binary, `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Equipment list cross-check vs DBM §MTU; vendor tag list when issued |
| R2 | Code review entry in vendor package; confirm against 26020-Package_Requirements.docx heading 20 |
| R3 | Material test reports (MTRs); vendor MoC declaration; building-walkdown for prohibited materials |
| R4 | P&ID review; flame-arrestor and PVRV datasheet entries; VRU/incinerator routing markup |
| R5 | Heat-trace / heater datasheet; insulation specification; temperature trend review at commissioning |
| R6 | Plot plan review; building general arrangement |
| R7 | Truck loading/unloading interface drawings; operations procedure review |
| R8 | Plot plan separation check; spacing matrix sign-off |
| R9 | Safety shower datasheet; DCS alarm test |
| R10 | Mechanical datasheet review (design SG field) |
| R11 | Vendor interface matrix returned and reconciled with project interface register |

## Documentation

Anticipated artifacts produced under this deliverable (from `_CONTEXT.md`):
- Package technical datasheet (this deliverable's primary artifact, with downstream vendor-facing form).
- Vendor engineering handoff basis (package datasheet + curated source extracts).
- Package interface requirements matrix (intentionally carried here per Notes: "interface facts are intentionally carried here as evidence rather than standalone deliverables").
- Source-supported equipment and design criteria summary.
