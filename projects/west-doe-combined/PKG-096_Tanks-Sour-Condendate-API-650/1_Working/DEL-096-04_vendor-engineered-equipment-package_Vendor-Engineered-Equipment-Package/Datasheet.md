# Datasheet — DEL-096-04 Vendor Engineered Equipment Package (Tanks, Sour Condensate, API 650)

> Descriptive deliverable artifact. Source-grounded where DBM text is locally accessible; values not directly stated in accessible sources are marked `TBD` or `ASSUMPTION`. This deliverable is the Package Vendor production unit, anchored by the EPC Scope of Work (DEL-096-01) and Package Datasheet (DEL-096-02).

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-096-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-096` |
| PackageName | Tanks, Sour Condensate (API 650) |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Anchoring EPC Inputs | DEL-096-01 Scope of Work; DEL-096-02 Package Datasheet |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub (LSD 03-25-80-15W6, north of Dawson Creek, BC) — SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01 |
| Service | Sour condensate atmospheric storage in the 03-25 Liquids Hub |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Vendor Deliverable Form | Engineered, designed, fabricated/supplied physical equipment package plus vendor design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Vendor Scope Anchor | EPC Scope of Work and EPC Package Datasheet | `_CONTEXT.md`; decomposition narrative ("developed from the EPC package Scope of Work and Package Datasheet") |
| Tank Count (sour service) | 2 × 3,800 bbl sour inlet condensate tanks + 4 × 3,800 bbl sour condensate tanks (subject to final tank register) | SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 406, 410, 411 |
| Tank Standard (asserted by package name) | API 650 | PackageName / `_CONTEXT.md`. ASSUMPTION: package title asserts "API 650"; DBM SEC-06 explicitly describes only produced-water tanks as "API-650 Modified" — see Guidance CT-01. |
| Stored Fluid | Stabilized sour C5+ condensate | SourcePath: same, lines 20, 376, 380, 382 |
| Sour Inlet Storage Retention | ≈ 0.6 day upset storage | Same source, line 411 |
| Mercaptan Species in Basis | Methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, methyl ethyl sulphide | Same source, line 210 |
| Vapour Service | Tank vapours to VRU header; VRU discharge routed to 04-25 SOC under SCA-002 | Same source, lines 422, 434, 436 |
| Minimum Design Ambient | −40 °C | Same source, line 145 |
| Site Class / Snow / Wind | Site Class D; Snow Ss 2.5 kPa; Wind 0.30 kPa (1-in-10) / 0.40 kPa (1-in-50); maximum wind 138 km/h TBC | Same source, SEC-02 |
| Site Elevation / Barometric | 673 m AMSL; 93.3 kPa(a) | Same source, SEC-02 |
| External Insulation / Heating | Required (winterization basis from −40 °C ambient governance); explicit cite is for produced-water tanks (line 421) — ASSUMPTION when extended to sour condensate tanks | Same source, lines 145, 421 |
| Internal Coating | TBD — Devchem 253 is the only locally-cited coating precedent (produced-water tanks, line 421); sour-condensate compatibility not stated — see CT-02 |
| Blanket Gas | LP fuel-gas blanket is the local atmospheric-tank convention (caustic/makeup tanks, lines 358, 402); extension to sour condensate tanks is ASSUMPTION |
| Aluminum Restriction | Aluminum prohibited in the caustic building (line 402); no general statement for sour condensate package — ASSUMPTION extended on conservative metallurgy grounds |
| Tank Register Supersession | "Unless superseded by final tank register" | Same source, line 406 |

## Conditions

| Condition | Value | Source / Note |
|---|---|---|
| Design Pressure | Atmospheric (API 650 service) | ASSUMPTION — explicit design pressure for condensate tanks not stated in accessible source |
| Design Temperature (min) | −40 °C (ambient governance) | Source line 145 |
| Design Temperature (max) | TBD | Not stated in accessible DBM slices |
| Stored Fluid SG / Density | TBD for stabilized sour condensate; DBM produced-water SG values (1.18 pump / 1.25 tank TBC, line 421) are **not** transferable to condensate service |
| H₂S Service | Sour service (sour condensate); H₂S concentration TBD from accessible slices | ASSUMPTION based on package title and DBM sour-gas context |
| Vapour Collection Pressure Coupling | All tank vapours to VRU suction header; tank vapour space pressure coupling to VRU header pressure | Source line 434 |
| Methanol Disposition | Methanol may appear infrequently; downstream methanol disposition TBD | Source line 218 |
| Sour Caustic / DSO Wetting Risk | Spent caustic and DSO are produced by mercaptan treating; not stored in this package | Source lines 387, 389 |

## Construction

| Item | Value | Source / Note |
|---|---|---|
| Code Basis | API 650 (per package name) | ASSUMPTION — see CT-01 |
| Vendor Engineering Scope | Process datasheet, mechanical datasheet, materials selection diagram, nozzle schedule, foundation loads, GA drawings, P&IDs (vendor scope), shop fabrication drawings, weld map, NDE/ITP plan, MTRs | ASSUMPTION — typical API 650 vendor package deliverable set; not enumerated in accessible source |
| Vendor Supply Scope | Engineered/fabricated tanks, internal coating system, externals (insulation, heat tracing, vents/PVRV, manways), nozzles, stairs/platforms/handrails, gauging/level/temperature/pressure instrumentation, grounding lugs | ASSUMPTION — typical vendor package boundary; not enumerated in accessible source |
| Foundation Type | TBD — confirm against final geotechnical report | Source SEC-02 (geotechnical preliminary) |
| Roof Type | TBD (fixed roof assumed for atmospheric vapour-collected service) | ASSUMPTION |
| Materials of Construction | TBD — sour service material selection requires alignment with NACE/CSA where mandated | ASSUMPTION |
| Internal Coating | TBD — Devchem 253 is candidate pending source confirmation | Source line 421 |
| External Insulation / Heat Tracing | Required (winterization basis) | Source line 145 |
| Earthing / Bonding | TBD | Not stated in accessible slices |
| Vents / PVRV | Vapour to VRU header; emergency relief device sizing TBD | Source line 434 |
| Overflow / Containment | TBD — secondary containment per local regulation | ASSUMPTION |
| Instrumentation (level, temperature, pressure) | TBD — minimum: level (continuous + hi/lo switches), temperature, PVRV, sample point | ASSUMPTION |
| Nozzle Schedule | TBD — to be developed by vendor against EPC Package Datasheet | ASSUMPTION |
| Surface Preparation / External Coating | TBD — typical SSPC/NACE prep + cold-climate compatible external coating | ASSUMPTION |
| Testing / Inspection | API 650 hydrostatic test, vacuum box of bottom welds, RT/UT/MT/PT per code, coating holiday test | ASSUMPTION — typical API 650 acceptance; clause-level standard text not locally accessible |
| Markings / Nameplate | API 650 nameplate, owner tag (e.g., per final tank register) | ASSUMPTION |
| Shipping / Site Erection | Vendor scope through tank erection at site, including shop assembly, field weld-up of shell courses, and tank-mounted appurtenance installation | ASSUMPTION — split between shop fabrication and field erection not stated in accessible source |
| Vendor Documentation Boundary | Vendor design basis and datasheet set issued under this deliverable; vendor document register and turnover package handled under DEL-096-05 | `_CONTEXT.md` Anticipated Artifacts; decomposition narrative |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible) — primary basis for tank counts, capacities, service, site ambient/civil conditions, and integration interfaces.
- `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` (accessible) — trace appendix.
- DEL-096-01 Scope of Work and DEL-096-02 Package Datasheet — anchoring EPC inputs (sibling deliverables; not yet ISSUED; treat as forthcoming authority for vendor scope binding).
- Workbook Packages row 92; `26020-Package_Requirements.docx` package heading 48 — referenced in `_CONTEXT.md`; **not locally accessible as readable text** (binary .docx). Content depending solely on this source is marked `TBD`.
- `26020-Packages_Interfaces_4_export.xlsx` — referenced; **not locally accessible as readable text** (binary .xlsx).
- API 650, "Welded Tanks for Oil Storage" — governing code per package name; **clause-level text not accessible locally** (location TBD).
- NACE MR0175 / ISO 15156 (sour service materials) — likely applicable; **not locally accessible** (location TBD). ASSUMPTION.
