# Specification — DEL-096-02 Package Datasheet (Tanks, Sour Condensate, API 650)

> Normative deliverable. Requirements are grounded in accessible source slices; inferred or downstream-design-dependent items are explicitly labeled `ASSUMPTION` or `TBD`.

## Scope

### In Scope
- Atmospheric storage tanks in **sour condensate service** within the 03-25 Liquids Hub: 2 × 3,800 bbl sour inlet condensate tanks and 4 × 3,800 bbl sour condensate tanks (subject to final tank register). SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 406, 410, 411.
- Tank shells, bottoms, roofs, internal coating, external insulation/heat tracing, nozzles, manways, and tank-mounted instrumentation/relief devices required for atmospheric sour condensate service.
- Vapour interface to the VRU header. SourcePath: same, line 434.
- Compliance with API 650 (per package title). ASSUMPTION pending source confirmation — see Guidance CT-01.

### Out of Scope
- Product (sweet) condensate tanks, slop tank, produced-water tanks, caustic tanks, and H₂O₂ tank — addressed by separate packages.
- Booster, loading, recycle, and skim pumps (addressed elsewhere in PKG-096 or sister packages).
- LACT and custody-transfer equipment (NRM third-party scope; same source, line 417).
- 03-25 stabilization, 03-25 SOC, and 03-25 condensate dehydration (withdrawn / removed per SCA basis; same source lines 64–65, 366, 442).
- Offsite pipeline scope (by others) downstream of the facility tie-in. Same source, line 432.

## Requirements

### R-1 — Quantity and Capacity (FACT)
The package shall provide **2 × 3,800 bbl sour inlet condensate tanks** and **4 × 3,800 bbl sour condensate tanks** unless superseded by the final tank register. SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 406, 410, 411.

### R-2 — Sour Inlet Storage Retention (FACT)
The sour inlet condensate storage shall provide approximately **0.6 day upset storage**. SourcePath: same, line 411.

### R-3 — Design Code (ASSUMPTION)
Tanks shall be designed and fabricated to **API 650** (per package title). ASSUMPTION — DBM section 06 explicitly cites "API-650 Modified" only for produced-water tanks (line 421); the literal code basis for sour condensate tanks is not stated in the accessible DBM slice. See Guidance CT-01. API 650 clause-level location: **TBD** (standard not locally accessible).

### R-4 — Minimum Design Ambient (FACT)
Tanks and tank-mounted equipment shall be suitable for a minimum ambient temperature of **−40 °C**. SourcePath: same, line 145.

### R-5 — Winterization (FACT)
Tanks shall include **external insulation and heating / heat tracing** consistent with the site winterization basis. SourcePath: same, lines 145, 421 (produced-water tanks explicitly insulated/heated; extension to sour condensate tanks is ASSUMPTION but supported by site ambient basis).

### R-6 — Vapour Routing (FACT)
Tank vapours shall be collected and routed to the **VRU suction header**; the VRU discharge shall route to the 04-25 SOC suction per SCA-002. SourcePath: same, lines 434, 436.

### R-7 — Stored Fluid (FACT)
The tanks shall store **stabilized sour C5+ condensate** received from 04-25 (stabilized) and future third-party stabilized sources. Raw 03-25 condensate is not stored locally in stabilized form; it is routed to 04-25 first. SourcePath: same, lines 20, 376, 380, 382.

### R-8 — Mercaptan Compatibility (FACT)
Tank materials, internal coating, vents, and sealing shall be compatible with the design condensate basis including methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, and methyl ethyl sulphide. SourcePath: same, line 210.

### R-9 — Internal Coating (TBD)
Internal coating selection is **TBD**. Devchem 253 is the accepted basis for produced-water tanks (line 421) and is a candidate for sour condensate service pending vendor confirmation. See CT-02.

### R-10 — Aluminum Use (PARTIAL FACT)
The accessible DBM prohibits aluminum **in the caustic building** (line 402). No equivalent prohibition for the condensate tank package is stated in the accessible slice; downstream design shall confirm metallurgy restrictions for sour service. ASSUMPTION: aluminum is not appropriate in sour wet hydrocarbon service.

### R-11 — Atmospheric Service (ASSUMPTION)
Tanks are atmospheric; design pressure per API 650 limits (typically ≤ 2.5 psig vapour space) — clause-level value **TBD** from API 650 (not locally accessible). Vapour collection to VRU shall not over-pressurize the tank vapour space.

### R-12 — Tank Register Supersession (FACT)
Tank quantity and functional allocation are subject to the **final tank register** per source statement "unless superseded by final tank register". SourcePath: same, line 406.

### R-13 — Interface Boundary (FACT)
Battery limit interfaces:
- VRU suction header — tank roof vapour nozzle (downstream piping outside this package).
- Sour condensate booster pump suction header — tank outlet nozzle (pumps outside this package).
- Stabilized condensate receipt from 04-25 and future third-party — tank inlet nozzles via facility receiving piping.
SourcePath: same, lines 412, 380, 382.

### R-14 — Excluded Local Processing (FACT)
The package shall not reintroduce **local 03-25 stabilization, local 03-25 SOC, or condensate dehydration**. SourcePath: same, lines 366, 442.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650, "Welded Tanks for Oil Storage" | Tank design, fabrication, examination, testing (per package title) | **location TBD** — standard not locally accessible |
| NACE MR0175 / ISO 15156 (sour-service material selection) | Applicable — sour service per package title and DBM context | **location TBD** — standard not locally accessible. ASSUMPTION |
| CSA Z662 | Not directly applicable to atmospheric tanks; applies to pipelines | ASSUMPTION |
| Local jurisdictional requirements (BC OGC, Alberta-equivalent) | Site permit basis | **location TBD** — not in accessible slices |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1, R-2, R-12 | Drawing/register review against final tank register; design review sign-off |
| R-3, R-11 | Vendor design package review for API 650 compliance; nameplate verification |
| R-4, R-5 | Cold-weather design review; heat-tracing calc and insulation thickness check |
| R-6 | P&ID review and VRU header tie-in walk-down; pressure/vacuum interlock test |
| R-7, R-8 | Process basis confirmation in vendor datasheet; coating chemical-resistance certification |
| R-9 | Internal coating qualification report (vendor) + holiday test post-installation |
| R-10 | Material take-off (MTO) review for prohibited materials |
| R-13 | Tie-in drawing review; interface flange audit |
| R-14 | Scope-of-supply review; absence of stabilization/SOC equipment in package |

## Documentation

Anticipated documentation set (from `_CONTEXT.md` and conventional EPC handoff):
- Package technical datasheet (this deliverable's headline artifact).
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design-criteria list.
- Tank mechanical drawings (G.A., nozzle schedule, foundation interface) — vendor scope.
- Coating and insulation specifications — vendor scope.
- Inspection and test plan (ITP) per API 650 — vendor scope.
