# Datasheet — DEL-066-02 Package Datasheet (PKG-066 Tanks, Condensate (API 650) 4-25)

ProvenanceNote: Source-grounded where locally accessible sources support a value. The named source `26020-Package_Requirements.docx` package heading 21 is not locally accessible in readable form; package-heading-specific facts derived from that source are marked `TBD (source not accessible)`. Locally accessible sources used: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-066-02_package-datasheet | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | PKG-066 | `_CONTEXT.md` |
| PackageName | Tanks, Condensate (API 650) 4-25 | `_CONTEXT.md` (note: original token "Condendate" preserved in folder name) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Facility Locator (per package name) | 04-25 Deep Cut Gas Plant | `_CONTEXT.md` (package name token "4-25") |

## Attributes (Package Tank Inventory)

ASSUMPTION: PKG-066 package name reads "Tanks, Condensate (API 650) 4-25". The locally accessible 04-25 DBM Product Storage Summary (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 Product Storage and Distribution Summary, lines 488-498) lists at 04-25 only produced-water tanks (2 x 2,000 bbl) and slop tanks (2 x 2,000 bbl). Stabilized C5+ sour condensate from 04-25 is stored at the 03-25 Liquids Hub. The mapping between the package name "Condensate (API 650) 4-25" and the actual atmospheric tank inventory therefore needs human ruling — see Conflict Table in `Guidance.md` (CONF-066-02-01). Until then the table below carries both candidate scopes as ASSUMPTION rows.

### Candidate A — 04-25-located atmospheric tanks (per 04-25 DBM SEC-04)

| Tank Service | Quantity x Size | Storage Duration | Disposition | Source |
|---|---|---|---|---|
| Produced water (04-25) | 2 x 2,000 bbl | 8.9 days at 380 bbl/d | Pipeline to 03-25; truck-out for emergencies | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 table |
| Slop (04-25) | 2 x 2,000 bbl | 17.0 days at 200 bbl/d | Slop handling / disposal | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 table |

### Candidate B — Condensate atmospheric tanks at 03-25 Liquids Hub (associated by virtue of 04-25-origin stabilized condensate)

| Tank Service | Quantity x Size | Storage Duration | Disposition | Source |
|---|---|---|---|---|
| Sour inlet condensate storage | 2 x 3,800 bbl | ~0.6 day upset | Feeds 03-25 sour condensate treating | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling |
| Sour C5+ condensate (shared, holds 04-25 stabilized) | 6 x 3,800 bbl (functional allocation 4 sour + 2 sour-shared TBC) | 1.0 day at 7,900 bbl/d | Treatment and blending | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 table; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage |
| Product (sales) condensate | 4 x 3,800 bbl | 0.6 day at 20,000 bbl/d | NRM via LACT | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 table |
| Slop (03-25) | 1 x 3,800 bbl | 40.4 days at 80 bbl/d | Slop handling / disposal | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 table |

## Conditions (Design Service Conditions)

| Parameter | Value | Source |
|---|---|---|
| Tank type/code (analog basis) | API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section (stated for produced-water tanks; analog application to condensate tanks is ASSUMPTION) |
| Stabilizer-bottoms condensate density (15 deg C) | < 650 kg/m3 expected; blending may be required | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` C5+ Condensate section |
| Reference condensate densities (winter) | Stabilizer condensate 670.0 kg/m3; stabilizer-bottoms condensate 641.4 kg/m3 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` C5+ Condensate table |
| Spacing — between atmospheric tanks | 2.35 m (7.72 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Atmospheric Tank and General Plant Spacing — NFPA 30, Table 22.4.2.1 |
| Spacing — atm tank to property line/building (unstable liquid) | 30.5 m (100 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — NFPA 30, Table 22.4.1.5 |
| Spacing — atm tank to nearest public road | 80 m (262.5 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — OGAOM Sec. 9.6.15, DPR 48 |
| Spacing — flare to atmospheric condensate tanks | 50 m (164 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — OGAOM Sec. 9.6.15 |
| Spacing — pressurized bullets to nearest atmospheric tank | 30.48 m (100 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — API 2510 |
| Spacing — fired heater to atmospheric tanks | 25 m (82 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — OGAOM Sec. 9.6.15 |
| Site environmental loading parameters (wind, snow, seismic, temperature) | TBD (location: site-specific design parameters table in 04-25 DBM SEC-03 — not extracted in this draft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 (location TBD) |

## Construction

| Item | Value | Source |
|---|---|---|
| Governing tank code | API 650 (per package name); API-650 Modified per produced-water analog | `_CONTEXT.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section |
| External insulation and heating | Required (per produced-water analog) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section (ASSUMPTION for condensate tanks) |
| Internal coating | Devchem 253 (produced-water tanks); for condensate tanks TBD | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section |
| Tank shell, bottom, roof construction details | TBD (source not accessible: `26020-Package_Requirements.docx` package heading 21) | — |
| Foundation, anchorage, dike/containment | TBD (source not accessible) | — |
| Nozzle schedule | TBD (source not accessible) | — |
| Materials of construction (shell, internals, gaskets) | TBD (source not accessible) | — |
| Inspection/NDE basis | TBD (source not accessible) | — |
| Surface preparation/external coating | TBD (source not accessible) | — |

## Interface Requirements (Package Datasheet carries interface facts per `_CONTEXT.md` Notes)

| Interface | Counterpart | Basis | Source |
|---|---|---|---|
| 04-25 stabilized condensate export | 03-25 sour condensate storage | 1,256 m3/d, 7,900 bbl/d | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 380 |
| Produced water transfer (04-25 to 03-25) | 03-25 produced-water system | Pipeline (truck for emergency) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 |
| Vapour recovery | 04-25 SOC suction (post SCA-002) | VRU collects vapours from condensate and produced-water tank systems | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Vapour Recovery |
| Tie-in to flare/incinerator | Plant flare/incinerator headers | Distances per atmospheric tank spacing table above | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 spacing |
| Electrical, control, instrumentation tie-ins | Plant electrical/DCS/PSS | TBD (location: `26020-Package_Requirements.docx` heading 21 — not accessible) | — |
| Civil/structural tie-ins (foundations, dike) | Plant civil scope | TBD (source not accessible) | — |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — 04-25 Deep Cut Gas Plant DBM (storage, spacing, feed/product/waste basis).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — 03-25 Compressor & Liquids Hub DBM (condensate storage, produced-water tank API-650 Modified analog).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row for DEL-066-02).
- `_REFERENCES.md` for full reference registry.
- Inaccessible/deferred: `26020-Package_Requirements.docx` package heading 21 — package-specific equipment list, nozzle schedule, MOC and inspection basis (TBD).
- Inaccessible/deferred: Workbook Packages row 89 (`26020-Packages_Interfaces_4_export.xlsx`) — package-row equipment and interface entries (TBD).
