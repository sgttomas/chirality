# Datasheet — Vendor Engineered Equipment Package (DEL-099-04)

> Descriptive document for the Package Vendor production unit that designs, engineers, fabricates/supplies, and delivers the physical equipment for the 03-25 Truck Product Loading Unit. Values are drawn from the locally accessible 03-25 Compressor Station and Liquids Hub Design Basis Memorandum (DBM). Items not resolvable from local sources are marked `TBD`. Inferred items are labeled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-099-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-099` |
| PackageName | Truck Product Loading Unit 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15 W6M, north of Dawson Creek, BC |
| Covers Scope Items | `SOW-0241`, `SOW-0242`, `SOW-0243`, `SOW-0244` |
| Supports Objectives (ASSUMPTION, PACKAGE_HEURISTIC) | `OBJ-002`–`OBJ-010` (best-effort mapping from `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouped) |
| Decomposition Source Row | Workbook Packages row 98; 26020-Package_Requirements.docx package heading 51 |

## Attributes

Package functional scope (from DBM `SEC-06`, source-grounded):

| Attribute | Current Basis | Source |
|---|---|---|
| Number of truck loading stations | 3 (product condensate) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (line ~40, 414, 654) |
| Loading station capacity (each) | 103 m³/h at 345 kPad differential | Same DBM, SEC-06 (line 415) |
| Condensate loading pumps | 3 pumps total, one per loading station, electric motor driven | Same DBM, SEC-06 (line 414, 526) |
| Product service | Stabilized C5+ condensate from product condensate storage | Same DBM, SEC-06 (line 376, 406, 417) |
| Upstream feed | Product condensate tanks (4 × 3,800 bbl) via loading pumps | Same DBM, SEC-06 (line 406) |
| Tank-vapour interface | Vapours from condensate / produced-water tank systems collected by VRU package (2 × 200 hp electric, 2 × 100 %) and routed (under SCA-002) to 04-25 SOC suction | Same DBM, SEC-06 "Vapour Recovery" (line 436) |
| Caustic interaction | Spent-caustic tank vents through flame arrestor to incinerator header and supports truck-out (separate caustic truck-out interface) | Same DBM, SEC-06 (line 402) |
| Produced-water truck-out interface | Vacuum truck connection assumed 2.75 m³/min per tank | Same DBM, SEC-06 (line 430) — note: scope distinct from product truck loading |
| Loading control / automation | TBD — package PLC / BPCS / ESD interfaces are stated as detailed-design items (DBM SEC-11/12 line 862) | DBM SEC-12 (line 862); resolution TBD |
| Loading arm / metering / vapour-return configuration | TBD (not specified in locally accessible DBM source slice) | TBD |
| Overfill protection (e.g., API 2350 level set) | TBD (not specified in accessible source) | TBD |
| Grounding / bonding for tanker loading | TBD; CEC and project electrical specifications govern grounding/bonding generally (DBM SEC-08, line 768, 893) | DBM SEC-08 |
| Area classification of loading apron | TBD (DBM SEC-08 cites CEC and project electrical specs but does not provide loading-area classification figure) | TBD |
| Fire / gas detection in loading area | LEL / H2S / methyl mercaptan / fire detection devices "shall be placed according to process hazards, building layouts, ventilation, equipment spacing, truck loading, tankage…" — quantity, set points, voting logic TBD | DBM SEC-12 (line 838) |
| Climate / environmental design conditions | Per 03-25 site basis (elevation 673 m AMSL, north BC); winterization detail TBD at vendor design stage | DBM SEC-02 (line 85) |
| Product chemistry hazards | Stabilized condensate with mercaptan content (non-regenerative caustic treating upstream removes mercaptan to product spec — exact spec TBD); methyl mercaptan toxicity / odour hazard relevant | DBM SEC-06 (line 389); SEC-07 (line 467) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site elevation | 673 m AMSL | DBM SEC-02 (line 85) |
| Location | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 (line 85) |
| Liquids-hub stabilized condensate throughput | 3,180 m³/d ≈ 20,000 bbl/d | DBM SEC-06 (line 376) |
| Product condensate storage allocation (upstream of loading) | 4 × 3,800 bbl product tanks (within 11-tank total) | DBM SEC-06 (line 406) |
| Loading-pump TDH / suction conditions | TBD (not given in accessible DBM slice; vendor to confirm against booster/loading hydraulic basis: booster 165 m³/h at 35 m TDH) | DBM SEC-06 (line 412) |
| Ambient / winter design temperatures | TBD (not in accessible DBM slice) | TBD |
| Seismic / wind / snow | TBD (not in accessible DBM slice) | TBD |

## Construction

| Aspect | Current Basis | Source |
|---|---|---|
| Modularization | DBM general basis treats major packages as modularized for shop assembly with field hookup; loading-station specifics TBD | DBM SEC-04 (line 294 indicates compressor packages modularized — ASSUMPTION that loading skids will likewise be vendor-modularized) |
| Materials of construction | TBD; product service is stabilized C5+ condensate with potential trace caustic/DSO/mercaptan exposure routed to separate equipment | TBD |
| Coatings / insulation | TBD for loading skid; tanks externally insulated and heated per DBM (line 421) — vendor scope confirms compatibility | DBM SEC-06 (line 421) |
| Electrical drive basis | Electric motor driven loading pumps | DBM SEC-06 (line 526) |
| Fabrication standards | TBD (specific code list not in accessible DBM slice; CEC for electrical applies generally) | TBD; DBM SEC-08 (line 893) |
| Shop QA / inspection plan | TBD — see `Procedure.md` for placeholder verification steps | TBD |

## Anticipated Artifacts

From `_CONTEXT.md`:

- Vendor-engineered physical equipment package (skids, loading stations, pumps, controls, interconnect)
- Vendor package design basis and datasheet set

These align with the vendor production unit deliverable framing in the decomposition row.

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — accessible, primary source for this deliverable's process basis.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — cited by decomposition row but **not** locally accessible as text in this run; content depending solely on this source is marked `TBD`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — cited (Workbook Packages row 98) but **not** locally accessible as text; content depending solely on this source is marked `TBD`.
- Gate 7 decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Sibling EPC anchor deliverables (consumed as inputs to vendor scope): `DEL-099-01` Scope of Work, `DEL-099-02` Package Datasheet — both currently `OPEN`; their content is not yet drafted (carried as a Conflict / TBD; see `Guidance.md`).
