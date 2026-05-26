# Datasheet — DEL-096-02 Package Datasheet (Tanks, Sour Condensate, API 650)

> Descriptive deliverable artifact. Source-grounded where DBM text is locally accessible; values not directly stated in accessible sources are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-096-02_package-datasheet` |
| Name | Package Datasheet |
| ParentPackageID | `PKG-096` |
| PackageName | Tanks, Sour Condensate (API 650) |
| Discipline | Mechanical |
| Type | EPC Package Datasheet |
| ResponsibleParty | EPC Integrator |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub (LSD 03-25-80-15W6, north of Dawson Creek, BC) — SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SectionRef: SEC-01 |
| Service | Sour condensate atmospheric storage in the 03-25 Liquids Hub |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Tank Standard (asserted by package name) | API 650 | PackageName / `_CONTEXT.md`. ASSUMPTION: package title asserts "API 650"; DBM section 06 explicitly describes only produced-water tanks as "API-650 Modified" — see Guidance Conflict Table CT-01. |
| Tank Count (sour service) | 4 sour condensate tanks + 2 sour inlet condensate tanks | SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 406 |
| Nominal Capacity per Tank | 3,800 bbl | Same source, line 406, 410, 411 |
| Functional Allocation | 2 sour inlet condensate tanks; 4 sour condensate tanks (of the 11-tank condensate set) | Same source, line 406 |
| Sour Inlet Storage Retention | ≈ 0.6 day upset storage | Same source, line 411 |
| Tank Configuration | Atmospheric, vertical, welded steel (ASSUMPTION typical of API 650) | ASSUMPTION — exact configuration not stated for condensate tanks in accessible DBM |
| External Insulation / Heating | Externally insulated and heated (basis taken from produced-water tank text; condensate tank treatment TBC) | SourcePath: same, line 421. ASSUMPTION applied across all liquids hub tank service due to site -40 °C minimum ambient (line 145). |
| Internal Coating | TBD — Devchem 253 cited for produced-water tanks; not stated for sour condensate tanks | Same source line 421 — see CT-02 |
| Vapour Service | Vapours routed to VRU header; VRU discharge rerouted to 04-25 SOC under SCA-002 | Same source, lines 422, 434, 436 |
| Blanket Gas | LP fuel-gas blanket asserted for caustic/makeup tanks; condensate-tank blanket basis TBC | Same source, lines 358, 402 — extension to condensate tanks is ASSUMPTION |
| Minimum Design Ambient | −40 °C (governs winterization, heat tracing, tank heating) | Same source, line 145 |
| Stored Fluid | Stabilized sour C5+ condensate, post 04-25 stabilization | Same source, lines 20, 376, 380, 382 |
| Mercaptan Species in Basis | Methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, methyl ethyl sulphide | Same source, line 210 |
| Total Liquids Hub Condensate Throughput | 3,180 m³/d ≈ 20,000 bbl/d | Same source, lines 14, 376, 383 |
| Sour Receipt Source — 04-25 stabilized | 1,256 m³/d ≈ 7,900 bbl/d | Same source, line 380 |
| Sour Receipt Source — Future third-party | 1,444 m³/d ≈ 9,081 bbl/d | Same source, line 382 |

## Conditions

| Condition | Value | Source / Note |
|---|---|---|
| Design Pressure | Atmospheric (API 650 service) | ASSUMPTION — explicit design pressure not stated for condensate tanks in accessible source |
| Design Temperature (min) | −40 °C (ambient governance) | Source line 145 |
| Design Temperature (max) | TBD | Not stated in accessible DBM slices |
| Stored Fluid SG | TBD for stabilized condensate; produced-water SG basis 1.18 (pump) / 1.25 (tank design TBC) cited for water service only | Source line 421 — not transferable to sour condensate |
| H₂S Service | Sour service (sour condensate); H₂S concentration TBD from accessible slices | ASSUMPTION based on package title and DBM sour-gas context |
| Vapour Collection | All tank vapours to VRU header (atmospheric tanks) | Source line 434 |
| Methanol Disposition | Methanol may appear infrequently; downstream methanol disposition TBD | Source line 218 |
| Sour Caustic / DSO Wetting Risk | Spent caustic and DSO are produced by mercaptan treating; not stored in this package | Source line 387, 389 |

## Construction

| Item | Value | Source / Note |
|---|---|---|
| Code Basis | API 650 (per package name) | ASSUMPTION — package title; DBM uses "API-650 Modified" qualifier only for produced-water tanks (line 421) |
| Foundation Type | TBD — to be confirmed in detailed design | Source line 145 acknowledges foundation design driven by site basis |
| Roof Type | TBD (fixed roof assumed for atmospheric vapour-collected service) | ASSUMPTION |
| Materials of Construction | TBD — sour service material selection requires alignment with NACE/CSA where mandated | ASSUMPTION |
| Internal Coating | TBD — Devchem 253 is cited only for produced-water tanks; carry forward as candidate pending source confirmation | Source line 421 |
| External Insulation / Heat Tracing | Required (winterization basis) | Source line 145 |
| Aluminum Restriction | Aluminum prohibited in the caustic building; no general statement for the condensate tank package | Source line 402 |
| Earthing / Bonding | TBD | Not stated in accessible slices |
| Vents / PVRV | Vapours to VRU header; emergency relief device sizing TBD | Source line 434, design specifics TBD |
| Overflow / Containment | TBD — secondary containment per local regulation | ASSUMPTION |
| Instrumentation (level, temperature, pressure) | TBD — minimum: level, temperature, hi/lo level switches; PVRV; sample point | ASSUMPTION |
| Nozzle Schedule | TBD | Not in accessible slices |
| Tank Register Supersession | "unless superseded by final tank register" — final allocation may differ | Source line 406 |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible) — primary basis for tank counts, capacities, service, and ambient conditions.
- `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` (accessible) — trace appendix.
- Workbook Packages row 92; `26020-Package_Requirements.docx` package heading 48 — referenced in `_CONTEXT.md`; **not locally accessible as readable text** (binary .docx). Content depending solely on these sources is marked `TBD`.
- `26020-Packages_Interfaces_4_export.xlsx` — referenced; **not locally accessible as readable text** (binary .xlsx).
- API 650, "Welded Tanks for Oil Storage" — governing code per package name; **clause-level text not accessible locally** (location TBD).
