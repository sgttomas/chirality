# Datasheet — DEL-083-04 Vendor Engineered Equipment Package (Inlet Separators 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-083-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-083` |
| PackageName | Inlet Separators 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Equipment Tags | V-1600-2, V-1700-2 (two identical horizontal three-phase inlet separator packages) — Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, §Inlet Separation (line 244) |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15W6, north of Dawson Creek, BC — Source: same, lines 7, 85 |

## Attributes (per separator package)

| Parameter | Value | Source |
|---|---|---|
| Configuration | Horizontal, three-phase | DBM 3-25 §Inlet Separation (line 244) |
| Service | Sour natural gas, raw condensate, produced water | DBM 3-25 line 244 |
| Gas flow | 40 MMSCFD | DBM 3-25 table at line 248 |
| Condensate flow | 556 m3/d (3,494 bbl/d) | line 249 |
| Produced-water flow | 1,800 m3/d (11,322 bbl/d) | line 250 |
| Vessel diameter | 2,743 mm (9 ft) | line 251 |
| Straight-side length | 12,191 mm (40 ft) | line 252 |
| Pressure class | ANSI 600# | line 253 |
| Design pressure | 4,963 kPag | line 254 |
| Slug handling | ~38 m3 | line 255 |
| Internal coating | Devchem 253 | lines 256, 611 |
| Internals | Manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions | line 260 |
| Piping coating | None under current basis | line 260 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Low operating pressure | 125 psig | line 258 |
| Design operating pressure | 200 psig | line 258 |
| Maximum operating pressure | 572 psig | line 258 |
| Normal high pressure | TBC | line 258 |
| Inlet design temperature | 8.3 deg C (reconcile required per source note) | line 258 |
| Inlet separator ESDV shutdown pressure | 635 psig | line 230 |
| Inlet pressure-control valves | ≥ 2 parallel per package; balanced globe hardened trim; ΔP limit ≤ 5 psid | line 266 |
| Produced-water level-control valves | ≥ 2 parallel per package | line 266 |
| Methanol drain expectation | Drain at inlet separator boot; downstream disposition TBD | line 218 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Quantity | Two identical packages, each 50% of facility capacity | DBM 3-25 line 244, line 570 |
| Capacity philosophy | 2 x 50 percent, no spare (older 2 x 100% language requires reconciliation) | line 570 |
| Housing | Instrumentation and one end of each package enclosed in heated self-framing building; building extent TBD | line 260 |
| Building reference | Package buildings for inlet separators listed under known buildings/interfaces | line 706 |
| Pressure-vessel design | Per applicable pressure class, sour-service requirements, corrosion allowance, coating, manway access, internals removal, drainage, venting, inspection | line 611 |
| Vendor-supplied artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (decomposition basis and source roots)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Inlet Separation section, Pressure Vessel section, Equipment Sparing table, Buildings list
- Decomposition: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-083-04
- `_Sources/26020-Package_Requirements.docx` package heading 36 — **location TBD** (binary file; not extracted in this run)

## Open Items

- `TBD` — Pig receiver size (DBM line 230)
- `TBD` — Delivery-point ESDV shutdown pressure (line 240)
- `TBD` — Heated building extent for separator packages (line 260)
- `TBD` — Methanol downstream disposition (line 218)
- `CONFLICT` — Sparing language `2 x 50%` vs older `2 x 100%` (line 570); reconciliation required by detailed design
