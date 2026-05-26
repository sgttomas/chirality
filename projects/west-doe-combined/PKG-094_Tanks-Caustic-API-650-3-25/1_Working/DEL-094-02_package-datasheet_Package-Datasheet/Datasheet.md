# Datasheet — Package Datasheet (PKG-094 Tanks, Caustic API 650 3-25)

> Status: INITIALIZED (Pass 1/Pass 2 draft). Substantive values cite the locally accessible
> 3-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`). The vendor RFQ
> Word source (`26020-Package_Requirements.docx` package heading 46) is referenced but not
> locally parsable in this environment; slice content from it is recorded as `location TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-094-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | PKG-094 — Tanks, Caustic (API 650) 3-25 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Number (vendor) | 26020-03-19-002 | PACKAGE_REGISTER.csv |
| Workbook Row | 86 | PACKAGE_REGISTER.csv |
| WBS | 03 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (datasheet owner); Package Vendor (package engineering/design) | PACKAGE_REGISTER.csv |
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM §Site Location (lines 85-89) |
| Governing Tank Code | API 650 | Package title (PACKAGE_REGISTER.csv); decomposition title |

## Package Function and Scope

| Field | Value | Source |
|---|---|---|
| Service | Storage of fresh and spent caustic solution supporting non-regenerative caustic mercaptan treating | DBM §Condensate Mercaptan Treating (line 389); PACKAGE_REGISTER.csv Notes |
| Equipment supplied | (1) Fresh Caustic Tank; (1) Spent Caustic Tank | PACKAGE_REGISTER.csv Notes |
| Fresh Caustic Tank function | Store and supply fresh caustic solution to the caustic treatment unit | PACKAGE_REGISTER.csv Notes |
| Spent Caustic Tank function | Receive and safely store spent caustic from the pressurized caustic drain drum | PACKAGE_REGISTER.csv Notes |
| Treating unit served | Non-regenerative caustic mercaptan treating package (Merichem or equivalent), 20,000 bbl/d C5+ condensate | DBM lines 389-395 |
| Package Vendor scope | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv |
| EPC Integrator scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | PACKAGE_REGISTER.csv |

## Tank Attributes (Fresh and Spent Caustic Tanks)

| Attribute | Value | Source |
|---|---|---|
| Quantity — Fresh Caustic | 1 | PACKAGE_REGISTER.csv Notes |
| Quantity — Spent Caustic | 1 | PACKAGE_REGISTER.csv Notes |
| Nominal capacity (each) | 400 bbl | DBM §Scope Inclusions (line 40) |
| Tank type | Atmospheric, API 650 | Package title; DBM line 402 ("atmospheric 32 oz tanks") |
| Design pressure (vapor space) | 32 oz/in² (atmospheric blanketed) | DBM line 402 |
| Blanket gas | LP fuel gas | DBM line 402 |
| Heating | Required (heated) | DBM line 402 |
| Insulation | Required (insulated) | DBM line 402 |
| Stored fluid | Caustic solution, 50 wt% NaOH/H₂O | DBM line 402 |
| Fluid specific gravity (basis) | 1.75 (TBC in source) | DBM line 402 — labeled TBC in DBM |
| Spent caustic vent path | Through flame arrestor to incinerator header; supports truck-out | DBM line 402 |
| Fresh caustic VRU connection | Not connected to VRU | DBM line 402 |

## Process Design Conditions

| Condition | Value | Source |
|---|---|---|
| Service category | Caustic storage (atmospheric, blanketed) | DBM line 402 |
| Caustic drain max temperature | 121 °C / 250 °F (TBC) | DBM §Drains (line 493) |
| Caustic drain min temperature | 80 °F | DBM line 493 |
| Caustic drain design pressure governance | Highest upstream equipment, terminating at 300# flange at spent-caustic tank | DBM line 493 |
| Heat tracing (drain) | 37.8 °C / 100 °F with redundant circuits (under consideration) | DBM line 493 |
| Ambient design conditions | Per DBM §Ambient Design Conditions | DBM §Ambient (line 94) — location TBD for specific min/max values |
| Wind / snow / seismic | Per DBM §Wind, Snow, Precipitation; §Geotechnical and Seismic | DBM §§ lines 109, 126 — location TBD for code-specific values |

