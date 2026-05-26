# Datasheet — Construction Work Package (DEL-074-03)

> Production document for the Construction Work Package of PKG-074 Caustic Treating (NGL Mercaptan Removal). Descriptive identification and key construction-relevant attributes. Source-grounded; unverified or missing values are marked `TBD`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-074-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-074` |
| PackageName | Caustic Treating (NGL Mercaptan Removal) |
| Discipline | Mechanical (multi-discipline construction execution) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Facility | West Doe 04-25 Deep Cut Gas Plant (greenfield expansion) |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 (`DELIVERABLE_REGISTER.csv` row for `DEL-074-03`) |

## Attributes (Package As Object Of Construction)

| Attribute | Value | Source |
|---|---|---|
| Treating technology | Non-regenerative caustic mercaptan treating unit on cooled C3+ NGL downstream of the de-ethanizer | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Current-Scope NGL Mercaptan Treating" (line ~1509-1513) |
| Process licensor | Third-party proprietary process provider (vendor-supplied detailed engineering package); selection TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Current-Scope NGL Mercaptan Treating" (line ~1511, 1548) |
| Design throughput | 2,385 m3/d / 15,000 bbl/d treated C3+ NGL | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "NGL Mercaptan Treating Design Parameters" |
| Inlet/outlet design pressure | 2,213 kPag inlet / 1,978 kPag outlet | Same |
| Inlet temperature range | Low 26.7 °C; design 43.3 °C; high 48.8 °C | Same |
| Fresh caustic concentration | 50 wt% NaOH | Same |
| Circulating caustic concentration | 14.7 wt% NaOH (TBC) | Same |
| Storage tanks | 1 × 400 bbl fresh caustic; 1 × 400 bbl spent caustic; 1 × 400 bbl DSO; all atmospheric, heated, insulated, blanketed with LP fuel gas (fresh caustic isolated from VRU) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "NGL Mercaptan Treating Equipment and Utilities" (lines ~1562-1564) |
| Caustic outlet filters | 2 × 100 % independent vessels downstream of contactor | Same (line ~1554) |
| Building requirement | Caustic-containing equipment indoors in Mercaptan Treating Unit (MTU) building; freeze/crystallization risk | Same (line ~1552) |
| Material restriction | No aluminum permitted in MTU caustic building; insulation cladding/straps in caustic exposure areas SS; caustic tank material polymer or caustic-compatible (final selection TBD) | Same (line ~1566) |
| Safety showers | Required in MTU building; quantity/location TBD; activation must produce discrete control-room alert | Same (line ~1552) |
| Incinerator interface | Spent caustic and DSO tank vapours route to incinerator physically located at 03-25 near flare stacks; KO drum upstream | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Incinerator Interface" (line ~1570) |
| Geographic location | 04-25 lease (greenfield) with cross-facility tie to 03-25 incinerator | Same |

## Construction-Specific Attributes

| Attribute | Value | Source |
|---|---|---|
| Site climate basis | -40 °C winter design basis governs winter execution, freeze protection, and module delivery planning | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 |
| Modularization basis | TBD — decomposition does not specify modular versus stick-built construction for this package |
| Heavy-lift requirements | TBD — contactor, drain drum, and storage-tank lift weights not provided in available sources |
| Tie-in points (process) | NGL inlet from de-ethanizer outlet path; treated NGL outlet to NGL filtration / water wash / molecular sieve; rich caustic to caustic heating; spent caustic and DSO truck-out; vapours to incinerator header at 03-25 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Current-Scope NGL Mercaptan Treating" (lines ~1511-1513), § "Incinerator Interface" |
| Tie-in points (utilities) | LP fuel gas (blanket / incinerator dilution); process water (make-up); sales gas (for downstream mole-sieve regen, adjacent package); produced water drain; HP and LP electrical; instrument air; heat tracing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "NGL Mercaptan Treating Equipment and Utilities", § "Disulphide Oil, Spent Caustic, and Waste Amine" |
| Truck-loading interfaces | Fresh caustic truck-in; spent caustic truck-out; DSO truck-out | Same |
| Anticipated artifacts (per `_CONTEXT.md`) | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md` |

## Construction Sequence Anchors (ASSUMPTION — typical EPC anchors)

ASSUMPTION: The following construction sequence anchors are derived by EPC-execution convention from the equipment basis above; the source documents do not prescribe a construction sequence. Confirm against the eventual vendor package and project execution plan.

1. Site preparation and MTU building foundation work.
2. MTU building erection and weather-tight enclosure (required before caustic-equipment installation due to freeze/crystallization risk).
3. Storage-tank (fresh caustic, spent caustic, DSO) foundation, erection, blanket-gas and incinerator-vent tie-in.
4. Caustic NGL contactor, drain drum, filters, pumps installation inside MTU.
5. Piping, heat tracing and insulation, electrical, instrumentation, fire and gas.
6. Tie-in to de-ethanizer outlet, downstream water wash / mole sieve, and 03-25 incinerator header.
7. Pre-commissioning (flushing, hydrotest, NDE, loop checks), commissioning, and turnover.

## Covered Scope Items

- `SOW-0059`, `SOW-0060`, `SOW-0061`, `SOW-0062` (per `_CONTEXT.md`, traceable to decomposition `DELIVERABLE_REGISTER.csv` row 272)

## Supported Objectives

- `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — best-effort PACKAGE_HEURISTIC mapping; no deliverable-level objective list in available decomposition)

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- GATE-07 `DELIVERABLE_REGISTER.csv` row 272 (`DEL-074-03_construction-work-package`)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-07, "Current-Scope NGL Mercaptan Treating" and "Incinerator Interface"
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — site climate and 03-25 incinerator co-location context
- `_Sources/26020-Package_Requirements.docx` — Workbook Packages row 51 / package heading 28 (cited by decomposition; not directly read in this run — location TBD inside document)
