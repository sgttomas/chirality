# Guidance — DEL-062-03 Construction Work Package (NGL Loading Pumps Building)

## Purpose

The Construction Work Package translates the EPC Scope of Work (DEL-062-01) and Package Datasheet (DEL-062-02) for PKG-062 NGL Loading Pumps Building into the execution-side basis for how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems (source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row 422). It is the EPC Integrator's Gate-5 anchor artifact on the construction side and is mandatory.

## Principles

1. **Source-grounded construction scope.** The construction work package shall reflect the package as defined by the upstream Scope of Work and Package Datasheet rather than inventing scope at the construction stage. (source: peer relationships in `DELIVERABLE_REGISTER.csv` rows 420, 421, 422)
2. **Whole-facility integration.** Installation and tie-in shall be planned so that the package becomes part of the larger facility systems — not as an isolated building (source: `_CONTEXT.md` Scope).
3. **Interface-aware execution.** Adjacent packages — notably PKG-058 NGL Booster and Transfer Pumps Building (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2548) and truck-loading facilities — are the physical neighbours whose construction sequence and tie-in points must be coordinated. (ASSUMPTION on adjacency; confirm in DEL-062-02 Package Datasheet.)
4. **Grounding discipline.** All building and equipment grounding shall tie back to the facility main ground grid; islanded grounds are not permitted (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2993; ASSUMPTION extending the published truck-loading grounding rule to building/equipment grounding for the same service envelope).
5. **Turnover discipline.** Construction turnover should be designed to feed cleanly into the vendor document turnover package (DEL-062-05) and the EPC vendor package review and acceptance (DEL-062-06) (source: `DELIVERABLE_REGISTER.csv` rows 424, 425; ASSUMPTION on flow).

## Considerations

- **Service nature.** The four pumps (P-9510-1, P-9520-1, P-9530-1, P-9540-1) are rotary-vane pumps in NGL service housed in a dedicated building (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610, line 2549). NGL is a flammable hydrocarbon stream, so construction planning shall treat the building and tie-in piping as hydrocarbon service requiring appropriate area classification, hot-work controls, and pre-commissioning cleanliness. (ASSUMPTION based on service identity; classification specifics — TBD.)
- **Building-as-equipment.** Because the equipment is housed inside a building, civil/structural work (foundation, slab, structural steel, building enclosure, HVAC, lighting, small power) is on the construction critical path before mechanical setting can complete. (ASSUMPTION based on package name "NGL Loading Pumps Building" — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2549.)
- **Vendor-package interaction.** The supplied equipment (DEL-062-04 vendor package) drives setting, alignment, piping connections, and instrumentation/control hook-ups; receipt, storage, and protection planning should anticipate vendor delivery sequencing (source: `DELIVERABLE_REGISTER.csv` row 423).
- **Objective coverage.** The deliverable supports OBJ-001 and OBJ-003 through OBJ-010 as attributed to PKG-062 (source: `OBJECTIVE_SCOPE_MAP.csv`; ASSUMPTION (PACKAGE_HEURISTIC) per `_CONTEXT.md` Supports Objectives).

## Trade-offs

- **Modular vs stick-built building.** Whether the building is delivered as a pre-engineered modular shelter or stick-built on site affects sequencing, lay-down area, and tie-in timing. (TBD — building delivery method not in locally accessible sources.)
- **Concurrent vs sequential tie-ins to PKG-058.** Performing NGL piping tie-ins concurrently with PKG-058 construction may compress schedule but introduces interface risk; sequential tie-ins are lower-risk but longer-duration. (ASSUMPTION on adjacency; trade-off framing — engineering judgment.)
- **In-shop vs field alignment of pumps.** Skid-mounted shop-aligned pumps reduce field labour; field alignment increases flexibility for piping strain compensation. (TBD — supplied pump form factor not in locally accessible sources.)

## Examples

- The DBM identifies four NGL loading pumps housed in a dedicated building (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2549, 2610). A typical construction work package for this configuration includes: civil foundation pour for the building slab and pump foundations, structural steel erection, building enclosure, four pump settings on the slab, NGL suction header tie-in from the adjacent NGL Booster and Transfer Pumps Building, NGL discharge tie-in to truck-loading service, building HVAC and electrical fit-out, grounding tie-in to the facility main ground grid, and mechanical completion walk-downs before turnover. (ASSUMPTION — drawn from the source package identity and standard EPC construction practice; not from locally accessible package-specific source text.)
