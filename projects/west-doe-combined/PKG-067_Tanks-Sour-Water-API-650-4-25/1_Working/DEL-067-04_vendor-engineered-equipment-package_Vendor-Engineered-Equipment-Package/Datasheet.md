# Datasheet — DEL-067-04 Vendor Engineered Equipment Package (Tanks, Sour Water — API 650, 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-067-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-067` | `_CONTEXT.md` |
| Package Name | Tanks, Sour Water (API 650) 4-25 | `_CONTEXT.md` |
| Workbook Row | 94 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 94 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Area / LSD | 4-25 (Deepcut) | DBM-Deepcut/4-25_Deepcut_DBM.md §"Package Line-Item Requirements" (row 99) |
| Equipment Tags (in scope) | `TK-9010-1`, `TK-9020-1` | DBM-Deepcut/4-25_Deepcut_DBM.md row 99 |
| Equipment Count | 2 (PRODUCED WATER STORAGE TANK x2) | DBM-Deepcut/4-25_Deepcut_DBM.md row 99 |
| Covers Scope Items | `SOW-0225`, `SOW-0226`, `SOW-0227`, `SOW-0228` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 531 |
| Supports Objectives | `OBJ-001`, `OBJ-003`–`OBJ-010` (ASSUMPTION via PACKAGE_HEURISTIC) | `_CONTEXT.md`; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | Produced water (sour) storage | DBM §"Product Storage and Distribution Summary" (location TBD line ref) |
| Tank quantity | 2 x 2,000 bbl tanks | DBM §"Product Storage and Distribution Summary" table entry "04-25 Deep Cut Gas Plant — Produced water — 2 x 2,000 bbl tanks" |
| Tag identifiers | TK-9010-1, TK-9020-1 | DBM Package Line-Item Requirements row 99 |
| Tank construction standard | Modified API-650 atmospheric tank | DBM §"Waste Streams and Disposition — Produced Water" (table: "Tank design") |
| Test pressure | 16 oz | DBM §"Produced Water" table (Tank design row) |
| Maximum fill | 90% of tank volume; thermal expansion review required | DBM §"Produced Water" table |
| Blanket gas basis | Provided for winter vacuum prevention; API-2000 basis for rates | DBM §"Produced Water" table |
| External insulation | Yes — externally insulated and heated | DBM §"Produced Water" prose ("externally insulated, heated, internally coated with Devchem 253") |
| Internal coating | Devchem 253 on floor, walls, and roof | DBM §"Produced Water" prose |
| Hydrocarbon skim system | Kennilworth-type hydrocarbon skim float system | DBM §"Produced Water" prose |
| Relief devices | At least one PVRV per tank; EPRV sizing to be reviewed during detailed engineering | DBM §"Produced Water" prose |
| Transfer pumps (off-skid scope context) | 2 x 100% produced water transfer pumps, suction from produced water storage | DBM §"Produced Water" table |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Stored fluid | Produced water; may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans (list not comprehensive, TBC) | DBM §"Produced Water" prose |
| Produced water density | 1008 kg/m3 at 26.7 °C | DBM §"Produced Water" prose |
| Tank design specific gravity | 1.25 (TBC) | DBM §"Produced Water" prose |
| Pump design specific gravity (conservative) | 1.18 | DBM §"Produced Water" prose |
| Average accumulated flow at 04-25 | 60 m3/d continuous | DBM §"Produced Water" prose |
| Batch pump-out to 03-25 Liquids Hub | ~240 m3/d | DBM §"Produced Water" prose |
| Storage residence time (basis) | 8.9 days (380 bbl/d basis vs 2 x 2,000 bbl) | DBM §"Product Storage and Distribution Summary" table |
| Flow to storage, summer | 1,684 kg/h / 39.9 Am3/d | DBM §"Produced Water" table |
| Flow to storage, normal | TBC | DBM §"Produced Water" table |
| Flow to storage, design | TBC | DBM §"Produced Water" table |
| Truck-out connection | Common envirobox connection | DBM §"Produced Water" table |
| Vacuum truck rate assumption | 2.75 m3/min if pump-out rate unknown; to be confirmed | DBM §"Produced Water" table |
| B-train basis | 55 m3 in 20 minutes | DBM §"Produced Water" table |
| Sour-service isolation | TBD; tank isolation philosophy to be reviewed in context of potential sour vapours | DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements" |

## Construction

| Item | Value | Source |
|---|---|---|
| Code of construction | API 650 (modified) — atmospheric | DBM §"Produced Water" table |
| Sour-service classification | TBD — sour-service isolation requirements explicitly TBD | DBM §"Assumptions and Unresolved Requirements" |
| Heating | Heated tanks (heater type TBD) | DBM §"Produced Water" prose |
| Insulation | External insulation (thickness, material TBD) | DBM §"Produced Water" prose |
| Internal coating | Devchem 253 (or equal — substitution to be vendor-confirmed) on floor, walls, roof | DBM §"Produced Water" prose |
| Internals | Kennilworth-type hydrocarbon skim float system | DBM §"Produced Water" prose |
| Venting / pressure protection | PVRV(s) per tank, sized per API-2000 basis; EPRV sizing TBD | DBM §"Produced Water" prose and table |
| Nozzles / instrumentation | TBD (vendor scope) | TBD |
| Dimensions (diameter, shell height) | TBD (vendor sizing within 2,000 bbl envelope) | TBD |
| Foundation / supports | EPC Integrator interface scope | PACKAGE_REGISTER.csv row 94 (Applicable interface types: Structural / Foundations / Supports) |
| Spacing requirements | Atmospheric tank spacing per DBM §2.5; e.g., 2.35 m between atmospheric tanks (NFPA 30 Table 22.4.2.1), 80 m to public road (OGAOM 9.6.15) | DBM §"Atmospheric Tank and General Plant Spacing" |

## References

- `_CONTEXT.md` (deliverable identity, scope, references list)
- `_REFERENCES.md` (authoritative decomposition basis; shared `_Sources` root)
- `_DEPENDENCIES.md` (DECLARED mode; none declared)
- DBM-Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — primary accessible source for sour-water tank service basis
  - §"Waste Streams and Disposition — Produced Water" (table + prose)
  - §"Product Storage and Distribution Summary" (storage table)
  - §"Package Line-Item Requirements" row 99 (tag identification)
  - §2.5 "Minimum Spacing Criteria" (atmospheric tank spacing)
- GATE-07 PROJECT_DECOMP snapshot:
  - `DELIVERABLE_REGISTER.csv` row 531 (DEL-067-04 narrative)
  - `PACKAGE_REGISTER.csv` row 94 (PKG-067 package scope and interfaces)
- `_Sources/26020-Package_Requirements.docx` (package heading 22) — referenced by decomposition row; **location TBD** (binary DOCX not text-readable in this run)
- API 650 (latest applicable edition) — **location TBD** (standard text not locally cached)
- API 2000 (venting) — **location TBD**
- NFPA 30 — **location TBD**
- OGAOM (Oil and Gas Activity Operations Manual, BC) — **location TBD**