## Materials and Construction

| Attribute | Value | Source |
|---|---|---|
| Tank construction code | API 650 | Package title (PACKAGE_REGISTER.csv) |
| Aluminum usage | Prohibited in caustic building | DBM line 402 |
| Tank material of construction | TBC — caustic tank material/coating details remain TBC | DBM line 402 |
| Coating / lining | TBC | DBM line 402 |
| Caustic drain piping material | Requires detailed review (embrittlement concerns) | DBM line 493 |
| Spent caustic tank outlet flange rating | 300# ANSI minimum | DBM line 493 |
| Foundations / supports | Per Structural / Foundations / Supports interface (EPC scope) | INTERFACE_REGISTER.csv IFC-94BBAEE00A |

## Nozzles and Connections (summary)

ASSUMPTION (best-effort scope): connections derived from interface applicability and DBM
service descriptions. Sizes and ratings are TBD pending vendor sizing.

| Connection | Service | Source / Note |
|---|---|---|
| Tank inlet (Fresh Caustic) | Caustic make-up loading | DBM line 389; size TBD |
| Tank outlet (Fresh Caustic) | Feed to caustic treatment unit | PACKAGE_REGISTER.csv Notes; size TBD |
| Tank inlet (Spent Caustic) | From pressurized caustic drain drum (caustic drain header, 300# ANSI min) | DBM line 493 |
| Tank outlet (Spent Caustic) | Truck-out connection | DBM line 402 |
| Vapor space — Fresh Caustic | LP fuel-gas blanket | DBM line 402 |
| Vapor space — Spent Caustic | Vent via flame arrestor to incinerator header | DBM line 402 |
| Heater / heat trace connections | Tank heating per DBM | DBM line 402; details TBD |
| Instrumentation tappings (level, temperature, pressure) | TBD per vendor design | TBD |
| Grounding / bonding | Per Grounding / Bonding interface | INTERFACE_REGISTER.csv IFC-35E994F2DE |
| Cathodic protection | Per Cathodic Protection interface | INTERFACE_REGISTER.csv IFC-7EBC5D8325 |

## Interface Summary (PKG-094 facility interfaces, all applicable)

| Interface | Applicable | Interface ID | Source |
|---|---|---|---|
| Process Piping | YES | IFC-12C92E9A0A | INTERFACE_REGISTER.csv |
| Relief / Flare / Vent | YES | IFC-AFD520D296 | INTERFACE_REGISTER.csv |
| Drain / Containment | YES | IFC-DA053E0FE2 | INTERFACE_REGISTER.csv |
| Grounding / Bonding | YES | IFC-35E994F2DE | INTERFACE_REGISTER.csv |
| Area / Exterior Lighting | YES | IFC-946F48A91C | INTERFACE_REGISTER.csv |
| Cathodic Protection | YES | IFC-7EBC5D8325 | INTERFACE_REGISTER.csv |
| I&C / Control Cabling | YES | IFC-15D9C87C0A | INTERFACE_REGISTER.csv |
| Grading / Site Drainage / Spill Containment | YES | IFC-61D7941475 | INTERFACE_REGISTER.csv |
| Structural / Foundations / Supports | YES | IFC-94BBAEE00A | INTERFACE_REGISTER.csv |

## Exclusions

- No package-specific exclusions stated in source materials (TBD; per PACKAGE_REGISTER.csv).
- Caustic regeneration is not part of the 03-25 basis (treating unit-level exclusion; DBM line 389).

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative reference index
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections: Scope Inclusions; Condensate Mercaptan Treating; Drains; Site Location)
- GATE-07 PROJECT_DECOMP snapshot: `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`
- `_Sources/26020-Package_Requirements.docx` package heading 46 — `location TBD` (binary; not parsed in this run)
